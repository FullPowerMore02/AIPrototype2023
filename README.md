# AIPrototype2023
Webpage

https://fullpowermore02.github.io/

Webapp


AI Prototype Class1

Cloud Computing คืออะไร
ทุกอย่างเป็นระบบคลาวด์ที่เราสามารถใช้ได้หากเราเข้าสู่ระบบอินเทอร์เน็ต

ประเภทของ Cloud Computing

Cloud
-IaaS : ระบบพื้นฐาน : Hardware on Cloud : IasS+ PasS → VM (Virtual Machine เราเช่าเครื่องของเขา)

-PasS: : Platform as a Service : Database ซื้อ → Add Data

-SaaS : Software as a Service : เราคือคนใช้งาน application ex. word, excel, google sheet 

Benifits of Cloud
-Cost : บริษัทสามารถ Manage ได้ใช้นานแค่ไหน ไม่จำ เป็นต้องซื้อ Computer ทั้งหมด ซื้อแค่ที่เราใช้

-Productivity : จ่ายเงินเพื่อให้คนเก่งมาพัฒนาและดูแลโดยคนเก่ง, อะไรที่ไม่จำ เป็นต้องโฟกัสก็ซื้อ

-Compliance : สามารถเข้ากับข้อตกลงของบริษัทได้ (มี Certificate)

-Only Web Browser Needed : Can use cloud
Precautions

-Always Change

-Require the internet :

-Paradigm Shift (Service Based) : รู้จัก Base Computer เพื่อใช้เกี่ยวกับ Cloud

-Everything is on the Internet

ls = List every file in folder 

pwd = Where is our folder 

mkdir (...) = Create folder (Name) 

Cd (name_folder) = Change Directory ... 

Cd (..) = Step back 1 step Cd = go to home 
rm = remove

rm -R = remove folder

vi (file_name) = create file

  
in vi file

 if press I = insert everything like word 

 wq = save file
  
ls -ltr 

cp = ./file1 ./teste1_1 = copy

file1 to folder test1_1 

mv = เปลี่ยนชื่อไฟล์ 

mv ~ = ย้าย






Code start after this

1.) mkdir testfolder1

2.) cd test_folder1

3.) mkdir testfolder1_1

4.) cd test_folder1_1

5.) mkdir testfoler1_1_1

6.) cd test_folder1_1_1 (ตอนนี้จะอยู่โฟลเดอร์นี้)
7.) vi file1 (สร้างไฟล์)

in vi file1

ในไฟล์ file1 ให้กดปุ่ม I แล้วพิม print(world)แล้วกด ESC -> พิมพ์ wq

wq = save file

8.)ls (เช็คว่าว่ มีไฟล์ file1 ไหม)

9.)cp ./file1 ./testfolder1_1/testfolder1_1_1./.

--------------------------------------------

AI Prototype Class 2

Create Virtual Machine 

1. portal azure 

a. Virtual Machine 

b. Resource group = Folder Collect Service 

c. in terminal

ssh pongpicha@ip #connect cloud 

password ********** 

exit #out VM 

htop = check process 

sudo chmod 755 username #set group user and other 

7=host read write excute, 5 = group read excute, 5 = other read excute

2. Scp File 
scp -r testfolder1/ pongpicha@ip # folder -> pc to cloud 
scp pongpicha@ip:/home/pongpicha/file.. ~/. #file -> Cloud to pc

Azure Cloud Shell 

Shell is on internet it make our connect easy 

1. upload file → it install in my pc 

2. Scp file to Cloud VM 

File type 

r = 4 read 

w = 2 write 

x = 1 execute ( run )

Python miniconda
https://docs.anaconda.com/free/miniconda/

--------------------------------------------

AI Prototype Class 3

sudo = install for everyone 

if want install something for only one should create enviorment 

Create enviorment 

conda create -n myenv python=3.9 #-n (name)= new 
enviorment name 

conda activate mypy38 # use this ev 

conda deactiveate # exit ev

Create Jupyter notebook 

conda install notebook #install 

jupyter notebook #Use notebook

Notebook on Cloud

ต้องการใช้ web ในเครื่องที่อยู่บน Cloud ใช้คำสั่ง screen 

ถ้าปิดหรือเน็ตหลุด section จะหาย

screen -S (name) #start Screen 

screen -S sc1 

