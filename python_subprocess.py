import subprocess

if __name__ == "__main__" :
        subprocess.run(['ls','-ltr'])
        subprocess.run(['rm','-r','/home/Pongpicha/testfolder1'])
        subprocess.run(['python','testpy.py','--num','100','--XX','90'])
        subprocess.run(['python','testpy.py','--num','10','--XX','-90'])
        subprocess.run(['python','testpy.py','--num','0','--XX','7'])


        ######