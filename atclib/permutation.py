class Permutation:
    @staticmethod
    def prev_permutation(arr):
        if arr == sorted(arr):
            return None

        i = len(arr) - 2
        while i >= 0 and arr[i] < arr[i + 1]:
            i -= 1

        j = len(arr) - 1
        while arr[j] >= arr[i]:
            j -= 1

        arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1 :] = reversed(arr[i + 1 :])
        return arr

    @staticmethod
    def next_permutation(arr):
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i == -1:
            return None
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1 :] = reversed(arr[i + 1 :])
        return arr

    @staticmethod
    def nth_permutation(arr):
        import math

        rank = 1
        n = len(arr)
        factorial = math.factorial

        for i in range(n):
            smaller = 0
            for j in range(i + 1, n):
                if arr[j] < arr[i]:
                    smaller += 1
            rank += smaller * factorial(n - i - 1)

        return rank
