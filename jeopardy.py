import pandas as pd
pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('jeopardy.csv')
#print(df.info())
##Remove extra whitespace from column names
df.columns = df.columns.str.strip()
#print(df.info())

"""
Function to filter questions in the dataset for words in a list.
Returns the rows with the questions that contain all the words from the list.
"""
def Q_KeyWords(data, words):
    #Lowercase all the words in the words list and in the questions. 
    #Returns True if all of the words in the list are in the question.
    filter = lambda x: all(word.lower() in x.lower() for word in words)
    #Apply the filter to the Question column and returns the rows 
    #where the function returned True
    return data.loc[data['Question'].apply(filter)]
    
king_england_questions = Q_KeyWords(df, ['King', 'England'])
#print(king_england_questions['Question'])

author_death_questions = Q_KeyWords(df, ['author', 'death'])
# print(author_death_questions['Question'])
# print(len(author_death_questions))


"""
Add a new column in which the items in the Value column to floats so they can 
be used for statistical calculations.
"""
df['float value'] = df.Value.apply(lambda x: float(x[1:].replace(',','') if x != 'None' else 0))

## Calculate the average value of questions containing the word 'King'
king_questions = Q_KeyWords(df, ['King'])
#print(king_questions['float value'].mean())


"""
Function to determine the unique answers and their counts for questions 
containing key words.
"""
def uniqueAnswers(data, words):
    questions = Q_KeyWords(data, words)
    return questions.Answer.value_counts().reset_index()

unique_answers_king = uniqueAnswers(df, ['King'])
#print(unique_answers_king)


"""
Determining how many times key words appeared in a question by year.
"""
df['Air Date'].convert_dtypes(convert_string=True)
df['Year'] = df['Air Date'].apply(lambda x: x[:4]) 
computer_questions = Q_KeyWords(df, ['Computer'])
computer_year = computer_questions.Year.value_counts()