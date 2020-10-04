import unittest
from unittest import mock
from unittest.mock import Mock
from unittest.mock import patch
from Source.main_part.main_code import round_handle_user_input,load_into_round_class
from Source.Classes.round_class import Round
from Source.Classes.favourites_class import Favourites
from Source.Classes.drink_and_people_class import Person,Drink
from Source.printing_functions.printing_outputs import print_table
from Source.main_part.main_code import print_people,load_people,load_into_list
from Source.main_part.main_code import print_previous_orders,add_faves_class

#test method in class
#try except block
#0x00000212D1D82130>, <Source.Core.drink_and_people_class.Person object at 0x00000212D1D82430>, <Source.Core.drink_and_people_class.Person object at 0x00000212D1E65D00>, <Source.Core.drink_and_people_class.Person object at 0x00000212D1E65F40>, <Source.Core.drink_and_people_class.Person object at 0x00000212D1E65FD0>, <Source.Core.drink_and_people_class.Person object at 0x00000212D1E65F70>, <Source.Core.drink_and_people_class.Person object at 0x00000212D1E65A90>, <Source.Core.drink_and_people_class.Person object at 0x00000212D1E77040>, <Source.Core.drink_and_people_class.Person object at 0x00000212D1E770A0>, <Source.Core.drink_and_people_class.Person object at 0x000002
class Test_methods(unittest.TestCase):
    # @patch('Source.Core.favourties_class.Favourites')
    # @patch('Source.main_part.main_code.add_faves_class')
    # def test_add_faves_class(self,mock_test_add_fave_class):
    
    #@patch('Source.Core.drink_and_people_class.Person')
    def test_people_class(self):
        #Arrange
        people_mock_test = Mock(Person)
        #Person_name =(people_mock_test('Joe')).name
        people_mock_test.name = 'joe'
        people_mock_test.age = '17'
        P1=Person('joe','17')
        Actual1 = P1.name
        Actual2 = P1.age
        #Assert
        self.assertEqual(Actual1,people_mock_test.name)
        self.assertEqual(Actual2,people_mock_test.age)
        
    def test_drinks_class(self):
        drinks_mock_test = Mock(Drink)
        drinks_mock_test.name = 'Amy'
        drinks_mock_test.age = '24'
        drinks_mock_test.cost = '1.50'
        D1 = Drink('Amy','24','1.50')
        Actual1 = D1.name
        Actual2 = D1.age
        Actual3 = D1.cost
        self.AssertEqual(Actual1,drinks_m)

        
   
   
   
   
    # @patch('Source.Core.drink_and_people_class.Person')
    # @patch('Source.main_part.main_code.load_into_list')
    # @patch('Source.main_part.main_code.load_people')
    # @patch('Source.main_part.main_code.print_people')
    # def test_print_people(self,mock_test_print_people,return_load_people,return_load_into_list_name,return_load_into_list_age):
    #     #Arrange
    #     return_load_into_list_name.return_value =['anna', 'greg', 'sham', 'douglas', 'fetus', 'dream', 'butter', 'hannah', 'joe', 'jenny']
    #     return_load_into_list_age.return_value= ['17', '16', '18', '15', '21', '25', '31', '26', '24', '24']
    #     person_mock = Mock(Person)
    #     people =[]
    #     for i,x in zip(return_load_into_list_name.return_value,return_load_into_list_age.return_value):
    #         people.append(person_mock(i,x))
    #     return_load_people.return_value =people
    #     return_load_people.return_value = [ 0x00000212D1D82130,  0x00000212D1D82430,  0x00000212D1E65D00, 0x00000212D1E65F40,  0x00000212D1E65FD0, 0x00000212D1E65F70, 0x00000212D1E65A90,  0x00000212D1E77040,  0x00000212D1E770A0,  0x00000212D1E77100]
    #     mock_test_print_people.return_value = [person_mock.name for person in return_load_people.return_value]
    #     #Actt at
    #     actual1 = load_into_list('person.csv','name')
    #     actual2 = load_into_list('person.csv','age')
    #     actual3 = load_people(actual1,actual2)
    #     actual4 = print_people()
    #     #Assert
    #     self.assertEqual(return_load_into_list_name.return_value,actual1)
    #     self.assertEqual(return_load_into_list_age.return_value,actual2)
    #     self.assertEqual(return_load_people.return_value,actual3)
    #     self.assertEqual(mock_test_print_people.return_value,actual4)
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
#     @patch('Source.Core.round_class.Round')
#     def test_round_class(self,mock_test_add_order):
# #         #Arrange
#         items =['harry','lucozade']
#         owner = ['justin']
#         round_mock = Mock(Round)
#         round_mock.owner = ['justin']
#         mock_test_add_order.return_value = {'harry':'lucozade'}
#         #mock_test_load_into_round_class.return_value = [0x000001C769E06820] 
#         #Act
#         r1 = Round(owner)
#         actual1 = Round(owner).owner
#         r1.add_order('harry','lucozade')
#         actual2 = r1.orders
#         #actual3 =load_into_round_class 
#         #Assert
#         self.assertEqual(round_mock.owner,actual1)
#         self.assertEqual(mock_test_add_order.return_value,actual2)
        #self.assertEqual(mock_test_load_into_round_class.return_value,actual3)
    
if __name__ == "__main__":
    unittest.main()


