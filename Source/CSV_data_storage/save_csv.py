from csv import writer

def save_csv_items(path,name,drink):
    with open(path,'a+') as csvfile:
        csv_writer = writer(csvfile)
        csv_writer.writerow([name,drink])

def save_round(ordername,name,drink):
    with open('round.csv','a+',newline ='') as csvfile:
        csv_writer = writer(csvfile)
        csv_writer.writerow([ordername,name,drink])