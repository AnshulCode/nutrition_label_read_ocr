import pytesseract
from PIL import Image
import re
from fuzzywuzzy import fuzz
import json
im = Image.open('label2.jpg')
objs = pytesseract.image_to_string(im)
file = open("output2.txt","w")
file.write(objs)
file = open("output2.txt","r")
list = file.readlines()
new_list = []
index = 0
totals = ""

def has_digit(string):
    str = ""
    for i in string:
        str = str + i
        if str.isdigit():
            return True
        else:
            return False
for i in list:
    for char in i:
        if char == '\n':
            break
        totals = totals + char
    new_list.append(totals)
    totals = ""
final_list = []
protein_obj = {'Protein':{'grams': "",'daliy_val': ""}}

nutrition_facts_object = {
                'servings info':"",
                'Calories':"",
                'Protein':{'grams': "",'daliy_val': ""},
                 'Trans Fat': {'grams': "",'daliy_val': ""},
                 'Total Sugars': {'grams': "",'daliy_val': ""},
                'Sodium':{'grams': "",'daliy_val': ""},
                'Vitamin D':{'grams': "",'daliy_val': ""},
                'Dietary Fiber': {'grams': "",'daliy_val': ""},
                'Calcium': {'grams': "",'daliy_val': ""},
                'Total Carbohydrate':{'grams': "",'daliy_val': ""},
                'Iron':{'grams': "",'daliy_val': ""},
                'Potassium': {'grams': "",'daliy_val': ""}
            }
check_list = ["Calories","Protein" ,"Trans Fat","Total Sugars", "Sodium","Vitamin D", "Dietary Fiber","Calcium","Total Carbohydrate","Iron","Potassium"]
for i in new_list:
    if i == "" or i == " ":
        continue
    final_list.append(i)

bool = True
print(final_list)
for int in final_list:
    if int.lower().__contains__("serving size"):
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
            string = elm.replace(elm2,"")
            string_arr = string.split(" ")
            for char in string_arr:
                if char.__contains__("g"):
                    nutrition_facts_object[elm2]['grams'] = char
                if  char.__contains__("%"):
                    nutrition_facts_object[elm2]['daliy_val'] = char
            break

print(json.dumps(nutrition_facts_object, indent=4))












