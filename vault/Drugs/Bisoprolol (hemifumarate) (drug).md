---
drug: "Bisoprolol (hemifumarate)"
type: "drug"
salt_base: "Bisoprolol"
targets: "ADRB1"
moa_fine: "Adrenoceptor agonist"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 40
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Bisoprolol (hemifumarate)

*Adrenoceptor agonist (inhibitor/antagonist) · targets: ADRB1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 15 / 17 / 40; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.19 / 0.16.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:F5 | 10 / 5 | — | +0.00 | +0.6/+0.7/+0.5 | — |
| 0.5 µM | [[Plate 08]]:F5 | 13 / 4 | — | -0.76 | +0.1/-0.1/-0.6 | — |
| 5 µM | [[Plate 09]]:F5 | 3 / 37 | — | -0.02 | +0.6/-0.4/-0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (10 genes, none with an alert): [[EPN1]] 1.22× (z +4.1, 16/48 lines), [[ATN1]] 1.25× (z +3.6, 21/48 lines), [[NFKB2]] 1.28× (z +3.5, 23/48 lines), [[PRKACA]] 1.23× (z +3.5, 2/47 lines), [[SCAF1]] 1.23× (z +3.5, 15/47 lines), [[H2BC18]] 1.64× (z +3.3, 7/38 lines), [[SIRPA]] 1.26× (z +3.2, 3/32 lines), [[RPSA]] 1.28× (z +3.0, 12/47 lines), [[H2BC15]] 1.26× (z +2.9, 7/46 lines), [[ENSG00000288755]] 1.53× (z +2.9, 8/35 lines)

**0.5 µM** (13 genes, none with an alert; 12 shown): [[ENSG00000262831]] 1.92× (z +5.6, 19/41 lines), [[P2RX5]] 1.49× (z +3.8, 3/25 lines), [[GREB1]] 1.33× (z +3.5, 2/37 lines), [[MLX]] 1.24× (z +3.5, 10/47 lines), [[ZNF649]] 1.29× (z +3.4, 3/33 lines), [[LRRC37A3]] 1.34× (z +3.3, 6/45 lines), [[CDC25B]] 1.24× (z +3.1, 8/47 lines), [[H2BC4]] 1.39× (z +3.0, 11/47 lines), [[KCNB1]] 1.39× (z +3.0, 0/31 lines), [[LINC00298]] 1.40× (z +2.9, 1/28 lines), [[HLA-L-1]] 1.22× (z +2.9, 5/37 lines), [[H2BC15]] 1.22× (z +2.8, 5/47 lines)

**5 µM** (3 genes, none with an alert): [[ENSG00000262831]] 1.60× (z +3.9, 13/40 lines), [[PGBD4]] 1.32× (z +3.4, 6/42 lines), [[ZNF30]] 1.34× (z +3.4, 5/39 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[PEX11B]] 0.776× (z -3.9, 17/44 lines), [[SRGAP2D]] 0.742× (z -3.6, 11/33 lines), [[ZNF566]] 0.831× (z -3.2, 11/42 lines), [[LAMB2P1]] 0.706× (z -3.2, 9/41 lines), [[TRMT1]] 0.815× (z -3.1, 5/45 lines)

**0.5 µM** (4 genes, none with an alert): [[ENSG00000256083]] 0.682× (z -3.4, 10/38 lines), [[CAPN8]] 0.721× (z -3.3, 1/13 lines), [[CRLF2]] 0.645× (z -3.3, 0/11 lines), [[RHOH]] 0.701× (z -3.2, 2/21 lines)

