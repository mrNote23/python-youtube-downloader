import tkinter
import customtkinter
from pytube import YouTube


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()


def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        title.configure(text=yt_object.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Download complete")
    except:
        finishLabel.configure(text="Error downloading", text_color="red")


# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.configure()

app.title("YouTube Downloader")

# ui elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0.5)
progressBar.pack(pady=10)

download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(pady=20)

# run app
app.mainloop()
