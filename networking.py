import urllib.request


def get_img(url, img_name):
    full_path = img_name+'.jpg'
    urllib.request.urlretrieve(url, full_path)





url = r"https://images.unsplash.com/photo-1551651767-d5ffbdd04b83?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1303&q=80"



get_img(url, 'Netherlands')
