import unittest
from unittest import mock
from unittest.mock import patch
from Source.main_part.main_code import round_handle_user_input#try ..\path to data
from Source.Core.round_class import Round
from Source.printing_functions.printing_outputs import print_table
#test method in class
#try except block
class Test_methods(unittest.TestCase):
    @patch('Source.Core.main_part.main_code.round_handle_user_input')
    def test_round_input(self,mock_test_round_handle):
        #Arrange
        list_data = ['a','j','k']
        element ='name'
        mock_test_return_value = i in range(len(list_data))
        #Act
        #no certain actual value
    
    
    @patch.object(Source.Core.round_class,'return_items')
    @patch.object(Source.Core.round_class.Round,'add_order')
   def test_round_class(self,mock_test_return_items):
        #Arrange
        items =['harry','lucozade']
        owner = ['justin']
        mock_test_return_items_value = print_table(f"{owner}'s round",items)
        #Act
        actual =Round
        #Assert
        self.assertEqual

if __name__ == "__main__":
    unittest.main()