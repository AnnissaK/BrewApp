import unittest
from unittest import mock
from unittest.mock import patch
from copy_working_classes import round_handle_user_input
from copy_working_classes import print_people,load_into_list

class Test_methods(unittest.TestCase):
    @patch('copy_working_classes.round_handle_user_input')
    @patch('copy_working_class.load_into_list')
    def test_round_handle_user_input(self,input_load_list,mock_test_order_request_returned)
        #Arrange
        mock_.return_value = 1
        #Act
        actual =round_handle_user_input(print_people(),'name')
        #Assert
        self.assertEqual(actual,1)

if __name__ == "__main__":
    unittest.main()
        

        


# def add_list_element(my_list, element):
#     """Appends specified element to specified list,
# IF the element is a string that contains only characters, and can not be
# empty, have all the characters be spaces, contain any numbers or be already in the list. """
#     if not element or element.isspace():
#         print("You have not entered anything!")
#     elif any(num in element for num in "0123456789"):
#         print("No numbers can be included in the name.")
#     elif element.capitalize() not in my_list:
#         my_list.append(element.capitalize())
#         print(f"Your choice: {element.capitalize()} was successfully added!")
#     else:
#         print("Already on the list. Try a different option.")
#     return my_list

# def test_list():
#     #Arrange
#     my_list = ['anna','james']
#     element ='fred'
#     expected = ['anna','james','Fred']

#     #Act
#     actual = add_list_element(my_list,element)

#     #Assert
#     assert actual== expected

# test_list()