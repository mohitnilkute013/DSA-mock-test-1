size = int(input("Enter size of array: "))

arr = list(map(int, input().split(' ')))

print(f"original list: {arr}")

def even_list(arr: list) -> list:
    ''' This function returns only the even numbers from the input list in a list '''

    return [i for i in arr if i%2==0]

print(f"final list: {even_list(arr)}")