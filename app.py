import streamlit as st
from utils.functions import combinations_of_two, data_query, get_scores, get_final_recipes, muse_comb, recipe_generator, image_generator
import pandas as pd
import pickle





#--------------------

# Set page session states
if 'page1' not in st.session_state:
    st.session_state['page1'] = True
if 'page2' not in st.session_state:
    st.session_state['page2'] = False
if 'page3' not in st.session_state:
    st.session_state['page3'] = False


# ##############################################################
# 1 Title Page
# ##############################################################

if st.session_state['page1']:

    # Set columns for page 1
    col1, col2, col3 = st.columns([1, 4, 1])

    # Mealmuse header
    col2.markdown("<h1 style='text-align: center; color: black; font-size:60px'>Mealmuse</h1>", unsafe_allow_html=True)

    # Mealmuse subheader (Turn What..)
    col2.markdown("<h2 style='text-align: center; color: grey; font-size:20px'>Turn What You have to What You Crave &#128512; </h2>", unsafe_allow_html=True)

    # Set center image
    col2.image('mealmuse_images/people4.png')
    start_button = col2.button('START')

    # # Images left, right and title background
    # st.image('mealmuse_images/circleobjectleft.png')
    # st.image('mealmuse_images/circleobjectright.png')
    # st.image('mealmuse_images/centerobjects.png')

    ########## experimenting ################


# Inject CSS for styling

    st.markdown("""
        <style>
        .left-img {
            position: fixed;
            left: 0px;
            bottom: 0px;
        }
        </style>
    """, unsafe_allow_html=True)

    # # Verify HTML with CSS class
    # st.markdown('<img src="mealmuse_images/circleobjectleft.png" class="left-img">', unsafe_allow_html=True)


######################################




    # Start button styles
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





# original ##############################################################

    # # left background image styles
    # st.markdown("""
    # <style>
    #     #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(2) > div > div{
    #         position: fixed;
    #         left: 0px;
    #         bottom: 0px;
    # }
    # </style>""", unsafe_allow_html=True)

    # # right background image styles
    # st.markdown("""
    # <style>
    #     #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(3) > div > div{
    #     position: fixed;
    #     right: -65px;
    #     bottom: 0px;
    # }
    # </style>""", unsafe_allow_html=True)

    # center background image styles
    st.markdown("""
    <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(4) > div > div{
        position: absolute;
        left:0px;
        top:-700px;
        }
    </style>""", unsafe_allow_html=True)

    # original ##############################################################

    # Go to page 2
    if start_button:
        st.session_state['page2'] = True
        st.session_state['page1'] = False
        st.rerun()



# ##############################################################
# 2 Input Page
# Takes user input and sends it as-is to Output Page.
# ##############################################################

if st.session_state['page2']:

    # Set columns for page 2
    col1, col2, col3 = st.columns([1, 4, 1])

    # Mealmuse header
    col2.markdown("<h1 style='text-align: center; color: black; font-size:60px'>Mealmuse</h1>", unsafe_allow_html=True)
    # Mealmuse subheader (Turn What..)
    col2.markdown("<h2 style='text-align: center; color: grey; font-size:20px'>Turn What You have to What You Crave &#128512; </h2>", unsafe_allow_html=True)


    st.session_state['ingredients'] = col2.text_input('', help='Enter your list of ingredients, separated by commas:')

    evaluate_button = col2.button('Recipes Muse')

    col2.markdown("<h3 style='text-align: center; color: grey; font-size:20px'>An AI-powered recipe generator that utilizes Machine Learning to offer customized cooking suggestions based on available ingredients</h3>", unsafe_allow_html=True)

    # # Images left, right and title background
    # st.image('mealmuse_images/circleobjectleft.png')
    # st.image('mealmuse_images/circleobjectright.png')
    # st.image('mealmuse_images/centerobjects.png')

    # evaluate button
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



    #  # left background image styles
    # st.markdown("""
    # <style>
    #     #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(2) > div > div{
    #         position: fixed;
    #         left: 0px;
    #         bottom: 0px;

    # }
    # </style>""", unsafe_allow_html=True)

    #  # right background image styles
    # st.markdown("""
    # <style>
    #     #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(3) > div > div{
    #     position: fixed;
    #     right: -65px;
    #     bottom: 0px;
    # }
    # </style>""", unsafe_allow_html=True)

    # #  center background image styles
    # st.markdown("""
    # <style>
    #     #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(4) > div > div{
    #     position: absolute;
    #     left:0px;
    #     top:-550px;
    #     }
    # </style>""", unsafe_allow_html=True)



    # main paragraph at the middle
    st.markdown("""
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div.st-emotion-cache-115gedg.e1f1d6gn3 > div > div > div > div:nth-child(5) > div{
        padding-top: 40px;
    }
    </style>""", unsafe_allow_html=True)

    # footer
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

    # Go to page 3
    if evaluate_button:
        st.session_state['page3'] = True
        st.session_state['page2'] = False
        st.rerun()




