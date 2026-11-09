---
drug: "Almonertinib (hydrochloride)"
type: "drug"
salt_base: "Almonertinib"
targets: "EGFR"
moa_fine: "EGFR/ERBB inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 51
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Almonertinib (hydrochloride)

*EGFR/ERBB inhibitor (inhibitor/antagonist) · targets: EGFR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 27 / 12 / 51; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.01 / 0.42.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:D7 | 7 / 20 | — | -0.36 | -0.7/-0.8/-0.4 | — |
| 0.5 µM | [[Plate 05]]:D7 | 12 / 0 | — | -0.15 | -0.8/-0.9/-0.5 | — |
| 5 µM | [[Plate 14]]:D7 | 49 / 2 | 0.512 | -0.53 | -1.7/-1.5/-0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (7 genes, none with an alert): [[ENSG00000275740]] 1.36× (z +4.1, 11/46 lines), [[ENSG00000286808]] 1.50× (z +3.9, 2/41 lines), [[ENSG00000273398]] 1.28× (z +3.7, 9/46 lines), [[ENSG00000273217]] 1.45× (z +3.5, 7/45 lines), [[SLC25A24P1]] 1.61× (z +3.4, 0/7 lines), [[ENSG00000248774]] 1.41× (z +3.1, 7/42 lines), [[ENSG00000261094]] 1.37× (z +3.0, 3/40 lines)

**0.5 µM** (12 genes, none with an alert): [[DHCR7]] 1.44× (z +3.7, 7/43 lines), [[NSMF]] 1.34× (z +3.4, 14/45 lines), [[PSG9]] 1.72× (z +3.4, 0/3 lines), [[OLFML2A]] 1.37× (z +3.4, 3/27 lines), [[ENSG00000291065]] 1.31× (z +3.4, 7/26 lines), [[SDC3]] 1.27× (z +3.3, 5/43 lines), [[MT-CO2]] 1.34× (z +3.3, 24/48 lines), [[GLB1L2]] 1.30× (z +3.2, 4/27 lines), [[MEN1]] 1.25× (z +3.1, 5/45 lines), [[ENSG00000291185]] 1.37× (z +3.1, 0/23 lines), [[ENSG00000132832]] 1.47× (z +3.1, 2/23 lines), [[ZNF702P]] 1.25× (z +2.9, 0/23 lines)

