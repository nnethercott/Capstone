import os
import pickle
import nibabel as nib
import numpy as np

data_path = 'C:\\Users\\david\\Desktop\\pkg36684-0001_REST\\ATLAS R 1.2\\standard_MNI\\standard_part1'
save_path = 'C:\\Users\\david\\Desktop\\Pickle_MRI\\standard_part1'
"""
data_path = 'C:\\Users\\david\\Desktop\\pkg36684-0001_REST\\ATLAS R 1.2\\native\\native_2\\native_2'
save_path = 'C:\\Users\\david\\Desktop\\Pickle_MRI\\native_2'
"""


for sub_one in os.listdir(data_path):
    if 'c' in sub_one:
        sub_path = data_path + '\\' + sub_one
        for sub_two in os.listdir(sub_path):
            if 'c' in sub_two:
                count = 0
                les_count = 0
                mri_path = sub_path + '\\' + sub_two
                for mri in os.listdir(mri_path):
                    if mri[len(mri)-6:] == 'nii.gz':
                        count += 1
                        if 'Lesion' in mri:
                            les_count +=1
                #print(count)
                to_be_saved = [None]
                str_index = list()
                
                for mri in os.listdir(mri_path):
                    if mri[len(mri)-6:] == 'nii.gz':
                        data = nib.load(mri_path + '\\' + mri) #Name of MRI file
                        data_mask = data.get_fdata() 
                        str_index.append(mri)
                        to_be_saved.append(data_mask)
                    
                to_be_saved[0] = str_index
                save_name = save_path + '\\' + sub_two + '.p'
                pickle.dump(to_be_saved, open(save_name, 'wb'))
                
#test = pickle.load(open('C:\\Users\\david\\Desktop\\Pickle_MRI\\native_1\\c0003s0015t01.p', 'rb'))