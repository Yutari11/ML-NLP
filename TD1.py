import streamlit as st

st.write("""
# Test of Zipf's Law
This app is used to test the Zipf's Law for three different articles.
""")

articles =  [
        "'Cette question m'agace' : Enora Malagré ferme la porte à un retour sur C8", 
        "Guerre en Ukraine: pourquoi Zelensky accuse la Russie de commettre un 'génocide'",
        "DIRECT. Guerre en Ukraine : la Pologne proteste contre les propos de Zelensky à l'ONU"
        ]

article_selected = st.radio(
    "Choose an article to preview :",
    articles,
    captions = [
        "Publié le 20/09/2023 à 13:54",
        "Publié le 20/09/2023 à 09:52",
        "Publié le 20/09/2023 à 06:40"
        ]
)

article_file = ["article1.txt", "article2.txt", "article3.txt"]
current_article = "article1.txt"
current_article = article_file[articles.index(article_selected)]

with open("articles/" + current_article) as f:
    lines = f.readlines()

st.write("\n".join(lines))
