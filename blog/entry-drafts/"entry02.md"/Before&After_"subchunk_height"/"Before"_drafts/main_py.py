#Enter Python code here and hit the Run button.world_generation_chunk = [] 
subchunk_height = 16
world_generation_chunk_height = 10892 
for i in range(world_generation_chunk_height):
    #
    exec(f('subchunk_{i} = []')) 
    # 
    for i_0 in range(subchunk_height):
        #
        exec(f('subchunk_{i}_layer_{i_0} = []')) 
        # 
        for i_1 in range ( 16 ): 
            #  
            exec(f('x{i_1}_y{i_0} = []')) 
            exec(f('subchunk_{i}_layer_{i_0}.append(x{i_1}_y{i_0})')) 
            if i_1 == 16 : 
                # 
                exec(f('subchunk_{i}.append(subchunk_{i}_layer_{i_0})')) 
                # 
            # 
            
            # 
        # 
        
        # world_generation_chunk.add(x{i_0}_y{i}) 
        
        # 
    # 
    exec(f('world_generation_chunk.append(subchunk_{i})')) 
    # 
# 

exec(f(‘world_generation_chunk_tuple = ({(", ").join( ( world_generation_chunk.copy() ) )})‘))
#
for i in range(world_generation_chunk.length()): 
    #
    world_generation_chunk.pop(0)
    #
#

print(world_generation_chunk_tuple)
print(world_generation_chunk)
