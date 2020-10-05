from tkinter import *
from math import *
from functools import partial

global aux_mudar_constante
aux_mudar_constante = ["Pa", "m^3", "kg.m^-3"]

def DensidadeGasCalculo(tfDensD, tfDensP, tfDensM, lbrR_D, tfDensT, uP, uT, uD):
    frToolBarBottom.grid_forget()
    Rv = lbrR_D.cget("text").split(" ")
    if "x10^" in Rv[0]:
        valores = Rv[0].split("x10^")
        final = valores[0]+"e"+valores[1]
        R = float(final)
    else:
        R = float(Rv[0])
    unidadePressao = uP.get()
    unidadeTemperatura = uT.get()
    unidadeDensidade = uD.get()
    fator_kg = 1
    if unidadeDensidade[0:2] == 'kg':
        fator_kg = 1000

    if len(tfDensD.get()) == 0 and len(tfDensP.get()) == 0 and len(tfDensM.get()) == 0 and len(tfDensT.get()) == 0:
        lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
        frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
        frToolBarBottom.config(bg = "red")
        lbAviso.grid(row = 0, column = 0)
        frToolBarBottom.columnconfigure(0, weight = 1)
        frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfDensD.get()) != 0 and len(tfDensP.get()) != 0 and len(tfDensM.get()) != 0 and len(tfDensT.get()) != 0:
        d = float(tfDensD.get())
        P = float(tfDensP.get())
        M = float(tfDensM.get())
        T = float(tfDensT.get())
        
        if d == (P*M)/(R*T*fator_kg):
            lbAviso = Label(frToolBarBottom, text = "Valid equality", bg = "green", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            lbAviso = Label(frToolBarBottom, text = "Invalid equality", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfDensD.get()) == 0:
        if len(tfDensP.get()) == 0 or len(tfDensM.get()) == 0 or len(tfDensT.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            P = float(tfDensP.get())
            M = float(tfDensM.get())
            T = float(tfDensT.get())
            d = (P*M)/(R*T*fator_kg)

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbv1Desejado = Label(frToolBarBottom, text = "d = "+str(d)+" "+unidadeDensidade, bg = "green", width = 40)
            lbv1Desejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfDensP.get()) == 0:
        if len(tfDensD.get()) == 0 or len(tfDensM.get()) == 0 or len(tfDensT.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            d = float(tfDensD.get())
            M = float(tfDensM.get())
            T = float(tfDensT.get())
            P = (d*R*T*fator_kg)/M

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbv1Desejado = Label(frToolBarBottom, text = "P = "+str(P)+" "+unidadePressao, bg = "green", width = 40)
            lbv1Desejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfDensM.get()) == 0:
        if len(tfDensD.get()) == 0 or len(tfDensP.get()) == 0 or len(tfDensT.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            d = float(tfDensD.get())
            P = float(tfDensP.get())
            T = float(tfDensT.get())
            M = (d*R*T*fator_kg/P)

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbv1Desejado = Label(frToolBarBottom, text = "M = "+str(M)+" "+"g.mol^-1", bg = "green", width = 40)
            lbv1Desejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfDensT.get()) == 0:
        if len(tfDensD.get()) == 0 or len(tfDensP.get()) == 0 or len(tfDensM.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else: 
            d = float(tfDensD.get())
            P = float(tfDensP.get())
            M = float(tfDensM.get())
            T = (P*M)/(d*R*fator_kg)

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbv1Desejado = Label(frToolBarBottom, text = "T = "+str(T)+" "+unidadeTemperatura, bg = "green", width = 40)
            lbv1Desejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)

def TranformacaoIsovolumetricaCalculo(tfIsovP1, tfIsovT1, tfIsovP2, tfIsovT2, uP, uT):
    frToolBarBottom.grid_forget()
    unidadePressao = uP.get()
    unidadeTemperatura = uT.get()

    if len(tfIsovP1.get()) == 0 and len(tfIsovT1.get()) == 0 and len(tfIsovP2.get()) == 0 and len(tfIsovT2.get()) == 0:
        lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
        frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
        frToolBarBottom.config(bg = "red")
        lbAviso.grid(row = 0, column = 0)
        frToolBarBottom.columnconfigure(0, weight=1)
        frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfIsovP1.get()) != 0 and len(tfIsovT1.get()) != 0 and len(tfIsovP2.get()) != 0 and len(tfIsovT2.get()) != 0:
        P1 = float(tfIsovP1.get())
        T1 = float(tfIsovT1.get())
        P2 = float(tfIsovP2.get())
        T2 = float(tfIsovT2.get())

        if P1/T1 == P2/T2:
            lbAviso = Label(frToolBarBottom, text = "Valid equality", bg = "green", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            lbAviso = Label(frToolBarBottom, text = "Invalid equality", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)

    elif len(tfIsovP1.get()) == 0:
            if len(tfIsovT1.get()) == 0 or len(tfIsovP2.get()) == 0 or len(tfIsovT2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                T1 = float(tfIsovT1.get())
                P2 = float(tfIsovP2.get())
                T2 = float(tfIsovT2.get())
                P1 = (T1*P2)/T2

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbp1Desejado = Label(frToolBarBottom, text = "P1 = "+str(P1)+" "+unidadePressao, bg = "green", width = 40)
                lbp1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
                
    elif len(tfIsovT1.get()) == 0:
            if len(tfIsovP1.get()) == 0 or len(tfIsovP2.get()) == 0 or len(tfIsovT2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                P1 = float(tfIsovP1.get())
                P2 = float(tfIsovP2.get())
                T2 = float(tfIsovT2.get())
                T1 = (T2*P1)/P2

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbv1Desejado = Label(frToolBarBottom, text = "T1 = "+str(T1)+" "+unidadeTemperatura, bg = "green", width = 40)
                lbv1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfIsovP2.get()) == 0:
            if len(tfIsovP1.get()) == 0 or len(tfIsovT1.get()) == 0 or len(tfIsovT2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                P1 = float(tfIsovP1.get())
                T1 = float(tfIsovT1.get())
                T2 = float(tfIsovT2.get())
                P2 = (T2*P1)/T1

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbp1Desejado = Label(frToolBarBottom, text = "P2 = "+str(P2)+" "+unidadePressao, bg = "green", width = 40)
                lbp1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfIsovT2.get()) == 0:
            if len(tfIsovP1.get()) == 0 or len(tfIsovT1.get()) == 0 or len(tfIsovP2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                P1 = float(tfIsovP1.get())
                T1 = float(tfIsovT1.get())
                P2 = float(tfIsovP2.get())
                T2 = (T1*P2)/P1

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbv1Desejado = Label(frToolBarBottom, text = "T2 = "+str(T2)+" "+unidadeTemperatura, bg = "green", width = 40)
                lbv1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)

def TranformacaoIsobaricaCalculo(tfIsobV1, tfIsobT1, tfIsobV2, tfIsobT2, uV, uT):
    frToolBarBottom.grid_forget()
    unidadeVolume = uV.get()
    unidadeTemperatura = uT.get()

    if len(tfIsobV1.get()) == 0 and len(tfIsobT1.get()) == 0 and len(tfIsobV2.get()) == 0 and len(tfIsobT2.get()) == 0:
        lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
        frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
        frToolBarBottom.config(bg = "red")
        lbAviso.grid(row = 0, column = 0)
        frToolBarBottom.columnconfigure(0, weight=1)
        frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfIsobV1.get()) != 0 and len(tfIsobT1.get()) != 0 and len(tfIsobV2.get()) != 0 and len(tfIsobT2.get()) != 0:
        V1 = float(tfIsobV1.get())
        T1 = float(tfIsobT1.get())
        V2 = float(tfIsobV2.get())
        T2 = float(tfIsobT2.get())

        if V1/T1 == V2/T2:
            lbAviso = Label(frToolBarBottom, text = "Valid equality", bg = "green", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            lbAviso = Label(frToolBarBottom, text = "Invalid equality", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)

    elif len(tfIsobV1.get()) == 0:
            if len(tfIsobT1.get()) == 0 or len(tfIsobV2.get()) == 0 or len(tfIsobT2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                T1 = float(tfIsobT1.get())
                V2 = float(tfIsobV2.get())
                T2 = float(tfIsobT2.get())
                V1 = (T1*V2)/T2

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbp1Desejado = Label(frToolBarBottom, text = "V1 = "+str(V1)+" "+unidadeVolume, bg = "green", width = 40)
                lbp1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
                
    elif len(tfIsobT1.get()) == 0:
            if len(tfIsobV1.get()) == 0 or len(tfIsobV2.get()) == 0 or len(tfIsobT2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                V1 = float(tfIsobV1.get())
                V2 = float(tfIsobV2.get())
                T2 = float(tfIsobT2.get())
                T1 = (T2*V1)/V2

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbv1Desejado = Label(frToolBarBottom, text = "T1 = "+str(T1)+" "+unidadeTemperatura, bg = "green", width = 40)
                lbv1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfIsobV2.get()) == 0:
            if len(tfIsobV1.get()) == 0 or len(tfIsobT1.get()) == 0 or len(tfIsobT2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                V1 = float(tfIsobV1.get())
                T1 = float(tfIsobT1.get())
                T2 = float(tfIsobT2.get())
                V2 = (T2*V1)/T1

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbp1Desejado = Label(frToolBarBottom, text = "V2 = "+str(V2)+" "+unidadeVolume, bg = "green", width = 40)
                lbp1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfIsobT2.get()) == 0:
            if len(tfIsobV1.get()) == 0 or len(tfIsobT1.get()) == 0 or len(tfIsobV2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                V1 = float(tfIsobV1.get())
                T1 = float(tfIsobT1.get())
                V2 = float(tfIsobV2.get())
                T2 = (T1*V2)/V1

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbv1Desejado = Label(frToolBarBottom, text = "T2 = "+str(T2)+" "+unidadeTemperatura, bg = "green", width = 40)
                lbv1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)

def TranformacaoIsotermicaCalculo(tfIsotP1, tfIsotV1, tfIsotP2, tfIsotV2, uP, uV):
    frToolBarBottom.grid_forget()
    unidadePressao = uP.get()
    unidadeVolume = uV.get()

    if len(tfIsotP1.get()) == 0 and len(tfIsotV1.get()) == 0 and len(tfIsotP2.get()) == 0 and len(tfIsotV2.get()) == 0:
        lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
        frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
        frToolBarBottom.config(bg = "red")
        lbAviso.grid(row = 0, column = 0)
        frToolBarBottom.columnconfigure(0, weight=1)
        frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfIsotP1.get()) != 0 and len(tfIsotV1.get()) != 0 and len(tfIsotP2.get()) != 0 and len(tfIsotV2.get()) != 0:
        p1 = float(tfIsotP1.get())
        V1 = float(tfIsotV1.get())
        p2 = float(tfIsotP2.get())
        V2 = float(tfIsotV2.get())

        if p1*V1 == p2*V2:
            lbAviso = Label(frToolBarBottom, text = "Valid equality", bg = "green", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            lbAviso = Label(frToolBarBottom, text = "Invalid equality", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)

    elif len(tfIsotP1.get()) == 0:
            if len(tfIsotV1.get()) == 0 or len(tfIsotP2.get()) == 0 or len(tfIsotV2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                V1 = float(tfIsotV1.get())
                P2 = float(tfIsotP2.get())
                V2 = float(tfIsotV2.get())
                P1 = (P2*V2)/V1

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbp1Desejado = Label(frToolBarBottom, text = "P1 = "+str(P1)+" "+unidadePressao, bg = "green", width = 40)
                lbp1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
                
    elif len(tfIsotV1.get()) == 0:
            if len(tfIsotP1.get()) == 0 or len(tfIsotP2.get()) == 0 or len(tfIsotV2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                P1 = float(tfIsotP1.get())
                P2 = float(tfIsotP2.get())
                V2 = float(tfIsotV2.get())
                V1 = (P2*V2)/(P1)

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbv1Desejado = Label(frToolBarBottom, text = "V1 = "+str(V1)+" "+unidadeVolume, bg = "green", width = 40)
                lbv1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfIsotP2.get()) == 0:
            if len(tfIsotP1.get()) == 0 or len(tfIsotV1.get()) == 0 or len(tfIsotV2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                P1 = float(tfIsotP1.get())
                V1 = float(tfIsotV1.get())
                V2 = float(tfIsotV2.get())
                P2 = (P1*V1)/V2

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbv1Desejado = Label(frToolBarBottom, text = "P2 = "+str(P2)+" "+unidadePressao, bg = "green", width = 40)
                lbv1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfIsotV2.get()) == 0:
            if len(tfIsotP1.get()) == 0 or len(tfIsotV1.get()) == 0 or len(tfIsotP2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                P1 = float(tfIsotP1.get())
                V1 = float(tfIsotV1.get())
                P2 = float(tfIsotP2.get())
                V2 = (P1*V1)/P2

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbv1Desejado = Label(frToolBarBottom, text = "V2 = "+str(V2)+" "+unidadeVolume, bg = "green", width = 40)
                lbv1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)

def EquacaoDeClapyronCalculo_n(tfP_n, tfV_n, tfn_n, lbrR, tfT_n, uP, uV):
    frToolBarBottom.grid_forget()
    Rv = lbrR.cget("text").split(" ")
    if "x10^" in Rv[0]:
        valores = Rv[0].split("x10^")
        final = valores[0]+"e"+valores[1]
        R = float(final)
    else:
        R = float(Rv[0])
    unidadePressao = uP.get()
    unidadeVolume = uV.get()

    if len(tfP_n.get()) == 0 and len(tfV_n.get()) == 0 and len(tfn_n.get()) == 0 and len(tfT_n.get()) == 0:
        lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
        frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
        frToolBarBottom.config(bg = "red")
        lbAviso.grid(row = 0, column = 0)
        frToolBarBottom.columnconfigure(0, weight=1)
        frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfP_n.get()) != 0 and len(tfV_n.get()) != 0 and len(tfn_n.get()) != 0 and len(tfT_n.get()) != 0:
        P = float(tfP_n.get())
        V = float(tfV_n.get())
        n = float(tfn_n.get())
        T = float(tfT_n.get())

        if P*V == n*R*T:
            lbAviso = Label(frToolBarBottom, text = "Valid equality", bg = "green", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            lbAviso = Label(frToolBarBottom, text = "Invalid equality", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)

    elif len(tfP_n.get()) == 0:
            if len(tfV_n.get()) == 0 or len(tfn_n.get()) == 0 or len(tfT_n.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                V = float(tfV_n.get())
                n = float(tfn_n.get())
                T = float(tfT_n.get())
                P = (n*R*T)/V

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbPDesejado = Label(frToolBarBottom, text = "P = "+str(P)+" "+unidadePressao, bg = "green", width = 40)
                lbPDesejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
                
    elif len(tfV_n.get()) == 0:
            if len(tfP_n.get()) == 0 or len(tfn_n.get()) == 0 or len(tfT_n.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                P = float(tfP_n.get())
                n = float(tfn_n.get())
                T = float(tfT_n.get())
                V = (n*R*T)/P

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbVDesejado = Label(frToolBarBottom, text = "V = "+str(V)+" "+unidadeVolume, bg = "green", width = 40)
                lbVDesejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfn_n.get()) == 0:
            if len(tfP_n.get()) == 0 or len(tfV_n.get()) == 0 or len(tfT_n.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                P = float(tfP_n.get())
                V = float(tfV_n.get())
                T = float(tfT_n.get())
                n = (P*V)/(R*T)

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbnDesejado = Label(frToolBarBottom, text = "n = "+str(n)+" mol(s)", bg = "green", width = 40)
                lbnDesejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfT_n.get()) == 0:
            if len(tfP_n.get()) == 0 or len(tfV_n.get()) == 0 or len(tfn_n.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                P = float(tfP_n.get())
                V = float(tfV_n.get())
                n = float(tfn_n.get())
                T = (P*V)/(n*R)

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbTDesejado = Label(frToolBarBottom, text = "T = "+str(T)+" K", bg = "green", width = 40)
                lbTDesejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)

def EquacaoDeClapyronCalculo_M(tfP_M, tfV_M, tfm_M, tfM_M, lbrR, tfT_M, uP, uV):
    frToolBarBottom.grid_forget()
    Rv = lbrR.cget("text").split(" ")
    if "x10^" in Rv[0]:
        valores = Rv[0].split("x10^")
        final = valores[0]+"e"+valores[1]
        R = float(final)
    else:
        R = float(Rv[0])
    unidadePressao = uP.get()
    unidadeVolume = uV.get()

    if len(tfP_M.get()) == 0 and len(tfV_M.get()) == 0 and len(tfm_M.get()) == 0 and len(tfM_M.get()) == 0 and len(tfT_M.get()) == 0:
        lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
        frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
        frToolBarBottom.config(bg = "red")
        lbAviso.grid(row = 0, column = 0)
        frToolBarBottom.columnconfigure(0, weight=1)
        frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfP_M.get()) != 0 and len(tfV_M.get()) != 0 and len(tfm_M.get()) != 0 and len(tfM_M.get()) != 0 and len(tfT_M.get()) != 0:
        P = float(tfP_M.get())
        V = float(tfV_M.get())
        m = float(tfm_M.get())
        M = float(tfM_M.get())
        T = float(tfT_M.get())

        if P*V == (m/M)*R*T:
            lbAviso = Label(frToolBarBottom, text = "Valid equality", bg = "green", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            lbAviso = Label(frToolBarBottom, text = "Invalid equality", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)

    elif len(tfP_M.get()) == 0:
        if len(tfV_M.get()) == 0 or len(tfm_M.get()) == 0 or len(tfM_M.get()) == 0 or len(tfT_M.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            V = float(tfV_M.get())
            m = float(tfm_M.get())
            M = float(tfM_M.get())
            T = float(tfT_M.get())
            P = (m*R*T)/(M*V)

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbPDesejado = Label(frToolBarBottom, text = "P = "+str(P)+" "+unidadePressao, bg = "green", width = 40)
            lbPDesejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfV_M.get()) == 0:
        if len(tfP_M.get()) == 0 or len(tfm_M.get()) == 0 or len(tfT_M.get()) == 0 or len(tfM_M.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            P = float(tfP_M.get())
            m = float(tfm_M.get())
            M = float(tfM_M.get())
            T = float(tfM_M.get())
            V = (m*R*T)/(M*P)

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbVDesejado = Label(frToolBarBottom, text = "V = "+str(V)+" "+unidadeVolume, bg = "green", width = 40)
            lbVDesejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfm_M.get()) == 0:
        if len(tfP_M.get()) == 0 or len(tfV_M.get()) == 0 or len(tfM_M.get()) == 0 or len(tfT_M.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            P = float(tfP_M.get())
            V = float(tfV_M.get())
            M = float(tfM_M.get())
            T = float(tfT_M.get())
            m = (P*V*M)/(R*T)

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbnDesejado = Label(frToolBarBottom, text = "m = "+str(m)+" g", bg = "green", width = 40)
            lbnDesejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfM_M.get()) == 0:
        if len(tfP_M.get()) == 0 or len(tfV_M.get()) == 0 or len(tfm_M.get()) == 0 or len(tfT_M.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            P = float(tfP_M.get())
            V = float(tfV_M.get())
            m = float(tfm_M.get())
            T = float(tfT_M.get())
            M = (m*R*T)/(P*V)

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbTDesejado = Label(frToolBarBottom, text = "M = "+str(M)+" g.mol^-1", bg = "green", width = 40)
            lbTDesejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfT_M.get()) == 0:
        if len(tfP_M.get()) == 0 or len(tfV_M.get()) == 0 or len(tfm_M.get()) == 0 or len(tfM_M.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            P = float(tfP_M.get())
            V = float(tfV_M.get())
            m = float(tfm_M.get())
            M = float(tfM_M.get())
            T = (M*P*V)/(R*m)

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbTDesejado = Label(frToolBarBottom, text = "T = "+str(T)+" K", bg = "green", width = 40)
            lbTDesejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
    
def EquacaoDeClapyronCalculo_N(tfP_N, tfV_N, tfN_N, lbrk, tfT_N, uP, uV):
    frToolBarBottom.grid_forget()
    kv = lbrk.cget("text").split(" ")
    if "x10^" in kv[0]:
        valores = kv[0].split("x10^")
        final = valores[0]+"e"+valores[1]
        k = float(final)
    else:
        k = float(kv[0])
    unidadePressao = uP.get()
    unidadeVolume = uV.get()

    if len(tfP_N.get()) == 0 and len(tfV_N.get()) == 0 and len(tfN_N.get()) == 0 and len(tfT_N.get()) == 0:
        lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
        frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
        frToolBarBottom.config(bg = "red")
        lbAviso.grid(row = 0, column = 0)
        frToolBarBottom.columnconfigure(0, weight=1)
        frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfP_N.get()) != 0 and len(tfV_N.get()) != 0 and len(tfN_N.get()) != 0 and len(tfT_N.get()) != 0:
        P = float(tfP_N.get())
        V = float(tfV_N.get())
        N = float(tfN_N.get())
        T = float(tfT_N.get())

        if P*V == N*k*T:
            lbAviso = Label(frToolBarBottom, text = "Valid equality", bg = "green", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            lbAviso = Label(frToolBarBottom, text = "Invalid equality", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)

    elif len(tfP_N.get()) == 0:
        if len(tfV_N.get()) == 0 or len(tfN_N.get()) == 0 or len(tfT_N.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            V = float(tfV_N.get())
            N = float(tfN_N.get())
            T = float(tfT_N.get())
            P = (N*k*T)/V

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbPDesejado = Label(frToolBarBottom, text = "P = "+str(P)+" "+unidadePressao, bg = "green", width = 40)
            lbPDesejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
            
    elif len(tfV_N.get()) == 0:
        if len(tfP_N.get()) == 0 or len(tfN_N.get()) == 0 or len(tfT_N.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            P = float(tfP_N.get())
            N = float(tfN_N.get())
            T = float(tfT_N.get())
            V = (N*k*T)/P

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbVDesejado = Label(frToolBarBottom, text = "V = "+str(V)+" "+unidadeVolume, bg = "green", width = 40)
            lbVDesejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfN_N.get()) == 0:
        if len(tfP_N.get()) == 0 or len(tfV_N.get()) == 0 or len(tfT_N.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            P = float(tfP_N.get())
            V = float(tfV_N.get())
            T = float(tfT_N.get())
            N = (P*V)/(k*T)

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbnDesejado = Label(frToolBarBottom, text = "N = "+str(N)+" particles", bg = "green", width = 40)
            lbnDesejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfT_N.get()) == 0:
        if len(tfP_N.get()) == 0 or len(tfV_N.get()) == 0 or len(tfN_N.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            P = float(tfP_N.get())
            V = float(tfV_N.get())
            N = float(tfN_N.get())
            T = (P*V)/(N*k)

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbTDesejado = Label(frToolBarBottom, text = "T = "+str(T)+" K", bg = "green", width = 40)
            lbTDesejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
def EquacaoDeClapyronCalculo_Na(tfP_Na, tfV_Na, tfN_Na, lbrR_Na, tfT_Na, uP, uV):
    frToolBarBottom.grid_forget()
    Rv = lbrR_Na.cget("text").split(" ")
    if "x10^" in Rv[0]:
        valores = Rv[0].split("x10^")
        final = valores[0]+"e"+valores[1]
        R = float(final)
    else:
        R = float(Rv[0])
    Na = 6.02*10**(23)
    unidadePressao = uP.get()
    unidadeVolume = uV.get()

    if len(tfP_Na.get()) == 0 and len(tfV_Na.get()) == 0 and len(tfN_Na.get()) == 0 and len(tfT_Na.get()) == 0:
        lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
        frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
        frToolBarBottom.config(bg = "red")
        lbAviso.grid(row = 0, column = 0)
        frToolBarBottom.columnconfigure(0, weight=1)
        frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfP_Na.get()) != 0 and len(tfV_Na.get()) != 0 and len(tfN_Na.get()) != 0 and len(tfT_Na.get()) != 0:
        P = float(tfP_Na.get())
        V = float(tfV_Na.get())
        N = float(tfN_Na.get())
        T = float(tfT_Na.get())

        if P*V == (N/Na)*R*T:
            lbAviso = Label(frToolBarBottom, text = "Valid equality", bg = "green", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            lbAviso = Label(frToolBarBottom, text = "Invalid equality", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)

    elif len(tfP_Na.get()) == 0:
        if len(tfV_Na.get()) == 0 or len(tfN_Na.get()) == 0 or len(tfT_Na.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            V = float(tfV_Na.get())
            N = float(tfN_Na.get())
            T = float(tfT_Na.get())
            P = (N*R*T)/(Na*V)

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbPDesejado = Label(frToolBarBottom, text = "P = "+str(P)+" "+unidadePressao, bg = "green", width = 40)
            lbPDesejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
            
    elif len(tfV_Na.get()) == 0:
        if len(tfP_Na.get()) == 0 or len(tfN_Na.get()) == 0 or len(tfT_Na.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            P = float(tfP_Na.get())
            N = float(tfN_Na.get())
            T = float(tfT_Na.get())
            V = (N*R*T)/(Na*P)

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbVDesejado = Label(frToolBarBottom, text = "V = "+str(V)+" "+unidadeVolume, bg = "green", width = 40)
            lbVDesejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfN_Na.get()) == 0:
        if len(tfP_Na.get()) == 0 or len(tfV_Na.get()) == 0 or len(tfT_Na.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            P = float(tfP_Na.get())
            V = float(tfV_Na.get())
            T = float(tfT_Na.get())
            N = (P*V*Na)/(R*T)

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbnDesejado = Label(frToolBarBottom, text = "N = "+str(N)+" particles", bg = "green", width = 40)
            lbnDesejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfT_Na.get()) == 0:
        if len(tfP_Na.get()) == 0 or len(tfV_Na.get()) == 0 or len(tfN_Na.get()) == 0:
            lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            P = float(tfP_Na.get())
            V = float(tfV_Na.get())
            N = float(tfN_Na.get())
            T = (P*V*Na)/(N*R)

            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbTDesejado = Label(frToolBarBottom, text = "T = "+str(T)+" K", bg = "green", width = 40)
            lbTDesejado.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight = 1)
            frToolBarBottom.rowconfigure(0, weight = 1)

def EquacaoGeralDosGasesCalculo(tfP1, tfV1, tfT1, tfP2, tfV2, tfT2, uP, uV, uT):
    frToolBarBottom.grid_forget()
    unidadePressao = uP.get()
    unidadeVolume = uV.get()
    unidadeTemperatura = uT.get()

    if len(tfP1.get()) == 0 and len(tfV1.get()) == 0 and len(tfT1.get()) == 0 and len(tfP2.get()) == 0 and len(tfV2.get()) == 0 and len(tfT2.get()) == 0:
        lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
        frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
        frToolBarBottom.config(bg = "red")
        lbAviso.grid(row = 0, column = 0)
        frToolBarBottom.columnconfigure(0, weight=1)
        frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfP1.get()) != 0 and len(tfV1.get()) != 0 and len(tfT1.get()) != 0 and len(tfP2.get()) != 0 and len(tfV2.get()) != 0 and len(tfT2.get()) != 0:
        p1 = float(tfP1.get())
        V1 = float(tfV1.get())
        T1 = float(tfT1.get())
        p2 = float(tfP2.get())
        V2 = float(tfV2.get())
        T2 = float(tfT2.get())

        if (p1*V1)/T1 == (p2*V2)/T2:
            lbAviso = Label(frToolBarBottom, text = "Valid equality", bg = "green", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "green")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)
        else:
            lbAviso = Label(frToolBarBottom, text = "Invalid equality", bg = "red", width = 40)
            frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
            frToolBarBottom.config(bg = "red")
            lbAviso.grid(row = 0, column = 0)
            frToolBarBottom.columnconfigure(0, weight=1)
            frToolBarBottom.rowconfigure(0, weight = 1)

    elif len(tfP1.get()) == 0:
            if len(tfV1.get()) == 0 or len(tfT1.get()) == 0 or len(tfP2.get()) == 0 or len(tfV2.get()) == 0 or len(tfT2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                V1 = float(tfV1.get())
                T1 = float(tfT1.get())
                P2 = float(tfP2.get())
                V2 = float(tfV2.get())
                T2 = float(tfT2.get())
                p1Desejado = (T1*P2*V2)/(T2*V1)

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbp1Desejado = Label(frToolBarBottom, text = "P1 = "+str(p1Desejado)+" "+unidadePressao, bg = "green", width = 40)
                lbp1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
                
    elif len(tfV1.get()) == 0:
            if len(tfP1.get()) == 0 or len(tfT1.get()) == 0 or len(tfP2.get()) == 0 or len(tfV2.get()) == 0 or len(tfT2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                P1 = float(tfP1.get())
                T1 = float(tfT1.get())
                P2 = float(tfP2.get())
                V2 = float(tfV2.get())
                T2 = float(tfT2.get())
                v1Desejado = (T1*P2*V2)/(P1*T2)

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbv1Desejado = Label(frToolBarBottom, text = "V1 = "+str(v1Desejado)+" "+unidadeVolume, bg = "green", width = 40)
                lbv1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfT1.get()) == 0:
            if len(tfP1.get()) == 0 or len(tfV1.get()) == 0 or len(tfP2.get()) == 0 or len(tfV2.get()) == 0 or len(tfT2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                P1 = float(tfP1.get())
                V1 = float(tfV1.get())
                P2 = float(tfP2.get())
                V2 = float(tfV2.get())
                T2 = float(tfT2.get())
                t1Desejado = (T2*P1*V1)/(P2*V2)

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbv1Desejado = Label(frToolBarBottom, text = "T1 = "+str(t1Desejado)+" "+unidadeTemperatura, bg = "green", width = 40)
                lbv1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfP2.get()) == 0:
            if len(tfP1.get()) == 0 or len(tfV1.get()) == 0 or len(tfT1.get()) == 0 or len(tfV2.get()) == 0 or len(tfT2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                P1 = float(tfP1.get())
                V1 = float(tfV1.get())
                T1 = float(tfT1.get())
                V2 = float(tfV2.get())
                T2 = float(tfT2.get())
                p2Desejado = (T2*P1*V1)/(T1*V2)

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbv1Desejado = Label(frToolBarBottom, text = "P2 = "+str(p2Desejado)+" "+unidadePressao, bg = "green", width = 40)
                lbv1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfV2.get()) == 0:
            if len(tfP1.get()) == 0 or len(tfV1.get()) == 0 or len(tfT1.get()) == 0 or len(tfP2.get()) == 0 or len(tfT2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                P1 = float(tfP1.get())
                V1 = float(tfV1.get())
                T1 = float(tfT1.get())
                P2 = float(tfP2.get())
                T2 = float(tfT2.get())
                v2Desejado = (T2*P1*V1)/(P2*T1)

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbv1Desejado = Label(frToolBarBottom, text = "V2 = "+str(v2Desejado)+" "+unidadeVolume, bg = "green", width = 40)
                lbv1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)
    elif len(tfT2.get()) == 0:
            if len(tfP1.get()) == 0 or len(tfV1.get()) == 0 or len(tfT1.get()) == 0 or len(tfP2.get()) == 0 or len(tfV2.get()) == 0:
                lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red", width = 40)
                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "red")
                lbAviso.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight=1)
                frToolBarBottom.rowconfigure(0, weight = 1)
            else:
                P1 = float(tfP1.get())
                V1 = float(tfV1.get())
                T1 = float(tfT1.get())
                P2 = float(tfP2.get())
                V2 = float(tfV2.get())
                t2Desejado = (T1*P2*V2)/(P1*V1)

                frToolBarBottom.grid(row = 2, column = 0, sticky = W+E)
                frToolBarBottom.config(bg = "green")
                lbv1Desejado = Label(frToolBarBottom, text = "T2 = "+str(t2Desejado)+" "+unidadeTemperatura, bg = "green", width = 40)
                lbv1Desejado.grid(row = 0, column = 0)
                frToolBarBottom.columnconfigure(0, weight = 1)
                frToolBarBottom.rowconfigure(0, weight = 1)

def DensidadeGas():
    lbAviso.grid_forget()
    frToolBarBottom.grid_forget()
    if vetor[0] == "EqGeral":
        frEqGeral.grid_forget()
    elif vetor[0] == "EqClapeyron_n":
        frEqClapeyron_n.grid_forget()
    elif vetor[0] == "EqClapeyron_M":
        frEqClapeyron_M.grid_forget()
    elif vetor[0] == "EqClapeyron_N":
        frEqClapeyron_N.grid_forget()
    elif vetor[0] == "EqClapeyron_Na":
        frEqClapeyron_Na.grid_forget()
    elif vetor[0] == "TransfIsot":
        frTransfIsot.grid_forget()
    elif vetor[0] == "TransfIsob":
        frTransfIsob.grid_forget()
    elif vetor[0] == "TransfIsov":
        frTransfIsov.grid_forget()
    elif vetor[0] == "DensGas":
        frDensGas.grid_forget()
    vetor[0]= "DensGas"
    frDensGas.grid(row = 1, column = 0)

def TransformacaoIsovolumetrica():
    lbAviso.grid_forget()
    frToolBarBottom.grid_forget()
    if vetor[0] == "EqGeral":
        frEqGeral.grid_forget()
    elif vetor[0] == "EqClapeyron_n":
        frEqClapeyron_n.grid_forget()
    elif vetor[0] == "EqClapeyron_M":
        frEqClapeyron_M.grid_forget()
    elif vetor[0] == "EqClapeyron_N":
        frEqClapeyron_N.grid_forget()
    elif vetor[0] == "EqClapeyron_Na":
        frEqClapeyron_Na.grid_forget()
    elif vetor[0] == "TransfIsot":
        frTransfIsot.grid_forget()
    elif vetor[0] == "TransfIsob":
        frTransfIsob.grid_forget()
    elif vetor[0] == "TransfIsov":
        frTransfIsov.grid_forget()
    elif vetor[0] == "DensGas":
        frDensGas.grid_forget()
    vetor[0]= "TransfIsov"
    frTransfIsov.grid(row = 1, column = 0)

def TransformacaoIsobarica():
    lbAviso.grid_forget()
    frToolBarBottom.grid_forget()
    if vetor[0] == "EqGeral":
        frEqGeral.grid_forget()
    elif vetor[0] == "EqClapeyron_n":
        frEqClapeyron_n.grid_forget()
    elif vetor[0] == "EqClapeyron_M":
        frEqClapeyron_M.grid_forget()
    elif vetor[0] == "EqClapeyron_N":
        frEqClapeyron_N.grid_forget()
    elif vetor[0] == "EqClapeyron_Na":
        frEqClapeyron_Na.grid_forget()
    elif vetor[0] == "TransfIsot":
        frTransfIsot.grid_forget()
    elif vetor[0] == "TransfIsob":
        frTransfIsob.grid_forget()
    elif vetor[0] == "TransfIsov":
        frTransfIsov.grid_forget()
    elif vetor[0] == "DensGas":
        frDensGas.grid_forget()
    vetor[0]= "TransfIsob"
    frTransfIsob.grid(row = 1, column = 0)

def TransformacaoIsotermica():
    lbAviso.grid_forget()
    frToolBarBottom.grid_forget()
    if vetor[0] == "EqGeral":
        frEqGeral.grid_forget()
    elif vetor[0] == "EqClapeyron_n":
        frEqClapeyron_n.grid_forget()
    elif vetor[0] == "EqClapeyron_M":
        frEqClapeyron_M.grid_forget()
    elif vetor[0] == "EqClapeyron_N":
        frEqClapeyron_N.grid_forget()
    elif vetor[0] == "EqClapeyron_Na":
        frEqClapeyron_Na.grid_forget()
    elif vetor[0] == "TransfIsot":
        frTransfIsot.grid_forget()
    elif vetor[0] == "TransfIsob":
        frTransfIsob.grid_forget()
    elif vetor[0] == "TransfIsov":
        frTransfIsov.grid_forget()
    elif vetor[0] == "DensGas":
        frDensGas.grid_forget()
    vetor[0]= "TransfIsot"
    frTransfIsot.grid(row = 1, column = 0)

def EquacaoDeClapeyron(tipo):
    lbAviso.grid_forget()
    frToolBarBottom.grid_forget()
    if vetor[0] == "EqGeral":
        frEqGeral.grid_forget()
    elif vetor[0] == "EqClapeyron_n":
        frEqClapeyron_n.grid_forget()
    elif vetor[0] == "EqClapeyron_M":
        frEqClapeyron_M.grid_forget()
    elif vetor[0] == "EqClapeyron_N":
        frEqClapeyron_N.grid_forget()
    elif vetor[0] == "EqClapeyron_Na":
        frEqClapeyron_Na.grid_forget()
    elif vetor[0] == "TransfIsot":
        frTransfIsot.grid_forget()
    elif vetor[0] == "TransfIsob":
        frTransfIsob.grid_forget()
    elif vetor[0] == "TransfIsov":
        frTransfIsov.grid_forget()
    elif vetor[0] == "DensGas":
        frDensGas.grid_forget()

    if tipo == "PV = nRT":
        vetor[0] = "EqClapeyron_n"
        frEqClapeyron_n.grid(row = 1, column = 0)
    elif tipo == "PV = (m/M)RT":
        vetor[0] = "EqClapeyron_M"
        frEqClapeyron_M.grid(row = 1, column = 0)
    elif tipo == "PV = NkT":
        vetor[0] = "EqClapeyron_N"
        frEqClapeyron_N.grid(row = 1, column = 0)
    elif tipo == "PV = (N/Na)RT":
        vetor[0] = "EqClapeyron_Na"
        frEqClapeyron_Na.grid(row = 1, column = 0)


def EquacaoGeralDosGases():
    lbAviso.grid_forget()
    frToolBarBottom.grid_forget()
    if vetor[0] == "EqGeral":
        frEqGeral.grid_forget()
    elif vetor[0] == "EqClapeyron_n":
        frEqClapeyron_n.grid_forget()
    elif vetor[0] == "EqClapeyron_M":
        frEqClapeyron_M.grid_forget()
    elif vetor[0] == "EqClapeyron_N":
        frEqClapeyron_N.grid_forget()
    elif vetor[0] == "EqClapeyron_Na":
        frEqClapeyron_Na.grid_forget()
    elif vetor[0] == "TransfIsot":
        frTransfIsot.grid_forget()
    elif vetor[0] == "TransfIsob":
        frTransfIsob.grid_forget()
    elif vetor[0] == "TransfIsov":
        frTransfIsov.grid_forget()
    elif vetor[0] == "DensGas":
        frDensGas.grid_forget()
    vetor[0]= "EqGeral"
    frEqGeral.grid(row = 1, column = 0)

def mudarConstante(parametro):
    if parametro == "Pa" or parametro == "atm" or parametro == "mmHg":
        if parametro == "Pa":
            aux_mudar_constante[0] = "Pa"
            if aux_mudar_constante[1] == "m^3" or aux_mudar_constante[2] == "g.m^-3" or aux_mudar_constante[2] == "kg.m^-3":
                lbrR["text"] = "8.31 Pa.m^3.mol^-1.K^-1"
                lbrR_Na["text"] = "8.31 Pa.m^3.mol^-1.K^-1"
                lbrR_M["text"] = "8.31 Pa.m^3.mol^-1.K^-1"
                lbrR_D["text"] = "8.31 Pa.m^3.mol^-1.K^-1"
            elif aux_mudar_constante[1] == "L" or aux_mudar_constante[2] == "g.L^-1":
                lbrR["text"] = "8.31x10^3 Pa.L.mol^-1.K^-1"
                lbrR_Na["text"] = "8.31x10^3 Pa.L.mol^-1.K^-1"
                lbrR_M["text"] = "8.31x10^3 Pa.L.mol^-1.K^-1"
                lbrR_D["text"] = "8.31x10^3 Pa.L.mol^-1.K^-1"
            elif aux_mudar_constante[1] == "mL" or aux_mudar_constante[2] == "g.ml^-1":
                lbrR["text"] = "8.31x10^6 Pa.mL.mol^-1.K^-1"
                lbrR_Na["text"] = "8.31x10^6 Pa.mL.mol^-1.K^-1"
                lbrR_M["text"] = "8.31x10^6 Pa.mL.mol^-1.K^-1"
                lbrR_D["text"] = "8.31x10^6 Pa.mL.mol^-1.K^-1"

        elif parametro == "atm":
            aux_mudar_constante[0] = "atm"
            if aux_mudar_constante[1] == "m^3" or aux_mudar_constante[2] == "g.m^-3" or aux_mudar_constante[2] == "kg.m^-3":
                lbrR["text"] = "8.2x10^-5 atm.m^3.mol^-1.K^-1"
                lbrR_Na["text"] = "8.2x10^-5 atm.m^3.mol^-1.K^-1"
                lbrR_M["text"] = "8.2x10^-5 atm.m^3.mol^-1.K^-1"
                lbrR_D["text"] = "8.2x10^-5 atm.m^3.mol^-1.K^-1"
            elif aux_mudar_constante[1] == "L" or aux_mudar_constante[2] == "g.L^-1":
                lbrR["text"] = "8.2x10^-2 atm.L.mol^-1.K^-1"
                lbrR_Na["text"] = "8.2x10^-2 atm.L.mol^-1.K^-1"
                lbrR_M["text"] = "8.2x10^-2 atm.L.mol^-1.K^-1"
                lbrR_D["text"] = "8.2x10^-2 atm.L.mol^-1.K^-1"
            elif aux_mudar_constante[1] == "mL" or aux_mudar_constante[2] == "g.ml^-1":
                lbrR["text"] = "82 atm.mL.mol^-1.K^-1"
                lbrR_Na["text"] = "82 atm.mL.mol^-1.K^-1"
                lbrR_M["text"] = "82 atm.mL.mol^-1.K^-1"
                lbrR_D["text"] = "82 atm.mL.mol^-1.K^-1"

        elif parametro == "mmHg":
            aux_mudar_constante[0] = "mmHg"
            if aux_mudar_constante[1] == "m^3" or aux_mudar_constante[2] == "g.m^-3" or aux_mudar_constante[2] == "kg.m^-3":
                lbrR["text"] = "6.2x10^-2 mmHg.m^3.mol^-1.K^-1"
                lbrR_Na["text"] = "6.2x10^-2 mmHg.m^3.mol^-1.K^-1"
                lbrR_M["text"] = "6.2x10^-2 mmHg.m^3.mol^-1.K^-1"
                lbrR_D["text"] = "6.2x10^-2 mmHg.m^3.mol^-1.K^-1"
            elif aux_mudar_constante[1] == "L" or aux_mudar_constante[2] == "g.L^-1":
                lbrR["text"] = "62.32 mmHg.L.mol^-1.K^-1"
                lbrR_Na["text"] = "62.32 mmHg.L.mol^-1.K^-1"
                lbrR_M["text"] = "62.32 mmHg.L.mol^-1.K^-1"
                lbrR_D["text"] = "62.32 mmHg.L.mol^-1.K^-1"
            elif aux_mudar_constante[1] == "mL" or aux_mudar_constante[2] == "g.ml^-1":
                lbrR["text"] = "62320 mmHg.mL.mol^-1.K^-1"
                lbrR_Na["text"] = "62320 mmHg.mL.mol^-1.K^-1"
                lbrR_M["text"] = "62320 mmHg.mL.mol^-1.K^-1"
                lbrR_D["text"] = "62320 mmHg.mL.mol^-1.K^-1"

    elif parametro == "m^3" or parametro == "L" or parametro == "mL" or parametro == "g.ml^-1" or parametro == "g.L^-1" or parametro == "kg.m^-3" or parametro == "g.m^-3":
        if parametro == "m^3" or parametro == "g.m^-3" or parametro == "kg.m^-3":
            if parametro == "m^3":
                aux_mudar_constante[1] = "m^3"
            elif parametro == "g.m^-3":
                aux_mudar_constante[1] = "m^3"
                aux_mudar_constante[2] = "g.m^-3"
            elif parametro == "kg.m^-3":
                aux_mudar_constante[1] = "m^3"
                aux_mudar_constante[2] = "kg.m^-3"
            if aux_mudar_constante[0] == "Pa":
                lbrR["text"] = "8.31 Pa.m^3.mol^-1.K^-1"
                lbrR_Na["text"] = "8.31 Pa.m^3.mol^-1.K^-1"
                lbrR_M["text"] = "8.31 Pa.m^3.mol^-1.K^-1"
                lbrR_D["text"] = "8.31 Pa.m^3.mol^-1.K^-1"
            if aux_mudar_constante[0] == "atm":
                lbrR["text"] = "8.2x10^-5 atm.m^3.mol^-1.K^-1"
                lbrR_Na["text"] = "8.2x10^-5 atm.m^3.mol^-1.K^-1"
                lbrR_M["text"] = "8.2x10^-5 atm.m^3.mol^-1.K^-1"
                lbrR_D["text"] = "8.2x10^-5 atm.m^3.mol^-1.K^-1"
            if aux_mudar_constante[0] == "mmHg":
                lbrR["text"] = "6.2x10^-2 mmHg.m^3.mol^-1.K^-1"
                lbrR_Na["text"] = "6.2x10^-2 mmHg.m^3.mol^-1.K^-1"
                lbrR_M["text"] = "6.2x10^-2 mmHg.m^3.mol^-1.K^-1"
                lbrR_D["text"] = "6.2x10^-2 mmHg.m^3.mol^-1.K^-1"
        elif parametro == "L" or parametro == "g.L^-1":
            aux_mudar_constante[1] = "L"
            aux_mudar_constante[2] = "g.L^-1"
            if aux_mudar_constante[0] == "Pa":
                lbrR["text"] = "8.31x10^3 Pa.L.mol^-1.K^-1"
                lbrR_Na["text"] = "8.31x10^3 Pa.L.mol^-1.K^-1"
                lbrR_M["text"] = "8.31x10^3 Pa.L.mol^-1.K^-1"
                lbrR_D["text"] = "8.31x10^3 Pa.L.mol^-1.K^-1"
            if aux_mudar_constante[0] == "atm":
                lbrR["text"] = "8.2x10^-2 atm.L.mol^-1.K^-1"
                lbrR_Na["text"] = "8.2x10^-2 atm.L.mol^-1.K^-1"
                lbrR_M["text"] = "8.2x10^-2 atm.L.mol^-1.K^-1"
                lbrR_D["text"] = "8.2x10^-2 atm.L.mol^-1.K^-1"
            if aux_mudar_constante[0] == "mmHg":
                lbrR["text"] = "62.32 mmHg.L.mol^-1.K^-1"
                lbrR_Na["text"] = "62.32 mmHg.L.mol^-1.K^-1"
                lbrR_M["text"] = "62.32 mmHg.L.mol^-1.K^-1"
                lbrR_D["text"] = "62.32 mmHg.L.mol^-1.K^-1"
        elif parametro == "mL" or parametro == "g.ml^-1":
            aux_mudar_constante[1] = "mL"
            aux_mudar_constante[2] = "g.ml^-1"
            if aux_mudar_constante[0] == "Pa":
                lbrR["text"] = "8.31x10^6 Pa.mL.mol^-1.K^-1"
                lbrR_Na["text"] = "8.31x10^6 Pa.mL.mol^-1.K^-1"
                lbrR_M["text"] = "8.31x10^6 Pa.mL.mol^-1.K^-1"
                lbrR_D["text"] = "8.31x10^6 Pa.mL.mol^-1.K^-1"
            if aux_mudar_constante[0] == "atm":
                lbrR["text"] = "82 atm.mL.mol^-1.K^-1"
                lbrR_Na["text"] = "82 atm.mL.mol^-1.K^-1"
                lbrR_M["text"] = "82 atm.mL.mol^-1.K^-1"
                lbrR_D["text"] = "82 atm.mL.mol^-1.K^-1"
            if aux_mudar_constante[0] == "mmHg":
                lbrR["text"] = "62320 mmHg.mL.mol^-1.K^-1"
                lbrR_Na["text"] = "62320 mmHg.mL.mol^-1.K^-1"
                lbrR_M["text"] = "62320 mmHg.mL.mol^-1.K^-1"
                lbrR_D["text"] = "62320 mmHg.mL.mol^-1.K^-1"

def mudarConstantek(parametro):
    if parametro == "Pa" or parametro == "atm" or parametro == "mmHg":
        if parametro == "Pa":
            aux_mudar_constante[0] = "Pa"
            if aux_mudar_constante[1] == "m^3":
                lbrk["text"] = "1.38x10^-23 Pa.m^3.K^-1.particle^-1"
            elif aux_mudar_constante[1] == "L":
                lbrk["text"] = "1.38x10^-20 Pa.L.K^-1.particle^-1"
            elif aux_mudar_constante[1] == "mL":
                lbrk["text"] = "1.38x10^-17 Pa.mL.K^-1.particle^-1"

        elif parametro == "atm":
            aux_mudar_constante[0] = "atm"
            if aux_mudar_constante[1] == "m^3":
                lbrk["text"] = "1.36x10^-28 atm.m^3.K^-1.particle^-1"
            elif aux_mudar_constante[1] == "L":
                lbrk["text"] = "1.36x10^-25 atm.L.K^-1.particle^-1"
            elif aux_mudar_constante[1] == "mL":
                lbrk["text"] = "1.36x10^-22 atm.mL.K^-1.particle^-1"
        
        elif parametro == "mmHg":
            aux_mudar_constante[0] = "mmHg"
            if aux_mudar_constante[1] == "m^3":
                lbrk["text"] = "1.03x10^-25 mmHg.m^3.K^-1.particle^-1"
            elif aux_mudar_constante[1] == "L":
                lbrk["text"] = "1.03x10^-22 mmHg.L.K^-1.particle^-1"
            elif aux_mudar_constante[1] == "mL":
                lbrk["text"] = "1.03x10^-19 mmHg.mL.K^-1.particle^-1"

    elif parametro == "m^3" or parametro == "L" or parametro == "mL":
        if parametro == "m^3":
            aux_mudar_constante[1] = "m^3"
            if aux_mudar_constante[0] == "Pa":
                lbrk["text"] = "1.38x10^-23 Pa.m^3.K^-1.particle^-1"
            if aux_mudar_constante[0] == "atm":
                lbrk["text"] = "1.36x10^-28 atm.m^3.K^-1.particle^-1"
            if aux_mudar_constante[0] == "mmHg":
                lbrk["text"] = "1.03x10^-25 mmHg.m^3.K^-1.particle^-1"    
        elif parametro == "L":
            aux_mudar_constante[1] = "L"
            if aux_mudar_constante[0] == "Pa":
                lbrk["text"] = "1.38x10^-20 Pa.L.K^-1.particle^-1"
            if aux_mudar_constante[0] == "atm":
                lbrk["text"] = "1.36x10^-25 atm.L.K^-1.particle^-1"
            if aux_mudar_constante[0] == "mmHg":
                lbrk["text"] = "1.03x10^-22 mmHg.L.K^-1.particle^-1"   
        elif parametro == "mL":
            aux_mudar_constante[1] = "mL"
            if aux_mudar_constante[0] == "Pa":
                lbrk["text"] = "1.38x10^-17 Pa.mL.K^-1.particle^-1"
            if aux_mudar_constante[0] == "atm":
                lbrk["text"] = "1.36x10^-22 atm.mL.K^-1.particle^-1"
            if aux_mudar_constante[0] == "mmHg":
                lbrk["text"] = "1.03x10^-19 mmHg.mL.K^-1.particle^-1"

janela = Tk()

#define the objects of the gas density frame
frDensGas = Frame(janela)
lbVazio = Label(frDensGas)
lbVazio1 = Label(frDensGas)
lbVazio2 = Label(frDensGas)

lbDensD = Label(frDensGas, text = "d")
tfDensD = Entry(frDensGas)
lbDensP = Label(frDensGas, text = "P")
tfDensP = Entry(frDensGas)
lbDensM = Label(frDensGas, text = "M")
tfDensM = Entry(frDensGas)
lbDensR = Label(frDensGas, text = "R")
lbDensT = Label(frDensGas, text = "T")
tfDensT = Entry(frDensGas)

tkD = StringVar(frDensGas)
escolhasD = {"g.ml^-1", "g.L^-1", "g.m^-3", "kg.m^-3"}
tkD.set("g.m^-3")

tkP = StringVar(frDensGas)
escolhasP = {"Pa", "atm", "mmHg"}
tkP.set("Pa")

tkM = StringVar(frDensGas)
escolhasM = {"g.mol^-1"}
tkM.set("g.mol^-1")

tkT = StringVar(frDensGas)
escolhasT = {"K"}
tkT.set("K")

lbUnidades = Label(frDensGas, text = "Select input units")

lbD = Label(frDensGas, text = "Density")
mnD = OptionMenu(frDensGas, tkD, *escolhasD, command = mudarConstante)
mnD.config(width = 18) 

lbP = Label(frDensGas, text = "Pressure")
mnP = OptionMenu(frDensGas, tkP, *escolhasP, command = mudarConstante)
mnP.config(width = 18)

lbMU_M = Label(frDensGas, text = "Molar mass")
mnM_M = OptionMenu(frDensGas, tkM, *escolhasM)
mnM_M.config(width = 18)

lbrR_D = Label(frDensGas, text = "8.31 J.K^-1.mol^-1")

lbT = Label(frDensGas, text = "Temperature")
mnT = OptionMenu(frDensGas, tkT, *escolhasT)
mnT.config(width = 18)

btCalcularDensidade = Button(frDensGas, text = "Calculate", width = 18)
btCalcularDensidade["command"] = partial(DensidadeGasCalculo, tfDensD, tfDensP, tfDensM, lbrR_D, tfDensT, tkP, tkT, tkD)

#define the object's positions in the density gas frame
lbVazio.grid(row = 0, column = 0)

lbDensD.grid(row = 1, column = 0)
tfDensD.grid(row = 1, column = 1)

lbDensP.grid(row = 2, column = 0)
tfDensP.grid(row = 2, column = 1)

lbDensM.grid(row = 3, column = 0)
tfDensM.grid(row = 3, column = 1)

lbDensT.grid(row = 4, column = 0)
tfDensT.grid(row = 4, column = 1)

lbVazio1.grid(row = 5, column = 0)

btCalcularDensidade.grid(row = 6, column = 1)

lbUnidades.grid(row = 7, column = 0)
lbD.grid(row = 8, column = 0)
mnD.grid(row = 8, column = 1)
lbP.grid(row = 9, column = 0)
mnP.grid(row = 9, column = 1)
lbMU_M.grid(row = 10, column = 0)
mnM_M.grid(row = 10, column = 1)
lbDensR.grid(row = 11, column = 0)
lbrR_D.grid(row = 11, column = 1)
lbT.grid(row = 12, column = 0)
mnT.grid(row = 12, column = 1)

#define the objetcs of the isochoric transformation frame
frTransfIsov = Frame(janela)
lbVazio = Label(frTransfIsov)
lbVazio1 = Label(frTransfIsov)
lbVazio2 = Label(frTransfIsov)

lbIsovP1 = Label(frTransfIsov, text = "P1")
tfIsovP1 = Entry(frTransfIsov)
lbIsovT1 = Label(frTransfIsov, text = "T1")
tfIsovT1 = Entry(frTransfIsov)
lbIsovP2 = Label(frTransfIsov, text = "P2")
tfIsovP2 = Entry(frTransfIsov)
lbIsovT2 = Label(frTransfIsov, text = "T2")
tfIsovT2 = Entry(frTransfIsov)
 
tkP = StringVar(frTransfIsov)
escolhasP = {"Pa", "atm", "mmHg"}
tkP.set("Pa")

tkT = StringVar(frTransfIsov)
escolhasT = {"K"}
tkT.set("K")

lbUnidades = Label(frTransfIsov, text = "Select input units")
lbP = Label(frTransfIsov, text = "Pressure")
mnP = OptionMenu(frTransfIsov, tkP, *escolhasP)
mnP.config(width = 18)
lbT = Label(frTransfIsov, text = "Temperature")
mnT = OptionMenu(frTransfIsov, tkT, *escolhasT)
mnT.config(width = 18)

btCalcularIsovolumetrica = Button(frTransfIsov, text = "Calculate", width = 18)
btCalcularIsovolumetrica["command"] = partial(TranformacaoIsovolumetricaCalculo, tfIsovP1, tfIsovT1, tfIsovP2, tfIsovT2, tkP, tkT)

#define the positions of the objects in the isochoric transformation frame
lbVazio.grid(row = 0, column = 0)

lbIsovP1.grid(row = 1, column = 0)
tfIsovP1.grid(row = 1, column = 1)

lbIsovT1.grid(row = 2, column = 0)
tfIsovT1.grid(row = 2, column = 1)

lbVazio1.grid(row = 3, column = 0)

lbIsovP2.grid(row = 4, column = 0)
tfIsovP2.grid(row = 4, column = 1)

lbIsovT2.grid(row = 5, column = 0)
tfIsovT2.grid(row = 5, column = 1)

lbVazio2.grid(row = 6, column = 0)

btCalcularIsovolumetrica.grid(row = 7, column = 1)

lbUnidades.grid(row = 8, column = 0)
lbP.grid(row = 9, column = 0)
mnP.grid(row = 9, column = 1)
lbT.grid(row = 10, column = 0)
mnT.grid(row = 10, column = 1)


#define the objetcs of the isobaric transformation frame
frTransfIsob = Frame(janela)
lbVazio = Label(frTransfIsob)
lbVazio1 = Label(frTransfIsob)
lbVazio2 = Label(frTransfIsob)

lbIsobV1 = Label(frTransfIsob, text = "V1")
tfIsobV1 = Entry(frTransfIsob)
lbIsobT1 = Label(frTransfIsob, text = "T1")
tfIsobT1 = Entry(frTransfIsob)
lbIsobV2 = Label(frTransfIsob, text = "V2")
tfIsobV2 = Entry(frTransfIsob)
lbIsobT2 = Label(frTransfIsob, text = "T2")
tfIsobT2 = Entry(frTransfIsob)
 
tkV = StringVar(frTransfIsob)
escolhasV = {"m^3", "L", "mL"}
tkV.set("m^3")

tkT = StringVar(frTransfIsob)
escolhasT = {"K"}
tkT.set("K")

lbUnidades = Label(frTransfIsob, text = "Select input units")
lbV = Label(frTransfIsob, text = "Volume")
mnV = OptionMenu(frTransfIsob, tkV, *escolhasV)
mnV.config(width = 18)
lbT = Label(frTransfIsob, text = "Temperature")
mnT = OptionMenu(frTransfIsob, tkT, *escolhasT)
mnT.config(width = 18)

btCalcularIsobarica = Button(frTransfIsob, text = "Calculate", width = 18)
btCalcularIsobarica["command"] = partial(TranformacaoIsobaricaCalculo, tfIsobV1, tfIsobT1, tfIsobV2, tfIsobT2, tkV, tkT)

#define the positions of the objects in the isobaric transformation frame
lbVazio.grid(row = 0, column = 0)

lbIsobV1.grid(row = 1, column = 0)
tfIsobV1.grid(row = 1, column = 1)

lbIsobT1.grid(row = 2, column = 0)
tfIsobT1.grid(row = 2, column = 1)

lbVazio1.grid(row = 3, column = 0)

lbIsobV2.grid(row = 4, column = 0)
tfIsobV2.grid(row = 4, column = 1)

lbIsobT2.grid(row = 5, column = 0)
tfIsobT2.grid(row = 5, column = 1)

lbVazio2.grid(row = 6, column = 0)

btCalcularIsobarica.grid(row = 7, column = 1)

lbUnidades.grid(row = 8, column = 0)
lbV.grid(row = 9, column = 0)
mnV.grid(row = 9, column = 1)
lbT.grid(row = 10, column = 0)
mnT.grid(row = 10, column = 1)

#define the objetcs of the isotermic transformation frame
frTransfIsot = Frame(janela)
lbVazio = Label(frTransfIsot)
lbVazio1 = Label(frTransfIsot)
lbVazio2 = Label(frTransfIsot)

lbIsotP1 = Label(frTransfIsot, text = "P1")
tfIsotP1 = Entry(frTransfIsot)
lbIsotV1 = Label(frTransfIsot, text = "V1")
tfIsotV1 = Entry(frTransfIsot)
lbIsotP2 = Label(frTransfIsot, text = "P2")
tfIsotP2 = Entry(frTransfIsot)
lbIsotV2 = Label(frTransfIsot, text = "V2")
tfIsotV2 = Entry(frTransfIsot)

tkP = StringVar(frTransfIsot)
escolhasP = {"Pa", "atm", "mmHg"}
tkP.set("Pa")
    
tkV = StringVar(frTransfIsot)
escolhasV = {"m^3", "L", "mL"}
tkV.set("m^3")

lbUnidades = Label(frTransfIsot, text = "Select input units")
lbP = Label(frTransfIsot, text = "Pressure")
mnP = OptionMenu(frTransfIsot, tkP, *escolhasP)
mnP.config(width = 18)
lbV = Label(frTransfIsot, text = "Volume")
mnV = OptionMenu(frTransfIsot, tkV, *escolhasV)
mnV.config(width = 18)

btCalcularIsotermica = Button(frTransfIsot, text = "Calculate", width = 18)
btCalcularIsotermica["command"] = partial(TranformacaoIsotermicaCalculo, tfIsotP1, tfIsotV1, tfIsotP2, tfIsotV2, tkP, tkV)

#define the positions of the objects in the isotermic transformation frame
lbVazio.grid(row = 0, column = 0)

lbIsotP1.grid(row = 1, column = 0)
tfIsotP1.grid(row = 1, column = 1)

lbIsotV1.grid(row = 2, column = 0)
tfIsotV1.grid(row = 2, column = 1)

lbVazio1.grid(row = 3, column = 0)

lbIsotP2.grid(row = 4, column = 0)
tfIsotP2.grid(row = 4, column = 1)

lbIsotV2.grid(row = 5, column = 0)
tfIsotV2.grid(row = 5, column = 1)

lbVazio2.grid(row = 6, column = 0)

btCalcularIsotermica.grid(row = 7, column = 1)

lbUnidades.grid(row = 8, column = 0)
lbP.grid(row = 9, column = 0)
mnP.grid(row = 9, column = 1)
lbV.grid(row = 10, column = 0)
mnV.grid(row = 10, column = 1)

#define the object of the clapeyron equation (state equation) frame - Na VERSION
frEqClapeyron_Na = Frame(janela)
lbVazio = Label(frEqClapeyron_Na)
lbVazio1 = Label(frEqClapeyron_Na)
lbVazio2 = Label(frEqClapeyron_Na) 

lbP_Na = Label(frEqClapeyron_Na, text = "P")
tfP_Na = Entry(frEqClapeyron_Na)
lbV_Na = Label(frEqClapeyron_Na, text = "V")
tfV_Na = Entry(frEqClapeyron_Na)
lbN_Na = Label(frEqClapeyron_Na, text = "N")
tfN_Na = Entry(frEqClapeyron_Na)
lbNa_Na = Label(frEqClapeyron_Na, text = "Avogadro's number")
lbR_Na = Label(frEqClapeyron_Na, text = "R")
lbT_Na = Label(frEqClapeyron_Na, text = "T")
tfT_Na = Entry(frEqClapeyron_Na)

tkP_Na = StringVar(frEqClapeyron_Na)
escolhasP_Na = {"Pa", "atm", "mmHg"}
tkP_Na.set("Pa")
    
tkV_Na = StringVar(frEqClapeyron_Na)
escolhasV_Na = {"m^3", "L", "mL"}
tkV_Na.set("m^3")

tkN_Na = StringVar(frEqClapeyron_Na)
escolhasNa = {"Particle(s)"}
tkN_Na.set("Particle(s)")

tkT_Na = StringVar(frEqClapeyron_Na)
escolhasT_Na = {"K"}
tkT_Na.set("K")

lbUnidades_Na = Label(frEqClapeyron_Na, text = "Select input units")

lbPU_Na = Label(frEqClapeyron_Na, text = "Pressure")
mnP_Na = OptionMenu(frEqClapeyron_Na, tkP_Na, *escolhasP_Na, command = mudarConstante)
mnP_Na.config(width = 18)

lbVU_Na = Label(frEqClapeyron_Na, text = "Volume")
mnV_Na = OptionMenu(frEqClapeyron_Na, tkV_Na, *escolhasV_Na, command = mudarConstante)
mnV_Na.config(width = 18)

lbNU_Na = Label(frEqClapeyron_Na, text = "Particles")
mnN_Na = OptionMenu(frEqClapeyron_Na, tkN_Na, *escolhasNa)
mnN_Na.config(width = 18)

lbrNa_Na = Label(frEqClapeyron_Na, text = "6.02x10^23 partícula.mol^-1")

lbrR_Na = Label(frEqClapeyron_Na, text = "8.31 J.K^-1.mol^-1")

lbTU_Na = Label(frEqClapeyron_Na, text = "Temperature")
mnT_Na = OptionMenu(frEqClapeyron_Na, tkT_Na, *escolhasT_Na)
mnT_Na.config(width = 18)

btCalcularClapeyron_Na = Button(frEqClapeyron_Na, text = "Calculate", width = 18)
btCalcularClapeyron_Na["command"] = partial(EquacaoDeClapyronCalculo_Na,tfP_Na, tfV_Na, tfN_Na, lbrR_Na, tfT_Na, tkP_Na, tkV_Na)

#define the positions of the objects in the clapeyron equation frame - Na VERSION
lbVazio.grid(row = 0, column = 0)
    
lbP_Na.grid(row = 1, column = 0)
tfP_Na.grid(row = 1, column = 1)
lbV_Na.grid(row = 2, column = 0)
tfV_Na.grid(row = 2, column = 1)
lbN_Na.grid(row = 3, column = 0)
tfN_Na.grid(row = 3, column = 1)
lbT_Na.grid(row = 5, column = 0)
tfT_Na.grid(row = 5, column = 1)

lbVazio1.grid(row = 6, column = 0)

btCalcularClapeyron_Na.grid(row = 7, column = 1)

lbUnidades_Na.grid(row = 8, column = 0)
lbPU_Na.grid(row = 9, column = 0)
mnP_Na.grid(row = 9, column = 1)
lbVU_Na.grid(row = 10, column = 0)
mnV_Na.grid(row = 10, column = 1)
lbNU_Na.grid(row = 11, column = 0)
mnN_Na.grid(row = 11, column = 1)
lbNa_Na.grid(row = 12, column = 0)
lbrNa_Na.grid(row = 12, column = 1)
lbR_Na.grid(row = 13, column = 0)
lbrR_Na.grid(row = 13, column = 1)
lbTU_Na.grid(row = 14, column = 0)
mnT_Na.grid(row = 14, column = 1)

#define the objects of the clapeyron equation (state equation) frame - N VERSION
frEqClapeyron_N = Frame(janela)
lbVazio = Label(frEqClapeyron_N)
lbVazio1 = Label(frEqClapeyron_N)
lbVazio2 = Label(frEqClapeyron_N) 

lbP_N = Label(frEqClapeyron_N, text = "P")
tfP_N = Entry(frEqClapeyron_N)
lbV_N = Label(frEqClapeyron_N, text = "V")
tfV_N = Entry(frEqClapeyron_N)
lbN_N = Label(frEqClapeyron_N, text = "N")
tfN_N = Entry(frEqClapeyron_N)
lbT_N = Label(frEqClapeyron_N, text = "T")
tfT_N = Entry(frEqClapeyron_N)

tkP_N = StringVar(frEqClapeyron_N)
escolhasP_N = {"Pa", "atm", "mmHg"}
tkP_N.set("Pa")
    
tkV_N = StringVar(frEqClapeyron_N)
escolhasV_N = {"m^3", "L", "mL"}
tkV_N.set("m^3")

tkN_N = StringVar(frEqClapeyron_N)
escolhasN = {"Particle(s)"}
tkN_N.set("Particle(s)")

tkT_N = StringVar(frEqClapeyron_N)
escolhasT_N = {"K"}
tkT_N.set("K")

lbUnidades_N = Label(frEqClapeyron_N, text = "Select input units")

lbPU_N = Label(frEqClapeyron_N, text = "Pressure")
mnP_N = OptionMenu(frEqClapeyron_N, tkP_N, *escolhasP_N, command = mudarConstantek)
mnP_N.config(width = 18)

lbVU_N = Label(frEqClapeyron_N, text = "Volume")
mnV_N = OptionMenu(frEqClapeyron_N, tkV_N, *escolhasV_N, command = mudarConstantek)
mnV_N.config(width = 18)

lbNU_N = Label(frEqClapeyron_N, text = "Particles")
mnN_N = OptionMenu(frEqClapeyron_N, tkN_N, *escolhasN)
mnN_N.config(width = 18)

lbkU = Label(frEqClapeyron_N, text = "k")
lbrk = Label(frEqClapeyron_N, text = "1.38x10^-23 Pa.m^3.K^-1.particle^-1")

lbTU_N = Label(frEqClapeyron_N, text = "Temperature")
mnT_N = OptionMenu(frEqClapeyron_N, tkT_N, *escolhasT_N)
mnT_N.config(width = 18)

btCalcularClapeyron_N = Button(frEqClapeyron_N, text = "Calculate", width = 18)
btCalcularClapeyron_N["command"] = partial(EquacaoDeClapyronCalculo_N,tfP_N, tfV_N, tfN_N, lbrk, tfT_N, tkP_N, tkV_N)

#define the positions of the objects in the clapeyron equation frame - N VERSION
lbVazio.grid(row = 0, column = 0)
    
lbP_N.grid(row = 1, column = 0)
tfP_N.grid(row = 1, column = 1)
lbV_N.grid(row = 2, column = 0)
tfV_N.grid(row = 2, column = 1)
lbN_N.grid(row = 3, column = 0)
tfN_N.grid(row = 3, column = 1)
lbT_N.grid(row = 5, column = 0)
tfT_N.grid(row = 5, column = 1)

lbVazio1.grid(row = 6, column = 0)

btCalcularClapeyron_N.grid(row = 7, column = 1)

lbUnidades_N.grid(row = 8, column = 0)
lbPU_N.grid(row = 9, column = 0)
mnP_N.grid(row = 9, column = 1)
lbVU_N.grid(row = 10, column = 0)
mnV_N.grid(row = 10, column = 1)
lbNU_N.grid(row = 11, column = 0)
mnN_N.grid(row = 11, column = 1)
lbkU.grid(row = 13, column = 0)
lbrk.grid(row = 13, column = 1)
lbTU_N.grid(row = 14, column = 0)
mnT_N.grid(row = 14, column = 1)


#define the objects of the clapeyron equation (state equation) frame - m/M VERSION
frEqClapeyron_M = Frame(janela)
frEqClapeyron_M = Frame(janela)
lbVazio = Label(frEqClapeyron_M)
lbVazio1 = Label(frEqClapeyron_M)
lbVazio2 = Label(frEqClapeyron_M) 

lbP_M = Label(frEqClapeyron_M, text = "P")
tfP_M = Entry(frEqClapeyron_M)
lbV_M = Label(frEqClapeyron_M, text = "V")
tfV_M = Entry(frEqClapeyron_M)
lbm_M = Label(frEqClapeyron_M, text = "m")
tfm_M = Entry(frEqClapeyron_M)
lbM_M = Label(frEqClapeyron_M, text = "M")
tfM_M = Entry(frEqClapeyron_M)
lbR_M = Label(frEqClapeyron_M, text = "R")
lbT_M = Label(frEqClapeyron_M, text = "T")
tfT_M = Entry(frEqClapeyron_M)

tkP_M = StringVar(frEqClapeyron_M)
escolhasP_M = {"Pa", "atm", "mmHg"}
tkP_M.set("Pa")
    
tkV_M = StringVar(frEqClapeyron_M)
escolhasV_M = {"m^3", "L", "mL"}
tkV_M.set("m^3")

tkm_M = StringVar(frEqClapeyron_M)
escolhasm = {"g"}
tkm_M.set("g")

tkM_M = StringVar(frEqClapeyron_M)
escolhasM = {"g.mol^-1"}
tkM_M.set("g.mol^-1")

tkT_M = StringVar(frEqClapeyron_M)
escolhasT_M = {"K"}
tkT_M.set("K")

lbUnidades_M = Label(frEqClapeyron_M, text = "Select input units")
lbPU_M = Label(frEqClapeyron_M, text = "Pressure")
mnP_M = OptionMenu(frEqClapeyron_M, tkP_M, *escolhasP_M, command = mudarConstante)
mnP_M.config(width = 18)
lbVU_M = Label(frEqClapeyron_M, text = "Volume")
mnV_M = OptionMenu(frEqClapeyron_M, tkV_M, *escolhasV_M, command = mudarConstante)
mnV_M.config(width = 18)
lbmU_M = Label(frEqClapeyron_M, text = "Mass")
mnm_M = OptionMenu(frEqClapeyron_M, tkm_M, *escolhasm)
mnm_M.config(width = 18)
lbMU_M = Label(frEqClapeyron_M, text = "Molar mass")
mnM_M = OptionMenu(frEqClapeyron_M, tkM_M, *escolhasM)
mnM_M.config(width = 18)
lbrR_M = Label(frEqClapeyron_M, text = "8.31 J.K^-1.mol^-1")
lbTU_M = Label(frEqClapeyron_M, text = "Temperature")
mnT_M = OptionMenu(frEqClapeyron_M, tkT_M, *escolhasT_M)
mnT_M.config(width = 18)

btCalcularClapeyron_M = Button(frEqClapeyron_M, text = "Calculate", width = 18)
btCalcularClapeyron_M["command"] = partial(EquacaoDeClapyronCalculo_M,tfP_M, tfV_M, tfm_M, tfM_M, lbrR_M, tfT_M, tkP_M, tkV_M)

#define the positions of the objects in the clapeyron equation frame - m/M VERSION
lbVazio.grid(row = 0, column = 0)
    
lbP_M.grid(row = 1, column = 0)
tfP_M.grid(row = 1, column = 1)
lbV_M.grid(row = 2, column = 0)
tfV_M.grid(row = 2, column = 1)
lbm_M.grid(row = 3, column = 0)
tfm_M.grid(row = 3, column = 1)
lbM_M.grid(row = 4, column = 0)
tfM_M.grid(row = 4, column = 1)
lbT_M.grid(row = 5, column = 0)
tfT_M.grid(row = 5, column = 1)

lbVazio1.grid(row = 6, column = 0)

btCalcularClapeyron_M.grid(row = 7, column = 1)

lbUnidades_M.grid(row = 8, column = 0)
lbPU_M.grid(row = 9, column = 0)
mnP_M.grid(row = 9, column = 1)
lbVU_M.grid(row = 10, column = 0)
mnV_M.grid(row = 10, column = 1)
lbmU_M.grid(row = 11, column = 0)
mnm_M.grid(row = 11, column = 1)
lbMU_M.grid(row = 12, column = 0)
mnM_M.grid(row = 12, column = 1)
lbR_M.grid(row = 13, column = 0)
lbrR_M.grid(row = 13, column = 1)
lbTU_M.grid(row = 14, column = 0)
mnT_M.grid(row = 14, column = 1)

#define the objects of the clapeyron equation (state equation) frame - n VERSION
frEqClapeyron_n = Frame(janela)
lbVazio = Label(frEqClapeyron_n)
lbVazio1 = Label(frEqClapeyron_n)
lbVazio2 = Label(frEqClapeyron_n)

lbP_n = Label(frEqClapeyron_n, text = "P")
tfP_n = Entry(frEqClapeyron_n)
lbV_n = Label(frEqClapeyron_n, text = "V")
tfV_n = Entry(frEqClapeyron_n)
lbn_n = Label(frEqClapeyron_n, text = "n")
tfn_n = Entry(frEqClapeyron_n)
lbR_n = Label(frEqClapeyron_n, text = "R")
tfR_n = Entry(frEqClapeyron_n)
lbT_n = Label(frEqClapeyron_n, text = "T")
tfT_n = Entry(frEqClapeyron_n)

tkP_n = StringVar(frEqClapeyron_n)
escolhasP_n = {"Pa", "atm", "mmHg"}
tkP_n.set("Pa")
    
tkV_n = StringVar(frEqClapeyron_n)
escolhasV_n = {"m^3", "L", "mL"}
tkV_n.set("m^3")

tkn_n = StringVar(frEqClapeyron_n)
escolhasn = {"mol"}
tkn_n.set("mol")
    
tkT_n = StringVar(frEqClapeyron_n)
escolhasT_n = {"K"}
tkT_n.set("K")

lbUnidades_n = Label(frEqClapeyron_n, text = "Select input units")
lbPU_n = Label(frEqClapeyron_n, text = "Pressure")
mnP_n = OptionMenu(frEqClapeyron_n, tkP_n, *escolhasP_n, command = mudarConstante)
mnP_n.config(width = 18)
lbVU_n = Label(frEqClapeyron_n, text = "Volume")
mnV_n = OptionMenu(frEqClapeyron_n, tkV_n, *escolhasV_n, command = mudarConstante)
mnV_n.config(width = 18)
lbnU_n = Label(frEqClapeyron_n, text = "Mols")
mnn_n = OptionMenu(frEqClapeyron_n, tkn_n, *escolhasn)
mnn_n.config(width = 18)
lbRU = Label(frEqClapeyron_n, text = "R")
lbrR = Label(frEqClapeyron_n, text = "8.31 J.K^-1.mol^-1")
lbTU_n = Label(frEqClapeyron_n, text = "Temperature")
mnT_n = OptionMenu(frEqClapeyron_n, tkT_n, *escolhasT_n)
mnT_n.config(width = 18)

btCalcularClapeyron_n = Button(frEqClapeyron_n, text = "Calculate", width = 18)
btCalcularClapeyron_n["command"] = partial(EquacaoDeClapyronCalculo_n,tfP_n, tfV_n, tfn_n, lbrR, tfT_n, tkP_n, tkV_n)

#define the positions of the objects in the clapeyron equation frame - n VERSION
lbVazio2.grid(row = 0, column = 0)
    
lbP_n.grid(row = 1, column = 0)
tfP_n.grid(row = 1, column = 1)
lbV_n.grid(row = 2, column = 0)
tfV_n.grid(row = 2, column = 1)
lbn_n.grid(row = 3, column = 0)
tfn_n.grid(row = 3, column = 1)
lbT_n.grid(row = 4, column = 0)
tfT_n.grid(row = 4, column = 1)

lbVazio1.grid(row = 5, column = 0)

btCalcularClapeyron_n.grid(row = 6, column = 1)

lbUnidades_n.grid(row = 10, column = 0)
lbPU_n.grid(row = 11, column = 0)
mnP_n.grid(row = 11, column = 1)
lbVU_n.grid(row = 12, column = 0)
mnV_n.grid(row = 12, column = 1)
lbnU_n.grid(row = 13, column = 0)
mnn_n.grid(row = 13, column = 1)
lbR_n.grid(row = 14, column = 0)
lbrR.grid(row = 14, column = 1)
lbTU_n.grid(row = 15, column = 0)
mnT_n.grid(row = 15, column = 1)

#define the objects of the general equation frame
frEqGeral = Frame(janela)

lbVazio = Label(frEqGeral)
lbVazio1 = Label(frEqGeral)
lbVazio2 = Label(frEqGeral)  
    
lbP1 = Label(frEqGeral, text = "P1")
tfP1 = Entry(frEqGeral)
lbV1 = Label(frEqGeral, text = "V1")
tfV1 = Entry(frEqGeral)
lbT1 = Label(frEqGeral, text = "T1")
tfT1 = Entry(frEqGeral)

lbP2 = Label(frEqGeral, text = "P2")
tfP2 = Entry(frEqGeral)
lbV2 = Label(frEqGeral, text = "V2")
tfV2 = Entry(frEqGeral)
lbT2 = Label(frEqGeral, text = "T2")
tfT2 = Entry(frEqGeral)

tkP = StringVar(frEqGeral)
escolhasP = {"Pa", "atm", "mmHg"}
tkP.set("Pa")
    
tkV = StringVar(frEqGeral)
escolhasV = {"m^3", "L", "mL"}
tkV.set("m^3")
    
tkT = StringVar(frEqGeral)
escolhasT = {"K"}
tkT.set("K")

lbUnidades = Label(frEqGeral, text = "Select input units")
lbP = Label(frEqGeral, text = "Pressure")
mnP = OptionMenu(frEqGeral, tkP, *escolhasP)
mnP.config(width = 18)
lbV = Label(frEqGeral, text = "Volume")
mnV = OptionMenu(frEqGeral, tkV, *escolhasV)
mnV.config(width = 18)
lbT = Label(frEqGeral, text = "Temperature")
mnT = OptionMenu(frEqGeral, tkT, *escolhasT)
mnT.config(width = 18)

btCalcular = Button(frEqGeral, text = "Calculate", width = 18)
btCalcular["command"] = partial(EquacaoGeralDosGasesCalculo, tfP1, tfV1, tfT1, tfP2, tfV2, tfT2, tkP, tkV, tkT)

#define the positions of the objects in the general equation frame

lbVazio.grid(row = 0, column = 0)
    
lbP1.grid(row = 1, column = 0)
tfP1.grid(row = 1, column = 1)
lbV1.grid(row = 2, column = 0)
tfV1.grid(row = 2, column = 1)
lbT1.grid(row = 3, column = 0)
tfT1.grid(row = 3, column = 1)

lbVazio1.grid(row = 4, column = 0)

lbP2.grid(row = 5, column = 0)
tfP2.grid(row = 5, column = 1)
lbV2.grid(row = 6, column = 0)
tfV2.grid(row = 6, column = 1)
lbT2.grid(row = 7, column = 0)
tfT2.grid(row = 7, column = 1)

lbVazio2.grid(row = 8, column = 0)
btCalcular.grid(row = 9, column = 1)

lbUnidades.grid(row = 10, column = 0)
lbP.grid(row = 11, column = 0)
mnP.grid(row = 11, column = 1)
lbV.grid(row = 12, column = 0)
mnV.grid(row = 12, column = 1)
lbT.grid(row = 13, column = 0)
mnT.grid(row = 13, column = 1)

#Toolbar and Label on the bot of the frame with the results and warnings
frToolBarBottom = Frame(janela, bg = "green")
lbAviso = Label(frToolBarBottom, text = "Invalid input", bg = "red")
lbAviso.grid(row = 0, column = 0)

#Toolbar with the equations and transformations
frToolBar = Frame(janela, bg = "gray")

#array to change save the previous screens
global vetor
vetor = [""]

tkClapeyron = StringVar(frToolBar)
escolhasClapeyron = {"PV = nRT", "PV = (m/M)RT","PV = NkT", "PV = (N/Na)RT"}
tkClapeyron.set("PV = nRT")

mnClapeyron = OptionMenu(frToolBar, tkClapeyron, *escolhasClapeyron, command = EquacaoDeClapeyron) #OLHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
mnClapeyron["width"] = 25

btEqGeral = Button(frToolBar, text = "Ideal gas law", width = 25, command = EquacaoGeralDosGases)
btBoyle = Button(frToolBar, text = "Isothermic transformation", width = 25, command = TransformacaoIsotermica)
btCharles = Button(frToolBar, text = "Isobaric transformation", width = 25, command = TransformacaoIsobarica)
btCharlesGayLussac = Button(frToolBar, text = "Isovolumetric transformation", width = 25, command = TransformacaoIsovolumetrica)
btDensidade = Button(frToolBar, text = "Gas density d = PM/RT", width = 25, command = DensidadeGas)

#put the buttons on the toolbar
btEqGeral.grid(row = 0, column = 0, padx = 5)
mnClapeyron.grid(row = 0, column = 1, padx = 5)
btBoyle.grid(row = 0, column = 2, padx = 5)
btCharles.grid(row = 0, column = 3, padx = 5)
btCharlesGayLussac.grid(row = 0, column = 4, padx = 5)
btDensidade.grid(row = 0, column = 5, padx = 5)

#put the toolbar on the mainframe
frToolBar.grid(row = 0, column = 0, sticky = W+E)

janela.mainloop()
