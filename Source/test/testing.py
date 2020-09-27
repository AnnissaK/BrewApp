import unittest
from unittest import mock
from unittest.mock import Mock
from unittest.mock import patch
from Source.main_part.main_code import round_handle_user_input,load_into_round_class
from Source.Core.round_class import Round
from Source.printing_functions.printing_outputs import print_table
#test method in class
#try except block
class Test_methods(unittest.TestCase):
    # @patch('Source.main_part.main_code.round_handle_user_input')
    # def test_round_input(self,mock_test_round_handle):
    #     #Arrange
    #     list_data = ['a','j','k']
    #     element ='name'
    #     mock_test_return_value = str(1)
    #     #Act
    #     actual = round_handle_user_input(list_data,element)
    #     #no certain actual value
    #     self.assertEqual(actual,mock_test_return_value)
    #@patch('Source.main_part.main_code.load_into_round_class')
    @patch('Source.Core.round_class.Round')
    def test_round_class(self,mock_test_add_order):
#         #Arrange
        items =['harry','lucozade']
        owner = ['justin']
        round_mock = Mock(Round)
        round_mock.owner = ['justin']
        mock_test_add_order.return_value = {'harry':'lucozade'}
        #mock_test_load_into_round_class.return_value = [0x000001C769E06820] 
        #Act
        r1 = Round(owner)
        actual1 = Round(owner).owner
        r1.add_order('harry','lucozade')
        actual2 = r1.orders
        #actual3 =load_into_round_class 
        #Assert
        self.assertEqual(round_mock.owner,actual1)
        self.assertEqual(mock_test_add_order.return_value,actual2)
        #self.assertEqual(mock_test_load_into_round_class.return_value,actual3)
    
if __name__ == "__main__":
    unittest.main()


