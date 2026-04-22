def test_metrics_logic():
    db = [{"store_id": "STORE_BLR_002", "visitor_id": "VIS_1"}]

    visitors = set(e["visitor_id"] for e in db)
    assert len(visitors) == 1