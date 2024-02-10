#import subprocess

#if __name__ == "__main__" :
     #   subprocess.run(['ls','-ltr'])
     #   subprocess.run(['rm','-r','/home/Pongpicha/testfolder1'])
    #   subprocess.run(['python3','testpy.py','--num','100','--XX','90'])
   #     subprocess.run(['python3','testpy.py','--num','10','--XX','-90'])
  #      subprocess.run(['python3','testpy.py','--num','0','--XX','7'])

 #       process_output = subprocess.Popen("python","firstpy.py","--num","0")
    
        ######
#import subprocess



###
import subprocess #สำหรับรัน terminal command

def print_():
    print("-----------------------------------------")
if __name__ == "__main__":
    #basic terminal command
    subprocess.run(["ls","-ltr"])
    print("first run num=100 XX=90")
    subprocess.run(["python", "testpy.py", "--num", "100","--XX", "90"])
    print_()
    print("second run num=-10 XX=-90")
    subprocess.run(["python", "testpy.py", "--num", "-10","--XX", "-90"])
    print_()
    print("third run num=0")
    subprocess.run(["python", "testpy.py", "--num", "0"])
    print_()
 

#use output from other program
process_output = subprocess.Popen(["python", "testpy.py", "--num", "0"],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
out, err = process_output.communicate()
print(out.decode('utf-8'))
print(len(out.decode('utf-8')))

##HW เขียน subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน hello world!)

sum_output = 0

output1 = subprocess.check_output(["python", "testpy.py", "--num", "100", "--XX", "90"]).decode('utf-8')
value1 = int(output1.split('\n')[3]) 
sum_output += value1

output2 = subprocess.check_output(["python", "testpy.py", "--num", "-10", "--XX", "-90"]).decode('utf-8')
value2 = int(output2.split('\n')[3])  
sum_output += value2

output3 = subprocess.check_output(["python", "testpy.py", "--num", "0"]).decode('utf-8')
value3 = int(output3.split('\n')[3])  
sum_output += value3

print("sum output")
print(sum_output)



    # Extract the last numbers from each command and convert to integers
    #last_command_first_two_numbers = [int(command[i]) for i in range(2)]

    # Extract the last two numbers from each command and convert to integers
    #last_two_numbers = [int(command[-2]) for command in commands]

    # Sum up the values and print the total result
    #total_result = sum(last_two_numbers + last_command_first_two_numbers)
    #print(f"The total result is: {total_result}")
    #results = [run_and_capture_output(command) for command in commands]

    # Sum up the values and print the total result
   # total_result = sum(results)
  #  print(f"The total result is: {total_result}")


#if __name__ == "__main__":
    #subprocess.run(['ls', '-ltr'])
   # subprocess.run(['rm', '-r', '/home/Pongpicha/testfolder1'])

#import subprocess

#def run_and_capture_output(command):
    # รัน subprocess และดึงข้อมูล output
 #   output = subprocess.check_output(command).decode()

    # ตรวจสอบว่า '--num' อยู่ใน output หรือไม่
  #  if '--num' in output:
        # แยกข้อมูลที่ต้องการ (เลือกตัวเลขที่ตำแหน่ง --num)
   #     num_value = int(output.strip().split('--num')[-1])
    #    return num_value
   # else:
        # กรณีที่ไม่พบ '--num' ใน output
    #    print("Error: '--num' not found in output.")
     #   return None

#if __name__ == "__main__":
    # กำหนดคำสั่ง subprocess
 #   commands = [
  #      ['python3', 'testpy.py', '--num', '100', '--XX', '90'],
   #     ['python3', 'testpy.py', '--num', '10', '--XX', '-90'],
    #    ['python3', 'testpy.py', '--num', '0', '--XX', '7']
   # ]

    # สร้างรายการผลลัพธ์จากการรัน subprocess
   # results = [run_and_capture_output(command) for command in commands]

    # แสดงผลลัพธ์
    print(f"The results are: {results}")

