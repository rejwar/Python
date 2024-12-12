def checkVowel(n):
    match n :
        case 'a' : return "Vowel Alphabate"
        case 'e' : return "Vowel Alabate"
        case 'i' : return "Vowel Alabate"
        case 'o' : return "Vowel Alabate"
        case 'u' : return "Vowel Alabate"
        case _: return "simple alphabate"
        
print(checkVowel('a'))
print(checkVowel('e'))
print(checkVowel('m'))
