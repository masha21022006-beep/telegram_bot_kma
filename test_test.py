def bubble_sort(a):
    a = a[:]  # копия, чтобы не менять исходный список
    n = len(a)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


nums = [5, 1, 4, 2, 8]
print(bubble_sort(nums))  # [1, 2, 4, 5, 8]
print(nums)               # исходный список не изменился
