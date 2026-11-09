---
drug: "Furosemide"
type: "drug"
salt_base: "Furosemide"
targets: "SLC12A1, SLC12A2"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 16
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Furosemide

*unclear (inhibitor/antagonist) · targets: SLC12A1, SLC12A2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 4 / 16 / 4; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.04 / 0.18.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:B1 | 1 / 3 | — | -0.28 | -0.4/+0.2/-0.9 | — |
| 0.5 µM | [[Plate 05]]:B1 | 3 / 13 | — | -0.23 | +1.9/+2.5/+0.8 | — |
| 5 µM | [[Plate 14]]:B1 | 1 / 3 | 0.804 | -0.04 | +1.1/+1.5/-1.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[EFHD1]] 1.33× (z +2.9, 3/36 lines)

**0.5 µM** (3 genes, none with an alert): [[ARMC1]] 1.23× (z +4.7, 20/48 lines), [[PIGS]] 1.28× (z +4.2, 9/47 lines), [[MAN1B1]] 1.21× (z +3.3, 8/48 lines)

**5 µM** (1 gene, none with an alert): [[TRIM6]] 1.22× (z +3.0, 4/30 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[FKBP7]] 0.691× (z -3.4, 3/36 lines), [[LINC02977]] 0.759× (z -3.4, 4/35 lines), [[LINC02458]] 0.750× (z -2.8, 6/46 lines)

**0.5 µM** (13 genes, none with an alert; 12 shown): [[ENSG00000256966]] 0.650× (z -4.5, 15/39 lines), [[CNPPD1]] 0.757× (z -4.4, 16/45 lines), [[WASH2P-1]] 0.659× (z -3.9, 16/41 lines), [[BTBD2]] 0.822× (z -3.7, 12/48 lines), [[ECSIT]] 0.819× (z -3.7, 9/47 lines), [[NDST2]] 0.745× (z -3.5, 10/44 lines), [[KIF5C]] 0.806× (z -3.5, 9/48 lines), [[PHLDB3]] 0.816× (z -3.3, 9/46 lines), [[PRDM1]] 0.806× (z -3.2, 6/33 lines), [[ENSG00000284685]] 0.711× (z -3.1, 11/35 lines), [[ENSG00000236255]] 0.786× (z -3.1, 12/48 lines), [[ENSG00000261273]] 0.701× (z -3.0, 12/35 lines)

**5 µM** (3 genes, none with an alert): [[GPC5]] 0.747× (z -3.5, 16/40 lines), [[ENSG00000288000]] 0.775× (z -3.1, 18/48 lines), [[KLRD1]] 0.767× (z -3.0, 8/40 lines)

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
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Trifluridine (drug)]] (+0.66, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Sonidegib (drug)]] (+0.56, Sonic inhibitor); [[Retinoic acid (drug)]] (+0.55, Retinoic receptor agonist); [[Pyridoxine (hydrochloride) (drug)]] (+0.54, unclear); [[Relugolix (drug)]] (+0.54, unclear, ⚠ only 5 significant genes); [[Lumateperone (tosylate) (drug)]] (+0.54, unclear, ⚠ only 9 significant genes); [[Megestrol (drug)]] (+0.52, unclear, ⚠ vector dose flagged: cell-cycle shift); [[LJI308 (drug)]] (+0.50, Other MAPK inhibitor); [[Berbamine (drug)]] (+0.48, unclear); [[Adenine (drug)]] (+0.46, unclear); [[Regorafenib (drug)]] (+0.46, Multi-TK inhibitor); [[OTS514 (drug)]] (+0.45, Other MAPK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 19 arrows, 19 of them with an alert ⚠; grade A 0, B 4, C 15. Shown: the 15 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MBNL3]] | 0.5 µM | B | MBNL3 activity raises the cells' numbers under Furosemide 0.5 µM (protects the cells) | lines that do not express MBNL3 (16) vs lines expressing it (32) | the lines without MBNL3: 0.86× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[P3H2]] | 0.5 µM | B | P3H2 activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express P3H2 (28) vs lines expressing it (20) | the lines without P3H2: 1.17× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: P3H2-AS1, SRGN, SPOCK1 |
| [[TSPAN12]] | 0.5 µM | B | TSPAN12 activity raises the cells' numbers under Furosemide 0.5 µM (protects the cells) | lines that do not express TSPAN12 (13) vs lines expressing it (35) | the lines without TSPAN12: 0.87× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; also absent: ATP8A1, PPP1R9A, SH3BGRL2; maybe low, not absent |
| [[LMO3]] | 0.5 µM | B | LMO3 activity raises the cells' numbers under Furosemide 0.5 µM (protects the cells) | lines that do not express LMO3 (36) vs lines expressing it (12) | the lines without LMO3: 0.91× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: MUC6, LINC02566, APOD; maybe low, not absent |
| [[NR3C1]] | 0.5 µM | C | NR3C1 activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.22× the cells of the other lines | 0.004 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[C2orf74]] | 0.5 µM | C | C2orf74 activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.19× the cells of the other lines | 0.019 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[FIGN]] | 0.5 µM | C | FIGN activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.16× the cells of the other lines | 0.021 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[SPART-AS1]] | 0.5 µM | C | SPART-AS1 activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.15× the cells of the other lines | 0.021 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[SIX1]] | 0.5 µM | C | SIX1 activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 1.21× the cells of the other lines | 0.026 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| [[ENSG00000286964]] | 0.5 µM | C | ENSG00000286964 activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.20× the cells of the other lines | 0.026 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |
| [[ITPK1]] | 0.5 µM | C | ITPK1 activity raises the cells' numbers under Furosemide 0.5 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.80× the cells of the other lines | 0.034 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| [[LIFR]] | 0.5 µM | C | LIFR activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 1.17× the cells of the other lines | 0.041 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| [[SLC36A4]] | 0.5 µM | C | SLC36A4 activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express SLC36A4 (5) vs lines expressing it (43) | the lines without SLC36A4: 1.24× the cells of the other lines | 0.054 | ⚠ tissue-confounded; across organs; co-occurs with CTNNB1; also absent: KLHL5, FBXL2, SIX4 |
| [[TBC1D9]] | 0.5 µM | C | TBC1D9 activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express TBC1D9 (6) vs lines expressing it (42) | the lines without TBC1D9: 1.20× the cells of the other lines | 0.068 | ⚠ tissue-confounded; across organs; also absent: SIX1, TRPC1, MTERF1 |
| [[SEMA4G]] | 0.5 µM | C | SEMA4G activity raises the cells' numbers under Furosemide 0.5 µM (protects the cells) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 0.83× the cells of the other lines | 0.076 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Furosemide"
- `tables/drugdoses.parquet` — dd in 480, 481, 482
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
