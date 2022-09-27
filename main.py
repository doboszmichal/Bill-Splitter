import random
def main():
    start()


def start():
    ask_user()

def ask_user():
    print("Enter the number of friends joining (including you):")
    people_number = int(input())
    if people_number <= 0:
        print("No one is joining for the party")
        exit()
    get_people_number(people_number)
    ask_names(people_number)


def get_people_number(people_number):
    number_of_people = people_number


def ask_names(people_number):
    name_dictionary = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(1, people_number + 1):
        name = input()
        name_dictionary[name] = 0
    print("Enter the total bill value:")
    total_bill = float(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    user_input = input()
    if user_input == "Yes":
        lucky = random.choice(list(name_dictionary))
        print("{} is the lucky one!".format(lucky))
        if total_bill % (people_number - 1) == 0:
            for i in name_dictionary:
                name_dictionary[i] = int(total_bill / (people_number - 1))
                name_dictionary[lucky] = 0
        elif total_bill % (people_number - 1) != 0:
            for i in name_dictionary:
                name_dictionary[i] = round((total_bill / (people_number - 1)), 2)
                name_dictionary[lucky] = 0
    else:
        print("No one is going to be lucky")
        if total_bill % people_number == 0:
            for i in name_dictionary:
                name_dictionary[i] = int(total_bill / people_number)
        elif total_bill % people_number != 0:
            for i in name_dictionary:
                name_dictionary[i] = round((total_bill / people_number), 2)
    print(name_dictionary)


if __name__ == '__main__':
    main()
