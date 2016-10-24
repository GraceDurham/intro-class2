tip_amount = 18.0
total_bill = 118.0
split_amount = 118.0

def calculate_bill(original_bill_amount,tip_percentage = 18, split_number = 1):
	global tip_amount
	global total_bill
	global split_amount
	total_bill= tip_amount + original_bill_amount
	print total_bill
	split_amount= original_bill_amount/split_number
	return split_amount




print calculate_bill(100,split_number=2)







