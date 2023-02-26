import streamlit as st
import time

st.title('streamlit 超入門')

#画像を表示させる方法
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}') #フォーマット構文
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input('あなたの趣味はなんですか？')
# st.write('あなたの趣味は',text ,'です。')

# condition = st.slider('How is it going?', 0, 100, 50)
# st.write('condition:', condition)

#インタラクティブなウィジェットはcheckbox, selectbox, text_input

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )
# st.write('あなたの好きな数字は', option, 'です。')


# if st.checkbox('Show Image'):
#     img = Image.open('square_kaede.jpg')
#     st.image(img, caption='kaede SUTO', use_column_width=True)



# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

#mapを表示させる方法
# st.map(df)

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

#st.write(df)でもst.dataframe(df)でもどちらでも書ける。
#st.table()でもいけるただし、dataframeと違って、静的なフレームフィルタなどがない。
#dataframeはサイズなどの引数を持っている。
# st.dataframe(df.style.highlight_max(axis=0))

# Magic Command
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """


