# PDF to Database Extraction Project

## Project Overview

This project is focused on the development of an efficient program to process and extract data from a database of PDF files. Each PDF file contains several pages of structured content, specifically taxonomies and associated companies listed under each category.

## Task Description

Your task is to create a program that can:

1. Process each PDF file programmatically.
2. Extract data while preserving the inherent structure of taxonomies and associated companies.
3. Convert the extracted content into a well-organized database format that reflects the taxonomy and company relationships as represented in the PDFs.

## Example PDF Structure

The structure of the data in the PDFs is as follows:

- **Taxonomy**: Each page contains a clear taxonomy categorization.
- **Companies**: Under each taxonomy category, there are multiple companies listed.

## Requirements

- The program should handle multiple pages within each PDF file efficiently.
- Ensure the integrity and accuracy of the extracted data.
- The final database should be in a format that allows easy querying and manipulation of the extracted data.

## Getting Started

Python 3.6+
Camelot-py (pip install camelot-py)
Pandas (pip install pandas)
