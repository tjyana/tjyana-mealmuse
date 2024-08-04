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

# Uncomment below and edit apikey for testing locally:
# import utils.config as config



# THINGS I WANT TO FIX
    # the thing with muse_comb spitting out one letter 'ingredients'
    # the images taking too long to load. display recipe first, then images





def get_model():
    with open("utils/model.pickle", "rb") as f:
        model = pickle.load(f)
    return model

# Initiate the model
model = get_model()

df = pd.read_parquet('data/Halved-DF.parquet.gzip')

###helll00000"""

'''-----------------------------------------------------------------------------------------------------------'''



# def combinations_of_two(ingredients_input): ###dealt with the issue of missing space crash

#     '''
#     The function generates all unique pairs of ingredients that can be made from the input list of ingredients.
#     NOTE FOR FRONT-END: The output of this function is the input for data_query()

#     Inputs (1):
#     ingredients_input (from: user input in app) =  single string with ingredients separated by commas and a space

#     Outputs (1):
#     ingredients_combinations (to: data_query) = 1 list with a mix of tuples and lists of tuples, containing various ingredient combinations

#     '''

    # ingredients_combinations = []
    # powerpowerset = []
    # ingredients = re.split(r',', ingredients_input.strip())
    # ingredients_list = list(set(ingredient.strip() for ingredient in ingredients))
    # for r in range(len(ingredients_list)+1):
    #     combinations = itertools.combinations(ingredients_list, r)
    #     #powerset.extend(subset for subset in combinations if len(subset) > 1)
    #     for comb in combinations:
    #         if len(comb) > 1:
    #             if len(comb) < 3:
    #                 ingredients_combinations.append(comb)
    #             else:
    #                 powerpowerset.append(comb)
    #                 for power in powerpowerset:
    #                     lowerset = []
    #                     combins = itertools.combinations(power, 2)
    #                     for arrange in combins:
    #                         lowerset.append(arrange)
    #                 ingredients_combinations.append(lowerset)
    # return ingredients_combinations


# fix to deal with both spaces and commas better
def combinations_of_two(ingredients_input):
    ingredients_combinations = []

    # Split the input string by commas and strip whitespace
    ingredients = re.split(r',', ingredients_input.strip())
    print('combinations_of_two -> ingredients:', ingredients)

    # Create a list of unique ingredients with stripped whitespace
    ingredients_list = list(set(ingredient.strip() for ingredient in ingredients))
    print('combinations_of_two -> ingredients_list:', ingredients_list)

    # Iterate over all possible combination lengths (from 0 to len(ingredients_list))
    for r in range(len(ingredients_list) + 1):

        # Generate combinations of ingredients of length r
        combinations = itertools.combinations(ingredients_list, r)

        # Iterate over each combination
        for comb in combinations:
            # If the combination length is greater than 1
            if len(comb) > 1:
                # If the combination length is less than 3, add it to ingredients_combinations
                if len(comb) < 3:
                    ingredients_combinations.append([comb])
                else:
                    # Create a list of all 2-element combinations of the current combination
                    lowerset = []
                    combins = itertools.combinations(comb, 2)
                    for arrange in combins:
                        lowerset.append(arrange)

                    # Add the lowerset to ingredients_combinations
                    ingredients_combinations.append(lowerset)

    return ingredients_combinations



'''-----------------------------------------------------------------------------------------------------------'''



# adapt to the above input
def data_query(ingredients_combinations):
    '''
    Scores combinations of ingredients.
    Added a penalty of -5 for pairings that are not in the dataframe

    Inputs (1):
    ingredients_combinations (from: combinations_of_two) = 1 list with a mix of tuples and lists of tuples, containing various ingredient combinations

    Outputs (1):
    df_comb (to: muse_comb) = 1 datafrome with columns 'Combination' and 'Score', containing ingredient combinations and their scores as a dataframe  (for 4 ingredients: all 6 combinations and their respective scores)

    '''


    data = []
    for combination in ingredients_combinations:
        print('data_query -> combination:', combination)
        if len(combination) < 3:
            ingredient1, ingredient2 = combination[0] # splitting issue here
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

    print('data_query -> data:', data)
    df_comb = pd.DataFrame(data)
    return df_comb


