# Create a Class to read, manipulate, display & write a ppm file

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

class ppmImage:
#constructor
  def __init__(self,magic_number, width, height, max_value=255 ):
    self.magic_number = magic_number
    self.width = width
    self.height = height
    self.max_value = max_value

    # We need to set this up to allow us to directly set pixels
    # and not have to read in a file. Otherwise we will get an error
    # when we have more than one object
    self.pixels = []
    for i in range(self.height):
      row = []
      for j in range(self.width):
        r=g=b = int(0)
        row.append((r, g, b))
      self.pixels.append(row)

  def read(self, filename):
    with open(filename, 'rb') as ppm_file:
      self.magic_number = ppm_file.readline().decode().strip()
      self.width, self.height = map(int, ppm_file.readline().decode().strip().split())
      self.max_value = ppm_file.readline().decode().strip()
      self.pixels = []
      for i in range(self.height):
        row = []
        for j in range(self.width):
         # reads 3 bytes an converts them to ints.
         r, g, b = map(int, ppm_file.read(3))
         # if you don't want to use map the following 3 lines do the same thing.
         #r = int.from_bytes(ppm_file.read(1), "big")
         #g = int.from_bytes(ppm_file.read(1), "big")
         #b = int.from_bytes(ppm_file.read(1), "big")
         row.append((r,g,b))
        self.pixels.append(row)

  def display(self):
    #pixel_array = np.array(self.pixels, dtype=np.uint8)
    plt.imshow(self.pixels)
    plt.axis('off')
    plt.show()

  def make_white_image(self):
      for i in range(self.width):
        for j in range(self.height):
            self.pixels[j][i] = (255, 255, 255)

  def manipulate_all_pixels(self):
      for i in range(self.width):
        for j in range(self.height):
            self.pixels[j][i] = (255, 0, 255)


  def print_raw_pixels(self):
    for i in range(3):
      for j in range (3):
        print(self.pixels[i][j])

  def write(self, filename):
        with open(filename, 'wb') as ppm_file:
            ppm_file.write(f"{self.magic_number}\n".encode())
            ppm_file.write(f"{self.width} {self.height}\n".encode())
            ppm_file.write(f"{self.max_value}\n".encode())
            for i in range(self.width):
              for j in range(self.height):
                ppm_file.write(bytes(self.pixels[j][i]))

  #def draw_square(square_x, square_y, square_size, r, g, b):

  def Invert(self):
      for i in range(self.width):
        for j in range(self.height):
            r = self.pixels[j][i][0]
            g = self.pixels[j][i][1]
            b = self.pixels[j][i][2]
            #x = 3 if a==2 else 0
            new_r = r-255 if ((r-255)>0) else -(r-255)
            new_g = b-255 if ((b-255)>0) else -(b-255)
            new_b = g-255 if ((g-255)>0) else -(g-255)
            self.pixels[j][i] = (new_r, new_g, new_b)

  def Greyscale(self):
      for i in range(self.width):
        for j in range(self.height):
            r = self.pixels[j][i][0]
            g = self.pixels[j][i][1]
            b = self.pixels[j][i][2]
            new_r = int((r * 0.299) + (g * 0.587) + (b * 0.114));
            new_g = int((r * 0.299) + (g * 0.587) + (b * 0.114));
            new_b = int((r * 0.299) + (g * 0.587) + (b * 0.114));
            self.pixels[j][i] = (new_r, new_g, new_b)


  def Sepia(self):
      #Red_new = 0.272 * Red_old + 0.534 * Green_old + 0.131 * Blue_old
      #Green_new = 0.349 * Red_old + 0.686 * Green_old + 0.168 * Blue_old
      #Blue_new = 0.393 * Red_old + 0.769 * Green_old + 0.189 * Blue_old
      for i in range(self.width):
        for j in range(self.height):
            r = self.pixels[j][i][0]
            g = self.pixels[j][i][1]
            b = self.pixels[j][i][2]
            new_r = int(0.393 * r + 0.769 * g + 0.189 * b)
            new_g = int(0.349 * r + 0.686 * g + 0.168 * b)
            new_b = int(0.272 * r + 0.534 * g + 0.131 * b)
            self.pixels[j][i] = (new_r, new_g, new_b)

  def Pixel_Noise(self):
      for i in range(self.width):
        for j in range(self.height):
            r = self.pixels[j][i][0]
            g = self.pixels[j][i][1]
            b = self.pixels[j][i][2]
            new_r = (random.randint(0, 60) + r) % 255
            new_g = (random.randint(0, 60) + g) % 255
            new_b = (random.randint(0, 60) + b) % 255
            self.pixels[j][i] = (new_r, new_g, new_b)

  def Thresholding(self):
      for i in range(self.width):
        for j in range(self.height):
            if ( (self.pixels[j][i][0]+self.pixels[j][i][1]+self.pixels[j][i][2])> 300):
              self.pixels[j][i] = (0, 0, 0)
            else:
              self.pixels[j][i] = (255, 255, 255)

  def Color_Channel_Swap(self):
      for i in range(self.width):
        for j in range(self.height):
            r = self.pixels[j][i][0]
            g = self.pixels[j][i][1]
            b = self.pixels[j][i][2]
            self.pixels[j][i] = (b, g, r)
  
  def draw_square(self, square_x, square_y, square_size, r, g, b):
      for i in range(square_x):
        for j in range(square_y):
         self.pixels[j][i] = (b, g, r)

  def my_own(self):
      for i in range(self.width):
        for j in range(self.height):
          r = self.pixels[j][i][0]
          g = self.pixels[j][i][1]
          b = self.pixels[j][i][2]
          r = (r + g + b)%255
          g = (r + g + b)%255
          b = (r + g + b)%255
          self.pixels[j][i] = (r, g, b)

# A simple image object
image = ppmImage("P6", 200, 500, 255)
image.read("redCube.ppm")
image.display()


myimage = ppmImage("P6", 200, 500, 255)
myimage.read("redCube.ppm")
#myimage.manipulate_all_pixels()
myimage.Sepia()
myimage.display()
myimage.write('output.ppm')
