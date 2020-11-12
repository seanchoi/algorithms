// Given two string, write a method to decide if one is permutation of the other
function checkPermu(strA,strB) {
    if (strA.length == strB.length) {
        var check = 0
        for (i = 0; i<strA.length; i++) {
            let letter = strA[i]
            for ( let j = 0; j<strB.length;j++){
                if (letter == strB[j] ){
                    check += 1                    
                }
            }        
        }        
        if (check == strA.length) {
            return console.log(`${strA} and ${strB}, These strings are permutated`)
        } else {
            return console.log(`${strA} and ${strB}, The words are unique from each other!`)    
        }
    }else{
        return console.log(`${strA} and ${strB},The words are unique from each other!`)
    }
    
}

checkPermu("ABCD", "BADCF")
checkPermu("ABCD", "BADC")