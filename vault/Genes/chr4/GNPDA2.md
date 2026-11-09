---
symbol: "GNPDA2"
type: "gene"
col: 8661
ensembl_id: "ENSG00000163281"
name: "glucosamine-6-phosphate deaminase 2"
location: "4p12"
module: 57
arm: "+"
pooled_cpm: 16.11
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# GNPDA2

*glucosamine-6-phosphate deaminase 2* — 4p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.32× (z +17.2, q 0e+00, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[LY-2584702 (tosylate salt) (drug)]] 5 µM: 0.625× (z -5.1, q 2e-04, down in 12 of 29 measured lines) ⚠ toxic. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.786× (z -4.8, q 5e-04, down in 17 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC40]] (+0.77, fdr 7e-06), [[HSD17B4]] (+0.77, fdr 7e-06), [[ADH5]] (+0.72, fdr 7e-06); moves opposite to [[PKNOX1]] (-0.61, fdr 1e-05), [[HIVEP1]] (-0.57, fdr 1e-05), [[TNRC6C]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRP12]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.32×** | +17.2 | 0e+00 | 41/45 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.12×** | +15.4 | 0e+00 | 39/45 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.19×** | +13.3 | 6e-38 | 41/46 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +7.7 | 2e-12 | 20/40 (C-33 A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +7.5 | 1e-11 | 12/24 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +6.8 | 9e-10 | 24/46 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +6.5 | 6e-09 | 20/46 (A-427, SW 900, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +5.9 | 2e-07 | 17/45 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +5.9 | 3e-07 | 14/32 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.73×** | +5.9 | 3e-07 | 17/38 (A549, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.45×** | +5.4 | 4e-06 | 17/46 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.20× | +5.2 | 1e-05 | 13/46 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +4.5 | 2e-04 | 14/46 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | **1.24×** | +4.3 | 7e-04 | 17/40 (NCI-H460, hTERT-HPNE, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.001 | 6/46 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.003 | 10/45 (SW48, PANC-1, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.018 | 6/45 (HEC-1-A, J82, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8661.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.625×** | -5.1 | 2e-04 | 12/29 (NCI-H1792, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.786×** | -4.8 | 5e-04 | 17/46 (C32, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.797×** | -4.7 | 6e-04 | 17/45 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.810×** | -4.3 | 0.002 | 16/45 (Hs 766T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.865× | -4.2 | 0.003 | 15/45 (NCI-H460, NCI-H1573, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.817×** | -4.2 | 0.003 | 12/46 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.831×** | -3.8 | 0.011 | 11/45 (SNU-423, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.827×** | -3.6 | 0.023 | 12/45 (MIA PaCa-2, HOP62, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.885× | -3.6 | 0.023 | 13/45 (SNU-1, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -3.0 | 0.15 | 10/45 (hTERT-HPNE, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.2 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -13.1) ⚠ cell-cycle shift, explains ~1% of this change |
| [[HOP62 (line)]] | alt | 19.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.08× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 15.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.90× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 19.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.40× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 16.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.43× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 19.1 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.190× (z -9.1) |
| [[A-172 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC40]] | +0.77 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[HSD17B4]] | +0.77 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[ADH5]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[BLMH]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[NXPE3]] | +0.71 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[JKAMP]] | +0.70 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[RAD23B]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.69 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[RTCA]] | +0.68 | +0.76 / +0.44 | both halves | 3e-05 |  |
| [[EPDR1]] | +0.67 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[CASP6]] | +0.67 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[MRPL19]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKNOX1]] | -0.61 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[HIVEP1]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.56 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[CATSPERG]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP12]] | B | LRP12 activity raises GNPDA2's level | lines that do not express LRP12 (8) vs lines expressing it (42) | 1.67× lower at baseline in the lines without LRP12 | 0.096 | ⚠ within organs, on part of the lines; also absent: CFAP54, RNF217, RNF217-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.8, -7.6); signed map (-27.8, -21.5). **Vector** length 81.4, 15.9% of its response variance represented; |z| ≥ 3 in 782 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.8 | +17.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.6 | +13.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +15.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +5.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +5.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.5 | -4.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -4.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | -4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -3.8 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -0.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.9 | -1.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | glucosamine-6-phosphate deaminase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p12 — chr4:44,682,200-44,726,588 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SB52 |
| Reactome | 3 pathways, smallest: Glycolysis; Glucose metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDQ7](https://www.uniprot.org/uniprotkb/Q8TDQ7) (Glucosamine-6-phosphate deaminase 2):

> Catalyzes the reversible conversion of alpha-D-glucosamine 6-phosphate (GlcN-6P) into beta-D-fructose 6-phosphate (Fru-6P) and ammonium ion, a regulatory reaction step in de novo uridine diphosphate-N-acetyl-alpha-D-glucosamine (UDP-GlcNAc) biosynthesis via hexosamine pathway. Deamination is coupled to aldo-keto isomerization mediating the metabolic flux from UDP-GlcNAc toward Fru-6P. At high ammonium level can drive amination and isomerization of Fru-6P toward hexosamines and UDP-GlcNAc …

**Summary**, from NCBI Gene [132789](https://www.ncbi.nlm.nih.gov/gene/132789):

> The protein encoded by this gene is an allosteric enzyme that catalyzes the reversible reaction converting D-glucosamine-6-phosphate into D-fructose-6-phosphate and ammonium. Variations of this gene have been reported to be associated with influencing body mass index and susceptibility to obesity. A pseudogene of this gene is located on chromosome 9. Alternative splicing results in multiple transcript variants that encode different protein isoforms. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:21526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21526) · Entrez [132789](https://www.ncbi.nlm.nih.gov/gene/132789) · UniProt [Q8TDQ7](https://www.uniprot.org/uniprotkb/Q8TDQ7) · Ensembl [ENSG00000163281](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163281)

## Data

Gene col 8661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8661); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8661]; `tensor/DDL_lfc|DDL_z.npy` [8661]; `embed/gene_vectors.npy` [8661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8661 or target_col == 8661). Every well: [[GNPDA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNPDA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
