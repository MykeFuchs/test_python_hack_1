"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    x = 0
    while x <= 5:
        if x % 2 !=0:
            result.insert(x , "@")
        x +=1
    return result