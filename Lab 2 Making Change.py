# makeChange.py
# This program converts pennies into as few coins as possible.


def main():
    print("Hello")
    print("The minimum number of coins required to make change is one pennie.")
    print("Please enter in your change amount out of one hundred.")

    pennies = int(input("Change: "))
    quarters = pennies // 25
    pennies = pennies - (quarters * 25)
    dimes = pennies // 10
    pennies = pennies - (dimes * 10)
    nickles = pennies // 5
    pennies = pennies - (nickles * 5)
    total = quarters + dimes + nickles + pennies
    print("-",quarters, "quarters")
    print("-",dimes, "dimes")
    print("-",nickles, "nickles")
    print("-",pennies, "pennies")


main()
    
