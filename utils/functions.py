import itertools
import re
import numpy as np
import pandas as pd
import openai
import pandas as pd
import itertools
import streamlit as st

# Anna's imports
from transformers import FlaxAutoModelForSeq2SeqLM
from transformers import AutoTokenizer
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from gradio_client import Client
from groq import Groq


df = pd.read_parquet('data/Halved-DF.parquet.gzip')

###helll00000"""

'''-----------------------------------------------------------------------------------------------------------'''





####################################
# Christine's code
####################################


# needs refactoring?? returning more than just the combinations
def combinations_of_two(ingredients_input): ###dealt with the issue of missing space crash

    '''
    The function generates all unique pairs of ingredients that can be made from the input list of ingredients.
    NOTE FOR FRONT-END: The output of this function is the input for data_query()
    '''

    ingredients_combinations = []
    powerpowerset = []
    ingredients = re.split(r',', ingredients_input.strip())
    ingredients_list = list(set(ingredient.strip() for ingredient in ingredients))
    for r in range(len(ingredients_list)+1):
        combinations = itertools.combinations(ingredients_list, r)
        #powerset.extend(subset for subset in combinations if len(subset) > 1)
        for comb in combinations:
            if len(comb) > 1:
                if len(comb) < 3:
                    ingredients_combinations.append(comb)
                else:
                    powerpowerset.append(comb)
                    for power in powerpowerset:
                        lowerset = []
                        combins = itertools.combinations(power, 2)
                        for arrange in combins:
                            lowerset.append(arrange)
                    ingredients_combinations.append(lowerset)
    return ingredients_combinations

'''-----------------------------------------------------------------------------------------------------------'''

def data_query(ingredients_combinations): ##Added a penalty of -5 for pairings that are not in the dataframe
    """
    INPUT: get_dataframe(), combinations_of_two()
    NOTE FOR FRONT-END: The output of this function is the input for muse_comb()
    """
    data = []
    for combination in ingredients_combinations:
        if len(combination) < 3:
            ingredient1, ingredient2 = combination
            query_str = f'(ingredient1 == "{ingredient1}" & ingredient2 == "{ingredient2}") | (ingredient1 == "{ingredient2}" & ingredient2 == "{ingredient1}")'
            score = df.query(query_str)['scaled_col'].values
            if len(score) > 0:
                data.append({'Combination': combination, 'Score': score})
            else:
                continue
        else:
            scores = []
            for i in combination:
                ingredient1, ingredient2 = i
                query_str = f'(ingredient1 == "{ingredient1}" & ingredient2 == "{ingredient2}") | (ingredient1 == "{ingredient2}" & ingredient2 == "{ingredient1}")'
                score = df.query(query_str)['scaled_col'].values
                if len(score) > 0:
                    scores.append(score[0])
                else:
                    scores.append(-5)
            data.append({'Combination': combination, 'Score': scores})

    df_comb = pd.DataFrame(data)
    return df_comb


# something is wrong with muse_comb
'''-----------------------------------------------------------------------------------------------------------'''
def muse_comb(df_comb): ###If this takes too long, consider taking the nested calculate_sum(array) outside of the function
    '''
     the function calculates the sum of the "Score" values and returns the three combinations with the largest sums
     OUTPUT: [['yeast', 'butter', 'eggs', 'pepper', 'cabbage', 'pork', 'flour', 'sugar'],
                 ['butter', 'eggs', 'pepper', 'cabbage', 'pork', 'flour', 'sugar'],
                 ['yeast', 'butter', 'eggs', 'pepper', 'cabbage', 'flour', 'sugar']]

     NOTE FOR FRONT-END: The return is a list of lists so access the values by indexing e.g. output[0]

                         The output of this function is the input for the recipe generator

                         We might need a function to convert each lists into strings if
                         the recipe generator doesn't do this automatically.
    '''

    def calculate_sum(array):
        return sum(array)

    def ingredients_to_lists(lists):
        ingredients_list = []
        for i in range(3):
            tmp_list = []
            for x in lists[i]:
                tmp_list.append(x[0])
                tmp_list.append(x[1])
            ingredients_list.append(list(set(tmp_list)))

        return ingredients_list

    for i in range(len(df_comb)):
        df_comb["Sum"] = df_comb["Score"].apply(calculate_sum)

    max_values = df_comb.nlargest(3, "Sum")

    max_values = max_values["Combination"].reset_index(drop=True)

    ingredients_lists = ingredients_to_lists(max_values)

    return ingredients_lists

