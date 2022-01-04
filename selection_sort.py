
def selection_sort(li):
    n = len(li)

    for i in range(0, n-1):
        index_min = i

        for j in range(i+1, n):
            if li[j] < li[index_min]:
                index_min = j

        if index_min != i:
            li[i], li[index_min] = li[index_min], li[i]


if __name__ == '__main__':
    lists = [5, 1, 9, 11, 5, 3, 10, 34]
    print(f'Before sort list : {lists}')
    selection_sort(lists)
    print(f'After sort list : {lists}')


""" Complexity

Worst case time complexity ---> O(n^2)
Best case complexity       ---> O(n)
Average case complexity    ---> O(n^2)
Space complexity           ---> O(1)

"""