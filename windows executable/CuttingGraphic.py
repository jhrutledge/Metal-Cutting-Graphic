# -*- coding: utf-8 -*-
"""
Script creates graphic for understanding orthoganol cutting

@author: jhrutledge
"""
import math
import numpy as np
import tkinter as tk
from tkinter import ttk,messagebox,scrolledtext
from CalculationClasses import calcForce,calcPower,forceTab,powerTab


#-------------------------------------------------------------------------------
''' when Force Tab update button is pressed '''
def update_force():
    global force,power,powerExt
    # test inputs
    newCalc = calcForce() # initialize calculation block
    if not force.inpTest(newCalc): # test arrangement and value type
        messagebox.showinfo('Invalid Input','Invalid input combination or\nunusable values supplied')
    else: # if good rerun merchants circle builder
        merchBuild(newCalc.alpha,newCalc.Fc,newCalc.Ft,newCalc.beta,newCalc.Ff,newCalc.Nf,newCalc.phi,newCalc.Fs,newCalc.Ns)
    # if values are bad then newCalc values will remain at 0
    # if values are good they will be calculated
    force.outputs = [newCalc.alpha,newCalc.Fc,newCalc.Ft,newCalc.beta,newCalc.Ff,newCalc.Nf,newCalc.phi,newCalc.Fs,newCalc.Ns]
    # display results
    for i in range(0,len(force.outputs)):
        force.outbox[i].config(state="enabled")
        force.outbox[i].delete(0,tk.END)
        force.outbox[i].insert(0,np.around(force.outputs[i],3))
        force.outbox[i].config(state="readonly")
    # values extended to power tab
    powerExt = [newCalc.Fc,newCalc.alpha,newCalc.Ff,newCalc.beta,newCalc.Fs,newCalc.phi]
    # print values to power tab
    for i in range(0,len(powerExt)):
        power.extbox[i].config(state="enabled")
        power.extbox[i].delete(0,tk.END)
        power.extbox[i].insert(0,np.around(powerExt[i],3))
        power.extbox[i].config(state="readonly")
    
#-------------------------------------------------------------------------------
''' when Power Tab update button is pressed '''
def update_power():
    global power,powerExt
    # test inputs
    newCalc = calcPower(powerExt) # initialize calculation block
    if not power.inpTest(newCalc): # test arrangement and value type
        messagebox.showinfo('Invalid Input','Invalid input combination or\nunusable values supplied')
    else: # if good rerun chip diagram builder
        chipBuild(newCalc.alpha,newCalc.phi,newCalc.t)
    # if values are bad then newCalc values will remain at 0
    # if values are good they will be calculated
    power.outputs = [newCalc.V,newCalc.Vc,newCalc.Vs,newCalc.r,newCalc.t,
                     newCalc.tc,newCalc.MRR,newCalc.uc,newCalc.uf,newCalc.us,
                     newCalc.mu,newCalc.Tau,newCalc.Gamma]
    # display results
    for i in range(0,len(power.outputs)):
        power.outbox[i].config(state="enabled")
        power.outbox[i].delete(0,tk.END)
        power.outbox[i].insert(0,np.around(power.outputs[i],3))
        power.outbox[i].config(state="readonly")

#-------------------------------------------------------------------------------
''' build Merchant Circle tab '''
def merchBuild(alpha=6,Fc=400,Ft=300,beta=42.87,Ff=340.17,Nf=366.45,phi=26.56,Fs=223.61,Ns=447.21):
    global canvas1
    # clear canvas element
    canvas1.delete("all");
    # center of circle
    c_x = 200
    c_y = 300
    R1 = 300 # scaled reaction
    #calc reaction
    R = math.hypot(Fc,Ft)
    #plot circle
    canvas1.create_oval(50,150,50+R1,150+R1)
    #plot center point
    canvas1.create_oval(c_x-2,c_y-2,c_x+2,c_y+2,fill="black")
    dx = R1 * math.cos(math.radians(beta-alpha)) / 2
    dy = R1 * math.sin(math.radians(beta-alpha)) / 2
    #tip point
    P1x = c_x + dx
    P1y = c_y - dy
    #end point
    P2x = c_x - dx
    P2y = c_y + dy
    #plot axis
    canvas1.create_line(0, P1y, 500, P1y, dash=(5,5))
    canvas1.create_line(P1x, 0, P1x, 500, dash=(5,5))
    #plot R line
    canvas1.create_line(P1x, P1y, P2x, P2y)
    canvas1.create_text(c_x, c_y, anchor="s", text="R")
    #plot F_c line
    canvas1.create_line(P1x, P1y, P2x, P1y)
    canvas1.create_text(c_x, P1y, anchor="s", text="F_c")
    #plot F_t line
    canvas1.create_line(P2x, P1y, P2x, P2y)
    canvas1.create_text(P2x+5, c_y, anchor="w", text="F_t")
    #plot tool
    dx1 = R1 * math.sin(math.radians(alpha)) / 2
    dy1 = R1 * math.cos(math.radians(alpha)) / 2
    canvas1.create_line(P1x, P1y, P1x+dx1, P1y-dy1,width=2)
    dx1 = R1 * math.cos(0.1) / 2
    dy1 = R1 * math.sin(0.1) / 2
    canvas1.create_line(P1x, P1y, P1x+dx1, P1y-dy1,width=2)
    canvas1.create_text(P1x+(R1/4), P1y-(R1/4), anchor="sw", text="tool")
    #plot friction lines
    dx1 = (Ff*R1/R) * math.sin(math.radians(alpha))
    dy1 = (Ff*R1/R) * math.cos(math.radians(alpha))
    canvas1.create_line(P1x, P1y, P1x-dx1, P1y+dy1, fill="green")
    canvas1.create_text(P1x-(dx1/2), P1y+(dy1/2), anchor="e", fill="green", text="F_f")
    canvas1.create_line(P1x-dx1, P1y+dy1, P2x, P2y, fill="green")
    canvas1.create_text(P2x+(dy1*2/3), P2y+(dx1/2),anchor="n",fill="green", text="N_f")
    #plot shear lines
    dx1 = (Fs*R1/R) * math.cos(math.radians(phi))
    dy1 = (Fs*R1/R) * math.sin(math.radians(phi))
    canvas1.create_line(P1x, P1y, P1x-dx1, P1y-dy1, fill="blue")
    canvas1.create_text(P1x-(dx1/2), P1y-(dy1/2), anchor="n", fill="blue", text="F_s")
    canvas1.create_line(P1x-dx1, P1y-dy1, P2x, P2y, fill="blue")
    canvas1.create_text(c_x-(dy1/2), P1y-(dy1/2), anchor="ne", fill="blue", text="N_s")
    # update canvas
    canvas1.update()          

