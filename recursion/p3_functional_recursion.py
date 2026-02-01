# reversing the array using recursion, using 2 pointers here
arr1 = [0, 1, 2, 3, 4, 5, 6]
arr2 = [0, 1, 2, 3, 4, 5, 6, 7]
arr3 = [1]
def rev(arr, l, r):
    print(l, r)
    if l>=r: return
    arr[l], arr[r] = arr[r], arr[l]
    rev(arr, l+1, r-1)
rev(arr1, 0, len(arr1)-1)
print(arr1)
rev(arr2, 0, len(arr2)-1)
print(arr2)
rev(arr3, 0, len(arr3)-1)
print(arr3)


# reversing the array using recursion, using 1 pointer here
def rev(arr, l):
    length = len(arr)
    if l == length//2: return
    arr[l], arr[length - (l +1)] =  arr[length - (l +1)], arr[l]
    rev(arr, l+1)
rev(arr1, 0)
print(arr1)
rev(arr2, 0)
print(arr2)
rev(arr3, 0)
print(arr3)


# check if the string is a palindrome
s1 = "abcdcba"
s2 = "abcdeba"
def check(letter1, letter2):
    return letter1 == letter2
def palin(s, l, r):
    if l >= r: return True
    if s[l] != s[r]: return False
    return palin(s, l+1, r-1)
palin(s1, 0, len(s1)-1)
palin(s2, 0, len(s2)-1)