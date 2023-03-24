"""Feedback Prize デモ用関数

gradio による Feedback Prize のデモ feedback-prize_model_demo.py で利用する関数

"""

from ast import arg
import sys
import re
import os
import pathlib

import pandas as pd

import spacy
from spacy import displacy

import matplotlib.pyplot as plt
import numpy as np


sys.path.append('../')


from feedback_prize_2021.src.models.huggingface_transformers import BERT


class CFG():
    """設定"""
    data_path="../feedback_prize_2021/data/feedback-prize-2021/"
    device='cpu'

train=pd.read_csv(os.path.join(CFG.data_path,"train.csv"),index_col='id')


models={
    "BERT":None,
    "RoBERTa":None,
    "DeBERTa":None,
}
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

    # 解析対象の文章
    
    
    text='select input type'

    # 対象の文章をデータから持ってくる
    if input_type=='use data':
        text=pathlib.Path(
                os.path.join(CFG.data_path,'train',essay_id+'.txt')
            ).read_text(encoding='utf-8')
    # 対象の文章を直接入力
    if input_type=='write':
        text=essay

    # ラベルをアノテーション情報から決定
    if input_type=='use data' and annotation_type=='groundtruth':
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

    

    # ラベルをアノテーション情報をモデルで推定
    if annotation_type=='prediction':

        if model_name=='BERT':

            if models['BERT']==None:
                print("setting BERT model...")
                # models['BERT']=BERT.transformers_BERT(pretrained_path='bert-base-uncased',device=CFG.device)
                models['BERT']=BERT.transformers_BERT(pretrained_path='../feedback_prize_2021/output/BERT/checkpoint-2160',device=CFG.device)

            text_with_annotation=element_predict(text,models['BERT'])

        # if model_name=='RoBERTa':

        #     if models['RoBERTa']==None:
        #         print("setting RoBERTa model...")
        #         models['RoBERTa']=BERT.transformers_RoBERTa(pretrained_path='bert-base-uncased',device=CFG.device)

        #     text_with_annotation=element_predict(text,models['RoBERTa'])

        if model_name=='DeBERTa':

            text_with_annotation=[("DeBERTa","Claim")]

        print(text_with_annotation)
        return text_with_annotation

    if annotation_type=='none':
        return re.split('[\n.]',text)



            

        # color_map={
        #     'Lead': '#8000ff',
        #     'Position': '#2b7ff6',
        #     'Evidence': '#2adddd',
        #     'Claim': '#80ffb4',
        #     'Concluding Statement': 'd4dd80',
        #     'Counterclaim': '#ff8042',
        #     'Rebuttal': '#ff0000'
        # }
        
        # # print("text:"+text)
        # # print(re.split('\n',text))
        # segments=re.split('[\n.,]',text)
        # if "" in segments:
        #     segments.remove('')

        # print(segments)

        # return [
        #     (word, list(color_map.keys())[len(word)%len(color_map)]) for word in segments
        # ]




def element_predict(text,model):
    """
    text内文章のelementをmodelを使って推定
    """
    sentences_with_annotation=[]

    sentences=re.split('[\n.]',text)

    argument_elements=['Lead','Position','Evidence','Claim', 'Concluding Statement', 'Counterclaim', 'Rebuttal']

    for sentence in sentences:

        inputs=model.tokenizer(sentence, return_tensors="pt")

        pred=model.model.forward(**inputs).logits.detach().numpy().argmax()
        # pre=model.forward(sentence)

        # pred=np.random.randint(0,7)

        sentences_with_annotation.append((sentence,argument_elements[0]))

    return sentences_with_annotation



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