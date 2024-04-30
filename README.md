# Warning The Code Only Been Tested in Windows ONLY
## There is no history system YET, so what has been done is not reversible

### ChangeBatchName
A small project that aims to make a python script to change files names in batch. It works not by replacing or renaming but
by slicing files names. ex : a file in named "[asdasd] My file.mp4"

0. [ | 0
1. a | 1
2. s | 2
3. d | 3
4. ] | 4
5. M | 5
6. y | 6
7. f | 7
8. i | 8
9. l | 9
10. e | 10
11. . | 11
12. m | 12
13. p | 13
14. 4 | 14

we slice from 5 to 14
the result is renamed file of "My file.mp4"

let's say you've downloaded files from somewhere (Example Files.png). the files has prefix like my example "[asdasd]". my program will remove all of them by slicing the name.
firstly, my program will check if a file has correct extensions first, if the file has wrong extension it will exclude the file. and then it will take the first filtered file as an example to show character indexes to slice. After that, you choose starting point and ending slice.