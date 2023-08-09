# reguler expression : are used to find out the pattren from a given set of data..
import re

text = "In common usage and statistics, data (US: /ˈdætə/; UK: /ˈdeɪtə/) is a collection of discrete or continuous values that convey information, describing the quantity, quality, fact, statistics, other basic units of meaning, or simply sequences of symbols that may be further interpreted formally. A datum is an individual value in a collection of data. Data is usually organized into structures such as tables that provide additional context and meaning, and which may themselves be used as data in larger structures. Data may be used as variables in a computational process.[1][2] Data may represent abstract ideas or concrete measurements.[3] Data is commonly used in scientific research, economics, and in virtually every other form of human organizational activity. Examples of data sets include price indices (such as consumer price index), unemployment rates, literacy rates, and census data. In this context, data represents the raw facts and figures which can be used in such a manner in order to capture the useful information out of it."


patrn = "and"


# mth = re.search(text, patrn)
mth = re.finditer(text, patrn)


print(mth)




text = "i am a devloper, i buid many wensites. my age is 20. my mobile number is 9187293813 and my usa mobile number is for now (987)-928-923-29. contact me for devlopment. 9827383864, and my altranative number is  7891287938."

# ptrn = "\d{10}"

# ptrn = "\(\d{3}\)-\d{3}-\d{3}-\d{2}"



# matches = re.search(ptrn, text)
matches = re.findall(ptrn, text)

print(matches)






10 + 20

# 20 - 19