#Road Rage

This is a Python program that is designed to simulate traffic given a set of
reasonable driver behaviors. The goal is to find the most optimal speed limit.

## To view the data or run

If you simply want to view the data, you can open the Ipython file in a read only
format straight from the Github repository. If you want to run the traffic_lib
python file. You will need Python installed and can then run the program from
the terminal by inputting python traffic_lib.py.

##Parameters and Results

Our drivers were very similar to human drivers in their behaviors. They all had
a 10% per second chance of slowing down by 2 m/s. Afterwards and in general, if
there was a space between their car and the next that was at least their speed
in m/s in meters in front of them, they would accelerate by 2 m/s.

The most optimal speed, tested over 1000 trials, was 72 k/h. At this limit, the
average speed was 69 k/h. As the highest speeds allowed got higher, there were
actually far more traffic jams and the average speed dropped significantly.
When the max speed was 90 k/h, the average speed was only 58 k/h.
