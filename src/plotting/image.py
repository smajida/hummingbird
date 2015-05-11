"""A plotting module for images"""
import numpy as np
import ipc

images = {}
def plotImage(record, history=10):
    """Plotting record.data as an image

    Args:
        :record(Record): Record to be plotted as an image

    Kwargs:
        :history(int):  Length of history buffer
    """
    if(not record.name in images):
        ipc.broadcast.init_data(record.name, data_type='image', history_length=history)
        images[record.name] = True
    image = record.data
    sh = image.shape
    if (image.ndim == 3):
        image = image.reshape(sh[0]*sh[2], sh[1])
    ipc.new_data(record.name, image)