#!/bin/sh

export WANDB_API_KEY="$(cat /nethome/jguertler/.secrets/wandb.key)"

python -u -m supar.cmds.const.crf train -b -d 0 -c con-crf-roberta-en -p model  \
    --train /data/users/jguertler/datasets/spmrl/GERMAN_SPMRL/gold/ptb/train/train.German.gold.ptb \
    --dev /data/users/jguertler/datasets/spmrl/GERMAN_SPMRL/gold/ptb/dev/dev.German.gold.ptb \
    --test /data/users/jguertler/datasets/spmrl/GERMAN_SPMRL/gold/ptb/test/test.German.gold.ptb  \
    --encoder=bert  \
    --bert=xlm-roberta-large  \
    --lr=5e-5  \
    --lr-rate=20  \
    --epochs=10  \
    --update-steps=4
