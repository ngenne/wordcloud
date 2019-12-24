# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:15:14 2019

@author: NGENNE
"""

## WORDCLOUD ##

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator


print('\nEnter text and if you want to make the display bigger than other words, write it few times, or just paste your text\n')
text = str(input())

print('\nPaste the absolute path to the image file without quotes\n')
mask = np.array(Image.open(str(input()), mode='r')) # without quotes, if not it will raise an error 22
image_colors = ImageColorGenerator(mask)

def wordcloud_gen(text): # optionally add: stopwords=STOPWORDS to determine after which pattern of words you want it stops
    wordcloud = WordCloud(font_path=r'C:\windows\Fonts\Arial.ttf', # if you want a result into another font, you could change the path here
                          width = 1600,
                          height = 800,
                          relative_scaling = 1.0,
                          prefer_horizontal = 0.75,
                          mask = mask,
                          color_func = image_colors,
                          repeat = True,
                          background_color = 'rgba(255, 255, 255, 0)', mode='RGBA'
                          ).generate(text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


wordcloud_gen(text).savefig('wc.png')













