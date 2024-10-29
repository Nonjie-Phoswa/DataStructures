import unittest
from data_structures import *

class MyTestCase(unittest.TestCase):
    def test_length_of_list(self):
        self.assertEqual(len(generate_random_list(5)), 5)
        
    def test_empty_list(self):
        self.assertEqual(generate_random_list(0), [])
         
    def test_random_values_within_range(self):
        random_list = generate_random_list(10)
        for number in random_list:
            self.assertGreaterEqual(number, 0)
            self.assertLessEqual(number, 100)
    
    
     
    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)
        
    def test_find_max_negative(self):
        self.assertEqual(find_max([0, -1 -2, -3, -4]), 0)
        
    def test_find_max_decimal(self):
        self.assertEqual(find_max([0.1, 0.7, 0.5, 0.6]), 0.7)
        
        

    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)
        
    def test_find_min_negative(self):
        self.assertEqual(find_min([0, -1 -2, -3, -4]), -4)
        
    def test_find_min_decimal(self):
        self.assertEqual(find_min([0.1, 0.7, 0.5, 0.6]), 0.1)
        
        

    def test_find_average(self):
        self.assertEqual(find_average([10, 29, 47, 70, 4]), 32)
        
    def test_find_average_negative(self):
        self.assertEqual(find_average([-10, -29, -47, -70, -4]), -32)
        
    def test_find_average_mixed(self):
        self.assertEqual(find_average([10, -29, 4.7, 70, -4]), 10.34)
        


    def test_find_all_even_numbers(self):
        self.assertEqual(find_even_numbers([1, 2, 4, 5, 6, 7]), (2, 4, 6))  
        
    def test_find_all_even_numbers_none(self):
        self.assertEqual(find_even_numbers([1, 3, 5, 7, 9]), ())
        
    def test_find_all_even_numbers_one(self):
        self.assertEqual(find_even_numbers([1, 3, 4, 5, 7]), (4,))



    def test_find_all_odd_numbers(self): 
        self.assertEqual(find_odd_numbers([1, 3, 4, 5, 7]), (1, 3, 5, 7))
        
    def test_find_all_odd_numbers_none(self): 
        self.assertEqual(find_odd_numbers([2, 4, 6, 8, 10]), ())
        
    def test_find_all_odd_numbers_one(self): 
        self.assertEqual(find_odd_numbers([2, 3, 4, 6, 8]), (3,))
        
        

    def test_find_total_number_of_even_numbers(self):
        self.assertEqual(find_number_of_even_numbers([3, 6, 8, 9, 10]), 3)
        
    def test_find_total_number_of_even_numbers_none(self):
        self.assertEqual(find_number_of_even_numbers([3, 7, 1, 9, 11]), 0)
        
    def test_find_total_number_of_even_numbers_negative(self):
        self.assertEqual(find_number_of_even_numbers([3, -6, -8, 9, 10]), 3)
          
        
    
    def test_find_total_number_of_odd_numbers(self):
        self.assertEqual(find_number_of_odd_numbers([3, 6, 8, 9, 10]), 2)
        
    def test_find_total_number_of_odd_numbers_none(self):
        self.assertEqual(find_number_of_odd_numbers([2, 6, 8, 10, 12]), 0)
        
    def test_find_total_number_of_odd_numbers_negative(self):
        self.assertEqual(find_number_of_odd_numbers([3, 6, 8, -9, 10]), 2)
        
           
    
    def test_return_list_stats(self):
        self.assertEqual(
            return_list_stats([1, 2, 3, 4, 5]),
                {"unique_numbers": {1, 2, 3, 4, 5},
                "min": 1,
                "max": 5,
                "average": 3.0,
                "even_numbers": (2, 4),
                "odd_numbers": (1, 3, 5),
                "number_of_even_numbers": 2,
                "number_of_odd_numbers": 3})
        
    def test_all_odd_numbers(self):
        self.assertEqual(
            return_list_stats([1, 3, 5, 7]),
                {"unique_numbers": {1, 3, 5, 7},
                "min": 1,
                "max": 7,
                "average": 4.0,
                "even_numbers": (),
                "odd_numbers": (1, 3, 5, 7),
                "number_of_even_numbers": 0,
                "number_of_odd_numbers": 4})
        
    
    
    def test_basic(self):
        input_list = ['a', '1', 'b', '3', 'c', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)

    def test_mixed_input(self):
        input_list = ['a', '1', 'b', '3', 'c', '2', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_repeated_characters(self):
        input_list = ['1', 'b', 'a', 'c', 'c', 'b', 'a', '1']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_special_characters(self):
        input_list = ['!', '@', '#', '1', '2', '3', '$', '%', '^']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_more_special_characters(self):
        input_list = ['%', '&', '*', '4', '6', '8', '(', ')', '!', 'x']
        result_alphabets, result_numbers = process_characters(input_list)


    def test_generate_squared_dict(self):
        assert generate_squared_dict(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


    
    def test_convert_word_list_sentence(self): 
        self.assertEqual(convert_to_word_list("This is a beautiful day"),
            ['this', 'is', 'a', 'beautiful', 'day'])   
         
    def test_convert_word_list_sentence_punctuation(self): 
        self.assertEqual(convert_to_word_list("This, is a beautiful day!"),
            ['this', 'is', 'a', 'beautiful', 'day'])
        
    def test_convert_word_list_spaces(self): 
        self.assertEqual(convert_to_word_list("This is    a beautiful    day"),
            ['this', 'is', 'a', 'beautiful', 'day'])
        
        

    def test_letters_count_sentence(self): 
        self.assertEqual(
            letters_count_map("This is a beautiful day"), {'a': 2, 'b': 1, 'c': 0, 'd': 1, 'e': 1, 'f': 1, 'g': 0, 'h': 1, 'i': 3, 'j': 0, 'k': 0, 
            'l': 1, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 2, 't': 2, 'u': 2, 'v': 0, 'w': 0, 'x': 0, 'y': 1, 'z': 0})
    def test_on_numbers_and_symbols(self):
        self.assertEqual(letters_count_map("1234!@#$"),
            {letter: 0 for letter in string.ascii_lowercase})
           
    def test_letters_count_sentence_empty(self): 
        self.assertEqual(letters_count_map(""),
            {letter: 0 for letter in string.ascii_lowercase})

    
        
    def test_alphanumeric_1(self):
        self.assertEqual(
            text_to_morse("Hello World 123"),
            '.... . .-.. .-.. ---   .-- --- .-. .-.. -..   .---- ..--- ...--')
    
    def test_alphanumeric_2(self):
        self.assertEqual(
            text_to_morse("Hi! How are you?"),
            '.... .. -.-.--   .... --- .--   .- .-. .   -.-- --- ..- ..--..')
    
    def test_alphanumeric_3(self):
        self.assertEqual(
            text_to_morse("   "),
            '     ')
    

