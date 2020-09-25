import csv
from csv import writer

def append_people_list(filename,list_of_elem):
    with open(filename,'a+',newline='')as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow(list_of_elem)
        

def people_list_load(filename):
    with open (filename)as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        line_count=0
        for row in csv_reader:
            line_count += 1
            print(f'Column names are {",".join(row)}')
                


people_list_load('list_people.csv')

#with open(filename,mode = 'w') as f:
# f.writer()


#bad_drink_list('./csv_from_new_folder/bad_drinks.csv')