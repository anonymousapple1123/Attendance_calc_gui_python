#This file contains core mathematical logic behind every calculation.
from logic import save_file_handler as save

def multiply(absent,total):
    return absent*total
def divide(num1,num2):
    return num1/num2
#calc file
def percent_attendance(absent,total):
    return 100-((absent/total)*100)
# attendance after leave
def need_leave(absent,total,days):
    lectures_per_day=int(list(save.load_settings().values())[0])

    curr_absent=float(float(absent)+(days*lectures_per_day))
    return 100 - ((curr_absent / total) * 100)
#days to stay present to avoid fine.
def avoid_fine(absent,total,leave_days):
    fine_starts_from=int(list(save.load_settings().values())[1])
    lectures_per_day=int(list(save.load_settings().values())[0])


    new_absent=absent+(leave_days*lectures_per_day)
    new_percentage=(100-((new_absent/total)*100))
    #lectures_to_be_present=(10*new_absent)-total -> this line calculated the lectures to be present to avoid fine which starts from 90% 
    lectures_to_be_present = ((100*new_absent)/(100-fine_starts_from)) - total # This line solves the issue and provides the output based on the user defined values of the fine starting percentages.
    return lectures_to_be_present
#get desired attendance
def get_attendance(absent,total,desired_attendance):
    curr_percentage=100-((absent/total)*100)#calculates current percentage.

    if curr_percentage!=100 and desired_attendance==100: #if requested percent is 100 and current is not 100 return error
        return -1.01
    elif desired_attendance<curr_percentage:
        absent_lectures=(((100-desired_attendance)/100)*total)-absent
        return absent_lectures
    elif desired_attendance > curr_percentage:
        present_lectures=((absent*100)/(100-desired_attendance))-total
        return present_lectures
    elif desired_attendance==curr_percentage:
        return 0
