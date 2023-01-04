import tabula


table = tabula.read_pdf('weather.pdf', pages=1)

print(table)

df = table[0]
df.to_csv('output.csv', index=False)
