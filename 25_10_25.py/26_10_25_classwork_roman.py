def roman_to_int(s):
    # Mapping of Roman numerals to integer values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # --- Constraint 1: Length Check ---
    if not (1 <= len(s) <= 15):
        return " Error: Roman numeral length must be between 1 and 15 characters."

    # --- Constraint 2: Valid Character Check ---
    for ch in s:
        if ch not in roman_values:
            return f" Error: Invalid character '{ch}' found. Use only I, V, X, L, C, D, M."

    # --- Constraint 3: No invalid repetitions ---
    invalid_repeats = ["IIII", "VV", "XXXX", "LL", "CCCC", "DD", "MMMM"]
    for pattern in invalid_repeats:
        if pattern in s:
            return f" Error: Invalid Roman numeral pattern '{pattern}'."

    total = 0
    i = 0

    # --- Conversion Logic ---
    while i < len(s):
        if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
            total += roman_values[s[i + 1]] - roman_values[s[i]]
            i += 2
        else:
            total += roman_values[s[i]]
            i += 1

    # --- Constraint 4: Valid Range [1, 3999] ---
    if not (1 <= total <= 3999):
        return f" Error: Result {total} is out of valid Roman numeral range [1–3999]."

    return total


# --- Example Tests ---
user_input=input("enter roman number ").upper()
print(roman_to_int(user_input))
