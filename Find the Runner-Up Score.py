if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    highest = -101
    for num in arr:
        if num > highest:
            highest = num
    
    runner_up = -101
    for i in range(n):
        x = arr[i]
        if x < highest and x > runner_up:
            runner_up = x
    print(runner_up)
