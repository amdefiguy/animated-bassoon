import time

localtime = time.asctime( time.localtime(time.time()) )

execTime = localtime

file = open("readme.md", 'w')
file.write("Kept code alive at : ")
file.write(str(execTime))
file.close()
