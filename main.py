from core.simulate_failure import sim_failure
from core.simulate_lifetime import sim_life_time


def main():
    while 1:
        print("Erasure code simulator")
        print("Menu")
        print("1. Simulate number of failure")
        print("2. Simulate system life time")
        print("3. run all")
        print("4. exit")
        selected_menu = input("Enter Menu number :")
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
