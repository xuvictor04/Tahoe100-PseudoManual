---
symbol: "RIPK4"
type: "gene"
col: 11400
ensembl_id: "ENSG00000183421"
name: "receptor interacting serine/threonine kinase 4"
location: "21q22.3"
module: 78
arm: "+"
pooled_cpm: 40.48
n_lines_expressing: 37
n_dd_up: 10
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# RIPK4

*receptor interacting serine/threonine kinase 4* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 13.1× (z +14.6, q 1e-45, up in 35 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.305× (z -12.4, q 1e-32, down in 27 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.625× (z -7.2, q 9e-11, down in 22 of 35 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ECE1]] (+0.61, fdr 1e-05), [[NET1]] (+0.55, fdr 4e-05), [[AFAP1]] (+0.55, fdr 3e-05); moves opposite to [[NUTM2B-AS1]] (-0.54, fdr 3e-05), [[N4BP2L2]] (-0.52, fdr 8e-05), [[WTIP]] (-0.52, fdr 3e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[SLC2A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **13.1×** | +14.6 | 1e-45 | 35/36 (C32, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.53×** | +8.6 | 2e-15 | 26/35 (C32, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.9 | 2e-04 | 18/34 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.52×** | +4.4 | 0.002 | 20/35 (NCI-H1573, HS-578T, …) | top dose only | plate-row cell shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.007 | 18/35 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.008 | 18/35 (HT-29, SW1417, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 0.5 µM |  | **1.62×** | +3.7 | 0.015 | 16/35 (SNU-423, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.40×** | +3.7 | 0.016 | 14/35 (SW1417, HT-29, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.39×** | +3.6 | 0.022 | 15/35 (SW480, COLO 205, …) | top dose only |  |
| [[TAK-733 (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.059 | 17/35 (SNU-423, NCI-H1792, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.72× | +3.1 | 0.10 | 10/25 (HS-578T, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.34× | +3.1 | 0.10 | 9/35 (HOP62, H4, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11400.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.305×** | -12.4 | 1e-32 | 27/29 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.356×** | -11.2 | 8e-27 | 30/32 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -7.2 | 9e-11 | 22/35 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.620×** | -5.2 | 3e-05 | 21/35 (PANC-1, HS-578T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.666×** | -4.2 | 0.002 | 20/34 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Darinaparsin (drug)]] 5 µM |  | **0.774×** | -3.9 | 0.007 | 18/35 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.775×** | -3.9 | 0.007 | 19/35 (A549, HS-578T, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.605×** | -3.9 | 0.007 | 20/35 (Hs 766T, SNU-423, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.707×** | -3.8 | 0.010 | 19/34 (NCI-H1573, A498, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -3.6 | 0.016 | 18/34 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.755×** | -3.6 | 0.019 | 18/35 (SW48, NCI-H1792, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -3.5 | 0.021 | 17/35 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.737×** | -3.3 | 0.038 | 17/35 (COLO 205, H4, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.739×** | -3.3 | 0.040 | 18/34 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.741×** | -3.3 | 0.043 | 15/35 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **0.813×** | -3.2 | 0.050 | 15/35 (A549, PANC-1, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.818×** | -3.1 | 0.067 | 12/35 (H4, SW 900, …) | rises with dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.754×** | -3.1 | 0.067 | 13/35 (HS-578T, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 79.9 | 1 | 9 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 9.44× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -19.0) |
| [[A498 (line)]] | wt | 92.7 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 22.0× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.0871× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.292× (z -8.7) |
| [[Hs 766T (line)]] | wt | 89.2 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 30.2× (z +13.0) | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.3) |
| [[HS-578T (line)]] | alt | 97.7 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 27.8× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 68.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0809× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 87.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -19.3) |
| [[NCI-H2347 (line)]] | alt | 35.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0333× (z -18.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 46.2 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 15.4× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -8.6) |
| [[A549 (line)]] | wt | 50.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.3) |
| [[C32 (line)]] | wt | 116 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 115× (z +15.7) | — |
| [[CFPAC-1 (line)]] | alt | 82.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -10.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 23.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.0992× (z -9.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 49.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -14.1) |
| [[KATO III (line)]] | alt | 24.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 28.9 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 38.4× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 22.4 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.14× (z +9.3) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 22.2× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 68.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.2× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -8.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 25.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 33.5× (z +9.3) | — |
| [[LoVo (line)]] | wt | 33.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.8× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 54.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 21.3× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 32.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -11.2) |
| [[SW 900 (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0587× (z -14.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 22.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +9.4) | — |
| [[A-172 (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.90 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.56 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.42 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.81 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.52 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 31.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECE1]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[NET1]] | +0.55 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[AFAP1]] | +0.55 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[KCTD6]] | +0.52 | +0.54 / +0.32 | both halves | 2e-04 |  |
| [[SMOX]] | +0.52 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[RAB3A]] | +0.52 | +0.45 / +0.30 | both halves | 2e-04 |  |
| [[TRERF1]] | +0.51 | +0.37 / +0.49 | both halves | 7e-05 |  |
| [[CDK5]] | +0.50 | +0.46 / +0.28 | both halves | 3e-04 |  |
| [[THYN1]] | +0.50 | +0.54 / +0.22 | both halves | 6e-04 |  |
| [[PLTP]] | +0.50 | +0.53 / +0.30 | both halves | 2e-04 |  |
| [[GVQW3]] | +0.49 | +0.33 / +0.28 | both halves | 3e-04 |  |
| [[ORC4]] | +0.49 | +0.44 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUTM2B-AS1]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[N4BP2L2]] | -0.52 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[WTIP]] | -0.52 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ZBTB8OS]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[FBXO10]] | -0.49 | -0.58 / -0.37 | both halves | 7e-05 |  |
| [[TIMM44]] | -0.49 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[HACD1]] | -0.48 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[KRBOX5]] | -0.47 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[ZNF721]] | -0.47 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[SPON1-AS1]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[LARP1B]] | -0.45 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[DCAF10]] | -0.45 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RIPK4's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.8% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[SMOX]] | B | SMOX activity raises RIPK4's level | lines that do not express SMOX (6) vs lines expressing it (44) | 3.88× lower at baseline in the lines without SMOX | 0.049 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[SEMA4B]], [[SLC2A1]] | C | SEMA4B, SLC2A1 activity raises RIPK4's level | lines that do not express SEMA4B, SLC2A1 (4) vs lines expressing them (46) | 5.50× lower at baseline in the lines without SEMA4B, SLC2A1 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent genes |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A1]] | B | RIPK4 activity raises SLC2A1's level | lines that do not express RIPK4 (13) vs lines expressing it (37) | 2.47× lower at baseline in the lines without RIPK4 | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |
| [[SEMA4B]] | B | RIPK4 activity raises SEMA4B's level | lines that do not express RIPK4 (13) vs lines expressing it (37) | 2.30× lower at baseline in the lines without RIPK4 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |
| [[AHDC1]] | B | RIPK4 activity raises AHDC1's level | lines that do not express RIPK4 (13) vs lines expressing it (37) | 1.53× lower at baseline in the lines without RIPK4 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |
| [[SHB]] | B | RIPK4 activity raises SHB's level | lines that do not express RIPK4 (13) vs lines expressing it (37) | 2.18× lower at baseline in the lines without RIPK4 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |
| [[HPCAL1]] | B | RIPK4 activity raises HPCAL1's level | lines that do not express RIPK4 (13) vs lines expressing it (37) | 2.14× lower at baseline in the lines without RIPK4 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |
| [[FZD4]] | B | RIPK4 activity lowers FZD4's level | lines that do not express RIPK4 (13) vs lines expressing it (37) | 1.77× higher at baseline in the lines without RIPK4 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |
| [[C15orf39]] | B | RIPK4 activity raises C15orf39's level | lines that do not express RIPK4 (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without RIPK4 | 0.065 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |
| [[SMAD7]] | B | RIPK4 activity raises SMAD7's level | lines that do not express RIPK4 (13) vs lines expressing it (37) | 1.59× lower at baseline in the lines without RIPK4 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |
| cells under [[Torkinib (drug)]] 5 µM | B | RIPK4 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express RIPK4 (13) vs lines expressing it (35) | the lines without RIPK4: 0.79× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.358). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.6, 61.8); signed map (-8.7, 49.8). **Vector** length 99.7, 28.1% of its response variance represented; |z| ≥ 3 in 822 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +14.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +8.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +3.4 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.2 | +3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +3.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.9 | +4.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | -11.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -5.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | receptor interacting serine/threonine kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:41,739,369-41,767,089 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DIK, ANKK2, RIP4, PKK; previously ANKRD3 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; MicroRNA protein coding host genes; Receptor interacting serine/threonine kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [P57078](https://www.uniprot.org/uniprotkb/P57078) (Receptor-interacting serine/threonine-protein kinase 4):

> Serine/threonine protein kinase (By similarity). Required for embryonic skin development and correct skin homeostasis in adults, via phosphorylation of PKP1 and subsequent promotion of keratinocyte differentiation and cell adhesion (By similarity). It is a direct transcriptional target of TP63. Plays a role in NF-kappa-B activation.

**Summary**, from NCBI Gene [54101](https://www.ncbi.nlm.nih.gov/gene/54101):

> The protein encoded by this gene is a serine/threonine protein kinase that interacts with protein kinase C-delta. The encoded protein can also activate NFkappaB and is required for keratinocyte differentiation. This kinase undergoes autophosphorylation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:496](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:496) · Entrez [54101](https://www.ncbi.nlm.nih.gov/gene/54101) · UniProt [P57078](https://www.uniprot.org/uniprotkb/P57078) · Ensembl [ENSG00000183421](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183421)

## Data

Gene col 11400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11400); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11400]; `tensor/DDL_lfc|DDL_z.npy` [11400]; `embed/gene_vectors.npy` [11400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11400 or target_col == 11400). Every well: [[RIPK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIPK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
