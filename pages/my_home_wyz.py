import streamlit as st;
from PIL import Image;

page=st.sidebar.radio("我的主页",["图片处理",'我的留言区','摆烂区（音乐）','我的兴趣推荐','词典']);
st.write("欢迎回来！");
st.image("ClassIn_20240124175410.jpeg");

def page_1():
    #xq
    st.write("王某某喜欢的电影");
    st.write('');
    st.write("王某某喜欢的食物");
    st.write("");
    st.write("王某某喜欢的饮料");
    st.write("");
    st.write("王某某喜欢的游戏");
    st.write("None");
    
def page_2():
    #ly
    st.write("恶语伤人心，注意文明用语哦！！！");
    with open('leave_messages.txt','r',encoding="utf-8")as f:
        message_list=f.read().split('\n');
    for i in range(len(message_list)):
        message_list[i]=message_list[i].split("#");
    for i in message_list:
        if i[1]=='编程猫':
            with st.chat_message("😸"):
                st.write(i[1],":",i[2]);
        elif i[1]=='阿短':
            with st.chat_message("🤠"):
                st.write(i[1],":",i[2]);
    name=st.selectbox("I'm...",["阿短","编程猫"]);
    new_message=st.text_input("what want say");
    if st.button('留言'):
        message_list.append([str(int(message_list[-1][0])+1),name,new_message]);
        with open("leave_messages.txt",'w',encoding='utf-8')as f:
            message='';
            for i in message_list:
                message+=i[0]+"#"+i[1]+"#"+i[2]+"\n";
            message=message[:-1];
            f.write(message);
    
def page_3():
    #音乐
    music=st.file_uploader("上传音乐文件",type=['mp3','wma','wav','asf','aac','vqf','flac','ape','mid']);
    st.audio(music);
def page_4():
    st.write(":sunglasses:上传图片:sunglasses:");
    #tp
    uploaded_file=st.file_uploader("上传图片",type=['png','jpeg','jpg','tif','jfif']);
    if uploaded_file:
        file_name=uploaded_file.name;
        file_type=uploaded_file.type;
        file_size=uploaded_file.size;
        img=Image.open(uploaded_file);
        tap1,tap2,tap3,tap4=st.tabs(['原图','2','3','4']);
        with tap1:
            st.image(image_change(img,0,1,2));

        with tap2:
            st.image(image_change(img,0,2,1));
        
        with tap3:
            st.image(image_change(img,1,2,0));
        
        with tap4:
            st.image(image_change(img,1,0,2));
def image_change(img,rc,gc,bc):
    width,height=img.size;
    img_array=img.load();
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc];
            g=img_array[x,y][gc];
            b=img_array[x,y][bc];
            img_array[x,y]=(r,g,b);
    return img;

def page_5():
    st.write("智能词典");
    with open('words_space.txt','r',encoding='utf-8') as f:
        word_list=f.read().split("\n");
    for i in range(len(word_list)):
        word_list[i]=word_list[i].split('#');
    word_diction={};
    for i in word_list:
        word_diction[i[1]]=[int(i[0]),i[2]];
    with open("cx_t.txt", 'r',encoding='utf-8') as f:
        time_list=f.read().split('\n');
    for i in range(len(time_list)):
        time_list[i]=time_list[i].split('#');
    time_dict={};
    for i in time_list:
        time_dict[int(i[0])]=int(i[1]);
    word = st.text_input('请输入要查询的单词');
    if word in word_diction:
        st.write(word_diction[word]);
        n=word_diction[word][0];
        if n in time_dict:
            time_dict[n]+=1;
        else:
            time_dict[n]=1;
            with open('cx_t.txt','w',encoding='utf-8')as f:
                message ='';
                for k,v in time_dict.items():
                    message+=str(k)+"#"+str(v)+"\n";
                message=message[:-1];
                f.write(message);
        st.write('查询次数',time_dict[n]);
    else:
        st.write("I'm sorry,I don't have this word");
    if word=="python":
       st.code("print('你好！干嘛喊我？')") ;
    if word=='snow':
        st.snow();
    if word=='balloon':
        st.balloons();
    
    
if page=='我的留言区':
    page_2();
if page=='摆烂区（音乐）':
    page_3();
if page=='我的兴趣推荐':
    page_1();
if page=='图片处理':
    page_4();
if page=="词典":
    page_5();
