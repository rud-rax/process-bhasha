
# Stemming

![Stemming](..\media\stemming-1.jpg)

Stemming is a text processing technique used in natural language processing (NLP) to reduce words to their base or root form, called the stem. The purpose of stemming is to normalize words so that variations of the same word are treated as the same word. For example, "running," "runs," and "ran" all share the same root, "run," and should be treated as such for many NLP tasks.

### Why Stemming?

1. **Normalization**: Stemming helps in normalizing text by reducing different forms of words to a common base form. This simplifies text analysis and improves the accuracy of tasks like text classification, information retrieval, and sentiment analysis.
  
2. **Reduced Vocabulary**: By reducing words to their stems, the vocabulary size decreases, which can improve the efficiency of algorithms and reduce the computational resources required for processing text.

3. **Improved Matching**: Stemming enables better matching of words in search queries or information retrieval systems. Users searching for "run" would also find documents containing "running" or "runs" if stemming is applied.

### How Stemming Works:

1. **Tokenization**: The text is first divided into individual words or tokens. This step is crucial as stemming operates on individual words.

2. **Stemming Algorithm**: Stemming algorithms apply a set of rules to modify words and reduce them to their root or stem. These rules are typically based on linguistic principles and aim to remove common suffixes and prefixes. Stemming algorithms vary in complexity and efficiency, with some being rule-based and others statistical or machine learning-based.

