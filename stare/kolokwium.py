def wyraz(a):
    result = []
    for x in range(0,len(a)):
        data = []
        for z in range(0,len(a)):
            if a[x][len(a)//2]==a[z][len(a)//2]:
                data.append(a[z])
            else:
                continue
    result.append(data)

    return result
def main():
    a="ala ala allrw"
    a=a.split(" ")
    print(wyraz(a))
main()