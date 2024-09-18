#EXAMPLE OF CONTEST:

def min_horseshoes_needed(s1, s2, s3, s4):
    # Create a set of the given colors to find unique colors
    unique_colors = set([s1, s2, s3, s4])
    # Calculate the number of horseshoes needed to have four unique colors
    return 4 - len(unique_colors)
 
# Input reading
s1, s2, s3, s4 = map(int, input().split())
# Output the result
print(min_horseshoes_needed(s1, s2, s3, s4))

#EXAMPLE OF ONE LINE
print(4 - len(set(map(int, input().split()))))