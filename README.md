# Brain Organizer

## Note: This program has not been written yet. This README document is meant to be an introduction to the project and an explanation of my intentions for it. Expect edits to this page in the future

## Problem

I often struggle with starting a new project because I get overwhelmed with new ideas. Most people advise starting any project or creative endeavor with a brainstorm, in which you write all of your ideas without regard to organization or editing. The idea is that after you've committed all of your ideas to paper, you go back through and sort your ideas into a collection of topics or other organizational pattern, and from there you pick the best ones to use in your project. My two struggles with this method are:

1. It's hard for me to brainstorm on paper. I struggle to write my ideas fast enough to keep up with them coming to me, and the inevitable result is either me only writing some of my ideas, forgetting the rest as I go, or me forgetting to write as I'm thinking of ideas and then having to go through the frustrating process of dictating the thought process I just went through, interrupting my creative "flow". Of course, a possible solution to either of these is using a dictation software to transcribe my voice, since I can speak faster than I can write. I can sometimes, rarely, also enter a flow where I'm writing all of my ideas as they come to me, and I don't have an issue with writing too slow to keep up with my thoughts. Both of those solutions result in a different problem, however.

2. If I make it through the first part of my "brainstorm" successfully, I always end up with a large block of text that I get overwhelmed at the prospect of sorting through. Since both dictation and writing my ideas with no thought towards their organizational structure result in a block of words with no structure, I get overwhelmed by the thought of having to organize it and end up not finishing the process.

In short, I need a way to apply some structure to my brainstorm without having to worry about organization during the beginning stage, so that I don't get overwhelmed by a wall of text that would otherwise be tedious to parse.

## My Program

I want to write a program that can read the results of a brainstorm (a stream of consciousness with little to no organizational structure) and apply a simple organizational structure to it by identifying topics and grouping individual ideas within those topics. The result would be a bullet-point list with headings representing the topics, potential subheadings with sub-topics, and ideas represented by bullet points. In the future, I could envision being able to choose different visualizations for this, like mind maps, chronological or cause and effect, moodboard, etc. My goal is only to simplify the ideas generated during the brainstorm, not to generate new ideas or to create a final draft outline or notes. Any output would be intended to be edited. I want the output to simplify the brainstorm and structure it in a less overwhelming way that is easier to work from than a wall of text.

## Technical Details

I'm strating this project by researching Natural Language Processing (NLP). The two topics most relevant to this project are topic modeling, since the output will be centered around ideas organized by topic, and summarization, which I want to attempt to use to simplify ideas presented in the brainstorm. What's most important to me is preserving the original meaning behind what was written in the input text, so I want to see if I can produce summarized bullet-points that prioritize consistency with the original document over clarity (the idea being that whoever is working with the brainstorm will have an easier time figuring out what something unclear was intended as than something unfaithful to what they originally meant, since usually the person organizing the brainstorm is the same person that dictated it). In the future, a software centered around this project would ideally have an embedded dictation feature, which is its own NLP topic, but for now I plan on using a different dictation tool and feeding its results to my model. 

## Resources (I'll add to this as I go)
- [DeepLearning.AI: NLP]('https://www.deeplearning.ai/resources/natural-language-processing/')