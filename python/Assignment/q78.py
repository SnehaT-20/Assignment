'''Write a python program to find the longest words. '''
sentence = "I my name is sneha timra."
words = sentence.split()
longest = ""
for i in words:
    if len(i) > len(longest):
        longest = i
print("Longest word:", longest)