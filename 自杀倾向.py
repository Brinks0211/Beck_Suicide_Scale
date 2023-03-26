# 构建窗口
# coding:utf-8
import smtplib  # smtp服务器
from email.mime.text import MIMEText  # 邮件文本
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sys
import os
import pandas as pd
switch_num = 0


return1 = os.system('ping www.baidu.com')

if return1:
    root0 = tk.Tk()
    root0.title('网络诊断')
    root0.geometry('500x300+200+100')
    root0.resizable(True, True)
    title = tk.Label(root0, text='正在检查是否已连接网络……', font='黑体 20 bold')
    title.place(relx=0.1, rely=0.3)
    title['text'] = '网络尚未连接，请链接后重试'
    btn1 = tk.Button(root0, text='确定', font='黑体 15 bold', width=15, height=2, command=sys.exit)
    btn1.place(relx=0.3, rely=0.5)
    root0.mainloop()
else:
    pass

# 信息录入界面销毁
def destroy():
    global filename, name, name_pin, gender, time
    import time
    name = ent1.get()
    name_pin = ent2.get()
    gender = cb3.get()
    Number = ent4.get()
    time = time.strftime('%Y_%m_%d_%H%M', time.localtime())
    filename = name_pin+'_'+gender+'_'+Number+'_'+time+'.csv'
    root1.destroy()


# 获取当前路径并建立data文件夹
path = os.getcwd()
path = path+'/data'
if os.path.exists(path):
    pass
else:
    os.mkdir(path)

# 信息录入界面
root1 = tk.Tk()
root1.title('问卷信息输入')
root1.geometry('500x300+200+100')
root1.resizable(True, True)
title = tk.Label(root1, text='被试信息填写', font='黑体 20 bold')
title.place(relx=0.3, rely=0.1)
txt1 = tk.Label(root1, text='姓名：', font='黑体 13 bold')
txt2 = tk.Label(root1, text='姓名全拼：', font='黑体 13 bold')
txt3 = tk.Label(root1, text='性别：', font='黑体 13 bold')
txt4 = tk.Label(root1, text='编号：', font='黑体 13 bold')
txt1.place(relx=0.1, rely=0.3)
txt2.place(relx=0.1, rely=0.4)
txt3.place(relx=0.1, rely=0.5)
txt4.place(relx=0.1, rely=0.6)
ent1 = tk.Entry(root1, width=30)
ent2 = tk.Entry(root1, width=30)
var = tk.StringVar()
cb3 = ttk.Combobox(root1, textvariable=var, value=(['male', 'female']), width=28)
ent4 = tk.Entry(root1, width=30)
ent1.place(relx=0.3, rely=0.3)
ent2.place(relx=0.3, rely=0.4)
cb3.place(relx=0.3, rely=0.5)
ent4.place(relx=0.3, rely=0.6)
btn1 = tk.Button(root1, text='确定', font='黑体 15 bold', command=destroy)
btn1.place(relx=0.4, rely=0.8)


# 退出确认
def on_closing():
    if messagebox.askokcancel("Quit", "您想要退出吗"):
        sys.exit()


# 信息录入界面进入循环
root1.protocol('WM_DELETE_WINDOW', on_closing)
root1.mainloop()

data_path = path+'/'+filename
root2 = tk.Tk()
root2.title("贝克自杀意念量表")
root2.geometry('1280x720+100+40')
root2.resizable(True, True)
# 读取量表及选项文件
f_question = open('贝克自杀意念量表.txt', 'r', encoding='utf-8')
questionnaire = f_question.readlines()
f_choice = open('贝克自杀意念量表选项.txt', 'r', encoding='utf-8')
choice = f_choice.readlines()
# 窗口内容呈现
answer_list = []


