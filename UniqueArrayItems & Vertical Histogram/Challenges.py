# ===== PROBLEM #1 ======
# Given an array of integers [5, 1, 2, 6, 1, 9, 2, 6, 5, 8, 12, 5, 19, 7, 8, ...]
# Write a function to return an array without duplicates.
# ===== PROBLEM #2 ======
# Given an array of integers [2, 1, 2, 101, 4, 95, 3, 250, 4, 1, 3, 2, 2, 7, 98, 123, 99, ...]
# Write a function to print the following sample output that resembles a histogram table:
#
# Num | count
#   1 | xx
#   2 | xxxx
#   3 | x
#   4 | xx
# ...
#  98 | x
#  99 | x
# 99+ | xxx
#
# To clarify, for problem #2, please print the output that closely matches the sample output
# including printing "99+" followed by all occurrences of numbers > 99.
from random import randint


# # # Challenge 1 # # #
class ArrayMaker:
    @classmethod
    def populate_new_array(cls, array_size, min_int, max_int):
        new_array = []
        safe_array_size = []
        feasability_size = max_int - min_int + 1
        if feasability_size < array_size:
            print('* Note* - Array size adjusted to allowable unique range of integers, as this was less than specified'
                  ' array size.')
            safe_array_size = feasability_size
        for x in range(0, safe_array_size):
            while True:
                if len(new_array) == safe_array_size - 1:
                    break
                new_val = randint(min_int, max_int)
                if new_val not in new_array:
                    new_array.append(new_val)
                    break
        return new_array

    def parameter_validation(self, limit, required_type):
        parameter_validity = True
        parameters = [limit, self.min_int, self.max_int]
        for param in parameters:
            if type(param) != required_type:
                parameter_validity = False
        if not parameter_validity:
            print('A type exception occurred while attempting to use input. Please only enter input of type: ' +
                  required_type + '.')
        return parameter_validity

    def __init__(self, min_int, max_int):
        self.min_int = min_int
        self.max_int = max_int

    def __repr__(self):
        return '<Randomized Array of min {}, max {}>'.format(self.max_int, self.min_int)


class RandomSizeAndUniqueValuesArray(ArrayMaker):
    def generate(self):
        if ArrayMaker.parameter_validation(self, self.upperbound, int):
            array_size = randint(1, self.upperbound)
            new_array = ArrayMaker.populate_new_array(array_size, self.min_int, self.max_int)
            return new_array

    def __init__(self, min_int, max_int, upperbound):
        super(self.__class__, self).__init__(min_int, max_int)
        self.upperbound = upperbound

    def __repr__(self):
        return '<Randomized Array of min {}, max {}, and upperbound {}.>'.format(self.max_int, self.min_int,
                                                                                 self.upperbound)


class RandomUniqueValuesArray(ArrayMaker):
    def generate(self):
        if ArrayMaker.parameter_validation(self, self.array_size, int):
            new_array = ArrayMaker.populate_new_array(self.array_size, self.min_int, self.max_int)
            return new_array

    def __init__(self, min_int, max_int, array_size):
        super(self.__class__, self).__init__(min_int, max_int)
        self.array_size = array_size

    def __repr__(self):
        return '<Randomized Array of min {}, max {}, and array size {}.>'.format(self.max_int, self.min_int,
                                                                                 self.array_size)


def challenge_1_menu():
    print(' * Option 1: To generate a randomly sized, random valued array with no duplicates, enter "1".')
    print(' * Option 2: To generate a randomly valued array of a specific size, with no duplicates, enter "2".')
    print(' * Option 3: To input your own array, press "3".')

    selection = int
    options = (1, 2, 3)

    while True:
        selection = int(input('Please input your selection: '))
        if type(selection) != int or selection not in options:
            print('Please input a selection: 1, 2, or 3.')
            continue
        else:
            break

    return selection


def challenge_1_sub_menu(selection):
    print('')
    if selection == 1 or selection == 2:
        new_array = []
        print('Please enter upper and lower bounds for the values to be generated into the array.')
        min_int = int(input('Min: '))
        max_int = int(input('Max: '))
        if selection == 1:
            print('Please enter the upper bound of the randomly sized array you wish to generate.')
            upperbound = int(input('Upperbound: '))
            new_array = RandomSizeAndUniqueValuesArray(min_int, max_int, upperbound).generate()
        if selection == 2:
            print('Please enter the upper bound of the size of the array to be generated.')
            array_size = int(input('Array Size: '))
            new_array = RandomUniqueValuesArray(min_int, max_int, array_size).generate()

        return new_array

    elif selection == 3:
        num_array = list()
        num = input("Enter how many elements you want: ")
        print('Enter numbers in array: ')
        print('* Note * - Any duplicates will be left out of the array, and if so, array will be shorter than '
              'previously specified.')
        for i in range(int(num)):
            n = input("num: ")
            if int(n) not in num_array:
                num_array.append(int(n))
        return num_array


