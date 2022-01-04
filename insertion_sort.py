def insertion_sort(li):
    n = len(li)

    for i in range(1, n):
        item = li[i]

        j = i - 1
        while j >= 0 and li[j] > li[j + 1]:
            li[j + 1] = li[j]
            j -= 1
            li[j + 1] = item


if __name__ == '__main__':
    lists = [6, 1, 4, 9, 2]
    # print(f'Before sort: {lists}')
    insertion_sort(lists)
    # print(f'After sort: {lists}')

""" Complexity

Worst case time complexity ---> O(n^2)
Best case complexity       ---> O(n)
Average case complexity    ---> O(n^2)
Space complexity           ---> O(1)

"""
