def get_metrics(db, store_id):
    visitors = set()

    for e in db:
        if e["store_id"] == store_id:
            visitors.add(e["visitor_id"])

    return {
        "store_id": store_id,
        "visitors": len(visitors)
    }