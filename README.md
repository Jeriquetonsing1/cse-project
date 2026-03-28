# Simple Disease Detection System

A lightweight Python program that suggests possible diseases based on a user’s symptoms. The tool compares the entered symptoms against a predefined knowledge base of diseases and their common symptoms, then returns a ranked list of possible conditions with match percentages.

## Brief Description

This project is a simple command-line application designed to help users quickly see which diseases from a built-in dataset match their reported symptoms. It uses a basic matching algorithm to calculate the percentage of symptoms that overlap with each disease. The program is **not** a medical diagnostic tool—it is meant for educational and informational purposes only.

## How It Works

1. **Data Storage**
   A dictionary (`disease_data`) maps disease names to a list of their typical symptoms.

2. **User Input**
   The user enters a comma‑separated list of symptoms. The input is cleaned and converted to lowercase.

3. **Matching Algorithm**
   For each disease:
   - The program counts how many of the user’s symptoms appear in the disease’s symptom list.
   - A match percentage is calculated as:
     `(matched_symptoms_count / total_symptoms_for_disease) * 100`.
   - Only diseases with at least one matching symptom are included in the results.

4. **Results**
   Diseases are sorted by match percentage (highest first). For each, the program displays:
   - Disease name
   - Match percentage
   - List of matched symptoms

5. **Output**
   The user sees a ranked list of possible diseases and the most likely one based solely on symptom overlap.

## Key Objectives

- **Educational Purpose** – Demonstrate a simple symptom‑matching algorithm and how a basic expert system can be structured in Python.
- **Command‑Line Interface** – Provide a straightforward, no‑dependencies tool that anyone can run locally.
- **Extensible Design** – The `disease_data` dictionary can be easily updated with more diseases or symptoms.
- **Transparency** – The program clearly states that it is not a substitute for professional medical advice.

## Usage

1. Clone the repository.
2. Run the script:
   ```bash
   python disease_detector.py
