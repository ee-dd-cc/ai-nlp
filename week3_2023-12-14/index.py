import re

txt = '#DrainTheSwamp - @GreggJarrett: No one takes anything Schiff says seriously because he lost all credibility. For 2 years he claimed there was a mound of criminal evidence. Where is it? Show us… because it doesn’t exist. #MAGA #AmericaFirst #Dobbs'

txtArr = txt.split()

txtArr1 = []
for item in txtArr:
  if re.match(r'^[@#]', item):
  # if item.find('#') > -1 or item.find('@') > -1:
    txtArr1.append(item)
print(txtArr1)


txt_upper_arr = []
txt_str = open('./bigcap.txt').read()
txt_str_arr = set(txt_str.split())
for item in txt_str_arr:
  # if item.isupper():
  if re.match(r'^[A-Z]+$', item):
    txt_upper_arr.append(item)

print(txt_upper_arr)
print(len(txt_upper_arr))