"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    Result= result.replace( "fooziman" , "F00Z1M@N")
    Result = list(Result)
    return Result 