```python
from aide_design.play import*
from coastal import*
from scipy import optimize
```
# Cynthia Chan
### Problem Set 2

#####1i. Find the wave speed and wavelength.
$$ c_{p} = \frac{\lambda}{T} = \frac{\sigma}{k}$$
$$ \lambda = \frac{2\pi}{k}$$
$$ \sigma^2 = g\cdot k\cdot tanh(kh)$$

Rearrange the dispersion equation to solve for k, wave number, alone.
$$ \left( \frac{2\pi}{T} \right)^2 = g\cdot k\cdot tanh(kh)$$
$$ 0 =  g\cdot k\cdot tanh(kh) - \left( \frac{2\pi}{T} \right)^2$$


```python
period = 4 * u.s
height = 5 * u.m
g = 9.80665 * u.m/u.s**2

k_number = wavenumber(period, height, 0.1, 3)
wave_length = wavelength(k_number)
wave_speed = celerity(wave_length, period)
```
| Parameter  | Value     |
| ---------- | --------- |
| k          | 0.2831    |
| wavelength | 22.19 m   |
| wave speed | 5.548 m/s |
#####1ii. Find the component water parcel velocities (u,w) and the pressure a distance 2 meters below the still water level and under the wave crest.

| Parameter               | Value     |
| ----------------------- | --------- |
| u velocity              | 1.121 m/s |
| w velocity              | 0 m/s     |
| pressure (z = -2m)      | 25.76 kPa |
| pressure crest (z = 1m) | 2.888 kPa |

```python
z = -2 * u.m
z_crest = 1 * u.m
x = 0 * u.m
t = 0 * u.s
temp = 20 * u.degC
amp = 1 * u.m

vel_u = velocity_u(period, height, amp, t, x, z)
vel_w = velocity_w(period, height, amp, t, x, z)
pressure = pressure_wave(period, height, amp, t, x, z, temp)
pressure_crest = pressure_wave(period, height, amp, t, x, z_crest, temp)
```


#####2ai. Find the minimum height of the seawall to prevent flooding.
The minimum height of the seawall is sum of the depth of the water and twice the amplitude of the waves.

$$H_{wall, min} = h + 2a$$
```python
height_design = 3 * u.m
amp_design = 0.5 * u.m
height_wall = 2 * amp_design + height_design
```
**The minimum wall height is 4 meters.**

#####2aii. Find the maximum force on the seawall.

From Dean and Dalmrymple, the first order wave force equation is as follows:
$$ F = \rho \frac{g h^2}{2} + \rho g h \left(\frac{tanh(kh)}{kh}\right)\eta_{w}$$

The maximum force occurs when:
$$ \eta = H/2 $$
This substitution results in the maximum force for a wave on a wall equation.

$$ F_{max} = \rho g \left(\frac{4h^2 + H^2}{8}\right) + \rho g h \frac{H}{2}\left(\frac{tanh(kh)}{kh}\right)$$

```python
period_design = 10* u.s
force_max = force_max(period_design, height_design, amp_design, temp)
```

**The maximum force exerted on the wall is 59.3 kN.**

pandoc PS2.md -o Cynthia_Chan_PS2.pdf
