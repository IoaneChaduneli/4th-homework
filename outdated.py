
while True:
    try:
        #Enter input the date
        date = input("Enter date: (MM/DD/YYYY)")
        #make a list according the separation marks
        date_1 = date.split("/")
        #while my list always be including 2 index year formatted by YYYY/MM/DD
        new_date = f'{date_1[2]}/{date_1[1]:0>2}/{date_1[0]:0>2}'
    except IndexError:
        pass
    else:
        print(new_date)