---
drug: "Abemaciclib"
type: "drug"
salt_base: "Abemaciclib"
targets: "CDK4, CDK6"
moa_fine: "CDK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 2427
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Abemaciclib

*CDK inhibitor (inhibitor/antagonist) · targets: CDK4, CDK6 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 77 / 1347 / 2427; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.28 / 0.78.
> Flags by dose: unreliable plate only / noisy plate (z scaled) / noisy plate (z scaled). ⚠ 0.05 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:A1 | 40 / 37 | — | +0.13 | -0.1/-0.2/-1.7 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 02]]:A5 | 483 / 864 | — | +0.10 | +0.9/+0.2/+0.8 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:A5 | 924 / 1,503 | — | +0.34 | +0.7/+0.2/+2.2 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (40 genes, 40 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[MEPCE]] ⚠ 1.44× (z +4.3, 22/48 lines), [[ZNF384]] ⚠ 1.30× (z +4.2, 20/48 lines), [[SLC4A2]] ⚠ 1.33× (z +4.1, 19/48 lines), [[GPI]] ⚠ 1.32× (z +4.0, 35/47 lines), [[DTX2P1]] ⚠ 1.56× (z +3.9, 10/45 lines), [[SH3BP5-AS1]] ⚠ 1.38× (z +3.7, 8/47 lines), [[HAL]] ⚠ 1.49× (z +3.7, 2/44 lines), [[FRMD5]] ⚠ 1.21× (z +3.6, 16/38 lines), [[NEU3]] ⚠ 1.26× (z +3.6, 14/48 lines), [[PYGM]] ⚠ 1.69× (z +3.5, 20/46 lines), [[OSGIN1]] ⚠ 1.36× (z +3.5, 7/44 lines), [[POLG]] ⚠ 1.22× (z +3.5, 17/48 lines)

**0.5 µM** (483 genes, none with an alert; 12 shown): [[CLCN5]] 1.60× (z +7.0, 24/47 lines), [[KIF21A]] 1.49× (z +6.6, 38/46 lines), [[STK4]] 1.27× (z +6.4, 30/48 lines), [[GPAT3]] 1.79× (z +6.3, 31/41 lines), [[POLR3G]] 1.68× (z +6.2, 27/45 lines), [[NOC3L]] 1.55× (z +5.7, 32/48 lines), [[FKBP14]] 1.62× (z +5.6, 36/48 lines), [[URB1]] 1.59× (z +5.5, 31/48 lines), [[AP3B1]] 1.30× (z +5.5, 34/48 lines), [[HARS1]] 1.46× (z +5.5, 23/48 lines), [[WDR75]] 1.37× (z +5.5, 30/48 lines), [[XPO5]] 1.43× (z +5.4, 22/48 lines)

