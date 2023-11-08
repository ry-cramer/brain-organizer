# %%
import re
from gensim import corpora
from gensim.models import LdaModel
from gensim.parsing.preprocessing import preprocess_documents

unprocessed_text = 'Problem to solve: I want to be able to brainstorm effectively. Brainstorming isn\'t necessarily scary, but having to go through my brainstorm and organize my ideas feels overwhelming. There are just so many different things to take into consideration, and when there\'s a big wall of text from my brainstorm, I get anxious thinking about having to organize and categorize everything. This is an even bigger worry with brainstorming out loud. I feel like I brainstorm better when I\'m speaking because speaking helps me keep up with my thoughts more easily than typing, but if I just use a voice dictation software, sifting through the resulting wall of text is even more daunting. Possible solutions: I basically want to be able to display my brainstorm as something with some sort of basic organizational structure. An example would be a bullet-point list, with headings and subheadings, and everything grouped by topic. The difficulty there is how to tell the computer to organize a stream of consciousness. I don\'t want the main topics to be explicitly stated as part of the input, as that gets in the way of the brainstorming process by limiting your ideas to one topic or section at a time, and I tend to ramble and think of things as I\'m speaking that relate to a topic I was talking about earlier. I want the input to be as unregulated as possible, to reduce the barrier to entry as much as possible, and I want the output to be able to structure things enough to take away some of the overwhelming feeling of organizing a big block of text. One of my ideas is to read each statement/sentence as a separate phrase and assign a level of importance to it, but that takes away the connections between topics. I want to be able to connect topics together, so maybe the program could read the statements and if a certain number matches to a certain topic it could become a unit with its own points and subtopics? Or maybe each phrase could have a score for how much it relates to every other phrase, and it could generate this sort of unsupervised learning matrix style model, and create topics from each of the clusters. The new problem there would be how to classify each phrase so that it gets put into the correct cluster. Or maybe create a bunch of different classifiers, and then put bigger weights on certain classifiers to make sure they\'re more likely to be put together. Like make a neural network, and determine the weights for each category based on the amount of relevance a particular category has in that thought dump. '
# Sample documents
documents_by_sentence = unprocessed_text.strip().split('. ')

heading_pattern = r'[^.?!]+:+'
headings = re.findall(heading_pattern, unprocessed_text)
documents_by_heading = re.split(r'[^.!/]+:', unprocessed_text)

# print([document.strip() for document in documents_by_heading])

# Preprocess the documents
processed_docs = preprocess_documents(documents_by_sentence)
# %%
dictionary = corpora.Dictionary(processed_docs)
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

# Build the LDA model
lda_model = LdaModel(corpus, num_topics=2, id2word=dictionary, passes=15)

# Print the topics and their top words
topic0 = lda_model.show_topic(0)
topic1 = lda_model.show_topic(1)
lda_model.print_topics(num_words=3)
# for topic in topics:
#     print(re.findall(r'"([^"]+)"', topic[1]))
# %%
# Initialize lists to store topic distributions for each sentence
topic_distributions = []

# Iterate through the sentences and get topic distributions
for sentence in processed_docs:
    doc_bow = dictionary.doc2bow(sentence)
    topic_distribution = lda_model[doc_bow]
    topic_distributions.append(topic_distribution)

# %%
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# Create and generate a word cloud image:
top_terms_by_topic = lda_model.show_topics(formatted=False)

# Create a word cloud for each topic
for topic_id, top_terms in top_terms_by_topic:
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(top_terms))
    
    # Plot the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'Topic {topic_id}')
    plt.axis("off")
    plt.show()