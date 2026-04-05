def match_transactions():
    from .models import Transaction

    transactions = list(Transaction.objects.all())

    matched = []
    unmatched = []

    for t in transactions:
        if t.amount > 1000:
            matched.append(t)
        else:
            unmatched.append(t)

    return matched, unmatched