function pigIt(str){
    var l = [];
    str = str.split(" ");console.log(str);
    var i;
    for (i=0; i<str.length; i++) {
        if (!(/[^a-zA-Z0-9]/.test(str[i])) ){ 
            var pig = str[i].slice(1) + str[i][0] + "ay";console.log(pig);
            l.push(pig);
        }  
        else {
            l.push(str[i]);
        }
    }
    return l.join(" ");
}