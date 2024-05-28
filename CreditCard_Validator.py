 def validate_credit_card(c_number):
     c_number = c_number.replace(" ", "")

     if not c_number.isdigit() or len(c_number) != 16:
        return "not valid"

     c_number = [int(char) for char in c_number]
     c_number.reverse()

     for i in range(1, len(c_number), 2):
        c_number[i] *= 2

     for i in range(len(c_number)):
        if c_number[i] > 9:
            c_number[i] -= 9

     sum_c = sum(c_number)

     if sum_c % 10 == 0:
        return "valid"
     else:
        return "not valid"

c_input = input("Enter credit card number: ")
print(validate_credit_card(c_input))
