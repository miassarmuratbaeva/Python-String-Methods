text1 = input("1-matn kiriting: ")
text2 = input("2-matn kiriting: ")

lower_text1 = text1.lower()
lower_text2 = text2.lower()

is_text_in = lower_text1 in lower_text2

if is_text_in:
    print(is_text_in)
else:
    print(is_text_in)
