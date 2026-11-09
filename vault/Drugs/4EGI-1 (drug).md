---
drug: "4EGI-1"
type: "drug"
salt_base: "4EGI-1"
targets: "EIF4E"
moa_fine: "Protein synthesis inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 174
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# 4EGI-1

*Protein synthesis inhibitor (inhibitor/antagonist) · targets: EIF4E · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 174 / 137; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.04 / 0.12.
> Flags by dose: - / cell-cycle shift; noisy plate (z scaled) / noisy plate (z scaled). ⚠ 0.5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:F12 | 2 / 0 | — | -0.16 | -1.4/-0.5/-0.1 | — |
| 0.5 µM | [[Plate 02]]:F12 | 28 / 146 | — | +0.55 | -4.0/-3.3/-2.4 | ⚠ cell-cycle shift · noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:F12 | 61 / 76 | — | -0.44 | -2.9/-0.9/-0.8 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[PHF13]] 1.21× (z +3.5, 7/48 lines), [[TM4SF19]] 1.24× (z +2.8, 5/28 lines)

**0.5 µM** (28 genes, 20 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 17 shown): [[MCTP1]] 1.42× (z +4.2, 18/35 lines; cell-cycle shift (explains ~0% here)), [[SUPT3H]] ⚠ 1.37× (z +3.9, 33/47 lines; cell-cycle shift, explains ~60% of this change), [[NAV2]] 1.35× (z +3.5, 20/31 lines; cell-cycle shift (explains ~15% here)), [[ZHX2]] ⚠ 1.31× (z +3.4, 18/41 lines; cell-cycle shift, explains ~49% of this change), [[UTP25]] ⚠ 1.23× (z +3.4, 3/48 lines; cell-cycle shift, explains ~23% of this change), [[ZFPM2-AS1]] 1.30× (z +3.4, 13/32 lines; cell-cycle shift (explains ~0% here)), [[GNG12-AS1]] ⚠ 1.40× (z +3.4, 8/45 lines; cell-cycle shift, explains ~37% of this change), [[DOCK11]] ⚠ 1.31× (z +3.3, 8/35 lines; cell-cycle shift, explains ~54% of this change), [[ENSG00000259363]] ⚠ 1.45× (z +3.2, 10/30 lines; cell-cycle shift, explains ~65% of this change), [[TPT1-AS1]] ⚠ 1.26× (z +3.2, 9/48 lines; cell-cycle shift, explains ~73% of this change), [[GAB2]] ⚠ 1.27× (z +3.2, 13/46 lines; cell-cycle shift, explains ~78% of this change), [[VMP1]] ⚠ 1.23× (z +3.2, 22/48 lines; cell-cycle shift, explains ~21% of this change), [[HMGA2]] 1.43× (z +3.1, 18/39 lines; cell-cycle shift (explains ~17% here)), [[DUSP5-DT]] 1.52× (z +3.1, 4/41 lines; cell-cycle shift (explains ~11% here)), [[BACH2]] 1.26× (z +3.0, 6/41 lines; cell-cycle shift (explains ~6% here)), [[PEPD]] 1.26× (z +2.8, 3/48 lines; cell-cycle shift (explains ~0% here)), [[RPGR]] 1.21× (z +2.7, 4/48 lines; cell-cycle shift (explains ~0% here))

