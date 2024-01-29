import streamlit as st
from PIL import Image
import time, random
guide = ['main page', 'my photo dealing tools', 'my intelligent dictionary', 'my replying area', 'number guessing game', 'video made by me']
page = st.sidebar.radio('my head page', guide)
def img_change(img, indexes):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            xaxis = [0, 0, 0]
            xaxis[0] = img_array[x, y][0]
            xaxis[1] = img_array[x, y][1]
            xaxis[2] = img_array[x, y][2]
            img_array[x, y] = (xaxis[indexes[0]], xaxis[indexes[1]], xaxis[indexes[2]])
    return img
def page_1():
    st.title('Welcome to my website!')
    st.write('have you ever made a website? No? I am equivalent to you!That means, this is my first website.')
    st.write('the website was made in 7 days and it might have many mistakes.if you hane some good ideas, please sent it to me!i would appreciate your advice.')
    st.write('---------------------------------------')
    st.write('I have made a main page to show what can you do on this website.')
    st.write('page 2:you can load a page and change its RGB data.maybe you will find a beautiful world.')
    st.write('page 3:a dictionary is built in here.it has about 8,000 different words.you can look it up anytime you want.')
    st.write('page 4:have a conversation here!you can sent a lot of massages if you want.')
    st.write('page 5:playing a mental games here.try how high score you can get!it does not as easy as it looks.')
    st.write('page 6')
    st.write('"Untitled" has made some videos for you to look.i beg you can not watch it till the end.I make sure it is amazing.')
    st.write('---------------------------------------')
    st.write('choose a tab you interestied in to explore this website!')
def page_2():
    st.write('physics experiment for junior high')
    up_file = st.file_uploader('upload the picture', type = ['png', 'jpg', 'jpeg'])
    if up_file:
        f_name = up_file.name
        f_type = up_file.type
        f_size = up_file.size
        img = Image.open(up_file)
        st.write('orgrian')
        st.image(img)
        tab1, tab2, tab3 = st.tabs(['RBG', 'BGR', 'GBR'])
        with tab1:
            st.image(img_change(img, [0, 2, 1]))
        with tab2:
            st.image(img_change(img, [2, 1, 0]))
        with tab3:
            st.image(img_change(img, [1, 2, 0]))
def page_3():
    st.write('physics experiment for junior high')
    with open('___.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n') 
    di = {}
    words_diet = {}
    for i in words_list:
        j = i.split('#')
        di[j[1]] = [int(j[0]), j[2]]
        words_diet[j[1]] = int(j[0])
    #st.write(str(di))
    wd = st.text_input('please input the word you want to look up:')
    if wd in di:
        with open('check_out_times.txt', 'r', encoding = 'utf-8') as ff:
            times_list = ff.read().split('\n')
        times_dict = {}
        for i in range(len(times_list)):
            times_list[i] = times_list[i].split('#')
            times_dict[int(times_list[i][0])] = int(times_list[i][1])
        st.write(':sunglasses:word founded:')
        num = di[wd][0]
        st.write('word number:' + str(num))
        st.write('word meaning:' + str(di[wd][1]))
        if num in times_dict:
            times_dict[num] += 1
        else:
            times_dict[num] = 1
        with open('check_out_times.txt', 'w', encoding = 'utf-8') as fff:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            fff.write(message)
        st.write(str(times_dict))
        st.write('time of you look it up:' + str(times_dict[num]))
        st.write('if you want to look more words up, click the tab again.')
        if st.checkbox('learn more'):
            st.write('learn more:')
        else:
            st.write('tap the checkbox above can show 20 new words.(except it reaches the end of the dictionary)')
    else:
        st.write('OH NO!word does not found.')
        st.write('try retyping this word by click the tab again.')
