import json, re, os
from src.services.commands.randon_responses import *
from src.services.commands.browser import *
from src.services.commands.search import *
from src.services.commands.project import *
from src.services.commands.emails import *

def load_json(file):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path+"/interations/"+file) as bot_responses:
        return json.load(bot_responses)

response_data = []
dir_path = os.path.dirname(os.path.realpath(__file__))
jsons = os.listdir(dir_path+"/interations")
for f in jsons:
    response_data += load_json(f)

def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1
        if required_score == len(required_words):
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1
        score_list.append(response_score)
    best_response = max(score_list)
    response_index = score_list.index(best_response)
    if input_string == "":
        return "Digite algo para que possamos conversar."
    if best_response != 0:
        bot_return = response_data[response_index]["bot_response"]
        chat = bot_return[0]
        if len(chat) >1:
            print(chat)
        if len(bot_return) > 1:
            funcs = bot_return[1:]
            for f in funcs:
                globals()[f]()
    else:
        return "Não entendi, senhor."

def command(command):
    get_response(command)
