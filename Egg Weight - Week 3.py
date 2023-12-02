# Landon Weitenbeck | Assingment 3 (Egg Weight) | Week 11/6 - 11/12
#Asks the user for the weight of their eggs and outputs infomation about the group of eggs.

egg_count = 0
egg_list=[]
#Fixed Variables
LARGEST_EGG = 16 #Fixed largest egg weight the program takes(16 oz is the largest egg ever laid)
MIN_JUMBO = 2.5 #Fixed minimum mass of an egg classified as Jumbo
MIN_XL = 2.25 #Fixed minimum mass of an egg classified as XL
MIN_LARGE = 2 #Fixed minimum mass of an egg classified as Large
MIN_MEDIUM = 1.75 #Fixed minimum mass of an egg classified as Medium
MIN_SMALL = 1.5 #Fixed minimum mass of an egg classified as Small

#Asks the user for the weight of eggs and stores it within a list to use for later
egg_weight = float(input('Enter the egg weight in oz. (0 to quit): '))
while egg_weight != 0:
    egg_count += 1
    #Checks to see if the weight entered is vaild
    while egg_weight > LARGEST_EGG or egg_weight < MIN_SMALL:
        print(egg_weight, 'is out of range')
        egg_weight = float(input('Enter the egg weight in oz. (0 to quit): '))
    egg_list.append(egg_weight)
    egg_weight = float(input('Enter the egg weight in oz. (0 to quit): '))

#Prints data about the eggs entered if egg_count is over 0    
print ('\nNumber of eggs: ', egg_count)
if egg_count > 0:
    print(f"{'Average egg weight:'} {sum(egg_list)/egg_count:.2f}")
    print(f"{'Heaviest egg weight:'} {max(egg_list):.2f}")
    print(f"{'Lightest egg weight:'} {min(egg_list):.2f}")
    #Prints the amount of eggs per a category 
    print('\nNumber of eggs by category:\n')
    
    print('Jumbo Eggs:\t', end='')
    for i in egg_list:
        if MIN_JUMBO <= i:
            print('*',end=" ")
            
    print('\nXL Eggs:\t', end ='')
    for i in egg_list:
        if MIN_XL <= i < MIN_JUMBO:
            print('*',end=" ")
            
    print('\nLarge Eggs:\t', end='')
    for i in egg_list:
        if MIN_LARGE <= i < MIN_XL:
            print('*',end=" ")
            
    print('\nMedium Eggs:\t', end='')
    for i in egg_list:
        if MIN_MEDIUM <= i < MIN_LARGE:
            print('*',end=" ")
            
    print('\nSmall Eggs:\t', end='')
    for i in egg_list:
        if  MIN_SMALL <= i < MIN_MEDIUM:
            print('*',end=" ")
    
