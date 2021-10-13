'''               WELCOME YOUR STEAKHOUSE                         ''' 




bill = float(input(" The Amount of your bilss is $"))
tax = .10 
tip = float(input("Thank You, What's percentage of gratuity will you be leaving today? "))
total_tip_amount = tip/100
num_of_people = float(input("Thank you, How many people are you splitting your bill with?"))




tax_amount = bill * tax
total_tip_amount= tip + bill
your_total = tax_amount + total_tip_amount 
splitting_your_bill = your_total / num_of_people

print(f'Your Bill was ${your_total}')
print(f'If you split your bill each person needs to pay ${splitting_your_bill}')