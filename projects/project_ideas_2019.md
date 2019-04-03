# Project ideas for the 2019 workshop

## Fastq quality filter (keep reads paired)

Fastq files are the files output by most whole genome sequencers. The first
step in most genome sequencing pipelines is to filter these reads by quality.
Calculate the average quality of each read (see the Wikipedia page for fastq
files), and filter read _pairs_ by quality, making sure to keep pairs matched
in terms of order in a pair of .fastq files.

## Implement a sequencing pipeline

Sequencing pipelines are somewhat standardized, and usually consist of:
1. read filtering (trimmomatic, fastq -> fastq)
2. read alignment to the reference (bwa, fastq -> sam/bam)
3. variant calling (GATK, sam/bam -> vcf)

Implement a pipeline like this using the `subprocess.run()` command in python.

## Sorting genes by ontology groups, then finding correlations with a variable

Many genomic analyses require comparison and correlation of genes. Write a program that does the following:

1. Take as input a tab-separated file containing gene names, associated gene ontology groups, and a variable of interest
2. Group genes into gene ontology groups, and print out genes organized by group.
3. Identify associations with the variable, both by correlation and ANOVA.

## parse gff, get coding sequence, cross-analyze with vcf

A gff file contains information about features, like genes, in the genome. Write a program that does the following:

1. parse the gff file
2. compare the gff file with the reference genome, extract the gene sequences from the gff, and print.
3. Compare the gff file with a VCF file, and identify genes that have a polymorphism that introduces a stop codon, a nonsynonymous coding change, or a synonymous change. Print these.
