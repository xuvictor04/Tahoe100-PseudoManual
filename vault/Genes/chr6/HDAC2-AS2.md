---
symbol: "HDAC2-AS2"
type: "gene"
col: 13661
ensembl_id: "ENSG00000228624"
name: "HDAC2 and HS3ST5 antisense RNA 2"
location: "6q21-q22.1"
module: 26
arm: "+"
pooled_cpm: 11.62
n_lines_expressing: 45
n_dd_up: 33
n_dd_down: 17
n_dd_up_clean: 29
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# HDAC2-AS2

*HDAC2 and HS3ST5 antisense RNA 2* — 6q21-q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.79× (z +34.4, q 0e+00, up in 38 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.597× (z -5.8, q 4e-06, down in 20 of 42 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Dexamethasone (drug)]] 0.5 µM: 0.666× (z -4.6, q 9e-04, down in 12 of 42 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP3K7CL]] (+0.74, fdr 7e-06), [[FBXO38-DT]] (+0.69, fdr 5e-05), [[EFCAB5]] (+0.69, fdr 6e-05); moves opposite to [[MAST3]] (-0.66, fdr 3e-04), [[BRAT1]] (-0.59, fdr 1e-04), [[HPCAL1]] (-0.58, fdr 2e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[GPR176]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.79×** | +34.4 | 0e+00 | 38/41 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +10.0 | 3e-21 | 23/36 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +9.5 | 5e-19 | 22/37 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +8.2 | 3e-14 | 23/43 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +7.7 | 2e-12 | 13/31 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +7.5 | 6e-12 | 17/38 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.87×** | +7.0 | 3e-10 | 21/42 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +6.7 | 2e-09 | 8/15 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +6.2 | 5e-08 | 7/22 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +5.9 | 2e-07 | 20/38 (SW48, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +5.7 | 7e-07 | 18/42 (A-172, SNU-423, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +5.5 | 1e-06 | 20/42 (SW480, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.55×** | +5.3 | 7e-06 | 16/43 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +5.0 | 2e-05 | 18/40 (SW480, LS 180, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.59×** | +5.0 | 2e-05 | 14/41 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.52×** | +4.9 | 4e-05 | 18/43 (SW480, H4, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.54×** | +4.8 | 5e-05 | 14/41 (SW480, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.36×** | +4.7 | 6e-05 | 14/43 (NCI-H2347, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13661.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.597×** | -5.8 | 4e-06 | 20/42 (LOX-IMVI, H4, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.651×** | -4.8 | 4e-04 | 15/42 (LOX-IMVI, SW 1271, …) | two highest doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.666×** | -4.6 | 9e-04 | 12/42 (SW 900, LOX-IMVI, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.669×** | -4.5 | 9e-04 | 15/42 (H4, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.681×** | -4.3 | 0.002 | 14/42 (H4, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.702×** | -4.0 | 0.007 | 16/42 (LOX-IMVI, H4, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.523×** | -3.8 | 0.012 | 10/40 (H4, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.720×** | -3.7 | 0.016 | 12/42 (LOX-IMVI, A498, …) | all doses, flat |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.732×** | -3.5 | 0.029 | 6/42 (hTERT-HPNE, LS 180, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.650×** | -3.5 | 0.031 | 8/43 (Panc 03.27, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **0.809×** | -3.4 | 0.038 | 15/43 (SW480, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.748×** | -3.3 | 0.050 | 14/42 (NCI-H23, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.750×** | -3.2 | 0.052 | 13/42 (SW48, H4, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.745×** | -3.2 | 0.058 | 12/40 (SNU-423, LS 180, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.759×** | -3.1 | 0.073 | 11/42 (H4, LOX-IMVI, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.766×** | -3.0 | 0.088 | 12/42 (NCI-H2030, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 145 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0603× (z -20.8) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -10.0) |
| [[SW480 (line)]] | alt | 15.5 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.72× (z +14.3) | [[Digitoxin (drug)]] 5 µM 0.175× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 6.52 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.6× (z +18.2) | — |
| [[HT-29 (line)]] | alt | 5.03 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +13.8) | [[Bendamustine (drug)]] 0.05 µM 0.0716× (z -9.0) |
| [[H4 (line)]] | wt | 27.9 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0584× (z -12.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HCT15 (line)]] | alt | 7.07 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 5.35 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +12.3) | — |
| [[LoVo (line)]] | wt | 5.43 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +16.7) | — |
| [[NCI-H23 (line)]] | alt | 3.77 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.50× (z +9.1) | [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0683× (z -8.6) |
| [[SW48 (line)]] | wt | 21.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +9.9) | — |
| [[A498 (line)]] | wt | 6.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.98× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 2.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 3.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 46.0× (z +13.8) | — |
| [[C-33 A (line)]] | alt | 4.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +10.6) | — |
| [[C32 (line)]] | wt | 3.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.6× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 3.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +11.8) | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.02× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 7.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.72× (z +13.4) | — |
| [[hTERT-HPNE (line)]] | wt | 8.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +10.6) | — |
| [[KATO III (line)]] | alt | 7.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +12.5) | — |
| [[LS 180 (line)]] | wt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 4.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 5.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 3.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +14.6) | — |
| [[Panc 03.27 (line)]] | alt | 5.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 3.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +16.9) | — |
| [[RPMI-7951 (line)]] | alt | 9.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.39× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 20.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +11.6) | — |
| [[SW 900 (line)]] | alt | 3.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.1× (z +10.5) | — |
| [[A-172 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K7CL]] | +0.74 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[FBXO38-DT]] | +0.69 | +0.75 / +0.40 | both halves | 5e-05 |  |
| [[EFCAB5]] | +0.69 | +0.70 / +0.39 | both halves | 6e-05 |  |
| [[SYT16]] | +0.68 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.68 | +0.66 / +0.38 | both halves | 6e-05 | same gene group |
| [[TMEM202-AS1]] | +0.67 | +0.67 / +0.36 | both halves | 9e-05 | same gene group |
| [[STARD4-AS1]] | +0.67 | +0.51 / +0.52 | both halves | 1e-05 | same gene group |
| [[PGM5P2-1]] | +0.67 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[CHODL]] | +0.67 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[PBLD]] | +0.66 | +0.65 / +0.31 | both halves | 2e-04 |  |
| [[CCDC90B-AS1]] | +0.66 | +0.65 / +0.37 | both halves | 8e-05 | same gene group |
| [[CIBAR1-DT]] | +0.65 | +0.58 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | -0.66 | -0.63 / -0.29 | both halves | 3e-04 |  |
| [[BRAT1]] | -0.59 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[HPCAL1]] | -0.58 | -0.61 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HDAC2-AS2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDK15]] | B | CDK15 activity raises HDAC2-AS2's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without CDK15 | 0.037 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent |
| [[FBN2]] | B | FBN2 activity raises HDAC2-AS2's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 1.94× lower at baseline in the lines without FBN2 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent |
| [[NTM]] | B | NTM activity raises HDAC2-AS2's level | lines that do not express NTM (33) vs lines expressing it (17) | 2.45× lower at baseline in the lines without NTM | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR176]] | B | HDAC2-AS2 activity raises GPR176's level | lines that do not express HDAC2-AS2 (5) vs lines expressing it (45) | 2.99× lower at baseline in the lines without HDAC2-AS2 | 0.058 | ⚠ within organs, on part of the lines; also absent: OPN3, ACVR1C, METTL21EP-1; maybe low, not absent |
| [[MFSD1]] | B | HDAC2-AS2 activity raises MFSD1's level | lines that do not express HDAC2-AS2 (5) vs lines expressing it (45) | 1.76× lower at baseline in the lines without HDAC2-AS2 | 0.067 | ⚠ within organs, on part of the lines; also absent: OPN3, ACVR1C, METTL21EP-1; maybe low, not absent |
| [[LRRC17]] | B | HDAC2-AS2 activity raises LRRC17's level | lines that do not express HDAC2-AS2 (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without HDAC2-AS2 | 0.073 | ⚠ within organs, on part of the lines; also absent: OPN3, ACVR1C, METTL21EP-1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (16.1, 20.6); signed map (27.0, -4.2). **Vector** length 91.6, 18.9% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.1 | +34.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.8 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.7 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.5 | +5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +5.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.7 | -5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -4.3 | -4.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -3.6 | -4.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.1 | -4.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.5 | -0.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.1 | -3.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | HDAC2 and HS3ST5 antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q21-q22.1 — chr6:113,969,701-114,471,705 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ENST00000421891 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43590) · Entrez [101927768](https://www.ncbi.nlm.nih.gov/gene/101927768) · Ensembl [ENSG00000228624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228624)

## Data

Gene col 13661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13661); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13661]; `tensor/DDL_lfc|DDL_z.npy` [13661]; `embed/gene_vectors.npy` [13661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13661 or target_col == 13661). Every well: [[HDAC2-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDAC2-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
