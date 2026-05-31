# Type script
Making JS logical and type safe with enforced type rules and data flow predictible out of mess of JS
Making errors easy to see through forgiving JS compilation.

let a:string = "String statement";
a = 10; <-- Made a specific to string cant assign into integer now as not into the js environment

Flow
writing ts files with specified types which compiles into js file and then we run the js file using node, initial errrors are fired while compiling with tsc commandline


## Basic Data types with type script
number -> store number, boolean -> bool , any -> store anything inside just to override the basics of type script

### Function definition with ts
    endless execution => Never keyword
    function greet():void{
        console ..
    }
Making void as the function return stuff if function doent returns anythig 
    
    NEED FOR THE GIVEN NEVER KEYWORD
    function add():never{
        enless logic flow
    }

## Array
string array
let array:string[] = '...' <-- Making array of string
tuples <-- storing for the tuple information

Making combination of such data types
let v:[string, number, boolean] = [...] <-- Making sure compiler know which variable to store into the given variable.

enum : WHAT IS enum and where to use this shit ? 

## making interface with ts
 

