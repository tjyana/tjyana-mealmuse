import streamlit as st
from utils.functions import combinations_of_two, data_query, get_scores, get_final_recipes, muse_comb, recipe_generator, image_generator
import pandas as pd
import pickle

# cache for the model

#Load the .csv file from Google Drive
#Make sure the file is set to "Anyone with a link" or "Anyone on the Internet"
#uncomment the code below after inserting the actual url to the file that we want to use:
###filtered_df = pd.read_csv(url)

#--------------------

if 'page1' not in st.session_state:
    st.session_state['page1'] = True
if 'page2' not in st.session_state:
    st.session_state['page2'] = False
if 'page3' not in st.session_state:
    st.session_state['page3'] = False




if st.session_state['page1']:

    col1, col2, col3 = st.columns([1, 4, 1])
    # Mealmuse header

    col2.markdown("<h1 style='text-align: center; color: black; font-size:60px'>Mealmuse</h1>", unsafe_allow_html=True)

    # Mealmuse subheader (Turn What..)
    col2.markdown("<h2 style='text-align: center; color: grey; font-size:20px'>Turn What You Have to What You Crave &#128512; </h2>", unsafe_allow_html=True)

    col2.image('Streamlit/pages/mealmuse_images/people4.png')
    start_button = col2.button('START')

    # Images left, right and title background
    st.image('Streamlit/pages/mealmuse_images/circleobjectleft.png')
    st.image('Streamlit/pages/mealmuse_images/circleobjectright.png')
    st.image('Streamlit/pages/mealmuse_images/centerobjects.png')



    # filtered_df = pd.read_parquet('df.parquet.gzip')

    # ingredient1 = filtered_df['ingredient1'].str.strip("'")
    # ingredient2 = filtered_df['ingredient2'].str.strip("'")
    # verified_pairings = set(zip(ingredient1, ingredient2))


    # start button styles#
    st.markdown("""
    <style>
    div.stButton {
            text-align:center;
                }
    </style>""", unsafe_allow_html=True)

    st.markdown("""
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button{
            background-color: #FEBA21;
            border-radius: 12px;
            cursor: pointer;
            padding: 10px 15px;
            text-align: center;
            transition: 200ms;
            width: 50%;
            box-sizing: border-box;
            border: 0;
            touch-action: manipulation;
            }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button:not(:disabled):hover,
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button:not(:disabled):focus{
            outline: 0;
            background: #D94F00;
            box-shadow: 0 0 0 2px rgba(0,0,0,.2), 0 3px 8px 0 rgba(0,0,0,.15);
            }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button:not(:disabled):disabled{
            filter: saturate(0.2) opacity(0.5);
            -webkit-filter: saturate(0.2) opacity(0.5);
            cursor: not-allowed;
            }

        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button > div > p{
            color: white;
            font-size: 20px;
            font-weight: bold;
            }
    </style>""", unsafe_allow_html=True)

    # left background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(2) > div > div{
            position: fixed;
            left: 0px;
            bottom: 0px;

    }
    </style>""", unsafe_allow_html=True)

    # right background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(3) > div > div{
        position: fixed;
        right: -65px;
        bottom: 0px;
    }
    </style>""", unsafe_allow_html=True)

    # center background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(4) > div > div{
        position: absolute;
        left:0px;
        top:-700px;
        }
    </style>""", unsafe_allow_html=True)

    if start_button:
        st.session_state['page2'] = True
        st.session_state['page1'] = False
        st.experimental_rerun()


# st.session_state['verified_pairings'] = verified_pairings

if st.session_state['page2']:
    col1, col2, col3 = st.columns([1, 4, 1])
    # Mealmuse header

    col2.markdown("<h1 style='text-align: center; color: black; font-size:60px'>Mealmuse</h1>", unsafe_allow_html=True)
    # Mealmuse subheader (Turn What..)
    col2.markdown("<h2 style='text-align: center; color: grey; font-size:20px'>Turn What You Have to What You Crave &#128512; </h2>", unsafe_allow_html=True)
    #col2.markdown("<h3 style='text-align: center; color: black; font-size:10px'>Enter Your Ingredients</h3>", unsafe_allow_html=True)

    st.session_state['ingredients'] = col2.text_input('', help='Enter the list of ingredients:')

    evaluate_button = col2.button('Recipes Muse')

    col2.markdown("<h3 style='text-align: center; color: grey; font-size:20px'>An AI-powered recipe generator that utilizes Machine Learning to offer customized cooking suggestions based on avalable ingredients</h3>", unsafe_allow_html=True)

    st.image('Streamlit/pages/mealmuse_images/circleobjectleft.png')
    st.image('Streamlit/pages/mealmuse_images/circleobjectright.png')
    st.image('Streamlit/pages/mealmuse_images/centerobjects.png')

    # evaluate button #
    st.markdown("""
    <style>
    div.stButton {
            text-align:center;
                }
    </style>""", unsafe_allow_html=True)

    st.markdown("""
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button{
            background-color: #FEBA21;
            border-radius: 12px;
            cursor: pointer;
            padding: 10px 15px;
            text-align: center;
            transition: 200ms;
            width: 50%;
            box-sizing: border-box;
            border: 0;
            touch-action: manipulation;
            }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button:not(:disabled):hover,
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button:not(:disabled):focus{
            outline: 0;
            background: #D94F00;
            box-shadow: 0 0 0 2px rgba(0,0,0,.2), 0 3px 8px 0 rgba(0,0,0,.15);
            }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button:not(:disabled):disabled{
            filter: saturate(0.2) opacity(0.5);
            -webkit-filter: saturate(0.2) opacity(0.5);
            cursor: not-allowed;
            }

        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(4) > div > button > div > p{
            color: white;
            font-size: 20px;
            font-weight: bold;
            }
    </style>""", unsafe_allow_html=True)



     # left background image styles

    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(2) > div > div{
            position: fixed;
            left: 0px;
            bottom: 0px;

    }
    </style>""", unsafe_allow_html=True)

     # right background image styles

    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(3) > div > div{
        position: fixed;
        right: -65px;
        bottom: 0px;
    }
    </style>""", unsafe_allow_html=True)

     # center background image styles

    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(4) > div > div{
        position: absolute;
        left:0px;
        top:-550px;
        }
    </style>""", unsafe_allow_html=True)



    #main paragraph at the middle

    st.markdown("""
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(5) > div{
        padding-top: 40px;
    }
    </style>""", unsafe_allow_html=True)

    #footer
    st.markdown("""
        <style>
        .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: black;
        text-align: center;
        }
        </style>
        <div class="footer">
        <p>Developed with ❤️ by <a style='display: block; text-align: center;' href="https://github.com/annaloanlin/Mealmuse-Workspace.git" target="_blank">Mealmuse Team</a></p>
        </div>
        </style>""", unsafe_allow_html=True)

    if evaluate_button:
        st.session_state['page3'] = True
        st.session_state['page2'] = False
        st.experimental_rerun()



