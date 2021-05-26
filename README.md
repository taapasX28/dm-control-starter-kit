### Installing dm_control and tonic_rl

#### dm_control

Most of the installation procedure for `dm_control` is listed in the official repository [here](https://github.com/deepmind/dm_control). However some key points to take care of are:

1. Extract Mujoco pro in `~/.mujoco/` directory. The key `mjkey.txt` you with get for Mujoco Pro 2.0 needs to be placed in the `bin` directory to run Mujoco independently. A sanity check that Mujoco is installed correctly can be done by `./simulate ../model/humanoid.xml` command (Linux and MacOS) by going into the `bin` directory. However `dm_control` requires the key in the `.mujoco` directory so place it there too.

2.  `dm_control` can then be installed by `pip` as stated in the repository or by cloning the repository and installing that by `pip intall -e.`

3.  For rendering although the dependencies listed for linux are ` libglfw3 libglew2.0` these might not work in that case use `sudo apt-get install libglfw-dev libglew-dev`. These substitute dependencies work out.

4. To test out `dm_control` try running the code `testdm.py`. If everything is installed correctly it will print out the reward, discount and observation of an episode for a simple cartpole task. Unlike gym after a step these three things are returned as a timestep object form which they can be accessed. 

   

#### tonic_rl

For training tasks in dm_control I recommend the tonic RL library that can be found [here](https://github.com/fabiopardo/tonic). The installation is pretty straight forward. The library provides with 2 variants of RL algorithms in `Pytorch` as well as `tensorflow` so it can be modified easily for research. Regarding how to train go to training folder of the repository.



* ###### For how to train a control suite environment go to `.\train\` and for making a custom environment refer to `.\create_env\`
