from  tkinter import *
from  tkinter import filedialog
from pygame import mixer
root=Tk()
root.title('mp3 player')
mixer.init()

songs_list=Listbox(root,bg="black",fg="white",font="arial 15",height=12,width=47,
selectmode=SINGLE,selectbackground="gray",selectforeground='black')
songs_list.grid(columnspan=6)

def play():
    songs=songs_list.get(ACTIVE)
    mixer.music.load('tone.mp3',songs)
    mixer.music.play()

def pause():
    mixer.music.pause()

def resume():
    mixer.music.unpause()

def stop():
    mixer.music.stop()

def previous():
    previous_one=songs_list.curselection()
    p_one=previous_one[0]-1
    temp=songs_list.get(p_one)
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_Clear(0,END)
    songs_list.activate(p_one)
    songs_list.selection_set(p_one)


def next():
    next_one=songs_list.curselection()
    n_one=next_one[0]+1
    temp2=songs_list.get(n_one)
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_Clear(0,END)
    songs_list.activate(n_one)
    songs_list.selection_set(n_one)


def add():
    temp_song=filedialog.askopenfilenames(title="choose a songs",filetypes=(("mp3 files","*.mp3"),))
    for s in temp_song:
        songs_list.insert((END))
def delete():
    curr_songs=songs_list.curselection()
    songs_list.delete(curr_songs[0])

play_btn=Button(root,text='play',font='arial,width=7',command=play)
play_btn.grid(row=1,column=0)

pause_btn=Button(root,text='pause',font='arial,width=7',command=pause)
pause_btn.grid(row=1,column=1)

stop_btn=Button(root,text='stop',font='arial,width=7',command=stop)
stop_btn.grid(row=1,column=2)

Resume_btn=Button(root,text='Resume',font='arial,width=7',command=resume)
Resume_btn.grid(row=1,column=3)

Previous_btn=Button(root,text='previous',font='arial,width=7',command=previous)
Previous_btn.grid(row=1,column=4)

Next_btn=Button(root,text='next',font='arial,width=7',command=next)
Next_btn.grid(row=1,column=5)

my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="menu",menu=add_song_menu)
add_song_menu.add_command(label="add songs",command=add)
add_song_menu.add_command(label="delete songs",command=delete)
root.mainloop()

