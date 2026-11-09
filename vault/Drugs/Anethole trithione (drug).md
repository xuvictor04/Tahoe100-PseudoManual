---
drug: "Anethole trithione"
type: "drug"
salt_base: "Anethole trithione"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 211
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Anethole trithione

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 11 / 211 / 193; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.60 / 0.60.
> Flags by dose: - / - / cell-cycle shift. ⚠ 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:H8 | 6 / 5 | — | +0.42 | -0.9/-2.3/-2.3 | — |
| 0.5 µM | [[Plate 05]]:H8 | 22 / 189 | — | +0.78 | -0.9/-2.7/-2.6 | — |
| 5 µM | [[Plate 14]]:H8 | 38 / 155 | 0.817 | -0.09 | -1.5/-4.6/-2.5 | ⚠ cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (6 genes, 2 with an alert ⚠): [[NF2]] ⚠ 1.22× (z +4.6, 14/47 lines; position correction uncertain), [[ACOT7]] ⚠ 1.23× (z +4.5, 13/46 lines; position correction uncertain), [[STK11IP]] 1.28× (z +3.9, 3/48 lines), [[PLD2]] 1.21× (z +3.2, 1/48 lines), [[ENSG00000259723]] 1.27× (z +3.2, 5/26 lines), [[CRYZL2P]] 1.36× (z +3.0, 4/34 lines)

**0.5 µM** (22 genes, 2 with an alert ⚠; 14 shown): [[NF2]] ⚠ 1.24× (z +5.1, 19/47 lines; position correction uncertain), [[DENND4C]] 1.21× (z +4.3, 25/48 lines), [[ACOT7]] ⚠ 1.20× (z +4.0, 10/46 lines; position correction uncertain), [[IL6ST]] 1.24× (z +3.9, 30/48 lines), [[ZZZ3]] 1.22× (z +3.8, 32/48 lines), [[STON2]] 1.27× (z +3.5, 7/29 lines), [[SYS1-DBNDD2]] 1.32× (z +3.5, 6/48 lines), [[ETNK1]] 1.21× (z +3.4, 22/48 lines), [[ZNF410]] 1.29× (z +3.4, 19/48 lines), [[POLA1]] 1.25× (z +3.4, 20/48 lines), [[KAT7]] 1.26× (z +3.3, 16/48 lines), [[TENT2]] 1.21× (z +3.3, 27/48 lines), [[GDAP2]] 1.22× (z +3.3, 15/48 lines), [[MFSD14A]] 1.22× (z +3.2, 13/48 lines)

