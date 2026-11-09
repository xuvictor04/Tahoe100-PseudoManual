---
symbol: "MEGF6"
type: "gene"
col: 8535
ensembl_id: "ENSG00000162591"
name: "multiple EGF like domains 6"
location: "1p36.32"
module: 189
arm: "+"
pooled_cpm: 26.42
n_lines_expressing: 39
n_dd_up: 15
n_dd_down: 25
n_dd_up_clean: 10
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# MEGF6

*multiple EGF like domains 6* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.11× (z +10.4, q 9e-23, up in 23 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.553× (z -8.2, q 9e-14, down in 24 of 36 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.595× (z -7.2, q 1e-10, down in 25 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAFK]] (+0.60, fdr 1e-05), [[ARVCF]] (+0.60, fdr 1e-05), [[PIK3CD]] (+0.58, fdr 2e-05); moves opposite to [[HOXA10]] (-0.46, fdr 1e-04), [[MBNL3]] (-0.45, fdr 1e-04), [[NFIA]] (-0.44, fdr 4e-05).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CELSR1]] → it (grade B ⚠); 7 go from it, the strongest it → [[ARHGEF4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8535.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.11×** | +10.4 | 9e-23 | 23/36 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +7.5 | 2e-11 | 19/36 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **1.26×** | +4.6 | 8e-04 | 12/37 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.007 | 15/34 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.32×** | +3.9 | 0.012 | 8/36 (KATO III, A-172, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.33×** | +3.8 | 0.013 | 13/37 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.021 | 11/34 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[MK-3903 (drug)]] 5 µM |  | **1.60×** | +3.4 | 0.041 | 6/34 (NCI-H460, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.049 | 7/36 (NCI-H460, SW 1271, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.050 | 4/34 (NCI-H460, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.050 | 15/36 (NCI-H460, HCT15, …) | rises with dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.093 | 8/36 (HS-578T, PANC-1, …) | all doses, flat |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.24×** | +3.1 | 0.095 | 10/36 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.24×** | +3.0 | 0.095 | 4/37 (SK-MEL-2, HT-29, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.24×** | +3.0 | 0.095 | 10/32 (LS 180, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8535.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.553×** | -8.2 | 9e-14 | 24/36 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.595×** | -7.2 | 1e-10 | 25/36 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.406×** | -6.6 | 1e-08 | 25/33 (HT-29, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.631×** | -6.4 | 2e-08 | 22/35 (LoVo, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.640×** | -6.2 | 6e-08 | 23/35 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.643×** | -6.1 | 7e-08 | 19/33 (LoVo, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -5.9 | 3e-07 | 22/36 (MIA PaCa-2, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.666×** | -5.7 | 1e-06 | 18/36 (LoVo, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -5.5 | 3e-06 | 19/35 (Hs 766T, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.773×** | -5.1 | 2e-05 | 18/37 (SNU-423, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.719×** | -4.6 | 2e-04 | 13/35 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.741×** | -4.2 | 0.001 | 11/37 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.753×** | -3.7 | 0.008 | 12/36 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **0.631×** | -3.4 | 0.031 | 3/37 (BT-474, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.781×** | -3.3 | 0.035 | 10/36 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.637×** | -3.3 | 0.036 | 9/34 (PANC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.792×** | -3.2 | 0.039 | 13/36 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.789×** | -3.1 | 0.059 | 12/36 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.803×** | -3.1 | 0.062 | 11/35 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8535. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 276 | 0 | 13 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0809× (z -26.6) |
| [[NCI-H460 (line)]] | wt | 39.2 | 9 (1 ⚠) | 3 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 5.48× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -11.8) |
| [[LoVo (line)]] | wt | 28.8 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0977× (z -17.5) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.193× (z -12.9) |
| [[SW480 (line)]] | alt | 23.2 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.92× (z +10.3) | [[Harringtonine (drug)]] 5 µM 0.266× (z -9.6) ⚠ cell-cycle shift, explains ~84% of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.118× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 39.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -12.0) |
| [[A549 (line)]] | wt | 20.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -9.3) |
| [[COLO 205 (line)]] | alt | 10.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 64.5× (z +20.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 44.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -10.3) |
| [[SW48 (line)]] | wt | 33.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -10.8) |
| [[A-172 (line)]] | wt | 27.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.05 µM 0.272× (z -8.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A498 (line)]] | wt | 29.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 49.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 8.91 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0316× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.7× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 47.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.127× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 12.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 77.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.11× (z +15.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.32 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.50 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.02 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.93 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.33 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.17 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 9.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8535), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAFK]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ARVCF]] | +0.60 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PIK3CD]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[MFSD12]] | +0.56 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[TNFRSF25]] | +0.55 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[DLGAP4]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[IGFN1]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ARHGAP23]] | +0.54 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[ZMIZ1]] | +0.53 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[RAP1B]] | +0.53 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[LZTS3]] | +0.52 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[AMDHD2]] | +0.52 | +0.45 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA10]] | -0.46 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[MBNL3]] | -0.45 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[NFIA]] | -0.44 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELSR1]] | B | CELSR1 activity raises MEGF6's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 2.76× lower at baseline in the lines without CELSR1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |
| [[IGFN1]] | B | IGFN1 activity raises MEGF6's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 1.72× lower at baseline in the lines without IGFN1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9 |
| [[LAMC2]] | B | LAMC2 activity raises MEGF6's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without LAMC2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[AHNAK2]] | B | AHNAK2 activity raises MEGF6's level | lines that do not express AHNAK2 (12) vs lines expressing it (38) | 2.27× lower at baseline in the lines without AHNAK2 | 0.080 | ⚠ within organs, on part of the lines; also absent: CAV1, CAV2, ITGA2; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF4]] | B | MEGF6 activity raises ARHGEF4's level | lines that do not express MEGF6 (11) vs lines expressing it (39) | 2.88× lower at baseline in the lines without MEGF6 | 0.007 | ⚠ within organs, on part of the lines; also absent: SQOR; maybe low, not absent |
| [[ARHGAP27]] | B | MEGF6 activity raises ARHGAP27's level | lines that do not express MEGF6 (11) vs lines expressing it (39) | 2.32× lower at baseline in the lines without MEGF6 | 0.032 | ⚠ within organs, on part of the lines; also absent: SQOR; maybe low, not absent |
| [[TNK2]] | B | MEGF6 activity raises TNK2's level | lines that do not express MEGF6 (11) vs lines expressing it (39) | 1.47× lower at baseline in the lines without MEGF6 | 0.035 | ⚠ within organs, on part of the lines; also absent: SQOR; maybe low, not absent |
| [[DENND2C]] | B | MEGF6 activity raises DENND2C's level | lines that do not express MEGF6 (11) vs lines expressing it (39) | 2.12× lower at baseline in the lines without MEGF6 | 0.045 | ⚠ within organs, on part of the lines; also absent: SQOR; maybe low, not absent |
| [[METTL27]] | B | MEGF6 activity raises METTL27's level | lines that do not express MEGF6 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without MEGF6 | 0.054 | ⚠ within organs, on part of the lines; also absent: SQOR; maybe low, not absent |
| [[L1CAM]] | B | MEGF6 activity raises L1CAM's level | lines that do not express MEGF6 (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without MEGF6 | 0.083 | ⚠ within organs, on part of the lines; also absent: SQOR; maybe low, not absent |
| [[CLIP2]] | B | MEGF6 activity raises CLIP2's level | lines that do not express MEGF6 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without MEGF6 | 0.086 | ⚠ within organs, on part of the lines; also absent: SQOR; maybe low, not absent |

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.0, -1.2); signed map (-4.5, 24.6). **Vector** length 98.8, 24.0% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +3.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +7.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.6 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +3.3 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -2.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -5.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.4 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | multiple EGF like domains 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:3,487,951-3,611,508 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously EGFL3 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [O75095](https://www.uniprot.org/uniprotkb/O75095) carries no function annotation.

**Summary**, from NCBI Gene [1953](https://www.ncbi.nlm.nih.gov/gene/1953):

> Predicted to enable scavenger receptor activity. Predicted to be involved in vesicle-mediated transport. Predicted to be located in extracellular region. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3232) · Entrez [1953](https://www.ncbi.nlm.nih.gov/gene/1953) · UniProt [O75095](https://www.uniprot.org/uniprotkb/O75095) · Ensembl [ENSG00000162591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162591)

## Data

Gene col 8535: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8535); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8535, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8535]; `tensor/DDL_lfc|DDL_z.npy` [8535]; `embed/gene_vectors.npy` [8535]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8535 or target_col == 8535). Every well: [[MEGF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEGF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
