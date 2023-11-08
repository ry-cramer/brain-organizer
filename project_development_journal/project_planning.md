# Project Development Journal

## Day 1
I wrote the first iteration of README.md. I articulated the problem, my proposed solution, and my proposed method of programming my solution.

### Research Topics for Day 2
- Topic modeling (start with DeepLearning.AI)
    - LDA and neural networks for topic modeling
- Summarization (start with DeepLearning.AI)
- NLP Data Collection and Preprocessing

### Things to Do/Figure Out Day 2
- Practice smaller scale models (try topic modeling tutorials) and familiarize with input/output
- What method of topic modeling to try first
- Where/How to collect training/testing data

### *Main Goal for Day 2: Learn*

## Day 2
I worked on `lda_1.py` to learn how gensim and topic modeling works (i.e. the types of outputs, the way gensim represents dictionaries and BOWs, creating word clouds, identifying regular expressions to interpret a document, etc.).

### What I learned:
1. LDA models might not give me the flexibility I need to work with such a diverse and unregulated input. Having to choose a number of topics to identify is realy limiting for the type of modeling I want to do
2. I need to solidify more what I want my output to look like. I know vaguely what I want my output to look like, but I need specifics:
- What structure do I want the output to be (at least to start out with)? Bullet point list, venn diagram, mind map?
- What information do I need to populate such a structure?
3. The basic flow of a topic model is:
    1. Clean the input (remove punctuation + capitalization + stop words, stemming and lemmitization)
    2. Create a dictionary and corpus
    3. Train the model
    4. Apply the model
    5. Visualize the output

### Day 3 Tasks:
- Create a few samples of inputs and desired outputs, and analyze the results. Questions to ask:
    - What changed about the input?
    - What information informed each change?
    - What didn't change about the input?
- Create a first draft frontend for the output
- Exploration should be mostly finished by the end of this day

## Day 3


