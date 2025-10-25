cp = {
    "benglore": 11,
    "mysuru": 89,
    "vij": 45
}

lc = {key:value for key,value in cp.items() if value >60 and value>s10}
print(lc)