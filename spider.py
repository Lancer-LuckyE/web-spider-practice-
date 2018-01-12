#encoding: UTF-8
import urllib.request, re
def get_url(page):
    ##head =
    start_url = "http://www.g-cores.com/categories/9/originals"
    Open_url = start_url + '?page=' + str(page)
    try:
        ## data = urllib.request.urlopen(Open_url, head = head)
        data = urllib.request.urlopen(Open_url).read()
        data = data.decode('UTF-8')
    except Exception as ex:
        print(ex)
    finally:
        return data

def matched_url(data):
    url_list = re.findall(r'http://www.g-cores.com/volumes/\d*', data)
    url_list = url_list[::2]
    return url_list

def matched_programme_title(data):
    title_list = re.findall(r'img alt=.*" src', data)
    return title_list

def Page(page):
    url_list = matched_url(get_url(page))
    title_list = matched_programme_title(get_url(page))
    programme_dic = {}
    try:
        for index in range(0, len(title_list)):
            title = re.findall(r'".*" ',title_list[index])[0]
            programme_dic[title] = url_list[index]
    except IndexError as ex:
        print(ex)
    return programme_dic

print(Page(1))