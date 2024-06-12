def main():
    #条件分岐
    branching()

def branching():
    num = 10
    if num > 10:
	    print("numは10以上")
    elif num == 10:
	    print("numは10")
    else:
	    print("numは10以下")

if __name__ == "__main__":
    main()