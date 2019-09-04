from PIL import Image
import os

parentdir = 'doll'
inputdir = 'input'
outputdir = 'output'
imgname_prefix = 'image_'
csvlogfilename = 'crop.csv'

def main():
    file_list = []
    for i in range(10000):
        filepath = './' + parentdir + '/' + inputdir + '/' + imgname_prefix + ('%04d' % i) + '.jpg'
        outputpath = './' + parentdir + '/' + outputdir + '/' + imgname_prefix + ('%04d' % i) + '.png'
        if os.path.exists(filepath):
            file_list.append((i, filepath, outputpath))
            im = Image.open(filepath)
            im.save(outputpath)
    

if __name__ == "__main__":
    main()