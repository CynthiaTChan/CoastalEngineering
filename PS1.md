```python
from aide_design.play import*

```

```python
kh = np.array(np.linspace(0.1,9.9,99))
# print(kh)
g = pc.gravity
Y_axis1 = kh * np.tanh(kh)
Y_axis2 = np.sqrt(np.tanh(kh) / kh)
# test = np.sin(kh)
#print(test)
#print(Y_axis1)

plt.figure()
plt.plot(kh,Y_axis1, 'c-')
plt.xlabel('kh')
plt.ylabel('sigma^2*h*g^-1')
plt.grid
plt.show()

plt.figure()
plt.plot(kh,Y_axis2, 'r-')
plt.xlabel('kh')
plt.ylabel('cp/(gh)^.5')
plt.grid
plt.show()


def wavelength(T,h):
  'Returns the wavelength of a wave given the period and the water height from the bed'
  lam = ((g * T**2)/(2 * np.pi)) * np.sqrt(np.tanh(4 * np.pi**2 * h/ (T**2 * g)))
  return(lam.to(u.m))

def celarity(wavelength, T):
  'Returns the wavespeed given a wavelenth and period'
  cp = wavelength/T
  return(cp.to(u.m/u.s))

def wavenumber(wavelength):
  'Returns the wavenumber given the wavelength'
  k = 2*np.pi / wavelength
  return(k.to(u.m**-1))

periods = np.array([10, 2, 1, 2, 3])*u.s
# print(periods.magnitude,periods.units)
heights = np.array([10, 10, .15, .15, .15])*u.m

wavelength_soln = wavelength(periods,heights)
print(wavelength_soln.magnitude)

celarity_soln = celarity(wavelength_soln,periods)
print(celarity_soln.magnitude,celarity_soln.units)

wavenumber_soln = wavenumber(wavelength_soln)

kh = wavenumber_soln * heights
print(kh.magnitude)

```

| Period(s) | Height(m) | wavelenth(m) | Wave Speed(m/s) | Wave type    | Dispersivity   |
| --------- | --------- | ------------ | --------------- | ------------ | -------------- |
| 10        | 10        | 96.48377771  | 9.64837777      | Transitional | Dispersive     |
| 2         | 10        | 6.24310728   | 3.12155364      | Deep         | Dispersive     |
| 1         | .15       | 1.14670339   | 1.14670339      | Transitional | Dispersive     |
| 2         | .15       | 2.41654617   | 1.20827309      | Transitional | Dispersive     |
| 3         | .15       | 3.63581453   | 1.21193818      | Shallow      | Non-dispersive |

```python
t = np.linspace(.1,10,100)
a = [0.5,1,0.1]
sig = [2*np.pi/15, 2*np.pi/20, 2*np.pi/25]



# def eta(t):
#   'Returns the location of the free surface given time'
#   eta_soln = [np.empty([100,3])]
#   for i in range(len(t)):
#     k = 0
#     result = a[k] * np.cos(sig[k]*t[i])
#     eta_soln = np.append(eta_soln, [result])
#   return(eta_soln)

eta_soln0 = []
for i in range(len(t)):
  result0 = a[0] * np.cos(sig[0]*t[i])
  eta_soln0 = np.append(eta_soln0,[result0])
  print(eta_soln0)

eta_soln1 = []
for i in range(len(t)):
  result1 = a[1] * np.cos(sig[1]*t[i])
  eta_soln1 = np.append(eta_soln1,[result1])
  print(eta_soln1)

eta_soln2 = []
for i in range(len(t)):
  result2 = a[2] * np.cos(sig[2]*t[i])
  eta_soln2 = np.append(eta_soln2,[result2])
  print(eta_soln2)

data = [eta_soln0]
print(data)
dataT = [[eta_soln0]].T
data = [[eta_soln0].T,[eta_soln1].T]
data = [[1,2,3],
        [1,2,3]]

column = 1
print sum(row[column] for row in data)


```
