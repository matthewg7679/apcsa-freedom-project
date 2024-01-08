( Edit: the code is under the assumption that Minecraft’s world height limit is 320 blocks, I don’t know the true world height so imagine in your head that the 3D list will have the “2D list” section taking up multiple lines of code. The “2D list” actually will have the same amount of lines of code to produce the container for “`x#_y#`” as the amount of blocks meant for the true world height. ) 

—————————

All the 3D list will contain is a bunch of strings for each list item in the 3D list. Each string is meant to symbolize each block in the Minecraft clone. 

—————————

This Minecraft clone of mine, for copyright reasons, will be renamed to “MatthewCraft” and that all code of Minecraft will not be looked at throughout this Minecraft clone. 

Any code that is similar or the same to Minecraft’s code will be considered as a coincidence. 

—————————

Turns out, there is a reason as to why the variables making up the lists in the “2D list” section of the 3D list are labeled in the format “`x#_y#`”. 

When you want to get a string of the 3D list that represents a block of the Minecraft clone, you get a `return` value from the line of code being “`world_generation_chunk[y_coordinate][x_coordinate][z_coordinate]`”. 

This also conveniently helps figure out how pistons work already since the block being moved just `adds or subtracts 1` of `any x, y, or z` direction depending on where the piston faces, having the head towards the block, in terms of direction. 

For the piston? It is just as easy at to replace the string value of the item in the list location of the 3D list. 

( Also forgot to mention that the head of the piston needs to be where the moved block used to be, facing the direction towards the block. ) 

—————————

Just as a proof of concept, here is how the model code could potentially look like. 
```language
world_generation_chunk[y-1][x][z] = String(world_generation_chunk[y][x][z])

if (y incremented by 1) : 
 world_generation_chunk[y][x][z] = String(“piston_head_face_up”) 
elif (y decremented by 1) : 
 world_generation_chunk[y][x][z] = String(“piston_head_face_down”) 

// [ . . . ] ( assuming more if statements depending on increment or decrement of x or z direction, since these if statements only show about the y_coordinate variable ) 
```

—————————

Example strings that could be used in the code to represent the facing of piston head: 

1 ) `“piston_head_face_left_x”` or `“piston_head_face_x_left”` 

2 ) `“piston_head_face_right_x”` or `“piston_head_face_x_right”`

3 ) `“piston_head_face_left_z”` or `“piston_head_face_z_left”` 

4 ) `“piston_head_face_right_z”` or `“piston_head_face_z_right”` 

( Image these strings for the model code ) 

—————————

Example strings that could be used in the code to represent the facing of piston body: 

1 ) `“piston_body_face_left_x”` or `“piston_body_face_x_left”` 

2 ) `“piston_body_face_right_x”` or `“piston_body_face_x_right”`

3 ) `“piston_body_face_left_z”` or `“piston_body_face_z_left”` 

4 ) `“piston_body_face_right_z”` or `“piston_body_face_z_right”` 

5 ) `“piston_body_face_up”` 

6 ) `“piston_body_face_down”` 

( These strings are meant for the if conditions of the piston body that extends the head of the piston in the first place. ) 

—————————

Example strings that could be used in the code to represent the facing of piston itself without extension/extending : 

1 ) `“piston_face_left_x”` or `“piston_face_x_left”` 

2 ) `“piston_face_right_x”` or `“piston_face_x_right”`

3 ) `“piston_face_left_z”` or `“piston_face_z_left”` 

4 ) `“piston_face_right_z”` or `“piston_face_z_right”` 

5 ) `“piston_face_up”` 

6 ) `“piston_face_down”` 

( These strings are meant for the piston by itself without it being extended, and also used for future if statements involving the retraction of the piston. ) 

—————————

I will now explain the basic block of the world generation. Hope you understand baised on the string names. 

1 ) `“grass_block”` 

2 ) `“dirt_block”` 

3 ) `“stone_block”` 

4 ) `“bedrock”` or `“bedrock_block”` 

5 ) `“cobblestone”` or `“cobblestone_block”` 

6 ) `“oak_log”` ( first of many log types ) 

7 ) `“oak_leaves”` ( first of many leave types ) 

8 ) “crafting_table” ( used for crafting in 3x3 grid, similar code to 2x2 crafting grid in first model code ) 

9 ) `“furnace”` or `“furnace_block”` ( more complicated [2D list], but duable: the furnace able to smelt items ) 

`[ . . . ( etc. , etc. , and etc. ) ]` 

( These String values of certain blocks are meant to be like variable names to represent each block in the first place. ) 

—————————

I am fine if you think the string names need to be changed due to copyright, just let me know in this slack conversation by simply copying the text of the list of items you want to change to avoid copyright then simply paste and rename and finally send your new list back to me. 

—————————

And now another idea came to my head : 

The if conditions for each block will have each condition being ( block_name = /* String name */ ) . 

The code will goes as follows : 

```language
if ( other_blocks == true ) : 
 // code that sends straight to the other blocks not mentioned in prior string lists 
elif ( modified_added_blocks == true ) : 
 // code that leads to different txt file for inclusion of the modified added blocks ( or to put in other words, blocks that are created for the mod ) 
elif ( block_name == /* vanilla MatthewCraft block */ ) : 
 // code relating to placing the block and the block’s properties down 
```
( every `elif` after this goes with all blocks mentioned before; please imagine this model code as well being a txt file, you will see why in a bit ) 

—————————

The code for the massive “`if elif`” statement will be in “`.txt`” format since I want the code to be a string just in case I want to add more blocks to my valina clone of Minecraft. 

The same will go for modded blocks since the mid creator can just insert code using their txt files of their code to put into my code. 

# Drafts 
