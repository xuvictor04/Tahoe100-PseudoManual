---
drug: "Glycyrrhizic acid"
type: "drug"
salt_base: "Glycyrrhizic acid"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 269
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Glycyrrhizic acid

*unclear (inhibitor/antagonist) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 218 / 269 / 29; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.11 / 0.06.
> Flags by dose: - / low cells (technical?) / -.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:G5 | 195 / 23 | — | -0.66 | -0.7/+0.2/+0.8 | — |
| 0.5 µM | [[Plate 08]]:G5 | 106 / 163 | — | -1.10 | -0.2/-0.7/-0.4 | low cells (technical?) |
| 5 µM | [[Plate 09]]:G5 | 1 / 28 | — | +0.12 | -0.5/+0.7/-0.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (195 genes, none with an alert; 12 shown): [[ANK1]] 1.56× (z +5.5, 3/22 lines), [[ENSG00000285822]] 1.68× (z +5.0, 1/9 lines), [[LINC02864]] 1.48× (z +4.8, 0/12 lines), [[CYP24A1]] 1.78× (z +4.5, 2/9 lines), [[MUC6]] 2.81× (z +4.3, 0/3 lines), [[LINGO2]] 1.31× (z +4.3, 2/20 lines), [[LINC00649]] 1.62× (z +4.2, 4/16 lines), [[SMPD3]] 1.57× (z +4.2, 2/15 lines), [[UNC5D]] 1.72× (z +4.2, 0/9 lines), [[CRLF2]] 1.82× (z +4.2, 4/11 lines), [[ENSG00000231937]] 1.72× (z +4.1, 1/10 lines), [[NCAM1]] 1.50× (z +4.1, 4/12 lines)

**0.5 µM** (106 genes, none with an alert; 12 shown): [[PRPF4B]] 1.24× (z +5.3, 29/48 lines), [[ATP1A1-AS1]] 1.40× (z +4.8, 15/46 lines), [[MALAT1]] 1.29× (z +4.6, 47/48 lines), [[CHD1]] 1.23× (z +4.5, 29/48 lines), [[TARDBP]] 1.27× (z +4.4, 30/48 lines), [[RELCH]] 1.23× (z +4.0, 19/48 lines), [[ENSG00000290792]] 1.45× (z +4.0, 7/43 lines), [[FAM209A]] 1.42× (z +4.0, 4/40 lines), [[KPNA1]] 1.24× (z +3.9, 23/48 lines), [[SUGT1P4-STRA6LP-CCDC180]] 1.49× (z +3.8, 9/34 lines), [[PHRF1]] 1.24× (z +3.8, 17/48 lines), [[ENSG00000272335]] 1.33× (z +3.8, 9/45 lines)

