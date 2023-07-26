def excelColumnNumber(str1):
    result=0
    n=len(str1)
    for i in range(n):
        char_value  = ord(str1[i])-ord('A')+1
        result = result*26+char_value
    return result
if __name__ =="__main__":
    str1 = input().strip()
    print(excelColumnNumber(str1))        
    # Write your code here.
