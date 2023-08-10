# Advent of Code (AoC)
Testing my algorithmic skills using self taught Data Structures and Algorithms from MOOCs and online resources.

[AoC](https://adventofcode.com/) is a yearly set of coding problems solvable from Dec 1 to 25, with 1 problem released per day. I recently got interested in solving these types of problems and am documenting my progress here.

# Working inside docker

Make sure you have docker daemon via docker desktop available.

This command composes the environment whilst rebuilding the image to account for any changes.

```
docker compose up --build
```

Afterwards, open the container using VScode Dev Containers. By default, the app directory will be `/root`. Change it by accessing the container configuration file. Refer to this (forum)[https://stackoverflow.com/questions/63962060/visual-studio-code-remote-containers-change-default-root-directory]

This will set the default folder to `/src`, which references `/src` in our local setup (this is specified in the Dockerfile).

Development is now streamlined using Dev Containers, which is a clean, base environment to work with.