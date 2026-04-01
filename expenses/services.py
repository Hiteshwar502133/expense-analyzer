def detect_category(description):
    desc = description.lower()

    if any(word in desc for word in ["pizza", "food", "burger"]):
        return "Food"
    elif any(word in desc for word in ["uber", "petrol", "fuel"]):
        return "Transport"
    elif any(word in desc for word in ["movie", "netflix", "game"]):
        return "Entertainment"
    elif any(word in desc for word in ["wisky", "whiskey", "beer", "alcohol"]):
        return "Lifestyle"
    else:
        return "Other"