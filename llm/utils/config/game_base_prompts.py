

game_base_prompts = {
    'order_sentence' : "given the following words: الأب, الكتاب, بصمت, قرأ. Make a sentence formed out of those words. Return the sentence only in a JSON format with the key:setence, and with no extra addition.", 
    'order_chars': "Given the following set of characters: ت, ق, ل, ب, م, س, ر, ه, ش return the set of words that can be formed out of those characters, you cannot use one character twice, and you shall return the words in a JSON format only with no addition.", 
	"match_words_with_syns": "given the following set of words: نجح, الوفي, تنظيم, تهوى. find a synonym and an opposite of each word and return your answer in JSON format. Provide the JSON only with no extra information"
    
}