# Beck_Suicide_Scale
贝克自杀意念量表的gui，该脚本能够实现在线收集自杀意念量表数据，并将有自杀意念的问卷结果一份保存到本地，一份发送到设定的邮箱

该程序基于stmp、tkinter、pandas开发，需要联网使用，可在.py文件中自己设置发件人邮箱和收件人邮箱。如需打包请自行使用pyinstaller，打包代码已放入pyinstaller.txt。
程序打开后会自行进行联网检测
![屏幕截图 2023-03-26 213922](https://user-images.githubusercontent.com/67633648/227779706-af3e2ba1-4fe4-45ec-8850-6dd047374239.png)

输入姓名、性别、编号等基本信息后会自动进入gui
![屏幕截图 2023-03-26 214009](https://user-images.githubusercontent.com/67633648/227779750-095555c9-55bd-43a1-bc08-381895e86ebb.png)

有自杀意念量表数据可通过网络发送到指定邮箱，实现结果在线收集
![屏幕截图 2023-03-26 214726](https://user-images.githubusercontent.com/67633648/227780172-cbf499ca-d5fe-4d9a-a353-0076d4306068.png)
![屏幕截图 2023-03-26 214752](https://user-images.githubusercontent.com/67633648/227780189-56450665-05cd-4ca0-b1e9-11ad01ce3414.png)
