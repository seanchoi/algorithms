
// There are three types of edits that can be performed on strings: insert, remove, replace
// Given two strings, write a function to check if they are one edit(or zero edits) away
function oneWay(a, b) {
    let check = 0
    let editable = ""
    let replace_spell
    a_arr = a.split("")
    b_arr = b.split("")
    for (i=0; i<a_arr.length; i++) {        
        const check_spell = b_arr.includes(a_arr[i])                
        if(check_spell == false) {
            check += 1
            if (check < 2) {
                editable = a_arr[i]
                if(a.length == b.length) {
                    replace_spell = b_arr[i]
                }                
            }
        }
    }
    if (check > 1) {
        return console.log(false)
    }else if (check == 1) {        
        if (a.length > b.length) {
            return console.log(`You can remove ${editable} from ${a} to make ${b}`)
        }else if (a.length == b.length){
            return console.log(`You can replace ${editable} with ${replace_spell} in ${a} to make ${b}`)
        }
        
    }else {
        return console.log(`You don't need to change anything! Both words are indentical`)
    }
}
oneWay('pale', 'ple')
oneWay('pake', 'pale')
oneWay('pale', 'bake')
oneWay('pale', 'pale')

