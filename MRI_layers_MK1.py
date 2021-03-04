import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import pickle 

#This function takes in a lesion mask and returns the layers of the MRI with part of the lesion present in the form of a list
def find_layers(im_data):
    layers = list()
    for i in range(0, len(im_data[0][0])):
        flag = False                                
        for j in range(0, len(im_data[0])):
            if flag:
                break
            for k in range(0,len(im_data)):
                if im_data[k][j][i] > 0:
                    layers.append(i)
                    flag = True
                    break
    return layers
#This function returns a boolean value indicating if a given point in a list is a border point
def is_border(lst, x, y, z):
    if lst[x][y][z] == 0:
        return False
    for i in range(x-1, x+1):
        if lst[i][y-1][z] == 0 or lst[i][y+1][z] == 0:
            return True
        elif lst[i][y][z] == 0 and i != x:
            return True
    return False

#This function takes a lesion mask and layers with lesion present as input and returns a list of border points
def find_border(im_data, layers):
    border = list()
    for layer in layers:
        for j in range(1, len(im_data[0])- 1):
            for i in range(1, len(im_data) - 1):
                if is_border(im_data, i, j, layer):
                    border.append([i, j, layer])
    return border

#This function takes a lesion mask or image data and a set of border points and returns a new mask with just the border outlined
def gen_bordermask(im_data, border):
    x_size = len(im_data)
    y_size = len(im_data[0])
    z_size = len(im_data[0][0])
    new_mask = np.zeros((x_size, y_size, z_size))
    for point in border:
        new_mask[point[0]][point[1]][point[2]] = 255
    return np.array(new_mask)

#This function displays a sequence of MRI slides side by side for the given layer list inputted        
def display_mri(im_data, im_mask, layers):
    for ind in layers:
        plt.figure()
        plt.subplot(1,2,1)
        plt.imshow(im_data[:,:,ind], cmap="gray")
        plt.subplot(1,2,2)
        plt.imshow(im_mask[:,:,ind], cmap="gray")
    plt.show()
    return
""" 
def mri_hole(im_data, im_mask, layers):
   x_size = len(im_data)
   y_size = len(im_data[0])
   z_size = len(im_data[0][0])
   new_data = [None]*

"""


data = nib.load("c0003s0002t01_LesionSmooth_stx.nii.gz") #Name of MRI file
image_mask = data.get_fdata() #This looks like an array
#mask = nib.load()
#image_mask = mask.get_fdata()
#plt.imshow(image_data[:,:,70], cmap="gray") #Use this to generate an image
data_1 = nib.load("c0003s0002t01_t1w_stx.nii.gz") #Name of MRI file
image_data = data_1.get_fdata() #This looks like an array
#plt.imshow(image_mask[:,:,70], cmap="gray") #Use this to generate an image
