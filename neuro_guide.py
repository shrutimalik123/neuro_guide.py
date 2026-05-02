import random

def psychedelic_tutor_game():
    # 1. Therapeutic Database
    # Compound: {Target, Mechanism, Duration, Risk}
    compounds = {
        "Psilocybin": {
            "target": "Treatment-Resistant Depression",
            "receptor": "5-HT2A Agonist",
            "duration": "4-6 Hours",
            "risk": "Psychosis history"
        },
        "MDMA": {
            "target": "Severe PTSD",
            "receptor": "Serotonin Releaser",
            "duration": "3-5 Hours",
            "risk": "Hypertension"
        },
        "Ketamine": {
            "target": "Acute Suicidality",
            "receptor": "NMDA Antagonist",
            "duration": "1 Hour",
            "risk": "Dissociative addiction"
        }
    }

    # 2. Patient Profile Generation
    conditions = list(compounds.keys())
    target_compound = random.choice(conditions)
    patient_needs = compounds[target_compound]["target"]
    
    print("--- 🧠 THE NEURO-GUIDE: THERAPEUTIC SIM 🧠 ---")
    print(f"PATIENT PROFILE: Diagnosed with {patient_needs}.")
    print("Mission: Select the correct therapeutic compound and manage the session.")

    # 3. Step 1: Compound Selection
    print("\nSTEP 1: Which compound is currently in FDA clinical trials for this condition?")
    for i, name in enumerate(compounds.keys(), 1):
        print(f"{i}) {name}")
    
    choice_idx = int(input("Select (1-3): ")) - 1
    selected_name = list(compounds.keys())[choice_idx]

    if selected_name == target_compound:
        print(f"✅ CORRECT. {selected_name} is the primary candidate for {patient_needs}.")
    else:
        print(f"❌ MISMATCH. {selected_name} is typically used for {compounds[selected_name]['target']}.")
        return

    # 4. Step 2: Neuro-Logic
    print(f"\nSTEP 2: What is the primary neuro-mechanism of {selected_name}?")
    mechanism_guess = input("Mechanism: ").strip().title()
    
    if mechanism_guess in compounds[selected_name]["receptor"]:
        print(f"✅ ACCURATE. Neuroplasticity is being stimulated via {compounds[selected_name]['receptor']}.")
    else:
        print(f"⚠️ INCORRECT. The actual mechanism is {compounds[selected_name]['receptor']}.")

    # 5. Step 3: Set and Setting
    print("\nSTEP 3: The session is beginning. Choose a focus:")
    print("A) Guided Music & Eye Shades (Internal processing)")
    print("B) Bright lights & Cognitive tests (External stimulus)")
    
    setting = input("Choice (A/B): ").strip().upper()
    
    if setting == "A":
        print("🏆 BREAKTHROUGH: The patient accessed suppressed memories and achieved emotional release.")
    else:
        print("📉 DISTRACTION: The external stimuli prevented the patient from entering the 'Inner Directed' state.")

    print("\n--- SESSION CONCLUDED ---")
    print("Remember: Psychedelics are currently controlled substances and must only be used in legal, clinical frameworks.")

psychedelic_tutor_game()