def btn1_clicked():
    global answer_list, switch_num, choice_list, questionnaire
    answer_list.append(1)
    switch_num += 1
    if switch_num == len(questionnaire):
        root2.destroy()
        root3 = tk.Tk()
        root3.geometry('500x400+400+200')
        thanks = tk.Label(root3, text='感谢您的参与！', font='黑体 15 bold')
        thanks.place(relx=0.3, rely=0.4)
    elif switch_num == 5 and answer_list[3] == 1 and answer_list[4] == 1:
        root2.destroy()
        root3 = tk.Tk()
        root3.geometry('800x400+400+200')
        thanks = tk.Label(root3, text='您没有自杀倾向，感谢您的参与！', font='黑体 20 bold')
        thanks.place(relx=0.3, rely=0.4)
    else:
        question_stm['text'] = '\n'.join(questionnaire[switch_num].split('new'))
        choice_list = choice[switch_num].split('，')
        for index, value in enumerate(choice_list):
            if len(value) > 10:
                contem = list(value)
                contem.insert(10, '\n')
                contem = ''.join(contem)
                choice_list[index] = contem
        choice_stim(choice_list)
        root2.update()


def btn2_clicked():
    global answer_list, switch_num, choice_list, questionnaire
    answer_list.append(2)
    switch_num += 1
    if switch_num == len(questionnaire):
        root2.destroy()
        root3 = tk.Tk()
        root3.geometry('500x400+400+200')
        thanks = tk.Label(root3, text='感谢您的参与！', font='黑体 15 bold')
        thanks.place(relx=0.3, rely=0.4)
    elif switch_num == 5 and answer_list[3] == 1 and answer_list[4] == 1:
        root2.destroy()
        root3 = tk.Tk()
        root3.geometry('800x400+400+200')
        thanks = tk.Label(root3, text='您没有自杀倾向，感谢您的参与！', font='黑体 20 bold')
        thanks.place(relx=0.3, rely=0.4)
    else:
        question_stm['text'] = '\n'.join(questionnaire[switch_num].split('new'))
        choice_list = choice[switch_num].split('，')
        for index, value in enumerate(choice_list):
            if len(value) > 10:
                contem = list(value)
                contem.insert(10, '\n')
                contem = ''.join(contem)
                choice_list[index] = contem
        choice_stim(choice_list)
        root2.update()


def btn3_clicked():
    global answer_list, switch_num, choice_list, questionnaire
    answer_list.append(3)
    switch_num += 1
    if switch_num == len(questionnaire):
        root2.destroy()
        root3 = tk.Tk()
        root3.geometry('500x400+400+200')
        thanks = tk.Label(root3, text='感谢您的参与！', font='黑体 15 bold')
        thanks.place(relx=0.3, rely=0.4)
    elif switch_num == 5 and answer_list[3] == 1 and answer_list[4] == 1:
        root2.destroy()
        root3 = tk.Tk()
        root3.geometry('800x400+400+200')
        thanks = tk.Label(root3, text='您没有自杀倾向，感谢您的参与！', font='黑体 20 bold')
        thanks.place(relx=0.3, rely=0.4)
    else:
        question_stm['text'] = '\n'.join(questionnaire[switch_num].split('new'))
        choice_list = choice[switch_num].split('，')
        for index, value in enumerate(choice_list):
            if len(value) > 10:
                contem = list(value)
                contem.insert(10, '\n')
                contem = ''.join(contem)
                choice_list[index] = contem
        choice_stim(choice_list)
        root2.update()


def btn4_clicked():
    global answer_list, switch_num, choice_list, questionnaire
    answer_list.append(0)
    switch_num += 1
    if switch_num == len(questionnaire):
        root2.destroy()
        root3 = tk.Tk()
        root3.geometry('500x400+400+200')
        thanks = tk.Label(root3, text='感谢您的参与！', font='黑体 15 bold')
        thanks.place(relx=0.3, rely=0.4)
    elif switch_num == 5 and answer_list[3] == 1 and answer_list[4] == 1:
        root2.destroy()
        root3 = tk.Tk()
        root3.geometry('800x400+400+200')
        thanks = tk.Label(root3, text='您没有自杀倾向，感谢您的参与！', font='黑体 20 bold')
        thanks.place(relx=0.3, rely=0.4)
    else:
        question_stm['text'] = '\n'.join(questionnaire[switch_num].split('new'))
        choice_list = choice[switch_num].split('，')
        for index, value in enumerate(choice_list):
            if len(value) > 10:
                contem = list(value)
                contem.insert(10, '\n')
                contem = ''.join(contem)
                choice_list[index] = contem
        choice_stim(choice_list)
        root2.update()


