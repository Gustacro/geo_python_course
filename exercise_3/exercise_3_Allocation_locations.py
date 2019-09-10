

# exercise 3 from Geo Python Course 

# Station names
stations = ['Hanko Russarö', 'Heinola Asemantaus', 'Helsinki Kaisaniemi', 
            'Helsinki Malmi airfield', 'Hyvinkää Hyvinkäänkylä', 'Joutsa Savenaho', 
            'Juuka Niemelä', 'Jyväskylä airport', 'Kaarina Yltöinen', 'Kauhava airfield', 
            'Kemi Kemi-Tornio airport', 'Kotka Rankki', 'Kouvola Anjala', 
            'Kouvola Utti airport', 'Kuopio Maaninka', 'Kuusamo airport', 
            'Lieksa Lampela', 'Mustasaari Valassaaret', 'Parainen Utö', 'Pori airport', 
            'Rovaniemi Apukka', 'Salo Kärkkä', 'Savonlinna Punkaharju Laukansaari', 
            'Seinäjoki Pelmaa', 'Siikajoki Ruukki', 'Siilinjärvi Kuopio airport', 
            'Tohmajärvi Kemie', 'Utsjoki Nuorgam', 'Vaala Pelso', 'Vaasa airport', 
            'Vesanto Sonkari', 'Vieremä Kaarakkala', 'Vihti Maasoja', 'Ylitornio Meltosjärvi']

# Latitude coordinates of Weather stations  
lats = [59.77, 61.2, 60.18, 60.25, 60.6, 61.88, 63.23, 62.4,
       60.39, 63.12, 65.78, 60.38, 60.7, 60.9, 63.14, 65.99,
       63.32, 63.44, 59.78, 61.47, 66.58, 60.37, 61.8, 62.94,
       64.68, 63.01, 62.24, 70.08, 64.5, 63.06, 62.92, 63.84,
       60.42, 66.53]

# Longitude coordinates of Weather stations 
lons = [22.95, 26.05, 24.94, 25.05, 24.8, 26.09, 29.23, 25.67, 
       22.55, 23.04, 24.58, 26.96, 26.81, 26.95, 27.31, 29.23, 
       30.05, 21.07, 21.37, 21.79, 26.01, 23.11, 29.32, 22.49, 
       25.09, 27.8, 30.35, 27.9, 26.42, 21.75, 26.42, 27.22, 
       24.4, 24.65]

# Cutoff values that correspond to the centroid of Finnish mainland
# North - South
north_south_cutoff = 64.5

# East-West
east_west_cutoff = 26.3

# REPLACE THE ERROR BELOW WITH YOUR OWN CODE
# variables
north_west = []
south_east = []
north_east = []
south_west = []

# This test print should work
# print(north_west, south_west)

# REPLACE THE ERROR BELOW WITH YOUR OWN CODE
N = len(stations)

# How many stations do we have?
print("In the data, there are", N, "stations.")


# REPLACE THE ERROR BELOW WITH YOUR OWN CODE
for name, lat, lon in zip(stations, lats, lons):
    if lat >= north_south_cutoff and lon >= east_west_cutoff:
        north_east.append(name)
    elif lat <= north_south_cutoff and lon >= east_west_cutoff:
        south_east.append(name)
    elif lat <= north_south_cutoff and lon <= east_west_cutoff:
        south_west.append(name)
    elif lat >= north_south_cutoff and lon <= east_west_cutoff:
        north_west.append(name)

# This test print should print out station names in North West
# Hint: there should be 4 stations in this class
# print("The names of the North-West stations are:\n", north_west)


# This test print should print out station names in North Eest
# Hint: there should be 2 stations in this class
# print("The names of the North-East stations are:\n", north_east)

# This test print should print out station names in South West
# Hint: there should be 16 stations in this class
# print("The names of the South-West stations are:\n", south_west)


# This test print should print out station names in South East
# Hint: there should be 12 stations in this class
# print("The names of the South-East stations are:\n", south_east)


# REPLACE THE ERROR BELOW WITH YOUR OWN CODE
north_west_share = (len(north_west) * 100)/ N
north_east_share = (len(north_east) * 100)/ N
south_west_share = (len(south_west) * 100)/ N
south_east_share = (len(south_east) * 100)/ N

# Print the information (you don't need to modify this)
# .format() is a Python function that can be used to easily insert values inside a text-template such as below.
# .0f below is a specific operator that rounds the decimal values into whole numbers
print("North-West contains{share: .0f} % of all stations.".format(share=north_west_share)) # formating str to obtain n decimals numbers {x : .<num_decimals><f>}
print("North-East contains{share: .0f} % of all stations.".format(share=north_east_share))
print("South-West contains{share: .0f} % of all stations.".format(share=south_west_share))
print("South-East contains{share: .0f} % of all stations.".format(share=south_east_share))