**5 µM** (49 genes, none with an alert; 12 shown): [[SCD]] 1.34× (z +5.8, 36/48 lines), [[ACAT2]] 1.25× (z +4.7, 21/48 lines), [[IDI1]] 1.28× (z +4.6, 34/48 lines), [[C12orf73]] 1.25× (z +4.5, 28/48 lines), [[PRSS51]] 1.49× (z +4.3, 1/11 lines), [[MVK]] 1.23× (z +4.1, 5/46 lines), [[FDPS]] 1.26× (z +4.0, 33/48 lines), [[COPZ2]] 1.36× (z +4.0, 6/34 lines), [[HMGCS1]] 1.26× (z +4.0, 25/47 lines), [[PCSK2]] 1.52× (z +3.9, 2/12 lines), [[LINC01203]] 1.50× (z +3.9, 1/7 lines), [[PCSK9]] 1.43× (z +3.8, 4/20 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (20 genes, none with an alert; 12 shown): [[MBD6]] 0.750× (z -4.0, 18/47 lines), [[PPP1R9B]] 0.740× (z -3.8, 22/47 lines), [[INF2]] 0.792× (z -3.8, 20/48 lines), [[TNKS1BP1]] 0.749× (z -3.7, 26/48 lines), [[KDM6B]] 0.759× (z -3.6, 27/48 lines), [[MED22]] 0.780× (z -3.6, 10/45 lines), [[CPNE7]] 0.737× (z -3.6, 11/35 lines), [[ATN1]] 0.826× (z -3.4, 21/48 lines), [[PLCB3]] 0.797× (z -3.3, 17/48 lines), [[TESK1]] 0.752× (z -3.2, 9/44 lines), [[ITPR3]] 0.784× (z -3.2, 20/42 lines), [[CYP2S1]] 0.741× (z -3.1, 10/28 lines)

**5 µM** (2 genes, none with an alert): [[NUAK2]] 0.826× (z -3.6, 9/38 lines), [[SPRY4]] 0.826× (z -3.4, 16/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 086]] (+2.5) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[J82 (line)]] (1.28), [[SW48 (line)]] (1.25), [[HS-578T (line)]] (1.16), [[SK-MEL-2 (line)]] (1.15) · weakest: [[SW 1088 (line)]] (0.0146), [[COLO 205 (line)]] (0.443), [[NCI-H23 (line)]] (0.665) |
| 0.5 µM | — | — |
| 5 µM | [[HT-29 (line)]] (-3.1) | [[SW 1088 (line)]] (1.91), [[CHP-212 (line)]] (1.64), [[H4 (line)]] (1.60), [[SW 1271 (line)]] (1.39) · weakest: [[J82 (line)]] (0.287), [[SW48 (line)]] (0.375), [[SW 900 (line)]] (0.404) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Tranilast (drug)]] (+0.72, unclear, ⚠ only 6 significant genes); [[Docetaxel (Trihydrate) (drug)]] (+0.71, Microtubule inhibitor); [[Entrectinib (drug)]] (+0.70, Other TK inhibitor); [[Vortioxetine (drug)]] (+0.69, unclear, ⚠ vector dose flagged: toxic); [[Terfenadine (drug)]] (+0.69, unclear); [[18β-Glycyrrhetinic acid (drug)]] (+0.68, unclear); [[Osimertinib (mesylate) (drug)]] (+0.67, EGFR/ERBB inhibitor); [[Almonertinib (mesylate) (drug)]] (+0.67, EGFR/ERBB inhibitor); [[Adagrasib (drug)]] (+0.66, RAS inhibitor); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.66, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 13 arrows, 13 of them with an alert ⚠; grade A 0, B 3, C 10.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[CRTAC1]] | 5 µM | B | CRTAC1 activity lowers the cells' numbers under Almonertinib (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express CRTAC1 (27) vs lines expressing it (21) | the lines without CRTAC1: 1.08× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2 |
| [[KLRC4-KLRK1]], [[KLRK1]] | 0.5 µM | B | KLRC4-KLRK1, KLRK1 activity lowers the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 1.14× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[KLRC3]] | 0.5 µM | B | KLRC3 activity lowers the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 1.13× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[NR3C1]] | 0.5 µM | C | NR3C1 activity raises the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (protects the cells) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 0.81× the cells of the other lines | 0.004 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[SIX1]] | 0.5 µM | C | SIX1 activity raises the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 0.82× the cells of the other lines | 0.014 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| [[C2orf74]] | 0.5 µM | C | C2orf74 activity raises the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (protects the cells) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 0.84× the cells of the other lines | 0.015 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[NPHS1]] | 5 µM | C | NPHS1 activity raises the cells' numbers under Almonertinib (hydrochloride) 5 µM (protects the cells) | lines that do not express NPHS1 (4) vs lines expressing it (44) | the lines without NPHS1: 0.82× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent |
| [[ENSG00000286964]] | 0.5 µM | C | ENSG00000286964 activity raises the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 0.83× the cells of the other lines | 0.024 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |
| [[SDC3]] | 5 µM | C | SDC3 activity raises the cells' numbers under Almonertinib (hydrochloride) 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.83× the cells of the other lines | 0.027 | ⚠ few lines (4 vs 46); across organs |
| [[LIFR]] | 0.5 µM | C | LIFR activity raises the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (protects the cells) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 0.84× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| [[FIGN]] | 0.5 µM | C | FIGN activity raises the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (protects the cells) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 0.86× the cells of the other lines | 0.030 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[SPART-AS1]] | 0.5 µM | C | SPART-AS1 activity raises the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 0.87× the cells of the other lines | 0.034 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[TBC1D9]] | 0.5 µM | C | TBC1D9 activity raises the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (protects the cells) | lines that do not express TBC1D9 (6) vs lines expressing it (42) | the lines without TBC1D9: 0.81× the cells of the other lines | 0.055 | ⚠ tissue-confounded; across organs; also absent: SIX1, TRPC1, MTERF1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Almonertinib (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 75, 76, 77
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
