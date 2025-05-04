import os
import pandas as pd

# Define the schedule as a DataFrame
data = {
    "ClassPeriod": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 22, 23, 24, 25, 26, 27, 28
    ],
    "Topics": [
        "Syllabus", 
        "Kit of Parts", 
        "Review of Biology/Biochemistry",
        "Recombinant DNA technology",
        "Introduction to Auxin",
        "Lab orientation: Safety, Pippetting, and Aseptic technique",
        "Biological Parts (Protein expression and plasmids)", 
        "Bioinformatics: Tools for working with biological sequences",
        "Modular Cloning",
        "Hypotheses, Research Questions, and Experimental Design", 
        "Level 0 Part Plasmid Design",
        "Measuring Biology",
        "Level 1 Transcriptional Unit Design", 
        "Level 2 Multicassette Plasmid Design",
        "Finalizing Designs",
        "Opentrons Lab automation",
        "Minipreps", 
        "DNA spectrophotometry",
        "DNA Assembly Methods",
        "Setting up Level 1 Assemblies",
        "Final projects",
        "PCR primer design",
        "Gel Electrophoresis",
        "Colony PCR",
        "Genome Engineering",
        "Yeast Transformation",
        "Sequencing Analysis",
        "Flow Cytometry"
    ]
}

df = pd.DataFrame(data)

# Create the project directory structure
quarto_dir = os.path.join("chapters")
os.makedirs(quarto_dir, exist_ok=True)

# Create a Quarto markdown file for each class period
for index, row in df.iterrows():
    filename = f"{row['ClassPeriod']:02d}_{row['Topics'].split(',')[0].strip().replace(' ', '_').replace('/', '_')}.qmd"
    filepath = os.path.join(quarto_dir, filename)
    with open(filepath, "w") as f:
        f.write(f"---\ntitle: \"{row['Topics']}\"\n---\n\n")



# Create _quarto.yml and index.qmd
with open(os.path.join("_quarto.yml"), "w") as f:
#    f.write("project:\n  type: book\n\nbook:\n  title: \"Synthetic Biology Course Book\"\n  author: \"Your Name\"\n  chapters:\n")
    for index, row in df.iterrows():
        filename = f"{row['ClassPeriod']:02d}_{row['Topics'].split(',')[0].strip().replace(' ', '_').replace('/', '_')}.qmd"
        f.write(f"    - chapters/{filename}\n")

with open(os.path.join("index.qmd"), "w") as f:
    f.write("---\ntitle: \"Synthetic Biology Course Book\"\nauthor: \"Your Name\"\ndescription: \"A course-based undergraduate research experience textbook.\"\n---\n\n# Welcome\n\nThis book supports the Synthetic Biology CURE course.\n")

