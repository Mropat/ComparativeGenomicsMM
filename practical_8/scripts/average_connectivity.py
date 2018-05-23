def average_con(filename):
    s = set()
    with open(filename, 'r') as f:
        f = f.readlines()
        for line in f:
            line = line.split(' ')
            s.add(line[0])       
    average = len(f)/len(s)
    print(average)                          
                
average_con('test.txt')

