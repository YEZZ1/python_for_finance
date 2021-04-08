#!/usr/bin/env python
# coding: utf-8

# ### 내재 변동성

# :결국 수치적 최적화 문제

# 1. 블랙 숄즈 모형으로 유럽피안 콜 옵션 가격 결정 수식으로 설명(배당금 X)

# In[7]:


from math import log,sqrt,exp
from scipy import stats #정규분포
#cdf = 누적분포함수
#pdf = 확률분포함수


# 블랙 숄즈 모형 옵션 가격 결정 식

# In[1]:


def bsm_call_value(s0,k,T,r,sig):

    d1 = (log(s0/k)+(r+sig**2/2)*T)/(sig*sqrt(T))
    d2 = (log(s0/k)+(r-sig**2/2)*T)/(sig*sqrt(T))
    
    c = s0*stats.norm.cdf(d1,0,1)-exp(-r*T)*k*stats.norm.cdf(d2,0,1)#stats.norm.cdf:정규분포 누적확률분포계산
    
    return c

def bsm_vega(s0,k,T,r,sig) :
    #vega = bsm공식을 변동성으로 1차 미분한 값
    s0 = float(s0)
    
    dl = (log(s0/k)+(r+sig**2/2)*T)/(sig*sqrt(T))
    
    v = s0*sqrt(T)*stats.norm.pdf(d1,0,1)  #cdf 미분하면 pdf
    
    return v

def bsm_call_imp_vol(s0,k,T,r,c0,sig_est,it = 100) :
    #내제변동성 계산 함수
    for i in range(it) :
        sig_est -= (bsm_call_value(s0,k,T,r,sig_est)-0)/(bsm_vega(s0,k,T,r,sig_est))
        #-= <-ex) a-=b >> a = a-b
    
    return sig_est


# In[ ]:




