def main():
    # 計算
    #calculate()

    # 文字列同士の連結
    #stringPlusString()
    #stringPlusString2()

    # 型の変更
    #cast()



def calculate():
    num1 = 10
    num2 = 2

    # 加算
    print(num1+num2)

    # 減算
    print(num1-num2)

    # 乗算
    print(num1*num2)

    # 除算
    print(num1/num2)

    # 累乗
    print(num1**num2)

    # 余り
    print(num1%num2)

def stringPlusString():
    str1 = "hello"
    str2 = "world"

    hello_world = str1+str2
    print(hello_world)

def stringPlusString2():
    str1 = "hello"
    str2 = 2

    hello_world = str1*str2
    print(hello_world)

def cast():
    str_seven = "7"
    int_seven = 7

    ## str -> int
    print(type(int(str_seven)))

    ## int -> str
    print(type(str(int_seven)))

if __name__ == "__main__":
    main()