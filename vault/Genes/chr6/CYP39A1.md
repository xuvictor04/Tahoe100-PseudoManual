---
symbol: "CYP39A1"
type: "gene"
col: 7075
ensembl_id: "ENSG00000146233"
name: "cytochrome P450 family 39 subfamily A member 1"
location: "6p12.3"
module: 45
arm: "+"
pooled_cpm: 4.1
n_lines_expressing: 36
n_dd_up: 37
n_dd_down: 10
n_dd_up_clean: 29
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# CYP39A1

*cytochrome P450 family 39 subfamily A member 1* — 6p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.89× (z +12.1, q 6e-31, up in 24 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.535× (z -5.6, q 1e-05, down in 16 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TDO2]] (+0.60, fdr 1e-05), [[MBNL2]] (+0.58, fdr 1e-05), [[NRG4]] (+0.56, fdr 1e-05); moves opposite to [[LINC01128]] (-0.52, fdr 2e-05), [[PPP3CB]] (-0.52, fdr 5e-05), [[ENTR1]] (-0.50, fdr 7e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NMRAL2P-1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LRP1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7075.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.89×** | +12.1 | 6e-31 | 24/32 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.30×** | +10.5 | 2e-23 | 21/31 (LS 180, C-33 A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.09×** | +10.1 | 2e-21 | 22/32 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.04×** | +9.9 | 5e-21 | 24/32 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.30×** | +9.6 | 1e-19 | 22/32 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +8.5 | 2e-15 | 21/32 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +8.4 | 3e-15 | 13/25 (HEC-1-A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.54×** | +8.3 | 8e-15 | 24/31 (H4, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +6.7 | 2e-09 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +6.4 | 9e-09 | 12/30 (LS 180, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +5.8 | 3e-07 | 6/16 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +5.6 | 1e-06 | 8/24 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.85×** | +5.5 | 2e-06 | 9/25 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +5.3 | 4e-06 | 11/20 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.85×** | +5.2 | 8e-06 | 13/29 (HOP62, A498, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.97×** | +5.1 | 1e-05 | 10/28 (HS-578T, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +4.8 | 4e-05 | 8/30 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7075.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.535×** | -5.6 | 1e-05 | 16/32 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.555×** | -5.3 | 4e-05 | 20/31 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.600×** | -4.6 | 9e-04 | 16/32 (AN3 CA, RKO, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.702×** | -4.5 | 9e-04 | 16/32 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.630×** | -4.2 | 0.004 | 16/23 (NCI-H460, HT-29, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.658×** | -3.8 | 0.015 | 9/31 (H4, SW 900, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.639×** | -3.7 | 0.020 | 11/27 (HepG2/C3A, H4, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.657×** | -3.4 | 0.040 | 12/31 (SW 900, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.693×** | -3.3 | 0.059 | 9/32 (SK-MEL-2, C-33 A, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.707×** | -3.1 | 0.099 | 3/31 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7075. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 18.1 | 0 | 4 (3 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.112× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 7.36 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0469× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 7.51 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0207× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 8.73 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0708× (z -10.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 3.39 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0321× (z -15.2) |
| [[A-172 (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.606 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.818 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.737 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.903 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7075), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TDO2]] | +0.60 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[MBNL2]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[NRG4]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CAPS2]] | +0.55 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ATP6V1A]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[CRISPLD1]] | +0.54 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[EFCAB7]] | +0.53 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[HMGN5]] | +0.53 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[CEP126]] | +0.53 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[PTGR1]] | +0.52 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[ARL6IP5]] | +0.52 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[TNRC6A]] | +0.51 | +0.36 / +0.54 | both halves | 9e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01128]] | -0.52 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[PPP3CB]] | -0.52 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[ENTR1]] | -0.50 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[ACTR3B]] | -0.49 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[BRD9]] | -0.48 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[SLC12A4]] | -0.46 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[ZBED4]] | -0.45 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[RIPK1]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[RAPGEFL1]] | -0.45 | -0.41 / -0.25 | both halves | 4e-04 |  |
| [[PARVB]] | -0.45 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[WDR27]] | -0.45 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[TECPR2]] | -0.44 | -0.21 / -0.44 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity raises CYP39A1's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without NMRAL2P-1 | 0.014 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[VEGFD]] | B | VEGFD activity raises CYP39A1's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.72× lower at baseline in the lines without VEGFD | 0.020 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[VAV3]] | B | VAV3 activity raises CYP39A1's level | lines that do not express VAV3 (30) vs lines expressing it (20) | 1.78× lower at baseline in the lines without VAV3 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RSPO3, ENSG00000289418, NRCAM |
| [[PIR]] | B | PIR activity raises CYP39A1's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.54× lower at baseline in the lines without PIR | 0.089 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP1B]] | B | CYP39A1 activity raises LRP1B's level | lines that do not express CYP39A1 (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without CYP39A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC25A27, ENSG00000259345; maybe low, not absent |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.420). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-4.6, 49.0); signed map (49.7, -13.8). **Vector** length 50.3, 8.46% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.4 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.0 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +10.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +8.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +2.8 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.7 | -4.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.6 | -3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 39 subfamily A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.3 — chr6:46,549,580-46,652,830 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cytochrome P450 family 39 |
| Hallmark sets | BILE_ACID_METABOLISM, KRAS_SIGNALING_DN |
| Reactome | 9 pathways, smallest: Synthesis of bile acids and bile salts via 24-hydroxycholesterol; Endogenous sterols; Synthesis of bile acids and bile salts |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYL5](https://www.uniprot.org/uniprotkb/Q9NYL5) (24-hydroxycholesterol 7-alpha-hydroxylase):

> A cytochrome P450 monooxygenase involved in neural cholesterol clearance through bile acid synthesis. Catalyzes 7-alpha hydroxylation of (24S)-hydroxycholesterol, a neural oxysterol that is metabolized to bile acids in the liver. Mechanistically, uses molecular oxygen inserting one oxygen atom into a substrate, and reducing the second into a water molecule, with two electrons provided by NADPH via cytochrome P450 reductase (CPR; NADPH-ferrihemoprotein reductase).

**Summary**, from NCBI Gene [51302](https://www.ncbi.nlm.nih.gov/gene/51302):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This endoplasmic reticulum protein is involved in the conversion of cholesterol to bile acids. Its substrates include the oxysterols 25-hydroxycholesterol, 27-hydroxycholesterol and 24-hydroxycholesterol. Alternate splicing results in multiple transcript …

**Accessions** — [HGNC:17449](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17449) · Entrez [51302](https://www.ncbi.nlm.nih.gov/gene/51302) · UniProt [Q9NYL5](https://www.uniprot.org/uniprotkb/Q9NYL5) · Ensembl [ENSG00000146233](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146233)

## Data

Gene col 7075: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7075); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7075, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7075]; `tensor/DDL_lfc|DDL_z.npy` [7075]; `embed/gene_vectors.npy` [7075]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7075 or target_col == 7075). Every well: [[CYP39A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP39A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
