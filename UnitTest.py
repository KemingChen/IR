from textblob import TextBlob as tb
from textblob import Word
a = "zgreement"
b = tb(a)
print tb("affectedareas").correct().words
print tb("zgreement").correct()
print tb("attitude..and").correct()
# print Word("arapaho.nsuok.edu/~uawc").spellcheck()
# print Word("alzheimersreadingroom.blogspot.com").spellcheck()
