require(XML)
require(httr)
tables <- GET("https://en.wikipedia.org/wiki/Demographics_of_India")
tables <- readHTMLTable(rawToChar(tables$content))
names(tables)
df = tables[[5]]
print(df)