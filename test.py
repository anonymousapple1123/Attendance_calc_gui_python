class Variable:
    #added a fookin comment
    def __init__(self):
        self.absent = 0.0
        self.total = 0.0
        self.percentage = 0.0


class Percentage:
    def __init__(self, absent=0.0, total=0.0):
        self.absent = absent
        self.total = total

    def setter_function(self, absent, total):
        self.absent = absent
        self.total = total

    def calculate_percentage(self):
        return 100 - ((self.absent / self.total) * 100)

    def total_val(self):
        return self.total

    def absent_val(self):
        return self.absent

    def add_absent_days(self, days):
        curr_absent = self.absent + (days * 8)
        percentage = 100 - ((curr_absent / self.total) * 100)
        print(f"\nAttendance after your leave -> {percentage:.2f}%")
        days_to_be_present = (10 * curr_absent) - self.total
        print(f"\nPresent for {days_to_be_present / 8:.2f} days to have {days} day fine free off.")


def input_lectures():
    absent = float(input("Enter number of lectures you were absent: "))
    total = float(input("Enter total number of lectures in the session: "))
    return absent, total


def calculate_percentage(absent, total):
    percentage = 100 - ((absent / total) * 100)
    print(f"Your current Percentage = {percentage:.2f}%")


def print_choice():
    print("\n\n1. Calculate percentage.")
    print("2. Days to take leave without fine.")
    print("3. Get specific attendance.")
    print("4. -- Need help! -- ")
    print(" --- Input 0 to quit --- ")


def help_box():
    print("\n******************")
    print("******************\n")
    print("* You have to input your choice as number, like for first choice press 1 and then hit enter button.")
    print("* 1. Calculate percentage. --> It will print your current attendance based on the absent lectures and total lectures.")
    print("* 2. Days to take leave without fine. --> This option will give you the number of days you have to be present or absent to stay away from fine.")
    print("* 3. Get specific attendance. --> In this you input a desired attendance percentage that you want to have.")
    print("* Input the number 0 (zero) to exit the program.")
    print("\n\n******************")
    print("******************\n")


def message_box():
    print("\n******************")
    print("******************\n")
    print("* Check your ERP portal for number of absent lectures and total lectures.")
    print("* Only input integral values without any symbols like '%'.")
    print("* Do not use any character or special symbol; only numeric digits are allowed.")
    print("* The program will provide the number of days to be present/absent without considering the session days left.")
    print("* The program provides near accurate lecture numbers and estimated days number for the same.")
    print("* The program is made keeping in mind the attendance structure as well as fine structure of PSIT-CHE only.")
    print("\n\n******************")
    print("******************\n")


def get_attendance(class_obj):
    percent = float(input("\nInput the percentage you want to obtain: "))
    current_attendance = class_obj.calculate_percentage()

    if percent == 100 and current_attendance != 100:
        print("\nThat is simply not possible")
    elif percent == 100 and current_attendance == 100:
        print("\nYour attendance is at 100%")
    elif percent < current_attendance:
        absent_lectures = (((100 - percent) / 100) * class_obj.total_val()) - class_obj.absent_val()
        absent_lectures_int = int(absent_lectures)
        print(f"\nAbsent for {-absent_lectures_int} lectures or {-absent_lectures_int / 8:.2f} days to reach attendance {percent}%.")
    elif percent > current_attendance:
        present_lectures = ((class_obj.absent_val() * 100) / (100 - percent)) - class_obj.total_val()
        present_lectures_int = int(present_lectures)
        print(f"\nPresent for {present_lectures_int} lectures or {present_lectures_int / 8:.2f} days to reach attendance {percent} %.")


def fine_free_off(class_obj):
    days = float(input("\nEnter number of days to be absent: "))
    class_obj.add_absent_days(days)


def main():
    message_box()
    choice = 0
    attendance = Variable()
    percentage_object = Percentage()

    attendance.absent, attendance.total = input_lectures()
    percentage_object.setter_function(attendance.absent, attendance.total)

    while True:
        print_choice()
        choice = int(input("\nInput choice number: "))
        print("\n****************\n")

        if choice == 0:
            print("Quitting the program...")
            break
        elif choice == 1:
            calculate_percentage(attendance.absent, attendance.total)
        elif choice == 2:
            fine_free_off(percentage_object)
        elif choice == 3:
            get_attendance(percentage_object)
        elif choice == 4:
            help_box()
        else:
            print("Please input a valid choice!")
            help_box()


if __name__ == "__main__":
    main()

