# Entry 2
##### X/X/XX

[https://github.com/aidanc1266/apcsa-freedom-project/blob/main/blog/entry02.md?authuser=0](https://github.com/aidanc1266/apcsa-freedom-project/blob/main/blog/entry02.md?authuser=0) < == Blog Entry Example ( for #2 ) . 

Text ( subchunk = 16 [ blocks in height ] [ and that a subchunk is like to chunk as substrings are like to strings . ]) 

[https://m.youtube.com/watch?v=LglApzUJ3oI](https://m.youtube.com/watch?v=LglApzUJ3oI) < == Example Video I will use for presenting my knowledge of the subject manner of subchunks . 
####### -----------

### All the other ideas I had ( as planning towards my main tool and/or main project to be worked on ) [ Part 2 ] 

. . . 

**Before** recognizing "subchunk height" : 
```langauge 
world_generation_chunk = [] 
world_generation_chunk_height = int(input("What is your world chunk height ? ( Can only place the world chunk hieght limit by amount of subchunks sadly . )") # world_generation_chunk_height = ???
for i in range(world_generation_chunk_height):
    #
    exec(f('variable_name_{i} = []'))
    # 
    for i_0 in range ( 16 ) : # for i in range ( 16 ) : 
        # 
        exec(f('x{i_0}_y{i} = []')) 
        exec(f('variable_name_{i}.append(x{i_0}_y{i})')) # exec(f('variable_name_{i}.add(x{i_0}_y{i})')) # exec(f('variable_name_{}.add(x{i_0}_y{i})')) # world_generation_chunk.add(x{i_0}_y{i})
        # 
        if i_0 == 16 :
            #
            exec(f('world_generation_chunk.append(variable_name_{i})')) # exec(f('world_generation_chunk.add(variable_name_{i})')) # exec(f('world_generation_chunk.add(x{i_0}_y{i})'))
            #
        # 
        >
        # 
    # 
    >
    # exec(f('world_generation_chunk.add(variable_name_{i})')) # exec(f('world_generation_chunk.add(x{i_0}_y{i})')) # world_generation_chunk.add(x{i_0}_y{i}) 
    >
    # 
# 
``` 

**After** recognizing "subchunk height" : 
```language
world_generation_chunk = [] 
subchunk_height = 16
world_generation_chunk_height = int(input("What is your world chunk height ? " ) # world_generation_chunk_height = ???
world_generation_chunk_height *= subchunk_height
# world_generation_chunk_tuple = ()
for i in range(world_generation_chunk_height) :
    #
    exec(f('subchunk_{i} = []')) # exec(f('variable_name_{i} = []')) 
    # 
    for i_0 in range(subchunk_height):
        #
        exec(f('subchunk_{i}_layer_{i_0} = []')) 
        # 
        for i_1 in range ( 16 ) : # for i in range ( 16 ) : 
            # 
            >
            exec(f('x{i_1}_y{i_0} = []')) 
            exec(f('subchunk_{i}_layer_{i_0}.append(x{i_1}_y{i_0})')) # exec(f('variable_name_{i}.append(x{i_0}_y{i})')) # exec(f('subchunk_{}_layer_{}.add(x{i_1}_y{i_0})')) # world_generation_chunk.add(x{i_1}_y{i_0})
            if i_1 == 16 : # if i_0 == 16 :
                #
                exec(f('subchunk_{i}.append(subchunk_{i}_layer_{i_0})')) # exec(f('subchunk_{i}_layer_{i_0}.append()')) # exec(f('world_generation_chunk.append(variable_name_{i})')) 
                #
            # 
            >
            # 
        # 
        >
        # world_generation_chunk.add(x{i_0}_y{i}) 
        >
        # 
    # 
    >
    exec(f('world_generation_chunk.append(subchunk_{i})')) 
    >
    # 
# 

""" 
#
tuple_string = '(' # tuple_string '('
#
for i in range(world_generation_chunk.length()): # for i in range(world_generation_chunk.length()): # for i in range(world_generation_chunk.length): # for i in range(world_generation_chunk_height):
    #
    tuple_string += f('{world_generation_chunk[0]}, ') # f('{world_generation_chunk[0]}, ') # f('world_generation_chunk[0]') # 'world_generation_chunk[0]'
    # 
    if i == world_generation_chunk.length() :
        #
        tuple_string -= ', '
        # 
    # 
    world_generation_chunk.pop(0) # world_generation_chunk.remove(0) 
    #
#
tuple_string += ')'
exec(tuple_string)) # exec(f('tuple_string')) 
""" 
exec(f(‘world_generation_chunk_tuple = ({(", ").join( ( world_generation_chunk.copy() ) )})‘))
#
for i in range(world_generation_chunk.length()): # Same for loop used anyay to clear elements to the list . 
    #
    world_generation_chunk.pop(0)
    #
#
``` 

### Section 

. . . 

[Previous](entry01.md) | [Next](entry03.md)

[Home](../README.md)
