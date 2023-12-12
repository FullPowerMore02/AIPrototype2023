#def printHello() :
 #   print("Hello Woeld")

#def multiplyby9() :
 #   print("Hello Woeld")

#if __name__=="__main__": 
 #   print("we are in the main function2")
  #  multiplyby9(20)
   # printHello()

#import argparse
#def parse_import():
 #   parser = argparse.ArhumentParser()

  #  parser.add_argument(
   #     '-- num'
    #    type=int,
     #   required=True
      #  help='imput for the multiplyby9 function'
    #)
    #args = perser.parse_args()
    #return args
#def printHello():
    #print("Hello World")

#def multiplyby9(inputV):
  #  print(9*inputV)

#if __name__ == "__main__"
   # imput_v = parse_import()
   # print(f'the input num is {input_v.num}')
  #  print('we are in the main function')
 #   multiplyby9(20)
   # printHello()
#import argparse

#def parse_import():
 #   parser = argparse.ArgumentParser()

  ##     '--num',
    #    type=int,
     #   required=True,
      #  help='input for the multiplyby9 function'
    #)
   # args = parser.parse_args()
   # return args

#def printHello():
 #   print("Hello World")

#def multiplyby9(inputV):
 #   print(9 * inputV)
     
#if __name__ == "__main__":
 #   input_v = parse_import()
  #  print(f'the input num is {input_v.num}')
   # print('we are in the main function')
    #multiplyby9(input_v.num)
    #printHello()
import argparse

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--num',
        type=int,
        required=True,
        help='input for the multiplyby9 function'
    )
    parser.add_argument(
        '--XX',
        type=int,
        required=7,
        help='input for XX function'
    )
    args = parser.parse_args()
    return args

def printHello():
    print("Hello World")

def multiplyby9(input_v):
    print(input_v)

if __name__ == "__main__":
    input_v = parse_input()
    print(f'the input XX is {input_v.XX}')
    print('we are in the main function')
    multiplyby9(input_v.num)
    printHello()

#########