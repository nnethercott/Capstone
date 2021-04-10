import pandas as pd
import os
import pickle 

import MRI_util_2 as ut 


data_path = 'C:\\Users\\david\\Desktop\\Pickle_MRI\\native_1'
save_path = 'C:\\Users\\david\\Desktop\\COM_native1'

columns = ['file', 'Max Intensity', 'Min Intensity', 'Average Intensity', 'Max Delta Intensity', 'Min Delta Intensity', 'Average Delta Intensity', 'Max Variance', 'Min Variance', 'Average Variance', 'Max Delta Variance', 'Min Delta Variance', 'Average Delta Variance']
df = pd.DataFrame(columns = columns)

length = len(os.listdir(data_path))
num = 0

for file in os.listdir(data_path):
    loaded = pickle.load(open(data_path + '\\' + file, 'rb'))
    new_row_x = dict()
    new_row_y = dict()
    
    mri = loaded[1]

    if len(loaded) > 3:
        lesion = loaded[3]
    else:
        lesion = loaded[2]
    
    layers = ut.find_layers(lesion)
    interior = ut.find_interior(lesion)

    temp = ut.test_intensity(interior, mri, layers)
    int_x = temp[0]
    var_x = temp[1]

    
    delta_x = [None]*(len(int_x)-1)
    delta_var_x = [None]*(len(var_x)-1)
  
    j = 0
    
    for i in range(0, len(int_x)-1):
        delta_x[i] = abs(int_x[i+1] - int_x[i])
        delta_var_x[i] = abs(var_x[i+1] - var_x[i])

        
    new_row_x['file'] = loaded[0][0]  
    new_row_x['Max Intensity'] = max(int_x)
    new_row_x['Min Intensity'] = min(int_x)
    new_row_x['Average Intensity'] = sum(int_x)/len(int_x)
    new_row_x['Max Delta Intensity'] = max(delta_x)
    new_row_x['Min Delta Intensity'] = min(delta_x)
    new_row_x['Average Delta Intensity'] = sum(delta_x)/len(delta_x)

    new_row_x['Max Variance'] = max(var_x)
    new_row_x['Min Variance'] = min(var_x)
    new_row_x['Average Variance'] = sum(var_x)/len(var_x)
    new_row_x['Max Delta Variance'] = max(delta_var_x)
    new_row_x['Min Delta Variance'] = min(delta_var_x)
    new_row_x['Average Delta Variance'] = sum(delta_var_x)/len(delta_var_x)
    

    
    
    
    
    df = df.append(new_row_x, ignore_index = True)

    num = num + 1
    print(str(num) + '/' + str(length))

df.to_excel("native1_intensity_xfilter.xlsx")


    

