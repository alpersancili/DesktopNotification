from plyer import notification
import tkinter

def my_notification():
    entry1_value = entry1.get()
    entry2_value = entry2.get()

    notification.notify(
        title=entry1_value,
        message=entry2_value,
        app_icon=None,
        timeout=10,
        toast=False
    )

window = tkinter.Tk()
window.title("VOICE RECORDER")
window.minsize(width=400, height=400)

notification_title = tkinter.Label(text="Notification Title")
notification_title.place(x=50, y=30)

notification_message = tkinter.Label(text="Notification Message")
notification_message.place(x=50, y=80)

entry1 = tkinter.Entry()
entry1.place(x=180, y=30)

entry2 = tkinter.Entry()
entry2.place(x=180, y=80)

btn = tkinter.Button(text="Show Notification", command=my_notification, bg="orange")
btn.config(height=3, width=15)
btn.place(x=150, y=190)

window.mainloop()