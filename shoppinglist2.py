my_list=['cheese','bunnies','shoes']

def add_shopping_list(item):
	if item in my_list:
		print 'item already exists'
	else:
		my_list.append (item)
		my_list.sort()
		# my_list.islower()

	  	return my_list



def return_shopping_list():
	my_list.sort()
	return my_list



def remove_item(item):
	if item not in my_list:
		print "not in list"
	elif item in my_list:
		my_list.remove(item)
  		my_list.sort 




def main():

	adding=raw_input("please add an item to my list")
	print add_shopping_list (adding)
	removing=raw_input("Please remove an item from my list")
	print remove_item(removing)
	print return_shopping_list()




if __name__ == '__main__':
	main()






