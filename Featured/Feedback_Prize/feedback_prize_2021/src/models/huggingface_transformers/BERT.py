import transformers


class transformers_BERT():

    def __init__(self,device='cpu',pretrained_path='bert-base-uncased'):

        self.tokenizer=transformers.BertTokenizer.from_pretrained(pretrained_path)

        self.model = transformers.BertForSequenceClassification.from_pretrained(pretrained_path,num_labels=7)

        self.model.to(device)


class transformers_RoBERTa():

    def __init__(self,device='cpu',pretrained_path='roberta-base'):

        self.tokenizer=transformers.RobertaTokenizer.from_pretrained(pretrained_path)

        self.model = transformers.RobertaForSequenceClassification.from_pretrained(pretrained_path,num_labels=7)

        self.model.to(device)


class transformers_DeBERTa():

    def __init__(self,device='cpu',pretrained_path='microsoft/deberta-base'):

        self.tokenizer=transformers.DebertaTokenizer.from_pretrained(pretrained_path)

        self.model = transformers.DebertaForSequenceClassification.from_pretrained(pretrained_path,num_labels=7)

        self.model.to(device)

