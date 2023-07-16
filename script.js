//  TODO: find sring to vowale example : a , e , i, o, u

const vowel = ['a','e','i','o','u'];

let count = 0;

function findVowale(string){
    for (let index = 0; index < string.length; index++) {
        const element = string[index];
         for (let i = 0; i < vowel.length; i++) {
            const word = vowel[i];
            if(element === word){
                console.log(element);
                count += 1;
            }
         }
    }
}

findVowale('Bangladesh is small country')

console.log(count);