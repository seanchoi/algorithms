function check_palindrome(word) {
    for(let i=0; i< Math.round(word.length/2); i++){
        if (word[i] !== word[word.length-1-i]){
            return false
        }
    }
    return true
}

function find_palindrome(word) {
    if(check_palindrome(word)) {
        console.log("Finally have my palindrome!")
        return word
    } 
    else { 
        if (check_palindrome(word.substring(1))) {
            console.log(word +" is not a palindrome!")
            return find_palindrome(word.substring(1))            
        }
        else if (check_palindrome(word.slice(0 ,-1))) {
            return find_palindrome(word.slice(0, -1))
        }
    }    
    }
console.log(find_palindrome("racecar1"))