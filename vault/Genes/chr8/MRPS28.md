---
symbol: "MRPS28"
type: "gene"
col: 7201
ensembl_id: "ENSG00000147586"
name: "mitochondrial ribosomal protein S28"
location: "8q21.13"
module: 33
arm: "+"
pooled_cpm: 84.01
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# MRPS28

*mitochondrial ribosomal protein S28* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.42× (z +9.1, q 6e-17, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.475× (z -20.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC123]] (+0.64, fdr 1e-05), [[TUBA8]] (+0.64, fdr 7e-06), [[POLR3B]] (+0.61, fdr 9e-06); moves opposite to [[TAPT1]] (-0.60, fdr 1e-05), [[NFYB]] (-0.56, fdr 2e-05), [[UBXN2A]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7201.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.42×** | +9.1 | 6e-17 | 39/49 (SW480, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.47×** | +7.2 | 2e-10 | 42/47 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +6.0 | 3e-07 | 35/48 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.4 | 0.001 | 0/50 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.1 | 0.004 | 18/48 (C32, A-172, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.006 | 24/48 (AsPC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.016 | 16/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.016 | 19/48 (HOP62, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.21×** | +3.5 | 0.030 | 19/48 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.19× | +3.5 | 0.030 | 21/48 (HOP62, SW480, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.033 | 15/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | 1.12× | +3.1 | 0.086 | 16/48 (Hs 766T, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.12× | +3.1 | 0.086 | 5/48 (NCI-H23, SHP-77, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.1 | 0.086 | 16/48 (HEC-1-A, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7201.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.475×** | -20.7 | 0e+00 | 48/48 (NCI-H1573, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.555×** | -16.4 | 0e+00 | 46/49 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -12.0 | 1e-30 | 44/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.590×** | -10.4 | 4e-23 | 40/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -9.8 | 2e-20 | 42/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.616×** | -9.2 | 4e-18 | 43/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -8.5 | 2e-15 | 29/48 (HS-578T, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.658×** | -8.3 | 1e-14 | 34/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -7.0 | 1e-10 | 35/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.692×** | -7.0 | 2e-10 | 26/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.705×** | -6.9 | 3e-10 | 34/48 (SW1417, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.741×** | -5.3 | 4e-06 | 31/49 (LoVo, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.760×** | -5.0 | 2e-05 | 25/45 (BT-474, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.776×** | -4.8 | 7e-05 | 26/47 (HS-578T, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.790×** | -4.2 | 9e-04 | 29/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -4.2 | 0.001 | 25/50 (HS-578T, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.744×** | -3.0 | 0.074 | 17/49 (J82, NCI-H2030, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7201. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 137 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -11.7) |
| [[HS-578T (line)]] | alt | 87.3 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -16.4) |
| [[PANC-1 (line)]] | alt | 76.2 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.05× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -16.3) |
| [[NCI-H1573 (line)]] | alt | 178 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -20.8) |
| [[C32 (line)]] | wt | 154 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.51× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -16.4) |
| [[SW480 (line)]] | alt | 86.2 | 2 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.82× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -12.0) |
| [[LoVo (line)]] | wt | 123 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.481× (z -11.9) |
| [[RKO (line)]] | wt | 96.3 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.343× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -10.1) |
| [[AN3 CA (line)]] | alt | 67.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 39.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -14.4) |
| [[Hs 766T (line)]] | wt | 48.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -11.3) |
| [[J82 (line)]] | alt | 100 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -14.6) |
| [[KATO III (line)]] | alt | 75.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.356× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 67.1 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 6.75× (z +10.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 169 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -14.8) |
| [[RPMI-7951 (line)]] | alt | 69.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -15.5) |
| [[SNU-1 (line)]] | wt | 117 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -13.1) |
| [[SNU-423 (line)]] | alt | 46.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -11.0) |
| [[SW 900 (line)]] | alt | 76.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -16.6) |
| [[A-172 (line)]] | wt | 35.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -13.7) |
| [[A-427 (line)]] | wt | 108 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -10.4) |
| [[H4 (line)]] | wt | 80.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -18.5) |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -12.8) |
| [[HOP62 (line)]] | alt | 75.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 77.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 76.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 89.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 57.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -11.3) |
| [[SHP-77 (line)]] | alt | 127 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 87.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -11.3) |
| [[SW1417 (line)]] | alt | 35.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -9.4) |
| [[A498 (line)]] | wt | 58.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -13.0) |
| [[A549 (line)]] | wt | 88.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -10.4) |
| [[C-33 A (line)]] | alt | 154 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 47.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -8.8) |
| [[CHP-212 (line)]] | wt | 76.8 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.231× (z -8.5) |
| [[COLO 205 (line)]] | alt | 82.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.3) |
| [[HT-29 (line)]] | alt | 49.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -12.9) |
| [[SW48 (line)]] | wt | 59.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -9.9) |
| [[HCT15 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 87.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7201), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC123]] | +0.64 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[TUBA8]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[POLR3B]] | +0.61 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[IL20RB]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[POLR3H]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[DIS3L2]] | +0.58 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[CCDC138]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CCT2]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[NOL10]] | +0.57 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PHB1]] | +0.56 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[CCT4]] | +0.56 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[SMIM8]] | +0.56 | +0.46 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAPT1]] | -0.60 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[NFYB]] | -0.56 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[UBXN2A]] | -0.55 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[ABCA5]] | -0.55 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[STXBP3]] | -0.53 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[LNX2]] | -0.53 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[VAMP4]] | -0.53 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[LRRC57]] | -0.53 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[CYLD]] | -0.53 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[WDR91]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[RO60]] | -0.51 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[NFKBIB]] | -0.51 | -0.54 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers MRPS28's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises MRPS28's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.524). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (39.8, -22.8); signed map (-11.3, -50.5). **Vector** length 123, 36.0% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.4 | +9.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +9.1 | +6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +7.0 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +6.3 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +3.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.2 | +3.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.6 | -16.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.7 | -20.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -8.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.7 | -12.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.5 | -7.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -2.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.1 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.0 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[Neratinib (drug)]] 5 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:79,918,717-80,030,289 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-S28, HSPC007, MRPS35 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9Y2Q9](https://www.uniprot.org/uniprotkb/Q9Y2Q9) carries no function annotation.

**Summary**, from NCBI Gene [28957](https://www.ncbi.nlm.nih.gov/gene/28957):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14513) · Entrez [28957](https://www.ncbi.nlm.nih.gov/gene/28957) · UniProt [Q9Y2Q9](https://www.uniprot.org/uniprotkb/Q9Y2Q9) · Ensembl [ENSG00000147586](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147586)

## Data

Gene col 7201: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7201); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7201, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7201]; `tensor/DDL_lfc|DDL_z.npy` [7201]; `embed/gene_vectors.npy` [7201]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7201 or target_col == 7201). Every well: [[MRPS28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
