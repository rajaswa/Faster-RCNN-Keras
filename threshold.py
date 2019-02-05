import pandas as pd

df = pd.read_csv('submit_rcnn.csv')

df[df['x1'] < 0] = 0
df[df['x2'] > 640] = 640
df[df['y1'] < 0] = 0
df[df['y2'] > 480] = 480


df.to_csv('frcnn_threshold.csv')
