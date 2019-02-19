# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import os
import sys
from matplotlib.offsetbox import (OffsetImage,
                                  AnnotationBbox)
import numpy as np
from scipy.misc import imresize

path = '/home/victor/vtrappler.github.io/_personalprojects/lnb logos/'
files = os.listdir(path)
import csv




def imscatter(x, y, image, ax=None, zoom=1, size = 200):
    if ax is None:
        ax = plt.gca()
    try:
        image = plt.imread(image)
    except TypeError:
        # Likely already an array...
        pass

    ratio = float(image.shape[1]) / float(image.shape[0])
    image = imresize(arr=image, size=(size, int(size * ratio)))
    im = OffsetImage(image, zoom=zoom)
    x, y = np.atleast_1d(x, y)
    artists = []
    for x0, y0 in zip(x, y):
        ab = AnnotationBbox(im, (x0, y0), xycoords='data', frameon=False)
        artists.append(ax.add_artist(ab))
    ax.update_datalim(np.column_stack([x, y]))
    ax.autoscale()
    return artists


def main(filename):
    fig, ax = plt.subplots()
    Or = np.empty(18)
    Dr = np.empty(18)
    njour = filename[-6:-4]
    print 'file extension: ' + str(njour)
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            team_name = row['team'].lower()
            ORTG = np.random.rand()
            DRTG = np.random.rand()
            ORTG = float(row['ORTG'])
            Or[i] = ORTG
            DRTG = float(row['DRTG'])
            Dr[i] = DRTG
            print team_name, ORTG, DRTG
            ext = '.png'
            if team_name == 'dijon':
                ext = '.gif'
            name = path + team_name + ext
            if team_name == 'fos':
                zoom = 0.3
            else:
                zoom = 0.5
            imscatter(ORTG, DRTG, name, zoom=zoom, ax=ax)
    plt.plot([Or.min(), Or.max()], [Or.min(), Or.max()], 'k')
    plt.xlabel('ORTG', fontsize = 18)
    plt.ylabel('DRTG', fontsize = 18)
    ax.tick_params(length=6, width=2, labelsize = 'large')
    props = dict(facecolor='white', alpha=0.9)
    ftsize = 18
    ax.text(0.0, 1.0, u'Mauvaise attaque\nMauvaise défense', transform=ax.transAxes, fontsize=ftsize,
            verticalalignment='top', bbox=props, clip_on=True)
    ax.text(0.90, 1.0, u'Bonne attaque\nMauvaise défense', transform=ax.transAxes, fontsize=ftsize,
            verticalalignment='top', bbox=props, clip_on=True)
    ax.text(0.0, 0.0, u'Mauvaise attaque\nBonne défense', transform=ax.transAxes, fontsize=ftsize,
            verticalalignment='top', bbox=props, clip_on=True)
    ax.text(0.90, 0.0, u'Bonne attaque\nBonne défense', transform=ax.transAxes, fontsize=ftsize,
            verticalalignment='top', bbox=props, clip_on=True)
    plt.grid(alpha = 0.4)
    ax.set_title(u'Offensive vs Defensive Rating\nJeepElite Journée ' + str(njour), fontsize = 20)
    plt.show()


# main('/home/victor/vtrappler.github.io/_personalprojects/stats_lnb_19.csv')
# filename = '/home/victor/vtrappler.github.io/_personalprojects/stats_lnb_19.csv'

if __name__ == '__main__':
    main(str(sys.argv[1]))
