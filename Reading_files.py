#⌨️ (2:53:28) Reading Files

from csv import DictReader
import csv


countries_file = open("./data/Countries.txt",mode='r',encoding='utf-8' )
print(countries_file.read())#(countries_file.readlines()[0])
countries_file.close()


# r=Read ,w=Write whats out this method will overwrite the entire file. ,a=Append ,x=Create
def read_file():
    for line in open("./data/Countries.md",mode='r',encoding='utf-8'):
        print(line) 


#Example Open a file on a different location:
def name_file():
    file = open('./data/Countries.csv','r') 
    csv_reader = csv.DictReader(file)
    country_list = list(csv_reader)
    print(country_list)


if __name__=='__main__':
    #read_file()
   #name_file()
    pass