#!/bin/bash

python3 -u launch_experiment.py \
--algo gpi_pd_continuous \
--env-id MOHopperDR-v5 \
--seed 5 \
--num-timesteps 3000000 \
--gamma 0.99 \
--wandb-group 'domain_randomization' \
--ref-point '-100.0' '-100.0' '-100.0' \
--test-generalization True \
--init-hyperparams per:True gradient_updates:1 batch_size:256 learning_starts:25000 dynamics_train_freq:2000 dynamics_rollout_freq:2000 dynamics_real_ratio:0.5 buffer_size:1000000  "net_arch:[256, 256, 256, 256]" \
--train-hyperparams timesteps_per_iter:25000 eval_mo_freq:100000  \
--generalization-hyperparams num_eval_weights:100 num_eval_episodes:1 "generalization_algo:'dr_state_action_history'" history_len:2 \
--test-envs "MOHopperDefault-v5,MOHopperLight-v5,MOHopperHeavy-v5,MOHopperSlippery-v5,MOHopperLowDamping-v5,MOHopperHard-v5" \
# --record-video True \
# --record_video_w_freq:203 \