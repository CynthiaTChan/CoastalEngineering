```python
from aide_design.play import*
from coastal import*
```
# Cynthia Chan
### Problem Set 3

1. You are building a small pier to be supported by piles. The water depth at
the front row of piles is **h(x)= 2 m**. The beach slope is **1/30**. A wave
buoy in the “deep water” measured the following wave conditions: Wave amplitude
**a = 0.5 m**; wave period **T = 12 sec**.

| Parameter | Value      |
| --------- | ---------- |
| Amplitude | 0.7271 m   |
| $kh$      | 0.238      |
| $u_{max}$ | 1.595 m/s  |
| $w_{max}$ | 0.3807 m/s |

a. Minimum clearance needed to maintain a dry deck

Wave Energy Conservation
$$ \overline{E}_0^+\cdot c_{g0} = \overline{E}_1^+\cdot c_{g1} $$

Using the relationship between energy and amplitude, relate the wave energy
conservation to an energy normalized by density basis.
$$ \overline{E}^+ = \frac{\rho g a^2}{2}$$
$$ \frac{a_1}{a_0} = \sqrt{\frac{c_{g0}}{c_{g1}}}$$


In deep water conditions, phase velocity can be simplified because $kh$ is large
so the $tanh(kh)$ term approaches 1.

$$c_p = \frac{gT}{2\pi } \tanh{kh} $$
$$c_{p0} = \frac{gT}{2\pi } $$

In deep water conditions, n = $\frac{1}{2}$ so the group velocity is
$$c_{g0} = \frac{gT}{2\pi } \cdot \frac{1}{2}$$

Substitute the shallow group velocity with Froude's number and solve only for
amplitude at the shallow regime.
$$a_1 = \frac{a_0\cdot \sqrt{c_{g0}}}{[g \cdot h_1]^{1/4}} $$


```python
amp0 = 0.5 * u.m
period = 12 * u.sec
g = 9.80665 * u.m/u.s**2
hx = 2 * u.m

amp1 = amplitude_shallow(amp0, period, hx)
print(amp1.to(u.m))

```
b. In order to confirm the shallow wave assumptions made above,
$kh < \frac{\pi}{10}$ must be true.

To find $k$, $\sigma$ must first be determined.
$$\sigma = \frac{2\pi}{T}$$
$$k = \sqrt{\frac{\sigma^2}{gh}}$$

Alternatively, the wavenumber function I have written searches for wave number
based on period and height using two bounds on k.

Since $kh$ = 0.238 < $\frac{\pi}{10}$, the shallow water assumption is valid.

```python
kh = wavenumber(period, hx) * hx
print(kh)
```

c. The maximum water particle velocities are as follows:
- Maximum $u$ @ wave crest and trough
- Maximum $w$ @ $\eta$ = 0

### Horizontal Velocity
The extreme values of the horizontal velocity appear at the phase positions
$(kx - \sigma t)$ = 0, $\pi$, ...(under the crest and trough positions).
$$ u = a\sigma \cdot \frac{\cosh k(h+z)}{\sinh(kh)}\cos(kx-\sigma t)$$
The cosine term goes to 1.
$$ u = a\sigma \cdot \frac{\cosh k(h+z)}{\sinh(kh)}$$

The vertical variation of the velocity components is best viewed by
starting at the bottom where k(h + z) = 0. Here the hyperbolic terms involving z
in both the u and w velocities are at their minima, 1 and 0, respectively. As we
progress upward in the fluid, the magnitudes of the velocity components increase.

$$ u = a\sigma \cdot \frac{1}{\sinh(kh)}$$

In shallow water, $\sinh(kh)$ goes to $kh$.
$$ u = \frac{a\sigma}{kh} $$

### Vertical Velocity

The extreme vertical velocities appear at $\pi/2$, $3\pi/2$, (where the
water surface displacement is zero).

$$ w = a\sigma \cdot \frac{\sinh k(h+z)}{\sinh(kh)}\sin(kx-\sigma t)$$

The sine term goes to 1.
$$ w = a\sigma \cdot \frac{\sinh k(h+z)}{\sinh(kh)} $$

The z elevation is 0 where the vertical velocity is greatest. The $sinh(kh)$
terms remaining go to $kh$ in shallow water conditions.

$$ w = a\sigma \cdot \frac{\sinh (kh)}{\sinh(kh)} $$

$$ w = a\sigma $$

```python
sig = freq_angular(period)
uvel = amp1 * sig / kh
print(uvel)

wvel = amp1 * sig
print(wvel)
```

2. Assumptions:
- the system is at steady state and there is no dissipation from geometry
- changes so wave energy can be conserved
- linear wave theory applies
- since H is constant, group velocities can be assumed to be the same
- density of water is constant

$$\overline{E}_1^+\cdot c_{g1} \cdot B_1 = \overline{E}_2^+\cdot c_{g2} \cdot B_2$$

$$ \overline{E}^+ = \frac{\rho g a^2}{2}$$


$$ \frac{\rho g a_1^2}{2}\cdot c_{g1} \cdot B_1 = \frac{\rho g a_2^2}{2}\cdot c_{g2} \cdot B_2 $$

$$ a_1^2 \cdot B_1 = a_2^2 \cdot B_2$$

$$ a_2 = a_1 \sqrt{\frac{B_1}{B_2}} $$

The functions I have defined are as follows:
```python
@u.wraps(u.Hz, [u.s], False)
def freq_angular(T):
    sig = (2 * np.pi)/T
    return(sig)


    @u.wraps(u.m/u.s, [u.s], False)
    def celerity_phase_deep(T):
        '''Returns the phase velocity in deep water conditions'''
        cp = (g*T)/(2*np.pi)
        return(cp)


    @u.wraps(u.m/u.s, [u.s], False)
    def celerity_group_deep(T):
        '''Returns the phase velocity in deep water conditions'''
        cp = (g*T)/(4*np.pi)
        return(cp)


    def amplitude_shallow(a_deep, T, height):
        '''Returns the shallow water wave amplitude. Inputs: deep water amplitude,
        period, shallow water depth.'''
        cg0 = celerity_group_deep(T)
        a = (a_deep * np.sqrt(cg0))/((g * height)**.25)
        return(a)


    @u.wraps(1/u.m, [u.s, u.m], False)
    def wavenumber(T, h):
        '''Returns wavelength given a period, depth of water,
        and two bounds on k. It should be noted that the bounds as a function of k
        less the angular frequency squared should be of different sign. The bounds
        are written inside this function and should be changed later.'''
        k_bound1 = 0
        k_bound2 = 10

        def _dispersion_k(k):
            return (g.magnitude * k * np.tanh(k * h) - (((2 * np.pi) / T))**2)
        root = optimize.ridder(_dispersion_k, k_bound1, k_bound2)
        return(root)

```
pandoc PS3.md -o Cynthia_Chan_PS3.pdf
