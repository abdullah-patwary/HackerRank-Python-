if __name__ == '__main__':
    n = int(input())
    arr = sorted(set(map(int, input().split())), reverse=True)

print(arr[1])