---
drug: "Clotrimazole"
type: "drug"
salt_base: "Clotrimazole"
targets: "CYP2A6, CYP51A1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 23
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Clotrimazole

*unclear (inhibitor/antagonist) · targets: CYP2A6, CYP51A1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 11 / 23; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.22 / 0.20.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:B2 | 0 / 1 | — | -0.07 | +0.1/-0.2/-0.3 | — |
| 0.5 µM | [[Plate 05]]:B2 | 8 / 3 | — | -0.45 | -0.2/-1.1/-0.9 | — |
| 5 µM | [[Plate 14]]:B2 | 3 / 20 | 0.843 | -0.03 | -2.0/-1.7/-0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (8 genes, none with an alert): [[ARHGAP28]] 1.37× (z +3.5, 0/23 lines), [[FMO4]] 1.43× (z +3.4, 1/32 lines), [[ENSG00000263603]] 1.39× (z +3.2, 5/36 lines), [[FSBP]] 1.24× (z +3.1, 4/44 lines), [[RARB]] 1.22× (z +3.1, 4/20 lines), [[ZNF385B]] 1.35× (z +3.0, 1/24 lines), [[STPG1]] 1.22× (z +2.8, 8/44 lines), [[KCNH1]] 1.33× (z +2.7, 2/31 lines)

**5 µM** (3 genes, none with an alert): [[DHRS3]] 1.24× (z +5.1, 19/36 lines), [[ZBTB14]] 1.31× (z +4.8, 22/48 lines), [[RARB]] 1.20× (z +4.1, 10/21 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[LMF2]] 0.791× (z -3.2, 4/44 lines)

**0.5 µM** (3 genes, none with an alert): [[SLC43A1]] 0.737× (z -3.8, 9/36 lines), [[PRSS16]] 0.717× (z -3.4, 6/27 lines), [[PARP3]] 0.758× (z -3.0, 9/39 lines)

**5 µM** (20 genes, none with an alert; 12 shown): [[ABCG1]] 0.335× (z -16.5, 30/34 lines), [[ABCA1]] 0.503× (z -11.5, 28/29 lines), [[MYLIP]] 0.647× (z -7.3, 40/48 lines), [[KLF9]] 0.753× (z -6.8, 27/44 lines), [[SCD]] 0.750× (z -5.9, 35/49 lines), [[LPCAT3]] 0.832× (z -4.9, 20/48 lines), [[PARD6G]] 0.800× (z -4.5, 7/37 lines), [[SREBF1]] 0.755× (z -4.3, 30/49 lines), [[CPM]] 0.802× (z -4.2, 15/48 lines), [[TMEM135]] 0.832× (z -4.2, 20/49 lines), [[CHAMP1]] 0.818× (z -3.7, 13/48 lines), [[OLMALINC]] 0.823× (z -3.7, 19/47 lines)

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
| 5 µM | — | [[COLO 205 (line)]] (1.46), [[H4 (line)]] (1.42), [[HOP62 (line)]] (1.37), [[SNU-1 (line)]] (1.31) · weakest: [[A-427 (line)]] (0.417), [[AN3 CA (line)]] (0.422), [[SW48 (line)]] (0.501) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Artesunate (drug)]] (+0.42, JAK/STAT inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Belumosudil (mesylate) (drug)]] (+0.42, unclear); [[Neratinib (maleate) (drug)]] (+0.35, EGFR/ERBB inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Resveratrol (drug)]] (+0.32, unclear); [[5-Azacytidine (drug)]] (+0.32, DNA methyltransferase inhibitor); [[18β-Glycyrrhetinic acid (drug)]] (+0.30, unclear); [[Bortezomib (drug)]] (+0.29, Proteasome inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Posaconazole (drug)]] (+0.29, unclear); [[Neratinib (drug)]] (+0.26, EGFR/ERBB inhibitor); [[Dihydroartemisinin (drug)]] (+0.24, unclear); [[ULK-101 (drug)]] (+0.24, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[CACNG7]] | 0.5 µM | B | CACNG7 activity lowers the cells' numbers under Clotrimazole 0.5 µM (makes them more sensitive) | lines that do not express CACNG7 (21) vs lines expressing it (27) | the lines without CACNG7: 1.18× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[SEMA4G]] | 0.5 µM | C | SEMA4G activity raises the cells' numbers under Clotrimazole 0.5 µM (protects the cells) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 0.79× the cells of the other lines | 0.017 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| [[CHCHD10]] | 0.5 µM | C | CHCHD10 activity raises the cells' numbers under Clotrimazole 0.5 µM (protects the cells) | lines that do not express CHCHD10 (5) vs lines expressing it (43) | the lines without CHCHD10: 0.78× the cells of the other lines | 0.021 | ⚠ tissue-confounded; across organs |
| [[NR3C1]] | 0.5 µM | C | NR3C1 activity lowers the cells' numbers under Clotrimazole 0.5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.17× the cells of the other lines | 0.055 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[C2orf74]] | 0.5 µM | C | C2orf74 activity lowers the cells' numbers under Clotrimazole 0.5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.16× the cells of the other lines | 0.055 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[ENSG00000286964]] | 0.5 µM | C | ENSG00000286964 activity lowers the cells' numbers under Clotrimazole 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.17× the cells of the other lines | 0.056 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |
| [[LIFR]] | 0.5 µM | C | LIFR activity lowers the cells' numbers under Clotrimazole 0.5 µM (makes them more sensitive) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 1.16× the cells of the other lines | 0.063 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| [[SPART-AS1]] | 0.5 µM | C | SPART-AS1 activity lowers the cells' numbers under Clotrimazole 0.5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.13× the cells of the other lines | 0.091 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[FIGN]] | 0.5 µM | C | FIGN activity lowers the cells' numbers under Clotrimazole 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.13× the cells of the other lines | 0.095 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Clotrimazole"
- `tables/drugdoses.parquet` — dd in 284, 285, 286
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
