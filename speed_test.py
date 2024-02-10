import speedtest
import concurrent.futures
from tkinter import *

def get_speed():
    def perform_speed_test():
        s = speedtest.Speedtest()
        download = s.download() / 1048576
        upload = s.upload() / 1048576
        ping = round(s.results.ping)
        return download, upload, ping

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(perform_speed_test)
        download, upload, ping = future.result()

    downloadlabel.config(text='Download speed: ' + str(download) + ' Mbps')
    uploadlabel.config(text='Upload speed: ' + str(upload) + ' Mbps')
    pinglabel.config(text='Ping: ' + str(ping) + ' ms')

root = Tk()
root.geometry('600x250')
root.title('Find by URL')
root.config(background='black')

downloadlabel = Label(text='Download speed: ', font='Times 20', fg='white', background='black')
downloadlabel.place(x=50, y=45)

uploadlabel = Label(text='Upload speed: ', font='Times 20', fg='white', background='black')
uploadlabel.place(x=50, y=105)

pinglabel = Label(text='Ping: ', font='Times 20', fg='white', background='black')
pinglabel.place(x=50, y=165)

button = Button(root, text="Get Speed", command=get_speed)
button.place(x=200, y=210)

root.mainloop()