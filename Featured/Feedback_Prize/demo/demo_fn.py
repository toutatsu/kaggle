import re
import os
import pathlib

import pandas as pd

import spacy
from spacy import displacy


import matplotlib.pyplot as plt
import numpy as np


class CFG():
    """設定"""
    data_path="./feedback-prize-2021/data/feedback-prize-2021/"

train=pd.read_csv(os.path.join(CFG.data_path,"train.csv"),index_col='id')

# from spacy.tokens import Span

nlp = spacy.blank("en")



def get_discourse(discourse_id):
    """???"""
    return train.iloc[discourse_id].discourse_text



def element_demo(input_type,essay,essay_id,annotation_type,model_name):
    """feedback-prize-2021のデモ用

    Args:
        input_type (str): 'use data' or 'write'
        essay (str): 
        essay_id (str):
        annotation_type,
        model_name

    Returns:
        result (str,str): text, annotation
    """
    # print(text)

    text='select input type'

    if input_type=='use data':
        text=pathlib.Path(
                os.path.join(CFG.data_path,'train',essay_id+'.txt')
            ).read_text(encoding='utf-8')

    if input_type=='write':
        text=essay

    if annotation_type=='groundtruth':
        ents = []
        for _, row in train[train.index== essay_id].iterrows():
            ents.append(

                (row['discourse_text'],row['discourse_type'])
                # {
                #     'word':row['discourse_text']
                #     'start': int(row['discourse_start']), 
                #     'end': int(row['discourse_end']), 
                #     'label': row['discourse_type']
                # }
            )
            ents.append(("\n", None))

        return ents

    if annotation_type=='prediction':

        def predict(text,model_name):

            a=[]

            sentences=re.split('[\n.,]',text)

            for sentence in sentences:

                pass
                # pre=BERT.forward(sentence)

                # a.append(pre)

            return


        if model_name=='BERT':


            pass

        color_map={
            'Lead': '#8000ff',
            'Position': '#2b7ff6',
            'Evidence': '#2adddd',
            'Claim': '#80ffb4',
            'Concluding Statement': 'd4dd80',
            'Counterclaim': '#ff8042',
            'Rebuttal': '#ff0000'
        }
        
        # print("text:"+text)
        # print(re.split('\n',text))
        segments=re.split('[\n.,]',text)
        if "" in segments:
            segments.remove('')

        print(segments)

        return [
            (word, list(color_map.keys())[len(word)%len(color_map)]) for word in segments
        ]


def effectiveness_demo(input_type,essay,essay_id,annotation_type,model_name):

    fig = plt.figure()

    left = np.array([1, 2, 3, 4, 5])
    height = np.array([100, 200, 300, 400, 500])
    plt.bar(left, height)

    return fig


def learning_demo():
    fig = plt.figure()

    left = np.array([1, 2, 3, 4, 5])
    height = np.array([100, 200, 300, 400, 500])
    plt.bar(left, height)

    return fig

# def visualize(text_id):
#     """可視化"""

#     ents = []
#     for _, row in train[train.index== text_id].iterrows():
#         ents.append(
#             {
#                 'start': int(row['discourse_start']), 
#                 'end': int(row['discourse_end']), 
#                 'label': row['discourse_type']
#             }
#         )

#     return displacy.render(
#         {
#             "text": pathlib.Path(
#                 os.path.join(CFG.data_path,'train',text_id+'.txt')
#             ).read_text(encoding='utf-8'),
#             "ents": ents,
#             "title": text_id
#         },
#         style="ent",
#         options={
#             "ents": train.discourse_type.unique().tolist(),
#             "colors":{
#                 'Lead': '#8000ff',
#                 'Position': '#2b7ff6',
#                 'Evidence': '#2adddd',
#                 'Claim': '#80ffb4',
#                 'Concluding Statement': 'd4dd80',
#                 'Counterclaim': '#ff8042',
#                 'Rebuttal': '#ff0000'
#             }
#         },
#         manual=True,
#         #jupyter=True
#     )