import csv
import re
import sys
import json
from thefuzz import fuzz, process
def overlappingCount(recipe_ingredients,available_ingredients):
    cnt = 0
    for ingredient in available_ingredients: # available ingredients is global set by request
        if re.search(ingredient,recipe_ingredients,re.IGNORECASE):
            cnt += 1 
    return cnt

def start(available_ingredients):
    available_string = ' '.join(available_ingredients)
    counts = []
    line = 0
    with open ("recipes.csv","r",encoding="utf-8") as recipes_csv:
        csv_reader = csv.reader(recipes_csv,delimiter=',')
        for row in csv_reader:
            break
    
    #sorted_list = sorted(counts, key= lambda x: x[1])
    #final_list = sorted_list[-5:]
    #d = {}
    #for e in final_list:
        #d[e[0]] = e[2]

    #output_json = json.dumps(d)
    ##print(output_json)
    #for key,value in d.items():
        #print(F"{key}  {value}")

def find_matches():
    with open ("recipes.csv","r",encoding="utf-8") as recipes_csv:
        csv_reader = csv.reader(recipes_csv,delimiter=',')
        line = 0
        counts = []
        for row in csv_reader:
            line +=1
            if line % 100 == 0:
                break


list_ingredients = ["lemon","blueberry","flour"]
string_ingredients = 'c("whole milk ricotta cheese", "quick-cooking grits", "orange marmalade", "eggs", "lemon juice", "butter")'
#matches = process.extract(list_ingredients,string_ingredients)
#print(matches)
string_ingredients = string_ingredients[2:-1]
list_required = (string_ingredients.split(','))
matches = process.extract(list_ingredients,list_required)
if __name__ == "__main__":
    #find_matches("x") 
    pass