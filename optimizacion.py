from skimage import io,color
import matplotlib.pyplot as plt
imagen =io.imread('Imagen3.png')
imagen1 =io.imread('Imagen3.png')
imagengris = color.rgb2gray(imagen)
imageng = color.rgb2gray(imagen)
imagengc = color.rgb2gray(imagen)
plt.title('Imagen original')
print (imagen.shape)
imagenca=imagengris
for i in range(568):
    for j in range(1218):
        if imagenca[i][j]<=0.38  and imagenca[i][j]>=0.27:
            imagenca[i][j]=0
            imagengc[i][j]=1
        else:
            imagenca[i][j]=1
            imagengc[i][j]=0

plt.subplot(221)
plt.imshow(imagenca, cmap='gray')
plt.title('pastos')
plt.subplot(222)
plt.imshow(imagen)
plt.title('Pasto y casas')
plt.subplot(223)
plt.imshow(imageng, cmap='gray')
plt.title('Imagen en gris')
plt.subplot(224)
plt.imshow(imagengc, cmap='gray')
plt.title('calles')
plt.show()