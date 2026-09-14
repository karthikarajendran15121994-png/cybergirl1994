import re

def check_password_strength(password: str) -> str:
    # Criteria checks
    length_ok = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[@#$%!]', password))

    criteria_met = sum([length_ok, has_upper, has_lower, has_digit, has_special])

    # Classify strength
    if criteria_met == 5:
        return "Strong 💪"
    elif criteria_met >= 3:
        return "Medium 🙂"
    else:
        return "Weak ❌"


def main():
    print("=== Password Strength Checker 🔐 ===")
    password = input("Enter a password to check: ")

    if not password:
        print("No password entered!")
        return

    strength = check_password_strength(password)

    print(f"\nPassword: {'*' * len(password)}")
    print(f"Length: {'✅' if len(password) >= 8 else '❌'} (min 8, got {len(password)})")
    print(f"Uppercase (A-Z): {'✅' if re.search(r'[A-Z]', password) else '❌'}")
    print(f"Lowercase (a-z): {'✅' if re.search(r'[a-z]', password) else '❌'}")
    print(f"Numbers (0-9):   {'✅' if re.search(r'[0-9]', password) else '❌'}")
    print(f"Special (@#$%!): {'✅' if re.search(r'[@#$%!]', password) else '❌'}")
    print(f"\nStrength: {strength}")


if __name__ == "__main__":
    main()