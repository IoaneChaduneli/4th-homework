months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]



while True:
    date = input("MM/DD/YYYY: ")

    if len(date.split("/")) == 3:
        # convert list and split the chars
        date = date.split("/")

        print(f'{date[2]}-{date[1]:0>2}-{date[0]:0>2}')
    
    # if string and int is in input
    elif date.replace(" ", "").isalnum():

        for month in months:
            #understand if month year and day is inputted
            if len(date.split(" ")) == 3:
                # convert list 
                new_date =  date.split(" ")
                # if input month is written in list
                if month in date:
                    # remove string month
                    new_date.remove(month)
                    # string month convert to num month
                    new_date.append(str(months.index(month)+1))
                    #understand which is more than two charachter
                    for i in new_date:
                        if len(i) > 2:
                            year = i
                    
                    print(f'{year}-{new_date[2]:0>2},{new_date[1]:0>2}')
    
    else:
        print("Please Invalid gives us invalid input")
                    
                        
                    
    