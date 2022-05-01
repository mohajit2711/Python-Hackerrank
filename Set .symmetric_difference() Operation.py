# Enter your code here. Read input from STDIN. Print output to STDOUT
e_num = int(raw_input())
e_set = set(map(int, raw_input().split()))
f_num = int(raw_input())
f_set = set(map(int, raw_input().split()))

print len(e_set.symmetric_difference(f_set))