3. **Example of Stemming**:

    ![Example of Stemming](..\media\stemming-2.jpg)

   - Original word: "running"
   - Stem: "run"
   - Original word: "cats"
   - Stem: "cat"
   - Original word: "better"
   - Stem: "better" (in some stemming algorithms, words may not change if they don't have recognizable suffixes or prefixes)



4. **Limitations of Stemming**:
   - Stemming algorithms do not always produce perfect results. They may generate stems that are not actual words or may produce stems that are different from the intended meaning. For example, "universe" might stem to "univers" instead of "universe."
   - Stemming algorithms are language-dependent, and different languages may require different stemming approaches.
   - Contextual information is often lost during stemming. Words with multiple meanings or ambiguous usage may be stemmed differently based on context.

### Popular Stemming Algorithms:

1. **Porter Stemming Algorithm**: One of the oldest and widely used stemming algorithms, developed by Martin Porter. It applies a series of rules to remove suffixes from words.
   
2. **Snowball Stemming Algorithm**: An extension of the Porter algorithm, also developed by Martin Porter. Snowball provides more flexibility and supports stemming in multiple languages.

3. **Lancaster Stemming Algorithm**: Another popular stemming algorithm that is more aggressive than Porter stemming, developed by Chris Paice.

Stemming is an essential preprocessing step in many NLP applications and is often followed by other techniques such as lemmatization and stop word removal to further enhance the text processing pipeline.

---

## Porter Stemming

The Porter stemming algorithm, developed by Martin Porter in 1980, is a widely used algorithm for stemming in natural language processing. It aims to reduce words to their base or root form by removing suffixes according to a set of predefined rules. While it may not always produce perfect results, it is fast and relatively simple to implement. Below are the general steps of the Porter stemming algorithm:

1. **Tokenization**: Split the text into individual words (tokens).

2. **Define the Five Phases**: The Porter algorithm consists of five phases, each aimed at removing specific suffixes from the word. These phases are applied sequentially.

   a. **Phase 1**: 
      - Apply a series of rules to remove common suffixes. For example:
        - Replace "sses" with "ss".
        - Replace "ies" with "i" if the preceding character is not a vowel.
        - Remove "ss", "s" or "us" if the word ends with "sses", "ss" or "us".

   b. **Phase 2**:
      - Apply additional rules to remove other suffixes. For example:
        - Replace "ational" with "ate".
        - Replace "tional" with "tion".
        - Replace "izer", "ization", "ational", and others with their base form.

   c. **Phase 3**:
      - Similar to Phase 2, this phase targets additional suffixes for removal.
        - Replace "ational" with "ate".
        - Replace "tional" with "tion".
        - Replace "alize" with "al".
        - Replace "ative" with "" (remove).

   d. **Phase 4**:
      - Handle special cases and remove specific suffixes.
        - Replace "ement" with "" (remove).
        - Replace "ment" with "" (remove).
        - Replace "sion" and "tion" with "t".

   e. **Phase 5**:
      - Apply final adjustments and remove endings.
        - Remove "e" if the preceding part has a measure greater than 1.
        - Remove "l" if the preceding part ends with "l".

3. **Stop if Convergence**: Repeat the five phases until no further changes can be made to the word.

4. **Output**: The resulting word after applying all applicable rules is considered the stemmed form of the original word.

It's important to note that the Porter stemming algorithm is rule-based and may not always produce the correct root form of a word, but it is efficient and widely used in many applications of natural language processing.


### Rules of Porter Stemming Algorithm
<details "hji">


The Porter stemming algorithm applies a series of rules to reduce words to their base or root form. These rules are organized into several phases, and each phase targets specific suffixes or endings to be removed from words. Here are the general rules used in the Porter stemming algorithm:

### Phase 1:

1. **SSES -> SS**: Replace "sses" at the end of a word with "ss".
2. **IES -> I**: Replace "ies" at the end of a word with "i" if the preceding letter is not a vowel.
3. **SS -> SS**: No change for words ending in "ss".
4. **S ->**: Remove "s" at the end of a word if the preceding word contains a vowel not immediately before the "s".
5. **US ->**: Remove "us" at the end of a word.

### Phase 2:

1. **TIONAL -> TION**: Replace "tional" at the end of a word with "tion".
2. **ATIONAL -> ATE**: Replace "ational" at the end of a word with "ate".
3. **IZATIONAL -> IZE**: Replace "izational" at the end of a word with "ize".
4. **ENTIAL -> ENT**: Replace "ential" at the end of a word with "ent".
5. **OUSLI -> OUS**: Replace "ousli" at the end of a word with "ous".
6. **IZATION -> IZE**: Replace "ization" at the end of a word with "ize".
7. **ATION -> ATE**: Replace "ation" at the end of a word with "ate".
8. **ALISM -> AL**: Replace "alism" at the end of a word with "al".
9. **IVITI -> IVE**: Replace "iviti" at the end of a word with "ive".
10. **BILITY -> BLE**: Replace "bility" at the end of a word with "ble".
11. **FULNESS -> FUL**: Replace "fulness" at the end of a word with "ful".
12. **OUSNESS -> OUS**: Replace "ousness" at the end of a word with "ous".

### Phase 3:

1. **ICATE -> IC**: Replace "icate" at the end of a word with "ic".
2. **ATIVE ->**: Remove "ative" at the end of a word.
3. **ALIZE -> AL**: Replace "alize" at the end of a word with "al".
4. **ICITI -> IC**: Replace "iciti" at the end of a word with "ic".
5. **ICAL -> IC**: Replace "ical" at the end of a word with "ic".
6. **FUL ->**: Remove "ful" at the end of a word.
7. **NESS ->**: Remove "ness" at the end of a word.

### Phase 4:

1. **AL ->**: Remove "al" at the end of a word.
2. **ANCE ->**: Remove "ance" at the end of a word.
3. **ENCE ->**: Remove "ence" at the end of a word.
4. **ER ->**: Remove "er" at the end of a word.
5. **IC ->**: Remove "ic" at the end of a word.
6. **ABLE ->**: Remove "able" at the end of a word.
7. **IBLE ->**: Remove "ible" at the end of a word.
8. **ANT ->**: Remove "ant" at the end of a word.
9. **EMENT ->**: Remove "ement" at the end of a word.
10. **MENT ->**: Remove "ment" at the end of a word.
11. **ENT ->**: Remove "ent" at the end of a word.
12. **ION -> (if preceding part contains a "S" or "T")**: Replace "ion" at the end of a word with nothing.

### Phase 5:

1. **E -> (if measure > 1)**: Remove "e" at the end of a word if the stem has a measure greater than 1.
2. **LL -> (if measure > 1)**: Remove "ll" at the end of a word if the stem ends with "ll" and has a measure greater than 1.

The "measure" mentioned in Phase 5 refers to the count of vowel-consonant sequences in the word. A sequence is defined as a string of consonants followed by a string of vowels, which is followed by a string of consonants.

</details>



---