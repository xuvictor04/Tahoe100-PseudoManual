---
drug: "Doxycycline (monohydrate)"
type: "drug"
salt_base: "Doxycycline"
targets: "MMP7, MMP8, MMP9, MMP13, MMP14"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 51
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Doxycycline (monohydrate)

*unclear (inhibitor/antagonist) · targets: MMP7, MMP8, MMP9, MMP13, MMP14 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 51 / 36; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.31 / 0.06.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:D7 | 0 / 3 | — | -0.29 | +0.4/+0.5/+0.4 | — |
| 0.5 µM | [[Plate 08]]:D7 | 2 / 49 | — | -0.51 | +0.6/+0.8/+0.4 | — |
| 5 µM | [[Plate 09]]:D7 | 18 / 18 | — | -0.36 | +0.4/+0.6/+0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (2 genes, none with an alert): [[IRF4]] 1.69× (z +3.3, 0/9 lines), [[PON3]] 1.30× (z +2.9, 0/25 lines)

**5 µM** (18 genes, none with an alert; 12 shown): [[DBN1]] 1.45× (z +4.3, 27/44 lines), [[NSMF]] 1.40× (z +3.8, 18/45 lines), [[TSPAN15]] 1.35× (z +3.8, 15/32 lines), [[MT-CO2]] 1.41× (z +3.7, 33/47 lines), [[KLC2]] 1.39× (z +3.7, 7/46 lines), [[TMTC4]] 1.27× (z +3.7, 10/46 lines), [[TEAD2]] 1.36× (z +3.6, 2/37 lines), [[MT-RNR1]] 1.88× (z +3.5, 47/47 lines), [[ARHGEF25]] 1.54× (z +3.4, 3/27 lines), [[FBXO4]] 1.32× (z +3.4, 6/45 lines), [[TMEM183A]] 1.29× (z +3.2, 11/47 lines), [[CDNF]] 1.46× (z +3.2, 3/35 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[TNKS1BP1]] 0.745× (z -3.5, 25/48 lines), [[SHC2]] 0.726× (z -3.2, 7/36 lines), [[FCHSD1]] 0.749× (z -3.1, 10/43 lines)

**0.5 µM** (49 genes, none with an alert; 12 shown): [[MBD6]] 0.693× (z -5.1, 21/47 lines), [[MTND2P28]] 0.533× (z -4.4, 23/46 lines), [[KDM6B]] 0.726× (z -4.2, 31/47 lines), [[FBRS]] 0.772× (z -4.2, 22/47 lines), [[NDST2]] 0.710× (z -4.1, 7/45 lines), [[CPNE7]] 0.705× (z -4.1, 16/35 lines), [[MT-ND4L]] 0.558× (z -4.0, 36/47 lines), [[INF2]] 0.784× (z -3.9, 18/47 lines), [[CYP2S1]] 0.689× (z -3.9, 11/28 lines), [[MT-ND1]] 0.553× (z -3.9, 47/47 lines), [[AMDHD2]] 0.735× (z -3.6, 10/46 lines), [[PRR36]] 0.641× (z -3.6, 9/27 lines)

