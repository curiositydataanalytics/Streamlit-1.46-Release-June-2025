import pandas as pd
import streamlit as st
import pydeck as pdk

# App config
#----------------------------------------------------------------------------------------------------------------------------------#
# Page config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(
    """
    <style>
    img[data-testid="stLogo"] {
                height: 6rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("What's new in Streamlit 1.46 ?")
st.divider()

with st.sidebar:
    st.logo('https://raw.githubusercontent.com/curiositydataanalytics/Integrate-a-PyDeck-map-into-Streamlit-using-Python-Tutorial/refs/heads/main/CDA_logo_2025_grey.png', size='large')
    st.empty()
#
#

def page1():
    st.header(':one: st.navigation')
    st.code('''
pg = st.navigation([st.Page(page1, title='st.navigation'),
                    st.Page(page2, title='st.context'),
                    st.Page(page3, title='nesting'),
                    st.Page(page4, title='st.columns'),
                    st.Page(page5, title='st.pydeck_chart')],
                    position='top')
pg.run()
''')



def page2():
    st.header(':two: st.context')

    st.code('''st.context.theme
''')
    st.context.theme


def page3():
    st.header(':three: nesting')
    cols = st.columns(2)
    cols[0].subheader('Streamlit 1.45')
    cols[0].code('''cols = st.columns(2)
# Level 1
with cols[0]:
    st.write('Col-1')
    # Level 2
    subcols = cols[0].columns(2)
    with subcols[0]:
        st.write('Col-1.1')
    with subcols[1]:
        st.write('Col-1.2')
with cols[1]:
    st.write('Col-2')
    # Level 2
    subcols = cols[1].columns(2)
    with subcols[0]:
        st.write('Col-2.1')
    with subcols[1]:
        st.write('Col-2.2')

''')
    
    subcols = cols[0].columns(2)
    with subcols[0]:
        st.write('Col-1')
        subsubcols = subcols[0].columns(2)
        with subsubcols[0]:
            st.write('Col-1.1')
        with subsubcols[1]:
            st.write('Col-1.2')
    with subcols[1]:
        st.write('Col-2')
        subsubcols = subcols[1].columns(2)
        with subsubcols[0]:
            st.write('Col-2.1')
        with subsubcols[1]:
            st.write('Col-2.2')


    cols[1].subheader('Streamlit 1.46')

    cols[1].code('''
cols = st.columns(2)
with cols[0]:
    st.write('Col-1')
    subcols = cols[0].columns(2)
    with subcols[0]:
        st.write('Col-1.1')
        subsubcols = subcols[0].columns(2)
        with subsubcols[0]:
            st.write('Col-1.1.1')
        with subsubcols[1]:
            st.write('Col-1.1.2')
    with subcols[1]:
        st.write('Col-1.2')
        subsubsubcols = subcols[1].columns(2)
        with subsubcols[0]:
            st.write('Col-1.2.1')
        with subsubcols[1]:
            st.write('Col-1.2.2')
with cols[1]:
    st.write('Col-2')
    subcols = cols[1].columns(2)
    with subcols[0]:
        st.write('Col-2.1')
        subsubcols = subcols[0].columns(2)
        with subsubcols[0]:
            st.write('Col-2.1.1')
        with subsubcols[1]:
            st.write('Col-2.1.2')
    with subcols[1]:
        st.write('Col-2.2')
        subsubcols = subcols[1].columns(2)
        with subsubcols[0]:
            st.write('Col-2.2.1')
        with subsubcols[1]:
            st.write('Col-2.2.2')
''')

    subcols = cols[1].columns(2)
    with subcols[0]:
        st.write('Col-1')
        subsubcols = subcols[0].columns(2)
        with subsubcols[0]:
            st.write('Col-1.1')
            subsubsubcols = subsubcols[0].columns(2)
            with subsubsubcols[0]:
                st.write('Col-1.1.1')
            with subsubsubcols[1]:
                st.write('Col-1.1.2')
        with subsubcols[1]:
            st.write('Col-1.2')
            subsubsubcols = subsubcols[1].columns(2)
            with subsubsubcols[0]:
                st.write('Col-1.2.1')
            with subsubsubcols[1]:
                st.write('Col-1.2.2')
    with subcols[1]:
        st.write('Col-2')
        subsubcols = subcols[1].columns(2)
        with subsubcols[0]:
            st.write('Col-2.1')
            subsubsubcols = subsubcols[0].columns(2)
            with subsubsubcols[0]:
                st.write('Col-2.1.1')
            with subsubsubcols[1]:
                st.write('Col-2.1.2')
        with subsubcols[1]:
            st.write('Col-2.2')
            subsubsubcols = subsubcols[1].columns(2)
            with subsubsubcols[0]:
                st.write('Col-2.2.1')
            with subsubsubcols[1]:
                st.write('Col-2.2.2')




def page4():
    st.header(':four: st.columns')

    cols = st.columns(2)
    cols[0].subheader('Streamlit 1.45')

    cols[0].code('''cols = st.columns(3, gap='small')
    cols[0].image('image.png', width=300)
    cols[1].image('image.png', width=300)
    cols[2].image('image.png', width=300)''', wrap_lines=True)

    subcols = cols[0].columns(3, gap='medium')
    subcols[0].image('https://raw.githubusercontent.com/curiositydataanalytics/Integrate-a-PyDeck-map-into-Streamlit-using-Python-Tutorial/refs/heads/main/CDA_logo_2025_grey.png', width=300)
    subcols[1].image('https://raw.githubusercontent.com/curiositydataanalytics/Integrate-a-PyDeck-map-into-Streamlit-using-Python-Tutorial/refs/heads/main/CDA_logo_2025_grey.png', width=300)
    subcols[2].image('https://raw.githubusercontent.com/curiositydataanalytics/Integrate-a-PyDeck-map-into-Streamlit-using-Python-Tutorial/refs/heads/main/CDA_logo_2025_grey.png', width=300)

    cols[1].subheader('Streamlit 1.46')

    cols[1].code('''cols = st.columns(3, gap=None)
    cols[0].image('image.png', width=300)
    cols[1].image('image.png', width=300)
    cols[2].image('image.png', width=300)''', wrap_lines=True)

    subcols = cols[1].columns(3, gap=None)
    subcols[0].image('https://raw.githubusercontent.com/curiositydataanalytics/Integrate-a-PyDeck-map-into-Streamlit-using-Python-Tutorial/refs/heads/main/CDA_logo_2025_grey.png', width=300)
    subcols[1].image('https://raw.githubusercontent.com/curiositydataanalytics/Integrate-a-PyDeck-map-into-Streamlit-using-Python-Tutorial/refs/heads/main/CDA_logo_2025_grey.png', width=300)
    subcols[2].image('https://raw.githubusercontent.com/curiositydataanalytics/Integrate-a-PyDeck-map-into-Streamlit-using-Python-Tutorial/refs/heads/main/CDA_logo_2025_grey.png', width=300)


def page5():
    st.header(':five: st.pydeck_chart')

    cols = st.columns(2)

    import numpy as np
    np.random.seed(42)
    base_lat, base_lon = 37.7749, -122.4194
    data = pd.DataFrame({
        'lat': base_lat + np.random.uniform(-0.03, 0.03, 10),
        'lon': base_lon + np.random.uniform(-0.03, 0.03, 10),
        'label': [f'Point {i+1}' for i in range(10)]
    })

    layer = pdk.Layer(
        'ScatterplotLayer',
        data=data,
        get_position='[lon, lat]',
        get_color='[200, 30, 0, 160]',
        get_radius=100,
    )

    # Define the deck.gl view
    view_state = pdk.ViewState(
        latitude=37.7749,
        longitude=-122.4194,
        zoom=12,
        pitch=0
    )

    cols[0].subheader('st.map')

    cols[0].map(data)

    cols[1].subheader('st.pydeck_chart')

    # Render in Streamlit
    cols[1].pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "{label}"}
    ))


pg = st.navigation([st.Page(page1, title='st.navigation'),
                    st.Page(page2, title='st.context'),
                    st.Page(page3, title='nesting'),
                    st.Page(page4, title='st.columns'),
                    st.Page(page5, title='st.pydeck_chart')],
                    position='top')
pg.run()