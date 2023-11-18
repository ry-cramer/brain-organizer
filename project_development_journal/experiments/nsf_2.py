# %%
import pandas as pd
import numpy as np
from textblob import TextBlob
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import TSNE
from gensim.models.coherencemodel import CoherenceModel
from gensim.corpora.dictionary import Dictionary
from gensim.models.nmf import Nmf
from gensim.parsing.preprocessing import preprocess_documents
from collections import Counter
from operator import itemgetter
import matplotlib.pyplot as plt
import seaborn as sns
import re

'''
To do:
    - Bi/trigrams
    - Stop words
    - Stemming
    - Contractions?
    - Punctuation
'''
class Input:
    # STOP_WORDS = ENGLISH_STOP_WORDS
    def __init__(self, texts: str):
        self.vectorizer = TfidfVectorizer(
            stop_words = 'english',
            max_df = .85,
            ngram_range = (1, 3),
            max_features = 100,
            preprocessor = ' '.join
            )
        self.texts = texts
        self.processed_texts = self.__preprocess_text(texts)
        self.tfidf = self.__vectorize_text(self.processed_texts, self.vectorizer)

    def __preprocess_text(self, texts):
        '''
        To do:
            - Bi/trigrams
            - Stop words
            - Stemming
            - Contractions?
            - Punctuation
        '''
        texts = re.split('\.\s', texts.lower())
        return [TextBlob(text).words for text in texts]
        

    def __vectorize_text(self, processed_texts, vectorizer):
        tfidf = self.vectorizer.fit_transform(processed_texts)
        return tfidf

neon_haven = Input('In the sprawling metropolis of Neon Haven, a city eternally draped in the luminous glow of holographic billboards and the ambient hum of neon lights, the air is thick with the palpable tension of a society caught in the perpetual dance between innovation and decay. Welcome to a cyberpunk world where the boundary between man and machine blurs, and the city itself becomes a living, breathing organism pulsating with the rhythm of technological progress and social disparity.\nThe skyline of Neon Haven is a chaotic tapestry of skyscrapers that scrape the heavens, adorned with massive LED displays that project advertisements for cybernetic enhancements, virtual realities, and illicit data trades. Buildings rise like colossal monuments to a future where the distinction between the physical and the digital is nearly indistinguishable. At street level, narrow alleyways and dimly lit backstreets serve as the arteries of the city, teeming with life both human and artificial.\nRain falls perpetually in Neon Haven, not the gentle drizzle romanticized in old films, but an acidic downpour that hisses as it makes contact with the synthetic surfaces of the city. Umbrellas adorned with glowing LED patterns are a common sight, shielding citizens from the corrosive droplets as they navigate the crowded streets. The rain, both a blessing and a curse, symbolizes the dichotomy of this cyberpunk world – a source of life for the city\'s megastructures and a relentless force eroding the humanity of its denizens.\nBeneath the neon-lit exterior lies the underbelly of Neon Haven, a labyrinth of subterranean tunnels and makeshift dwellings where those who have fallen through the cracks of society eke out a living. Here, the flickering fluorescence of broken signs and malfunctioning streetlights cast long shadows on the faces of the disenfranchised, the hackers, the rebels, and those who resist the corporate stranglehold on the city.\nThe corporate elite, ruling from the penthouses of glittering skyscrapers, control every aspect of life in Neon Haven. Massive conglomerates like OmniCorp and Synthetics Unlimited dictate the flow of information, control access to advanced technologies, and exploit the populace for cheap labor. In this cyberpunk dystopia, power is not wielded by politicians but by the CEOs and board members who sit atop colossal corporate pyramids, their empires built on the backs of the augmented workforce.\nAugmentation is not a luxury in Neon Haven; it\'s a necessity for survival. Cybernetic enhancements are ubiquitous, ranging from neural interfaces that connect individuals to the city\'s vast digital network to biomechanical limbs that enhance physical capabilities. The streets are populated by the augmented and the organically human alike, creating a surreal juxtaposition of sleek metallic limbs and exposed flesh.\nThe streets pulse with the constant exchange of data and information. Augmented reality overlays cling to every surface, transforming the city into a canvas for hackers and activists to broadcast their messages. Citizens navigate this sea of information using neural implants and augmented reality glasses, their field of vision cluttered with pop-up ads, personal messages, and real-time data streams.\nLaw enforcement in Neon Haven is an extension of corporate interests, private security firms patrolling the streets with a heavy hand. Autonomous drones equipped with facial recognition technology scan the crowds, ensuring that dissent is swiftly quelled. The concept of privacy is a relic of the past; every step, every purchase, and every interaction is tracked and monitored in the name of maintaining order.\nThe black market thrives in the shadows of Neon Haven, a clandestine network where goods, services, and information are traded beyond the watchful eyes of the corporations. Here, hackers with pseudonyms like ZeroDay and ShadowCipher operate from hidden cybercafes, their fingers dancing across holographic keyboards as they breach the firewalls of mega-corporations and expose their darkest secrets.\nNeon Haven\'s entertainment district is a dizzying array of virtual reality arcades, underground clubs, and futuristic casinos. The sounds of synthwave music and the glow of holographic dancers spill onto the streets, offering a temporary escape from the harsh realities of the city. In the VR parlors, users immerse themselves in fantastical worlds, seeking solace in digital realms where they can momentarily shed their augmented identities.\nAmidst the chaos, a resistance brews in the shadows, a coalition of hackers, activists, and disillusioned citizens determined to break free from the chains of corporate oppression. Their symbol, a glitched icon of a circuit board breaking free from chains, is spray-painted on the walls of abandoned buildings and hidden in the code of the city\'s mainframe.\nNeon Haven is a world where the line between right and wrong is blurred, where survival often necessitates compromise, and where the relentless march of progress leaves the less fortunate in its wake. In the cyberpunk streets, where the glow of neon illuminates the stories of both the powerful and the powerless, the future is uncertain, and the only constant is the ever-present hum of the city itself.')
# experiment_input = 'Apples are crunchy and sweet. Bananas are soft and sweet. Carrots are nutritious vegetables, as are broccoli and spinach. I don\'t really like vegetables, but I love fruits like apples and grapes.'

