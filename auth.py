import self
from customtkinter import *
from PIL import Image

class AuthWindow(CTk):
    super().__init__()
    self.title('Logi Talk')
    self.geometry('700x400')
    self.resizable(False, False)
    self.left_Frame = CTkFrame(self)
    self.left_Frame.pack(side=LEFT, fill="both")
    bg = Image.open("bg.png")
    ctk_image = CTkImage(light_image=bg, size=(400, 400))
    self.label = CTkLabel(self, left_Frame, image=ctk_image, text_color="white", text="Welcome", font=("Arial", 25, "bold"))
    self.label.pack()
    self.right_Frame = CTkFrame(self)
    self.right_Frame.pack(side=RIGHT, fill="both", expand=True)
    self.talklabel = CTkLabel(self.right_Frame, text="Logi Talk", text_color="purple", font=("Arial", 25, "bold"))
    self.talklabel.pack(pady=10)
window = AuthWindow()
window.mainloop()

