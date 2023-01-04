import tabula


table, = tabula.read_pdf('Table-and-Text.pdf', pages=1)
print(table)
table.to_excel('output.xlsx', index=False)
