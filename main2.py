import streamlit as st
from PIL import Image
import time

st.title('何がくるかな')

#画像を表示させる方法
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'おらおらいくぞー!! {i+1}') #フォーマット構文
    bar.progress(i+1)
    time.sleep(0.1)

time.sleep(0.2)

'どどん!!!!'
img = Image.open('kurumiCat.jpg')
st.image(img, caption='かわいいねこだよ', use_column_width=True)