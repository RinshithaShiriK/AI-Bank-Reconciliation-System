import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import Transaction
from .utils import match_transactions


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['file']

            try:
                # ✅ Handle both CSV and Excel
                if file.name.endswith('.csv'):
                    df = pd.read_csv(file)

                elif file.name.endswith('.xlsx'):
                    df = pd.read_excel(file, engine='openpyxl')

                else:
                    return HttpResponse("❌ Unsupported file format")

                # ✅ Clear old data
                Transaction.objects.all().delete()

                # ✅ Process each row
                for _, row in df.iterrows():

                    debit = row.get('Debit', 0)
                    credit = row.get('Credit', 0)

                    amount = 0
                    txn_type = ''

                    # Handle NaN safely
                    if pd.notna(debit) and debit != 0:
                        amount = float(debit)
                        txn_type = 'debit'

                    elif pd.notna(credit) and credit != 0:
                        amount = float(credit)
                        txn_type = 'credit'

                    Transaction.objects.create(
                        date=row.get('Date'),
                        amount=amount,
                        type=txn_type,
                        description=row.get('Description', ''),
                        source='bank'
                    )

                # ✅ Redirect after success
                return redirect('/dashboard/')

            except Exception as e:
                return HttpResponse(f"❌ Error: {str(e)}")

    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})


def dashboard(request):
    matched, unmatched = match_transactions()

    return render(request, 'dashboard.html', {
        'matched': matched,
        'unmatched': unmatched
    })