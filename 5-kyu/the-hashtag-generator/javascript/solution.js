function generateHashtag (str) {
    if (!(str.length == 0) && str.trim() ){
        str = str.split(/[ ,]+/).filter(Boolean);
        let word;
        for (word in str) {
            //console.log(str[word]);
            if (str[word].length >= 140) {
                return false;
            }
            else {
                let arr = str.map((word) => {
                    return word[0].toUpperCase() + word.slice(1);
                  });
                return '#'+arr.join("");
            }
        }
    }
    else {
        return false;
    }

}