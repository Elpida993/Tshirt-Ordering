import time
import os
os.system('clear')
class bcolors:
	BOLD = '\033[1m'
	UNBOLD = '033[0m'
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
def Checkout():
    result = 0    
    for s in open('total.txt'): result += int(s.strip())
    print'Your Current total is:$',result
def another():
    user = raw_input('Add another order?:')
    if user == 'y':
        os.system('clear')        
        main()
    if user == 'n':
        Checkout()
def main():
    print bcolors.HEADER + bcolors.BOLD + bcolors.FAIL + 'Welcome To Team CIS110 T-Shirt Orders' + bcolors.ENDC
    print'Shirt Sizes Listed Below:'
    print("""
    	[1]: s = $7.00
    	[2]: m = $7.00
    	[3]: l = $7.00
    	[4]: xl = $7.00
        [5]: 2xl = $8.00
        [6]: Checkout""")
    choice = raw_input(bcolors.OKGREEN + 'What shirt size do you need?:' + bcolors.ENDC)
    choice = int(choice)  
    if choice == 1:
        user = raw_input('will the shirt be customized?:')        
        if user == 'y':
            print(bcolors.BOLD + bcolors.HEADER + 'OK. A Small shirt with customization will cost $12.00' + bcolors.ENDC)
            with open('total.txt', 'a') as file:
                file.write('12\n')
            another()     
        elif user == 'n':
            print(bcolors.BOLD + bcolors.HEADER + 'OK A Small shirt without customization will cost $7.00' + bcolors.ENDC)
            with open('total.txt', 'a') as file:
                file.write('7\n')
            another()
        else:
            print'No valid option selected. Try agaim'
            main()
    elif choice == 2:
        user = raw_input('Will the shirt be customized?:')
        if user == 'y':
            print(bcolors.BOLD + bcolors.HEADER + 'OK. A Medium shirt with customization will cost $12.00' + bcolors.ENDC)
            with open('total.txt', 'a') as file:
                file.write('12\n')
            another()
        elif user == 'n':
            print(bcolors.BOLD + bcolors.HEADER + 'OK. A Medium shirt without customization will cost $7.00' + bcolors.ENDC)
            with open('total.txt', 'a') as file:
                file.write('7\n')
            another()
        else:
            print'No valid option selected. try again'       
            main()
    elif choice == 3:
        user = raw_input('Will the shirt be customized?:')
        if user == 'y':
            print(bcolors.BOLD + bcolors.HEADER + 'OK. A Large shirt with customization will cost $12.00' + bcolors.ENDC)
            with open('total.txt', 'a') as file:
                file.write('12\n')
            another()
        elif user == 'n':
            print(bcolors.BOLD + bcolors.HEADER + 'OK. A Large shirt without customization will cost $7.00' + bcolors.ENDC)
            with open('total.txt', 'a') as file:
                file.write('7\n')
            another()
        else:
            print'No valid option selected. Try again'
            main()
    elif choice == 4:
        user = raw_input('Will the shirt be customized?:')
        if user == 'y':
            print(bcolors.BOLD + bcolors.HEADER + 'OK. A Extra Large shirt with customization will cost $12.00' + bcolors.ENDC)
            with open('total.txt', 'a') as file:
                file.write('12\n')
            another()
        elif user == 'n':
            print(bcolors.BOLD + bcolors.HEADER + 'OK. A Extra Large shirt without customization will cost $7.00' + bcolors.ENDC)
            with open('total.txt', 'a') as file:
                file.write('7\n')
            another()
        else:
            print' No valid option selected. try again'
            main()    
    elif choice == 5:
        user = raw_input('Will the shirt be customized?:')
        if user == 'y':
            print(bcolors.BOLD + bcolors.HEADER + 'OK. A 2XL shirt with customization will cost $13.00' + bcolors.ENDC)
            with open('total.txt', 'a') as file:
                file.write('13\n')
            another()
        elif user == 'n':
            print(bcolors.BOLD + bcolors.HEADER + 'OK A 2XL shirt without customization will cost $8.00' + bcolors.ENDC)
            with open('total.txt', 'a') as file:
                file.write('8\n')
            another()
        else:
            print'no valid option selected. try again.'
            main()
    elif choice == 6:
        print'Checking balance...'
        time.sleep(1)
        Checkout() 
    else:
        print('No Valid Option Selected. Try Again')
        main()
main()
