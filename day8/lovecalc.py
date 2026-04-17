def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    # TRUE count
    true_total = (
        combined_names.count('t') +
        combined_names.count('r') +
        combined_names.count('u') +
        combined_names.count('e')
    )

    # LOVE count
    love_total = (
        combined_names.count('l') +
        combined_names.count('o') +
        combined_names.count('v') +
        combined_names.count('e')
    )

    # Combine into a 2-digit number
    love_score = int(str(true_total) + str(love_total))

    print(love_score)


# Example
calculate_love_score("moynak sinha",  "moynak sinha")