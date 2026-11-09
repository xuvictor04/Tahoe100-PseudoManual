---
drug: "Cepharanthine"
type: "drug"
salt_base: "Cepharanthine"
targets: "CYP3A4, CYP2E1, CYP2C9"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 364
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Cepharanthine

*unclear (inhibitor/antagonist) · targets: CYP3A4, CYP2E1, CYP2C9 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 15 / 364; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.06 / 0.31.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:E11 | 1 / 0 | — | +0.24 | +0.3/+0.6/-0.2 | — |
| 0.5 µM | [[Plate 05]]:E11 | 12 / 3 | — | -0.48 | -1.4/-1.0/-0.5 | — |
| 5 µM | [[Plate 14]]:E11 | 328 / 36 | 0.874 | -0.90 | -4.1/-2.7/-1.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[RYR2]] 1.47× (z +3.6, 8/48 lines)

**0.5 µM** (12 genes, none with an alert): [[ENSG00000100101]] 1.31× (z +4.3, 18/47 lines), [[SLC38A4]] 1.55× (z +4.2, 1/23 lines), [[ENSG00000291112]] 1.44× (z +4.1, 9/29 lines), [[ADAMTS10]] 1.42× (z +3.7, 4/17 lines), [[G2E3-AS1]] 1.48× (z +3.6, 4/35 lines), [[CYP1B1]] 1.67× (z +3.5, 14/19 lines), [[CD36]] 1.38× (z +3.4, 6/22 lines), [[RYR2]] 1.38× (z +3.2, 9/46 lines), [[IRAK3]] 1.33× (z +3.1, 1/12 lines), [[ENSG00000270265]] 1.41× (z +3.0, 1/28 lines), [[JAKMIP2]] 1.37× (z +2.9, 2/18 lines), [[PPP1R3B-DT]] 1.26× (z +2.8, 1/34 lines)

**5 µM** (328 genes, none with an alert; 12 shown): [[LPIN1]] 1.88× (z +20.0, 44/48 lines), [[ACSS2]] 2.41× (z +19.7, 44/47 lines), [[SCD]] 2.65× (z +19.5, 48/48 lines), [[MSMO1]] 3.39× (z +18.5, 45/47 lines), [[IDI1]] 2.55× (z +17.6, 47/48 lines), [[CYP51A1]] 2.21× (z +17.5, 45/47 lines), [[FDPS]] 2.65× (z +17.2, 47/48 lines), [[HMGCS1]] 2.65× (z +16.9, 46/47 lines), [[HMGCR]] 2.25× (z +16.6, 47/48 lines), [[MVK]] 2.31× (z +16.5, 43/47 lines), [[ACAT2]] 2.17× (z +16.5, 46/48 lines), [[SC5D]] 1.98× (z +16.1, 42/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (3 genes, none with an alert): [[MAD2L1BP]] 0.772× (z -3.6, 10/44 lines), [[ERCC6L]] 0.767× (z -3.6, 13/44 lines), [[METTL1]] 0.764× (z -3.5, 6/41 lines)

**5 µM** (36 genes, none with an alert; 12 shown): [[AGPAT1]] 0.737× (z -5.7, 34/48 lines), [[FTH1]] 0.682× (z -5.5, 44/44 lines), [[SF3A1]] 0.787× (z -5.3, 37/48 lines), [[ABCG1]] 0.739× (z -4.5, 16/33 lines), [[MCAM]] 0.732× (z -4.5, 10/26 lines), [[DTL]] 0.799× (z -4.4, 20/48 lines), [[RAD51AP1]] 0.800× (z -4.3, 27/46 lines), [[EME1]] 0.767× (z -4.1, 15/46 lines), [[IGFBP6]] 0.720× (z -4.1, 22/32 lines), [[REXO5]] 0.801× (z -4.0, 16/46 lines), [[C17orf58]] 0.795× (z -3.9, 13/48 lines), [[RPL4]] 0.799× (z -3.8, 40/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 086]] (+11.4) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[CHP-212 (line)]] (1.57), [[A549 (line)]] (1.42), [[NCI-H23 (line)]] (1.37), [[HOP62 (line)]] (1.33) · weakest: [[SHP-77 (line)]] (0.381), [[RKO (line)]] (0.512), [[NCI-H661 (line)]] (0.556) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Entrectinib (drug)]] (+0.56, Other TK inhibitor); [[Simotinib (drug)]] (+0.49, EGFR/ERBB inhibitor, ⚠ vector dose flagged: toxic); [[Almonertinib (hydrochloride) (drug)]] (+0.47, EGFR/ERBB inhibitor); [[Pyridoxine (drug)]] (+0.46, unclear); [[Ritonavir (drug)]] (+0.45, unclear); [[Adagrasib (drug)]] (+0.45, RAS inhibitor); [[(S)-Crizotinib (drug)]] (+0.45, unclear); [[Berbamine (dihydrochloride) (drug)]] (+0.44, unclear); [[Chlorhexidine (diacetate) (drug)]] (+0.44, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PHF11]] | 5 µM | C | PHF11 activity lowers the cells' numbers under Cepharanthine 5 µM (makes them more sensitive) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 1.31× the cells of the other lines | 0.015 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[CEBPD]], [[GCA]] | 5 µM | C | CEBPD, GCA activity lowers the cells' numbers under Cepharanthine 5 µM (makes them more sensitive) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 1.30× the cells of the other lines | 0.031 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| [[LRRCC1]], [[OXR1]] | 5 µM | C | LRRCC1, OXR1 activity lowers the cells' numbers under Cepharanthine 5 µM (makes them more sensitive) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 1.21× the cells of the other lines | 0.047 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| [[SPAG16]] | 5 µM | C | SPAG16 activity lowers the cells' numbers under Cepharanthine 5 µM (makes them more sensitive) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 1.18× the cells of the other lines | 0.080 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |
| [[ENSG00000256029]] | 5 µM | C | ENSG00000256029 activity lowers the cells' numbers under Cepharanthine 5 µM (makes them more sensitive) | lines that do not express ENSG00000256029 (4) vs lines expressing it (44) | the lines without ENSG00000256029: 1.20× the cells of the other lines | 0.096 | ⚠ few lines (4 vs 46); across organs; also absent: ERRFI1, FXYD5, CAV2; maybe low, not absent |
| [[LY6E]] | 5 µM | C | LY6E activity lowers the cells' numbers under Cepharanthine 5 µM (makes them more sensitive) | lines that do not express LY6E (4) vs lines expressing it (44) | the lines without LY6E: 1.18× the cells of the other lines | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ARHGEF10; maybe low, not absent |
| [[PSMB8]] | 5 µM | C | PSMB8 activity lowers the cells' numbers under Cepharanthine 5 µM (makes them more sensitive) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 1.20× the cells of the other lines | 0.099 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Cepharanthine"
- `tables/drugdoses.parquet` — dd in 254, 255, 256
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
