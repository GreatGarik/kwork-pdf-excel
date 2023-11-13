import tabula
import csv
# address of the file
myfile = 'input.pdf'
# using the read_pdf() function
mytable = tabula.read_pdf(myfile, pages = 1)
# printing the table
tabula.convert_into(myfile, 'temp.csv', output_format='csv', lattice=True, stream=False, pages="all")
set1 = set()
lst = []
with open('temp.csv', encoding='UTF-8') as file:
    data = csv.reader(file)
    next(data)
    for i in data:
        art = i[6].replace('\n', '')
        lst.append(art)
        set1.add(art)
with open('output.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    for item in set1:
        writer.writerow([item, lst.count(item)])