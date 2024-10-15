header = """
projekt_1.py: first project for Engeto Online Python Academy

author: Dominik Šváb
email: dominik.svab123@gmail.com
discord: domin08
"""
separator = 40 * "-"
print(header)
print(separator)

registered_users = [
    {"user": "bob", "password": "123"},
    {"user": "ann", "password": "pass123"},
    {"user": "mike", "password": "password123"},
    {"user": "liz", "password": "pass123"}
]

texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

user = input("Enter your username: ")
password = input("Enter your password: ")

is_registered = False

for user_entry in registered_users:
    if user_entry["user"] == user and user_entry["password"] == password:
        is_registered = True

        print("Welcome to the app, ", user, "!")
        print("We have", len(texts), "texts to be analyzed.")
        print(separator)
        print("Enter number between 1 and", len(texts), "to select.")
        
        text_number = input("Enter the number: ")
        if text_number.isdigit() and 0 < int(text_number) <= len(texts):
            text_number = int(text_number)
            print("You have selected number ", str(text_number), ".")
            words = texts[text_number - 1].replace(",", "").replace("\n", " ").replace(".", "").split()
            
            word_count = len(words)
            titlecase_word_count = 0
            uppercase_word_count = 0
            lowercase_word_count = 0
            number_count = 0
            sum_of_numbers = 0

            for item in words:
                if item[0].isupper():
                    titlecase_word_count += 1
                if item.isupper() and item.isalpha():
                    uppercase_word_count += 1
                if item.islower():
                    lowercase_word_count += 1
                if item.isnumeric():
                    number_count += 1
                    sum_of_numbers += int(item)
            
            print(separator)
            print("There are", word_count, "words in the selected text.")
            print("There are", titlecase_word_count, "titlecase words.")
            print("There are", uppercase_word_count, "uppercase words.")
            print("There are", lowercase_word_count, "lowercase words.")
            print("There are", number_count, "numeric strings.")
            print("The sum of all the numbers is", sum_of_numbers, ".")
            
            word_statistics = {}
            for item in words:
                length = len(item)
                if length not in word_statistics:
                    word_statistics[length] = 0
                word_statistics[length] += 1
            
            print(separator)
            print("  LEN |     OCCURRENCES    | NR.")

            for length, count in sorted(word_statistics.items()):
                stars = count * "*"
                print(f"{length:6}|{stars:<20}|{word_statistics[length]}")

        elif not text_number.isdigit():
            print("You have to enter a number!")
        else:
            print("The number you have entered is not valid!")
        
        break
  
else:
    print("$ python projekt1.py")
    print("username:", user)
    print("password:", password)
    print("unregistered user, terminating the program...")
