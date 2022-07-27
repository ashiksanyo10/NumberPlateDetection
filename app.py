import pyshorteners as ps 

url = "https://youtu.be/dQw4w9WgXcQ"

link = ps.Shortener().tinyurl.short(url)

print(link)