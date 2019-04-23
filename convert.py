import PIL.Image as Image
import os

train_dir = './train/'
test_dir = './test1/'

out_train_dir = './train_converted/'
out_test_dir = './test1_converted/'

for img in os.listdir(train_dir):
	im = Image.open(train_dir+img).convert('L')
	im.save(out_train_dir+img[:-3] + 'tif')

for img in os.listdir(test_dir):
	im = Image.open(test_dir+img).convert('L')
	im.save(out_test_dir+img[:-3] + 'tif')