**5 µM** (37 genes, none with an alert; 12 shown): [[NFKB2]] 0.666× (z -6.1, 45/47 lines), [[MNT]] 0.696× (z -5.4, 39/47 lines), [[BCKDHA]] 0.741× (z -5.1, 18/46 lines), [[NCKIPSD]] 0.718× (z -5.0, 26/47 lines), [[TTC9]] 0.717× (z -4.5, 3/24 lines), [[FBRS]] 0.757× (z -4.3, 24/47 lines), [[ATN1]] 0.786× (z -4.1, 26/47 lines), [[INF2]] 0.768× (z -4.1, 20/47 lines), [[RELA]] 0.757× (z -4.0, 23/47 lines), [[ST14]] 0.750× (z -3.8, 0/16 lines), [[CREB3L1]] 0.760× (z -3.8, 1/23 lines), [[ENSG00000259986]] 0.709× (z -3.8, 9/40 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[Hs 766T (line)]] (-6.2) | — |
| 0.5 µM | [[A498 (line)]] (-4.2), [[SNU-423 (line)]] (-3.9), [[HOP62 (line)]] (-3.5) | — |
| 5 µM | — | [[COLO 205 (line)]] (1.42), [[HCT15 (line)]] (1.40), [[NCI-H460 (line)]] (1.38), [[NCI-H661 (line)]] (1.37) · weakest: [[RPMI-7951 (line)]] (0.674), [[HT-29 (line)]] (0.729), [[HepG2_C3A (line)]] (0.783) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Adenosine (drug)]] (+0.83, unclear, ⚠ only 9 significant genes); [[Doxycycline (monohydrate) (drug)]] (+0.77, unclear); [[Loperamide (hydrochloride) (drug)]] (+0.71, unclear); [[Dapagliflozin (drug)]] (+0.67, Glucose transporter inhibitor); [[Vismodegib (drug)]] (+0.60, Sonic inhibitor, ⚠ only 5 significant genes); [[Ribociclib (drug)]] (+0.57, CDK inhibitor, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only; position not correctable)); [[Fenofibrate (drug)]] (+0.57, unclear); [[Brimonidine (drug)]] (+0.54, Adrenoceptor agonist); [[Dabrafenib (drug)]] (+0.54, RAF inhibitor); [[Erlotinib (drug)]] (+0.52, EGFR/ERBB inhibitor); [[MK-8353 (drug)]] (+0.49, Other MAPK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 40 arrows, 40 of them with an alert ⚠; grade A 0, B 15, C 25. Shown: the 15 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000230647]] | 0.5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Bisoprolol (hemifumarate) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.35× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[ENSG00000230615]] | 0.5 µM | B | ENSG00000230615 activity lowers the cells' numbers under Bisoprolol (hemifumarate) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.37× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.73× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[FMNL1-DT]] | 0.05 µM | B | FMNL1-DT activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express FMNL1-DT (23) vs lines expressing it (25) | the lines without FMNL1-DT: 0.87× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| [[GLIS3]] | 5 µM | B | GLIS3 activity lowers the cells' numbers under Bisoprolol (hemifumarate) 5 µM (makes them more sensitive) | lines that do not express GLIS3 (21) vs lines expressing it (27) | the lines without GLIS3: 1.19× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[DENND2C]] | 0.05 µM | B | DENND2C activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express DENND2C (10) vs lines expressing it (38) | the lines without DENND2C: 0.87× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: MSN, CAV1, RIMKLB |
| [[BEX2]] | 0.05 µM | B | BEX2 activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express BEX2 (18) vs lines expressing it (30) | the lines without BEX2: 0.83× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, BEX4, PAPLN |
| [[ENSG00000225751]] | 0.5 µM | B | ENSG00000225751 activity lowers the cells' numbers under Bisoprolol (hemifumarate) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000225751 (14) vs lines expressing it (34) | the lines without ENSG00000225751: 1.30× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: SLFN5, MMRN2, MGLL |
| [[TUBB6]] | 0.05 µM | B | TUBB6 activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express TUBB6 (11) vs lines expressing it (37) | the lines without TUBB6: 0.88× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |
| [[PROX1-AS1]] | 0.05 µM | B | PROX1-AS1 activity lowers the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (makes them more sensitive) | lines that do not express PROX1-AS1 (29) vs lines expressing it (19) | the lines without PROX1-AS1: 1.16× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1 |
| [[NLGN4X]] | 0.5 µM | B | NLGN4X activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.5 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.96× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| [[COL27A1]] | 0.5 µM | B | COL27A1 activity lowers the cells' numbers under Bisoprolol (hemifumarate) 0.5 µM (makes them more sensitive) | lines that do not express COL27A1 (12) vs lines expressing it (36) | the lines without COL27A1: 1.27× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[SRGN]] | 0.5 µM | B | SRGN activity lowers the cells' numbers under Bisoprolol (hemifumarate) 0.5 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.43× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[EPCAM]] | 0.5 µM | B | EPCAM activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.77× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[SLFN5]] | 0.5 µM | B | SLFN5 activity lowers the cells' numbers under Bisoprolol (hemifumarate) 0.5 µM (makes them more sensitive) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 1.33× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Bisoprolol (hemifumarate)"
- `tables/drugdoses.parquet` — dd in 203, 204, 205
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
