[ link ](https://ctxt.io/2/AAAwJZQQFg) 
```language
  public static void shiftLeft(ArrayList<String> arr){
    String temp = arr.get(0);
    for (int i = 0; i < arr.size()-1; i++){
      arr.set(i, arr.get(i+1));
    }
    arr.set(arr.size()-1, temp);
  }
``` 
