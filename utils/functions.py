import itertools
import re
import numpy as np
import pandas as pd
import itertools
import streamlit as st
import pickle

# Anna's imports
from transformers import FlaxAutoModelForSeq2SeqLM
from transformers import AutoTokenizer
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from gradio_client import Client
from groq import Groq

import utils.config as config


def get_model():
    with open("utils/model.pickle", "rb") as f:
        model = pickle.load(f)
    return model

# Initiate the model
model = get_model()

df = pd.read_parquet('data/Halved-DF.parquet.gzip')

###helll00000"""

'''-----------------------------------------------------------------------------------------------------------'''



def combinations_of_two(ingredients_input): ###dealt with the issue of missing space crash

    '''
    The function generates all unique pairs of ingredients that can be made from the input list of ingredients.
    NOTE FOR FRONT-END: The output of this function is the input for data_query()

    UPDATES
    5/22/2024 by TJ:
    - Modified it quite a bit so output format is one list of tuples
    - Removed the powerset stuff

    Inputs (1):
    ingredients_input (from user input) =  single string with ingredients separated by commas and a space

    Outputs (1):
    ingredients_combinations (to data_query) = a list of tuples, containing all possible combinations of 2 (so if it's 4 ingredients, a list of 6 tuples and nothing more)

    '''

    # split into list of individual ingredients
    ingredients_list = []
    ingredients = re.split('\s|,', ingredients_input)
    [ingredients_list.append(ingredient) for ingredient in ingredients if ingredient != '']

    # create list of all ingredient combinations
    ingredients_combinations = []
    combinations = itertools.combinations(ingredients_list, 2)
    ingredients_combinations = list(combinations)

    return ingredients_combinations

'''-----------------------------------------------------------------------------------------------------------'''

def data_query(ingredients_combinations):
    '''
    Scores all combinations of two ingredients.

    Updates:

    Previous update:
    ##Added a penalty of -5 for pairings that are not in the dataframe

    5/22/2024 by TJ:
    - Removed 'df' from params, defined it outside globally
    - Added descriptions for input and output

    Inputs (1):
    ingredients_combinations (from combinations_of_two) = a list of tuples, containing all possible combinations of 2 as

    Outputs (1):
    df_comb (to muse_comb) = a datafrome with columns 'Combination' and 'Score', containing ingredient combinations and their scores as a dataframe  (for 4 ingredients: all 6 combinations and their respective scores)

    '''

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

    Updates:
    5/22/2024 by TJ:
    - Added descriptions for input and output

    Inputs (1):
    df_comb (from data_query) = a datafrome with columns 'Combination' and 'Score', containing ingredient combinations and their scores as a dataframe  (for 4 ingredients: all 6 combinations and their respective scores)

    Outputs (1):
    ingredients_list (to recipe_generator) = a list of 3 lists, containing the 3 ingredients combinations with highest scores

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


def recipe_generator(ingredients_lists):

    '''
    Takes ingredients_list from muse_comb and returns the actual recipes with titles, ingredients, and directions.

    Updates:
    5/22/2024 by TJ:
    - Added config.py file to protect API Key.

    Inputs (1):
    ingredients_list (from: muse_comb) = a list of 3 lists, containing the 3 ingredients combinations with highest score

    Outputs (1):
    recipe_list (to: get_scores, final_recipe) = a list of 3 dictionaries with 3 keys each: 'title', 'ingredients', 'directions', containing info for the 3 recipes

    '''


    api_key = config.api_key2
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

def get_scores(recipe_list):
    '''
    Generates the score of each recipe.

    Inputs (1):
    recipe_list (from: recipe_generator) = a list of 3 dictionaries with 3 keys each: 'title', 'ingredients', 'directions', containing info for the 3 recipes

    Outputs (1):
    scores (to: final_recipes) = a list of 3 integers, containing the scores for each recipe.
    '''

    scores = []
    recipe_direction = []

    for recipe in recipe_list:
        if 'directions' in recipe:
            recipe_direction.append(recipe['directions'])
        else:
            recipe_direction.append("")

    for direction in recipe_direction:
        scores.append(model.predict_proba([direction])[0][1])

    return scores


'''--------------------------------------------------------------------------------------------------------------'''

def final_recipes(recipe_list, scores, model):  ###<=== Function for evaluating if the score passes the threshold and regenerating if it doesn't

    """
    This evaluates whether the score of a recipe passes or fails the threshold.
    If the recipe doesn't meet the threshold after 3 attempts, the last generated recipe is added.
    NOTE FOR FRONT-END: it's important to make sure that the outputs of the new recipe generator are the same as the
                        old version for this function to still work.
                        optimized_gptrecipe() and scoring_model() must be replaced with the actual functions

    Inputs (3):
    recipe_list (from recipe_generator) = a list of 3 dictionaries with 3 keys each: 'title', 'ingredients', 'directions', containing info for the 3 recipes
    scores (from code in app.py) = list of 3 integers, containing scores for each recipe
    model (from get_model in app.py) = object

    Outputs (1):
    final_recipes = a list of 3 dictionaries with 3 keys each: 'title', 'ingredients', 'directions', containing info for 3 final recipes

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
    '''


    '''
    client = Client("ByteDance/SDXL-Lightning")
    result = client.predict(
            recipe, # str  in 'Enter your prompt (English)' Textbox component
            "1-Step",   # Literal['1-Step', '2-Step', '4-Step', '8-Step']  in 'Select inference steps' Dropdown component
            api_name="/generate_image_1"
    )
    file_path = result.split('gradio')[1]
    url = 'https://bytedance-sdxl-lightning.hf.space/file=/tmp/gradio' + file_path
    return url
