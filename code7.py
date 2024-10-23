amt=input()
con_rate=input()
try:
    amt=float(amt)
    con_rate=float(con_rate)
    if con_rate==0:
        raise ValueError("It cannot be zero.")
    converted=amt*con_rate
    print("Converted Rate:",converted)
except ValueError as ve:
    print("error:",ve)
except exception as e:
    print("exception:,",e)



