---
symbol: "ATG2B"
type: "gene"
col: 838
ensembl_id: "ENSG00000066739"
name: "autophagy related 2B"
location: "14q32.2"
module: 130
arm: "+"
pooled_cpm: 40.18
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 14
n_dd_up_clean: 19
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# ATG2B

*autophagy related 2B* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.29× (z +17.3, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.451× (z -11.8, q 2e-29, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.383× (z -7.4, q 3e-11, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBR1]] (+0.67, fdr 9e-06), [[RBM33]] (+0.65, fdr 3e-05), [[CILK1]] (+0.64, fdr 7e-06); moves opposite to [[DEPDC5]] (-0.57, fdr 5e-05), [[TUBA1C]] (-0.52, fdr 1e-05), [[LINC01399]] (-0.51, fdr 2e-04).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CFL2]] → it (grade C ⚠); 1 goes from it, the strongest it → [[MPP3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 838.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +17.3 | 0e+00 | 45/48 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.92×** | +9.3 | 4e-18 | 37/48 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +7.5 | 1e-11 | 38/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +7.2 | 6e-11 | 37/48 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.7 | 2e-09 | 30/48 (MIA PaCa-2, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +6.4 | 2e-08 | 30/48 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +5.9 | 2e-07 | 35/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +4.9 | 7e-05 | 26/49 (Panc 03.27, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +4.4 | 5e-04 | 28/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +4.3 | 9e-04 | 32/48 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.001 | 23/48 (SK-MEL-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.1 | 0.002 | 26/48 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +4.1 | 0.002 | 25/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.003 | 23/48 (CFPAC-1, LOX-IMVI, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.005 | 22/48 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.024 | 16/48 (C32, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 838.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.451×** | -11.8 | 2e-29 | 48/48 (HEC-1-A, KATO III, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.383×** | -7.4 | 3e-11 | 43/48 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.427×** | -6.6 | 8e-09 | 35/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.446×** | -6.2 | 6e-08 | 37/48 (PANC-1, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.448×** | -6.2 | 6e-08 | 41/48 (PANC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.470×** | -5.8 | 5e-07 | 33/48 (H4, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.608×** | -4.8 | 1e-04 | 31/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.620×** | -4.6 | 3e-04 | 30/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.647×** | -4.2 | 0.002 | 26/48 (SW480, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.750×** | -4.0 | 0.003 | 24/48 (SW48, LoVo, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.659×** | -3.2 | 0.065 | 15/46 (SW48, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.793×** | -3.2 | 0.067 | 15/48 (HT-29, SNU-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.807×** | -3.2 | 0.067 | 20/46 (C32, HT-29, …) | two highest doses | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.814×** | -3.0 | 0.095 | 14/47 (hTERT-HPNE, SNU-423, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 59.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +21.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.355× (z -8.5) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 41.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -10.6) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 39.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +21.0) | — |
| [[NCI-H460 (line)]] | wt | 28.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.374× (z -8.8) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 44.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +14.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.155× (z -10.8) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 59.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.388× (z -10.5) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 26.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +14.5) | — |
| [[HEC-1-A (line)]] | alt | 36.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +13.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.242× (z -11.7) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 44.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 25.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 56.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.2) | [[Bortezomib (drug)]] 5 µM 0.145× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 35.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.384× (z -8.9) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 52.7 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.276× (z -9.9) |
| [[A-172 (line)]] | wt | 32.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +14.8) | — |
| [[A498 (line)]] | wt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.0) | — |
| [[A549 (line)]] | wt | 41.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +16.3) | — |
| [[BT-474 (line)]] | alt | 39.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +12.5) | — |
| [[C32 (line)]] | wt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[HCT15 (line)]] | alt | 52.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.366× (z -9.3) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[J82 (line)]] | alt | 35.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +14.9) | — |
| [[KATO III (line)]] | alt | 53.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.229× (z -10.9) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 46.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.308× (z -10.0) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 38.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.112× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 56.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 57.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.309× (z -10.3) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBR1]] | +0.67 | +0.65 / +0.57 | both halves | 9e-06 | STRING 543 |
| [[RBM33]] | +0.65 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[CILK1]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[FBXO8]] | +0.63 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CREBL2]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[NR1D2]] | +0.62 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[CREBRF]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[KLHDC2]] | +0.61 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[WDR48]] | +0.60 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[MAT2B]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ETFRF1]] | +0.56 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[NDUFS1]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DEPDC5]] | -0.57 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[TUBA1C]] | -0.52 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[LINC01399]] | -0.51 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[CACNB4]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[FRMD5]] | -0.50 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[EIF4A3]] | -0.49 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[UBA6]] | -0.49 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[RRP7BP-1]] | -0.49 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[MPP3]] | -0.49 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[MAP2K1]] | -0.49 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[GALNT12]] | -0.49 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[MAD1L1]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFL2]] | C | CFL2 activity raises ATG2B's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.32× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPP3]] | C | ATG2B's natural level weakens MPP3's drug response | ATG2B's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.39; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.8, -47.2); signed map (9.1, -27.3). **Vector** length 88.5, 21.8% of its response variance represented; |z| ≥ 3 in 1,068 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +17.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.8 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +4.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.7 | -11.8 |
|  | [[EX229 (drug)]] 5 µM |  | -6.7 | -6.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.0 | -6.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.9 | -7.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.8 | -6.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.2 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:96,279,195-96,363,341 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10242, BLTP4B; previously C14orf103 |
| Gene groups (HGNC) | Autophagy related; Bridge-like lipid transfer protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BY7](https://www.uniprot.org/uniprotkb/Q96BY7) (Autophagy-related protein 2 homolog B):

> Lipid transfer protein required for both autophagosome formation and regulation of lipid droplet morphology and dispersion. Tethers the edge of the isolation membrane (IM) to the endoplasmic reticulum (ER) and mediates direct lipid transfer from ER to IM for IM expansion. Binds to the ER exit site (ERES), which is the membrane source for autophagosome formation, and extracts phospholipids from the membrane source and transfers them to ATG9 (ATG9A or ATG9B) to the IM for membrane expansion (By …

**Summary**, from NCBI Gene [55102](https://www.ncbi.nlm.nih.gov/gene/55102):

> This gene encodes a protein required for autophagy. The encoded protein is involved in autophagosome formation. A germline duplication of a region that includes this gene is associated with predisposition to myeloid malignancies. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:20187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20187) · Entrez [55102](https://www.ncbi.nlm.nih.gov/gene/55102) · UniProt [Q96BY7](https://www.uniprot.org/uniprotkb/Q96BY7) · Ensembl [ENSG00000066739](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066739)

## Data

Gene col 838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 838); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 838]; `tensor/DDL_lfc|DDL_z.npy` [838]; `embed/gene_vectors.npy` [838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 838 or target_col == 838). Every well: [[ATG2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
