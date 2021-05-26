#!/bin/bash

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

python -m tonic.train \
--header 'import tonic.torch' \
--agent 'tonic.torch.agents.PPO()' \
--environment 'tonic.environments.ControlSuite("quadruped-walk")' \
--seed 0

# Plot and reload.
python -m tonic.plot --path quadruped-walk/ &
python -m tonic.play --path quadruped-walk/PPO/0 &
wait