**5 µM** (61 genes, none with an alert; 12 shown): [[ITGA1]] 1.51× (z +4.7, 10/30 lines), [[BEAN1]] 1.92× (z +4.3, 4/24 lines), [[WFDC3]] 2.03× (z +4.0, 12/28 lines), [[DNTTIP1]] 1.58× (z +3.8, 22/48 lines), [[ENSG00000225339]] 1.84× (z +3.8, 16/41 lines), [[DUSP5-DT]] 1.98× (z +3.7, 9/33 lines), [[MBP]] 1.37× (z +3.7, 13/39 lines), [[ARSG]] 1.63× (z +3.6, 14/38 lines), [[CEMIP]] 1.92× (z +3.6, 8/29 lines), [[AHNAK2]] 1.77× (z +3.6, 22/36 lines), [[ABRAXAS1]] 1.52× (z +3.5, 2/42 lines), [[GK]] 1.64× (z +3.5, 10/39 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (146 genes, 108 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 21 shown): [[PSAT1]] 0.610× (z -4.5, 18/40 lines; cell-cycle shift (explains ~7% here)), [[CLSPN]] ⚠ 0.509× (z -4.4, 28/44 lines; cell-cycle shift, explains ~68% of this change), [[LAPTM4B]] ⚠ 0.768× (z -4.2, 16/44 lines; cell-cycle shift, explains ~42% of this change), [[FAM111B]] ⚠ 0.504× (z -4.2, 17/38 lines; cell-cycle shift, explains ~73% of this change), [[PHGDH]] 0.618× (z -4.2, 22/43 lines; cell-cycle shift (explains ~8% here)), [[RDH11]] ⚠ 0.661× (z -4.2, 30/48 lines; cell-cycle shift, explains ~26% of this change), [[PBK]] ⚠ 0.597× (z -4.1, 21/44 lines; cell-cycle shift, explains ~64% of this change), [[MCM10]] ⚠ 0.609× (z -4.0, 12/44 lines; cell-cycle shift, explains ~86% of this change), [[RAD51AP1]] ⚠ 0.658× (z -4.0, 18/46 lines; cell-cycle shift, explains ~72% of this change), [[ESCO2]] ⚠ 0.588× (z -4.0, 14/47 lines; cell-cycle shift, explains ~81% of this change), [[GPT2]] 0.703× (z -4.0, 16/46 lines; cell-cycle shift (explains ~0% here)), [[E2F7]] ⚠ 0.739× (z -4.0, 9/43 lines; cell-cycle shift, explains ~49% of this change), [[DIXDC1]] 0.761× (z -3.9, 10/48 lines; cell-cycle shift (explains ~1% here)), [[APLP1]] 0.639× (z -3.7, 5/36 lines; cell-cycle shift (explains ~25% here)), [[UGT1A1]] 0.389× (z -3.7, 2/11 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000230615]] 0.677× (z -3.5, 3/23 lines; cell-cycle shift (explains ~13% here)), [[ITGB6]] 0.730× (z -3.5, 1/16 lines; cell-cycle shift (explains ~1% here)), [[P2RY6]] 0.610× (z -3.4, 2/19 lines; cell-cycle shift (explains ~6% here)), [[CYP4F3]] 0.562× (z -3.4, 3/19 lines; cell-cycle shift (explains ~0% here)), [[FAM162A]] 0.570× (z -3.4, 37/47 lines; cell-cycle shift (explains ~20% here)), [[GPX8]] 0.695× (z -3.3, 12/40 lines; cell-cycle shift (explains ~4% here))

**5 µM** (76 genes, none with an alert; 12 shown): [[RAD54B]] 0.618× (z -4.9, 26/48 lines), [[MIR924HG]] 0.492× (z -4.6, 24/40 lines), [[DIAPH3]] 0.674× (z -4.4, 21/45 lines), [[CHUK]] 0.666× (z -4.0, 15/47 lines), [[POLQ]] 0.606× (z -4.0, 21/46 lines), [[TLCD4]] 0.660× (z -4.0, 12/32 lines), [[TENT5A]] 0.647× (z -4.0, 19/37 lines), [[MYBL2]] 0.496× (z -3.9, 21/41 lines), [[RAD54L]] 0.552× (z -3.9, 15/45 lines), [[PALS1]] 0.748× (z -3.9, 23/48 lines), [[HELLS]] 0.576× (z -3.8, 17/48 lines), [[BUD13]] 0.690× (z -3.8, 7/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 170]] (+2.1), [[Module 124]] (+2.0) | — |
| 5 µM | — | [[Module 006]] (-2.5) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Hs 766T (line)]] (1.55), [[SNU-1 (line)]] (1.54), [[MIA PaCa-2 (line)]] (1.43), [[H4 (line)]] (1.33) · weakest: [[SW1417 (line)]] (0.612), [[BT-474 (line)]] (0.641), [[HepG2_C3A (line)]] (0.647) |
| 5 µM | [[Hs 766T (line)]] (-4.2), [[HCT15 (line)]] (-3.9), [[LoVo (line)]] (-3.7) | [[Hs 766T (line)]] (1.40), [[NCI-H1573 (line)]] (1.28), [[H4 (line)]] (1.26), [[LS 180 (line)]] (1.24) · weakest: [[SW 1271 (line)]] (0.577), [[NCI-H661 (line)]] (0.657), [[SW1417 (line)]] (0.658) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[BAY1125976 (drug)]] (+0.80, PI3K/AKT inhibitor); [[Dabrafenib (drug)]] (+0.61, RAF inhibitor); [[ULK-101 (drug)]] (+0.58, unclear); [[Ivermectin (drug)]] (+0.56, unclear); [[Larotrectinib sulfate (drug)]] (+0.51, Other TK inhibitor, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Rapamycin (drug)]] (+0.49, MTOR inhibitor); [[Pexidartinib (hydrochloride) (drug)]] (+0.48, Multi-TK inhibitor); [[Fenofibrate (drug)]] (+0.46, unclear); [[Cilostazol (drug)]] (+0.43, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[EPHA1-AS1]] | 5 µM | B | EPHA1-AS1 activity lowers the cells' numbers under 4EGI-1 5 µM (makes them more sensitive) | lines that do not express EPHA1-AS1 (6) vs lines expressing it (42) | the lines without EPHA1-AS1: 1.35× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[ENSG00000225647]] | 5 µM | B | ENSG00000225647 activity lowers the cells' numbers under 4EGI-1 5 µM (makes them more sensitive) | lines that do not express ENSG00000225647 (10) vs lines expressing it (38) | the lines without ENSG00000225647: 1.23× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: BTBD6, CPA6; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "4EGI-1"
- `tables/drugdoses.parquet` — dd in 9, 10, 11
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