**5 µM** (38 genes, 29 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 18 shown): [[NF2]] ⚠ 1.22× (z +6.6, 20/47 lines; position correction uncertain; cell-cycle shift (explains ~0% here)), [[SLC18B1]] ⚠ 1.31× (z +5.5, 15/42 lines; cell-cycle shift, explains ~21% of this change), [[MTX2]] ⚠ 1.22× (z +5.3, 26/48 lines; cell-cycle shift, explains ~30% of this change), [[SEC31B]] ⚠ 1.25× (z +5.1, 14/47 lines; cell-cycle shift, explains ~17% of this change), [[FIGN]] 1.26× (z +4.9, 15/32 lines; cell-cycle shift (explains ~0% here)), [[PRUNE1]] ⚠ 1.23× (z +4.6, 14/48 lines; cell-cycle shift, explains ~18% of this change), [[MRS2]] ⚠ 1.22× (z +4.5, 15/48 lines; cell-cycle shift, explains ~14% of this change), [[ANO9]] 1.31× (z +4.3, 10/26 lines; cell-cycle shift (explains ~0% here)), [[CDH26]] ⚠ 1.38× (z +4.1, 7/41 lines; cell-cycle shift, explains ~38% of this change), [[ENSG00000284773]] ⚠ 1.36× (z +4.0, 5/44 lines; cell-cycle shift, explains ~22% of this change), [[GLRB]] ⚠ 1.23× (z +3.9, 7/27 lines; cell-cycle shift, explains ~21% of this change), [[ARRDC3]] 1.27× (z +3.9, 29/48 lines; cell-cycle shift (explains ~0% here)), [[AGAP13P]] 1.34× (z +3.9, 1/44 lines; cell-cycle shift (explains ~17% here)), [[PFKFB4]] 1.23× (z +3.8, 23/48 lines; cell-cycle shift (explains ~2% here)), [[PDK1]] 1.25× (z +3.6, 37/48 lines; cell-cycle shift (explains ~5% here)), [[PER1]] 1.37× (z +3.5, 25/47 lines; cell-cycle shift (explains ~0% here)), [[FLVCR2]] 1.30× (z +3.0, 11/42 lines; cell-cycle shift (explains ~5% here)), [[SLC16A4-AS1]] 1.28× (z +2.9, 5/45 lines; cell-cycle shift (explains ~4% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[TRAPPC3]] 0.789× (z -3.6, 15/48 lines), [[ORMDL2]] 0.742× (z -3.4, 14/47 lines), [[SMIM29]] 0.658× (z -3.3, 14/47 lines), [[KCNJ14]] 0.771× (z -3.0, 5/48 lines), [[CDKN3]] 0.737× (z -3.0, 12/47 lines)

**0.5 µM** (189 genes, none with an alert; 12 shown): [[ENSG00000286481]] 0.624× (z -5.6, 0/11 lines), [[ENSG00000266302]] 0.672× (z -5.1, 0/16 lines), [[SKAP1]] 0.709× (z -5.0, 0/14 lines), [[USH1C]] 0.655× (z -5.0, 0/14 lines), [[FAM50A]] 0.668× (z -4.8, 37/48 lines), [[NOP56]] 0.628× (z -4.5, 42/48 lines), [[ADD2]] 0.749× (z -4.4, 0/17 lines), [[NCAM1]] 0.671× (z -4.4, 0/14 lines), [[ENSG00000267327]] 0.642× (z -4.4, 0/12 lines), [[NUDT4]] 0.777× (z -4.3, 25/48 lines), [[WBP4]] 0.748× (z -4.3, 30/48 lines), [[SOX11]] 0.555× (z -4.3, 0/11 lines)

**5 µM** (155 genes, 82 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 18 shown): [[MYH9]] 0.723× (z -7.0, 46/47 lines; cell-cycle shift (explains ~10% here)), [[SPDL1]] ⚠ 0.715× (z -5.7, 39/45 lines; cell-cycle shift, explains ~41% of this change), [[MAP7D1]] ⚠ 0.805× (z -5.5, 28/48 lines; cell-cycle shift, explains ~13% of this change), [[CHD4]] ⚠ 0.820× (z -5.2, 31/48 lines; cell-cycle shift, explains ~30% of this change), [[NOP14]] ⚠ 0.811× (z -5.2, 27/48 lines; cell-cycle shift, explains ~26% of this change), [[WNT2B]] 0.716× (z -5.0, 39/48 lines; cell-cycle shift (explains ~0% here)), [[GCC1]] 0.796× (z -4.9, 18/48 lines; cell-cycle shift (explains ~0% here)), [[CAP1]] ⚠ 0.805× (z -4.9, 36/48 lines; cell-cycle shift, explains ~22% of this change), [[POLR1G]] 0.651× (z -4.9, 27/48 lines; cell-cycle shift (explains ~20% here)), [[NPAS1]] 0.738× (z -4.8, 13/38 lines; cell-cycle shift (explains ~1% here)), [[CAVIN1]] ⚠ 0.761× (z -4.8, 39/42 lines; cell-cycle shift, explains ~36% of this change), [[NABP1]] 0.753× (z -4.7, 37/44 lines; cell-cycle shift (explains ~0% here)), [[CHMP7]] 0.800× (z -4.7, 26/48 lines; cell-cycle shift (explains ~5% here)), [[MYH14]] 0.806× (z -4.7, 7/27 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000266302]] 0.774× (z -4.6, 0/16 lines; cell-cycle shift (explains ~0% here)), [[PJA1]] 0.779× (z -4.6, 12/48 lines; cell-cycle shift (explains ~0% here)), [[SGSM3-AS1]] 0.681× (z -4.5, 13/44 lines; cell-cycle shift (explains ~0% here)), [[PRECSIT]] 0.669× (z -4.5, 9/37 lines; cell-cycle shift (explains ~0% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 029]] (+2.7), [[Module 020]] (+2.1) | [[Module 002]] (-2.9) |
| 5 µM | [[Module 146]] (+3.6), [[Module 179]] (+3.0), [[Module 065]] (+2.9) | [[Module 060]] (-2.2), [[Module 160]] (-2.2), [[Module 002]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[NCI-H2347 (line)]] (-3.1) | [[SW 1271 (line)]] (1.85), [[SW 1088 (line)]] (1.82), [[SNU-1 (line)]] (1.79), [[NCI-H661 (line)]] (1.69) · weakest: [[NCI-H2347 (line)]] (0.762), [[NCI-H1573 (line)]] (0.800), [[CFPAC-1 (line)]] (0.810) |
| 5 µM | — | [[SW 1088 (line)]] (1.30), [[AN3 CA (line)]] (1.26), [[SHP-77 (line)]] (1.24), [[COLO 205 (line)]] (1.17) · weakest: [[NCI-H1573 (line)]] (0.863), [[NCI-H460 (line)]] (0.883), [[A-172 (line)]] (0.914) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Erlotinib (drug)]] (+0.80, EGFR/ERBB inhibitor); [[Benproperine (phosphate) (drug)]] (+0.80, unclear); [[Tucatinib (drug)]] (+0.78, EGFR/ERBB inhibitor); [[Rutin (trihydrate) (drug)]] (+0.78, unclear); [[Lucanthone (drug)]] (+0.77, unclear); [[Fenofibrate (drug)]] (+0.77, unclear); [[Paclitaxel (drug)]] (+0.74, Microtubule inhibitor, ⚠ only 3 significant genes); [[MK-8353 (drug)]] (+0.72, Other MAPK inhibitor); [[Encorafenib (drug)]] (+0.72, RAF inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 46 arrows, 46 of them with an alert ⚠; grade A 0, B 6, C 40. Shown: the 15 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000259200]] | 0.5 µM | B | ENSG00000259200 activity raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | lines that do not express ENSG00000259200 (18) vs lines expressing it (30) | the lines without ENSG00000259200: 0.86× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, CSGALNACT1, ENSG00000232692; maybe low, not absent |
| [[ERC2]] | 0.5 µM | B | ERC2 activity raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | lines that do not express ERC2 (20) vs lines expressing it (28) | the lines without ERC2: 0.93× the cells of the other lines | 0.070 | ⚠ within organs, on part of the lines; also absent: VAT1L, LDOC1, SNAP91; maybe low, not absent |
| [[LINC00922]] | 0.5 µM | B | LINC00922 activity raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | lines that do not express LINC00922 (9) vs lines expressing it (39) | the lines without LINC00922: 0.81× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: MGC4859, ENSG00000250149, LINC01811; maybe low, not absent |
| [[SPOCK1]] | 0.5 µM | B | SPOCK1 activity raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.87× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[BMPER]] | 0.5 µM | B | BMPER activity raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 0.87× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[SVEP1]] | 0.5 µM | B | SVEP1 activity raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | lines that do not express SVEP1 (15) vs lines expressing it (33) | the lines without SVEP1: 0.89× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent |
| [[EZR]], [[TMC7]] | 0.5 µM | C | EZR, TMC7 activity lowers the cells' numbers under Anethole trithione 0.5 µM (makes them more sensitive) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 1.33× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| [[IFT74]] | 5 µM | C | IFT74 activity raises the cells' numbers under Anethole trithione 5 µM (protects the cells) | lines that do not express IFT74 (3) vs lines expressing it (45) | the lines without IFT74: 0.86× the cells of the other lines | 0.081 | ⚠ few lines (3 vs 47); across organs; also absent: LCA5, P3H4, TOMM40L; maybe low, not absent |
| [[DHCR7]], [[ENSG00000254682]] | 5 µM | C | DHCR7, ENSG00000254682 activity lowers the cells' numbers under Anethole trithione 5 µM (makes them more sensitive) | lines that do not express DHCR7, ENSG00000254682 (3) vs lines expressing them (45) | the lines without DHCR7, ENSG00000254682: 1.18× the cells of the other lines | 0.084 | ⚠ few lines (3 vs 47); across organs; also absent: LPIN3, TACC2, INSR; co-absent genes |
| [[ENSG00000258302]] | 0.5 µM | C | ENSG00000258302's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | ENSG00000258302's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72 | 0.201 over the table, 0.009 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[COG3]] | 0.5 µM | C | COG3's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | COG3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.71 | 0.260 over the table, 0.012 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ENSG00000240571]] | 0.5 µM | C | ENSG00000240571's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | ENSG00000240571's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69 | 0.268 over the table, 0.013 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[RCBTB2]] | 0.5 µM | C | RCBTB2's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | RCBTB2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.285 over the table, 0.021 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ENSG00000260392]] | 0.5 µM | C | ENSG00000260392's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | ENSG00000260392's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.310 over the table, 0.025 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ARHGAP39]] | 0.5 µM | C | ARHGAP39's natural level lowers the cells' numbers under Anethole trithione 0.5 µM (makes them more sensitive) | ARHGAP39's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.339 over the table, 0.029 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Anethole trithione"
- `tables/drugdoses.parquet` — dd in 93, 94, 95
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
