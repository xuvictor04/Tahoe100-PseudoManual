---
symbol: "CAPN1-AS1"
type: "gene"
col: 14885
ensembl_id: "ENSG00000254614"
name: "CAPN1 antisense RNA 1"
location: "11q13.1"
module: 168
arm: "+"
pooled_cpm: 5.04
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# CAPN1-AS1

*CAPN1 antisense RNA 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.60× (z +10.3, q 5e-22, up in 16 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.45× (z +5.7, q 1e-06, up in 13 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.326× (z -16.9, q 0e+00, down in 30 of 33 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAP4-1]] (+0.58, fdr 1e-05), [[ZNF836]] (+0.58, fdr 2e-05), [[SDHAP4]] (+0.56, fdr 1e-05); moves opposite to [[MED1]] (-0.53, fdr 2e-05), [[CXCL10]] (-0.53, fdr 3e-05), [[MYCBP2]] (-0.50, fdr 2e-04).
> It sits in the **+** arm of [[Module 168]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +10.3 | 5e-22 | 16/24 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +8.4 | 2e-14 | 4/8 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +7.4 | 2e-11 | 17/24 (Panc 03.27, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +6.0 | 2e-07 | 9/15 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +5.7 | 1e-06 | 13/42 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +4.8 | 1e-04 | 15/39 (LS 180, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +4.0 | 0.004 | 10/26 (A-427, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.2 | 0.091 | 5/37 (HT-29, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14885.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.326×** | -16.9 | 0e+00 | 30/33 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.295×** | -13.0 | 2e-36 | 27/34 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.314×** | -11.9 | 2e-30 | 31/39 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.377×** | -10.4 | 3e-23 | 35/44 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.463×** | -8.2 | 2e-14 | 28/41 (Panc 03.27, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.490×** | -7.6 | 2e-12 | 25/41 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.505×** | -7.3 | 2e-11 | 24/44 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.513×** | -7.1 | 7e-11 | 21/41 (HEC-1-A, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.542×** | -6.5 | 4e-09 | 23/41 (AsPC-1, A-172, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.560×** | -6.2 | 4e-08 | 20/31 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.563×** | -6.1 | 4e-08 | 21/41 (NCI-H1792, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.589×** | -5.3 | 5e-06 | 19/38 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.619×** | -5.1 | 1e-05 | 18/39 (KATO III, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.431×** | -4.7 | 1e-04 | 16/30 (SNU-423, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.444×** | -4.5 | 2e-04 | 12/37 (KATO III, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.655×** | -4.3 | 7e-04 | 11/41 (Panc 03.27, LS 180, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.675×** | -4.2 | 1e-03 | 9/42 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.488×** | -4.0 | 0.002 | 18/38 (Panc 03.27, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.713×** | -3.6 | 0.009 | 11/41 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 20.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -13.1) |
| [[HOP62 (line)]] | alt | 6.93 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0867× (z -11.8) |
| [[KATO III (line)]] | alt | 11.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0313× (z -17.2) |
| [[AsPC-1 (line)]] | alt | 8.51 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 8.54 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0600× (z -20.4) |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0939× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0570× (z -24.3) |
| [[PANC-1 (line)]] | alt | 3.48 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0233× (z -17.5) |
| [[SNU-423 (line)]] | alt | 4.51 | 0 | 2 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0651× (z -9.7) |
| [[SW480 (line)]] | alt | 2.22 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0948× (z -12.7) |
| [[A-172 (line)]] | wt | 6.31 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0342× (z -14.1) |
| [[Hs 766T (line)]] | wt | 6.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -9.8) |
| [[LoVo (line)]] | wt | 5.08 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0933× (z -10.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LOX-IMVI (line)]] | wt | 2.42 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0427× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 6.65 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0802× (z -14.8) ⚠ cell-cycle shift, explains ~88% of this change |
| [[NCI-H2030 (line)]] | alt | 5.61 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 2.64 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0938× (z -9.3) |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -13.0) |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.814 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.855 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP4-1]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ZNF836]] | +0.58 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[SDHAP4]] | +0.56 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[RAP1A]] | +0.55 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[MED17]] | +0.54 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[DHRS1]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[NTAN1]] | +0.53 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[ZBTB34]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ARPC1A]] | +0.52 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[FRG1HP]] | +0.52 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[CDS2]] | +0.52 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[CAPG]] | +0.51 | +0.66 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED1]] | -0.53 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[CXCL10]] | -0.53 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[MYCBP2]] | -0.50 | -0.31 / -0.62 | both halves | 2e-04 |  |
| [[PRH1]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ITPR2]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[TAS2R14]] | -0.48 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[DDX60]] | -0.48 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[CDK12]] | -0.48 | -0.57 / -0.40 | both halves | 4e-05 |  |
| [[LRRC37A2]] | -0.47 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[CPSF2]] | -0.47 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[EIF2B5]] | -0.46 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[INO80]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-3.0, -15.1); signed map (-37.0, -9.1). **Vector** length 55.6, 8.17% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +7.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.7 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +4.8 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +1.7 | +3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +0.6 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.4 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -11.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -13.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | CAPN1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q13.1 — chr11:65,177,606-65,181,834 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56068) · Entrez [728975](https://www.ncbi.nlm.nih.gov/gene/728975) · Ensembl [ENSG00000254614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254614)

## Data

Gene col 14885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14885); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14885]; `tensor/DDL_lfc|DDL_z.npy` [14885]; `embed/gene_vectors.npy` [14885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14885 or target_col == 14885). Every well: [[CAPN1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPN1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
