def main():
    #条件分岐
    branching()

    #繰り返し
    roop()
    
    #関数呼び出し
    total = sum(1, 3)
    print(total)

def branching():
    num = 10
    if num > 10:
	    print("numは10以上")
    elif num == 10:
	    print("numは10")
    else:
	    print("numは10以下")

def roop():
    for i in range(5, 10, 1):
        print(i)
    list = ["a", "b", "c", "d"]
    for i in list:
	    print(i)
    # nが10になるまで繰り返し
    n = 0
    while n < 10:
        print(n)
        n += 1 # +1するのを忘れずに。

def sum(x, y):
    sum_num = x+y
    return sum_num



if __name__ == "__main__":
    main()