cltr+A D # ตัดตัวเองออกจาก Screen = detech from screen 

screen -R (name) #Retech 

screen -R sc1 

screen -ls # check how many screen right now 

cltr+A k y = delte screen

Screen Notebook

#create notebook 

scree -s notebook 

jupyter notebook 

ssh -L 8866:localhost:8888 nattakonpu@ip 

(สร้าร้ง link port 8866 map to 8888 เครื่อง nattakonpu@ip)

Github on linux 

git config --global user.name "..." 

git config --global user.email "..." 

git clone https://github.com/.../AIPrototype2023.git 

Vi Readme.md# Can config readme file 

Ctrl wq = exit = quite write 

Ctrl q! = exit = quite no write git status # ดูว่า 
ไฟล์ไหนแก้ไขไปบ้าง 

git add # upfile to github 

git commit -m*add myname* # บอกว่าว่ แก้อะไร

--------------------------------------------
AI Prototype Class 4

Step this week 

1. in folder ubuntu → folder AIPrototype66 

2. code testpy.py # สร้าง folder 

3. Ctrl + S #ได้ไฟล์ py ที่เราเขียน

#Step after create file.py git pull # 

ก่อนตลอดก่อนเริ่มแก้โค้ด เรียกให้ อัพเดท code 

git status # Check

git add (filename) 

git commit -m "..." 

git push 

#upload file to github on internet

4. In vm : folder code → AI

git pull # เรียกเวอร์ชันล่าสุด 

python (filename)

argparse : รับรู้ input ข้างนอก 

import argparse 

def parse_input():

    parser = argparse.ArgumentParser() 
    parser.add_argument('--num', type=int, required=True, 
    help='input for the multiplyby9 function')
    parser.add_argument('--XX', type=int, default=7, help='input for the multiplyby9 function')
    args = parser.parse_args() 
    return args 

def printhello():

    print("hello world")

def multiplyby9(input_V):
    print(9 * input_V)

if __name__ == "__main__":
    # โปรแกรมหลัก

    input_V = parse_input()
    print(f'The input XX is {input_V.XX}')  # รับค่า
    print("We are in the main function")
    multiplyby9(input_V.num)
    printhello()

1. Import package : argparse : รับรั input ข้างนอก 

2. Create function parse_input ( ให้รับตัวแปรตอนเรารัน 
python 

1. num = จำ เป็นต้องใส่เป็นตัวเลข 

2. xx = ไม่จำเป็นต้องใส่ ถ้าใส่จะเป็นเลข ถ้าไม่ใส่จะเป็น “7” 

3. function hello word 
4. function การคูณ a. 9*(input) (xx=ตัวเลขที่ใส่ไม่ใส่ =7) 
5. main function (flow follow after this) เริ่มริ่ จาก รับรั ค่าตัวแปร input_V = parse_input() {function} print(the input xx i (ค่าตัวแปร x ไม่มีก็=7) print("we are in the main function") function การคูณ 9*ตัวแปร x print(”hello”) function 
3 รอบ 1,2 เลขอะไรก็ได้ 
3 แค่ num
--------------------------------------------
AI Prototype Class 9+10

Deep Learning 

input = image ( This class) Theory 

1. Classical 

  → แปลงให้อยู่ในรูป Vector → ชุดของตัวเลข {x1,x2,x3,…,xn} 

  → data is feature vector have n dimension 

2. Deep Learning 

→ Feature engineering 

→ Histogram of Oriented Gradients 

→ Image 

→ Sobel filter 

→ Gx, Gy = ค่ามาก = แนวตั้ง, ค่าน้อย = ไม่ตั้ง

6.7.1เพร์เซฟตรอน เป็นข่ายงานประสาทแบบง่ายมีหน่วยเดียว
 
x = feateur 

w =weight
 
 
ผลรวมของ sum > 0 จะผ่าน activation function → output = 1 แต่ค่าจริงริๆ = 0 

ผลรวมของ sum < 0 จะผ่าน avtivation function → output = 0

Fully connected / Dense layer 

Input Node ขึ้นอยู่กับ feature = n 

Input Node → layer 1 → layer 2 → output
 
 

: max pooling = สรุปเฉพาะจุดเด่น 

activation function = กำหนดค่าที่ไปคูณให้อยู่ใน range 

ต้องการ

Soble filter 

Binary cross entropy loss
 
→ for Many Class