#-------------------------------------------------------------------------------
''' build Chip Diagram tab '''
def chipBuild(alpha=6,phi=26,t=3):
    global canvas2
    canvas2.delete("all")
    # tool tip
    c_x = 350
    c_y = 350
    c1 = 200
    hyp = t / math.sin(math.radians(phi))
    tc = hyp * math.sin(math.radians(alpha+90-phi))
    #plot cut path
    canvas2.create_line(c_x,c_y,c_x+500,c_y)
    canvas2.create_line(c_x,c_y,0,c_y,dash=(5,5))
    # plot tool
    dx = 300 * math.sin(math.radians(alpha))
    dy = 300 * math.cos(math.radians(alpha))
    canvas2.create_line(c_x,c_y,c_x+dx,c_y-dy,width=3)
    canvas2.create_text(c_x+(dy/4),c_y-(dy/4),text="tool")
    dx = 300*math.cos(math.pi/18)
    dy = 300*math.sin(math.pi/18)
    canvas2.create_line(c_x,c_y,c_x+dx,c_y-dy,width=3)
    # plot shear plane
    dy = t*(c1/hyp)
    dx = dy/math.tan(math.radians(phi))
    canvas2.create_line(c_x,c_y,c_x-dx,c_y-dy,fill="blue")
    # plot material
    canvas2.create_line(c_x-dx,c_y-dy,0,c_y-dy,width=2,fill="gray")
    dx = c_x-dx-100
    dy = c_y-dy
    canvas2.create_line(dx,dy,dx,c_y,fill="gray10",dash=(2,1))
    canvas2.create_text(dx-5,(c_y+dy)/2,anchor="e",text="t")
    # plot feed
    canvas2.create_line(dx-50,dy-10,dx+50,dy-10)
    canvas2.create_line(dx-50,dy-10,dx-45,dy-5)
    canvas2.create_line(dx-50,dy-10,dx-45,dy-15)
    canvas2.create_text(dx,dy-15,anchor="s",text="V")
    # plot chip
    cx = c_x-(t*(c1/hyp)/math.tan(math.radians(phi)))
    cy = c_y-(t*(c1/hyp))
    dx = 300 * math.sin(math.radians(alpha))
    dy = 300 * math.cos(math.radians(alpha))
    canvas2.create_line(cx,cy,cx+dx,cy-dy,width=2,fill="gray")
    # plot chip feed
    canvas2.create_line(cx+15,cy-5,cx+(dx/4)+15,cy-(dy/4)-5)
    canvas2.create_line(cx+(dx/4)+15,cy-(dy/4)-5,cx+(dx/4)+10,cy-(dy/4))
    canvas2.create_line(cx+(dx/4)+15,cy-(dy/4)-5,cx+(dx/4)+20,cy-(dy/4))
    canvas2.create_text(cx+(dx/4)+15,cy-(dy/4)-10,anchor="s",text="Vc")
    cx = c_x+(dx*3/4)
    cy = c_y-(dy*3/4)
    dx = tc*(c1/hyp)*math.cos(math.radians(alpha))
    dy = tc*(c1/hyp)*math.sin(math.radians(alpha))
    canvas2.create_line(cx,cy,cx-dx,cy-dy,fill="gray10",dash=(2,1))
    canvas2.create_text(cx-(dx/2),cy-(dy/2)-5,anchor="s",text="tc")
    # update canvas
    canvas2.update()
    
