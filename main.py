import tkinter as tk

# --------------------------VARIABLES--------------------------

windowBgColor = "gray10"
numBgColor = "gray95"
numFgColor = "black"
signBgColor = "dodgerblue2"
signFgColor = "white"
btnPadding = 4
calcFont = "Roboto"
calcFontSize = 18
btnWidth = 5
btnHeight = 1
displayBgColor = "gray10"
displayFgColor = "white"
displayInPadding = 6
displayFontSize = calcFontSize




root = tk.Tk()
root.title("Calculadora Tkinter")
root.resizable(0, 0)
root.config(padx=10, pady=10, bg=displayBgColor)



# ---------------------------PANTALLA---------------------------

display = tk.Entry(root, font=(calcFont, displayFontSize), bg=displayBgColor, relief="flat", fg=displayFgColor, justify="right")
display.focus()
display.grid(column=0, row=0, columnspan=4, pady="20", sticky="ew", ipady=displayInPadding, ipadx=displayInPadding)





# ---------------------------BOTONES---------------------------

btn_0 = tk.Button(root,
                  text="0",
                  width=btnWidth,
                  height=btnHeight,
                  bg=numBgColor,
                  fg=numFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_0.grid(column=1, row=4, padx=btnPadding, pady=btnPadding)


btn_1 = tk.Button(root,
                  text="1",
                  width=btnWidth,
                  height=btnHeight,
                  bg=numBgColor,
                  fg=numFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_1.grid(column=0, row=3, padx=btnPadding, pady=btnPadding)


btn_2 = tk.Button(root,
                  text="2",
                  width=btnWidth,
                  height=btnHeight,
                  bg=numBgColor,
                  fg=numFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_2.grid(column=1, row=3, padx=btnPadding, pady=btnPadding)


btn_3 = tk.Button(root,
                  text="3",
                  width=btnWidth,
                  height=btnHeight,
                  bg=numBgColor,
                  fg=numFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_3.grid(column=2, row=3, padx=btnPadding, pady=btnPadding)


btn_4 = tk.Button(root,
                  text="4",
                  width=btnWidth,
                  height=btnHeight,
                  bg=numBgColor,
                  fg=numFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_4.grid(column=0, row=2, padx=btnPadding, pady=btnPadding)


btn_5 = tk.Button(root,
                  text="5",
                  width=btnWidth,
                  height=btnHeight,
                  bg=numBgColor,
                  fg=numFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_5.grid(column=1, row=2, padx=btnPadding, pady=btnPadding)


btn_6 = tk.Button(root,
                  text="6",
                  width=btnWidth,
                  height=btnHeight,
                  bg=numBgColor,
                  fg=numFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_6.grid(column=2, row=2, padx=btnPadding, pady=btnPadding)


btn_7 = tk.Button(root,
                  text="7",
                  width=btnWidth,
                  height=btnHeight,
                  bg=numBgColor,
                  fg=numFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_7.grid(column=0, row=1, padx=btnPadding, pady=btnPadding)


btn_8 = tk.Button(root,
                  text="8",
                  width=btnWidth,
                  height=btnHeight,
                  bg=numBgColor,
                  fg=numFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_8.grid(column=1, row=1, padx=btnPadding, pady=btnPadding)


btn_9 = tk.Button(root,
                  text="9",
                  width=btnWidth,
                  height=btnHeight,
                  bg=numBgColor,
                  fg=numFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_9.grid(column=2, row=1, padx=btnPadding, pady=btnPadding)


btn_eq = tk.Button(root,
                  text="=",
                  width=btnWidth,
                  height=btnHeight,
                  bg=signBgColor,
                  fg=signFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_eq.grid(column=0, row=4, padx=btnPadding, pady=btnPadding)


btn_dot = tk.Button(root,
                  text=".",
                  width=btnWidth,
                  height=btnHeight,
                  bg=signBgColor,
                  fg=signFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_dot.grid(column=2, row=4, padx=btnPadding, pady=btnPadding)


btn_res = tk.Button(root,
                  text="-",
                  width=btnWidth,
                  height=btnHeight,
                  bg=signBgColor,
                  fg=signFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_res.grid(column=3, row=1, padx=btnPadding, pady=btnPadding)


btn_sum = tk.Button(root,
                  text="+",
                  width=btnWidth,
                  height=btnHeight,
                  bg=signBgColor,
                  fg=signFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_sum.grid(column=3, row=4, padx=btnPadding, pady=btnPadding)


btn_mul = tk.Button(root,
                  text="x",
                  width=btnWidth,
                  height=btnHeight,
                  bg=signBgColor,
                  fg=signFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_mul.grid(column=3, row=3, padx=btnPadding, pady=btnPadding)


btn_div = tk.Button(root,
                  text="%",
                  width=btnWidth,
                  height=btnHeight,
                  bg=signBgColor,
                  fg=signFgColor,
                  borderwidth=0,
                  font=(calcFont, calcFontSize, "bold"),
                  cursor="hand2")
btn_div.grid(column=3, row=2, padx=btnPadding, pady=btnPadding)









root.mainloop()