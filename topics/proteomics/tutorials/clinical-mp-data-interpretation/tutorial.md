---
layout: tutorial_hands_on

title: Clinical-MP-Database Interpretation
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
      - clinical-metaproteomics
subtopic: multi-omics
tags: [label-TMT11]
---


# Introduction

The final workflow in the array of clinical metaproteomics tutorials is the data interpretation workflow. Interpreting MaxQuant data using MSstats involves applying a rigorous statistical framework to glean meaningful insights from quantitative proteomic datasets. The MaxQuant output is explored to understand data distribution and variability. Subsequent normalization helps account for systematic variations. MSstats allows the user to define the experimental design, including sample groups and conditions, to perform statistical analysis. The output provides valuable information about differential protein expression across conditions, estimates of fold changes, and associated p-values, aiding in the identification of biologically significant proteins. Furthermore, MSstats enables quality control and data visualization, ultimately enhancing our ability to draw meaningful conclusions from complex proteomic datasets.

![Database-Interpretation](../../images/clinical-mp/clinical-mp-data-interpretation.jpg "FIGURE-1")
> <agenda-title></agenda-title>
>
> In this tutorial, we will cover:
>
> 1. TOC
> {:toc}
>
{: .agenda}

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


## Sub-step with **Unipept**

> <hands-on-title> Task description </hands-on-title>
>
> 1. {% tool [Unipept](toolshed.g2.bx.psu.edu/repos/galaxyp/unipept/unipept/4.5.1) %} with the following parameters:
>    - *"Unipept application"*: `peptinfo: Tryptic peptides and associated EC and GO terms and lowest common ancestor taxonomy`
>    - *"Peptides input format"*: `tabular`
>        - {% icon param-file %} *"Tabular Input Containing Peptide column"*: `output` (Input dataset)
>        - *"Select column with peptides"*: `cc1`
>    - *"Match input peptides by"*: `Match to the full input peptide`
>    - *"Choose outputs"*: ``
>
>
{: .hands_on}


## Sub-step with **Select**

> <hands-on-title> Task description </hands-on-title>
>
> 1. {% tool [Select](Grep1) %} with the following parameters:
>    - {% icon param-file %} *"Select lines from"*: `output` (Input dataset)
>    - *"that"*: `NOT Matching`
>    - *"the pattern"*: `(HUMAN)|(REV)|(CON)|(con)`
>    - *"Keep header line"*: `Yes`
>
>
{: .hands_on}

## Sub-step with **Select**

> <hands-on-title> Task description </hands-on-title>
>
> 1. {% tool [Select](Grep1) %} with the following parameters:
>    - {% icon param-file %} *"Select lines from"*: `output` (Input dataset)
>    - *"the pattern"*: `(HUMAN)`
>    - *"Keep header line"*: `Yes`
>
>
{: .hands_on}


## Sub-step with **MSstatsTMT**

> <hands-on-title> Task description </hands-on-title>
>
> 1. {% tool [MSstatsTMT](toolshed.g2.bx.psu.edu/repos/galaxyp/msstatstmt/msstatstmt/2.0.0+galaxy1) %} with the following parameters:
>    - *"Input Source"*: `MaxQuant`
>        - {% icon param-file %} *"evidence.txt - feature-level data"*: `output` (Input dataset)
>        - {% icon param-file %} *"proteinGroups.txt"*: `out_file1` (output of **Select** {% icon tool %})
>        - {% icon param-file %} *"annotation.txt"*: `output` (Input dataset)
>    - In *"Plot Output Options"*:
>        - *"Select protein IDs to draw plots"*: `generate all plots for each protein`
>    - *"Compare Groups"*: `Yes`
>        - *"Use comparison matrix?"*: `Yes`
>            - {% icon param-file %} *"Comparison Matrix"*: `output` (Input dataset)
>        - In *"Comparison Plot Options"*:
>            - *"Select protein IDs to draw plots"*: `generate all plots for each protein`
>            - *"Select comparisons to draw plots"*: `Generate all plots for each comparison`
>
>
{: .hands_on}


## Sub-step with **Select**

> <hands-on-title> Task description </hands-on-title>
>
> 1. {% tool [Select](Grep1) %} with the following parameters:
>    - {% icon param-file %} *"Select lines from"*: `out_file1` (output of **Select** {% icon tool %})
>    - *"that"*: `NOT Matching`
>    - *"the pattern"*: `(REV)|(con)`
>    - *"Keep header line"*: `Yes`
>
>
{: .hands_on}


## Sub-step with **MSstatsTMT**

> <hands-on-title> Task description </hands-on-title>
>
> 1. {% tool [MSstatsTMT](toolshed.g2.bx.psu.edu/repos/galaxyp/msstatstmt/msstatstmt/2.0.0+galaxy1) %} with the following parameters:
>    - *"Input Source"*: `MaxQuant`
>        - {% icon param-file %} *"evidence.txt - feature-level data"*: `output` (Input dataset)
>        - {% icon param-file %} *"proteinGroups.txt"*: `out_file1` (output of **Select** {% icon tool %})
>        - {% icon param-file %} *"annotation.txt"*: `output` (Input dataset)
>    - In *"Plot Output Options"*:
>        - *"Select protein IDs to draw plots"*: `generate all plots for each protein`
>    - *"Compare Groups"*: `Yes`
>        - *"Use comparison matrix?"*: `Yes`
>            - {% icon param-file %} *"Comparison Matrix"*: `output` (Input dataset)
>        - In *"Comparison Plot Options"*:
>            - *"Select protein IDs to draw plots"*: `generate all plots for each protein`
>            - *"Select comparisons to draw plots"*: `Generate all plots for each comparison`
>
>
{: .hands_on}

# Conclusion
With the completion of this tutorial, you have successfully completed the clinical metaproteomics tutorials.
In conclusion, clinical metaproteomics tutorials represent an essential gateway to harnessing the power of advanced proteomic techniques in the realm of clinical research and applications. These bioinformatics tutorials serve as valuable guides for understanding the intricacies of metaproteomic workflows, from  data analysis to interpretation. By providing comprehensive knowledge and practical insights, they equip researchers and clinicians with the tools necessary to explore the rich diversity of the microbiome and its impact on health and disease or environment. As metaproteomic techniques continue to evolve and integrate with clinical practice, we hope these tutorials will be instrumental in shaping the clinical research.
