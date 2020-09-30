import requests,urllib.request
from bs4 import BeautifulSoup

branch=input('Branch:')
start=int(input('Start:'))
end=int(input('End:'))

url='http://results.git.edu/index.php'
pload={'usn':'',"option":"com_examresult","task":"getResult"}

for i in range(start,end+1):
    if i<10:
        l3d='00'+str(i)
    elif i<100:
        l3d='0'+str(i)
    else:
        l3d=str(i)

    usn='2gi18'+branch+l3d
    pload['usn']=usn

    r=requests.post(url,data=pload)
    soup=BeautifulSoup(r.text,'html.parser')
    images=soup('img')
    try:
        imagepartofurl=images[2].get('src')
        if ' ' in imagepartofurl:
            imagepartofurl=imagepartofurl.replace(' ','%20')
        studimg=urllib.request.urlopen('http://results.git.edu'+imagepartofurl).read()
        imgfh=open(usn+'.jpg','wb')
        imgfh.write(studimg)
        imgfh.close()
    except IndexError as e:
        print(usn)
    
print('Successfully completed')
