def main():
    nums = list(map(int, input().split()))
    window_size = int(input())
    print_max_in_window(nums, window_size)


def print_max_in_window(nums, window_size):
    max_num = max(nums[:window_size])
    print(max_num)

    for i in range(window_size, len(nums)):
        max_num = max(max_num, nums[i])
        print(max_num)


if __name__ == '__main__':
    main()
