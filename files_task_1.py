def main():

    file_1 = open('reflex.txt','w+')
    file_1.write('Im genuis')

    with open("reflex.txt") as file:
        for line in file:
            for ch in line:
                print(ch)

if __name__ == "__main__":
    main()