**5 µM** (1 gene, none with an alert): [[CNPPD1]] 1.25× (z +3.4, 8/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (23 genes, none with an alert; 12 shown): [[ZNF35]] 0.694× (z -5.4, 18/42 lines), [[REEP3]] 0.804× (z -4.9, 27/47 lines), [[ENSG00000228434]] 0.670× (z -4.5, 14/34 lines), [[ENSG00000279598]] 0.619× (z -4.4, 16/29 lines), [[ARSK]] 0.752× (z -4.2, 18/45 lines), [[BRCC3]] 0.805× (z -3.9, 23/47 lines), [[PDLIM1]] 0.799× (z -3.8, 12/35 lines), [[TLCD4]] 0.818× (z -3.7, 15/33 lines), [[AASS]] 0.828× (z -3.6, 16/40 lines), [[DTWD2]] 0.771× (z -3.5, 12/44 lines), [[ENSG00000281593]] 0.797× (z -3.5, 21/45 lines), [[GPAM]] 0.813× (z -3.4, 13/44 lines)

**0.5 µM** (163 genes, none with an alert; 12 shown): [[CD68]] 0.548× (z -7.2, 38/41 lines), [[KIF5C]] 0.674× (z -6.3, 20/47 lines), [[NUMBL]] 0.726× (z -6.2, 23/47 lines), [[CITED2]] 0.575× (z -6.1, 40/45 lines), [[PLBD2]] 0.735× (z -6.0, 30/48 lines), [[ATN1]] 0.731× (z -5.6, 32/48 lines), [[PPP1R13L]] 0.762× (z -5.2, 25/42 lines), [[SELENON]] 0.685× (z -5.2, 24/45 lines), [[PIGT]] 0.747× (z -4.9, 25/48 lines), [[PLP2]] 0.641× (z -4.9, 33/44 lines), [[CYP2S1]] 0.632× (z -4.8, 18/27 lines), [[KXD1]] 0.704× (z -4.7, 34/47 lines)

**5 µM** (28 genes, none with an alert; 12 shown): [[FREM2]] 0.663× (z -4.2, 3/16 lines), [[ENSG00000273489]] 0.641× (z -4.1, 7/34 lines), [[TBC1D10B]] 0.775× (z -4.0, 15/47 lines), [[MUC17]] 0.558× (z -3.9, 0/4 lines), [[TARID]] 0.741× (z -3.8, 1/18 lines), [[VSTM2L]] 0.628× (z -3.8, 3/19 lines), [[MYRFL]] 0.690× (z -3.6, 10/32 lines), [[SYN2]] 0.704× (z -3.6, 10/20 lines), [[BMPR1B]] 0.789× (z -3.5, 4/20 lines), [[ENSG00000242396]] 0.683× (z -3.5, 8/33 lines), [[TLCD4-RWDD3]] 0.715× (z -3.4, 6/30 lines), [[AMER1]] 0.689× (z -3.4, 9/42 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Module 048]] (-2.7), [[Module 118]] (-2.1) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[RKO (line)]] (-6.3), [[C-33 A (line)]] (-4.8), [[CHP-212 (line)]] (-3.8), [[Hs 766T (line)]] (-3.6), [[SHP-77 (line)]] (-3.4) | [[CHP-212 (line)]] (2.36), [[AN3 CA (line)]] (2.25), [[C-33 A (line)]] (2.01), [[RKO (line)]] (1.78) · weakest: [[NCI-H1792 (line)]] (0.316), [[PANC-1 (line)]] (0.326), [[NCI-H2347 (line)]] (0.349) |
| 0.5 µM | [[SNU-423 (line)]] (-3.5) | [[SW 1271 (line)]] (1.42), [[CHP-212 (line)]] (1.19), [[SK-MEL-2 (line)]] (1.19), [[NCI-H661 (line)]] (1.17) · weakest: [[LS 180 (line)]] (0.779), [[A-172 (line)]] (0.782), [[RPMI-7951 (line)]] (0.826) |
| 5 µM | — | [[RKO (line)]] (1.76), [[SNU-1 (line)]] (1.73), [[SNU-423 (line)]] (1.57), [[NCI-H1792 (line)]] (1.52) · weakest: [[SW 1088 (line)]] (-0.303), [[AN3 CA (line)]] (0.352), [[SW 1271 (line)]] (0.396) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Tadalafil (drug)]] (+0.68, unclear); [[Imiquimod (maleate) (drug)]] (+0.53, unclear); [[Dapagliflozin (drug)]] (+0.46, Glucose transporter inhibitor); [[Sildenafil (drug)]] (+0.42, unclear, ⚠ only 5 significant genes); [[Dihydroartemisinin (drug)]] (+0.42, unclear); [[MK-8353 (drug)]] (+0.40, Other MAPK inhibitor); [[Adenosine (drug)]] (+0.38, unclear, ⚠ only 9 significant genes); [[Trimetrexate (drug)]] (+0.38, DNA synthesis/repair inhibitor); [[Orlistat (drug)]] (+0.38, unclear); [[Elagolix sodium (drug)]] (+0.37, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 25 arrows, 25 of them with an alert ⚠; grade A 0, B 7, C 18. Shown: the 15 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[NT5E]] | 0.05 µM | B | NT5E activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express NT5E (14) vs lines expressing it (34) | the lines without NT5E: 0.70× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[GSTA4]] | 0.5 µM | B | GSTA4 activity lowers the cells' numbers under Glycyrrhizic acid 0.5 µM (makes them more sensitive) | lines that do not express GSTA4 (5) vs lines expressing it (43) | the lines without GSTA4: 1.22× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PHGDH, P3H3; maybe low, not absent |
| [[INPP4B]] | 0.05 µM | B | INPP4B activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express INPP4B (10) vs lines expressing it (38) | the lines without INPP4B: 0.68× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[CAV2]], [[ENSG00000237813]] | 0.05 µM | B | CAV2, ENSG00000237813 activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express CAV2, ENSG00000237813 (8) vs lines expressing them (40) | the lines without CAV2, ENSG00000237813: 0.62× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent; co-absent genes |
| [[LIN7A]] | 0.05 µM | B | LIN7A activity lowers the cells' numbers under Glycyrrhizic acid 0.05 µM (makes them more sensitive) | lines that do not express LIN7A (34) vs lines expressing it (14) | the lines without LIN7A: 1.16× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1 |
| [[RAB32]] | 0.05 µM | B | RAB32 activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express RAB32 (7) vs lines expressing it (41) | the lines without RAB32: 0.57× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| [[F11R]] | 0.5 µM | B | F11R activity raises the cells' numbers under Glycyrrhizic acid 0.5 µM (protects the cells) | lines that do not express F11R (10) vs lines expressing it (38) | the lines without F11R: 0.93× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |
| [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] | 0.05 µM | C | ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.50× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| [[ENSG00000285458]] | 0.05 µM | C | ENSG00000285458 activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express ENSG00000285458 (5) vs lines expressing it (43) | the lines without ENSG00000285458: 0.60× the cells of the other lines | 0.011 | ⚠ tissue-confounded; across organs; also absent: TBILA, GCA, RILP; maybe low, not absent |
| [[DDR1]] | 0.05 µM | C | DDR1 activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 0.54× the cells of the other lines | 0.012 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| [[RILP]] | 0.05 µM | C | RILP activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.53× the cells of the other lines | 0.014 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| [[SCAMP5]] | 0.5 µM | C | SCAMP5 activity raises the cells' numbers under Glycyrrhizic acid 0.5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.67× the cells of the other lines | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| [[GSTP1]] | 0.5 µM | C | GSTP1 activity raises the cells' numbers under Glycyrrhizic acid 0.5 µM (protects the cells) | lines that do not express GSTP1 (5) vs lines expressing it (43) | the lines without GSTP1: 0.75× the cells of the other lines | 0.039 | ⚠ tissue-confounded; across organs; also absent: MARVELD1 |
| [[ACCS]] | 0.05 µM | C | ACCS activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 0.64× the cells of the other lines | 0.040 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| [[PLEKHN1]] | 0.05 µM | C | PLEKHN1 activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 0.57× the cells of the other lines | 0.044 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Glycyrrhizic acid"
- `tables/drugdoses.parquet` — dd in 510, 511, 512
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
