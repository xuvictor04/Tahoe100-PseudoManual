---
drug: "olaparib"
type: "drug"
salt_base: "olaparib"
targets: "PARP1, PARP2"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 26
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# olaparib

*DNA synthesis/repair inhibitor (unclear) · targets: PARP1, PARP2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 26 / 0 / 3; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.50 / -0.13.
> Flags by dose: unreliable plate only / noisy plate (z scaled) / noisy plate (z scaled). ⚠ 0.05 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:A8 | 6 / 20 | — | -0.02 | -1.3/-2.0/-1.7 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 02]]:G2 | 0 / 0 | — | +0.63 | -0.2/-0.4/-1.0 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:G2 | 2 / 1 | — | -0.32 | -0.1/+0.3/+0.2 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (6 genes, 6 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[RHOXF1]] ⚠ 1.23× (z +3.2, 8/47 lines), [[PARP12]] ⚠ 1.24× (z +3.1, 10/46 lines), [[GBP2]] ⚠ 1.22× (z +3.0, 10/35 lines), [[SIPA1L2]] ⚠ 1.21× (z +2.9, 1/38 lines), [[BCL2L11]] ⚠ 1.24× (z +2.8, 12/48 lines), [[SLCO5A1]] ⚠ 1.20× (z +2.7, 0/41 lines)

**5 µM** (2 genes, none with an alert): [[DMD]] 1.41× (z +3.3, 0/27 lines), [[TRABD2A]] 1.52× (z +3.2, 0/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (20 genes, 20 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[RAB3B]] ⚠ 0.793× (z -3.8, 8/31 lines), [[EIF4EBP1]] ⚠ 0.689× (z -3.4, 20/48 lines), [[YEATS4]] ⚠ 0.825× (z -3.3, 10/47 lines), [[NLRP3]] ⚠ 0.664× (z -3.2, 7/19 lines), [[TM4SF19]] ⚠ 0.789× (z -3.1, 7/28 lines), [[TMEM158]] ⚠ 0.608× (z -3.1, 16/29 lines), [[PLIN3]] ⚠ 0.779× (z -3.1, 18/47 lines), [[RIN1]] ⚠ 0.726× (z -3.0, 8/45 lines), [[AKAP12]] ⚠ 0.762× (z -3.0, 16/30 lines), [[WT1]] ⚠ 0.757× (z -3.0, 1/18 lines), [[DUSP6]] ⚠ 0.715× (z -3.0, 26/44 lines), [[RAC2]] ⚠ 0.769× (z -2.9, 12/29 lines)

**5 µM** (1 gene, none with an alert): [[CREB5]] 0.734× (z -2.9, 10/35 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 179]] (+2.2) | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[H4 (line)]] (3.45), [[SW 1088 (line)]] (2.43), [[A-172 (line)]] (2.24), [[J82 (line)]] (2.08) · weakest: [[SHP-77 (line)]] (0.275), [[SK-MEL-2 (line)]] (0.318), [[LoVo (line)]] (0.517) |
| 0.5 µM | — | — |
| 5 µM | [[PANC-1 (line)]] (-4.1), [[A-172 (line)]] (-3.5) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 3 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[XRK3F2 (drug)]] (+0.69, unclear); [[Entrectinib (drug)]] (+0.67, Other TK inhibitor); [[Bicalutamide (drug)]] (+0.67, Androgen receptor antagonist); [[Capmatinib (drug)]] (+0.65, EGFR/ERBB inhibitor); [[AZD-7648 (drug)]] (+0.64, DNA synthesis/repair inhibitor); [[Alpelisib (drug)]] (+0.63, PI3K/AKT inhibitor); [[Vortioxetine (drug)]] (+0.62, unclear, ⚠ vector dose flagged: toxic); [[Hydroxyfasudil (drug)]] (+0.61, unclear); [[Bendamustine (drug)]] (+0.61, DNA synthesis/repair inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 19 arrows, 19 of them with an alert ⚠; grade A 0, B 5, C 14. Shown: the 15 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ASCL1]] | 5 µM | B | ASCL1 activity raises the cells' numbers under olaparib 5 µM (protects the cells) | lines that do not express ASCL1 (41) vs lines expressing it (7) | the lines without ASCL1: 0.69× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[RAB32]] | 5 µM | B | RAB32 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express RAB32 (7) vs lines expressing it (41) | the lines without RAB32: 1.45× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| [[PPARG]] | 5 µM | B | PPARG activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express PPARG (20) vs lines expressing it (28) | the lines without PPARG: 1.29× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[ENSG00000256514]] | 5 µM | B | ENSG00000256514 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express ENSG00000256514 (9) vs lines expressing it (39) | the lines without ENSG00000256514: 1.42× the cells of the other lines | 0.085 | ⚠ within organs, on part of the lines; also absent: HTATIP2, CLCF1, SAT1; maybe low, not absent |
| [[TMEM92]] | 5 µM | B | TMEM92 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express TMEM92 (22) vs lines expressing it (26) | the lines without TMEM92: 1.29× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[FZD6]] | 5 µM | C | FZD6 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express FZD6 (5) vs lines expressing it (43) | the lines without FZD6: 1.61× the cells of the other lines | 0.004 | ⚠ tissue-confounded; across organs; also absent: DOCK5, PMAIP1, ISG20 |
| [[TBILA]] | 5 µM | C | TBILA activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 1.64× the cells of the other lines | 0.006 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| [[ENSG00000285458]] | 5 µM | C | ENSG00000285458 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express ENSG00000285458 (5) vs lines expressing it (43) | the lines without ENSG00000285458: 1.54× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: TBILA, GCA, RILP; maybe low, not absent |
| [[ISG20]] | 5 µM | C | ISG20 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 1.64× the cells of the other lines | 0.011 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| [[PSMB8]] | 5 µM | C | PSMB8 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 1.59× the cells of the other lines | 0.025 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[PMAIP1]] | 5 µM | C | PMAIP1 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express PMAIP1 (4) vs lines expressing it (44) | the lines without PMAIP1: 1.54× the cells of the other lines | 0.036 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent |
| [[CEBPD]], [[GCA]] | 5 µM | C | CEBPD, GCA activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 1.64× the cells of the other lines | 0.042 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| [[DOCK5]] | 5 µM | C | DOCK5 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express DOCK5 (3) vs lines expressing it (45) | the lines without DOCK5: 1.58× the cells of the other lines | 0.051 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: PMAIP1, FZD6, GCA; maybe low, not absent |
| [[PHF11]] | 5 µM | C | PHF11 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 1.58× the cells of the other lines | 0.056 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[RILP]] | 5 µM | C | RILP activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 1.63× the cells of the other lines | 0.063 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "olaparib"
- `tables/drugdoses.parquet` — dd in 1117, 1118, 1119
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
