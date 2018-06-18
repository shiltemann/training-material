#!/usr/bin/env python3

'''
take a Galaxy workflow definition file (.ga) and create a skeleton
tutorial file with hands-on boxes per tool.

usage: workflow-to-tutorial.py --workflow <workflow file>
'''

import argparse
import json
import sys


template_question = '''
<-- Consider adding a question to test the learners understanding of the previous exercise -->
> ### {% icon question %} Questions
>
> 1. Question1?
> 2. Question2?
>
>    > ### {% icon solution %} Solution
>    >
>    > 1. Answer for question1
>    > 2. Answer for question2
>    >
>    {: .solution}
>
{: .question}
'''


def nested_dict_iter(nested):
    for key, value in nested.items():
        try:
            value = json.loads(value)
            yield from nested_dict_iter(value)
        except Exception:
            pass

        if isinstance(value, dict):
            yield from nested_dict_iter(value)
        # if isinstance(value, list):

        else:
            yield key, value


def get_handson_box(step):
    ''' make the first hands-on box for data upload'''
    # TODO: get data library name from yaml file
    global template_question

    # print(json.dumps(step, indent=4))
    tool_name = step[1]['name']

    if tool_name == 'Input dataset':
        return

    inputs = step[1]['input_connections']
    parameters = step[1]['tool_state']

    print(parameters)
    print(inputs)

    inputlist = ''
    for i in inputs:
        print("input: ", i, step[1]['input_connections'][i]['id'])
        inputlist += '\n>   - {% icon param-file %} *"' + i + '"*: `' + \
                     step[1]['input_connections'][i]['output_name'] + \
                     ' output from step ' + \
                     str(step[1]['input_connections'][i]['id']) + '`'

    g = nested_dict_iter(json.loads(parameters))

    paramlist = ''

    while True:
        try:
            (k, v) = next(g)
            print("param: ", k, v)
        except StopIteration:
            break

        if not v or v == 'null' or v == '[]':
            pass
        elif 'RuntimeValue' in str(v):
            pass
            # print("myinputs:", v, inputs)
            # print(inputs)
        elif '__' not in k and k != 'chromInfo':
            paramlist += '\n>   - *"' + k + '"*: `' + str(v).strip('"[]') + '`'

    # print(paramlist)

    template = '''
> ### {{% icon hands_on %}} Hands-on: TODO: task description
>
> **{tool_name}** {{% icon tool %}} with the following parameters:{inputlist}{paramlist}
>
>   TODO: check parameter descriptions
>   TODO: some of these parameters may be the default values and can be removed
>         unless they have some didactic value.
>
{{: .hands_on}}
'''
    context = {
        "tool_name": tool_name,
        "paramlist": paramlist,
        "inputlist": inputlist
    }
    # print(context)
    return template.format(**context) + template_question


def get_tutorial_header(topic, tutorial_name):
    ''' Make the tutorial preabmle e.g. intro and agenda '''

    template = '''---
layout: tutorial_hands_on
topic_name: {topic}
tutorial_name: {tutorial_name}
---

# Introduction
{{:.no_toc}}

write a (short) introduction here

> ### Agenda
>
> In this tutorial, we will cover:
>
> 1. TOC
> {{:toc}}
>
{{: .agenda}}

# Title for your first section

Give some background about what the trainees will be doing in the section.

Below are a series of hand-on boxes, one for each tool in your workflow file.
Often you may wish to combine several boxes into one or make other adjustments such
as breaking the tutorial into sections, we encourage you to make such changes as you
see fit, this is just a starting point :)

Anywhere you find the word `TODO`, there is something that needs to be changed
depending on the specifics of your tutorial.

have fun!

'''
    context = {
        "topic": topic,
        "tutorial_name": tutorial_name
    }
    return template.format(**context)


def get_data_upload_box():
    ''' make the first hands-on box for the data upload step '''
    # TODO: get data library name from yaml file

    template = '''
> ### {% icon hands_on %} Hands-on: Data upload
>
> 1. Import the following files from [Zenodo](https://zenodo.org/record/<TODO>) or from a data
>    library named `TODO` if available (ask your instructor)
>    - `file1.txt`
>    - `file2.vcf`
>    - `fileN.bam`
>
>    > ### {% icon tip %} Tip: Importing data via links
>    >
>    > * Copy the link location
>    > * Open the Galaxy Upload Manager
>    > * Select **Paste/Fetch Data**
>    > * Paste the link into the text field
>    > * Press **Start**
>    >
>    > By default, Galaxy uses the url as the name, so please rename them to something more pleasing.
>    {: .tip}
>
>    > ### {% icon tip %} Tip: Importing data from a data library
>    >
>    > * Go into "Shared data" (top panel) then "Data libraries"
>    > * Click on "Training data" and then "Analyses of metagenomics data"
>    > * Select interesting file
>    > * Click on "Import selected datasets into history"
>    > * Import in a new history
>    {: .tip}
>
{: .hands_on}

'''
    return template


def get_tutorial_footer():
    template = '''
# Conclusion
{:.no_toc}

Sum up the tutorial and the key takeaways here. We encourage adding an overview image of the
pipeline used.

'''
    return template


def create_tutorial(workflowfile, outfile, topic, tutorial_name):
    # print(workflowfile, outfile)
    with open(workflowfile, 'r') as wf:
        try:
            workflow = json.load(wf)
        except json.decoder.JSONDecodeError:
            print("workflow file looks invalid")
            sys.exit()
    # print(json.dumps(workflow, indent=4))

    # create the tutorial
    print(get_tutorial_header(topic, tutorial_name))
    print(get_data_upload_box())
    for step in workflow['steps'].items():
        print(get_handson_box(step))
    print(get_tutorial_footer())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a skeleton tutorial markdown file from a Galaxy workflow definition file')
    parser.add_argument('workflow', help='location of workflow .ga file to base tutorial on')
    parser.add_argument('-o', '--outputfile', default='tutorial.md', help='file to save the resulting tutorial .md file to')
    parser.add_argument('--topic', default='TODO', help='topic your tutorial is intended for')
    parser.add_argument('--tutorial', default='TODO', help='name of your tutorial (must be the same as name of your tutorial folder)')

    args = parser.parse_args()

    create_tutorial(args.workflow, args.outputfile, args.topic, args.tutorial)
