import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation as FA
from scipy.integrate import solve_ivp

C1=0.35
C2=0.7
g=9.81#m/s62
ro_0=1.225#kg/m^3
c=340#m/s
m_f=108#kg
m_d=37#kg
r=0.1#m
v_w=0.2#m/s
A=np.pi*r**2#m^2
H=10400#m
Isp1=250#s
mu=-5.4#kg/s

print('type in initial velocity:')
v_0=float(input())#m/s
print('type in initial launch angle:')
alfa=float(input())
al=np.radians(alfa)
t=np.linspace(0,92,10000)#s
def dSdt(t,S):
    x,y,v_x,v_y,m=S
    ro=ro_0*np.exp(-y/H)
    mach=np.sqrt(v_x**2+v_y**2)/c
    dmdt=mu
    C=C1
    Isp=Isp1
    if(t>(m_f/-mu)):
        dmdt=0
    
    if(mach>1):
        C=C2
    a_x=-0.5*ro*C*A*(v_x+v_w)*np.sqrt((v_x+v_w)**2+v_y**2)/m-dmdt*Isp*g*(v_x)/(m*np.sqrt((v_x)**2+v_y**2))
    a_y=-g-0.5*ro*C*A*v_y*np.sqrt((v_x+v_w)**2+v_y**2)/m-Isp*g*dmdt*v_y/(m*np.sqrt((v_x)**2+v_y**2))
    return v_x,v_y,a_x,a_y,dmdt
x_0=0
y_0=0
v_x_0=v_0*np.cos(al)
v_y_0=v_0*np.sin(al)
m_0=m_f+m_d
S_0=[x_0,y_0,v_x_0,v_y_0,m_0]
def event_y_zero(t,y):
    return y[1]
event_y_zero.terminal=True
event_y_zero.direction=-1
sol=solve_ivp(dSdt,t_span=(0,max(t)),y0=S_0,t_eval=t,dense_output=True,events=event_y_zero)
x_sol=sol.y[0]
y_sol=sol.y[1]
v_x_sol=sol.y[2]
v_y_sol=sol.y[3]
m_sol=sol.y[4]
t_sol=sol.t
fig,ax=plt.subplots()
ax.set_xlim(0,max(x_sol)+100)
ax.set_ylim(0,max(y_sol)+100)
ax.set_xlabel('horizontal fight length [m]')
ax.set_ylabel('altitude [m]')
ax.set_title('flight trajectory')
t_val=[]
x_val=[]
y_val=[]
v_sol=np.sqrt(v_x_sol**2+v_y_sol**2)
line_y,=ax.plot([],[],color='orange',label='trajectory')
fig2,ax2=plt.subplots()
ax2.set_xlim(0,t_sol[-1])
ax2.set_ylim(0,max(v_sol)+10)
ax2.set_xlabel('time [s]')
ax2.set_ylabel('velocity [m/s]')
ax2.set_title('velocity')
plt.axvline(m_f/-mu,color='red',linestyle='--')
v_val=[]
line_v,=ax2.plot([],[],color='blue',label='velocity')
def update(frame):
    t_val=t[:frame+1]
    x_val=x_sol[:frame+1]
    y_val=y_sol[:frame+1]
    v_val=v_sol[:frame+1]
    line_y.set_data(x_val,y_val)
    line_v.set_data(t_val,v_val)
    return line_y,line_v
ani=FA(fig,update,frames=len(t_sol),interval=1,blit=True,repeat=False)
ax.legend()
ax2.legend()
ax.grid()
ax2.grid()
print('max altitude:')
print(round(max(y_sol),3))
print('max flight horizontal length:')
print(round(max(x_sol),3))
print('max velocity:')
print(round(max(v_sol),3))
print('max mach number:')
max_mn=max(v_sol/c)
print(round(max_mn,3))
plt.show()
    





                                                                 
