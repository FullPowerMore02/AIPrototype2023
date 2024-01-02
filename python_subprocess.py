#import subprocess

#if __name__ == "__main__" :
 #       subprocess.run(['ls','-ltr'])
  #      subprocess.run(['rm','-r','/home/Pongpicha/testfolder1'])
   #     subprocess.run(['python','testpy.py','--num','100','--XX','90'])
    #    subprocess.run(['python','testpy.py','--num','10','--XX','-90'])
     #   subprocess.run(['python','testpy.py','--num','0','--XX','7'])

      #  process_output = subprocess.Popen("python","firstpy.py","--num","0")

        ######
import subprocess

def run_and_capture_output(command):
    return int(subprocess.check_output(command).decode())

if __name__ == "__main__":
    subprocess.run(['ls', '-ltr'])
    subprocess.run(['rm', '-r', '/home/Pongpicha/testfolder1'])

    # Define the subprocess commands
    commands = [
        ['python', 'testpy.py', '--num', '100', '--XX', '90'],
        ['python', 'testpy.py', '--num', '10', '--XX', '-90'],
        ['python', 'testpy.py', '--num', '0', '--XX', '7']
    ]

    # Extract the last numbers from each command and convert to integers
    last_numbers = [int(command[-1]) for command in commands]

    # Sum up the values and print the total result
    total_result = sum(last_numbers)
    print(f"The total result is: {total_result}")
    results = [run_and_capture_output(command) for command in commands]

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