#-------------------------------------------------------------------------------
''' build angle diagram tab '''
def angleBuild():
    '''This tab will show the cutting interface on the mohr's circle explaining the angles'''
    global canvas3
    # clear canvas element
    canvas3.delete("all")
    # center of diagram (tool tip)
    c_x = 250
    c_y = 250
    L1 = 200
    # plot center
    canvas3.create_oval(-530.116,69.884,330.116,930.116)
    canvas3.create_oval(c_x-2,c_y-2,c_x+2,c_y+2,fill="black")
    #plot axis
    canvas3.create_line(0, c_y, 500, c_y, dash=(5,5))
    canvas3.create_line(c_x, 0, c_x, 500, dash=(5,5))
    # plot tool
    dx = L1*math.cos(math.pi/9) # 20deg
    dy = L1*math.sin(math.pi/9)
    canvas3.create_line(c_x,c_y,c_x+dy,c_y-dx,width=2)
    canvas3.create_line(c_x,c_y,c_x+dx,c_y-dy,width=2)
    canvas3.create_text(c_x+(L1*3/4),c_y-(L1*3/4),text="tool")
    canvas3.create_text(c_x+(dy/4),c_y-(dx/2),anchor="s",text="alpha")
    canvas3.create_text(c_x+(dx/2),c_y-(dy/2),anchor="nw",text="flank angle")
    # plot shear
    dx = L1*math.cos(math.pi/6) # 40deg
    dy = L1*math.sin(math.pi/6)
    canvas3.create_line(c_x,c_y,c_x-dx,c_y-dy,width=2,fill="blue")
    canvas3.create_text(c_x-dx,c_y-dy,anchor="e",fill="blue",text="F_s")
    canvas3.create_text(c_x-(dx/2),c_y-(dy/4),anchor="ne",fill="blue",text="phi")
    # plot cut
    canvas3.create_line(c_x,c_y,c_x-L1,c_y,width=2)
    canvas3.create_text(c_x-L1,c_y,anchor="se",text="F_c")
    # plot R
    dx = L1*math.cos(math.pi/4) # 45deg
    canvas3.create_line(c_x,c_y,c_x-dx,c_y+dx,width=2)
    canvas3.create_text(c_x-dx,c_y+dx,anchor="ne",text="R")
    canvas3.create_text(c_x-(dx/2),c_y+(dy/4),anchor="s",text="beta-alpha")
    # plot friction
    dx = L1*math.sin(math.pi/9) # 20deg
    dy = L1*math.cos(math.pi/9)
    canvas3.create_line(c_x,c_y,c_x-dx,c_y+dy,width=2,fill="green")
    canvas3.create_text(c_x-dx,c_y+dy,anchor="ne",fill="green",text="F_f")
    canvas3.create_text(c_x-dx/2,c_y+(dy/2),anchor="e",fill="green",text="90-beta")
    # update canvas
    canvas3.update()    
    
#-------------------------------------------------------------------------------
''' build readme tab '''
def reaBuild():
    global readme
    rm = open("README.txt",'r').read()
    scr = scrolledtext.ScrolledText(readme,width=77,height=25,wrap=tk.WORD)
    scr.grid(column=0,row=1)
    scr.insert(tk.INSERT,rm)

#-------------------------------------------------------------------------------
''' Initialize Master Window '''
master = tk.Tk()
''' Build Tab Frames '''
master.title("Orthoganol Cutting")
tabControl = ttk.Notebook(master)
# Directions tab
readme = ttk.Frame(tabControl)
tabControl.add(readme,text="README")
reaBuild()
# Force Calculations tab
force = forceTab(tabControl)
tabControl.add(force.tab,text="Force Calculations")
# update button
ttk.Button(force.tab,text="Update",command=update_force).grid(column=4,row=11)
# Merchant Circle tab
merchTab = ttk.Frame(tabControl)
tabControl.add(merchTab,text="Merchant Circle")
canvas1 = tk.Canvas(merchTab, width=500,height=500)
canvas1.pack()
# Power Calculations tab
power = powerTab(tabControl)
tabControl.add(power.tab,text="Power Calculations")
# update button
ttk.Button(power.tab,text="Update",command=update_power).grid(column=4,row=13)
# Chip Diagram tab
chipTab = ttk.Frame(tabControl)
tabControl.add(chipTab,text="Chip Diagram")
canvas2 = tk.Canvas(chipTab, width=500,height=500)
canvas2.pack()
# Angle Diagram tab
angleTab = ttk.Frame(tabControl)
tabControl.add(angleTab,text="Angle Diagram")
canvas3 = tk.Canvas(angleTab, width=500,height=500)
canvas3.pack()
# build window
tabControl.pack() #expand=1,fill="both"
# Execute diagram build functions
merchBuild()
chipBuild()
angleBuild()
# continuously display window
master.mainloop()