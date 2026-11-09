---
symbol: "JAK3"
type: "gene"
col: 2631
ensembl_id: "ENSG00000105639"
name: "Janus kinase 3"
location: "19p13.11"
module: 45
arm: "+"
pooled_cpm: 3.83
n_lines_expressing: 42
n_dd_up: 14
n_dd_down: 26
n_dd_up_clean: 13
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# JAK3

*Janus kinase 3* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.48× (z +6.5, q 5e-08, up in 14 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.344× (z -12.3, q 5e-32, down in 27 of 38 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.435× (z -9.6, q 1e-19, down in 26 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOC2A]] (+0.62, fdr 1e-05), [[VSIG10L]] (+0.60, fdr 1e-05), [[PCOLCE]] (+0.57, fdr 2e-05); moves opposite to [[LINC01956]] (-0.52, fdr 2e-04), [[MRPS16]] (-0.50, fdr 4e-05), [[ENOX2]] (-0.50, fdr 5e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ATP2A3]] → it (grade B ⚠); 5 go from it, the strongest it → [[CTDSPL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2631.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +6.5 | 5e-08 | 14/39 (LS 180, SNU-423, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +6.2 | 2e-07 | 14/32 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +5.7 | 2e-06 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.0 | 1e-04 | 11/29 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +4.4 | 0.001 | 8/36 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.002 | 6/39 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.017 | 6/39 (NCI-H2030, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.038 | 8/38 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.038 | 5/31 (NCI-H2030, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.049 | 3/37 (LS 180, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.053 | 2/36 (LS 180, LoVo) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.077 | 2/33 (SW480, NCI-H23) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.077 | 2/26 (Hs 766T, A549) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.077 | 1/30 (HepG2/C3A) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2631.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.344×** | -12.3 | 5e-32 | 27/38 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.384×** | -10.3 | 3e-22 | 23/35 (SW480, NCI-H23, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.435×** | -9.6 | 1e-19 | 26/36 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.462×** | -8.9 | 7e-17 | 17/25 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.595×** | -8.5 | 3e-15 | 21/31 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.501×** | -8.0 | 1e-13 | 19/35 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.501×** | -8.0 | 1e-13 | 21/36 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.581×** | -6.3 | 3e-08 | 18/28 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.368×** | -6.0 | 1e-07 | 17/33 (Panc 03.27, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.603×** | -5.8 | 3e-07 | 15/38 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.605×** | -5.8 | 4e-07 | 20/36 (HepG2/C3A, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.399×** | -5.5 | 1e-06 | 13/27 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.615×** | -5.2 | 8e-06 | 12/22 (NCI-H23, A549, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.643×** | -5.1 | 1e-05 | 15/38 (SW 900, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.655×** | -4.9 | 4e-05 | 12/34 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.655×** | -4.9 | 4e-05 | 15/36 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.516×** | -4.0 | 0.002 | 4/24 (CFPAC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.549×** | -3.6 | 0.009 | 6/26 (NCI-H460, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.802×** | -3.6 | 0.010 | 12/38 (AN3 CA, AsPC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.739×** | -3.5 | 0.014 | 11/37 (NCI-H460, LS 180, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.744×** | -3.4 | 0.016 | 6/34 (SW 900, CFPAC-1, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.598×** | -3.1 | 0.045 | 5/30 (A498, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.836× | -2.9 | 0.080 | 11/37 (HepG2/C3A, NCI-H23, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.780×** | -2.9 | 0.089 | 4/37 (HOP62, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2631. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 37.4 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.294× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 18.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0553× (z -24.0) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.210× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 3.12 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0556× (z -12.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.118× (z -8.9) |
| [[A549 (line)]] | wt | 4.77 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0723× (z -10.0) |
| [[PANC-1 (line)]] | alt | 5.05 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.100× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.177× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 6.61 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -12.6) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SW480 (line)]] | alt | 3.22 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0733× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 4.19 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0923× (z -8.9) |
| [[Hs 766T (line)]] | wt | 5.41 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0657× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.996 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.951 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.361 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2631), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOC2A]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[VSIG10L]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[PCOLCE]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[LMTK3]] | +0.56 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[CCDC88B]] | +0.56 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[HSF4]] | +0.54 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[CAPN12]] | +0.53 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[TNNI3]] | +0.53 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[GTF2IP4]] | +0.53 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[SIPA1]] | +0.52 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[ODF3B]] | +0.52 | +0.56 / +0.38 | both halves | 7e-05 |  |
| [[DUSP9]] | +0.52 | +0.57 / +0.35 | both halves | 1e-04 | pathway: MAPK family signaling cascades |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01956]] | -0.52 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[MRPS16]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ENOX2]] | -0.50 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[HLCS]] | -0.46 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[CPSF2]] | -0.45 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[ERCC6L2]] | -0.44 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[SCMH1]] | -0.44 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[RAB28]] | -0.44 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[VPS13B]] | -0.44 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[SH3D19]] | -0.43 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[TAOK1]] | -0.43 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[MAPKAP1]] | -0.43 | -0.43 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP2A3]] | B | ATP2A3 activity raises JAK3's level | lines that do not express ATP2A3 (16) vs lines expressing it (34) | 1.45× lower at baseline in the lines without ATP2A3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: WBP2NL, BEX4, NSUN7; maybe low, not absent |
| [[SEC14L4]] | B | SEC14L4 activity raises JAK3's level | lines that do not express SEC14L4 (29) vs lines expressing it (21) | 2.18× lower at baseline in the lines without SEC14L4 | 0.068 | ⚠ within organs, on part of the lines; also absent: WT1-AS, ACP7, PLTP |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTDSPL]] | B | [[JAK1]], JAK3 activity lowers CTDSPL's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[NALCN]] | B | [[JAK1]], JAK3 activity lowers NALCN's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[PTPRB]] | B | [[JAK1]], JAK3 activity lowers PTPRB's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[LYPD6B]] | B | [[JAK1]], JAK3 activity lowers LYPD6B's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ZNF704]] | B | [[JAK1]], JAK3 activity lowers ZNF704's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.402). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (23.4, -32.9); signed map (1.1, 11.7). **Vector** length 44.7, 5.81% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.5 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | -1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +3.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.7 | -6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -8.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.6 | -10.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.3 | -12.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | Janus kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,824,780-17,848,071 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L-JAK, JAKL, LJAK, JAK3_HUMAN, JAK-3 |
| Gene groups (HGNC) | Jak family tyrosine kinases |
| Reactome | 20 pathways, smallest: Interleukin-9 signaling; Interleukin-21 signaling; Interleukin-2 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P52333](https://www.uniprot.org/uniprotkb/P52333) (Tyrosine-protein kinase JAK3):

> Non-receptor tyrosine kinase involved in various processes such as cell growth, development, or differentiation. Mediates essential signaling events in both innate and adaptive immunity and plays a crucial role in hematopoiesis during T-cells development. In the cytoplasm, plays a pivotal role in signal transduction via its association with type I receptors sharing the common subunit gamma such as IL2R, IL4R, IL7R, IL9R, IL15R and IL21R. Following ligand binding to cell surface receptors, …

**Summary**, from NCBI Gene [3718](https://www.ncbi.nlm.nih.gov/gene/3718):

> The protein encoded by this gene is a member of the Janus kinase (JAK) family of tyrosine kinases involved in cytokine receptor-mediated intracellular signal transduction. It is predominantly expressed in immune cells and transduces a signal in response to its activation via tyrosine phosphorylation by interleukin receptors. Mutations in this gene are associated with autosomal SCID (severe combined immunodeficiency disease). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6193) · Entrez [3718](https://www.ncbi.nlm.nih.gov/gene/3718) · UniProt [P52333](https://www.uniprot.org/uniprotkb/P52333) · Ensembl [ENSG00000105639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105639)

## Data

Gene col 2631: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2631); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2631, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2631]; `tensor/DDL_lfc|DDL_z.npy` [2631]; `embed/gene_vectors.npy` [2631]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2631 or target_col == 2631). Every well: [[JAK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JAK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
