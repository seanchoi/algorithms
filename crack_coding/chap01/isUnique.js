// Implement an alogirithm to determine if a string has all unique characters.
// You should first ask your interviewer if the string is an ASCII or a Unicode string. 

function isUnique(string){
    console.log(string.length)
    for ( i=0; i<string.length-2; i++ ){
        console.log(i)
        console.log(string[string.length-1])
        letter = string[i]        
        for ( j=i+1; j<string.length;j++ ) {
            console.log(string[j])
            if (letter == string[j]) {
                
                return false
            }            
        }
    }
    return true
}

console.log(isUnique("abcdefghijklmnop"))

a = "abc"
console.log(a.length)
console.log(a[a.length-1])