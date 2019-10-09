Markdown:
'''
First, file input is used to determine sequence one and sequence two.
Second, create functions to define shifting, get matching numbers, and shift results. And use the join function to add -, and insert - to achieve the result of the output.
Third, store the sequence in the dictionary so that we can get the largest matching number in the dictionary operation we learned in the last lesson.
Finally, use the try function to troubleshoot exceptions.
'''



Code:
sequence1 = input("Input the DNA Sequence 1")
sequence2 = input("Input the DNA Sequence 2")
with open('DNA_1.txt', 'w') as f:
    f.write(sequence1)
with open('DNA_2.txt', 'w') as f:
    f.write(sequence2)

def shift_sequence1(lt, n):
    lt = list(lt)
    for i in range(n % len(lt)):
        lt.insert(0, '-')
    return "".join(lt)

def shift_sequence2(lt, n):
    lt = list(lt)
    for i in range(n % len(lt)):
        lt.insert(len(lt), '-')
    return "".join(lt)

def shift_result(n):
    shift_list = []
    for i in range(0,n):

        if n <= len(sequence1):
            shift_list.append(shift_sequence1(sequence1, i))
            shift_list.append(shift_sequence2(sequence2, i))

        else:
            shift_list.append(shift_sequence2(sequence1, i))
            shift_list.append(shift_sequence1(sequence2, i))
    return shift_list

def match_score(s1, s2):
    len_s1 = len(s1)
    matching = 0
    for i in range(len_s1):
        if s1[i] == s2[i]:
            matching = matching + 1
    return matching

store = []
dictionary_score = {}
count = 0

try:
    for i in range(0, len(sequence1)):
        shift_sequence1(sequence1, i)
        shift_sequence2(sequence2, i)
        match_score(shift_sequence1(sequence1, i), shift_sequence2(sequence2, i))
        count += 1
        dictionary_score.update({count:match_score(shift_sequence1(sequence1, i), shift_sequence2(sequence2, i))})
    for i in range(0, len(sequence2)):
        shift_sequence2(sequence1, i)
        shift_sequence1(sequence2, i)
        match_score(shift_sequence2(sequence1, i), shift_sequence1(sequence2, i))
        count += 1
        dictionary_score.update({count: match_score(shift_sequence2(sequence1, i), shift_sequence1(sequence2, i))})
except(IndexError):
    print("You must input the same length")
except(ZeroDivisionError):
    print("Wrong Input")

try:
 key_max = max(dictionary_score, key=dictionary_score.get)
 a = shift_result(key_max)
 print("max score is " + a[-1])
 print("max score is " + a[-2])
 print("match number is " + str(match_score(a[-1], a[-2])))
 if key_max <= len(sequence1):
    print("shifting sequence 1 by " + str((key_max) - 1))
 else:
    print("shifting sequence2 by " + str((key_max) - len(sequence1) - 1))

except(ValueError,IndexError):
    print("Wrong input, please try again!")


Example1:
Input the DNA Sequence 1ASDF
Input the DNA Sequence 2ASDFSAF

Wrong input, please try again!


Example2:
Input the DNA Sequence 1ACGTACGT
Input the DNA Sequence 2AGTCATAG
max score is AGTCATAG--
max score is --ACGTACGT
match number is 3
shifting sequence 1 by 2

Example3：
Input the DNA Sequence 1GTACGTAC
Input the DNA Sequence 2GAAAAAAA
max score is GAAAAAAA
max score is GTACGTAC
match number is 3
shifting sequence 1 by 0

Example4：
Input the DNA Sequence 1ACGTACGT
Input the DNA Sequence 2GTACGTAC
max score is GTACGTAC--
max score is --ACGTACGT
match number is 6
shifting sequence 1 by 2


