# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 00:09:03 2018

@author: jhrut
"""
import math
import numpy as np
import tkinter as tk
from tkinter import ttk

#-------------------------------------------------------------------------------
''' object controlling Force Calculations tab '''
class forceTab():
    def __init__(self,tabControl): # initialize instance of forceTab
        # Force Calculations tab object
        self.tab = ttk.Frame(tabControl)
        # initialize arrays
        self.inputs = np.array([]) # array of input objects
        self.inbox = np.array([]) # array of input boxes
        self.outputs = np.array([]) # array of output objects
        self.outbox = np.array([]) # array of output boxes
        # instructions
        inst = "\n Instructions: \n\n       Enter any 2 Angles and 1 Force \n                    or \n       Enter alpha, F_c, and F_t   \t \n"
        ttk.Label(self.tab,text=inst).grid(column=0,row=0,columnspan=3)
        ttk.Label(self.tab,text='      ').grid(column=0,row=1)
        # description
        desc = "\n This tab will output remaining values and update the \n Merchant Circle tab when update is pressed. \n"
        ttk.Label(self.tab,text=desc).grid(column=3,row=0,columnspan=5)
        # list of inputs
        varLabels = ["Rake Angle","Cutting Force","Thrust Force",
                     "Friction Angle","Friction Force","Friction Normal",
                     "Shear Angle","Shear Force","Shear Normal"]
        var2 = ["(alpha)","(F_c)","(F_t)","(beta)","(F_f)","(N_f)","(phi)","(F_s)","(N_s)"]
        dims = ["deg","N","N","deg","N","N","deg","N","N"]
        ttk.Label(self.tab,text="Variables:").grid(column=1,row=1,columnspan=2)
        ttk.Label(self.tab,text="[dim]").grid(column=3,row=1)
        ttk.Label(self.tab,text="Inputs:").grid(column=4,row=1)
        ttk.Label(self.tab,text="Outputs:").grid(column=5,row=1)
        # display variables, build boxes
        for i in range(0,len(varLabels)):
            ttk.Label(self.tab,text=varLabels[i]).grid(column=1,row=i+2)
            ttk.Label(self.tab,text=var2[i]).grid(column=2,row=i+2)
            ttk.Label(self.tab,text=dims[i]).grid(column=3,row=i+2)
            self.inputs = np.append(self.inputs,tk.StringVar())
            self.inbox = np.append(self.inbox,ttk.Entry(self.tab,width=12,textvariable=self.inputs[i]))
            self.inbox[i].grid(column=4,row=i+2)
            self.outbox = np.append(self.outbox,ttk.Entry(self.tab,width=12))
            self.outbox[i].grid(column=5,row=i+2)
            self.outbox[i].config(state="readonly")
            
    ''' test an array of input strings to see if they contain numbers '''
    def test_nums(self,nums):
        for i in range(0,len(nums)):
            try:
                float(nums[i])
            except: # if one fails
                return False
        return True

    ''' cast inputs to float '''
    def inCast(self):
        newIn = np.array([])
        for i in range(0,len(self.inputs)):
            try: # good input
                newIn = np.append(newIn,float(self.inputs[i].get()))
            except: # empties and others to 0.0
                newIn = np.append(newIn,0.0)
        return newIn

    ''' define input set and calculate remaining values '''
    def inpTest(self,newCalc):
        inPop = np.array([]) # empty array for checking populated inputs
        for i in range(0,len(self.inputs)):
            if self.inputs[i].get(): # not empty
                inPop = np.append(inPop,True)
            else: # is empty
                inPop = np.append(inPop,False)
        # initialize output boolean
        goodSet = True 
        # check arrangement of populated inputs
        if inPop[0] and inPop[3]: #alpha and beta
            if inPop[1]: #Fc
                if self.test_nums([self.inputs[0].get(),self.inputs[3].get(),self.inputs[1].get()]):
                    newIn = self.inCast()
                    newCalc.calc1(newIn)
                    newCalc.calc4(newIn)
                else:
                    goodSet = False
            elif inPop[2]: #Ft
                 if self.test_nums([self.inputs[0].get(),self.inputs[3].get(),self.inputs[2].get()]):
                    newIn = self.inCast()
                    newCalc.calc1(newIn)
                    newCalc.calc5(newIn)
                 else:
                    goodSet = False
            elif inPop[4]: #Ff
                if self.test_nums([self.inputs[0].get(),self.inputs[3].get(),self.inputs[4].get()]):
                    newIn = self.inCast()
                    newCalc.calc1(newIn)
                    newCalc.calc6(newIn)
                else:
                    goodSet = False
            elif inPop[5]: #Nf
                if self.test_nums([self.inputs[0].get(),self.inputs[3].get(),self.inputs[5].get()]):
                    newIn = self.inCast()
                    newCalc.calc1(newIn)
                    newCalc.calc7(newIn)
                else:
                    goodSet = False
            elif inPop[7]: #Fs
                if self.test_nums([self.inputs[0].get(),self.inputs[3].get(),self.inputs[7].get()]):
                    newIn = self.inCast()
                    newCalc.calc1(newIn)
                    newCalc.calc8(newIn)
                else:
                    goodSet = False
            elif inPop[8]: #Ns
                if self.test_nums([self.inputs[0].get(),self.inputs[3].get(),self.inputs[8].get()]):
                    newIn = self.inCast()
                    newCalc.calc1(newIn)
                    newCalc.calc9(newIn)
                else:
                    goodSet = False
            else: #not enough inputs
                goodSet = False
        elif inPop[0] and inPop[6]: #alpha and phi
            if inPop[1]: #Fc
                if self.test_nums([self.inputs[0].get(),self.inputs[6].get(),self.inputs[1].get()]):
                    newIn = self.inCast()
                    newCalc.calc2(newIn)
                    newCalc.calc4(newIn)
                else:
                    goodSet = False
            elif inPop[2]: #Ft
                if self.test_nums([self.inputs[0].get(),self.inputs[6].get(),self.inputs[2].get()]):
                    newIn = self.inCast()
                    newCalc.calc2(newIn)
                    newCalc.calc5(newIn)
                else:
                    goodSet = False
            elif inPop[4]: #Ff
                if self.test_nums([self.inputs[0].get(),self.inputs[6].get(),self.inputs[4].get()]):
                    newIn = self.inCast()
                    newCalc.calc2(newIn)
                    newCalc.calc6(newIn)
                else:
                    goodSet = False
            elif inPop[5]: #Nf
                if self.test_nums([self.inputs[0].get(),self.inputs[6].get(),self.inputs[5].get()]):
                    newIn = self.inCast()
                    newCalc.calc2(newIn)
                    newCalc.calc7(newIn)
                else:
                    goodSet = False
            elif inPop[7]: #Fs
                if self.test_nums([self.inputs[0].get(),self.inputs[6].get(),self.inputs[7].get()]):
                    newIn = self.inCast()
                    newCalc.calc2(newIn)
                    newCalc.calc8(newIn)
                else:
                    goodSet = False
            elif inPop[8]: #Ns
                if self.test_nums([self.inputs[0].get(),self.inputs[6].get(),self.inputs[8].get()]):
                    newIn = self.inCast()
                    newCalc.calc2(newIn)
                    newCalc.calc9(newIn)
                else:
                    goodSet = False
            else: #not enough inputs
                goodSet = False
        elif inPop[3] and inPop[6]: #beta and phi
            if inPop[1]: #Fc
                if self.test_nums([self.inputs[3].get(),self.inputs[6].get(),self.inputs[1].get()]):
                    newIn = self.inCast()
                    newCalc.calc3(newIn)
                    newCalc.calc4(newIn)
                else:
                    goodSet = False
            elif inPop[2]: #Ft
                if self.test_nums([self.inputs[3].get(),self.inputs[6].get(),self.inputs[2].get()]):
                    newIn = self.inCast()
                    newCalc.calc3(newIn)
                    newCalc.calc5(newIn)
                else:
                    goodSet = False
            elif inPop[4]: #Ff
                if self.test_nums([self.inputs[3].get(),self.inputs[6].get(),self.inputs[4].get()]):
                    newIn = self.inCast()
                    newCalc.calc3(newIn)
                    newCalc.calc6(newIn)
                else:
                    goodSet = False
            elif inPop[5]: #Nf
                if self.test_nums([self.inputs[3].get(),self.inputs[6].get(),self.inputs[5].get()]):
                    newIn = self.inCast()
                    newCalc.calc3(newIn)
                    newCalc.calc7(newIn)
                else:
                    goodSet = False
            elif inPop[7]: #Fs
                if self.test_nums([self.inputs[3].get(),self.inputs[6].get(),self.inputs[7].get()]):
                    newIn = self.inCast()
                    newCalc.calc3(newIn)
                    newCalc.calc8(newIn)
                else:
                    goodSet = False
            elif inPop[8]: #Ns
                if self.test_nums([self.inputs[3].get(),self.inputs[6].get(),self.inputs[8].get()]):
                    newIn = self.inCast()
                    newCalc.calc3(newIn)
                    newCalc.calc9(newIn)
                else:
                    goodSet = False
            else: #not enough inputs
                goodSet = False
        elif inPop[0] and inPop[1] and inPop[2]: # alpha,F_c,F_t
            if self.test_nums([self.inputs[0].get(),self.inputs[1].get(),self.inputs[2].get()]):
                newIn = self.inCast()
                newCalc.calcX(newIn)
            else:
                goodSet = False
        else: #not enough inputs
            goodSet = False
        return goodSet

#-------------------------------------------------------------------------------
''' object controlling Power Calculations tab '''
class powerTab():
    ''' initialize instance of powerTab, builds power calculations tab '''
    def __init__(self,tabControl):
        # Power calculations tab object
        self.tab = ttk.Frame(tabControl)
        # initialize arrays
        self.inputs = np.array([]) # array of input objects
        self.inbox = np.array([]) # array of input boxes
        self.outputs = np.array([]) # array of output objects
        self.outbox = np.array([]) # array of output boxes
        self.extbox = np.array([]) # array of input(from force) boxes
        # instructions
        inst = "\n Instructions: \n\n               Enter V, w, and \n                 t or t_c \n"
        ttk.Label(self.tab,text=inst).grid(column=0,row=0,columnspan=3)
        ttk.Label(self.tab,text='      ').grid(column=0,row=1)
        # description
        desc = "\n This tab will calculate outputs and update the Chip Diagram tab \n when update is pressed. \n"
        ttk.Label(self.tab,text=desc).grid(column=4,row=0,columnspan=6)
        # list of variables from force tab
        varLabels = ["Cutting Force","Rake Angle","Friction Force","Friction Angle",
                     "Shear Force","Shear Angle"]
        var2 = ["(F_c)","(alpha)","(F_f)","(beta)","(F_s)","(phi)"]
        dims = ["N","deg","N","deg","N","deg"]
        ttk.Label(self.tab,text="Variables:").grid(column=1,row=1,columnspan=2)
        ttk.Label(self.tab,text="[dim] ").grid(column=3,row=1)
        ttk.Label(self.tab,text="From Force Tab:").grid(column=4,row=1)
        # display variables, build boxes
        for i in range(0,len(varLabels)):
            ttk.Label(self.tab,text=varLabels[i]).grid(column=1,row=i+2)
            ttk.Label(self.tab,text=var2[i]).grid(column=2,row=i+2)
            ttk.Label(self.tab,text=dims[i]).grid(column=3,row=i+2)
            self.extbox = np.append(self.extbox,ttk.Entry(self.tab,width=12))
            self.extbox[i].grid(column=4,row=i+2)
            self.extbox[i].config(state="readonly")
        # set inputs under transferred variables
        offset = len(varLabels)
        # list of inputs
        varLabels = ["Feedrate","Depth of Cut","Chip Thickness","Width of Cut"]
        var2 = ["(V)","(t)","(t_c)","(w)"]
        dims = ["mm/s","mm","mm","mm"]
        ttk.Label(self.tab,text="Inputs:").grid(column=4,row=offset+2)
        # display inputs, build boxes
        for i in range(0,len(varLabels)):
            ttk.Label(self.tab,text=varLabels[i]).grid(column=1,row=i+3+offset)
            ttk.Label(self.tab,text=var2[i]).grid(column=2,row=i+3+offset)
            ttk.Label(self.tab,text=dims[i]).grid(column=3,row=i+3+offset)
            self.inputs = np.append(self.inputs,tk.StringVar())
            self.inbox = np.append(self.inbox,ttk.Entry(self.tab,width=12,textvariable=self.inputs[i]))
            self.inbox[i].grid(column=4,row=i+3+offset)   
        # list of outputs
        varLabels = ["Feedrate","Chip Velocity","Shear Velocity","Cutting Ratio","Depth of Cut",
                     "Chip Thickness","Material Removal Rate","Cutting Energy",
                     "Friction Energy","Shear Energy","Coefficient of Friction","Shear Stress","Shear Strain"]
        var2 = ["(V)","(V_c)","(V_s)","(r)","(t)","(t_c)","(MRR)","(u_c)","(u_f)","(u_s)","(mu)","(Tau)","(Gamma)"]
        dims = ["mm/s","mm/s","mm/s","-","mm","mm","mm3/s","J/cm3","J/cm3","J/cm3","-","kPa","-"]
        ttk.Label(self.tab,text="Variables:").grid(column=5,row=1,columnspan=2)
        ttk.Label(self.tab,text="[dim]").grid(column=7,row=1)
        ttk.Label(self.tab,text="Outputs:").grid(column=8,row=1)
        # display outputs, build boxes
        for i in range(0,len(varLabels)):
            ttk.Label(self.tab,text=varLabels[i]).grid(column=5,row=i+2)
            ttk.Label(self.tab,text=var2[i]).grid(column=6,row=i+2)
            ttk.Label(self.tab,text=dims[i]).grid(column=7,row=i+2)
            self.outbox = np.append(self.outbox,ttk.Entry(self.tab,width=12))
            self.outbox[i].grid(column=8,row=i+2)
            self.outbox[i].config(state="readonly")
            
    ''' test an array of input strings to see if they contain numbers '''
    def test_nums(self,nums):
        for i in range(0,len(nums)):
            try:
                float(nums[i])
            except:
                return False
        return True

    ''' cast inputs to float '''
    def inCast(self):
        newIn = np.array([])
        for i in range(0,len(self.inputs)):
            try: # good input
                newIn = np.append(newIn,float(self.inputs[i].get()))
            except: # empties and others to 0.0
                newIn = np.append(newIn,0.0)
        return newIn

    ''' define input set and calculate remaining values '''
    def inpTest(self,newCalc):
        inPop = np.array([]) # array for checking populated inputs
        inSet = np.array([]) # array for type check
        for i in range(0,len(self.inputs)):
            if self.inputs[i].get(): # not empty
                inPop = np.append(inPop,True)
            else: # is empty
                inPop = np.append(inPop,False)
            inSet = np.append(inSet,self.inputs[i].get())
        # initialize output boolean
        goodSet = True
        # test input arrangement
        if inPop[0] and inPop[3]: # V,w
            if inPop[1] and not inPop[2]: # t
                if self.test_nums([inSet[0],inSet[3],inSet[1]]): # numbers provided
                    newIn = self.inCast()
                    newCalc.calctc(newIn) # calculate remaining values
                else: # bad values
                    goodSet = False
            elif inPop[2] and not inPop[1]: # tc
                if self.test_nums([inSet[0],inSet[3],inSet[2]]): # numbers provided
                    newIn = self.inCast()
                    newCalc.calct(newIn) # calculate remaining values
                else: # bad values
                    goodSet = False
            else: # bad values
                goodSet = False
        else: # bad values
            goodSet = False
        return goodSet
    
#-------------------------------------------------------------------------------
''' calculations for forceTab '''
class calcForce():
    def __init__(self): # initialize variables
        self.alpha = 0.0
        self.beta = 0.0
        self.phi = 0.0
        self.Fc = 0.0
        self.Ft = 0.0
        self.R = 0.0
        self.Ff = 0.0
        self.Nf = 0.0
        self.Fs = 0.0
        self.Ns = 0.0
    
    def calc1(self,newIn): # with alpha, beta given
        self.alpha = newIn[0]
        self.beta = newIn[3]
        self.phi = 45.0-(self.beta/2)+(self.alpha/2)
        
    def calc2(self,newIn): # with alpha, phi given
        self.alpha = newIn[0]
        self.phi = newIn[6]
        self.beta = 2*(45.0-self.phi+(self.alpha/2))
        
    def calc3(self,newIn): # with beta, phi given
        self.beta = newIn[3]
        self.phi = newIn[6]
        self.alpha = 2*(self.phi-45.0+(self.beta/2))
        
    def calc4(self,newIn): # with Fc given
        self.Fc = newIn[1]
        self.R = self.Fc/math.cos(math.radians(self.beta-self.alpha))
        self.Ft = self.R*math.sin(math.radians(self.beta-self.alpha))
        self.Ff = self.R*math.sin(math.radians(self.beta))
        self.Nf = self.R*math.cos(math.radians(self.beta))
        self.Fs = self.R*math.cos(math.radians(self.phi+self.beta-self.alpha))
        self.Ns = self.R*math.sin(math.radians(self.phi+self.beta-self.alpha))
        
    def calc5(self,newIn): # with Ft given
        self.Ft = newIn[2]
        self.R = self.Ft/math.sin(math.radians(self.beta-self.alpha))
        self.Fc = self.R*math.cos(math.radians(self.beta-self.alpha))
        self.Ff = self.R*math.sin(math.radians(self.beta))
        self.Nf = self.R*math.cos(math.radians(self.beta))
        self.Fs = self.R*math.cos(math.radians(self.phi+self.beta-self.alpha))
        self.Ns = self.R*math.sin(math.radians(self.phi+self.beta-self.alpha))
        
    def calc6(self,newIn): # with Ff given
        self.Ff = newIn[4]
        self.R = self.Ff/math.sin(math.radians(self.beta))
        self.Nf = self.R*math.cos(math.radians(self.beta))
        self.Fc = self.R*math.cos(math.radians(self.beta-self.alpha))
        self.Ft = self.R*math.sin(math.radians(self.beta-self.alpha))
        self.Nf = self.R*math.cos(math.radians(self.beta))
        self.Fs = self.R*math.cos(math.radians(self.phi+self.beta-self.alpha))
        self.Ns = self.R*math.sin(math.radians(self.phi+self.beta-self.alpha))
        
    def calc7(self,newIn): # with Nf given
        self.Nf = newIn[5]
        self.R = self.Nf/math.cos(math.radians(self.beta))
        self.Ff = self.R*math.sin(math.radians(self.beta))
        self.Fc = self.R*math.cos(math.radians(self.beta-self.alpha))
        self.Ft = self.R*math.sin(math.radians(self.beta-self.alpha))
        self.Fs = self.R*math.cos(math.radians(self.phi+self.beta-self.alpha))
        self.Ns = self.R*math.sin(math.radians(self.phi+self.beta-self.alpha))
        
    def calc8(self,newIn): # with Fs given
        self.Fs = newIn[7]
        self.R = self.Fs/math.cos(math.radians(self.phi+self.beta-self.alpha))
        self.Ns = self.R*math.sin(math.radians(self.phi+self.beta-self.alpha))
        self.Fc = self.R*math.cos(math.radians(self.beta-self.alpha))
        self.Ft = self.R*math.sin(math.radians(self.beta-self.alpha))
        self.Ff = self.R*math.sin(math.radians(self.beta))
        self.Nf = self.R*math.cos(math.radians(self.beta))
        
    def calc9(self,newIn): # with Ns given
        self.Ns = newIn[8]
        self.R = self.Ns/math.sin(math.radians(self.phi+self.beta-self.alpha))
        self.Fs = self.R*math.cos(math.radians(self.phi+self.beta-self.alpha))
        self.Fc = self.R*math.cos(math.radians(self.beta-self.alpha))
        self.Ft = self.R*math.sin(math.radians(self.beta-self.alpha))
        self.Ff = self.R*math.sin(math.radians(self.beta))
        self.Nf = self.R*math.cos(math.radians(self.beta))
        
    def calcX(self,newIn): # with alpha, Fc, Ft given
        self.alpha = newIn[0]
        self.Fc = newIn[1]
        self.Ft = newIn[2]
        self.R = math.hypot(self.Fc,self.Ft)
        self.beta = math.degrees(math.radians(self.alpha) + math.acos(self.Fc/self.R))
        self.phi = 45.0-(self.beta/2)+(self.alpha/2)
        self.Ff = self.R*math.sin(math.radians(self.beta))
        self.Nf = self.R*math.cos(math.radians(self.beta))
        self.Fs = self.R*math.cos(math.radians(self.phi+self.beta-self.alpha))
        self.Ns = self.R*math.sin(math.radians(self.phi+self.beta-self.alpha))
        
#-------------------------------------------------------------------------------
''' calculations for powerTab '''
class calcPower():
    def __init__(self,ins1): # initialize variables
        # apply inputs from Force Tab
        self.Fc = ins1[0]
        self.alpha = ins1[1]
        self.Ff = ins1[2]
        self.beta = ins1[3]
        self.Fs = ins1[4]
        self.phi = ins1[5]
        self.V = 0.0
        self.t = 0.0
        self.tc = 0.0
        self.w = 0.0
        self.MRR = 0.0
        self.Vc = 0.0
        self.Vs = 0.0
        self.r = 0.0
        self.mu = 0.0
        self.uc = 0.0
        self.uf = 0.0
        self.us = 0.0
        self.Tau = 0.0
        self.Gamma = 0.0
        
    def calct(self,newIn): # with t, w given
        self.V = newIn[0]
        self.tc = newIn[2]
        self.w = newIn[3]
        self.t = (self.tc/math.sin(math.radians(self.alpha+90-self.phi)))*math.sin(math.radians(self.phi))
        self.calcRem()
        
    def calctc(self,newIn): # with tc, w given
        self.V = newIn[0]
        self.t = newIn[1]
        self.w = newIn[3]
        self.tc = (self.t/math.sin(math.radians(self.phi)))*math.sin(math.radians(self.alpha+90-self.phi))
        self.calcRem()
        
    def calcRem(self): # calculate remaining outputs
        self.MRR = self.t*self.w*self.V
        self.Vc = self.V*(math.sin(math.radians(self.phi))/math.cos(math.radians(self.phi-self.alpha)))
        self.Vs = self.V*(math.cos(math.radians(self.alpha))/math.cos(math.radians(self.phi-self.alpha)))
        self.r = self.t / self.tc
        self.mu = math.tan(math.radians(self.beta))
        self.uc = self.Fc*self.V/self.MRR
        self.uf = self.Ff*self.Vc/self.MRR
        self.us = self.Fs*self.Vs/self.MRR
        self.Tau = self.Fs / ((self.t*self.w/1000.)/math.sin(math.radians(self.phi)))
        self.Gamma = math.cos(math.radians(self.alpha))/(math.sin(math.radians(self.phi))*math.cos(math.radians(self.phi-self.alpha)))
        

