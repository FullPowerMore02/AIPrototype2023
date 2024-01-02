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

import subprocess

if __name__ == "__main__":
    subprocess.run(['ls', '-ltr'])
    subprocess.run(['rm', '-r', '/home/Pongpicha/testfolder1'], errors='ignore')

    # ระบุตำแหน่งที่มีเลข
    position_90 = 3
    position_minus_90 = 4
    position_0 = 5

    # วนลูปผ่านคำสั่งและดึงผลลัพธ์
    numbers = []
    for command in [
        ['python3', 'testpy.py', '--num', '100', '--XX', '90'],
        ['python3', 'testpy.py', '--num', '10', '--XX', '-90'],
        ['python3', 'testpy.py', '--num', '0', '--XX', '7']
    ]:
        output = subprocess.run(command, stdout=subprocess.PIPE, text=True).stdout
        # ตรวจสอบและดึงตัวเลขจากผลลัพธ์
        number = [int(word) for word in output.split() if word.isdigit()]
        if number:
            numbers.append(number[0])

    # พิมพ์ตำแหน่งของเลข 90, -90, และ 0
    print(f"Position of 90: {numbers[position_90 - 1]}")
    print(f"Position of -90: {numbers[position_minus_90 - 1]}")
    print(f"Position of 0: {numbers[position_0 - 1]}")






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

