---
drug: "Riluzole hydrochloride"
type: "drug"
salt_base: "Riluzole hydrochloride"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 23
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Riluzole hydrochloride

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 6 / 23 / 3; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.00 / 0.20.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:A9 | 0 / 6 | — | +0.24 | +1.4/+0.5/+0.2 | — |
| 0.5 µM | [[Plate 05]]:A9 | 18 / 5 | — | -0.28 | +0.6/+0.3/-0.0 | — |
| 5 µM | [[Plate 14]]:A9 | 2 / 1 | 0.808 | +0.39 | +1.5/+1.9/+1.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (18 genes, none with an alert; 12 shown): [[NONO]] 1.29× (z +5.4, 34/48 lines), [[CPNE1]] 1.27× (z +5.0, 31/48 lines), [[STK11]] 1.23× (z +4.3, 12/45 lines), [[PRELID3B]] 1.27× (z +4.1, 27/48 lines), [[CEP85]] 1.24× (z +4.0, 11/48 lines), [[COQ9]] 1.24× (z +3.9, 10/48 lines), [[NOLC1]] 1.35× (z +3.8, 36/48 lines), [[PMS2P3-1]] 1.57× (z +3.6, 18/47 lines), [[RAB8A]] 1.24× (z +3.4, 23/48 lines), [[CLTB]] 1.28× (z +3.4, 14/48 lines), [[MYL6B-AS1]] 1.42× (z +3.4, 3/36 lines), [[ARGLU1]] 1.20× (z +3.4, 21/48 lines)

**5 µM** (2 genes, none with an alert): [[BDH2]] 1.22× (z +3.1, 1/45 lines), [[CBR1]] 1.31× (z +3.0, 16/44 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (6 genes, none with an alert): [[RNF212]] 0.678× (z -4.4, 1/12 lines), [[TRIM15]] 0.643× (z -3.5, 0/14 lines), [[CYP3A5]] 0.796× (z -3.3, 1/16 lines), [[PTGS2]] 0.783× (z -2.9, 0/21 lines), [[LINC00862]] 0.792× (z -2.9, 11/47 lines), [[NR4A1]] 0.771× (z -2.8, 10/42 lines)

**0.5 µM** (5 genes, none with an alert): [[POLR2J3-1]] 0.692× (z -3.9, 16/43 lines), [[HAPLN3]] 0.746× (z -3.6, 11/36 lines), [[PIAS4]] 0.818× (z -3.4, 16/48 lines), [[ENSG00000290890]] 0.823× (z -2.9, 15/48 lines), [[TRIM8]] 0.833× (z -2.9, 9/46 lines)

**5 µM** (1 gene, none with an alert): [[PLXNA3]] 0.808× (z -3.4, 19/46 lines)

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
| 0.05 µM | [[NCI-H1792 (line)]] (-3.4) | — |
| 0.5 µM | — | [[HS-578T (line)]] (1.74), [[RPMI-7951 (line)]] (1.56), [[MIA PaCa-2 (line)]] (1.52), [[SW 900 (line)]] (1.47) · weakest: [[C32 (line)]] (0.405), [[SK-MEL-2 (line)]] (0.515), [[NCI-H2030 (line)]] (0.563) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Aliskiren (drug)]] (+0.55, unclear); [[Nevirapine (drug)]] (+0.53, unclear, ⚠ only 7 significant genes); [[LJI308 (drug)]] (+0.53, Other MAPK inhibitor); [[Benproperine (phosphate) (drug)]] (+0.51, unclear); [[Imiquimod (maleate) (drug)]] (+0.50, unclear); [[Orlistat (drug)]] (+0.48, unclear); [[Perindopril (erbumine) (drug)]] (+0.47, unclear); [[Docetaxel (drug)]] (+0.44, Microtubule inhibitor, ⚠ vector dose flagged: transcription drop; cell-cycle shift); [[Bosentan (hydrate) (drug)]] (+0.44, unclear); [[Erlotinib (drug)]] (+0.38, EGFR/ERBB inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 54 arrows, 54 of them with an alert ⚠; grade A 0, B 46, C 8. Shown: the 15 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[KLRC4-KLRK1]], [[KLRK1]] | 0.05 µM | B | KLRC4-KLRK1, KLRK1 activity raises the cells' numbers under Riluzole hydrochloride 0.05 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.86× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[IL15]] | 5 µM | B | IL15 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 0.86× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[KLRC3]] | 0.05 µM | B | KLRC3 activity raises the cells' numbers under Riluzole hydrochloride 0.05 µM (protects the cells) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 0.86× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[AMIGO2]] | 5 µM | B | AMIGO2 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express AMIGO2 (12) vs lines expressing it (36) | the lines without AMIGO2: 0.89× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[ABLIM3]] | 5 µM | B | ABLIM3 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express ABLIM3 (15) vs lines expressing it (33) | the lines without ABLIM3: 0.89× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[SORL1]] | 0.05 µM | B | SORL1 activity raises the cells' numbers under Riluzole hydrochloride 0.05 µM (protects the cells) | lines that do not express SORL1 (21) vs lines expressing it (27) | the lines without SORL1: 0.84× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[PCED1B]] | 5 µM | B | PCED1B activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express PCED1B (11) vs lines expressing it (37) | the lines without PCED1B: 0.87× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[CXCL3]] | 5 µM | B | CXCL3 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express CXCL3 (14) vs lines expressing it (34) | the lines without CXCL3: 0.88× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[ATP1B1]] | 5 µM | B | ATP1B1 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 0.88× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[ENSG00000251537]] | 5 µM | B | ENSG00000251537 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express ENSG00000251537 (9) vs lines expressing it (39) | the lines without ENSG00000251537: 0.89× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: FBXW10B, PCED1B, NHS; maybe low, not absent |
| [[LINC02257]] | 5 µM | B | LINC02257 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express LINC02257 (15) vs lines expressing it (33) | the lines without LINC02257: 0.90× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent |
| [[DPP4]] | 5 µM | B | DPP4 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express DPP4 (29) vs lines expressing it (19) | the lines without DPP4: 0.91× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[MAML2]] | 5 µM | B | MAML2 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express MAML2 (8) vs lines expressing it (40) | the lines without MAML2: 0.88× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[LGALS3BP]] | 5 µM | B | LGALS3BP activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.85× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[ENSG00000251584]] | 5 µM | B | ENSG00000251584 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express ENSG00000251584 (28) vs lines expressing it (20) | the lines without ENSG00000251584: 0.89× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: HPGD, HNF1A-AS1, ENSG00000267881 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Riluzole hydrochloride"
- `tables/drugdoses.parquet` — dd in 896, 897, 898
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
