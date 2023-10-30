---
layout: tutorial_hands_on

title: Clinical-MP-Database Quantitation
zenodo_link: ''
questions:
- Which biological questions are addressed by the tutorial?
- Which bioinformatics techniques are important to know for this type of data?
objectives:
- The learning objectives are the goals of the tutorial
- They will be informed by your audience and will communicate to them and to yourself
  what you should focus on during the course
- They are single sentences describing what a learner should be able to do once they
  have completed the tutorial
- You can use Bloom's Taxonomy to write effective learning objectives
time_estimation: 3H
key_points:
- The take-home messages
- They will appear at the end of the tutorial
contributors:
- contributor1
- contributor2
requirements:
  -
    type: "internal"
    topic_name: proteomics
    tutorials:
      - clinical-metaproteonics
subtopic: clinical-metaproteonics
tags: [label-TMT11]
---


# Introduction

<!-- This is a comment. -->

General introduction about the topic and then an introduction of the
tutorial (the questions and the objectives). It is nice also to have a
scheme to sum up the pipeline used during the tutorial. The idea is to
give to trainees insight into the content of the tutorial and the (theoretical
and technical) key concepts they will learn.

You may want to cite some publications; this can be done by adding citations to the
bibliography file (`tutorial.bib` file next to your `tutorial.md` file). These citations
must be in bibtex format. If you have the DOI for the paper you wish to cite, you can
get the corresponding bibtex entry using [doi2bib.org](https://doi2bib.org).

With the example you will find in the `tutorial.bib` file, you can add a citation to
this article here in your tutorial like this:
{% raw %} `{% cite Batut2018 %}`{% endraw %}.
This will be rendered like this: {% cite Batut2018 %}, and links to a
[bibliography section](#bibliography) which will automatically be created at the end of the
tutorial.

![Data Quantitation](../../images/clinical-mp/clinical-mp-quantitation.jpg "FIGURE-1")



> <agenda-title></agenda-title>
>
> In this tutorial, we will cover:
>
> 1. TOC
> {:toc}
>
{: .agenda}

# Title for your first section

Give some background about what the trainees will be doing in the section.
Remember that many people reading your materials will likely be novices,
so make sure to explain all the relevant concepts.

## Title for a subsection
Section and subsection titles will be displayed in the tutorial index on the left side of
the page, so try to make them informative and concise!

# Hands-on Sections
Below are a series of hand-on boxes, one for each tool in your workflow file.
Often you may wish to combine several boxes into one or make other adjustments such
as breaking the tutorial into sections, we encourage you to make such changes as you
see fit, this is just a starting point :)

Anywhere you find the word "***TODO***", there is something that needs to be changed
depending on the specifics of your tutorial.

have fun!

## Get data

> <hands-on-title> Data Upload </hands-on-title>
>
> 1. Create a new history for this tutorial
> 2. Import the files from [Zenodo]({{ page.zenodo_link }}) or from
>    the shared data library (`GTN - Material` -> `{{ page.topic_name }}`
>     -> `{{ page.title }}`):
>
>    ```
>    
>    ```
>    ***TODO***: *Add the files by the ones on Zenodo here (if not added)*
>
>    ***TODO***: *Remove the useless files (if added)*
>
>    {% snippet faqs/galaxy/datasets_import_via_link.md %}
>
>    {% snippet faqs/galaxy/datasets_import_from_data_library.md %}
>
> 3. Rename the datasets
> 4. Check that the datatype
>
>    {% snippet faqs/galaxy/datasets_change_datatype.md datatype="datatypes" %}
>
> 5. Add to each database a tag corresponding to ...
>
>    {% snippet faqs/galaxy/datasets_add_tag.md %}
>
{: .hands_on}

# Title of the section usually corresponding to a big step in the analysis

It comes first a description of the step: some background and some theory.
Some image can be added there to support the theory explanation:

![Alternative text](../../images/image_name "Legend of the image")

The idea is to keep the theory description before quite simple to focus more on the practical part.

***TODO***: *Consider adding a detail box to expand the theory*

> <details-title> More details about the theory </details-title>
>
> But to describe more details, it is possible to use the detail boxes which are expandable
>
{: .details}

A big step can have several subsections or sub steps:



{: .question}

## Sub-step with **MaxQuant**

In the Discovery Module (**cite Discovery module**), we used MaxQuant (**cite tool**) to identify peptides for verification. Now, we will again use MaxQuant to further quantify the PepQuery-verified peptides, both microbial and human.

The outputs we are most interested in consist of the MaxQuant Evidence file, MaxQuant Protein Groups, and MaxQuant Peptides. The MaxQuant Peptides file will allow us to group them to generate a list of quantified microbial peptides.

> <hands-on-title> Task description </hands-on-title>
>
> 1. {% tool [MaxQuant](toolshed.g2.bx.psu.edu/repos/galaxyp/maxquant/maxquant/1.6.17.0+galaxy4) %} with the following parameters:
>    - In *"Input Options"*:
>        - {% icon param-file %} *"FASTA files"*: `Quantitation Database for MaxQuant` (Input dataset)
>    - In *"Search Options"*:
>        - {% icon param-file %} *"Specify an experimental design template (if needed). For detailed                           instructions see the help text."*: `output` (Input dataset)
>        - *"minimum peptide length"*: `8`
>        - *"Match between runs"*: `Yes`
>        - *"Maximum peptide length for unspecific searches"*: `50`
>    - In *"Protein quantification"*:
>        - *"Use only unmodified peptides"*: `Yes`
>            - *"Modifications used in protein quantification"*: ``
>        - In *"LFQ Options"*:
>            - *"iBAQ (calculates absolute protein abundances by normalizing to copy number and not protein mass)"*: `No`
>    - In *"Parameter Group"*:
>        - {% icon param-repeat %} *"Insert Parameter Group"*
>            - {% icon param-collection %} *"Infiles"*: `output` (Input dataset collection)
>            - *"fixed modifications"*: ``
>            - *"variable modifications"*: ``
>            - *"enzyme"*: ``
>            - *"Quantitation Methods"*: `reporter ion MS2`
>                - *"isobaric labeling"*: `TMT11plex`
>                - *"Filter by PIF"*: `Yes`
>    - In *"Output Options"*:
>        - *"Select the desired outputs."*: ``
>
>    ***TODO***: *Check parameter descriptions*
>
>    ***TODO***: *Consider adding a comment or tip box*
>
>    > <comment-title> short description </comment-title>
>    >
>    > A comment about the tool or something else. This box can also be in the main text
>    {: .comment}
>
{: .hands_on}

***TODO***: *Consider adding a question to test the learners understanding of the previous exercise*

> <question-title></question-title>
>
> 1. Why can we switch back to using RAW files for MaxQuant, instead of using MGF files?
> 2. Previously, we used MaxQuant in the Discovery workflow. Why are we using MaxQuant again, instead of Search GUI/PeptideShaker?
>
> > <solution-title></solution-title>
> >
> > 1. **TODO** Answer for question1
> > 2. **TODO** Answer for question2
> >
> {: .solution}
>
{: .question}

## Sub-step with **Select**

> <hands-on-title> Task description </hands-on-title>
>
> 1. {% tool [Select](Grep1) %} with the following parameters:
>    - {% icon param-file %} *"Select lines from"*: `proteinGroups` (output of **MaxQuant** {% icon tool %})
>    - *"that"*: `NOT Matching`
>    - *"the pattern"*: `(_HUMAN)|(_REVERSED)|(CON)|(con)`
>
>    ***TODO***: *Check parameter descriptions*
>
>    ***TODO***: *Consider adding a comment or tip box*
>
>    > <comment-title> short description </comment-title>
>    >
>    > A comment about the tool or something else. This box can also be in the main text
>    {: .comment}
>
{: .hands_on}

***TODO***: *Consider adding a question to test the learners understanding of the previous exercise*

> <question-title></question-title>
>
> 1. Question1?
> 2. Question2?
>
> > <solution-title></solution-title>
> >
> > 1. **TODO** Answer for question1
> > 2. **TODO** Answer for question2
> >
> {: .solution}
>
{: .question}

## Sub-step with **Select**

> <hands-on-title> Task description </hands-on-title>
>
> 1. {% tool [Select](Grep1) %} with the following parameters:
>    - {% icon param-file %} *"Select lines from"*: `peptides` (output of **MaxQuant** {% icon tool %})
>    - *"that"*: `NOT Matching`
>    - *"the pattern"*: `(_HUMAN)|(_REVERSED)|(CON)|(con)`
>
>    ***TODO***: *Check parameter descriptions*
>
>    ***TODO***: *Consider adding a comment or tip box*
>
>    > <comment-title> short description </comment-title>
>    >
>    > A comment about the tool or something else. This box can also be in the main text
>    {: .comment}
>
{: .hands_on}

***TODO***: *Consider adding a question to test the learners understanding of the previous exercise*

> <question-title></question-title>
>
> 1. Question1?
> 2. Question2?
>
> > <solution-title></solution-title>
> >
> > 1. **TODO** Answer for question1
> > 2. **TODO** Answer for question2
> >
> {: .solution}
>
{: .question}

## Sub-step with **Cut**

> <hands-on-title> Task description </hands-on-title>
>
> 1. {% tool [Cut](Cut1) %} with the following parameters:
>    - *"Cut columns"*: `c1`
>    - {% icon param-file %} *"From"*: `out_file1` (output of **Select** {% icon tool %})
>
>    ***TODO***: *Check parameter descriptions*
>
>    ***TODO***: *Consider adding a comment or tip box*
>
>    > <comment-title> short description </comment-title>
>    >
>    > A comment about the tool or something else. This box can also be in the main text
>    {: .comment}
>
{: .hands_on}

***TODO***: *Consider adding a question to test the learners understanding of the previous exercise*

> <question-title></question-title>
>
> 1. Question1?
> 2. Question2?
>
> > <solution-title></solution-title>
> >
> > 1. **TODO** Answer for question1
> > 2. **TODO** Answer for question2
> >
> {: .solution}
>
{: .question}

## Sub-step with **Cut**

> <hands-on-title> Task description </hands-on-title>
>
> 1. {% tool [Cut](Cut1) %} with the following parameters:
>    - *"Cut columns"*: `c1`
>    - {% icon param-file %} *"From"*: `out_file1` (output of **Select** {% icon tool %})
>
>    ***TODO***: *Check parameter descriptions*
>
>    ***TODO***: *Consider adding a comment or tip box*
>
>    > <comment-title> short description </comment-title>
>    >
>    > A comment about the tool or something else. This box can also be in the main text
>    {: .comment}
>
{: .hands_on}

***TODO***: *Consider adding a question to test the learners understanding of the previous exercise*

> <question-title></question-title>
>
> 1. Question1?
> 2. Question2?
>
> > <solution-title></solution-title>
> >
> > 1. **TODO** Answer for question1
> > 2. **TODO** Answer for question2
> >
> {: .solution}
>
{: .question}

## Sub-step with **Group**

> <hands-on-title> Task description </hands-on-title>
>
> 1. {% tool [Group](Grouping1) %} with the following parameters:
>    - {% icon param-file %} *"Select data"*: `out_file1` (output of **Cut** {% icon tool %})
>    - *"Group by column"*: `c1`
>
>    ***TODO***: *Check parameter descriptions*
>
>    ***TODO***: *Consider adding a comment or tip box*
>
>    > <comment-title> short description </comment-title>
>    >
>    > A comment about the tool or something else. This box can also be in the main text
>    {: .comment}
>
{: .hands_on}

***TODO***: *Consider adding a question to test the learners understanding of the previous exercise*

> <question-title></question-title>
>
> 1. Question1?
> 2. Question2?
>
> > <solution-title></solution-title>
> >
> > 1. **TODO** Answer for question1
> > 2. **TODO** Answer for question2
> >
> {: .solution}
>
{: .question}

## Sub-step with **Group**

> <hands-on-title> Task description </hands-on-title>
>
> 1. {% tool [Group](Grouping1) %} with the following parameters:
>    - {% icon param-file %} *"Select data"*: `out_file1` (output of **Cut** {% icon tool %})
>    - *"Group by column"*: `c1`
>
>    ***TODO***: *Check parameter descriptions*
>
>    ***TODO***: *Consider adding a comment or tip box*
>
>    > <comment-title> short description </comment-title>
>    >
>    > A comment about the tool or something else. This box can also be in the main text
>    {: .comment}
>
{: .hands_on}

***TODO***: *Consider adding a question to test the learners understanding of the previous exercise*

> <question-title></question-title>
>
> 1. Question1?
> 2. Question2?
>
> > <solution-title></solution-title>
> >
> > 1. **TODO** Answer for question1
> > 2. **TODO** Answer for question2
> >
> {: .solution}
>
{: .question}


## Re-arrange

To create the template, each step of the workflow had its own subsection.

***TODO***: *Re-arrange the generated subsections into sections or other subsections.
Consider merging some hands-on boxes to have a meaningful flow of the analyses*

# Conclusion

Sum up the tutorial and the key takeaways here. We encourage adding an overview image of the
pipeline used.
