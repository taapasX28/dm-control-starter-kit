import numpy as np
from dm_control import composer
from dm_control.composer.variation import distributions
from dm_control.locomotion.arenas import corridors as corr_arenas
from dm_control.locomotion.tasks import corridors as corr_tasks
from dm_control.locomotion.walkers import ant


walker = ant.Ant(
      observable_options={'egocentric_camera': dict(enabled=True)})

# Build a corridor-shaped arena that is obstructed by walls that are randomly spawned at the start of each episode.
arena = corr_arenas.WallsCorridor(
      wall_gap=4.,
      wall_width=distributions.Uniform(1, 7),
      wall_height=3.0,
      corridor_width=10,
      corridor_length=100,
      include_initial_padding=False)

  # Build a task that rewards the agent for running down the corridor at a
  # specific velocity.
task = corr_tasks.RunThroughCorridor(
      walker=walker,
      arena=arena,
      walker_spawn_position=(0.5, 0, 0),
      target_velocity=3.0,
      physics_timestep=0.005,
      control_timestep=0.03)

#compose the environment
env = composer.Environment(
    task=task,
    time_limit=10,
    random_state=np.random.RandomState(42),
    strip_singleton_obs_buffer_dim=True,
)


#registering it as an environment
from dm_control.utils import containers

SUITE = containers.TaggedTasks()
_DEFAULT_TIME_LIMIT = 20
@SUITE.add('benchmarking')
def my_task(time_limit=_DEFAULT_TIME_LIMIT, random=None, environment_kwargs=None):
    return env

# from dm_control import suite

# env = suite.load(domain_name="cartpole", task_name="swingup")

action_spec = env.action_spec()

# Step through the environment for one episode with random actions.
time_step = env.reset()
while not time_step.last():
  action = np.random.uniform(action_spec.minimum, action_spec.maximum,
                             size=action_spec.shape)
  time_step = env.step(action)
  print("reward = {}, discount = {}, observations = {}.".format(
      time_step.reward, time_step.discount, time_step.observation))

from dm_control import viewer

viewer.launch(environment_loader=env)

