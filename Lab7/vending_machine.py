import re


def parse_coins(coins_csv):
    """Parse comma-separated integers without crashing on invalid input."""
    if not isinstance(coins_csv, str):
        return []

    if not coins_csv.strip():
        return []

    try:
        return [int(part.strip()) for part in coins_csv.split(",")]
    except ValueError:
        return []


def slot_position(code):
    """Convert a slot code such as B7 into zero-based coordinates."""
    if not isinstance(code, str):
        return None

    if not re.fullmatch(r"[A-Za-z][0-9]+", code):
        return None

    row = ord(code[0].upper()) - ord("A")

    try:
        column = int(code[1:]) - 1
    except ValueError:
        return None

    if column < 0:
        return None

    return row, column


def change_due(payment):
    """Calculate change in five-coin units for valid payment input."""
    if not isinstance(payment, str):
        return None

    if not re.fullmatch(r"[0-9]+/[0-9]+", payment):
        return None

    try:
        paid_text, price_text = payment.split("/")
        paid = int(paid_text)
        price = int(price_text)
    except ValueError:
        return None

    if paid < price:
        return None

    change = paid - price

    if change % 5 != 0:
        return None

    return str(change // 5) + " five-coins"


def main():
    print("==== Running parse_coins ====")
    user_input = input("Enter coin values as CSV (e.g. 5,10,25): ")
    result = parse_coins(user_input)
    print("Coins:", result)

    print("\n==== Running slot_position ====")
    user_input = input("Enter a slot code (e.g. B7): ")
    result = slot_position(user_input)
    print("Row and Column:", result)

    print("\n==== Running change_due ====")
    user_input = input("Enter paid/price (e.g. 200/150): ")
    result = change_due(user_input)
    print("Change Due:", result)


if __name__ == "__main__":
    main()
