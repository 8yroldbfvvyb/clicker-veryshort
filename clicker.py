score = 2
import sys
sys.set_int_max_str_digits(1000000)

while True:
    click = input("press enter to click quit to close: ")
    
    try:
        if click == 'quit':
            print("bye")
            break
            
        if click == '':
            score = score ** 2
            print(score)
            continue

            print(score)
            continue
            
    except ValueError:
        print("too big!")
    except OverflowError:
        print("too big")


    
        
