import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    guess = None

    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个1到100之间的数字。")

    while guess != number_to_guess:
        try:
            guess = int(input("请输入你的猜测："))

            if guess < number_to_guess:
                print("太小了，再试一次！")
            elif guess > number_to_guess:
                print("太大了，再试一次！")
        except ValueError:
            print("请输入一个有效的数字！")

    print("恭喜你，猜对了！")

if __name__ == "__main__":
    guess_number_game()