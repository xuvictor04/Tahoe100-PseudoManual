---
symbol: "LARP4"
type: "gene"
col: 8454
ensembl_id: "ENSG00000161813"
name: "La ribonucleoprotein 4"
location: "12q13.12"
module: 4
arm: "+"
pooled_cpm: 110.71
n_lines_expressing: 50
n_dd_up: 43
n_dd_down: 1
n_dd_up_clean: 25
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# LARP4

*La ribonucleoprotein 4* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (18 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.10× (z +26.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.943× (z -4.6, q 0.002, down in 1 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM: 0.838× (z -4.2, q 0.009, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.772×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAA50]] (+0.73, fdr 7e-06), [[HSPA4]] (+0.72, fdr 7e-06), [[TMEM33]] (+0.70, fdr 7e-06); moves opposite to [[GCAT]] (-0.65, fdr 1e-05), [[ING1]] (-0.64, fdr 9e-06), [[MINDY2]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AKR1C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 24 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8454.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.10×** | +26.5 | 0e+00 | 48/48 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.90×** | +23.6 | 0e+00 | 48/48 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +22.9 | 0e+00 | 44/48 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.64×** | +22.8 | 0e+00 | 48/48 (A-172, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.31×** | +19.6 | 0e+00 | 48/48 (SW480, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +18.8 | 0e+00 | 48/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.17×** | +18.2 | 0e+00 | 47/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +18.1 | 0e+00 | 44/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.55×** | +15.5 | 0e+00 | 46/49 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +14.8 | 0e+00 | 45/48 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.82×** | +14.0 | 4e-43 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.77×** | +13.4 | 3e-39 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.97×** | +13.4 | 5e-39 | 43/45 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +12.9 | 1e-36 | 42/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.84×** | +12.8 | 5e-36 | 41/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.04×** | +12.0 | 2e-31 | 46/49 (A-172, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +10.0 | 6e-22 | 40/48 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +7.9 | 4e-14 | 33/48 (CFPAC-1, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8454.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.772×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -4.6 | 0.002 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.838× | -4.2 | 0.009 | 19/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.888× | -4.0 | 0.014 | 8/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Meloxicam (drug)]] 0.5 µM |  | 0.859× | -3.6 | 0.038 | 13/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.854× | -3.6 | 0.038 | 15/48 (AsPC-1, RPMI-7951, …) | top dose only | plate-row cell shift |
| [[Entrectinib (drug)]] 5 µM |  | 0.862× | -3.5 | 0.044 | 16/48 (KATO III, NCI-H2030, …) | rises with dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.868× | -3.3 | 0.068 | 17/48 (NCI-H2347, SW 900, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.824×** | -3.3 | 0.079 | 18/48 (AN3 CA, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bicalutamide (drug)]] 0.05 µM |  | 0.873× | -3.2 | 0.087 | 9/48 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Adenosine (drug)]] 5 µM |  | 0.911× | -3.1 | 0.090 | 9/48 (COLO 205, SHP-77, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.877× | -3.1 | 0.090 | 13/49 (NCI-H661, SNU-423, …) | two highest doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.872× | -3.1 | 0.090 | 10/48 (SK-MEL-2, KATO III, …) | top dose only |  |
| [[Hesperidin (drug)]] 0.05 µM |  | 0.870× | -3.0 | 0.10 | 10/48 (RPMI-7951, NCI-H1573, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.880× | -3.0 | 0.10 | 13/47 (A549, RKO, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 137 | 17 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.25× (z +17.2) | — |
| [[SW480 (line)]] | alt | 190 | 17 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.44× (z +17.3) | — |
| [[LoVo (line)]] | wt | 182 | 15 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +17.6) | — |
| [[NCI-H460 (line)]] | wt | 133 | 13 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.55× (z +16.4) | — |
| [[HOP62 (line)]] | alt | 51.3 | 12 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.95× (z +16.0) | — |
| [[SNU-423 (line)]] | alt | 92.1 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +17.3) | — |
| [[H4 (line)]] | wt | 57.0 | 11 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.69× (z +11.9) | — |
| [[HS-578T (line)]] | alt | 57.7 | 11 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.02× (z +13.0) | — |
| [[KATO III (line)]] | alt | 97.6 | 11 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +14.6) | — |
| [[NCI-H1792 (line)]] | alt | 46.3 | 11 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.25× (z +11.8) | — |
| [[A-172 (line)]] | wt | 78.8 | 10 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.25× (z +17.8) | — |
| [[COLO 205 (line)]] | alt | 67.6 | 10 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 11.0× (z +21.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 5.05× (z +14.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 79.3 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.6) | — |
| [[Panc 03.27 (line)]] | alt | 112 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 47.2 | 9 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +14.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.10× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 102 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +15.5) | — |
| [[NCI-H23 (line)]] | alt | 143 | 9 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.23× (z +13.7) | — |
| [[C32 (line)]] | wt | 75.4 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +15.0) | — |
| [[Hs 766T (line)]] | wt | 57.8 | 8 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.12× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 114 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +15.8) | — |
| [[J82 (line)]] | alt | 153 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +14.2) | — |
| [[NCI-H1573 (line)]] | alt | 64.1 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.98× (z +15.5) | — |
| [[SK-MEL-2 (line)]] | alt | 148 | 8 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.78× (z +12.6) | — |
| [[A-427 (line)]] | wt | 162 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +14.6) | — |
| [[hTERT-HPNE (line)]] | wt | 50.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +13.2) | — |
| [[A498 (line)]] | wt | 138 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.98× (z +14.8) | — |
| [[A549 (line)]] | wt | 107 | 6 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.22× (z +12.4) | — |
| [[SW1417 (line)]] | alt | 142 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 94.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 105 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.8) | — |
| [[SW48 (line)]] | wt | 108 | 5 | 0 | [[Auranofin (drug)]] 5 µM 2.73× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 80.7 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.09× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 85.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.17× (z +12.7) | — |
| [[LOX-IMVI (line)]] | wt | 101 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.41× (z +11.2) | — |
| [[RKO (line)]] | wt | 138 | 4 | 0 | [[Auranofin (drug)]] 5 µM 2.46× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 61.6 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.61× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 115 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.49× (z +10.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 105 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 129 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.47× (z +14.5) | — |
| [[NCI-H2030 (line)]] | alt | 109 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.92× (z +11.5) | — |
| [[C-33 A (line)]] | alt | 107 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.58× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 171 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA50]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[HSPA4]] | +0.72 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.70 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[NAA25]] | +0.69 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[LARP1]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 | same gene group; STRING 400 |
| [[PEX26]] | +0.67 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[IDE]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 | STRING 459 |
| [[PSMD11]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CCT5]] | +0.64 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[TMX3]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MGST1]] | +0.64 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[GSR]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCAT]] | -0.65 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[ING1]] | -0.64 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[MINDY2]] | -0.63 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[BTG1]] | -0.62 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[ANKRD37]] | -0.62 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[SEC22A]] | -0.61 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[WIPF2]] | -0.60 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.59 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[CDK2AP2]] | -0.59 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[FSCN1]] | -0.58 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[CNNM4]] | -0.58 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[LGALS1]] | -0.57 | -0.61 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C1]] | B | AKR1C1 activity lowers LARP4's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.39× higher at baseline in the lines without AKR1C1 | 0.009 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[TOP2A]] | B | TOP2A activity lowers LARP4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.1, -30.6); signed map (-10.7, -43.8). **Vector** length 88.3, 32.1% of its response variance represented; |z| ≥ 3 in 1,824 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.50 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.8 | +23.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +19.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +26.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +22.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | +4.6 | +6.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.1 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +7.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +4.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -5.3 | +8.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -4.9 | +11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | +22.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.7 | +11.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | +14.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.4 | -0.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.4 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.0 | -3.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | La ribonucleoprotein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:50,392,383-50,480,004 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PP13296 |
| Gene groups (HGNC) | La ribonucleoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q71RC2](https://www.uniprot.org/uniprotkb/Q71RC2) (La-related protein 4):

> RNA binding protein that binds to the poly-A tract of mRNA molecules. Associates with the 40S ribosomal subunit and with polysomes. Plays a role in the regulation of mRNA translation. Essential for proper regulation of cell morphology and cytoskeletal organization.

**Summary**, from NCBI Gene [113251](https://www.ncbi.nlm.nih.gov/gene/113251):

> Enables mRNA 3'-UTR binding activity and poly(A) binding activity. Involved in positive regulation of translation. Located in cytoplasmic stress granule and cytosolic small ribosomal subunit. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24320) · Entrez [113251](https://www.ncbi.nlm.nih.gov/gene/113251) · UniProt [Q71RC2](https://www.uniprot.org/uniprotkb/Q71RC2) · Ensembl [ENSG00000161813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161813)

## Data

Gene col 8454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8454); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8454]; `tensor/DDL_lfc|DDL_z.npy` [8454]; `embed/gene_vectors.npy` [8454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8454 or target_col == 8454). Every well: [[LARP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LARP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