###################
# HUGE PROBLEM HERE
# something is wrong with muse_comb
'''-----------------------------------------------------------------------------------------------------------'''
def muse_comb(df_comb):
    '''
    The function calculates the sum of the "Score" values and returns the three combinations with the largest sums

    Inputs (1):
    df_comb (from: data_query) = a dataframe with columns 'Combination' and 'Score', containing ingredient combinations and their scores as a dataframe  (for 4 ingredients: all 6 combinations and their respective scores)

    Output (1):
    ingredients_list (to: recipe_generator) = 1 list of 3 lists, containing the 3 ingredients combinations with highest scores
        ex.:[['yeast', 'butter', 'eggs', 'pepper', 'cabbage', 'pork', 'flour', 'sugar'], ['butter', 'eggs', 'pepper', 'cabbage', 'pork', 'flour', 'sugar'], ['yeast', 'butter', 'eggs', 'pepper', 'cabbage', 'flour', 'sugar']]

    '''

    def calculate_sum(array):
        return sum(array)


    # IS IT HERE?????????????
    # THIS FUNCTION IS CUTTING UP TUPLES INTO SINGLE LETTERS
    def ingredients_to_lists(lists):
        # list of lists of tuples are fed into the function
        # eg. [[('yeast', 'mustard'), ('butter', 'sage'')], [('eggs', 'cabbage'), ('pepper', 'pork')], [('cabbage', 'chicken'), ('pork', 'flour')]]
        ingredients_list = [] # initialize
        for i in range(3):
            tmp_list = [] # initialize
            for x in lists[i]:
                tmp_list.append(x[0]) # append first element
                tmp_list.append(x[1]) # append second element
            ingredients_list.append(list(set(tmp_list)))

        return ingredients_list

    print('muse_comb -> df_comb -> columns in df_comb', df_comb.columns)
    print('muse_comb -> df_comb -> len(df_comb["Combination"])', len(df_comb['Combination']))
    print('muse_comb -> df_comb -> df_comb["Combination"]', df_comb['Combination'])
    # sum upp all scores for each combination in a new column "Sum"
    df_comb["Sum"] = df_comb["Score"].apply(calculate_sum)

    # select top 3 rows with largest sums
    max_values = df_comb.nlargest(3, "Sum")
    print('muse_comb -> max_values (first one):', max_values)

    # take only the "Combination" column
    max_values = max_values["Combination"].reset_index(drop=True)
    print('muse_comb -> max_values (second one):', max_values)

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
    ingredients_list (from: muse_comb) = 1 list of 3 lists, containing the 3 ingredients combinations with highest scores

    Outputs (1):
    recipe_list (to: get_scores, final_recipe) = 1 list of 3 dictionaries with 3 keys each: 'title', 'ingredients', 'directions', containing info for the 3 recipes

    '''


    api_key = st.secrets['api_key2']
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
    Gets the score of each recipe.

    Inputs (1):
    recipe_list (from: recipe_generator) = 1 list of 3 dictionaries with 3 keys each: 'title', 'ingredients', 'directions', containing info for the 3 recipes

    Outputs (1):
    scores (to: final_recipes) = 1 list of 3 integers, containing the scores for each recipe.
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

def get_final_recipes(recipe_list, scores, model):

    """
    1. Evaluates whether the score of a recipe passes or fails the threshold.
    2. If a recipe fails, a new recipe is generated.
    3. If the recipe doesn't meet the threshold after 3 attempts, the last generated recipe is added.
    4. Separates the recipe output into titles, ingredients, directions (different output from recipe_generator).

    Inputs (3):
    recipe_list (from: recipe_generator) = 1 list of 3 dictionaries with 3 keys each: 'title', 'ingredients', 'directions', containing info for the 3 recipes
    scores (from: get_scores) = 1 list of 3 integers, containing scores for each recipe
    model (from: get_model in app.py) = object

    Outputs (1):
    final_recipes = 1 dictionary with 3 keys:
        'title': list of 3 strings, each string containing recipe title
        'ingredients': list of 3 strings, each string containing recipe ingredients
        'directions': list of 3 strings, each string containing recipe directions
    """

    final_recipes = {"title": [], "ingredients": [], "directions": []}
    threshold = 0.3

    for i in range(len(recipe_list)):
        if scores[i] >= threshold:
            final_recipes["title"].append(recipe_list[i]['title'])
            final_recipes["ingredients"].append(recipe_list[i]['ingredients'])
            final_recipes["directions"].append(recipe_list[i]['directions'])
        else:
            n = 0
            tmp_recipe = {
                "title":recipe_list[i]['title'],
                "ingredients":recipe_list[i]['ingredients'],
                "directions":recipe_list[i]['directions']
                         }
            last_recipe = {"title":[],
                           "ingredients":[],
                           "directions":[]
                         }
            while n < 3:
                new_recipe = recipe_generator([tmp_recipe["ingredients"]]) ###<=== insert actual recipe generator
                new_score = model.predict_proba([new_recipe[0]['directions']]) ###<=== insert the actual scoring model function here
                if new_score[0][1] >= threshold:
                    final_recipes["title"].append(new_recipe[0]["title"])
                    final_recipes["ingredients"].append(new_recipe[0]["ingredients"])
                    final_recipes["directions"].append(new_recipe[0]["directions"])
                    break  # Exit loop if the new recipe passes the threshold
                else:
                    last_recipe = new_recipe  # Update tmp_recipe with the new recipe if the threshold isn't met
                    n += 1
            else: # Add the last generated recipe if the loop completes without finding a passing recipe
                final_recipes["title"].append(last_recipe[0]["title"][0][0])
                final_recipes["ingredients"].append(last_recipe[0]["ingredients"][0][0])
                final_recipes["directions"].append(last_recipe[0]["directions"][0][0])
                break  # Exit the outer loop to prevent an unending loop

    return final_recipes

'''--------------------------------------------------------------------------------------------------------------'''



def image_generator(final_recipes):

    '''
    Generates images for each recipe title.

    Inputs (1):
    final_recipes = 1 dictionary with 3 keys:
        'title': list of 3 strings, each string containing recipe title
        'ingredients': list of 3 strings, each string containing recipe ingredients
        'directions': list of 3 strings, each string containing recipe directions

    Outputs (1):
    image_urls = 1 list with 3 strings, containing URLs for each generated image.
    '''

    client = Client("ByteDance/SDXL-Lightning")

    titles = final_recipes['title']
    print(titles)
    image_urls = []
    for title in titles:
        result = client.predict(
                title, # str  in 'Enter your prompt (English)' Textbox component
                "1-Step",   # Literal['1-Step', '2-Step', '4-Step', '8-Step']  in 'Select inference steps' Dropdown component
                api_name="/generate_image_1"
        )
        file_path = result.split('gradio')[1]
        url = 'https://bytedance-sdxl-lightning.hf.space/file=/tmp/gradio' + file_path
        image_urls.append(url)
    return image_urls
