import streamlit as st

st.title("👗 プリンセスドレスきせかえ")

st.write("ステキなドレスを作ろう！")

dress_color = st.select_slider(
    "ドレスの色をえらんでね",
    options=["ピンク 💗", "むらさき 💜", "みずいろ 💙", "きいろ 💛", "しろ 🤍"]
)

ribbon = st.radio(
    "リボンはどれ？",
    ["大きいリボン 🎀", "小さいリボン 🎀", "リボンなし"]
)

tiara = st.checkbox("ティアラをつける ✨👑")

if st.button("ドレスかんせい！"):
    st.success("✨ ステキなドレスができたよ！ ✨")
    st.write(f"### 👗 {dress_color} のドレス")
    st.write(f"### 🎀 {ribbon}")
    if tiara:
        st.write("### 👑 キラキラティアラ")
    st.balloons()
    st.write("プリンセスみたい！かわいい！💕")
