"我的主页"
import streamlit as st
from PIL import Image
page=st.sidebar.radio('我的页面',['我的兴趣推荐','我的图片处理器','我的智能词典','我的留言区','网站链接'])
def page_1():
    '''我的兴趣推荐'''
    st.audio('a.mp3')
    st.header('游戏推荐', divider='rainbow')
    st.image('cb63d142a8af64d3109c7bdb3aed7ad0.jpg')
    st.write('《文明6》是Firaxis Games开发，2K Games发行的历史策略回合制游戏，于2016年10月21日发行PC版本，2018年11月16日登陆Switch平台，2019年11月22日发布了XboxOne、PS4版本，为《文明》系列第六部。 游戏中玩家建立起一个帝国，并接受时间的考验。玩家将创建及带领自己的文明从石器时代迈向信息时代，并成为世界的领导者。在尝试建立起世界上赫赫有名的伟大文明的过程中，玩家将启动战争、实行外交、促进文化，同时正面对抗历史上的众多领袖。')
    go = st.selectbox('点击跳转', ['文明6新手教程'])
    if go == '文明6新手教程':
        st.link_button('跳转到'+go, 'https://www.bilibili.com/video/BV1rX4y1n7Fv/?spm_id_from=333.337.search-card.all.click&vd_s')
    
def img_change(img):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][0]
            g = img_array[x, y][1]
            b = img_array[x,y][2]
            img_array[x,y] = (b,g,r)
    return img


def page_2():
    '''我的图片处理器'''
    st.audio('b.mp3')
    st.header(':sunglasses:图片处理小程序:sunglasses:', divider='rainbow')
    upload_file=st.file_uploader('上传图片',type=['png','jpeg','jpg'])
    if upload_file:
        img=Image.open(upload_file)
        st.image(img)
        st.image(img_change(img))
   
    
def page_3():
    '''我的智能词典'''
    st.header('智慧词典', divider='rainbow')
    with open( 'words_space.txt','r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    with open('check out times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
        
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
        times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
        words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        st.write('查询次数',times_dict[n])
    else:
        st.write('找不到')
    with open('check out times.txt','w',encoding='utf-8') as f:
        message = ''
        for k, v in times_dict.items():
            message += str(k) +'#' + str(v) +'\n'
        message = message[:-1]
        f.write(message)
def page_4():
    '''我的留言区'''
    
    st.header('我的留言区', divider='rainbow')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] =='阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] =='编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name=st.selectbox("我是....",['阿短 ，编程猫'])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8 ') as f:       
            message=''           
            for i in messages_list:
                message += i[0] +'#'+ i[1] +'#'+i[2] +'\n'
            message = message[:-1]
            f.write(message)
def page_5():
    '''网站链接'''
    st.link_button('百度首页', 'https://www.baidu.com/')
    st.link_button('点击获得一百万', 'https://www.bilibili.com/video/BV1he4y1w7wB/?spm_id_from=333.337.search-card.all.click&vd_source=78b7a3e66839a58d57d906eb3f6d6d13')
    st.link_button('bilibili', 'https://www.bilibili.com/')
    st.link_button(' ', 'https://www.yuanshen.com/#/')
    st.link_button('听歌', 'https://music.163.com/')
    st.write('----')
    go = st.selectbox('选择想要查看的网页', ['百度', 'bilibili',' ','点击获得一百万','听歌'])
    if go == '点击获得一百万':
        st.link_button('跳转到'+go, 'https://www.bilibili.com/video/BV1he4y1w7wB/?spm_id_from=333.337.search-card.all.click&vd_source=78b7a3e66839a58d57d906eb3f6d6d13')
    elif go == '百度':
        st.link_button('跳转到'+go, 'https://www.baidu.com/')
    elif go =='bilibili':
        st.link_button('跳转到'+go, 'https://www.bilibili.com/')
    elif go ==' ':
        st.link_button('跳转到'+go, 'https://www.yuanshen.com/#/')
    elif go=='听歌':
        st.link_button('跳转到'+go, 'https://music.163.com/')
if page == '我的兴趣推荐':
    page_1()

elif page =='我的图片处理器':
    page_2()

elif  page =='我的智能词典':
    page_3()
elif  page =='我的留言区':
    page_4()
elif page=='网站链接':
    page_5()






