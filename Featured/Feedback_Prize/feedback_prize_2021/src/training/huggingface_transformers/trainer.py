# from torch.utils.data import DataLoader
# import warnings
import transformers
# import logging
import torch
import transformers

# if iskaggle:
#     !pip install --no-index --find-links ../input/huggingface-datasets datasets -q


from sklearn.metrics import log_loss


def score(preds): 
    return {
        'log loss': log_loss(
            preds.label_ids,
            torch.nn.functional.softmax(
                torch.Tensor(preds.predictions),
                dim=0
            )
        )
    }

def transformers_get_trainer(output_dir,model,tokenizer,data):

    args = transformers.TrainingArguments(
        output_dir,
        learning_rate=8e-6,
        warmup_ratio=0.1,
        lr_scheduler_type='cosine',
        #fp16=True,
        evaluation_strategy="epoch",
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8*2,
        num_train_epochs=10,
        weight_decay=0.01,
        report_to='none',

        logging_strategy='epoch',

        save_total_limit = 2,
        save_strategy = "epoch",
        load_best_model_at_end=True,
    )

    return transformers.Trainer(
        model,
        args,
        train_dataset=data['train'],
        eval_dataset=data['val'],
        tokenizer=tokenizer,
        compute_metrics=score,
    )