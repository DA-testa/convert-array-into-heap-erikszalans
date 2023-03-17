# python3


def build_heap(data):
    swaps = []
    garums = len(data)
    for i in range(garums//2, -1,-1):
         swaps = heap(data,i,swaps)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    return swaps


def heap(data, i ,swaps):
    garums = len(data)
    while i*2+1 < garums:
        j = i*2+1
        if j+1 < garums and data[j+1] < data[j]:
            j += 1
        if data[i] <= data[j]:
            break
        data[i], data[j], = data[j], data[i]
        swaps.append((i,j))  
        i=j

    return swaps

def heap_sort(data):
    swaps = build_heap(data)
    garums = len(data)
    for i in range(garums-1, 0, -1):
        data[0], data[i] = data[i],data[0]
        swaps.append((0,i))
        swaps = heap(data, 0, swaps[:])

    return swaps


def main():
    
            # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    ievade = input()
    if "I" in ievade:
        n = int(input())
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    elif "F" in ievade:

        filename = input()
        with open(f"tests/{filename}") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split))



    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
  


if __name__ == "__main__":
    main()
