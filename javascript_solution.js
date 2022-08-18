/* Hundred letters problem.
Javascript version.

Given a string, return the first 100 characters and full words.
If a word would get cut off, do not include it and instead end at the last whole word.

Ex. "a picture is worth one hundred words"
For sake of brevity, say the space after "hundred" is character 97, and "words" is 98, 99, 100, 102, 103
Do not include "words" in this case, because it gets cut off at the 100 index. */

// Case 1: return the whole string.
case1 = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabca";

// Case 2: Return the first "word", easily spotted by the chars END.
case2 = "abcabcabcabcabcabcabcabcabcabcabcabcabcabEND       ThisPartShouldNotBeReturnedBecauseThisVeryLongWordGoesWayOver100";

// Case 3:The space after the word "algorithm" is character 99, so the word "works" would get cut off.
// This case should return up to the word "algorithm".
case3 = "I could be a passage from a story, blog, article or any other source. Make sure that the algorithm works correctly. This test case ends at the word algorithm";

// Case 4: Same as Case 3, but with more spaces.
case4 = "I could be a passage from a story, blog, article or any other source. Make sure that the algorithm                       works correctly. This test case should also end at the word algorithm.";

// Case 5: A string full of blank chars.
case5 = "                    ";

// Case 6: String of length 0.
case6 = "";


function hundredSolver(myString) {
    console.log(`\nDEBUG original string length: ${myString.length}`);
    
    if (myString.length <= 100) {
        return myString;
    };

    index = 99;
    while (index >= 0) {
        if (myString[index] === ' ' && myString[index - 1] !== ' ') {
            console.log(`\nDEBUG returned string length: ${myString.slice(0, index).length}`);
            return myString.slice(0, index);
        };
        index--;
    };
};


console.log(hundredSolver(case1));
console.log(hundredSolver(case2));
console.log(hundredSolver(case3));
console.log(hundredSolver(case4));
console.log(hundredSolver(case5));
console.log(hundredSolver(case6));