if st.session_state['page3']:



    col1, col2, col3 = st.columns([1, 4, 1])
    # Mealmuse header

    col2.markdown("<h1 style='text-align: center; color: black; font-size:60px'>Mealmuse</h1>", unsafe_allow_html=True)
    # Mealmuse subheader (Turn What..)
    col2.markdown("<h2 style='text-align: center; color: grey; font-size:20px'>Turn What You Have to What You Crave &#128512; </h2>", unsafe_allow_html=True)
    #col2.markdown("<h3 style='text-align: center; color: black; font-size:10px'>Enter Your Ingredients</h3>", unsafe_allow_html=True)

    st.image('Streamlit/pages/mealmuse_images/circleobjectleft.png')
    st.image('Streamlit/pages/mealmuse_images/circleobjectright.png')
    st.image('Streamlit/pages/mealmuse_images/centerobjects.png')

    @st.cache_data
    def get_model():
        with open("model.pickle", "rb") as f:
            model = pickle.load(f)
        return model

    model = get_model()

    # set user input as ingredients
    ingredients = st.session_state['ingredients']
     # candidates = 3 ingredient combinations and their scores
    verified_pairings = st.session_state['verified_pairings']
    candidates = find_top_3_groups(ingredients, verified_pairings)
    # print(candidates)
    # re-assign ingredient pairings to new variable:
    st.session_state['scored_ingredients'] = candidates

    # old version
    # contents, titles, ingredients, scores = [], [], [], []  ##<==== changed the variables a bit so the variables below will not be affected
    # # st.session_state['scored_ingredients'] = ingredient combinations and scores
    # for ing in st.session_state['scored_ingredients']:
    #     # recipe = full chatgpt output, unmodified
    #     recipe = prompt_muse(ing)
    #     # title, ing, content = info parsed from chatgpt output
    #     title, ing, content = get_recipe_info(recipe)
    #     # contents = recipe instructions
    #     contents.append(content) # content = from get_recipe_info func
    #     # ingredients = recipe ingredients
    #     ingredients.append(ing) # ing = from get_recipe_info func
    #     # titles = recipe titles
    #     titles.append(title) #
    #     scores.append(model.predict_proba(contents))
    #     # evaluate the recipe generated by chatgpt and output the final recipes
    #     final_recipe = final_recipes(recipe, scores) ##<===added the regenerator and reassigned the titles, ingredients, and contents variables to reflect the final recipes
    #     titles = final_recipe["Title"]
    # st.write(final_recipe)
    #     ingredients = final_recipe["Ingredients"]
    #     contents = final_recipe["Instructions"]

    contents, titles, ingredients = [], [], []
    contents1, titles1, ingredients1, scores = [], [], [], []  ##<==== changed the variables a bit so the variables below will not be affected
    # st.session_state['scored_ingredients'] = ingredient combinations and scores


    # st.write(st.session_state['scored_ingredients'])
    for ing in st.session_state['scored_ingredients']:

        # recipe = full chatgpt output, unmodified
        recipe = prompt_muse(ing)
        # title, ing, content = info parsed from chatgpt output
        title, ing, content = get_recipe_info(recipe)

        # contents = recipe instructions
        contents1.append(content) # content = from get_recipe_info func
        # ingredients = recipe ingredients
        ingredients1.append(ing) # ing = from get_recipe_info func
        # titles = recipe titles
        titles1.append(title) #
        scores.append(model.predict_proba([content])[0][1])
        # evaluate the recipe generated by chatgpt and output the final recipes
        print(scores)
    recipe_dict = {'Title': titles1, 'Ingredients': ingredients1, 'Instructions': contents1}
    final_recipe = final_recipes(recipe_dict, scores, model) ##<===added the regenerator and reassigned the titles, ingredients, and contents variables to reflect the final recipes
    titles.append(final_recipe["Title"])
    ingredients.append(final_recipe["Ingredients"])
    contents.append(final_recipe["Instructions"])


    # re-assigning variables to fit page switch format
    # not necessary but keeping for simplicity
    st.session_state['titles'] = titles[0]
    st.session_state['ingredients'] = ingredients[0]
    st.session_state['instructions'] = contents[0]

    # Model predicts probabilities:
    st.session_state['scores'] = scores
    # st.session_state['scores'] = model.predict_proba(contents)
    # carrying over variables from previous page and re-assigning
    # not necessary but keeping for simplicity
    # titles = RECIPE TITLE. variable not being used below...?
    #------titles = st.session_state['titles']
    # scores = RECIPE EVALUATION SCORE. variable not being used below...?
    #---------scores = st.session_state['scores']





    # left background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(2) > div > div{
            position: fixed;
            left: 0px;
            bottom: 0px;

    }
    </style>""", unsafe_allow_html=True)

    # right background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(3) > div > div{
        position: fixed;
        right: -65px;
        bottom: 0px;
    }
    </style>""", unsafe_allow_html=True)

    # center background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(4) > div > div{
        position: absolute;
        left:0px;
        top:-250px;
        }
    </style>""", unsafe_allow_html=True)


    img_list = []
    for title in st.session_state['titles']:
        if title != None:
            img = imagegen(title)
            img_list.append(img['data'][0]['url'])

    with st.container():

        dishes = [f'Dish {n+1}' for n in range(len(st.session_state['ingredients']))]
        for index, tab in enumerate(st.tabs(dishes)):


            with tab:
                st.subheader(st.session_state['titles'][index])

                col1, col2, col3 = st.columns([1, 2, 1])
                with col1:
                    st.subheader('Ingredients')
                    if index < len(st.session_state['ingredients']):
                        st.write(st.session_state['ingredients'][index])
                with col2:
                    st.subheader('Instructions')
                    if index < len(st.session_state['instructions']):
                        st.write(st.session_state['instructions'][index])
                with col3:
                    st.subheader('Image')
                    if index < len(img_list):
                        st.image(img_list[index], width=200)


    # tab styles
    st.markdown("""
    <style>
        .stTabs [data-baseweb="tab-list"] {
            gap: 2px;
        }

        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: #FEBA21;
            border-radius: 999px;
            gap: 1px;
            color: white;
            padding: 10px 20px 10px 20px;
        }

        .stTabs [aria-selected="true"] {
            background-color: #D94F00;
        }

        .stTabs [data-baseweb="tab-highlight"] {
            background-color: transparent;
        }

        #tabs-bui2-tab-0 > div > p {
            color: white;
            font-size: 15px;
            font-weight: bold;
            }
        #tabs-bui2-tab-1 > div > p {
            color: white;
            font-size: 15px;
            font-weight: bold;
            }
        #tabs-bui2-tab-2 > div > p {
            color: white;
            font-size: 15px;
            font-weight: bold;
            }
        #tabs-bui4-tabpanel-0 > div > div > div > div > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div > img{
            border-radius: 30px;
            -webkit-filter: drop-shadow(12px 12px 7px rgba(217,79,0,0.5));
            }
        #tabs-bui4-tabpanel-1 > div > div > div > div > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div > img{
            border-radius: 30px;
            -webkit-filter: drop-shadow(12px 12px 7px rgba(217,79,0,0.5));
            }
        #tabs-bui4-tabpanel-2 > div > div > div > div > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div > img{
            border-radius: 30px;
            -webkit-filter: drop-shadow(12px 12px 7px rgba(217,79,0,0.5));
            }
    </style>""", unsafe_allow_html=True)

    #footer
    st.markdown("""
        <style>
        .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: black;
        text-align: center;
        }
        </style>
        <div class="footer">
        <p>Developed with ❤️ by <a style='display: block; text-align: center;' href="https://github.com/annaloanlin/Mealmuse-Workspace.git" target="_blank">Mealmuse Team</a></p>
        </div>
        </style>""", unsafe_allow_html=True)
