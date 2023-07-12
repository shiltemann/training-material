---
layout: tutorial_hands_on

title: "Database generation"
edam_ontology: ["topic_0121"]
zenodo_link: "https://doi.org/10.5281/zenodo.839701"
questions:
  - "Where can I download microbiome database from?"
  - "How can I reduce the size of the database?"
objectives:
  - "Dabatabase generation and reduce the size of the database"
time_estimation: "2h"
key_points:
  - "Use dataset collections"
  - "With SearchGUI and PeptideShaker you can gain access to multiple search engines"
  - "Learning the basics of SQL queries can pay off"
contributors:
  - subinamehta
  - dechenbhuming
subtopic: clincal-metaproteomics
tags: [microbiome]
---
---

In this metaproteomics tutorial we will identify expressed proteins from a complex bacterial community sample.
For this MS/MS data will be matched to peptide sequences provided through a FASTA file.

Metaproteomics is the large-scale characterization of the entire protein complement of environmental microbiota
at a given point in time. It has the potential to unravel the mechanistic details of microbial interactions with
the host / environment by analyzing the functional dynamics of the microbiome.

In this tutorial, we will analyze a sample of sea water that was collected in August of 2013 from the Bering
Strait chlorophyll maximum layer (7m depth, 65° 43.44″ N, 168° 57.42″ W). The data were originally published in {% cite May_2016 %}.

> <agenda-title></agenda-title>
>
> In this tutorial, we will deal with:
>
> 1. TOC
> {:toc}
>
{: .agenda}

# Pretreatments

## Data upload

There are three ways to upload your data.

*   Upload/Import the files from your computer
*   Using a direct link
*   Import from the data library if your instance provides the files

In this tutorial, we will get the data from Zenodo: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.839701.svg)](https://doi.org/10.5281/zenodo.839701).

> <hands-on-title>Data upload and organization</hands-on-title>
>
> 1. Create a new history and name it something meaningful (e.g. *Metaproteomics tutorial*)
>
>    {% snippet faqs/galaxy/histories_create_new.md %}
>
>    {% snippet faqs/galaxy/histories_rename.md %}
>
> 2. Import the three MGF MS/MS files and the FASTA sequence file from Zenodo.
>
>    {% snippet faqs/galaxy/datasets_import_via_link.md %}
>    ```
>    https://zenodo.org/record/839701/files/2016_Jan_12_QE2_45.mgf
>    https://zenodo.org/record/839701/files/2016_Jan_12_QE2_46.mgf
>    https://zenodo.org/record/839701/files/2016_Jan_12_QE2_47.mgf
>    https://zenodo.org/record/839701/files/FASTA_Bering_Strait_Trimmed_metapeptides_cRAP.fasta
>    https://zenodo.org/record/839701/files/Gene_Ontology_Terms.tabular
>    ```
>
>    As default, Galaxy takes the link as name.
>
>    > <comment-title></comment-title>
>    > - Rename the datasets to a more descriptive name
>    {: .comment}
>
> 3. Build a **Dataset list** for the three MGF files
>
>    {% snippet faqs/galaxy/collections_build_list.md %}
>
{: .hands_on}

We have a choice to run all these steps using a single workflow, then discuss each step and the results in more detail.

> <hands-on-title>Pretreatments</hands-on-title>
>
> 1. **Import the workflow** into Galaxy:
>
>    {% snippet faqs/galaxy/workflows_run_trs.md path="topics/proteomics/tutorials/metaproteomics/workflows/workflow.ga" title="Pretreatments" %}
>
> 2. Run **Workflow** {% icon workflow %} using the following parameters:
>    - *"Send results to a new history"*: `No`
>    - {% icon param-file %} *"1: SixGill generated protein fasta file"*: `FASTA_Bering_Strait_Trimmed_metapeptides_cRAP.fasta`
>    - {% icon param-file %} *"2: Dataset collection of Bering Strait MGF files"*: `Dataset collection of bering MGF`
>    - {% icon param-file %} *"3: GeneOntology terms (selected)"*: `Gene_Ontology_terms.tabular`
>
>    {% snippet faqs/galaxy/workflows_run.md %}
>
{: .hands_on}
