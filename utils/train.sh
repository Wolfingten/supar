#!/bin/sh

export WANDB_API_KEY="$(cat /nethome/jguertler/.secrets/wandb.key)"
export WANDB_PROJECT="supar"
export WANDB_NAME="ger"

python -u -m supar.cmds.const.crf train -b -d 0 -c con-crf-roberta-en -p model  \
    --train /data/users/jguertler/datasets/spmrl/GERMAN_SPMRL/gold/ptb/train/train_trees_with_punct.txt \
    --dev /data/users/jguertler/datasets/spmrl/GERMAN_SPMRL/gold/ptb/dev/valid_trees_with_punct.txt \
    --test /data/users/jguertler/datasets/spmrl/GERMAN_SPMRL/gold/ptb/test/test_trees_with_punct.txt  \
    --encoder=bert  \
    --bert=xlm-roberta-large  \
    --lr=5e-5  \
    --lr-rate=20  \
    --epochs=10  \
    --update-steps=4 \
    --wandb
