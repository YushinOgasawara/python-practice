def main():
    #条件分岐
    branching()

    #繰り返し
    roop()
    
    #test

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


if __name__ == "__main__":
    main()