[ link https://ctxt.io/2/AADQurxNEw ](https://ctxt.io/2/AADQurxNEw) 
```language
// Approach 1:
String first = words.get(0);
for(int i=0; i<words.size()-1; i++) {
  words.set(i,words.get(i+1));
}
words.set(words.size()-1, first);

// Approach 2:
for(int i = 1; i < words.size(); i++){
  words.add(i-1,words.remove(i));
}

// Approach 3: 
String word = words.remove(0);
words.add(words.size(),word);

// Approach 4:
words.add(words.remove(0));
``` 