**5 µM** (924 genes, none with an alert; 12 shown): [[TRIB3]] 2.89× (z +7.8, 39/45 lines), [[TSR1]] 2.09× (z +7.6, 44/48 lines), [[XPO5]] 1.96× (z +7.5, 37/48 lines), [[FKBP14]] 2.35× (z +7.3, 41/48 lines), [[ATP2B1]] 1.58× (z +7.3, 27/47 lines), [[XPOT]] 1.96× (z +7.3, 44/48 lines), [[POLR3G]] 2.63× (z +7.3, 28/45 lines), [[YARS1]] 1.99× (z +7.3, 42/48 lines), [[DHX37]] 2.16× (z +7.3, 30/47 lines), [[NOC3L]] 2.14× (z +7.2, 40/48 lines), [[ZPR1]] 2.31× (z +7.1, 35/47 lines), [[FRMD5]] 2.08× (z +7.1, 25/38 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (37 genes, 37 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[TFDP2]] ⚠ 0.766× (z -8.2, 38/48 lines), [[CREBRF]] ⚠ 0.678× (z -6.0, 40/48 lines), [[CCDC28A]] ⚠ 0.680× (z -5.9, 30/48 lines), [[FBXO25]] ⚠ 0.764× (z -5.9, 22/44 lines), [[NDUFAF6]] ⚠ 0.781× (z -5.3, 25/48 lines), [[KLHL24]] ⚠ 0.726× (z -5.1, 35/48 lines), [[JMY]] ⚠ 0.732× (z -5.0, 31/47 lines), [[CRBN]] ⚠ 0.818× (z -4.3, 16/48 lines), [[CCPG1]] ⚠ 0.833× (z -4.2, 21/48 lines), [[YPEL2]] ⚠ 0.798× (z -3.8, 18/44 lines), [[NFU1]] ⚠ 0.778× (z -3.7, 13/48 lines), [[REPS2]] ⚠ 0.780× (z -3.7, 9/35 lines)

**0.5 µM** (864 genes, none with an alert; 12 shown): [[TNRC6B]] 0.528× (z -19.3, 47/48 lines), [[TFDP2]] 0.466× (z -16.8, 48/48 lines), [[PDCD4]] 0.425× (z -13.4, 46/48 lines), [[CCDC28A]] 0.399× (z -11.4, 44/48 lines), [[KLHL24]] 0.350× (z -11.0, 47/48 lines), [[RB1CC1]] 0.543× (z -10.7, 48/48 lines), [[CREBRF]] 0.409× (z -9.9, 47/48 lines), [[PLEKHM3]] 0.491× (z -9.9, 43/48 lines), [[FBXO25]] 0.477× (z -9.6, 32/44 lines), [[TCP11L2]] 0.369× (z -9.4, 47/48 lines), [[BCAS3]] 0.480× (z -9.4, 47/48 lines), [[RPS6KA5]] 0.568× (z -9.3, 37/48 lines)

**5 µM** (1503 genes, none with an alert; 12 shown): [[TFDP2]] 0.372× (z -15.9, 46/48 lines), [[FBXL20]] 0.210× (z -15.8, 48/48 lines), [[PDCD4]] 0.253× (z -15.7, 46/48 lines), [[KLHL24]] 0.144× (z -15.6, 47/48 lines), [[PLEKHM3]] 0.221× (z -15.4, 47/48 lines), [[FBXO25]] 0.263× (z -15.3, 40/43 lines), [[RB1CC1]] 0.303× (z -15.3, 48/48 lines), [[YPEL2]] 0.195× (z -14.5, 39/45 lines), [[CREBRF]] 0.186× (z -13.7, 48/48 lines), [[CCDC28A]] 0.223× (z -13.6, 45/48 lines), [[WIPI2]] 0.318× (z -13.1, 47/48 lines), [[TNRC6B]] 0.372× (z -12.7, 47/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 179]] (+2.1) | [[Module 054]] (-2.3), [[Module 045]] (-2.1) |
| 0.5 µM | [[Module 207]] (+2.6), [[Module 229]] (+2.1) | [[Module 225]] (-4.9), [[Module 076]] (-4.2), [[Module 069]] (-4.0) |
| 5 µM | [[Module 005]] (+3.4), [[Module 001]] (+3.1), [[Module 060]] (+2.9) | [[Module 069]] (-6.4), [[Module 225]] (-6.0), [[Module 145]] (-6.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SNU-1 (line)]] (1.44), [[LoVo (line)]] (1.31), [[SW48 (line)]] (1.27), [[PANC-1 (line)]] (1.26) · weakest: [[SW 1088 (line)]] (0.682), [[LOX-IMVI (line)]] (0.685), [[BT-474 (line)]] (0.721) |
| 0.5 µM | — | [[NCI-H460 (line)]] (1.38), [[MIA PaCa-2 (line)]] (1.37), [[SW48 (line)]] (1.36), [[NCI-H1792 (line)]] (1.31) · weakest: [[BT-474 (line)]] (0.700), [[LS 180 (line)]] (0.724), [[A-427 (line)]] (0.741) |
| 5 µM | [[A549 (line)]] (-6.5), [[SK-MEL-2 (line)]] (-6.2), [[NCI-H1792 (line)]] (-5.4), [[A498 (line)]] (-5.0), [[LOX-IMVI (line)]] (-4.7) | [[MIA PaCa-2 (line)]] (1.43), [[NCI-H460 (line)]] (1.38), [[NCI-H1792 (line)]] (1.37), [[Hs 766T (line)]] (1.21) · weakest: [[LS 180 (line)]] (0.660), [[C-33 A (line)]] (0.723), [[BT-474 (line)]] (0.749) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[c-Kit-IN-1 (drug)]] (+0.91, Multi-TK inhibitor); [[TAK-733 (drug)]] (+0.89, MEK inhibitor); [[EX229 (drug)]] (+0.87, unclear); [[venetoclax (drug)]] (+0.76, unclear); [[Volasertib (drug)]] (+0.64, unclear); [[Sapanisertib (drug)]] (+0.57, MTOR inhibitor); [[Belzutifan (drug)]] (+0.55, unclear); [[Everolimus (drug)]] (+0.54, MTOR inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[HOXB9]] | 5 µM | B | HOXB9 activity lowers the cells' numbers under Abemaciclib 5 µM (makes them more sensitive) | lines that do not express HOXB9 (17) vs lines expressing it (31) | the lines without HOXB9: 1.29× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: LINC02086, HOXB8; maybe low, not absent |
| [[ENSG00000275993]] | 5 µM | B | ENSG00000275993 activity raises the cells' numbers under Abemaciclib 5 µM (protects the cells) | lines that do not express ENSG00000275993 (7) vs lines expressing it (41) | the lines without ENSG00000275993: 0.70× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: GAL3ST1, LINC00571; maybe low, not absent |
| [[SLC29A4]] | 5 µM | B | SLC29A4 activity lowers the cells' numbers under Abemaciclib 5 µM (makes them more sensitive) | lines that do not express SLC29A4 (6) vs lines expressing it (42) | the lines without SLC29A4: 1.40× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[SPART-AS1]] | 5 µM | C | SPART-AS1 activity lowers the cells' numbers under Abemaciclib 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.32× the cells of the other lines | 0.026 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[C2orf74]] | 5 µM | C | C2orf74 activity lowers the cells' numbers under Abemaciclib 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.36× the cells of the other lines | 0.027 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[NR3C1]] | 5 µM | C | NR3C1 activity lowers the cells' numbers under Abemaciclib 5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.34× the cells of the other lines | 0.043 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[ENSG00000286964]] | 5 µM | C | ENSG00000286964 activity lowers the cells' numbers under Abemaciclib 5 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.36× the cells of the other lines | 0.056 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |
| [[FIGN]] | 5 µM | C | FIGN activity lowers the cells' numbers under Abemaciclib 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.29× the cells of the other lines | 0.085 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Abemaciclib"
- `tables/drugdoses.parquet` — dd in 42, 43, 44
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
