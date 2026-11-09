---
drug: "Adagrasib"
type: "drug"
salt_base: "Adagrasib"
targets: "KRAS"
moa_fine: "RAS inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 321
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Adagrasib

*RAS inhibitor (inhibitor/antagonist) · targets: KRAS · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 321 / 0 / 245; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.06 / 0.01.
> Flags by dose: position not correctable / - / -. ⚠ 0.05 µM: position not correctable (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:G10, [[Plate 10]]:H10 | 195 / 126 | 0.742 | +0.21 | +1.3/+0.6/-0.4 | ⚠ position not correctable |
| 0.5 µM | [[Plate 08]]:G10 | 0 / 0 | — | -0.23 | -1.3/-0.7/-1.0 | — |
| 5 µM | [[Plate 09]]:G10 | 195 / 50 | — | +0.52 | -1.8/-0.6/+0.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (195 genes, 195 with an alert ⚠; the drug-dose carries ⚠ position not correctable; 12 shown): [[RN7SKP71]] ⚠ 19.7× (z +37.8, 48/48 lines), [[CSNK2A2]] ⚠ 1.28× (z +26.3, 45/50 lines), [[ENSG00000290823]] ⚠ 2.06× (z +24.0, 44/47 lines), [[ALG2]] ⚠ 1.69× (z +23.7, 48/48 lines), [[CNPY3]] ⚠ 1.42× (z +23.0, 48/48 lines), [[GRINA]] ⚠ 1.66× (z +21.6, 48/48 lines), [[BMS1P2]] ⚠ 1.86× (z +21.3, 44/45 lines), [[AGPAT3]] ⚠ 1.27× (z +20.2, 37/50 lines), [[PET100]] ⚠ 1.88× (z +19.1, 47/48 lines), [[CMPK1]] ⚠ 1.24× (z +18.6, 40/50 lines), [[ATP2C2-AS1]] ⚠ 1.65× (z +18.2, 41/47 lines), [[VDAC2]] ⚠ 1.31× (z +16.9, 48/50 lines)

**5 µM** (195 genes, none with an alert; 12 shown): [[SCD]] 1.95× (z +9.1, 44/48 lines), [[IDI1]] 1.90× (z +8.2, 41/48 lines), [[ACSS2]] 1.66× (z +7.7, 30/47 lines), [[CYP51A1]] 1.59× (z +7.0, 37/47 lines), [[ACAT2]] 1.58× (z +6.4, 32/48 lines), [[NIBAN1]] 1.48× (z +6.1, 26/37 lines), [[FDPS]] 1.65× (z +6.0, 33/48 lines), [[OSTM1]] 1.35× (z +5.9, 25/48 lines), [[LPIN1]] 1.30× (z +5.7, 27/48 lines), [[IDH1]] 1.51× (z +5.6, 34/48 lines), [[MVK]] 1.51× (z +5.5, 15/47 lines), [[FADS1]] 1.65× (z +5.5, 29/41 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (126 genes, 126 with an alert ⚠; the drug-dose carries ⚠ position not correctable; 12 shown): [[ENSG00000271204]] ⚠ 0.741× (z -17.1, 41/43 lines), [[ENSG00000258757]] ⚠ 0.622× (z -15.2, 47/48 lines), [[GRIPAP1]] ⚠ 0.818× (z -15.1, 35/49 lines), [[LTB4R]] ⚠ 0.731× (z -13.7, 45/47 lines), [[RPS7]] ⚠ 0.623× (z -13.6, 48/50 lines), [[ENSG00000255422]] ⚠ 0.740× (z -13.1, 45/48 lines), [[ENSG00000290709]] ⚠ 0.671× (z -12.6, 44/47 lines), [[ENSG00000290921]] ⚠ 0.768× (z -12.0, 45/48 lines), [[EBLN2]] ⚠ 0.745× (z -11.9, 45/48 lines), [[ENSG00000283765]] ⚠ 0.676× (z -11.8, 38/48 lines), [[PKD1P6]] ⚠ 0.808× (z -11.8, 33/48 lines), [[ENSG00000228886]] ⚠ 0.683× (z -11.7, 43/48 lines)

**5 µM** (50 genes, none with an alert; 12 shown): [[NUAK2]] 0.665× (z -5.2, 12/38 lines), [[GLB1L2]] 0.699× (z -4.3, 5/28 lines), [[DLC1]] 0.831× (z -4.1, 11/34 lines), [[POMGNT1]] 0.802× (z -3.9, 9/48 lines), [[FANCL]] 0.826× (z -3.6, 15/48 lines), [[DPY19L3-DT]] 0.620× (z -3.6, 10/40 lines), [[HSPG2]] 0.819× (z -3.6, 17/46 lines), [[POLA2]] 0.814× (z -3.5, 5/48 lines), [[LINC02458]] 0.679× (z -3.5, 9/45 lines), [[SARDH]] 0.630× (z -3.5, 4/21 lines), [[CORO1C]] 0.781× (z -3.5, 32/48 lines), [[DDAH1]] 0.805× (z -3.5, 19/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 179]] (+4.4), [[Module 168]] (+3.0), [[Module 146]] (+2.7) | [[Module 077]] (-3.2), [[Module 229]] (-3.1), [[Module 021]] (-2.8) |
| 0.5 µM | — | — |
| 5 µM | [[Module 086]] (+3.9), [[Module 133]] (+2.5), [[Module 043]] (+2.4) | [[Module 179]] (-2.4), [[Module 006]] (-2.2), [[Module 020]] (-2.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[NCI-H1792 (line)]] (-5.5) | [[NCI-H1573 (line)]] (1.08), [[SW 900 (line)]] (1.07), [[A-427 (line)]] (1.06), [[J82 (line)]] (1.05) · weakest: [[NCI-H596 (line)]] (0), [[NCI-H2122 (line)]] (0.516), [[SW 1088 (line)]] (0.664) |
| 0.5 µM | [[HOP62 (line)]] (-4.6), [[NCI-H23 (line)]] (-3.8), [[NCI-H1792 (line)]] (-3.4) | — |
| 5 µM | [[NCI-H23 (line)]] (-5.2), [[NCI-H1792 (line)]] (-4.7), [[CHP-212 (line)]] (-3.5) | [[HOP62 (line)]] (1.77), [[NCI-H23 (line)]] (1.52), [[NCI-H2030 (line)]] (1.32), [[hTERT-HPNE (line)]] (1.30) · weakest: [[SHP-77 (line)]] (0.527), [[NCI-H2347 (line)]] (0.603), [[SW 1088 (line)]] (0.630) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Almonertinib (hydrochloride) (drug)]] (+0.66, EGFR/ERBB inhibitor); [[Terfenadine (drug)]] (+0.65, unclear); [[Tolcapone (drug)]] (+0.65, unclear, ⚠ only 6 significant genes); [[Entrectinib (drug)]] (+0.59, Other TK inhibitor); [[Almonertinib (mesylate) (drug)]] (+0.55, EGFR/ERBB inhibitor); [[Sulfatinib (drug)]] (+0.55, Multi-TK inhibitor); [[Chlorhexidine (diacetate) (drug)]] (+0.55, unclear); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.54, unclear); [[Hydroxyfasudil (drug)]] (+0.51, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 40 arrows, 40 of them with an alert ⚠; grade A 0, B 19, C 21. Shown: the 15 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000232884]] | 5 µM | B | ENSG00000232884 activity raises the cells' numbers under Adagrasib 5 µM (protects the cells) | lines that do not express ENSG00000232884 (12) vs lines expressing it (36) | the lines without ENSG00000232884: 0.80× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, NRIP1, ATXN1; maybe low, not absent |
| [[PLBD1]] | 5 µM | B | PLBD1 activity lowers the cells' numbers under Adagrasib 5 µM (makes them more sensitive) | lines that do not express PLBD1 (24) vs lines expressing it (24) | the lines without PLBD1: 1.21× the cells of the other lines | 0.059 | ⚠ within organs, on part of the lines; also absent: PLBD1-AS1, LINC01357, IKZF3 |
| [[ENSG00000230615]] | 0.5 µM | B | ENSG00000230615 activity lowers the cells' numbers under Adagrasib 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.25× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[SRGN]] | 0.5 µM | B | SRGN activity lowers the cells' numbers under Adagrasib 0.5 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.32× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[PCED1B]] | 5 µM | B | PCED1B activity raises the cells' numbers under Adagrasib 5 µM (protects the cells) | lines that do not express PCED1B (11) vs lines expressing it (37) | the lines without PCED1B: 0.79× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Adagrasib 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.80× the cells of the other lines | 0.067 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[ENSG00000230647]] | 0.5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Adagrasib 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.23× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[IKZF3]] | 5 µM | B | IKZF3 activity lowers the cells' numbers under Adagrasib 5 µM (makes them more sensitive) | lines that do not express IKZF3 (31) vs lines expressing it (17) | the lines without IKZF3: 1.15× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| [[SPOCK1]] | 0.5 µM | B | SPOCK1 activity lowers the cells' numbers under Adagrasib 0.5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.28× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity lowers the cells' numbers under Adagrasib 0.5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.26× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[AMIGO2]] | 5 µM | B | AMIGO2 activity raises the cells' numbers under Adagrasib 5 µM (protects the cells) | lines that do not express AMIGO2 (12) vs lines expressing it (36) | the lines without AMIGO2: 0.81× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[NRIP1]] | 5 µM | B | NRIP1 activity raises the cells' numbers under Adagrasib 5 µM (protects the cells) | lines that do not express NRIP1 (8) vs lines expressing it (40) | the lines without NRIP1: 0.78× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[IGFBP4]] | 5 µM | B | IGFBP4 activity raises the cells' numbers under Adagrasib 5 µM (protects the cells) | lines that do not express IGFBP4 (19) vs lines expressing it (29) | the lines without IGFBP4: 0.85× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: SDR16C5, TNFRSF1B, TSPAN15 |
| [[ENSG00000225647]] | 5 µM | B | ENSG00000225647 activity raises the cells' numbers under Adagrasib 5 µM (protects the cells) | lines that do not express ENSG00000225647 (10) vs lines expressing it (38) | the lines without ENSG00000225647: 0.82× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: BTBD6, CPA6; maybe low, not absent |
| [[TLE4]] | 5 µM | B | TLE4 activity raises the cells' numbers under Adagrasib 5 µM (protects the cells) | lines that do not express TLE4 (10) vs lines expressing it (38) | the lines without TLE4: 0.80× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[KRAS]] | [[MFSD2A]] | does not move it that way (the class's other compounds do) | B | KRAS activity raises MFSD2A's level | compounds that target KRAS: 3 of 4 lower it (BI-3406, Lonafarnib, RMC-6236) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

## Data

- `tables/drugs.parquet` — drug == "Adagrasib"
- `tables/drugdoses.parquet` — dd in 54, 55, 56
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
