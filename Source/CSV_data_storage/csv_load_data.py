from csv import DictReader
def load_into_list(filename,header):
    data_list =[]
    with open(filename,'r') as csvfile:
        csv_dict_reader = DictReader(csvfile)
        for row in csv_dict_reader:
            data_list.append(row[header])
        return data_list

def load_into_round_class(x,y,z):
    order_requests=[]
    for owner,name,drink in zip(x,y,z):
        R1=Round(owner)
        R1.add_order(name,drink)
        order_requests.append(R1)
    return order_requests
