"""デモ"""

import re
import os
import pathlib

import pandas as pd
import gradio as gr

import spacy
from spacy import displacy

class CFG():
    """設定"""
    data_path="./feedback-prize-2021/data/feedback-prize-2021/"

train=pd.read_csv(os.path.join(CFG.data_path,"train.csv"),index_col='id')

# from spacy.tokens import Span

nlp = spacy.blank("en")





def get_discourse(discourse_id):
    """???"""
    return train.iloc[discourse_id].discourse_text


# feedback-prize-2021のデモ

def detect_text_element(text):
    """???"""
    # print(text)

    color_map={
        'Lead': '#8000ff',
        'Position': '#2b7ff6',
        'Evidence': '#2adddd',
        'Claim': '#80ffb4',
        'Concluding Statement': 'd4dd80',
        'Counterclaim': '#ff8042',
        'Rebuttal': '#ff0000'
    }
    print(text)
    print(re.split('\n',text))
    segments=re.split('\n',text)
    if "" in segments:
        segments=segments.remove("")

    return [
        (word, list(color_map.keys())[len(word)%len(color_map)]) for word in segments
    ]

element=gr.Interface(
    detect_text_element,
    [
        gr.Textbox(
            label="text",
            lines=3,
            value="input text here",
        ),
    ],
    gr.HighlightedText(
        label="text element",
        combine_adjacent=False,
    ).style(
        color_map={
            'Lead': '#8000ff',
            'Position': '#2b7ff6',
            'Evidence': '#2adddd',
            'Claim': '#80ffb4',
            'Concluding Statement': 'd4dd80',
            'Counterclaim': '#ff8042',
            'Rebuttal': '#ff0000'
        }
    ),
    examples=[
        get_discourse(0),
        get_discourse(1),
        get_discourse(2),
        get_discourse(3),
    ]
)


# feedback-prize-effectivenessのデモ

def visualize(text_id):
    """可視化"""

    ents = []
    for _, row in train[train.index== text_id].iterrows():
        ents.append(
            {
                'start': int(row['discourse_start']), 
                'end': int(row['discourse_end']), 
                'label': row['discourse_type']
            }
        )

    return displacy.render(
        {
            "text": pathlib.Path(
                os.path.join(CFG.data_path,'train',text_id+'.txt')
            ).read_text(encoding='utf-8'),
            "ents": ents,
            "title": text_id
        },
        style="ent",
        options={
            "ents": train.discourse_type.unique().tolist(),
            "colors":{
                'Lead': '#8000ff',
                'Position': '#2b7ff6',
                'Evidence': '#2adddd',
                'Claim': '#80ffb4',
                'Concluding Statement': 'd4dd80',
                'Counterclaim': '#ff8042',
                'Rebuttal': '#ff0000'
            }
        },
        manual=True,
        #jupyter=True
    )

effectiveness=gr.Interface(
    visualize,
    gr.Dropdown(list(train.index.unique().values)[:10]),
    ["html"],
    # gr.HighlightedText(
    #     label="effectiveness",
    #     combine_adjacent=False,
    # ).style(color_map={"+": "red", "-": "green"}),

    # examples=['The quick brown fox jumped over the lazy dogs.'],
)

# feedback-prize-english-language-learningのデモ
learning=gr.Interface(
    visualize,
    gr.Dropdown(list(train.index.unique().values)[:10]),
    ["html"],
) 


demo = gr.TabbedInterface([element, effectiveness], ["element", "effectiveness"])

if __name__ == "__main__":
    demo.launch(server_port=10010)
    demo.close()