vectorizer = neon_haven.vectorizer
processed_texts = neon_haven.processed_texts
tfidf = neon_haven.tfidf
print(f'{processed_texts}\n{tfidf}')
# %%
# Plotting DTM
dense_tfidf = pd.DataFrame(tfidf.todense())
# sns.barplot(dense_tfidf, x=dense_tfidf.columns)
feature_names = vectorizer.get_feature_names_out().tolist()
dense_tfidf.columns = feature_names
dense_tfidf.loc['Mean'] = dense_tfidf.mean()
df = dense_tfidf.sort_values(by='Mean', axis=1, ascending=False)
df = df.iloc[:, :100 + 1]
# Create a heatmap with the top N features
plt.figure(figsize=(12, 8))
sns.heatmap(df, cmap='viridis')
plt.title('Top N Features TF-IDF Heatmap')
plt.xlabel('Top N Features')
plt.ylabel('Documents')
plt.show()
# %%
# Calculating optimal topic number

def determine_optimal_topics(matrix, max_topics=10):
    error = []
    for i in range(1, max_topics + 1):
        nmf = NMF(n_components=i, random_state=42, max_iter=1000, alpha=1)
        nmf.fit(matrix)
        error.append(nmf.reconstruction_err_)

    # Use the elbow method to find the optimal number of topics
    elbow = 0
    difference_error = 0
    for i in range(2, max_topics - 1):
        slope_before = error[i] - error[i - 1]
        slope_after = error[i + 1] - error[i]
        curr_difference_error = slope_after - slope_before
        print(curr_difference_error)
        if curr_difference_error > difference_error:
            difference_error = curr_difference_error
            elbow = i + 1

    # Optionally, you can also visualize the elbow method plot
    plt.plot(range(1, max_topics + 1), error, marker='o')
    plt.title('Elbow Method for Optimal Number of Topics')
    plt.xlabel('Number of Topics')
    plt.ylabel('Reconstruction Error')
    plt.show()

    return elbow

print(determine_optimal_topics(tfidf))
# %%
# NMF Model: 1st draft
components = 3
NMF_model = NMF(n_components=components, random_state=42, max_iter=1000, alpha=1)
W = NMF_model.fit_transform(tfidf)
H = NMF_model.components_

topic_word_list = []
def get_topics(components): 
    for i, comp in enumerate(components):
        terms_comp = zip(vectorizer.get_feature_names_out(),comp)
        sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:7]
        topic=" "
        for t in sorted_terms:
            topic= topic + ' ' + t[0]
        topic_word_list.append(topic)
    return topic_word_list

topics = get_topics(H)
for i in range(len(topics)):
    print(f'Topic {i+1}:\n{topics[i]}')

# %%
# Word clouds
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create a word cloud for each topic
for i in range(len(topics)):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(topics[i])
    
    # Plot the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'Topic {i+1}')
    plt.axis("off")
    plt.show()
# %%
# Graphic visualization
tsne_model = TSNE(n_components=2, perplexity=10, random_state=42)
tsne_representation = tsne_model.fit_transform(W)

plt.figure(figsize=(10, 8))
for i in range(components):
    plt.scatter(tsne_representation[W.argmax(axis=1) == i, 0],
                tsne_representation[W.argmax(axis=1) == i, 1],
                label=f'Topic {i + 1}')

plt.title('t-SNE Visualization of NMF Clusters')
plt.legend()
plt.show()
# %%
# Sentences per Topic
# Identify the dominant topic for each sentence
dominant_topics = W.argmax(axis=1)

# Add the dominant topic information to the original sentences
sentences_with_topics = pd.DataFrame({'Sentence': neon_haven.processed_texts, 'Dominant Topic': dominant_topics + 1})

# Display the sentences with their dominant topics
sentences_with_topics
# %%
