import csv
from tkinter import filedialog
def list_to_csv(L:list):
    path=filedialog.asksaveasfilename()
    with open(path+".csv",'w',newline='') as file:
        writer=csv.writer(file)
        writer.writerows(L)

        print(f"file saved at: '{path}'")
        return path+'.csv'
    
list_to_csv()