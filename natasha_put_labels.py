import os
import shutil
import numpy as np

base_dir = '/home/natasha/Downloads/timber'
train_dir = os.path.join(base_dir, 'train', 'labels')
test_dir = os.path.join(base_dir, 'test', 'labels')
val_dir = os.path.join(base_dir, 'val', 'labels')
high_dir = os.path.join(base_dir, 'high')
low_dir = os.path.join(base_dir, 'low')
labels_all_dir = os.path.join(base_dir, 'labels-all')

high_list = os.listdir(high_dir)
low_list = os.listdir(low_dir)
labels_list = os.listdir(labels_all_dir)
train_images_list = os.listdir(train_dir.replace('labels', 'images'))
test_images_list = os.listdir(test_dir.replace('labels', 'images'))
val_images_list = os.listdir(val_dir.replace('labels', 'images'))

print(train_images_list[0])

for label in labels_list:
    if label.replace('txt', 'jpg') in test_images_list:
        shutil.copyfile(src=os.path.join(labels_all_dir, label), dst=os.path.join(test_dir, label))
    if label.replace('txt', 'jpg') in val_images_list:
        shutil.copyfile(src=os.path.join(labels_all_dir, label), dst=os.path.join(val_dir, label))
    if label.replace('txt', 'jpg') in train_images_list:
        print('label ', label)
        # create new label
        with open(os.path.join(labels_all_dir, label), 'r') as f:
            label_data = f.read()
            print('label_data ', label_data)
            label_data = label_data.split('\n')
            new_data = []
            for l in label_data:
                new_data.extend(l.split(' '))
            new_data = np.array(new_data).reshape(-1, 5)
            print('new_data ', new_data)
            for idx, line in enumerate(new_data):
                if line[0] == '0' and label.replace('txt', 'jpg') in low_list:
                    new_data[idx, 0] = '2'
            print('new_data after', new_data)
            new_data_as_string = ''
            for line in new_data:
                for el in line:
                    new_data_as_string += el
                    new_data_as_string += ' '
                new_data_as_string.strip()
                new_data_as_string += '\n'
            print('new_data_as_string ', new_data_as_string)
            #input()
        with open(os.path.join(train_dir, label), 'w') as fout:
            fout.write(new_data_as_string)

