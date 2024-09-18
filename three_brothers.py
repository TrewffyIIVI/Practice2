brothers = ['1','2','3']
onTime = input(" ").split()
lateBrother = list(set(brothers) - set(onTime))
print(lateBrother[0])
#SOLVED