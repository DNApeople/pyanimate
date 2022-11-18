import time
import os 
os.system("cls")


frames = [
"""    .                                                                                          
    .                                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    .                                            ~~|~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~|~~|~~~~~~ 
    .                                              _TT TT_          ^$^$^$^$^       ====       
    .                                             /  ***  \        |$^$^$^$^$|      [##]       
    .                                            /_|+++++|_\       |^$^$^$^$^|      [##]__     
    .                                              |-----|         |$^$^$^$^$|      (_!_!_)    
    .                                              |_____|         |_$_$_$_$_|                  """,
"""    .                                                                                          
    .                                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    .                                            ~|~~~~~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~|~
    .                                            ==         _TT TT_          ^$^$^$^$^       ==
    .                                            #]        /  ***  \        |$^$^$^$^$|      [#
    .                                            #]__     /_|+++++|_\       |^$^$^$^$^|      [#
    .                                            !_!_)      |-----|         |$^$^$^$^$|      (_
    .                                                       |_____|         |_$_$_$_$_|         """,
"""    .                                                                                          
    .                                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    .                                            |~~~~~~|~~|~~~~~~~~~|~~~~~|~~~~~~~~~|~~~~~~~~~
    .                                                   ====         _TT TT_          ^$^$^$^$^
    .                                            |      [##]        /  ***  \        |$^$^$^$^$
    .                                            |      [##]__     /_|+++++|_\       |^$^$^$^$^
    .                                            |      (_!_!_)      |-----|         |$^$^$^$^$
    .                                            |                   |_____|         |_$_$_$_$_ """,
"""    .                                                                                          
    .                                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    .                                            ~~~~~~~~~~|~~~~~~|~~|~~~~~~~~~|~~~~~|~~~~~~~~|
    .                                             ^$^$^$^$^       ====         _TT TT_         
    .                                             $^$^$^$^$|      [##]        /  ***  \       |
    .                                             ^$^$^$^$^|      [##]__     /_|+++++|_\      |
    .                                             $^$^$^$^$|      (_!_!_)      |-----|        |
    .                                             _$_$_$_$_|                   |_____|        | """,
"""    .                                                                                          
    .                                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    .                                            ~~~~~~~~~|~~~~~~~~~|~~~~~~|~~|~~~~~~~~~|~~~~~|
    .                                                      ^$^$^$^$^       ====         _TT TT_
    .                                                     |$^$^$^$^$|      [##]        /  ***  
    .                                                     |^$^$^$^$^|      [##]__     /_|+++++|
    .                                                     |$^$^$^$^$|      (_!_!_)      |-----|
    .                                                     |_$_$_$_$_|                   |_____| """,
"""    .                                                                                          
    .                                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    .                                            ~|~~~~~|~~~~~~~~~|~~~~~~~~~|~~~~~~|~~|~~~~~~~~
    .                                             _TT TT_          ^$^$^$^$^       ====        
    .                                            /  ***  \        |$^$^$^$^$|      [##]        
    .                                            _|+++++|_\       |^$^$^$^$^|      [##]__     /
    .                                             |-----|         |$^$^$^$^$|      (_!_!_)     
    .                                             |_____|         |_$_$_$_$_|                   """
]

nlines = 8
# scroll up to make room for output
print(f"\033[{nlines}S", end="")

# move cursor back up
print(f"\033[{nlines}A", end="")

# save current cursor position
print("\033[s", end="")
while True:
    for t in range(6):
    # restore saved cursor position
      print("\033[u", end="")
      print(frames[0 + t])
    
      t += 1
      time.sleep(.1)