height = 7
middle  = height // 2
#top half
for i in range(middle + 1):

    spaces_before = middle - i
    spaces_between = i * 2 - 1
    
    for _ in range(spaces_before):
        print(' ', end = '')
    print('*', end = '')

    if spaces_between > 0: 
        for _ in range(spaces_between):
            print(' ', end = '')
        print('*', end ='')
    print()

#bottom half
for i in range(middle - 1, -1, -1):

    spaces_before = middle - i
    spaces_between = i * 2 - 1

    for _ in range(spaces_before):
        print(' ', end = '')
    print('*', end = '')

    if spaces_between > 0: 
        for _ in range(spaces_between):
            print(' ', end = '')
        print('*', end = '')
    print()