def classify_glucose(value, unit="mg/dL"):
    try:
        v = float(value)
    except (TypeError, ValueError):
        return "invalid"
    if v != v or v <= 0:   # NaN, zero, negative
        return "invalid"
    if unit == "mmol/L":
        v = v * 18.0
    elif unit != "mg/dL":
        return "invalid"
    if v < 70 or v > 300:
        return "urgent"
    return "normal"