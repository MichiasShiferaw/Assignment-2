def vote():
    """ ()-> (float)
    Precondition: all values within the string are either abstained, yes or no"""
    input_string = input('Enter the yes, no, abstained votes one by one and then press enter: ')
    input_string1 = vote_percentage(input_string)
    if input_string1 == 1.0: # if the amount of yes's are equal to 1
       return print('Proposal passes, unanimously')
    elif 1 > input_string1 >= float(2/3): # if the amount of yes's are either between 1 and 2/3
        return print('Proposal passes with super majority')
    elif float(2/3) > input_string1 >= float(1/2): # if the amount of yes's are between 2/3 and 1/2
        return print('Proposal passes with simple majority')
