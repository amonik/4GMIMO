import numpy as np 
import random as rd
import math as math

from spatial import spatial

def binarymap(obj, xin_0):


	#print xin_0

	symlength = obj.NFFT + obj.CP

	d1 = np.zeros(obj.L*symlength)
	d2 = np.zeros(obj.L*symlength)
	d3 = np.zeros(obj.L*symlength)
	d4 = np.zeros(obj.L*symlength)
	


	No_Bits=len(obj.bins_used)*4

	for symbs in range(1,obj.L+1):
		spatial.xin = xin_0[(symbs - 1)*No_Bits:symbs*No_Bits]
		d_bpsk = 2*np.array(spatial.xin) -1
		print d_bpsk.shape

		Hk_00 = np.fft.fft(obj.h00_n, obj.NFFT) #64 point FFT of all 16 time domain channels
    	Hk_01 = np.fft.fft(obj.h01_n, obj.NFFT)
    	Hk_02 = np.fft.fft(obj.h02_n, obj.NFFT)
    	Hk_03 = np.fft.fft(obj.h03_n, obj.NFFT)
    	Hk_10 = np.fft.fft(obj.h10_n, obj.NFFT)
    	Hk_11 = np.fft.fft(obj.h11_n, obj.NFFT)
    	Hk_12 = np.fft.fft(obj.h12_n, obj.NFFT)
    	Hk_13 = np.fft.fft(obj.h13_n, obj.NFFT)
    	Hk_20 = np.fft.fft(obj.h20_n, obj.NFFT)
    	Hk_21 = np.fft.fft(obj.h21_n, obj.NFFT)
    	Hk_22 = np.fft.fft(obj.h22_n, obj.NFFT)
    	Hk_23 = np.fft.fft(obj.h23_n, obj.NFFT)
    	Hk_30 = np.fft.fft(obj.h30_n, obj.NFFT)
    	Hk_31 = np.fft.fft(obj.h31_n, obj.NFFT)
    	Hk_32 = np.fft.fft(obj.h32_n, obj.NFFT)
    	Hk_33 = np.fft.fft(obj.h33_n, obj.NFFT)

    	spatial.H_k = np.zeros((4,4,62), dtype = complex) #Need to make this complex. Creates three denominational array.

    	spatial.H_k[0,0,:] = Hk_00[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[0,1,:] = Hk_01[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[0,2,:] = Hk_02[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[0,3,:] = Hk_03[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[1,0,:] = Hk_10[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[1,1,:] = Hk_11[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[1,2,:] = Hk_12[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[1,3,:] = Hk_13[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[2,0,:] = Hk_20[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[2,1,:] = Hk_21[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[2,2,:] = Hk_22[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[2,3,:] = Hk_23[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[3,0,:] = Hk_30[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[3,1,:] = Hk_31[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[3,2,:] = Hk_32[np.array([spatial.BinsUsedMatlab])]
    	spatial.H_k[3,3,:] = Hk_33[np.array([spatial.BinsUsedMatlab])]

    	A_1 = d_bpsk[0::4] #breaks up the data into 240 chunks 
    	A_2 = d_bpsk[1::4]
    	A_3 = d_bpsk[2::4]
    	A_4 = d_bpsk[3::4]


    	A11 = np.zeros(len(A_1))
    	A22 = np.zeros(len(A_2))
    	A33 = np.zeros(len(A_3))
    	A44 = np.zeros(len(A_4))
    	
    	#for i in range(1,spatial.H_k.shape[2]+1):
    		#[spatial.U[:,:,i], spatial.S[:,:,i], spatial.V[:,:,i]] #add single value decomposition 
		

	return obj
	return xin_0
'''
complete class spatial objects, and be sure to pass values back to variables from functions with spatial.varible_name
'''
'''

	return d1
	return d2
	return d3
	return d4

'''