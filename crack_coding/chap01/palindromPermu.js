// Given a string, write a function to check if it is a prermutation of a palindrome

function palinPermu(string) {    
    let single_count = 0   
    let pair_count = 0
    string = string.toLowerCase()    
    let string_list = string.split("")    
    for (i=0; i<string_list.length; i++) {             
        let letter = string[i]        
        if (letter != " ") {
        const pair = string_list.filter((string_list)=>{            
            return string_list.indexOf(letter) != -1;
                            // -1 은 그 값이 없을 때 출력되는 값이다. 그러므로 그 값이 있다면 리턴하라의 뜻과 같다.                            
            })        
        if (pair.length == 1) {
            single_count += 1            
        }else if (pair.length == 2) {
            pair_count +=1
        }
        }
    }
    console.log("Pair Count: " + pair_count)
    console.log("Sing String Count: " + single_count)
    if (single_count > 1) {
        return console.log(false)
    }else{
        return console.log(true)
    }
}
palinPermu("Tact Coa")
palinPermu("TactCoa")
palinPermu("TactCoa1")
