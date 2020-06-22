import pytesseract
from PIL import Image
from io import StringIO
import re
from fuzzywuzzy import fuzz
import json
import cv2

def has_digit(string):
    str = ""
    for i in string:
        str = str + i
        if str.isdigit():
            return True
        else:
            return False
def print_json(im):
    ratio = im.size[1] / im.size[0]
    ratio = round(ratio)
    if not ratio == 2:
        im = im.resize((im.size[0],im.size[0]*2))
    objs = pytesseract.image_to_string(im)
    file = StringIO(objs)
    list = file.readlines()
    new_list = []
    index = 0
    totals = ""
    final_list = []
    protein_obj = {'Protein': {'grams': "", 'daliy_val': ""}}

    nutrition_facts_object = {
        'servings info': "",
        'Calories': "",
        'Protein': {'grams': "", 'daily_val': ""},
        'Trans Fat': {'grams': "", 'daily_val': ""},
        'Total Sugars': {'grams': "", 'daily_val': ""},
        'Sodium': {'grams': "", 'daily_val': ""},
        'Vitamin D': {'grams': "", 'daily_val': ""},
        'Dietary Fiber': {'grams': "", 'daily_val': ""},
        'Calcium': {'grams': "", 'daily_val': ""},
        'Total Carbohydrate': {'grams': "", 'daily_val': ""},
        'Iron': {'grams': "", 'daily_val': ""},
        'Potassium': {'grams': "", 'daily_val': ""}
    }
    check_list = ["Calories", "Protein", "Trans Fat", "Total Sugars", "Sodium", "Vitamin D", "Dietary Fiber", "Calcium",
                  "Total Carbohydrate", "Iron", "Potassium"]
    totals = ""
    for i in list:
        for char in i:
            if char == '\n':
                break
            totals = totals + char
        new_list.append(totals)
        totals = ""

    for i in new_list:
        if i == "" or i == " ":
            continue
        final_list.append(i)

    bool = True
    for int in final_list:
        if int.lower().__contains__("serving size") or int.lower().startswith("serving"):
            nutrition_facts_object['servings info'] = int
            final_list.remove(int)
        else:
            if int.startswith("Calories"):
                string = int.split(" ")
                for i in string:
                    if i.isdigit():
                        nutrition_facts_object['Calories'] = i
                        break
                final_list.remove(int)
    for elm in final_list:
        for elm2 in check_list:
            if elm.startswith(elm2):
                string = elm.replace(elm2, "")
                string_arr = string.split(" ")
                for char in string_arr:
                    if char.__contains__("g") or char.isdigit():
                        if not char.__contains__("g"):
                            nutrition_facts_object[elm2]['grams'] = char +"g"
                        nutrition_facts_object[elm2]['grams'] = char
                    if char.__contains__("%"):
                        nutrition_facts_object[elm2]['daily_val'] = char
                break
    file.close()
    for elm in check_list:
        if elm.__contains__(" "):
            old = elm
            string = elm.replace(" ", "_")
            nutrition_facts_object[string] = nutrition_facts_object.pop(old)
    return json.dumps(nutrition_facts_object, indent=4)


im = Image.open('label1.png')
print(print_json(im))