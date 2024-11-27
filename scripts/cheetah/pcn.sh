#!/bin/bash

python3 -u launch_experiment.py \
--algo pcn \
--env-id MOHalfCheetahDR-v5 \
--seed 5 \
--num-timesteps 5000000 \
--gamma 0.99 \
--wandb-group 'domain_randomization' \
--ref-point '-100.0' '-500.0' \
--test-generalization True \
--init-hyperparams "learning_rate:0.0003" "scaling_factor:[0.1, 0.1, 0.1]" "max_return:[12300, 0]" "noise:0.2" "net_arch:[256, 256, 256, 256]" \
--train-hyperparams eval_mo_freq:100000 max_buffer_size:10000 num_er_episodes:1000 \
--generalization-hyperparams num_eval_weights:100 num_eval_episodes:1 record_video_w_freq:225 \
--test-envs "MOHalfCheetahDefault-v5,MOHalfCheetahLight-v5,MOHalfCheetahHeavy-v5,MOHalfCheetahSlippery-v5,MOHalfCheetahHard-v5" \
# --record-video True \