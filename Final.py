from datetime import datetime as dt

# Variable for Range of Years and Value of Key

start_year = 1970
end_year = 2100

start_value = -1000000
end_value = 1000000
print(" Enter Dictionary Value pairs in format yyyy-mm-dd in range [1970-01-01....2100-01-01] "
      "and unique key value in integer range [-1,000,000...1,000,000] ")
print("Also enter consistent dates from the first entry with same year and month")

# Dictionaries for Processing

input_dates = {}
temp_dict = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
final_dict = {}


# Function to validate if input is in given range and format

def validate_input(input_date, input_key):
    try:
        input_date = dt.strptime(input_date, "%Y-%m-%d")
        if start_year <= input_date.year <= end_year:
            pass
        else:
            print("Enter Year between 1970-2100")

        if start_value <= input_key <= end_value:
            pass
        else:
            print("Enter Key Value between -1,000,000..1,000,000")

        # assigning key value to the date entered by the user
        input_dates[date] = date_key
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


# Function for finding the day of given dates and adding their values

def find_weekday(temp_dates, dict_add, ans_dict):
    i = 0
    j = 0
    first_date = list(temp_dates.keys())[0]
    input_date = dt.strptime(first_date, "%Y-%m-%d")
    first_year = str(input_date.year)
    first_month = str(input_date.month)
    # finding duplicate values
    # from dictionary
    # using a naive approach
    rev_dict = {}

    for key, value in input_dates.items():
        rev_dict.setdefault(value, set()).add(key)

    duplicate_key = [key for key, values in rev_dict.items()
                     if len(values) > 1]
    duplicate_value = [values for key, values in rev_dict.items()
                       if len(values) > 1]

    # printing result if any duplicates entry are found in Dictionary
    print("duplicate Keys found " + str(duplicate_key) + " Duplicates Values found for dates " + str(duplicate_value))

    if len(first_month) == 1:
        first_month = "0" + first_month
    else:
        pass

    # Condition to check whether at least one Monday and Sunday are present in the Dates Dictionary
    for input_date, input_datekey in temp_dates.items():
        input_date = dt.strptime(input_date, "%Y-%m-%d")
        if input_date.strftime("%A") == "Monday":
            i = i + 1
        if input_date.strftime("%A") == "Sunday":
            j = j + 1

    if input_date.strftime("%Y") == first_year and input_date.strftime("%m") == first_month:
        print("All years and months of the dates are correct")
    else:
        print("Years or months of the given dates didn't matched")

    if i == 0 or j == 0:
        print("Add at least one Monday and Sunday in the List")

    # for loop for adding the Key value pair of Dictionary
    for input_date, input_datekey in temp_dates.items():
        input_date = dt.strptime(input_date, "%Y-%m-%d")
        if input_date.strftime("%A") == list(dict_add.keys())[0]:
            ans_dict[input_date.strftime("%a")] = input_datekey + dict_add.get("Monday")
            dict_add["Monday"] = input_datekey
        elif input_date.strftime("%A") == list(dict_add.keys())[1]:
            ans_dict[input_date.strftime("%a")] = input_datekey + dict_add.get("Tuesday")
            dict_add["Tuesday"] = input_datekey
        elif input_date.strftime("%A") == list(dict_add.keys())[2]:
            ans_dict[input_date.strftime("%a")] = input_datekey + dict_add.get("Wednesday")
            dict_add["Wednesday"] = input_datekey
        elif input_date.strftime("%A") == list(dict_add.keys())[3]:
            ans_dict[input_date.strftime("%a")] = input_datekey + dict_add.get("Thursday")
            dict_add["Thursday"] = input_datekey
        elif input_date.strftime("%A") == list(dict_add.keys())[4]:
            ans_dict[input_date.strftime("%a")] = input_datekey + dict_add.get("Friday")
            dict_add["Friday"] = input_datekey
        elif input_date.strftime("%A") == list(dict_add.keys())[5]:
            ans_dict[input_date.strftime("%a")] = input_datekey + dict_add.get("Saturday")
            dict_add["Saturday"] = input_datekey
        elif input_date.strftime("%A") == list(dict_add.keys())[6]:
            ans_dict[input_date.strftime("%a")] = input_datekey + dict_add.get("Sunday")
            dict_add["Sunday"] = input_datekey
    print(ans_dict)


add_dates = True

while add_dates:
    # prompt user for adding date and it's key value
    date: str = input("\n Enter date in yyyy-mm-dd format & in range [1970-01-01....2100-01-01] ")
    date_key: int = int(input("\n Enter key value between [-1,000,000...1,000,000] "))
    validate_input(date, date_key)
    repeat = input("\n If you don't want to add more dates type no else press any key ")
    if repeat == 'no':
        add_dates = False

    # adding dates to the dictionary completed

find_weekday(input_dates, temp_dict, final_dict)
print("The Dates added are: " + str(input_dates))

# For Finding missing dates and appending it to Dictionary I have tried using panda and Dataframes
# But it would take a lot of time so Posting the remaining work
# start_date: datetime = dt.strptime(temp_dates[0], "%Y-%m-%d")  # parse first date
# end_date = dt.strptime(temp_dates[-1], "%Y-%m-%d")  # parse last date
# days = (end_date - start_date).days  # how many days between?

# create a dictionary of all dates with 0 occurrences
# all_dates = {dt.strftime(start_date + dt.timedelta(days=k),
# "%Y-%m-%d"): 0 for k in range(days + 1)}

# print(all_dates)

# df = pd.DataFrame(input_dates)
# idx = pd.date_range(temp_dates[0], temp_dates[-1])
# s = pd.Series(input_dates)
# s.index = DatetimeIndex(s.index)

# s = s.reindex(idx, fill_value=0)
# print(s)
