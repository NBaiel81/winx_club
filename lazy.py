# for ex input localization,output  l10n(in midle len letters between 1st and last letter)
text1=input()
if len(text1)>10:
    count1=len(text1)
    count2=count1-2
    hello=(str(text1[0])+str(count2)+str(text1[-1]))
    print(hello)
else:
    print(text1)
