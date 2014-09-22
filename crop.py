from PIL import Image
from pylab import *

def select_region(img):
    """Takes input the diagonal coordinates"""
    print "Click on 2 points to select an area"
    x = ginput(2)
    box = x[0] + x[1]
    box = tuple(int(i) for i in box)
    region = img.crop(box)
    return region
    
def main():
    
    image_filename = "test_image.png"
    img = Image.open(image_filename)
    imshow(array(img))
    region = select_region(img)
    figure()
    region = array(region)
    imshow(region)
    print region[0,0]
    axis('off')
    show()

main()
