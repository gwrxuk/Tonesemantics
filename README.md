# Tonesemantics: Computational Analysis of Tonal Emergence

## Research Scope
**Tonesemantics** investigates the historical formation and evolution of the Western tonal system using interdisciplinary approaches from Artificial Intelligence, Music Informatics, and Historical Musicology. The project models the transition from modal polyphony to functional tonality and its subsequent expansion, covering a broad historical range from the 13th to the 21st century.

## Core Research Goals
1.  **Multimodal Corpus Development**: Curating and encoding a substantial dataset of scores spanning Medieval to Contemporary eras.
2.  **Cognitive & Theoretical Agents**: Designing autonomous agents capable of learning and analyzing harmonic syntax and contrapuntal rules across different stylistic periods.
3.  **Neural Music Modeling**: Utilizing state-of-the-art architectures (Transformers, LLMs) to capture long-term dependencies and generative grammar in symbolic music.

## Technical Components
*   **Symbolic Processing**: Robust pipelines for parsing and normalizing MusicXML, MIDI, and MEI data formats.
*   **Computational Theory**: Algorithms implementing formal music theory concepts (e.g., Roman Numeral Analysis, voice-leading schemata).
*   **Audio Signal Analysis**: Complementary analysis of audio recordings to extract harmonic and rhythmic features (e.g., Chromagrams, Tonnetz trajectories).

## Repository Organization
*   `src/`: Primary codebase.
    *   `data_loader.py`: Ingestion logic for symbolic and audio data.
    *   `agents.py`: Framework for analytic agents (e.g., HarmonicAgent, CounterpointAgent).
    *   `models.py`: Neural network implementations (Custom Transformers, Embeddings).
    *   `harmonic_analysis.py`: Rule-based and statistical analysis modules.
    *   `audio_analysis.py`: Signal processing tools for audio feature extraction.
*   `data/`: Storage for corpora and derived datasets.
*   `analysis/`: Human-readable analysis reports and logs.
*   `result/`: Machine-readable analysis outputs (JSON).
*   `example/`: Sample scripts and analysis outputs (e.g., `run_analysis.py`).
*   `notebooks/`: Research experiments and data visualizations.
*   **Root Scripts**:
    *   `generate_samples.py`: Generates basic tonal progression samples.
    *   `generate_historical_samples.py`: Generates historical style samples (13th-21st century).
    *   `batch_analysis.py`: Runs mass analysis on all MIDI files in `data/`.

## Usage
1.  **Generate Data**:
    ```bash
    python3 generate_samples.py
    python3 generate_historical_samples.py
    ```
2.  **Run Analysis**:
    ```bash
    python3 batch_analysis.py
    ```
3.  **View Results**: Check the `analysis/` folder for text reports and `result/` for JSON data.

## Dataset Mapping
The following table maps the generated sample files in `data/` to their corresponding analysis outputs.

| Input File (`data/`) | Analysis Report (`analysis/`) | JSON Result (`result/`) | Description |
| :--- | :--- | :--- | :--- |
| `century_13_medieval.mid` | `century_13_medieval_analysis.txt` | `century_13_medieval_result.json` | 13th Century: Organum style (Parallel 5ths). |
| `century_14_ars_nova.mid` | `century_14_ars_nova_analysis.txt` | `century_14_ars_nova_result.json` | 14th Century: Ars Nova (Landini Cadence). |
| `century_15_renaissance.mid` | `century_15_renaissance_analysis.txt` | `century_15_renaissance_result.json` | 15th Century: Early Renaissance (Triadic harmony). |
| `century_16_high_renaissance.mid` | `century_16_high_renaissance_analysis.txt` | `century_16_high_renaissance_result.json` | 16th Century: High Polyphony (Palestrina style). |
| `century_17_baroque.mid` | `century_17_baroque_analysis.txt` | `century_17_baroque_result.json` | 17th Century: Baroque (Basso Continuo/Sequence). |
| `century_18_classical.mid` | `century_18_classical_analysis.txt` | `century_18_classical_result.json` | 18th Century: Classical (Functional Cadence). |
| `century_19_romantic.mid` | `century_19_romantic_analysis.txt` | `century_19_romantic_result.json` | 19th Century: Romantic (Chromaticism). |
| `century_20_modern.mid` | `century_20_modern_analysis.txt` | `century_20_modern_result.json` | 20th Century: Modern (Whole Tone/Atonal). |
| `century_21_contemporary.mid` | `century_21_contemporary_analysis.txt` | `century_21_contemporary_result.json` | 21st Century: Contemporary (Pop/Loop-based). |
| `sample_01_c_major.mid` | `sample_01_c_major_analysis.txt` | `sample_01_c_major_result.json` | Basic I-IV-V-I progression in C Major. |
| `sample_02_a_minor.mid` | `sample_02_a_minor_analysis.txt` | `sample_02_a_minor_result.json` | Minor key progression (i-iv-V7-i) in A Minor. |
| `sample_03_g_major.mid` | `sample_03_g_major_analysis.txt` | `sample_03_g_major_result.json` | Standard progression (I-vi-ii-V-I) in G Major. |
| `sample_04_f_major.mid` | `sample_04_f_major_analysis.txt` | `sample_04_f_major_result.json` | Progression with inversion (I-V6/5-I-IV-I) in F Major. |
| `sample_05_d_minor.mid` | `sample_05_d_minor_analysis.txt` | `sample_05_d_minor_result.json` | Minor key with diminished chord (i-VI-ii°-V-i) in D Minor. |

## Environment & Requirements
*   **Runtime**: Python 3.8+
*   **Symbolic Library**: `music21`, `pretty_midi`
*   **Audio Library**: `librosa`, `soundfile`
*   **Machine Learning**: `torch` (PyTorch), `transformers` (Hugging Face)
*   **Data Science**: `numpy`, `pandas`, `scikit-learn`
