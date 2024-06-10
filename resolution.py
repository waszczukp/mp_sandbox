def resolution(n):
    resolution=0
    while ((n*10**resolution)//1) != (n*10**resolution) or resolution >12:
        resolution = resolution + 1
    return resolution
