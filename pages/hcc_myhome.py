'''我的主页'''
import streamlit as st
from PIL import Image

page=st.sidebar.radio('科比的首页',['科比的兴趣推荐','科比的图片处理工具','科比的智能词典','科比的留言区','科比的BMI'])

def page_1():
    '''科比的兴趣推荐'''
    st.title('科比的电影推荐：')
    st.write('《速度与激情》')
    st.title('科比的书籍推荐：')
    st.write('《科比传》')
    st.title('科比的衣服推荐：')
    st.write('24号紫金球衣')
    st.title('科比的运动推荐：')
    st.write('打篮球》')

def page_2():
    '''科比的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses")
    uploaded_file=st.file_uploader('上传图片',type=['jpg','png','jpeg'])
    if uploaded_file:
        #获取图片文件的名称、类型和大小
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,0,2,1))
        tab1,tab2,tab3,tab4=st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img_change(img,0,1,2))
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
        
            
def page_3():
    '''科比的智能词典'''
    st.write('智障词典')
    #从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    #将列表中的每一项内容进行分割，分为“编号，单词，解释”
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    #将列表中的内容导入词典，方便查询，格式为“单词：序号‘解释”
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]

    with open('check_out_times.txt','r',encoding='utf-8')as f:
        times_list=f.read().split('\n')

    #将列表转为字典
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    #创建输入框
    word=st.text_input('请输入您要查询的单词：')
    #显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open('check_out_times','w',encoding='utf-8')as f:
            message=''
            for k,v in times_dict.items():
                message+=str(k)+'#'+str(v)+'\n'
            message=message[:-1]
            f.write(message)
        st.write('查询次数',times_dict[n])
        
    if word=='python':
        st.code('看来你很喜欢学python啊')
    if word=='Kobe'or word=='kobe':
        st.balloons()
        st.write('SEE YOU AGAIN')

def page_4():
    '''科比的留言区'''
    st.write('我的留言区')
    #从文件中加载内容，并处理成列表
    with open('leave_messages.txt','r',encoding='utf-8')as f:
        messages_list=f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split('#')
    for i in messages_list:
        if i[1]=='阿短':
            with st.chat_message('💯'):
                st.write(i[1],":",i[2])
        elif i[1]=='编程猫':
            with st.chat_message('🌞'):
                st.write(i[1],":",i[2])
    name=st.selectbox('我是......',['阿短','编程猫'])
    new_message=st.text_input('想要说的话')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_meaasges.txt','w',encoding='utf-8')as f:
            message=''
            for i in messages_list:
                message+=i[0]+'#'+i[1]+'#'+i[2]+'\n'
            message=message[:-1]
            f.write(message)

def page_5():
    '''科比的BMI'''
    weight=st.slider('体重(kg)：',1.0,200.0,0.1)
    height=st.slider('身高(m)：',0.0,2.5,0.01)

    w=weight/(height**2)
    st.write('你的BMI为',w)
    if w<18.5:
        st.title('你的体重太轻了！快多吃点东西吧！')
    elif 18.5<=w and w<24:
        st.title('你的体重刚刚好！继续保持哦~')
    elif 24<=w and w<28:
        st.title('你处于微胖状态','保持健康的生活习惯，相信你可以瘦下去的')
    elif 28<=w and w<32:
        st.title('你处于肥胖状态，','保持健康的生活习惯，相信你可以瘦下去的')
    elif w>32:
        st.title('你太胖了！快点减肥吧！')
def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            #获取RGB值
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img

if page=='科比的兴趣推荐':
    page_1()
elif page=='科比的图片处理工具':
    page_2()
elif page=='科比的智能词典':
    page_3()
elif page=='科比的留言区':
    page_4()
elif page=='科比的BMI':
    page_5()