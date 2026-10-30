import sys

def calculateChange(coins, amount):
    if amount < 0:
        return None
    result = []
    for i in range(len(coins)):
        if amount >= coins[i]:
            result.append((coins[i], amount // coins[i]))
            amount = amount % coins[i]
    if (amount != 0):
        return None
    
    return result

def getUserInput():
    text = input("Enter change to match or type 'exit' to quit: ")
    if text.lower().strip() == "exit":
        print("Exiting...")
        sys.exit(0)
    try:
        return int(text)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None

if __name__ == "__main__":
    coins = [1, 5, 10, 25, 100, 500]
    if len(sys.argv) == 1:
        print("No arguments provided. Using default values for coins: 1, 5, 10, 25, 100, and 500.")
    else:
        try:
            hasZero = False
            for arg in sys.argv[1:]:
                coin = int(arg)
                if (coin <= 0):
                    print("Coin values cannot be zero. Using default values for coins: 1, 5, 10, 25, 100, and 500.")
                    hasZero = True
                    break
            if (not hasZero):
                coins = [int(arg) for arg in sys.argv[1:]]
                print(f"Using coin values: {coins}")
        except ValueError:
            print("Invalid coin values. Please provide valid integers.")

    coins.sort(reverse=True)
    while 1:
        answer = getUserInput()
        if (answer is not None):
            if (answer == 0):
                print("No change needed.")
                continue
            result = calculateChange(coins, answer)
            if (result is None):
                print("Given change cannot be made with the provided coins.")
            else:
                print("Change can be made with following coins:")
                for i in range(len(result)):
                    entry = result[i]
                    if (i == len(result) - 1):
                       print(f"{entry[1]}x {entry[0]}")
                    else:
                       print(f"{entry[1]}x {entry[0]}", end=", ")