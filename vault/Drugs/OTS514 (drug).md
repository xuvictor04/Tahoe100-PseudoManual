---
drug: "OTS514"
type: "drug"
salt_base: "OTS514"
targets: "MAP3K8"
moa_fine: "Other MAPK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 64
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# OTS514

*Other MAPK inhibitor (inhibitor/antagonist) · targets: MAP3K8 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 56 / 4 / 64; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.08 / -0.56.
> Flags by dose: transcription drop / noisy plate (z scaled) / noisy plate (z scaled). ⚠ 0.05 µM: transcription drop (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:G5 | 9 / 47 | — | -0.18 | +0.4/+0.7/+1.2 | ⚠ transcription drop |
| 0.5 µM | [[Plate 02]]:G5 | 0 / 4 | — | +0.02 | -1.6/-1.4/-1.1 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:G5 | 20 / 44 | — | -0.85 | +1.0/+1.1/+1.1 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (9 genes, 9 with an alert ⚠; the drug-dose carries ⚠ transcription drop): [[POMGNT2]] ⚠ 1.47× (z +5.2, 13/43 lines), [[PLA2G15]] ⚠ 1.33× (z +4.4, 11/46 lines), [[RIMKLA]] ⚠ 1.24× (z +3.6, 9/39 lines), [[PITX1]] ⚠ 1.43× (z +3.5, 5/36 lines), [[H4C3]] ⚠ 1.82× (z +3.4, 27/48 lines), [[C11orf24]] ⚠ 1.20× (z +3.1, 9/47 lines), [[RNF125]] ⚠ 1.21× (z +3.1, 3/36 lines), [[MTCH1]] ⚠ 1.25× (z +2.9, 19/48 lines), [[AP1B1]] ⚠ 1.20× (z +2.7, 8/48 lines)

**5 µM** (20 genes, none with an alert; 12 shown): [[NT5DC2]] 2.05× (z +4.4, 10/33 lines), [[ZC3HAV1]] 1.51× (z +4.3, 23/46 lines), [[RAB4A]] 1.50× (z +3.9, 16/44 lines), [[LRPAP1]] 1.59× (z +3.7, 22/46 lines), [[SRP9]] 1.35× (z +3.4, 18/46 lines), [[AKAP1]] 1.35× (z +3.4, 6/42 lines), [[RABGGTA]] 1.74× (z +3.3, 1/23 lines), [[KNSTRN]] 1.48× (z +3.3, 6/42 lines), [[ZDHHC3]] 1.25× (z +3.2, 9/45 lines), [[RPL6]] 1.72× (z +3.1, 19/46 lines), [[PPT2]] 1.56× (z +3.1, 2/28 lines), [[GNA11]] 1.42× (z +3.1, 3/43 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (47 genes, 47 with an alert ⚠; the drug-dose carries ⚠ transcription drop; 12 shown): [[C4orf19]] ⚠ 0.704× (z -5.0, 4/33 lines), [[UTY]] ⚠ 0.737× (z -4.9, 0/17 lines), [[CLASP1-AS1]] ⚠ 0.480× (z -4.5, 13/39 lines), [[MIR137HG]] ⚠ 0.610× (z -4.5, 2/19 lines), [[POU5F1]] ⚠ 0.729× (z -4.4, 2/21 lines), [[ENSG00000229618]] ⚠ 0.753× (z -4.3, 0/16 lines), [[FLI1]] ⚠ 0.723× (z -3.9, 1/17 lines), [[BCL2L2-PABPN1]] ⚠ 0.792× (z -3.8, 13/48 lines), [[FSTL5]] ⚠ 0.746× (z -3.8, 1/13 lines), [[SCEL]] ⚠ 0.659× (z -3.8, 0/13 lines), [[VSIG1]] ⚠ 0.559× (z -3.8, 6/14 lines), [[ENSG00000267581]] ⚠ 0.713× (z -3.8, 3/27 lines)

**0.5 µM** (4 genes, none with an alert): [[ENSG00000251652]] 0.611× (z -3.5, 0/11 lines), [[KIF5C]] 0.747× (z -3.4, 8/48 lines), [[CD68]] 0.701× (z -3.0, 13/42 lines), [[PLBD2]] 0.808× (z -3.0, 1/48 lines)

**5 µM** (44 genes, none with an alert; 12 shown): [[BUD13]] 0.576× (z -5.6, 22/43 lines), [[WAPL]] 0.756× (z -4.8, 28/46 lines), [[UBE2Q2P2]] 0.623× (z -4.6, 27/45 lines), [[ENSG00000290835]] 0.616× (z -4.4, 15/42 lines), [[KMT5B]] 0.780× (z -4.0, 20/46 lines), [[NBPF11]] 0.682× (z -4.0, 18/44 lines), [[NDUFS4]] 0.745× (z -4.0, 22/46 lines), [[PRPF4B]] 0.740× (z -3.9, 25/46 lines), [[CYB5R4]] 0.648× (z -3.7, 23/46 lines), [[PTPN2]] 0.805× (z -3.7, 18/46 lines), [[SNX27]] 0.758× (z -3.6, 18/46 lines), [[ENSG00000279598]] 0.507× (z -3.5, 10/23 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 179]] (-2.0) |
| 0.5 µM | — | — |
| 5 µM | [[Module 184]] (+2.1) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[C32 (line)]] (1.58), [[BT-474 (line)]] (1.50), [[HCT15 (line)]] (1.46), [[COLO 205 (line)]] (1.44) · weakest: [[NCI-H661 (line)]] (0.290), [[SW 1271 (line)]] (0.591), [[HS-578T (line)]] (0.623) |
| 0.5 µM | — | — |
| 5 µM | [[A549 (line)]] (-3.5), [[NCI-H460 (line)]] (-3.0) | [[MIA PaCa-2 (line)]] (1.42), [[A549 (line)]] (1.22), [[HCT15 (line)]] (1.22), [[SW 900 (line)]] (1.18) · weakest: [[AN3 CA (line)]] (0.567), [[SW 1088 (line)]] (0.598), [[SNU-423 (line)]] (0.602) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[LY-2584702 (tosylate salt) (drug)]] (+0.68, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[9-ING-41 (drug)]] (+0.64, GSK3 inhibitor); [[XRK3F2 (drug)]] (+0.62, unclear); [[Canagliflozin (drug)]] (+0.61, Glucose transporter inhibitor); [[BI-78D3 (drug)]] (+0.60, Other MAPK inhibitor); [[DT-061 (drug)]] (+0.57, unclear); [[Lenalidomide (hemihydrate) (drug)]] (+0.57, unclear); [[Docetaxel (drug)]] (+0.56, Microtubule inhibitor, ⚠ vector dose flagged: transcription drop; cell-cycle shift); [[Ferulic acid (drug)]] (+0.55, Other TK inhibitor); [[Sonidegib (drug)]] (+0.55, Sonic inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SOX6]] | 0.05 µM | B | SOX6 activity raises the cells' numbers under OTS514 0.05 µM (protects the cells) | lines that do not express SOX6 (22) vs lines expressing it (26) | the lines without SOX6: 0.88× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[OR9Q1]] | 5 µM | B | OR9Q1 activity lowers the cells' numbers under OTS514 5 µM (makes them more sensitive) | lines that do not express OR9Q1 (26) vs lines expressing it (22) | the lines without OR9Q1: 1.17× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[HS3ST3B1]] | 5 µM | B | HS3ST3B1 activity lowers the cells' numbers under OTS514 5 µM (makes them more sensitive) | lines that do not express HS3ST3B1 (18) vs lines expressing it (30) | the lines without HS3ST3B1: 1.15× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[KLRK1-AS1]] | 0.05 µM | B | KLRK1-AS1 activity raises the cells' numbers under OTS514 0.05 µM (protects the cells) | lines that do not express KLRK1-AS1 (11) vs lines expressing it (37) | the lines without KLRK1-AS1: 0.92× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| [[NR3C1]] | 0.05 µM | C | NR3C1 activity lowers the cells' numbers under OTS514 0.05 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.19× the cells of the other lines | 0.025 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[LIFR]] | 0.05 µM | C | LIFR activity lowers the cells' numbers under OTS514 0.05 µM (makes them more sensitive) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 1.16× the cells of the other lines | 0.066 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| [[ITPK1]] | 0.05 µM | C | ITPK1 activity raises the cells' numbers under OTS514 0.05 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.81× the cells of the other lines | 0.079 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| [[SETD7]] | 0.05 µM | C | SETD7 activity lowers the cells' numbers under OTS514 0.05 µM (makes them more sensitive) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 1.29× the cells of the other lines | 0.081 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| [[ENSG00000256029]] | 0.05 µM | C | ENSG00000256029 activity lowers the cells' numbers under OTS514 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000256029 (4) vs lines expressing it (44) | the lines without ENSG00000256029: 1.25× the cells of the other lines | 0.082 | ⚠ few lines (4 vs 46); across organs; also absent: ERRFI1, FXYD5, CAV2; maybe low, not absent |
| [[C2orf74]] | 0.05 µM | C | C2orf74 activity lowers the cells' numbers under OTS514 0.05 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.15× the cells of the other lines | 0.091 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[ZNF484]] | 5 µM | C | ZNF484's natural level lowers the cells' numbers under OTS514 5 µM (makes them more sensitive) | ZNF484's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.73 | 0.186 over the table, 0.008 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[PPP1R12A-AS2]] | 0.05 µM | C | PPP1R12A-AS2's natural level lowers the cells' numbers under OTS514 0.05 µM (makes them more sensitive) | PPP1R12A-AS2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.081 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "OTS514"
- `tables/drugdoses.parquet` — dd in 729, 730, 731
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
