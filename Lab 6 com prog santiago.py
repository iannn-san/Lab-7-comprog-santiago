def calculate_fee(age, is_member):
    if age < 18:
        if is_member:
            fee = 450.00
        else:
            fee = 650.00
    elif 18 <= age <= 65:
        if is_member:
            fee = 550.00
        else:
            fee = 750.00
    else:   # age > 65
        if is_member:
            fee = 400.00
        else:
            fee = 600.00
    return fee

# usage bossing
age = int(input("Enter your age: "))
is_member = input("Are you a member? (yes/no): ").lower() == 'yes'

fee = calculate_fee(age, is_member)
print(f"The registration fee is: {fee} pesos")