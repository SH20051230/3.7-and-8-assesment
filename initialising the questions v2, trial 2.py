import random
# In this trial instead of using a class I choose to create a dictionaries to store the same information
# and using random choice method to randomly selecting one of the month in the dictionaries)
# Define a list of dictionaries for each quiz question
questions = [
    {"eng_month": "January", "maori_month": "Kohi-tātea", "num_month": 1},
    {"eng_month": "February", "maori_month": "Hui-tanguru", "num_month": 2},
    {"eng_month": "March", "maori_month": "Poutū-te-rangi", "num_month": 3},
    {"eng_month": "April", "maori_month": "Paenga-whāwhā", "num_month": 4},
    {"eng_month": "May", "maori_month": "Haratua", "num_month": 5},
    {"eng_month": "June", "maori_month": "Pipiri", "num_month": 6},
    {"eng_month": "July", "maori_month": "Hōngongoi", "num_month": 7},
    {"eng_month": "August", "maori_month": "Here-turi-kōkā", "num_month": 8},
    {"eng_month": "September", "maori_month": "Mahuru", "num_month": 9},
    {"eng_month": "October", "maori_month": "Whiringa-ā-nuku", "num_month": 10},
    {"eng_month": "November", "maori_month": "Whiringa-ā-rangi", "num_month": 11},
    {"eng_month": "December", "maori_month": "Hakihea", "num_month": 12},
]

def random_question(questions):
    # Choose a random question from the list
    question = random.choice(questions)
    return question["eng_month"], question["maori_month"], question["num_month"]

# Example usage
print(random_question(questions))