'''--------------------------------------------------------------------------------------------------------------'''


####################################
# Anna's code
####################################

def recipe_generator(ingredients_lists):
    api_key = "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"
    client = Groq(
    api_key=api_key
    )
    recipe_list = []

    if len(ingredients_lists) == 1:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Suggest one recipe with {ingredients_lists} only. The final format of the output should contain Title, Ingredients and Directions only",
                }
            ],
            model="llama3-8b-8192",
        )

        recipe = chat_completion.choices[0].message.content

        parts = recipe.split("**")
        title = parts[1].strip()
        ingredients = parts[4].strip()
        directions = parts[6].strip()

        recipe_dict = {}
        recipe_dict['title'] = title
        recipe_dict['ingredients'] = ingredients
        recipe_dict['directions'] = directions

        recipe_list.append(recipe_dict)

    else:
      for i in range(len(ingredients_lists)):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Suggest one recipe with {ingredients_lists[i]} only. The final format of the output should contain Title, Ingredients and Directions only",
                }
            ],
            model="llama3-8b-8192",
        )

        recipe = chat_completion.choices[0].message.content

        parts = recipe.split("**")
        title = parts[1].strip()
        ingredients = parts[4].strip()
        directions = parts[6].strip()

        recipe_dict = {}
        recipe_dict['title'] = title
        recipe_dict['ingredients'] = ingredients
        recipe_dict['directions'] = directions

        recipe_list.append(recipe_dict)

    return recipe_list


'''--------------------------------------------------------------------------------------------------------------'''

def final_recipes(recipe_list, scores, model):  ###<=== Function for evaluating if the score passes the threshold and regenerating if it doesn't
    """
    This evaluates whether the score of a recipe passes or fails the threshold.
    If the recipe doesn't meet the threshold after 3 attempts, the last generated recipe is added.
    INPUT: Output of the recipe generator function
    NOTE FOR FRONT-END: it's important to make sure that the outputs of the new recipe generator are the same as the
                        old version for this function to still work.
                        optimized_gptrecipe() and scoring_model() must be replaced with the actual functions
    """
    final_recipes = {"Title": [], "Ingredients": [], "Directions": []}
    threshold = 0.3

    for i in range(len(recipe_list)):
        if scores[i] >= threshold:
            final_recipes["Title"].append(recipe_list[i]['title'])
            final_recipes["Ingredients"].append(recipe_list[i]['ingredients'])
            final_recipes["Directions"].append(recipe_list[i]['directions'])
        else:
            n = 0
            tmp_recipe = {
                "Title":recipe_list[i]['title'],
                "Ingredients":recipe_list[i]['ingredients'],
                "Directions":recipe_list[i]['directions']
                         }
            last_recipe = {"title":[],
                           "ingredients":[],
                           "directions":[]
                         }
            while n < 3:
                new_recipe = recipe_generator([tmp_recipe["Ingredients"]]) ###<=== insert actual recipe generator
                new_score = model.predict_proba([new_recipe[0]['directions']]) ###<=== insert the actual scoring model function here
                if new_score[0][1] >= threshold:
                    final_recipes["Title"].append(new_recipe[0]["title"])
                    final_recipes["Ingredients"].append(new_recipe[0]["ingredients"])
                    final_recipes["Directions"].append(new_recipe[0]["directions"])
                    break  # Exit loop if the new recipe passes the threshold
                else:
                    last_recipe = new_recipe  # Update tmp_recipe with the new recipe if the threshold isn't met
                    n += 1
            else: # Add the last generated recipe if the loop completes without finding a passing recipe
                final_recipes["Title"].append(last_recipe[0]["title"][0][0])
                final_recipes["Ingredients"].append(last_recipe[0]["ingredients"][0][0])
                final_recipes["Directions"].append(last_recipe[0]["directions"][0][0])
                break  # Exit the outer loop to prevent an unending loop

    return final_recipes

'''--------------------------------------------------------------------------------------------------------------'''

def image_generator(recipe):
    client = Client("ByteDance/SDXL-Lightning")
    result = client.predict(
            recipe, # str  in 'Enter your prompt (English)' Textbox component
            "1-Step",   # Literal['1-Step', '2-Step', '4-Step', '8-Step']  in 'Select inference steps' Dropdown component
            api_name="/generate_image_1"
    )
    file_path = result.split('gradio')[1]
    url = 'https://bytedance-sdxl-lightning.hf.space/file=/tmp/gradio' + file_path
    return url
