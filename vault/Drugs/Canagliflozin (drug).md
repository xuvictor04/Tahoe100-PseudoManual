---
drug: "Canagliflozin"
type: "drug"
salt_base: "Canagliflozin"
targets: "SLC5A2"
moa_fine: "Glucose transporter inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 76
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Canagliflozin

*Glucose transporter inhibitor (inhibitor/antagonist) · targets: SLC5A2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 76 / 2 / 16; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.06 / -0.06.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:E5 | 66 / 10 | — | -0.60 | +0.1/+0.0/+1.7 | — |
| 0.5 µM | [[Plate 08]]:E5 | 0 / 2 | — | +0.07 | +0.5/+0.4/+0.5 | — |
| 5 µM | [[Plate 09]]:E5 | 12 / 4 | — | -0.62 | -0.4/-0.5/-0.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (66 genes, none with an alert; 12 shown): [[KRT10-AS1]] 1.37× (z +4.4, 5/39 lines), [[IHO1]] 1.78× (z +4.3, 0/7 lines), [[SUN2]] 1.22× (z +3.8, 10/47 lines), [[ENSG00000291042]] 1.46× (z +3.7, 2/33 lines), [[CNTN6]] 1.60× (z +3.7, 0/6 lines), [[ENSG00000263655]] 1.76× (z +3.7, 0/6 lines), [[ZNF229]] 1.38× (z +3.6, 3/21 lines), [[ADORA1]] 1.53× (z +3.5, 5/26 lines), [[ENSG00000287862]] 1.54× (z +3.4, 0/6 lines), [[COX18]] 1.26× (z +3.4, 8/43 lines), [[FAM110B]] 1.29× (z +3.4, 1/20 lines), [[ACYP1]] 1.28× (z +3.4, 11/42 lines)

**5 µM** (12 genes, none with an alert): [[UBE2D3-AS1]] 1.34× (z +3.6, 6/42 lines), [[EML5]] 1.28× (z +3.3, 6/28 lines), [[ENSG00000286076]] 1.61× (z +3.0, 1/17 lines), [[LINC02284]] 1.39× (z +3.0, 2/25 lines), [[INO80B]] 1.26× (z +3.0, 6/45 lines), [[IGSF11]] 1.33× (z +3.0, 5/32 lines), [[ENSG00000237461]] 1.37× (z +3.0, 4/46 lines), [[CCDC144A]] 1.34× (z +2.9, 1/21 lines), [[PRKG1-AS1]] 1.37× (z +2.9, 1/22 lines), [[CYP2U1]] 1.38× (z +2.9, 4/36 lines), [[PKHD1]] 1.38× (z +2.9, 3/13 lines), [[ENSG00000287231]] 1.42× (z +2.8, 0/16 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (10 genes, none with an alert): [[CSRP1-AS1]] 0.606× (z -4.7, 9/28 lines), [[ARHGAP4]] 0.741× (z -4.1, 13/42 lines), [[RPGR]] 0.826× (z -3.5, 13/46 lines), [[MALAT1]] 0.810× (z -3.5, 39/47 lines), [[ENSG00000205236]] 0.766× (z -3.3, 10/40 lines), [[RNF216P1]] 0.748× (z -3.2, 13/41 lines), [[LINC01237]] 0.738× (z -3.1, 13/35 lines), [[RASA3]] 0.810× (z -2.9, 9/38 lines), [[PDXDC2P-NPIPB14P]] 0.802× (z -2.7, 9/43 lines), [[SLC10A7]] 0.825× (z -2.7, 12/46 lines)

**0.5 µM** (2 genes, none with an alert): [[ENSG00000289474]] 0.448× (z -3.8, 6/8 lines), [[SPATA20]] 0.799× (z -3.0, 2/47 lines)

**5 µM** (4 genes, none with an alert): [[MAMDC2]] 0.678× (z -4.2, 4/30 lines), [[BARX2]] 0.787× (z -3.5, 3/19 lines), [[TBC1D17]] 0.824× (z -3.1, 9/46 lines), [[RASSF2]] 0.768× (z -3.1, 7/27 lines)

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
| 0.05 µM | — | [[SW 1271 (line)]] (1.79), [[SW48 (line)]] (1.67), [[AN3 CA (line)]] (1.35), [[CHP-212 (line)]] (1.30) · weakest: [[NCI-H23 (line)]] (0.130), [[NCI-H1792 (line)]] (0.247), [[Hs 766T (line)]] (0.332) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[LY-2584702 (tosylate salt) (drug)]] (+0.79, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Hydroxyurea (drug)]] (+0.78, DNA synthesis/repair inhibitor); [[9-ING-41 (drug)]] (+0.75, GSK3 inhibitor); [[BI-78D3 (drug)]] (+0.75, Other MAPK inhibitor); [[Thymol (drug)]] (+0.75, unclear); [[XRK3F2 (drug)]] (+0.74, unclear); [[Nimesulide (drug)]] (+0.72, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Pyridoxine (drug)]] (+0.70, unclear); [[Lenalidomide (hemihydrate) (drug)]] (+0.70, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.66, Glucose transporter inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 13 arrows, 13 of them with an alert ⚠; grade A 0, B 3, C 10.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[TNNT2]] | 5 µM | B | TNNT2 activity raises the cells' numbers under Canagliflozin 5 µM (protects the cells) | lines that do not express TNNT2 (29) vs lines expressing it (19) | the lines without TNNT2: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[MBNL3]] | 5 µM | B | MBNL3 activity raises the cells' numbers under Canagliflozin 5 µM (protects the cells) | lines that do not express MBNL3 (16) vs lines expressing it (32) | the lines without MBNL3: 0.86× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[AOX1]] | 5 µM | B | AOX1 activity lowers the cells' numbers under Canagliflozin 5 µM (makes them more sensitive) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 1.18× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[ITPK1]] | 5 µM | C | ITPK1 activity raises the cells' numbers under Canagliflozin 5 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.78× the cells of the other lines | 0.013 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| [[FIGN]] | 5 µM | C | FIGN activity lowers the cells' numbers under Canagliflozin 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.17× the cells of the other lines | 0.023 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[C2orf74]] | 5 µM | C | C2orf74 activity lowers the cells' numbers under Canagliflozin 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.18× the cells of the other lines | 0.027 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[SPART-AS1]] | 5 µM | C | SPART-AS1 activity lowers the cells' numbers under Canagliflozin 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.14× the cells of the other lines | 0.051 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[SCAMP5]] | 5 µM | C | SCAMP5 activity raises the cells' numbers under Canagliflozin 5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.78× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| [[UBL4A]] | 5 µM | C | UBL4A's natural level lowers the cells' numbers under Canagliflozin 5 µM (makes them more sensitive) | UBL4A's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.74 | 0.162 over the table, 0.004 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ACTR3-AS1]] | 5 µM | C | ACTR3-AS1's natural level lowers the cells' numbers under Canagliflozin 5 µM (makes them more sensitive) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.73 | 0.186 over the table, 0.004 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[RNU4-2]] | 5 µM | C | RNU4-2's natural level raises the cells' numbers under Canagliflozin 5 µM (protects the cells) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69 | 0.268 over the table, 0.016 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ENSG00000270019]] | 5 µM | C | ENSG00000270019's natural level lowers the cells' numbers under Canagliflozin 5 µM (makes them more sensitive) | ENSG00000270019's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.021 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[MAST1]] | 5 µM | C | MAST1's natural level raises the cells' numbers under Canagliflozin 5 µM (protects the cells) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.360 over the table, 0.048 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Canagliflozin"
- `tables/drugdoses.parquet` — dd in 230, 231, 232
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
