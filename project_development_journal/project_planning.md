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
**Main discovery: I need to narrow the scope of this project to start, complete the project with scalability in mind but not as the focus, and think about expansion after I've completed a basic form of the project**
I've realized that my idea was too broad in scope and that it will be difficult to create a software with all the capability I envisioned with my current resources and time. I'd still like to expand this project in the future to apply to a wide range of brainstorming tasks, but for now the amount I would need to account for in doing so is too much.

### Narrow focus possibilities
- Brainstorming for creativity
    - Plotting a story
    - Writing an essay, article, blog post, etc.
    - Creating a fantasy world (for video game, book, movie, etc)
- Brainstorming for productivity
    - Planning a project (ex. software design, writing and publishing a book, art project prep)
    - Scheduling
    - Problem solving
- Brainstorming to generate ideas
In short, I can either design my project to focus on creative brainstorming or productive brainstorming. The distinction is largely in the purpose of the brainstorm. When making a creative brainstorm, the objective is to generate as many ideas as possible with less regard to a specific goal or structure. The most important thing is generating content, which one can later parse and process to apply a structure to it. A productive brainstorm is more structured; there's typically a goal to achieve or a problem to solve, and a big part of the brainstorm is considering and judging previous ideas based on their efficacy. There's a bit of overlap in where and how people apply both brainstorming techniques: for example, a writer might use a productive brainstorm to work out a chronology for their story, and a software development team might brainstorm features to add to their software with less regard to a specific goal. I think I've been thinking of both methods as interchangeable so far, and I've been struggling to come up with how to deal with all the possible ways to handle different brainstorms. For example, one person might want their outline to be categorized by task rather than by topic (ex. problem, solutions; as opposed to "technology" and "fashion" if they're brainstorming ways to design a sewing patterning software), but another might want to organize their brainstorm by topic. I realized that the main difference is that the two people have two different brainstorming goals: one is worried about a specific goal (as implied by their focus on problems and solutions), and the other is focused on generating ideas.
I've decided that my software concept as it stands will probably be better suited to creative brainstorming for a few reasons:
1. A productive brainstorm is likely to have more internal organization to begin with, and therefore would not benefit as much from a software mainly designed to apply structure to something that doesn't have any.
2. Identifying key words to associate with certain categories (i.e. is likely to talk about "pros and cons," "problems" and "solutions", "things to avoid" and "goals", etc.) is better suited to text classification than topic modeling, and since structure is usually relatively predictable in a productive brainstorm, this would likely be the more beneficial task. 
3. My main struggle is with creative brainstorming. I have a hard time creating something from nothing, and my main goal at the beginning was creating a software that would remove the organization hurdle I face with creative brainstorming. I don't struggle as much with productive brainstorming because I have a focused goal, the number of ideas I can generate is usually smaller, and having a focused structure from the beginning helps me to put all of my ideas in context of my project and generate new ideas because of those correlations. It's much easier to avoid getting overwhelmed with productive brainstorming, at least for me, so that's the problem I'm most interested in solving.