# ##############################################################
# 3 Output Page
# Takes user input as a string from Input Page.
# Outputs ingredients, instructions, and image.
# Compatibility functions and the model are here.
# ##############################################################


if st.session_state['page3']:

    col1, col2, col3 = st.columns([1, 4, 1])
    # Mealmuse header

    col2.markdown("<h1 style='text-align: center; color: black; font-size:60px'>Mealmuse</h1>", unsafe_allow_html=True)
    # Mealmuse subheader (Turn What..)
    col2.markdown("<h2 style='text-align: center; color: grey; font-size:20px'>Turn What You Have to What You Crave &#128512; </h2>", unsafe_allow_html=True)
    #col2.markdown("<h3 style='text-align: center; color: black; font-size:10px'>Enter Your Ingredients</h3>", unsafe_allow_html=True)

    # st.image('Streamlit/pages/mealmuse_images/circleobjectleft.png')
    # st.image('Streamlit/pages/mealmuse_images/circleobjectright.png')
    # st.image('Streamlit/pages/mealmuse_images/centerobjects.png')

    @st.cache_data
    def get_model():
        with open("utils/model.pickle", "rb") as f:
            model = pickle.load(f)
        return model

    # Initiate the model
    model = get_model()

    # Load the dataframe
    df = pd.read_parquet('data/Halved-DF.parquet.gzip')



    # Set user input as ingredients_input (bring from page 2 in st.session_state format)
    ingredients_input = st.session_state['ingredients']


    # Function calls

    ingredients_combinations = combinations_of_two(ingredients_input)
    # ingredients_combinations = list containing tuples and lists

    df_comb = data_query(ingredients_combinations)
    # df_comb = datafrome with 2 columns: 'Combination' and 'Score'

    ingredients_list = muse_comb(df_comb)
    # ingredients_list = list of 3 lists

    recipe_list = recipe_generator(ingredients_list)
    # recipe_list = list of 3 dictionaries

    scores = get_scores(recipe_list)
    # scores = list of 3 integers

    final_recipes = get_final_recipes(recipe_list, scores, model)
    # final_recipes = 1 dictionary with 3 keys:
    #     'title': list of 3 strings, each string containing recipe title
    #     'ingredients': list of 3 strings, each string containing recipe ingredients
    #     'directions': list of 3 strings, each string containing recipe directions





    # # Columns
    # col1, col2, col3 = st.columns([1, 4, 1])

    # # Mealmuse header
    # col2.markdown("<h1 style='text-align: center; color: black; font-size:60px'>Mealmuse</h1>", unsafe_allow_html=True)
    # # Mealmuse subheader (Turn What..)
    # col2.markdown("<h2 style='text-align: center; color: grey; font-size:20px'>Turn What You have to What You Crave &#128512; </h2>", unsafe_allow_html=True)
    # #col2.markdown("<h3 style='text-align: center; color: black; font-size:10px'>Enter Your Ingredients</h3>", unsafe_allow_html=True)

    # # Background images
    # st.image('mealmuse_images/circleobjectleft.png')
    # st.image('mealmuse_images/circleobjectright.png')
    # st.image('mealmuse_images/centerobjects.png')

    # # left background image styles
    # st.markdown("""
    # <style>
    #     #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(2) > div > div{
    #         position: fixed;
    #         left: 0px;
    #         bottom: 0px;

    # }
    # </style>""", unsafe_allow_html=True)

    # # right background image styles
    # st.markdown("""
    # <style>
    #     #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(3) > div > div{
    #     position: fixed;
    #     right: -65px;
    #     bottom: 0px;
    # }
    # </style>""", unsafe_allow_html=True)

    # # center background image styles
    # st.markdown("""
    # <style>
    #     #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(4) > div > div{
    #     position: absolute;
    #     left:0px;
    #     top:-250px;
    #     }
    # </style>""", unsafe_allow_html=True)






    with st.container():

        dishes = [f'Dish {n+1}' for n in range(len(final_recipes['title']))]

        placeholders = []
        for index, tab in enumerate(st.tabs(dishes)):

            with tab:
                st.subheader(final_recipes['title'][index])

                col1, col2, col3 = st.columns([1, 2, 1])
                with col1:
                    st.subheader('Ingredients')
                    if index < len(final_recipes['ingredients']):
                        st.write(final_recipes['ingredients'][index])
                with col2:
                    st.subheader('Directions')
                    if index < len(final_recipes['directions']):
                        st.write(final_recipes['directions'][index])
                placeholder = col3.empty()
                placeholders.append(placeholder)

        # image_urls -> list of 3 strings, each string containing image url
        for index, placeholder in enumerate(placeholders):
            with placeholder:
                with st.spinner('Loading images...'):
                    image_urls = image_generator(final_recipes)
                    print('image_urls:', image_urls)
                    st.subheader('Image')
                    if index < len(image_urls):
                        st.image(image_urls[index], width=200)


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
