### Grasping the Craftmanship

A subjective journey from a Reservoir Physicist towards a Professional Developer

Note:
Hi everyone, my name is Lars Petter: background

There is no secret that there are a lot of personel in this company developing code that have a similar background as myself, or at least not IT background, that are likely to be missing some of those elements that might be obvious here, and that I also missed. During this talk I will try to elaborate on some of the "design" reasons that I took. I believe there could be similarities between what I've done and what other non-IT people have done. I mean, they are not stupid people, even though they've taken some stupid decisions.

Talk about:
  - What were my intentions of developing
  - How did I use to work

Take aways:
  - Early benefits for someone with my background

---
###  What got me going?

Interpreting Experimental Results:
@ul
 - Numerical measurements
 - Aggregating data (usually excel)
 - Repeated analysis
 - Compare with others
@ulend

Note:

I performed a large range of different core analysis experiments as part of my master and PhD, and typically would the results of such experiments be enterpretation of the results. Different devices measured different conditions and often could those measurements be exported as csv files and the work normally consisted of augmenting the readings.

Excel was by far the number 1 most used tool in our group, and that is likely the case in this company as well. Comparing results from different experiments tend to be very tedious (especially if there are modifications to data, and the metadata to those modifications get lost). Once you do the same kind of analysis over and over again, it doesn't take too long before you google "how to do this in excel", and Visual Basics becomes a familiar tool.

Personally I went as far that I ended up creating a GUI in java, with a MySQL database as backend in order to store and compare experimental results. While I was at the university every master student on the field that I worked with used the tool. That doesn't mean the tool was any good, it just means there was a market for it. I had an excellent distribution system -> email. My issue tracker was a comment section in the code. I had version control, demonstrated by folders with new version numbers (The reasoning behind going from v1 to v2 was strictly based on appearance. "Ah, this looks to have changed quite a lot, let's bumb major").

---
### What got me going?

@img[fragment](sc_days2019/img/core_to_viz.jpg)

Note:

By far the most used format was CSV files, but we also interpreted data from different Imaging machines which used other data formats in order to get 3D data.

The Petroleum Industry has a large range of different file formats, as evident by the number of in-house tools to read them.

---
### The Goal

The goal of my code was to:
@ul
 - Ease the analysis part (repeated tasks)
 - Standardize graphics
 - Perform analysis that would not be possible to do manually
@ulend

Note:
So from my perspective at that time the goal was to:
 - Quickly generate results
 - Spend the least amount of time developing (I would even procrastinate refactoring, because that would be work that didn't add to the project)

The goal was not:
  - clean readable code (I didn't revisit the same code multiple times - it works, don't touch it)
  - Efficient deploy (mail would do)
  - multiple people on the same project

Code is the goal vs report is the goal

---
### Perspectives

What's the worst that can happen?
@ul
 - Crashing is the second best thing
@ulend

---
### Typical setup

@ul
 - Code written as a recipe
 - Have minimal amount of functions - inline everything
 - New features added where "it fits"
 - 500+ lines not uncommon
 - Does "everything"; parsing/transformations/plotting
@ulend

Note:

In the early days I was fairly used to writing my script as a recipe, and line by line do the next thing.

Decoupling responsibilites was time consuming then and there, and the code "already worked"

What made it easier for me to acknowledge was that:
 - A function should be trustable - it should behave as expected.

---
### Enjoyed Improving

Implement and ask:
@ul
 - Name my variables and functions properly
   - Are they what you expect?
 - Create functions that behave as expected
   - Does it do what you think?
 - Create testable functions (and tests of course)
   - Simple setup and asserts?
@ulend

Note:

So taking a step back, reading the function name and ask yourself; What do you expect this function to do? Does it perform as expected?

All of this made me trust my code much more, and be certain that the results were as expected. Of course it takes time, but a couple examples goes a long way.

---
### Enjoyed Improving

Why tests?
@ul
 - Ensure correct function output
 - Documentation
 - **Facilitate changes without fearing unexpected behaviour**
@ulend

Note:
Having the tests made me much less scared of touching the code as well - having tests weren't only about proving that functions work with input/output

---
### But my code is..

Ask someone to try to refactor and you could get the reponse;
> But my function is so complex, it needs all those arguments, that's just how it is

Note:

I don't have a definite reponse to this, but at least; if your problem is complex, the last thing you want is to make it more complex by having code that is hard to understand.

---
### Reaching the balance

Technical debt: Quick & Dirty vs Smart & Elegant

- There is a balance, and it is much closer to Quick and Dirty for Non-IT

---
### What I enjoy about SIB

We strive to follow Software Craftmanship

@ul
- **well-crafted software**
- **steadily adding value**
- **community of professionals**
- **productive partnerships**
@ulend

Note:
What I really enjoy about working in SIB is that we not only allow ourselves to spend time on refactoring and making sure the code is readable, testable and maintanable. 
We _must_ stop and think about if this approach is the right approach, we _have_ to create well-crafted software.
It is not about just implementing user requests, but about setting of time to see if this part of the code could be improved - or if you've learned about a new way of solving something, see if it is applicable in your code base.
