import streamlit as st
#変数の用意
#学内所属の変数
#attribute_interior_var=("教員","職員","学生","その他")
#学外所属の変数
#attribute_exterior_var=("高校生","観光","その他")
#所属の変数
attribute_var = ("教員(学内)","職員(学内)","学生(学内)","高校生","観光","その他")
#来校目的
visiting_purposes_var=("通勤・通学","散歩","オープンキャンパス","観光","その他")


title = st.title("写真投稿フォーム")

with st.form("upload_form"):
  name_input = st.text_input("ニックネーム")
  
  post_date_input = st.date_input("投稿日")
  
  attribute_exterior_input = st.radio("所属を教えて下さい",attribute_var)
  
  visiting_purposes_input = st.multiselect("来校の目的を教えて下さい(複数回答可)",visiting_purposes_var)
  
  upload_photo = st.file_uploader("お気に入りの一枚")
  
  st.text_input("写真を撮った場所を教えて下さい")
  
  st.text_area("お気に入りの理由を教えて下さい")

  st.form_submit_button("送信")
