with open("text.txt", "r+", encoding='utf-8') as f:
    lines = f.readlines() 
    f.seek(0)
    for line in lines:
        line = line.replace("*", "") 
        f.write(line) 

    f.truncate()
