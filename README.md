# 🧠 Know Your Therapeutic Psychedelics - The Neuro-Guide

A clinical simulation designed to teach the fundamentals of psychedelic-assisted therapy and neurobiology. You play as a Clinical Facilitator responsible for matching patients with the appropriate breakthrough treatment based on FDA clinical trial data. You must navigate compound selection, receptor-site logic, and the management of "Set and Setting" to facilitate a safe, therapeutic experience.

This project focuses on teaching:
* **Neuropharmacology:** Understanding the different pathways of compounds, such as 5-HT2A Agonists (Psilocybin) vs. NMDA Antagonists (Ketamine).
* **Clinical Indications:** Learning which substances are currently being researched for specific conditions like PTSD, TRD, and Acute Suicidality.
* **Psychological Frameworks:** Implementing the "Set and Setting" theory as a critical component of the therapeutic outcome.
* **Safety Protocols:** Recognizing risks and contraindications (such as psychosis history or hypertension) in a clinical environment.

---

## ✨ Features

* **Evidence-Based Compound Library:** Features a data-driven look at Psilocybin, MDMA, and Ketamine based on modern clinical research.
* **Mechanism Validation:** Challenges the player to identify the molecular targets of each compound (e.g., Serotonin Releasers vs. Receptors Agonists).
* **Set and Setting Logic:** A decision-based branch that determines the quality of the "Breakthrough" based on the clinical environment.
* **Medical Contextualization:** Provides clear distinctions between recreational use and the highly structured "Inner Directed" clinical model.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `neuro_guide.py`.
2.  **Open Terminal:** Navigate to the folder containing the file.
3.  **Run the Script:**
    ```bash
    python neuro_guide.py
    ```

### 3. Gameplay Instructions
1.  **Assess the Patient:** Read the diagnosis (e.g., "Severe PTSD").
2.  **Select the Compound:** Choose the substance currently being studied for that specific condition.
3.  **Identify the Mechanism:** Type in the primary receptor or action (e.g., "5-HT2A" or "Serotonin Releaser").
4.  **Manage the Setting:** Choose the environmental parameters (Music, Lighting, Support) to ensure a therapeutic result.



---

## 🧠 Code Structure Highlights

### Pharmacological Mapping
The game uses a nested dictionary to store technical data. This allows for strict validation of the "Why" (Mechanism) and the "What" (Target Condition) during the player's audit.

```python
compounds = {
    "Psilocybin": {
        "target": "Treatment-Resistant Depression",
        "receptor": "5-HT2A Agonist",
        # ...
    }
}

