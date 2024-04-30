# ChangeBatchName
A small project that aims to make a python script to change files names in batch. It works not by replacing or renaming but
by slicing files names. ex : a file in named "[asdasd] My file.mp4"

[ | 0
a | 1
s | 2
d | 3
] | 4
M | 5
y | 6
f | 7
i | 8
l | 9
e | 10
. | 11
m | 12
p | 13
4 | 14

we slice from 5 to 14
the result is renamed file of "My file.mp4"

let's say you've downloaded files from somewhere (Example Files.png). the files has prefix like my example "[asdasd]". my program will remove all of them by slicing the name.
firstly, my program will check if a file has correct extensions first, if the file has wrong extension it will exclude the file. and then it will take the first filtered file as an example to show character indexes to slice. After that, you choose starting point and ending slice.