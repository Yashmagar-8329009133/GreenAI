def predict_sustainability(data):
    """
    Simple ML model logic for demonstration.
    Calculates a sustainability score based on inputs.
    """
    energy = data.get("energy", 0)
    water = data.get("water", 0)
    co2 = data.get("co2", 0)
    renewable = data.get("renewable", 0)
    waste = data.get("waste", 0)

    # Simple scoring logic (0-100)
    score = max(0, min(100,
        50 + (renewable - co2/10 + waste/2 - energy/100 - water/1000)
    ))
    return round(score, 2)
