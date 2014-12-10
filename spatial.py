import numpy as np 
import random as rd
import math as math


class spatial:

	
	H_k=[]
	V=[]                 
	U = []                
	S =[]
	EqTaps = []
	v=0.1
	y1=[]
	y2=[]
	y3=[]
	y4=[]
	NFREQ=2^16
	L= []
	NFFT=16
	CP=1
	#bins_used=[-6, -5, -4, -3, -2, 5]
	xin = []
	BinsUsedMatlab=[]
	f1=[]
	f2=[]
	f3=[]
	f4=[]

	SignalPowerFreq=[]
	SNRdB=[]
	EbNodB=[]
	y_eq=[]

	def __init__(self,h00_n,h01_n,h02_n,h03_n,h10_n,h11_n,h12_n,h13_n,
					h20_n,h21_n,h22_n,h23_n,h30_n,h31_n,h32_n,h33_n,
					noisevar, NFFT, CP, L, bins_used):


		self.h00_n = h00_n
		self.h01_n = h01_n
		self.h02_n = h02_n
		self.h03_n = h03_n
		self.h10_n = h10_n
		self.h11_n = h11_n
		self.h12_n = h12_n
		self.h13_n = h13_n
		self.h20_n = h20_n
		self.h21_n = h21_n
		self.h22_n = h22_n
		self.h23_n = h23_n
		self.h30_n = h30_n
		self.h31_n = h31_n
		self.h32_n = h32_n
		self.h33_n = h33_n
		self.noisevar = noisevar
		self.NFFT = NFFT
		self.CP = CP 
		self.L = L
		self.bins_used = bins_used
		
		
		
		



