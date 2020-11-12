function Urlify(string) {
    var new_string = []
    console.log(string)
    console.log(string.length)    
    for (let i=0; i<string.length; i++){        
        if(string[i] == " ") {                        
            new_string += "%20"            
        }else {
            new_string += string[i]            
        }
        
    }
    return console.log(new_string)
}

Urlify("My Name Is Sean!")