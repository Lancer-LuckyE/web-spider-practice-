def Open_file():
    try:
        file = open('C:\\Users\\RoyLiu\\Desktop\\缓存.txt', 'a+')
    except IOError:
        file =