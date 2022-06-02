# Lazy_Calculator
# Siphesihle Sandiso Dlamini
# 20/05/2021
from factor_finder import take_input

print("""
                            Welcome to The HCF and LCM Calculator. 
                                Please use only whole numbers.\n
        """
      )

run = True

while run:
    # Let's start with two numbers
    class UsableSet:
        """A Class to collect the user's number inputs."""

        def __init__(self,
                     first_num,
                     second_num,
                     numbers,
                     ordered_nums,
                     new_ordered_num_list):
            self.first_num = first_num
            self.second_num = second_num
            self.numbers = numbers
            self.ordered_nums = ordered_nums
            self.new_ordered_num_list = new_ordered_num_list

        num_correct = True
        while num_correct:
            try:
                first_num = int(
                    input("What's the first number you'd like to use ?: "
                          ).replace(' ' and ',', ''))
                take_input(first_num)
                second_num = int(
                    input("\nWhat's the second number you'd like to use ?: "
                          ).replace(' ' and ',', ''))
                take_input(second_num)
            except ValueError:
                print("INVALID INPUT")
                continue
            else:
                # Add the numbers into a list for easier management
                numbers = [first_num, second_num]
                ordered_nums = sorted(numbers)
                new_ordered_num_list = sorted(numbers.copy())
                num_correct = False


    def find_hcf():
        """Calculate The Highest Common Factor."""
        # Create loop
        hcf = True
        while hcf:
            try:
                remainder = (int(UsableSet.ordered_nums[1])
                             % int(UsableSet.ordered_nums[0]))
            except ZeroDivisionError:
                print("You can't divide by Zero.")
                remainder = 0
            except NameError:
                print("Please make sure you type in the correct numbers.")
                break
            UsableSet.ordered_nums[1] = remainder
            UsableSet.ordered_nums.sort()

            if remainder == 0:
                return UsableSet.ordered_nums[1]


    def find_lcm():
        """Calculate The Lowest Common Multiple."""
        usable_hcf = int(find_hcf())
        try:
            a = UsableSet.new_ordered_num_list[0] / usable_hcf
        except ZeroDivisionError:
            a = 0
        return a * UsableSet.new_ordered_num_list[1]


    def display_hcf():
        """Display The Highest Common Factor."""
        usable_hcf = int(find_hcf())
        if usable_hcf == 0:
            print(str(UsableSet.new_ordered_num_list[0])
                  + " Doesn't have any factors therefore "
                  + str(UsableSet.first_num) + " and "
                  + str(UsableSet.second_num) +
                  " don't have a Highest Common Factor. ")
        else:
            print('\nThe Highest Common Factor of ' + str(UsableSet.first_num)
                  + ' and ' + str(UsableSet.second_num) + ' is '
                  + str(usable_hcf) + '.')


    def display_lcm():
        """Display The Lowest Common Multiple."""
        usable_lcm = int(find_lcm())
        print('\nThe Lowest Common Multiple of ' + str(UsableSet.first_num) +
              ' and ' + str(UsableSet.second_num) + ' is '
              + str(usable_lcm) + '.')


    def main():

        print("""
                Choose what you want to calculate:
                
                                1- HCF
                                2- LCM
                                0- Quit
            
                      """)
        choice = input('Choice: ')

        while choice != 0:
            if choice == '1':
                display_hcf()
                break
            if choice == '2':
                display_lcm()
                break
            if choice == '0':
                break
            print('\nPlease choose the correct input !!')
            print(((f'The numbers you chose are {str(UsableSet.first_num)}' +
                    ' and ') + str(UsableSet.second_num) + '.'))

            print("""
                Choose what you want to calculate:
                
                                        1- HCF
                                        2- LCM
                                        0- Quit

                                     """)
            choice = input('Choice:')


    main()

    use_again = input("\n\nPress any button then 'enter' to continue or "
                      "press 'q' then 'enter' to quit.\n")
    print('\n\n')
    if use_again.lower() == 'q':
        run = False
    else:
        run = True
