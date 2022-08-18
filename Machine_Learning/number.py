import pylab
from sklearn import datasets
number_dataset = datasets.load_digits()
print(number_dataset.images[101])

#pylab.imshow(number_dataset.images[101],cmap = pylab.cm.gray_r)
#pylab.show()
