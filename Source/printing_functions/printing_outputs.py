def print_table(title,data):
    width = width_table(title,data)
    print_header(title,width)
    for item in data:
        print(f'| {item}')
    seperator(width)
    
def print_header(title,width):
    seperator(width)
    print(f'| {title.upper()}')
    seperator(width)

def seperator(width):
    print(f"+ {'='* width}")

def width_table(title,data):
    longest =len(title)
    for item in data:
        if len(item)> longest:
            longest = len(item)
    return longest
