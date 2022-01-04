def bubble_sort(li):
    n = len(li)

    for i in range(0, n):
        for j in range(0, n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


if __name__ == '__main__':
    li = [6, 2, 4, 7, 0, 5, 1]
    # print(f'Before sort: {li}')
    bubble_sort(li)
    # print(f'After sort: {li}')


""" Complexity

Worst time complexity   ---> O(n^2)
Best case complexity    ---> O(n)
Average case complexity ---> O(n^2)
Space complexity        ---> O(1)

"""