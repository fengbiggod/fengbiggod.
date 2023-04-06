import streamlit as st
import time

st.title('异地恋情侣小调查')

with st.expander(''):
     
     st.write('有人说，异地恋是爱情最快乐的想象。')
     st.write('也有人说，爱终究会因为距离消失。')
     st.write('异地恋有多大的概率能熬到最好的结局？')
     st.write('这份调查分析是对你末来或者正在进行的异地恋分手的预警分析。')
     st.write('你也可以将它看作对你过去某段异地恋的回顾。')
     st.write('如果触碰到伤疤,无意冒犯。')
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.0001)
     my_bar.progress(percent_complete + 1)

st.balloons()

st.write('调查小背景：此网页收集整理了一系列关于异地恋的数据，试图找出异地恋之间的共同点和如何避免在异地恋之中的一些小问题，并做了一个有关异地恋分手的概率测试')

st.write('采用问卷调查所收集的数据，很好的采纳了不同年龄段的人群，各自对异地恋的看法，使数据呈现出一个的较为准确的结果。所用模型：随机森林。')

st.title('经历异地恋的次数')

import streamlit as st
import matplotlib.pyplot as plt
fig = plt.figure()
label=['one twice','two twice','three twice','four twice and more']
explode=[0.01,0.01,0.01,0.01]
value=[62.5,25,9.6,2.9]
plt.pie(value, explode=explode,labels=label, autopct='%1.1f%%')
plt.show()
st.pyplot(fig)

st.title('经历异地恋的时间')

import streamlit as st
import matplotlib.pyplot as plt
fig = plt.figure()
label=['0-6month','6-12month','1-3year','3year and more']
explode=[0.01,0.01,0.01,0.01]
value=[25,21.9,32.9,20.2]
plt.pie(value, explode=explode,labels=label, autopct='%1.1f%%')
plt.title('How long have we been talking about long-distance relationships')
plt.show()
st.pyplot(fig)

st.title('异地恋成功的概率')

import streamlit as st
import matplotlib.pyplot as plt
fig = plt.figure()
label=['success','fail']
explode=[0.01,0.01]
value=[70.6,29.4]
plt.pie(value, explode=explode,labels=label, autopct='%1.1f%%')
plt.show()
st.pyplot(fig)

import streamlit as st
st.header('异地恋分手概率测试')
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
import streamlit as st
st.write('1.性别')
a=st.button('男')
b=st.button('女')
if a or b: 
 df = pd.DataFrame({
     '性别': ['男','女'],
     '比例': ['32.1%', '67.9%']
     })
 st.write(df)

import streamlit as st
st.write ('2.您和您的恋人的距离')
icecream = st.checkbox('跨城')
coffee = st.checkbox('跨省')
cola= st.checkbox('跨国')
if icecream or coffee or cola: 
 st.write('距离数据')
 df = pd.DataFrame({
     '距离': ['跨城','跨省','跨国'],
     '比例': ['24.4%', '68.9%', '17.0%']
     })
 st.write(df)

import streamlit as st
st.write ('3.您和您的恋人的见面频率')
icecream = st.checkbox('0-1个月')
coffee = st.checkbox('1-6个月')
cola= st.checkbox('6个月-1年')
xuebi= st.checkbox('1年以上')
if icecream or coffee or cola or xuebi: 
 st.write('见面频率')
 df = pd.DataFrame({
     '时间': ['0-1个月','1-6个月','6-12个月','12个月以上'],
     '总体比例': ['13.6%','63.6%', '20.5%', '2.3%']
     })
 st.write(df)


import streamlit as st
st.write('4.您和您恋人目前的矛盾')
options = st.multiselect(
    '矛盾分类',
    ['累了，看不到未来', '性格不合适', '家庭问题','激情退却', '变心','没有安全感','其它'])
st.write('您的矛盾是:', options)
if options:
  df = pd.DataFrame({
     '时间': ['累了，看不到未来', '性格不合适', '家庭问题','激情退却', '变心','没有安全感','其它'],
     '总体比例': ['32.9%','16.5%', '7%', '5.9%','18.2%','8.9%', '10.6%']
     })
  st.write(df)

import streamlit as st
a=st.button('提交')
if a: 
 df = pd.DataFrame({
     '异地结果': ['未分手','已分手'],
     '比例': ['70.6%', '29.4%']
     })
 st.write(df)

import streamlit as st
st.write('异地恋真的很辛苦，希望携手坚持到现在的你们，')
st.write ('不要因为一时的距离和一些细枝末节，而疏忽了这个本该相守一生的人。')
st.write ('等下次见面，请给他（她）一个大大的拥抱吧！')