import streamlit as st

# Set page session states
if 'page1' not in st.session_state:
    st.session_state['page1'] = True
if 'page2' not in st.session_state:
    st.session_state['page2'] = False
if 'page3' not in st.session_state:
    st.session_state['page3'] = False








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

    # CSS to position the background images
    css = """
    <style>
        .left-image {
            position: fixed;
            left: 0;
            bottom: 0;
            max-width: 200px;
        }
        .right-image {
            position: fixed;
            right: 0;
            bottom: 0;
            max-width: 200px;
        }
        .center-image {
            position: absolute;
            left: 50%;
            top: -700px;
            transform: translateX(-50%);
            max-width: 800px;
        }
    </style>
    """

    # Display background images with CSS
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(f'<img src="mealmuse_images/circleobjectleft.png" class="left-image">', unsafe_allow_html=True)
    st.markdown(f'<img src="mealmuse_images/circleobjectright.png" class="right-image">', unsafe_allow_html=True)
    st.markdown(f'<img src="mealmuse_images/centerobjects.png" class="center-image">', unsafe_allow_html=True)

    # Start button styles
    # ... (existing start button styles)










# images show but in wrong place

# if st.session_state['page1']:
#     # Set columns for page 1
#     col1, col2, col3 = st.columns([1, 4, 1])

#     # Mealmuse header
#     col2.markdown("<h1 style='text-align: center; color: black; font-size:60px'>Mealmuse</h1>", unsafe_allow_html=True)

#     # Mealmuse subheader (Turn What..)
#     col2.markdown("<h2 style='text-align: center; color: grey; font-size:20px'>Turn What You have to What You Crave &#128512; </h2>", unsafe_allow_html=True)

#     # Set center image
#     col2.image('mealmuse_images/people4.png')
#     start_button = col2.button('START')

#     # Display background images
#     col1.image('mealmuse_images/circleobjectleft.png', use_column_width=True)
#     col3.image('mealmuse_images/circleobjectright.png', use_column_width=True)
#     col2.image('mealmuse_images/centerobjects.png', use_column_width=True)

#     # Start button styles
#     # ... (existing start button styles)










# images don't show but seem to be in right place

# # CSS to hold the background images
# page1_css = f"""
#     <style>
#         .background-image-container {{
#             position: relative;
#         }}
#         .background-image-left {{
#             position: absolute;
#             left: 0;
#             bottom: 0;
#         }}
#         .background-image-right {{
#             position: absolute;
#             right: 0;
#             bottom: 0;
#         }}
#         .background-image-center {{
#             position: absolute;
#             left: 50%;
#             top: -700px;
#             transform: translateX(-50%);
#         }}
#     </style>
# """

# if st.session_state['page1']:
#     # Set columns for page 1
#     col1, col2, col3 = st.columns([1, 4, 1])

#     # Mealmuse header
#     col2.markdown("<h1 style='text-align: center; color: black; font-size:60px'>Mealmuse</h1>", unsafe_allow_html=True)

#     # Mealmuse subheader (Turn What..)
#     col2.markdown("<h2 style='text-align: center; color: grey; font-size:20px'>Turn What You have to What You Crave &#128512; </h2>", unsafe_allow_html=True)

#     # Set center image
#     col2.image('mealmuse_images/people4.png')
#     start_button = col2.button('START')

#     # Display background images
#     st.markdown(page1_css, unsafe_allow_html=True)

#     # Create a container for background images
#     background_image_container = st.container()
#     with background_image_container:
#         st.markdown("""
#             <div class="background-image-container">
#                 <img src="mealmuse_images/circleobjectleft.png" class="background-image-left">
#                 <img src="mealmuse_images/circleobjectright.png" class="background-image-right">
#                 <img src="mealmuse_images/centerobjects.png" class="background-image-center">
#             </div>
#         """, unsafe_allow_html=True)

#     # Start button styles
#     # ... (existing start button styles)







# # images don't show but seem to be in right place

# # CSS to hold the background images and images
# page1_css = f"""
#     <style>
#         .background-image-left {{
#             position: fixed;
#             left: 0;
#             bottom: 0;
#         }}
#         .background-image-right {{
#             position: fixed;
#             right: 0;
#             bottom: 0;
#         }}
#         .background-image-center {{
#             position: absolute;
#             left: 50%;
#             top: -700px;
#             transform: translateX(-50%);
#         }}
#     </style>
#     <img src="mealmuse_images/circleobjectleft.png" class="background-image-left">
#     <img src="mealmuse_images/circleobjectright.png" class="background-image-right">
#     <img src="mealmuse_images/centerobjects.png" class="background-image-center">
# """

# if st.session_state['page1']:
#     # Set columns for page 1
#     col1, col2, col3 = st.columns([1, 4, 1])

#     # Mealmuse header
#     col2.markdown("<h1 style='text-align: center; color: black; font-size:60px'>Mealmuse</h1>", unsafe_allow_html=True)

#     # Mealmuse subheader (Turn What..)
#     col2.markdown("<h2 style='text-align: center; color: grey; font-size:20px'>Turn What You have to What You Crave &#128512; </h2>", unsafe_allow_html=True)

#     # Set center image
#     col2.image('mealmuse_images/people4.png')
#     start_button = col2.button('START')

#     # Display background images
#     st.markdown(page1_css, unsafe_allow_html=True)

#     # Start button styles
#     # ... (existing start button styles)

# ##################################
