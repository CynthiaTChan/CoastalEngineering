Cynthia Chan
</br>
CEE 4530
</br>
March 14, 2018
</br>
Lab 2

### Introduction
The "Dispersion Relation and Water Particle Velocity" lab aims to inform students on some of the fundamental principles in linear, or small amplitude wave theory. The dispersion relationship refers to angular wave frequency, or $\sigma$, which is related to $kh$, a dimensionless height parameter, by the following equation:

$$ \sigma^2 = g\cdot k\cdot tanh(kh)$$

The wave particle veloicty is measured using an acoustic Doppler velocimeter (ADV). The ADV works in a Eulerian frame and uses both geometry and trigonometry to measure the three components of velocity at a given point.

### Experimental Setup

The disperion relation section of the lab uses two wave gauges and a wavemaker in a flume. One wave gauge is fixed and the other is slowly moved away from the fixed gauge until the two gauges are in phase. When they are in phase they should only be one wavelength from each other. This value is recorded and is the wavelength of the wave for the given frequency.

The wave particle velocity portion of this lab uses a ADV to obtain wave velocity data in three directions for the wave frequency of 1 Hz. The wavemaker frequency is kept constant while the depth of deployment for the ADV is changed and recorded at four different depths below the still water level.

### Methods
#### Dispersion Relation

From experimental data, we have an experimental wavelength value. The depth of the water in the flume is 0.2 m.

$$ k = \frac{2\pi}{\lambda}$$
$$ kh = k \cdot  h $$

In order to graph $\frac{\sigma^2h}{g}$ needs to be a function of kh.
$$ \frac{\sigma^2h}{g} = kh \cdot \tanh{kh}$$

Wave celerity can be calculated as follows.
$$c_{p} = \lambda \cdot f $$
$$\frac{c_{p}}{gh} = \sqrt{\frac{\tanh{kh}}{kh \cdot g\cdot h}} $$

#### Wave Particle Velocity

First, `.dat` files are opened in R and labeled according to `.hdr` files. Extraneous data points are deleted so that the u_max values start at a crest. The sampling frequency is 200 Hz.

In order to obtain a $u_{max}$ value, the u values are sorted by absolute value, then the mean of the largest 800 (~10%) is used as the $u_{max}$ value for the given heights.

Next, amplitude is calculated for each wave depth from the velocity component. Since the wave extraneous data is deleted such that the waves start at a crest, x=0, and assumed to start at t=0, the cosine term goes to 1.

#### Horizontal Velocity
$$ u = a\sigma \cdot \frac{\cosh k(h+z)}{\sinh(kh)}\cos(kx-\sigma t)$$

$$ u = a\sigma \cdot \frac{\cosh k(h+z)}{\sinh(kh)}$$
#### Vertical Velocity
$$ w = a\sigma \cdot \frac{\sinh k(h+z)}{\sinh(kh)}\sin(kx-\sigma t)$$

$$ w = a\sigma \cdot \frac{\sinh k(h+z)}{\sinh(kh)} $$

The $\sigma$ value that goes into the above values is 6.28, calculated from $\sigma = 2\pi f$. The $k$ value can be calculated from a solver using period, $T$ and depth of water and is $k$ = 5.18.


| Depth (m) | $u$ (m/s) | $a$ (m) |
| --------- | --------- | ------- |
| -0.075    | 0.093     | 0.0149  |
| -0.1      | 0.082     | 0.0141  |
| -0.125    | 0.071     | 0.0130  |
| -0.175    | 0.070     | 0.0137  |


| Depth (m) | $w$ (m/s) | $a$ (m) |
| --------- | --------- | ------- |
| -0.075    | 0.042     | 0.0119  |
| -0.1      | 0.038     | 0.0140  |
| -0.125    | 0.026     | 0.0129  |
| -0.175    | 0.011     | 0.0178  |

After amplitude values are obtained from the velocities, a theoretical amplitude is set to be the mean of the above 8 experimental amplitudes.

The theoretical amplitude is 0.014 m. This theoretical value is used in conjunction with $\sigma$ and $k$ which do not change, to obtain theoretical $u_{max}$ and $w_{max}$ values.

### Results and Discussion

In the two figures below, the experimental data and the theoretical for the dispersion relationship match very well. The experimental data for a given frequency is similar between 5 and 10 mm strokes because $kh$ and $\frac{\sigma^2h}{g}$ are not functions of amplitude.
![Disp_5](/Users/cynthia/github/CoastalEngineering/Disp_5.png)

![Disp10](/Users/cynthia/github/CoastalEngineering/Disp_10.png)


The two figures below show the relationship between experimental and theoretical wave celerity. In the 10 mm stroke condition, the theoretical wave celerity underestimates the observed data. This may be due to some error that had increasing perturbation from one parameter, dispersion, to the next, celerity.
![Cel_5](/Users/cynthia/github/CoastalEngineering/Cel_5.png)

![Cel_10](/Users/cynthia/github/CoastalEngineering/Cel_10.png)


The two figures below show the vertical profile of both horizontal velocity ($u$) and vertical velocity ($w$). The theoretical values and observed values for maximum horizontal velocity do not match very well, although the trend is captured in the observed data. It seems that there was some error in the ADV vertical placement due to human error and error in reading ruler measurements in water. The vertical velocity vertical profile matches more closely to the theoretical values. 
![umax](/Users/cynthia/github/CoastalEngineering/umax.png)

![wmax](/Users/cynthia/github/CoastalEngineering/max.png)
