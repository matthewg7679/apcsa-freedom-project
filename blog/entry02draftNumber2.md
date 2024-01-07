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
world_generation_chunk_height = ???
for i in range(world_generation_chunk_height):
    #
    exec(f('variable_name_{i} = []'))
    # 
    for i_0 in range ( 16 ) : # for i in range ( 16 ) : 
        # 
        >
        exec(f('x{i_0}_y{i} = []')) 
        exec(f('variable_name_{i}.add(x{i_0}_y{i})')) # exec(f('variable_name_{}.add(x{i_0}_y{i})')) # world_generation_chunk.add(x{i_0}_y{i})
        >
        # 
    # 
    >
    # exec(f('world_generation_chunk.add(x{i_0}_y{i})')) # world_generation_chunk.add(x{i_0}_y{i}) 
    >
    # 
# 
``` 

**After** recognizing "subchunk height" : 
```language
world_generation_chunk = [] 
subchunk_height = 16
world_generation_chunk_height = ???
for i in range(world_generation_chunk_height) : 
    for i_0 in range(subchunk_height):
        # 
        for i_1 in range ( 16 ) : # for i in range ( 16 ) : 
            # 
            >
            exec(f('x{i_1}_y{i_0} = []')) 
            # exec(f('subchunk_{}_layer_{}.add(x{i_1}_y{i_0})')) # world_generation_chunk.add(x{i_1}_y{i_0})
            >
            # 
        # 
        >
        # world_generation_chunk.add(x{i_0}_y{i}) 
        >
        # 
    # 
    >
    .
    >
    # 
# 
``` 

### Section 

. . . 

[Previous](entry01.md) | [Next](entry03.md)

[Home](../README.md)