# # # Challenge 2 # # #
class VerticalHistogram:
        def get_under_99_tally(self, array):
            tally = {}
            # tally = self.append_header(tally)
            for item in array:
                if item < 99:
                    if item in tally:
                        count = tally[item] + 1
                    else:
                        count = 1
                    tally.update({item: count})
            return tally

        def get_over_98_tally(self, array):
            count = 0
            for item in array:
                if item >= 99:
                    count += 1
            return count

        def genterate_row_list(self, tally_dict):
            histogram = []
            for key in tally_dict:
                padding = ''
                if key == '99+':
                    padding = ''
                else:
                    if int(key) <= 9:
                        padding = '  '
                    elif int(key) > 9:
                        padding = ' '
                histogram.append(str(key) + padding + self.column_delimeter + str(tally_dict[key]))
            return histogram

        def convert_counts_to_bars(self, tally_counts):
            for key in tally_counts:
                bar = tally_counts[key] * 'x'
                tally_counts.update({key: bar})
            tally_bars = tally_counts
            return tally_bars

        def make_vertical_histogram(self, array):
            tally_value_counts = self.get_under_99_tally(array)
            over_99_tally = self.get_over_98_tally(array)
            self.table_footer = '99+' + self.column_delimeter + 'x'*over_99_tally
            tally_value_bars = self.convert_counts_to_bars(tally_value_counts)
            histogram = self.genterate_row_list(tally_value_bars)
            return histogram

        def print(self):
            print('')
            print(self.table_header)
            for row in self.vertical_histogram:
                print(row)
            print(self.table_footer)

        def __init__(self, array):
            self.column_delimeter = ' | '
            self.bar_symbol = 'x'
            self.key_title = 'Num'
            self.count_title = 'Count'
            self.table_header = self.key_title + self.column_delimeter + self.count_title
            self.input_array = sorted(array)
            self.vertical_histogram = self.make_vertical_histogram(self.input_array)
            self.print()

        def __repr__(self):
            return str(self.vertical_histogram)


def get_intput_array():
    num_array = list()
    num = input("Enter how many elements you want: ")
    print('Enter numbers in array: ')
    for i in range(int(num)):
        n = input("num: ")
        num_array.append(int(n))
    return num_array


def challenge_2_menu(sample_array):
    print(' * Option 1: To use the "sample array" shown below, enter "1"')
    print('   - Sample Array: ' + str(sample_array))
    print(' * Option 2: To create a fresh, new array, enter "2".')

    selection = int
    options = (1, 2)

    while True:
        selection = int(input('Please input your selection: '))
        if type(selection) != int or selection not in options:
            print('Please input a selection: 1, or 2.')
            continue
        else:
            break

    return selection


# # # Challenge 1 & 2 Menu # # #
def main_menu():
    print('')
    print('# # # Welcome # # #')
    print('Challenge #1:')
    print('Given an array of integers [5, 1, 2, 6, 1, 9, 2, 6, 5, 8, 12, 5, 19, 7, 8, ...]')
    print('Write a function to return an array without duplicates.')
    print('Challenge #2:')
    print('Given an array of integers [2, 1, 2, 101, 4, 95, 3, 250, 4, 1, 3, 2, 2, 7, 98, 123, 99, ...]')
    print('Write a function to print the following sample output that resembles a histogram table.')
    print('')

    selection = int
    options = (1, 2)

    while True:
        selection = int(input('Please select a challenge: '))
        if type(selection) != int or selection not in options:
            print('Please input a selection: 1, or 2.')
            continue
        else:
            break

    return selection


if __name__ == '__main__':
    challenge_selection = main_menu()
    if challenge_selection == 1:
        selection_1 = challenge_1_menu()
        generated_array = challenge_1_sub_menu(selection_1)
        print('')
        print('Here is your new array: ')
        print(str(generated_array))
    elif challenge_selection == 2:
        sample_array = [2, 1, 2, 101, 4, 95, 3, 250, 4, 1, 3, 2, 2, 7, 98, 123, 99]
        input_array = []
        selection_1 = challenge_2_menu(sample_array)
        if selection_1 == 1:
            input_array = sample_array
        elif selection_1 == 2:
            input_array = get_intput_array()
        vertical_histogram = VerticalHistogram(input_array)