def page_4():
    st.write('physics experiment for junior high')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('A'):
                st.write(i[1], ":", i[2])
        elif i[1] == '编程猫':
            with st.chat_message('B'):
                st.write(i[1], ':', i[2])
    name = st.selectbox('i am__', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话__')
    if st.button('reply'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding = 'utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + "#" + i[1] + "#" + i[2] +'\n'
            message = message[:-1]
            f.write(message)
def page_5():
    st.write('welcome to my number guessing game!you can select 4 diffierent difficulties oh here.than click the restart button to begin the game with the new difficulty.')
    selection = st.radio('select difficulty', ['easy', 'medium', 'hard', 'very hard'], captions = ['number from 1 to 100', 'number from 1 to 1000', 'number from 1 to 10000', 'number from 1 to 1048575'])
    st.write('game rules:')
    st.write('after the game starts you have a few chance to guess a certain random number(int form) in a certain range(the range of it just according to the game difficulty).you can try your best to input the correct number in these chances.and if once you inputed, i will tell you whether the number is big, small or just correct.the less chances you used in the game, the more score you are gived. every time you guess new numbers, click the affirm button.')
    if st.button('restart'):
        if selection == 'easy':
            number = random.randint(1, 100)
            max_choice = 8
            diff = 1
        if selection == 'medium':
            number = random.randint(1, 1000)
            max_choice = 11
            diff = 3
        if selection == 'hard':
            number = random.randint(1, 10000)
            max_choice = 13
            diff = 5
        if selection == 'very hard':
            number = random.randint(1, 1048575)
            max_choice = 20
            diff = 12
        line = str(str(number) + ',' + str(max_choice) + ',' + str(max_choice) + ',' + str(diff))
        with open('texting.txt', 'w', encoding='utf-8') as f:
           f.write(line)
    guess = -1
    st.write('___________NOW START____________')
    guess = st.text_input('input a number and press ENTER.if you make sure the number you wanna guess, click the affirm button to coutiune.')
    lefting = st.progress(100, 'lest chances')
    with open('texting.txt', 'r', encoding='utf-8') as f:
        line = f.read()
        line = line.split(',')
        number = int(line[0])
        max_choice = int(line[1])
        choice = int(line[2])
        diff = int(line[3])
    st.write(str(choice) + ' chances left.')
    lefting.progress(round(100 * (choice / max_choice)), 'left chances')
    aff = st.button('affirm')
    if aff and choice > 0:
        try:
            guess = int(guess)
        except:
            guess = -1
            st.write('OH NO! IT SEEMS THAT YOU HAVE INPUTED A WRONG NUMBER.TRY AGAIN.')
        if guess != -1:
            guess = int(guess)
            choice -= 1
            line = str(str(number) + ',' + str(max_choice) + ',' + str(choice) + ',' + str(diff))
            with open('texting.txt', 'w', encoding='utf-8') as f:
                f.write(line)
            if guess < number:
                st.write('Hmmm:the number you guess is too SMALL.try again!')
            elif guess > number:
                st.write('Hmmm:the number you guess is too BIG.try again!')
            elif guess == number:
                scored = (2 ** choice) * diff
                st.write('Wow!complete correct!You are amazing and winning the game!here is the score you earn:' + str(scored))
                lefting.progress(0, 'Well Done!')
    if choice <= 0:
        st.write('no chances left.GAME OVER!the correct number is ' + str(number) +'.good luck next time!To restart, tap the restart button above.')
def page_6():
    st.write('Hi there!there are a few videos made by "Untitled".')
    st.write('#listening to the music made by a gread 9 junior high school student.')
    st.link_button('watch it now', 'https://www.bilibili.com/video/BV1284y1m7aa/?spm_id_from=333.999.0.0')
    st.write('#watch the full experiment in junior high school physics textbooks.')
    st.link_button('watch it now', 'https://www.bilibili.com/video/BV1zw411a7YD/?spm_id_from=333.999.0.0')
    st.write('more videos cooming soon!')
if page == guide[0]:
    page_1()
elif page == guide[1]:
    page_2()
elif page == guide[2]:
    page_3()
elif page == guide[3]:
    page_4()
elif page == guide[4]:
    page_5()
elif page == guide[5]:
    page_6()