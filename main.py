from core.simulate_failure import sim_failure
from core.simulate_lifetime import sim_life_time
from modules.colors import Colors

def main():
    while 1:
        print(f"{Colors.HEADER}Erasure code simulator{Colors.ENDC}")
        print(f"{Colors.OKGREEN}1. Simulate number of failure{Colors.ENDC}")
        print(f"{Colors.OKGREEN}2. Simulate system life time{Colors.ENDC}")
        print(f"{Colors.OKGREEN}3. run all{Colors.ENDC}")
        print(f"{Colors.OKGREEN}4. exit{Colors.ENDC}")
        selected_menu = input(f"{Colors.OKCYAN}Enter Menu number :{Colors.ENDC}")
        if selected_menu == "1":
            sim_failure()
        elif selected_menu == "2":
            sim_life_time()
        elif selected_menu == "3":
            sim_failure()
            sim_life_time()
        elif selected_menu == "4":
            exit(1)


if __name__ == "__main__":
    main()
