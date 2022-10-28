# -*- coding: utf-8 -*-
"""Feedback Prize デモ

gradio による Feedback Prize のデモ

"""

import gradio as gr

from demo_fn import element_demo, effectiveness_demo, learning_demo, train


# Feedback Prize 2021のデモ
element=gr.Interface(

    fn=element_demo,

    inputs=[
        gr.Radio(
            choices=['use data','write'],
            label='input_type'
        ),
        gr.Textbox(
            label="essay",
            lines=3,
            value="input_essay",
        ),
        gr.Dropdown(
            list(train.index.unique().values)[:100],
            label='essay_id'
        ),
        gr.Radio(
            choices=['none','groundtruth','prediction'],
            label='annotation_type'
        ),
        gr.Radio(
            choices=['BERT','RoBERTa','DeBERTa'],
            label='model_name'
        ),
    ],

    outputs=gr.HighlightedText(
        label="text element",
        combine_adjacent=False,
        elem_id="element_result",
    ).style(
        color_map={
            'Lead': '#8000ff',
            'Position': '#2b7ff6',
            'Evidence': '#2adddd',
            'Claim': '#80ffb4',
            'Concluding Statement': '#d4dd80',
            'Counterclaim': '#ff8042',
            'Rebuttal': '#ff0000'
        }
    ),

    # examples=[
    #     get_discourse(0),
    #     get_discourse(1),
    #     get_discourse(2),
    #     get_discourse(3),
    # ]
)


# feedback-prize-effectivenessのデモ
effectiveness=gr.Interface(
    fn=effectiveness_demo,
    inputs=[
        gr.Radio(
            choices=['use data','write'],
            label='input_type'
        ),
        gr.Textbox(
            label="essay",
            lines=3,
            value="input_essay",
        ),
        gr.Dropdown(
            list(train.index.unique().values)[:10],
            label='essay_id'
        ),
        gr.Radio(
            choices=['none','groundtruth','prediction'],
            label='annotation_type'
        ),
        gr.Radio(
            choices=['BERT','RoBERTa','DeBERTa'],
            label='model_name'
        ),
    ],
    outputs=[gr.Plot()],
    # gr.HighlightedText(
    #     label="effectiveness",
    #     combine_adjacent=False,
    # ).style(color_map={"+": "red", "-": "green"}),

    # examples=['The quick brown fox jumped over the lazy dogs.'],
)


# feedback-prize-english-language-learningのデモ
learning=gr.Interface(
    fn=learning_demo,
    inputs=[
        gr.Radio(
            choices=['use data','write'],
            label='input_type'
        ),
        gr.Textbox(
            label="essay",
            lines=3,
            value="input_essay",
        ),
        gr.Dropdown(
            list(train.index.unique().values)[:10],
            label='essay_id'
        ),
        gr.Radio(
            choices=['none','groundtruth','prediction'],
            label='annotation_type'
        ),
        gr.Radio(
            choices=['BERT','RoBERTa','DeBERTa'],
            label='model_name'
        ),
    ],
    outputs=["html"],
) 


demo = gr.TabbedInterface(
    [element, effectiveness, learning],
    ["element", "effectiveness", "learning"],
    # css="#element_result span {white-space: pre}"
)


if __name__ == "__main__":

    try:
        demo.launch(server_port=10010)
    except KeyboardInterrupt:
        demo.close()
    demo.close()