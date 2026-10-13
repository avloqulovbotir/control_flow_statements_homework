def main(t):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if t < 0:
        return "Freezing"
    if 1 <= t <= 10:
        return "Very Cold"
    if 11 <= t <= 20:
        return "Cold"
    if 21 <= t <= 30:
        return "Normal"
    if 31 <= t <= 40:
        return "Hot"
    if t > 40:
        return "Very Hot"