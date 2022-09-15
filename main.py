from math import log


def free_space_loss(freq, dist):
    """Return the Free Space Path Loss in dB for a frequency in GHz and distance in km."""

    return 92.45 + 20 * log(dist, 10) + 20 * log(freq, 10)


if __name__ == '__main__':
    f = float(input("Frequency (GHz): "))
    d = float(input("Distance (km): "))
    print(f"Free Space Path Loss at {f}GHz for distance {d:,}km is {free_space_loss(f, d):.2f}db.")