**5 µM** (18 genes, none with an alert; 12 shown): [[FKBP14]] 0.781× (z -3.9, 17/47 lines), [[SPART-AS1]] 0.652× (z -3.9, 5/26 lines), [[FAXDC2]] 0.737× (z -3.8, 3/45 lines), [[MAP1LC3B2]] 0.673× (z -3.8, 9/43 lines), [[AKAP13-AS1]] 0.686× (z -3.8, 9/44 lines), [[CPA4]] 0.616× (z -3.8, 7/19 lines), [[BLZF1]] 0.769× (z -3.8, 29/47 lines), [[ENSG00000228793]] 0.705× (z -3.7, 5/40 lines), [[SPATA32]] 0.638× (z -3.5, 6/34 lines), [[CA9]] 0.643× (z -3.4, 11/27 lines), [[MYPN]] 0.727× (z -3.4, 2/19 lines), [[SGIP1]] 0.704× (z -3.3, 4/16 lines)

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
| 0.5 µM | [[A498 (line)]] (-3.9), [[HOP62 (line)]] (-3.4) | [[A549 (line)]] (1.59), [[HepG2_C3A (line)]] (1.47), [[COLO 205 (line)]] (1.29), [[AN3 CA (line)]] (1.22) · weakest: [[SW 1271 (line)]] (0.647), [[A-172 (line)]] (0.783), [[J82 (line)]] (0.804) |
| 5 µM | [[HS-578T (line)]] (-4.0), [[HOP62 (line)]] (-3.8), [[J82 (line)]] (-3.4), [[A549 (line)]] (-3.4), [[Hs 766T (line)]] (-3.1) | [[HT-29 (line)]] (1.46), [[COLO 205 (line)]] (1.43), [[Panc 03.27 (line)]] (1.37), [[AsPC-1 (line)]] (1.31) · weakest: [[HepG2_C3A (line)]] (0.457), [[PANC-1 (line)]] (0.474), [[H4 (line)]] (0.497) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Bisoprolol (hemifumarate) (drug)]] (+0.77, Adrenoceptor agonist); [[Ribociclib (drug)]] (+0.71, CDK inhibitor, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only; position not correctable)); [[Diammonium Glycyrrhizinate (drug)]] (+0.59, unclear); [[Adenosine (drug)]] (+0.59, unclear, ⚠ only 9 significant genes); [[Allantoin (drug)]] (+0.54, unclear); [[Acetohexamide (drug)]] (+0.52, unclear); [[Loperamide (hydrochloride) (drug)]] (+0.50, unclear); [[Norepinephrine (hydrochloride) (drug)]] (+0.50, Adrenoceptor agonist); [[Berbamine (drug)]] (+0.50, unclear); [[Brimonidine (drug)]] (+0.49, Adrenoceptor agonist)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 27 arrows, 27 of them with an alert ⚠; grade A 0, B 12, C 15. Shown: the 15 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PLEKHG3]] | 5 µM | B | PLEKHG3 activity raises the cells' numbers under Doxycycline (monohydrate) 5 µM (protects the cells) | lines that do not express PLEKHG3 (5) vs lines expressing it (43) | the lines without PLEKHG3: 0.72× the cells of the other lines | 0.051 | ⚠ across organs; also absent: ATP11A, SHC2, PPP1R26; maybe low, not absent |
| [[BNC2]] | 5 µM | B | BNC2 activity lowers the cells' numbers under Doxycycline (monohydrate) 5 µM (makes them more sensitive) | lines that do not express BNC2 (21) vs lines expressing it (27) | the lines without BNC2: 1.37× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[GJA1]] | 5 µM | B | GJA1 activity lowers the cells' numbers under Doxycycline (monohydrate) 5 µM (makes them more sensitive) | lines that do not express GJA1 (26) vs lines expressing it (22) | the lines without GJA1: 1.36× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| [[KCNH8]] | 5 µM | B | KCNH8 activity raises the cells' numbers under Doxycycline (monohydrate) 5 µM (protects the cells) | lines that do not express KCNH8 (32) vs lines expressing it (16) | the lines without KCNH8: 0.74× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| [[ENSG00000230615]] | 0.5 µM | B | ENSG00000230615 activity lowers the cells' numbers under Doxycycline (monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.32× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[PCDH1]] | 5 µM | B | PCDH1 activity raises the cells' numbers under Doxycycline (monohydrate) 5 µM (protects the cells) | lines that do not express PCDH1 (20) vs lines expressing it (28) | the lines without PCDH1: 0.83× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[ANKRD22]] | 5 µM | B | ANKRD22 activity raises the cells' numbers under Doxycycline (monohydrate) 5 µM (protects the cells) | lines that do not express ANKRD22 (34) vs lines expressing it (14) | the lines without ANKRD22: 0.72× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity lowers the cells' numbers under Doxycycline (monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.29× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[CGN]] | 5 µM | B | CGN activity raises the cells' numbers under Doxycycline (monohydrate) 5 µM (protects the cells) | lines that do not express CGN (21) vs lines expressing it (27) | the lines without CGN: 0.74× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[EPCAM]] | 5 µM | B | EPCAM activity raises the cells' numbers under Doxycycline (monohydrate) 5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.76× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[SSPN]] | 0.5 µM | B | SSPN activity lowers the cells' numbers under Doxycycline (monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express SSPN (15) vs lines expressing it (33) | the lines without SSPN: 1.26× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| [[C12orf75-AS1]] | 0.5 µM | B | C12orf75-AS1 activity lowers the cells' numbers under Doxycycline (monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express C12orf75-AS1 (22) vs lines expressing it (26) | the lines without C12orf75-AS1: 1.27× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[PWWP2B]] | 0.5 µM | C | PWWP2B activity raises the cells' numbers under Doxycycline (monohydrate) 0.5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.63× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| [[FIGN]] | 0.5 µM | C | FIGN activity lowers the cells' numbers under Doxycycline (monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.24× the cells of the other lines | 0.026 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[SCAMP5]] | 5 µM | C | SCAMP5 activity raises the cells' numbers under Doxycycline (monohydrate) 5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.65× the cells of the other lines | 0.029 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Doxycycline (monohydrate)"
- `tables/drugdoses.parquet` — dd in 380, 381, 382
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
