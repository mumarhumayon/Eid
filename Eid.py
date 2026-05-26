import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Eman 🌙",
    page_icon="🌙",
    layout="centered"
)

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>

body {
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #141e30, #243b55);
    font-family: Arial, sans-serif;
    color: white;
}

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 95vh;
}

.card {
    width: 80%;
    max-width: 700px;
    background: rgba(255,255,255,0.08);
    padding: 45px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.35);
}

.name {
    font-size: 72px;
    font-weight: bold;
    background: linear-gradient(to right, #ff4d6d, #ff85a1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 15px;
}

.eid {
    font-size: 28px;
    margin-bottom: 25px;
    color: #ffffff;
}

.message {
    font-size: 21px;
    line-height: 1.9;
    color: #f2f2f2;
}

</style>
</head>

<body>

<div class="container">

    <div class="card">

        <div class="name">
            Eman ✨
        </div>

        <div class="eid">
            Eid Mubarak 🌙✨
        </div>

        <div class="message">

            May this Eid bring peace to your heart, softness to your thoughts,
            and beautiful moments that quietly heal and brighten your days.
            Wishing you genuine happiness, inner calm,
            and many reasons to smile in the days ahead 🤍

        </div>

    </div>

</div>

</body>
</html>
"""

components.html(html_code, height=700)
