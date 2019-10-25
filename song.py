lyrics = ('Ambassador go dey chop And Governor go dey chop And President go dey chop When dem say make we jump, we go jump Ambassador go dey chop And  President go dey chop And Governor go dey chop When dey say make we jump, we go jump No be for here wey dem born Jesus ehee My country problem e pass Jesus Because na we be our own problem ehee Na who go come reason well? well, well, well Ambassador go dey chop dey there ooo And Governor go dey chop dey nd President go dey chop dey there ooo there ooo When dey say make we jump, we go jump dey there ooo Some people go somersault dey there ooo Dem get headache we go drink Panadol dey there ooo Meanwhile president go dey chop dey there ooo')
list_of_lyrics = lyrics.split(' ')
print(list_of_lyrics)
print(len(list_of_lyrics))
unique_words= set(list_of_lyrics)
print(unique_words)
print(len(unique_words))
word_histogram = dict.fromkeys(unique_words, 0)
for word in list_of_lyrics:
    word_histogram[word] = word_histogram[word]+ 1
print(word_histogram['President'])
import plotly
from plotly.offline import iplot, init_notebook_mode
from plotly import tools
import plotly.graph_objs as go 
init_notebook_mode(connected=True)
trace={'type': 'bar', 'x':list(uniquewords), 'y': list(word_histogram.values())}
plotly,offline,iplot({'data':[trace]})