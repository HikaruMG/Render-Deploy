#mv .xml to new folder
import os
anntotate_path = "Users/Owner/Desktop/LeafData.v1i.voc/test/annots"
folder_path = "Users/Owner/Desktop/LeafData.v1i.voc/test"
each_path = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.lower().endswith(".xml"):
            #print(f"{root}\{file}")
            #print(file)
            os.replace(f"{root}/{file}", f"{anntotate_path}/{file}" )
print("replace file complete!")