---
symbol: "FBXO21"
type: "gene"
col: 5654
ensembl_id: "ENSG00000135108"
name: "F-box protein 21"
location: "12q24.22"
module: 24
arm: "+"
pooled_cpm: 83.68
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# FBXO21

*F-box protein 21* — 12q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.37× (z +9.1, q 6e-17, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.691× (z -10.2, q 2e-21, down in 28 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.719× (z -9.4, q 1e-18, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMTOR5]] (+0.66, fdr 1e-05), [[AFMID]] (+0.64, fdr 1e-05), [[SLC25A4]] (+0.62, fdr 5e-05); moves opposite to [[ZSCAN30]] (-0.58, fdr 9e-05), [[NRAS]] (-0.57, fdr 3e-05), [[CTBP1-DT]] (-0.57, fdr 5e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5654.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +9.1 | 6e-17 | 36/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +8.0 | 5e-13 | 31/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +7.2 | 9e-11 | 1/50 (MIA PaCa-2) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.26×** | +6.5 | 9e-09 | 28/48 (LoVo, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +5.4 | 9e-06 | 12/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.34×** | +4.4 | 1e-03 | 23/47 (LoVo, A549, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.002 | 14/47 (HS-578T, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | 1.14× | +3.8 | 0.009 | 15/48 (J82, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[DTP3 (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.021 | 10/48 (AN3 CA, A498, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.12× | +3.3 | 0.059 | 12/48 (BT-474, LoVo, …) | two highest doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.080 | 11/48 (Hs 766T, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5654.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -10.2 | 2e-21 | 28/44 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.719×** | -9.4 | 1e-18 | 34/48 (HT-29, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.710×** | -9.4 | 1e-18 | 31/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.540×** | -9.2 | 5e-18 | 36/49 (PANC-1, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.717×** | -8.8 | 2e-16 | 26/45 (NCI-H1792, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.751×** | -7.9 | 4e-13 | 28/47 (A-427, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.614×** | -7.3 | 3e-11 | 37/48 (HS-578T, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.634×** | -6.8 | 7e-10 | 24/38 (BT-474, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.810×** | -6.0 | 1e-07 | 21/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.866× | -5.8 | 3e-07 | 19/49 (NCI-H2347, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.823×** | -5.6 | 1e-06 | 26/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.729×** | -4.7 | 1e-04 | 22/48 (SW 900, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.858× | -4.4 | 5e-04 | 20/49 (NCI-H460, RKO, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.868× | -3.8 | 0.005 | 9/47 (C32, J82, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.777×** | -3.8 | 0.006 | 17/48 (A498, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.784×** | -3.6 | 0.010 | 15/48 (SW 900, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.800×** | -3.3 | 0.027 | 14/47 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.902× | -3.0 | 0.094 | 2/48 (AsPC-1, hTERT-HPNE) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 110 | 0 | 12 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.376× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.379× (z -13.7) |
| [[A-172 (line)]] | wt | 64.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.398× (z -11.6) |
| [[LoVo (line)]] | wt | 92.2 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.419× (z -12.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 92.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.492× (z -8.9) |
| [[A-427 (line)]] | wt | 86.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.500× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 101 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -14.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 83.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.409× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.447× (z -10.6) |
| [[LS 180 (line)]] | wt | 68.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.24× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.610× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 67.5 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 1.83× (z +9.4) | [[TAK-901 (drug)]] 5 µM 0.328× (z -9.1) |
| [[SW 900 (line)]] | alt | 115 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.431× (z -9.8) |
| [[A549 (line)]] | wt | 115 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.481× (z -9.5) |
| [[BT-474 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +9.2) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[NCI-H1573 (line)]] | alt | 100 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 91.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +8.5) ⚠ cell-cycle shift, explains ~53% of this change | [[Dinaciclib (drug)]] 5 µM 0.485× (z -8.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 65.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -10.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 88.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -12.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 80.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.474× (z -9.8) |
| [[HT-29 (line)]] | alt | 79.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.420× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 92.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.421× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 91.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 98.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 83.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.653× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 80.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -13.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 58.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -14.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 80.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.320× (z -9.4) ⚠ toxic |
| [[SW48 (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -9.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 93.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.73× (z +9.5) | — |
| [[A498 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 98.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 104 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 91.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMTOR5]] | +0.66 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[AFMID]] | +0.64 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[SLC25A4]] | +0.62 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[CCDC107]] | +0.60 | +0.40 / +0.60 | both halves | 4e-05 |  |
| [[C19orf81]] | +0.60 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[NSFP1]] | +0.59 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[WIPF2]] | +0.58 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[LSM2]] | +0.57 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[CCDC127]] | +0.57 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[ARID3A]] | +0.57 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[PPFIA1]] | +0.57 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[CAMLG]] | +0.56 | +0.39 / +0.61 | both halves | 5e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN30]] | -0.58 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[NRAS]] | -0.57 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[CTBP1-DT]] | -0.57 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[MAMDC2-AS1]] | -0.56 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[ARRDC3-AS1]] | -0.56 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[ZMPSTE24]] | -0.55 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[KRT8P12]] | -0.54 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[LINC02966]] | -0.54 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[TASOR]] | -0.54 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[MAPRE1]] | -0.54 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[DARS2]] | -0.54 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[FLG-AS1]] | -0.54 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers FBXO21's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.9, -18.5); signed map (-28.3, 12.9). **Vector** length 118, 30.0% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.7 | +8.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +4.3 | +6.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +9.1 |
|  | [[NG25 (drug)]] 5 µM |  | +3.9 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.9 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.7 | +4.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.7 | +3.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.3 | +2.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.7 | -9.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -7.5 | -9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.3 | -8.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -9.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.9 | -7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.22 — chr12:117,141,991-117,190,470 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBX21, KIAA0875 |
| Gene groups (HGNC) | F-boxes other |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [O94952](https://www.uniprot.org/uniprotkb/O94952) (F-box only protein 21):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex.

**Summary**, from NCBI Gene [23014](https://www.ncbi.nlm.nih.gov/gene/23014):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13592) · Entrez [23014](https://www.ncbi.nlm.nih.gov/gene/23014) · UniProt [O94952](https://www.uniprot.org/uniprotkb/O94952) · Ensembl [ENSG00000135108](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135108)

## Data

Gene col 5654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5654); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5654]; `tensor/DDL_lfc|DDL_z.npy` [5654]; `embed/gene_vectors.npy` [5654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5654 or target_col == 5654). Every well: [[FBXO21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
