with open("movie.txt", "w") as file_obj:

    file_obj.write("the movies i watched previous year:  \n 1.purple hearts \n 2. beach rats \n 3. my policeman \n 4. umbrella academy")

file = open("movie.txt", "r")

file1 = file.read()
print(file1)


import numpy
