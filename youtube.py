from pytube import YouTube
import PySimpleGUI as sg
# Make this into a PySimpleGUI thing

font = ("Britannic Bold","12")
sg.theme("DarkBrown4")

layout = [
    [sg.Image('youtube.png'), sg.Text(" YouTube Downloader")],
    [sg.Text('Link: '), sg.Input(key='link')],
    [sg.Button('Submit')]
]
window = sg.Window("YouTube Downloader: Link", layout, margins=(50,50), font=font)
event, values = window.read()
if event == "Submit" or event == sg.WIN_CLOSED:
    window.close()
link = values['link']
yt = YouTube(link)
yd = yt.streams.get_highest_resolution()

layout3 = [
    [sg.Text("Title:", font=("Britannic Bold","12", "bold")), sg.Text(yt.title)],
    [sg.Text("Channel:", font=("Britannic Bold","12", "bold")), sg.Text(yt.author)],
    [sg.Text("Choose a folder:", font=("Britannic Bold","12", "bold"))],
    [sg.Input(enable_events=True, expand_x=True, key='path'), sg.FolderBrowse()],
    [sg.Button("Done")]
]
window3 = sg.Window("YouTube Downloader: Choose Folder", layout3, margins=(50,50), font=font)
event3, values3 = window3.read()
if event3 == "Done":
    yd.download(values3['path'])

window3.close()
