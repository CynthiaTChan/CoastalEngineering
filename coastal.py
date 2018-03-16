from aide_design.play import*
import math
from scipy import optimize

g = 9.80665 * u.m/u.s**2


@u.wraps(u.m/u.s, [u.m, u.s], False)
def celerity(wavelength, T):
    '''Returns the velocity given a wavelenth and period'''
    cp = wavelength/T
    return(cp)


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
    k_bound2 = 20

    def _dispersion_k(k):
        return (g.magnitude * k * np.tanh(k * h) - (((2 * np.pi) / T))**2)
    root = optimize.ridder(_dispersion_k, k_bound1, k_bound2)
    return(root)


@u.wraps(u.m, [None], False)
def wavelength(k):
    '''Returns wavelength given the period and water depth.'''
    length = 2*np.pi / k
    return(length)


@u.wraps(u.m/u.s, [u.s, u.m, u.m, u.s, u.m, u.m], False)
def velocity_u1(T, h, a, t, x, z):
    '''Returns the x-direction velocity for a wave. Inputs are period,
    water depth, amplitude, time, x-coord, and z-coord'''
    sig = (2 * np.pi/T)
    k = wavenumber(T, h)
    velocity_u = a * sig * (np.cosh(k*(h+z))/np.sinh(k*h)) * (
        np.cos(k*x - sig*t))
    return(velocity_u)


@u.wraps(u.m/u.s, [u.s, u.m, u.m, u.s, u.m, u.m], False)
def velocity_u2(T, h, a, t, x, z):
    '''Returns the x-direction velocity for a wave. Inputs are period,
    water depth, amplitude, time, x-coord, and z-coord'''
    sig = (2 * np.pi/T)
    k = wavenumber(T, h)
    velocity_u = a * sig * (np.cosh(k*(h+z))/np.sinh(k*h)) * (
        np.cos(k*x - sig*t))
    return(velocity_u)


@u.wraps(u.m/u.s, [u.s, u.m, u.m, u.s, u.m, u.m], False)
def velocity_w(T, h, a, t, x, z):
    '''Returns the z-direction velocity for a wave. Inputs are period,
    water depth, amplitude, time, x-coord, and z-coord'''
    sig = (2 * np.pi/T)
    k = wavenumber(T, h)
    velocity_w = a * sig * (np.sinh(k*(h+z))/np.sinh(k*h)) * (
        np.sin(k*x - sig*t))
    return(velocity_w)


@u.wraps(u.Pa, [u.s, u.m, u.m, u.s, u.m, u.m, u.degK], False)
def pressure_wave(T, h, a, t, x, z, temp):
    '''Returns the pressure of a wave from both the hydrostatic and dynamic
    components. Inputs are period, water depth, amplitude, time, x-coord, and
    z-coord. I assume a density of pure water based on a temperature of 20C'''
    sig = (2 * np.pi/T)
    k = wavenumber(T, h)
    rho_h2o = (pc.density_water(temp)).magnitude
    pressure = (rho_h2o * g.magnitude * a * np.cosh(k*(h+z))/np.cosh(k*h) * (
        np.cos(k*x - sig*t)) + (-rho_h2o * g.magnitude * z))
    return(pressure)


@u.wraps(u.N, [u.s, u.m, u.m, u.degK], False)
def force_max(T, h, a, temp):
    '''Returns the maximum force exerted at a wall. Inputs are period, water
    depth, amplitude, and water temperature.'''
    k = wavenumber(T, h)
    rho_h2o = (pc.density_water(temp)).magnitude
    H = 2 * a
    force = (rho_h2o * g.magnitude * h * H / 2 * np.tanh(k * h) / (k * h)) + (
            rho_h2o * g.magnitude * ((4 * h**2 + H**2) / 8))
    return(force)


@u.wraps(u.Hz, [u.s], False)
def freq_angular(T):
    sig = (2 * np.pi)/T
    return(sig)
