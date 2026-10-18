# Kepler452b-Sonification-Research-Code-Docs
Kepler-452b Light-Curve Sonification

This repository documents a proof-of-concept for processing 50,000+ Kepler-452b light-curve flux values and exploring how astronomical data can be translated into sound. This work is part of original research by Nitya Sharma exploring sonification as a potential complement to visual-only scientific data, particularly for blind and visually impaired audiences.

To Read Research: https://nhsjs.com/2026/barriers-in-science-lack-of-accessibility-to-visual-only-scientificdata-for-the-bvi-community-and-sonification-as-a-viable-alternativeto-data-interpretation-a-pilot-study/

Data was explored through Kaggle: Kepler-452b Exoplanet Datasets.
The exact file and flux column used in the original workflow still need to be added.

Documented Workflow
The recovered screenshots show a process that:
1. Loads flux measurements into a pandas DataFrame.
2. Groups consecutive values into windows of five and averages them.
3. Calculates deviations from a baseline value.
4. Maps those deviations to MIDI pitches.
5. Exports the notes as a MIDI file.
Disclaimer

This repository is not the complete original research code as putting all the code here is still work in progress. 

Technologies
Python · pandas · KaggleHub · Mido
