from PIL import Image
import numpy as np
import csv
import urllib2
import os
import zipfile


def get_mask(img, x_start, y_start):
    mask = []
    for x in range(10):
        mask_y = []
        for y in range(10):
            mask_y.append(img[x_start + x, y_start + y])
            mask.append(mask_y)
    return mask


def search(pb, a, b):
    zf = zipfile.ZipFile('Data/Train1.zip', 'r')
    unzippedFile = zf.open('Train1/Train1/' + pb, 'r', 'happyhalloween')
    content = unzippedFile.read()
    f = open('Data/image_v.tif', 'w')
    f.write(content)
    unzippedFile.close()
    f.close()

    gun = Image.open('Data/image_v.tif')
    # gun = gun.convert("RGBA")
    pixdata_gun = gun.load()
    search_mask = get_mask(pixdata_gun, (gun.size[0] - (16000 - int(a))) - 5, (gun.size[1] - (576 - int(b))) - 5)

    i = 1
    while i < 1001:
        unzippedFile = zf.open('Train1/Train1/' + str(i) + '.tif', 'r', 'happyhalloween')
        content = unzippedFile.read()
        f = open('Data/image.tif', 'w')
        f.write(content)
        unzippedFile.close()
        f.close()
        img = Image.open('Data/image.tif')
        pixdata_img = img.load()
        for x in range(img.size[0] - 10):
            for y in range(img.size[1] - 10):
                if pixdata_img[x, y] == search_mask[0][0]:
                    pixdata_mask = get_mask(pixdata_img, x, y)
                    if pixdata_mask == search_mask:
                        print "Search image coordinates: [{}, {}]".format(x + 5, y + 5)
        i = i + 1


def getmass(data):
    def write_response(response):
        u = urllib2.urlopen(response)
        data = u.read()
        u.close()
        filepath = os.path.join('Data/Train1.zip')
        with open(filepath, "wb") as f:
            f.write(data)

    write_response(data)

    with open("Data/objects.csv", 'rb') as f:
        coordinate = list(csv.reader(f, delimiter=';', quotechar=','))

    coordinate = np.array(coordinate[1:])
    labels = coordinate[:, 0]
    coordinate = coordinate[:, 1:]

    for j in labels:
        for row in coordinate:
            p = ', '.join(row)
            x, y = p.split(",")
            p1 = j + '.tif'
            search(p1, x, y)