choice_list = choice[switch_num].split('，')
question_stm = tk.Label(root2, justify='left', text='\n'.join(questionnaire[switch_num].split('new')),
                        font='黑体 25 bold')
question_stm.place(relx=0.1, rely=0.2)

def choice_stim(choice_list):
    if len(choice_list) == 3:
        btn1 = tk.Button(root2, text=choice_list[0].strip(), width=20,
                         height=3, font='黑体 15 bold', command=btn1_clicked)
        btn1.place(relx=0.1, rely=0.5)
        root2.update()
        btn2 = tk.Button(root2, text=choice_list[1].strip(), width=20,
                         height=3, font='黑体 15 bold', command=btn2_clicked)
        btn2.place(relx=0.3, rely=0.5)
        root2.update()
        btn3 = tk.Button(root2, text=choice_list[2].strip(), width=20,
                         height=3, font='黑体 15 bold', command=btn3_clicked)
        btn3.place(relx=0.5, rely=0.5)
        root2.update()
        btn4 = tk.Button(root2, width=20,
                         height=3, font='黑体 15 bold')
        btn4.place(relx=0.7, rely=0.5)
        root2.update()
    elif len(choice_list) == 4:
        btn1 = tk.Button(root2, text=choice_list[0].strip(), width=20,
                         height=3, font='黑体 15 bold', command=btn1_clicked)
        btn1.place(relx=0.1, rely=0.5)
        root2.update()
        btn2 = tk.Button(root2, text=choice_list[1].strip(), width=20,
                         height=3, font='黑体 15 bold', command=btn2_clicked)
        btn2.place(relx=0.3, rely=0.5)
        root2.update()
        btn3 = tk.Button(root2, text=choice_list[2].strip(), width=20,
                         height=3, font='黑体 15 bold', command=btn3_clicked)
        btn3.place(relx=0.5, rely=0.5)
        root2.update()
        btn4 = tk.Button(root2, text=choice_list[3].strip(), width=20,
                         height=3, font='黑体 15 bold', command=btn4_clicked)
        btn4.place(relx=0.7, rely=0.5)
        root2.update()
    root2.update()


choice_stim(choice_list)
root2.protocol('WM_DELETE_WINDOW', on_closing)
root2.mainloop()


def data_sum(data, onset, end):
    sum = 0
    for i in data[onset:end]:
        sum += i
    return sum


answer_list.append(data_sum(answer_list, 0, 5))
contem = data_sum(answer_list, 5, 19)
contem = round((contem-9)/33*100, 2)
answer_list.append(contem)
df = pd.DataFrame(columns=['SSI1', 'SSI2', 'SSI3', 'SSI4', 'SSI5', 'SSI6', 'SSI7', 'SSI8', 'SSI9',
                           'SSI10', 'SSI11', 'SSI12', 'SSI13', 'SSI14', 'SSI15', 'SSI16', 'SSI17',
                           'SSI18', 'SSI19', '自杀意念', '自杀危险'], )
for index, value in enumerate(answer_list):
    df.loc[0, df.columns[index]] = value
if answer_list[3] == 1 and answer_list[4] == 1:
    pass
else:
    df.to_csv(data_path, index=False, encoding='gbk')



# 邮件构建

subject = "实验数据"  # 邮件标题
sender = "zhangyihao0211@163.com"  # 发送方邮箱
content = "实验数据文件见附件。"
recver = "1115618265@qq.com"  # 接收方邮箱
password = r"XXXXXXXX"  # 发送方邮箱密码（使用邮箱授权码登录）
message = MIMEMultipart() # content 发送内容     "plain"文本格式   utf-8 编码格式
message['Subject'] = subject  # 邮件标题
message['To'] = recver  # 收件人
message['From'] = sender  # 发件人

# 邮件正文内容
part = MIMEText(content, 'plain', 'utf-8')
message.attach(part)# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEApplication(open(data_path, 'rb').read())
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1.add_header('Content-Disposition', 'attachment', filename=filename)
message.attach(att1)
smtp = smtplib.SMTP_SSL("smtp.163.com", 994)  # 实例化smtp服务器
smtp.login(sender, password)  # 发件人登录
smtp.sendmail(sender, recver, message.as_string())  # as_string 对 message 的消息进行了封装
smtp.close()
# 青少年抑郁、焦虑、睡眠
