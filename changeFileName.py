# -*- coding: UTF-8 -*-
import os

i=0
path = 'D://vain//wangyi_spider//网易悦图图文数据集//wyyt_caijing'
items = os.listdir(path)
for item in items:
    # print(item)
    path2 = 'D://vain//wangyi_spider//网易悦图图文数据集//wyyt_caijing//%s' % item
    for each in os.listdir(path2):

        # print(each)

        if each[-8:] == '.jpg.jpg':
            print(each)
            newname = each[:-4]
            # try:
            os.rename(os.path.join(path2, each), os.path.join(path2, newname))
            # except:
            #     pass

            # print(newname)




        # break
        # each = each[:-3]
        # print(each)

    # newname = "2__"+item
    # os.rename(os.path.join(path, item), os.path.join(path, newname))


















