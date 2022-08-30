import os
import matplotlib.pyplot as plt


def get_center(image):
    center = (image.shape[0] / 2 + .5, image.shape[1] / 2 + .5)
    return center


def subplot_result(image1, image2, title, draw_center=None):
    plt.figure(title)
    plt.subplot(121), plt.imshow(image1, cmap="gray")
    plt.xticks([]), plt.yticks([])
    if draw_center == 1:
        center1 = get_center(image1)
        draw_center_point(center1[0], center1[1])

    plt.subplot(122), plt.imshow(image2, cmap='gray')
    plt.xticks([]), plt.yticks([])
    if draw_center == 1:
        center2 = get_center(image2)
        draw_center_point(center2[0], center2[1])


def plot_result(image, title):
    plt.figure(title)
    plt.imshow(image, cmap="gray")
    plt.xticks([]), plt.yticks([])


def save_picture(image, title):
    plt.figure(title)
    plt.imshow(image, cmap="gray")
    plt.xticks([]), plt.yticks([])
    plt.savefig(title + '.png')


def draw_center_point(x, y):
    plt.scatter(x, y, color='r')


def save_pictures(results_list):
    if not os.path.exists('results'):
        os.mkdir('results')
    os.chdir('./results')
    for i in range(len(results_list)):
        save_picture(results_list[i][0], results_list[i][1])
