import random

def salutation():
    responses = [
        "Oi, senhor.", "Ola, senhor.",
        "Oi, meu bem.", "Ola, meu bem.", "Oie, meu bem.",
        "Oiii!!!", "Oieee!!!"
    ]
    print(random.choice(responses))
def farewell():
    responses = [
        "Tchau!", "Ate mais!", "Ate breve!"
        "Tchau, senhor.", "Tchau, senhor, foi um prazer.",
        "Tchau, meu bem.", "Tchau, meu bem, foi um prazer."
    ]
    print(random.choice(responses))