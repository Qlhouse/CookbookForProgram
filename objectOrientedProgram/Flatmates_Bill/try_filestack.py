from filestack import Client
client = Client('A2aGAGBUDQJGj84zis6Pzz')

new_filelink = client.upload(filepath='files/December 2021.pdf')
print(new_filelink.url)
