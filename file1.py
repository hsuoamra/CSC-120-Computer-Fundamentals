import random
def create_list():

  my_list = []
  MAX_LEN = 50
  for i in range(MAX_LEN):
    my_list.append(random.randint(1,99))
  sorted_list = sorted(my_list)
  min_num = sorted_list[0]
  #print(my_list)
  #print(sorted_list)
  print("The minimum number in the list is: ", min_num)
  #return my_list
#Calling the function
create_list()
