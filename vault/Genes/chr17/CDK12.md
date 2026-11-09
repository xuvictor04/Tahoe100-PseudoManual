---
symbol: "CDK12"
type: "gene"
col: 9442
ensembl_id: "ENSG00000167258"
name: "cyclin dependent kinase 12"
location: "17q12"
module: 7
arm: "+"
pooled_cpm: 187.39
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CDK12

*cyclin dependent kinase 12* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.50× (z +11.6, q 2e-28, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.749× (z -11.8, q 4e-29, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED1]] (+0.78, fdr 7e-06, ⚠ same locus), [[TAF2]] (+0.74, fdr 7e-06), [[LANCL2]] (+0.71, fdr 7e-06), [[RCC1L]] (+0.70, fdr 1e-05); moves opposite to [[ARL6]] (-0.63, fdr 1e-05), [[STX7]] (-0.63, fdr 3e-05), [[INPP5F]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9442.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +11.6 | 2e-28 | 45/48 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +11.5 | 3e-28 | 1/50 (HOP62) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +11.4 | 5e-28 | 33/49 (AsPC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +9.6 | 9e-20 | 43/48 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +9.3 | 1e-18 | 30/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +9.3 | 2e-18 | 25/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +8.3 | 1e-14 | 24/48 (BT-474, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +8.2 | 1e-14 | 36/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +8.2 | 2e-14 | 38/48 (HOP62, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +7.9 | 1e-13 | 32/48 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +7.8 | 4e-13 | 38/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +7.1 | 8e-11 | 33/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +6.0 | 7e-08 | 29/48 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.7 | 5e-07 | 30/45 (SNU-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +5.4 | 2e-06 | 25/48 (HOP62, HS-578T, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +5.0 | 2e-05 | 22/48 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +4.0 | 0.002 | 18/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tetracycline (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.9 | 0.002 | 9/49 (NCI-H1573, NCI-H460, …) | top dose only | plate-row cell shift; position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.004 | 22/48 (SW480, BT-474, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9442.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.749×** | -11.8 | 4e-29 | 45/48 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.736×** | -8.8 | 4e-16 | 42/49 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.798×** | -6.5 | 2e-08 | 29/48 (LoVo, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.892× | -4.7 | 4e-04 | 6/48 (RKO, BT-474, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.755×** | -4.2 | 0.003 | 19/38 (BT-474, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -4.1 | 0.004 | 17/48 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.864× | -4.0 | 0.004 | 17/47 (LoVo, KATO III, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.8 | 0.009 | 20/48 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.796×** | -3.4 | 0.037 | 20/49 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.889× | -3.4 | 0.039 | 5/48 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.894× | -3.2 | 0.059 | 7/48 (HCT15, CHP-212, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.895× | -3.2 | 0.062 | 9/48 (C32, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9442. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 118 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +13.9) | — |
| [[NCI-H23 (line)]] | alt | 265 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.403× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.664× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 92.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +17.0) | — |
| [[BT-474 (line)]] | alt | 1,383 | 1 | 3 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.60× (z +10.8) | [[Tucidinostat (drug)]] 5 µM 0.620× (z -11.0) |
| [[HOP62 (line)]] | alt | 131 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 117 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 2.41× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 177 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.06× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.517× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 146 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.4) | [[Auranofin (drug)]] 5 µM 0.352× (z -15.1) |
| [[A-427 (line)]] | wt | 197 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -9.5) |
| [[C32 (line)]] | wt | 119 | 1 | 2 | [[Ixazomib citrate (drug)]] 5 µM 1.95× (z +8.5) | [[Ponatinib (drug)]] 5 µM 0.495× (z -8.9) |
| [[COLO 205 (line)]] | alt | 232 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.12× (z +10.4) | — |
| [[LoVo (line)]] | wt | 184 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +11.5) | [[Tucidinostat (drug)]] 5 µM 0.666× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 141 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.09× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 111 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.36× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 169 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 225 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +9.5) | [[Auranofin (drug)]] 5 µM 0.564× (z -9.0) |
| [[SW1417 (line)]] | alt | 178 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +10.5) | — |
| [[SW480 (line)]] | alt | 204 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 2.06× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.633× (z -10.7) |
| [[C-33 A (line)]] | alt | 189 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.11× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 237 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +11.6) | — |
| [[CHP-212 (line)]] | wt | 303 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.401× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.426× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 231 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 1.62× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 98.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +11.0) | — |
| [[KATO III (line)]] | alt | 230 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.520× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 106 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 253 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 212 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.56× (z +10.1) | — |
| [[RKO (line)]] | wt | 209 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.480× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 104 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +12.4) | — |
| [[SW 1088 (line)]] | alt | 136 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0850× (z -10.7) |
| [[A-172 (line)]] | wt | 171 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 159 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 119 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 108 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 187 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 146 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9442), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED1]] | +0.78 | +0.78 / +0.67 | both halves | 7e-06 | STRING 548; ⚠ same locus (10.2 kb: neighbours can correlate without regulation) |
| [[TAF2]] | +0.74 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[LANCL2]] | +0.71 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[RCC1L]] | +0.70 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[SON]] | +0.69 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[CHD8]] | +0.68 | +0.68 / +0.56 | both halves | 1e-05 | STRING 417 |
| [[INO80]] | +0.68 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.68 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[PRR14L]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[DHX37]] | +0.66 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[MRPS7]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ZNF189]] | +0.65 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[RHBDD3]] | +0.65 | +0.67 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6]] | -0.63 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[STX7]] | -0.63 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[INPP5F]] | -0.61 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[SPOPL]] | -0.61 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[FOXO6]] | -0.61 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[TMOD2]] | -0.60 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[RADX]] | -0.60 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[TBC1D2B]] | -0.60 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[SNX30]] | -0.60 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[FCHO1]] | -0.60 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[TMEM185A]] | -0.59 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[HACE1]] | -0.59 | -0.55 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CDK12's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[SLC4A8]] | B | SLC4A8 activity raises CDK12's level | lines that do not express SLC4A8 (11) vs lines expressing it (39) | 1.31× lower at baseline in the lines without SLC4A8 | 0.078 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[PIP4P2]] | C | PIP4P2 activity lowers CDK12's level | lines that do not express PIP4P2 (4) vs lines expressing it (46) | 2.01× higher at baseline in the lines without PIP4P2 | 0.035 | ⚠ few lines (4 vs 46); across organs; also absent: THEM4, MRPS30-DT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-22.0, 11.4); signed map (13.5, -29.8). **Vector** length 144, 45.6% of its response variance represented; |z| ≥ 3 in 1,234 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.1 | +9.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.6 | +11.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.4 | +8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.5 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +8.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.7 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -13.0 | -11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.9 | -8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -8.5 | -6.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.5 | -3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -6.1 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.6 | -4.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:39,461,486-39,567,559 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CRK7, CRKR, KIAA0904; previously CRKRS |
| Gene groups (HGNC) | Cyclin dependent kinases |
| Reactome | 2 pathways, smallest: TP53 Regulates Transcription of DNA Repair Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYV4](https://www.uniprot.org/uniprotkb/Q9NYV4) (Cyclin-dependent kinase 12):

> Cyclin-dependent kinase that phosphorylates the C-terminal domain (CTD) of the large subunit of RNA polymerase II (POLR2A), thereby acting as a key regulator of transcription elongation. Regulates the expression of genes involved in DNA repair and is required for the maintenance of genomic stability. Preferentially phosphorylates 'Ser-5' in CTD repeats that are already phosphorylated at 'Ser-7', but can also phosphorylate 'Ser-2'. Required for RNA splicing, possibly by phosphorylating …

**Summary**, from NCBI Gene [51755](https://www.ncbi.nlm.nih.gov/gene/51755):

> Enables RNA polymerase II CTD heptapeptide repeat kinase activity and cyclin binding activity. Involved in several processes, including cellular response to estrogen stimulus; negative regulation of intracellular signal transduction; and positive regulation of transcription elongation by RNA polymerase II. Located in nuclear speck. Part of cyclin K-CDK12 complex. Biomarker of gastric adenocarcinoma; hepatocellular carcinoma; and stomach cancer. [provided by Alliance of Genome Resources, Jun …

**Accessions** — [HGNC:24224](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24224) · Entrez [51755](https://www.ncbi.nlm.nih.gov/gene/51755) · UniProt [Q9NYV4](https://www.uniprot.org/uniprotkb/Q9NYV4) · Ensembl [ENSG00000167258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167258)

## Data

Gene col 9442: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9442); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9442, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9442]; `tensor/DDL_lfc|DDL_z.npy` [9442]; `embed/gene_vectors.npy` [9442]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9442 or target_col == 9442). Every well: [[CDK12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
