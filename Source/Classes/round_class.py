import calendar
import datetime
class Round():
    def __init__(self,owner,weekday):
        self.owner = owner
        self.orders = {}
        self.weekday = weekday
    
    def add_order(self,name,drink):
        self.orders[name]=drink
      
    def return_items(self):
        items = []
        for name,drink in self.orders.items():
            items.append(f'{name},{drink}')
        
        print_table(f"{self.owner}'s round",items)


# class test_that_test_round():
#     def method_under_test(self):
#         myclass=Round()
#         return Round.return_items()


