python3 \
    ./train.py \
    --dataset-config local_training_example.json \
    --model-config ckpts/model_config.json \
    --name output-train \
    --seed 128 \
    --save-dir checkpoints \
    --checkpoint-every 1000 \
    --batch-size 128 \
    --num-workers 12 \
    --pretrained-ckpt-path ckpts/model.ckpt \
    --precision 16
