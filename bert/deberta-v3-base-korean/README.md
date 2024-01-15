---
license: apache-2.0
language:
- ko
tags:
- deberta-v3
---
# deberta-v3-base-korean

## Model Details

DeBERTa는 Disentangled Attention과 Enhanced Masked Language Model을 통해 BERT의 성능을 향상시킨 모델입니다.
그중 DeBERTa V3은 ELECTRA-Style Pre-Training에 Gradient-Disentangled Embedding Sharing을 적용사여 DeBERTA를 개선했습니다.

이 연구는 구글의 TPU Research Cloud(TRC)를 통해 지원받은 Cloud TPU로 학습되었습니다.

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, DebertaV2ForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("team-lucid/deberta-v3-base-korean")
model = DebertaV2ForSequenceClassification.from_pretrained("team-lucid/deberta-v3-base-korean")

inputs = tokenizer("안녕, 세상!", return_tensors="pt")
outputs = model(**inputs)
```

## Evaluation

|                    | Backbone<br/>Parameters(M) | **NSMC**<br/>(acc) | **PAWS**<br/>(acc) | **KorNLI**<br/>(acc) | **KorSTS**<br/>(spearman) | **Question Pair**<br/>(acc) |
|:-------------------|:--------------------------:|:------------------:|:------------------:|:--------------------:|:-------------------------:|:---------------------------:|
| DistilKoBERT       |            22M             |       88.41        |       62.55        |        70.55         |           73.21           |            92.48            |
| KoBERT             |            85M             |       89.63        |       80.65        |        79.00         |           79.64           |            93.93            |       
| XLM-Roberta-Base   |            85M             |       89.49        |       82.95        |        79.92         |           79.09           |            93.53            |     
| KcBERT-Base        |            85M             |       89.62        |       66.95        |        74.85         |           75.57           |            93.93            |      
| KcBERT-Large       |            302M            |       90.68        |       70.15        |        76.99         |           77.49           |            94.06            |   
| KoELECTRA-Small-v3 |            9.4M            |       89.36        |       77.45        |        78.60         |           80.79           |            94.85            |
| KoELECTRA-Base-v3  |            85M             |       90.63        |       84.45        |        82.24         |         **85.53**         |            95.25            |
| Ours               |                            |                    |                    |                      |                           |                             |
| DeBERTa-xsmall     |            22M             |       91.21        |       84.40        |        82.13         |           83.90           |            95.38            |
| DeBERTa-small      |            43M             |     **91.34**      |       83.90        |        81.61         |           82.97           |            94.98            |
| DeBERTa-base       |            86M             |       91.22        |      **85.5**      |      **82.81**       |           84.46           |          **95.77**          |

\* 다른 모델의 결과는 [KcBERT-Finetune](https://github.com/Beomi/KcBERT-Finetune)
과 [KoELECTRA](https://github.com/monologg/KoELECTRA)를 참고했으며, Hyperparameter 역시 다른 모델과 유사하게 설정습니다.

## Model Memory Requirements

| dtype            | Largest Layer or Residual Group   | Total Size   | Training using Adam   |
|:-----------------|:----------------------------------|:-------------|:----------------------|
| float32          | 187.79 MB                         | 513.77 MB    | 2.01 GB               |
| float16/bfloat16 | 93.9 MB                           | 256.88 MB    | 1.0 GB                |
| int8             | 46.95 MB                          | 128.44 MB    | 513.77 MB             |
| int4             | 23.47 MB                          | 64.22 MB     | 256.88 MB             |
