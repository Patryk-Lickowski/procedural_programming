def is_anagram():
    count = 0
    word1 = input("Enter your first word: ")
    word2 = input("Enter your second word: ")

    for i in range(0, len(word1)):
        if word1[i] in word2:
            count += 1
    if count == len(word1):
        print("True")
    else:
        print("False")

is_anagram()
