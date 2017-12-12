# should_continue = True
# if should_continue:
#     print("hello")


# known_people = ['John', "Anna", "Mary"]
# person = input("Enter the person you know: ")
#
# if person in known_people:
#     print("You know {}!".format(person)) # .format method format string "You know {}!", by replecing {} by parameter in the argument (person)
# else:
#     print("You don't know {}!".format(person))

def who_do_you_know():
    people = input("Enter the names of people you know, separete it by commas: ")
    people_list = people.split(",") # Split the string in to a list
    return people_list

    people_without_spaces = []
    for person in who_do_you_know():
        people_without_spaces.append(person.strip())

    return people_without_spaces

def ask_user():
    person = input("Enter a name of someone you know: ")
    if person in who_do_you_know():
        print("You know {}!".format(person))

ask_user()
