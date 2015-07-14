import urllib
import os
import random

comicCounter=0
errorCount=0

wallpaperNames = ['yhPMX', 'yEdqB', 'y0jxq','WShwr','wo0Kz','wD1cy','UmLZN','T12Gb','r0mR3','ph6bC','nQPT6','mrtED','KBwb0','INmTx','Hwruc','v39tc','FzraQ','eWMps','dfble','CJiOR','bu7qB','72ccc','58EbZ','fcdea','1LSss','4gR8Z']

def download_comic(url,comicName):
    """
    download a comic in the form of

    url = http://www.example.com
    comicName = '00000000.jpg'
    """
    image=urllib.URLopener()
    image.retrieve(url,comicName)  # download comicName at URL



curr_path = str(os.getcwd())
print curr_path
if os.path.exists(curr_path + '/CalvinHobbesPictures/'):
	os.chdir(curr_path + '/CalvinHobbesPictures/')
	print "changed directories"
else:
	print "making directory"
	os.mkdir(curr_path + '/CalvinHobbesPictures/')

	os.chdir(curr_path + '/CalvinHobbesPictures/')  # set where files download to
	for string in wallpaperNames:
	    print 1
	    
	    try:
	        comicName = str("CalvinWallpaper_"+str(comicCounter))
	        url = str("http://unrealitymag.bcmediagroup.netdna-cdn.com/wp-content/uploads/2011/09/"+string+".jpg")  # string containing the file name
	        comicCounter+=1  # increments the comic counter to go to the next comic, must be before the download in case the download raises an exception
	        download_comic(url,comicName)  # uses the function defined above to download the comic
	        print url
		   
	    except IOError:  # urllib raises an IOError for a 404 error, when the comic doesn't exist
	        errorCount+=1  # add one to the error count
	        
        else:
            print str("comic"+ ' ' + str(comicCounter) + string+' ' + "does not exist")  # otherwise say that the certain comic number doesn't exist
	print "comics created"  # prints if all comics are downloaded
numPics = len(os.listdir('.'))
random.seed()
randPicture = "poop"
longString = ""
while os.path.exists(randPicture) == False:
	randNum = random.randrange(0,numPics)
	randPicture = str(curr_path + "/CalvinHobbesPictures/CalvinWallpaper_" + str(randNum))
	randPic = str("file://" + randPicture)
	longString = str("gsettings set org.gnome.desktop.background picture-uri " + randPic)
	print randPic
os.system(longString)