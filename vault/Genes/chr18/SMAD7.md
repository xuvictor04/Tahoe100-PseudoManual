---
symbol: "SMAD7"
type: "gene"
col: 2163
ensembl_id: "ENSG00000101665"
name: "SMAD family member 7"
location: "18q21.1"
module: 14
arm: "+"
pooled_cpm: 16.27
n_lines_expressing: 45
n_dd_up: 14
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SMAD7

*SMAD family member 7* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 13.5× (z +18.0, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.575× (z -7.0, q 1e-09, down in 19 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 0.731× (z -4.1, q 0.005, down in 16 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GATA6]] (+0.67, fdr 7e-06), [[BCOR]] (+0.64, fdr 7e-06), [[MAP3K8]] (+0.63, fdr 7e-06); moves opposite to [[MAP3K7]] (-0.53, fdr 1e-05), [[SLC30A6]] (-0.53, fdr 1e-05), [[TMED5]] (-0.49, fdr 5e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 5 go from it, the strongest it → [[MARCKS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2163.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **13.5×** | +18.0 | 0e+00 | 42/43 (SW1417, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.68×** | +10.7 | 3e-24 | 30/39 (HEC-1-A, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.73×** | +10.3 | 2e-22 | 31/42 (CFPAC-1, KATO III, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.8 | 2e-09 | 25/41 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +6.7 | 2e-09 | 29/43 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +6.3 | 2e-08 | 23/43 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.8 | 6e-07 | 20/37 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +4.8 | 1e-04 | 18/43 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +4.4 | 7e-04 | 15/43 (A549, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +4.3 | 1e-03 | 14/43 (NCI-H2030, CHP-212, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.003 | 19/40 (A549, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.006 | 16/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.008 | 15/43 (RKO, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.4 | 0.024 | 11/43 (LOX-IMVI, HCT15, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.26×** | +3.1 | 0.080 | 11/42 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2163.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.575×** | -7.0 | 1e-09 | 19/25 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.869× | -6.4 | 6e-08 | 17/43 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.637×** | -6.0 | 5e-07 | 25/37 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.731×** | -4.1 | 0.005 | 16/42 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.738×** | -4.0 | 0.007 | 17/42 (NCI-H2347, SW 1271, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.659×** | -3.9 | 0.008 | 13/41 (C32, HS-578T, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.756×** | -3.7 | 0.018 | 12/42 (SHP-77, CFPAC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.757×** | -3.5 | 0.037 | 14/43 (SW48, SW 900, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.773×** | -3.4 | 0.041 | 11/42 (HS-578T, NCI-H2347, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.613×** | -3.4 | 0.041 | 12/39 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.778×** | -3.3 | 0.046 | 11/42 (COLO 205, HS-578T, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.837× | -3.3 | 0.046 | 11/43 (NCI-H2347, NCI-H1792, …) | rises with dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.784×** | -3.2 | 0.060 | 9/42 (KATO III, HS-578T, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.790×** | -3.1 | 0.077 | 8/43 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.794×** | -3.0 | 0.088 | 10/43 (NCI-H2347, HS-578T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 34.6 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +10.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 20.3× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 48.1 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 24.3× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.0705× (z -21.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 70.8 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 25.5× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -11.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 59.4 | 2 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 59.8× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 22.9 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 12.8× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.116× (z -14.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 20.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +12.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 30.2× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[LS 180 (line)]] | wt | 28.7 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.4× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -10.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 13.9 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 31.9× (z +12.6) | — |
| [[C32 (line)]] | wt | 23.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 30.8× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.119× (z -10.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 14.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +14.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 17.1× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 20.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 21.8× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -8.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 36.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 30.1× (z +14.2) | — |
| [[A-172 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 17.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +11.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 7.69 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[BT-474 (line)]] | alt | 8.05 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0997× (z -8.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 35.9 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0947× (z -8.6) |
| [[HT-29 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -9.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +9.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 11.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +10.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 23.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 17.6× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[Panc 03.27 (line)]] | alt | 7.95 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +8.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SHP-77 (line)]] | alt | 10.3 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.126× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 54.7× (z +10.0) | — |
| [[A-427 (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATA6]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[BCOR]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[MAP3K8]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ANKRD33B]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[SOX9]] | +0.56 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[IFFO2]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[CBX8]] | +0.54 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[DBP]] | +0.53 | +0.49 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[NUAK1]] | +0.53 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[NUAK2]] | +0.53 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[BAMBI]] | +0.53 | +0.47 / +0.57 | both halves | 2e-05 | pathway: Downregulation of TGF-beta receptor signaling; STRING 977 |
| [[CADM1]] | +0.53 | +0.57 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K7]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 | pathway: HALLMARK_TGF_BETA_SIGNALING; STRING 595 |
| [[SLC30A6]] | -0.53 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[TMED5]] | -0.49 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[SPTLC1]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[FAM120B]] | -0.48 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ZCCHC4]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ZNF731P]] | -0.47 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[PIGG]] | -0.46 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[FUBP3]] | -0.45 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[GPR89A]] | -0.45 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[GDI2]] | -0.44 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[ZDHHC6]] | -0.44 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers SMAD7's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[NFATC2]] | B | NFATC2 activity raises SMAD7's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without NFATC2 | 0.048 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[KLF4]] | B | KLF4 activity raises SMAD7's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 2.49× lower at baseline in the lines without KLF4 | 0.053 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[RRAD]] | B | RRAD activity raises SMAD7's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.36× lower at baseline in the lines without RRAD | 0.068 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[RIPK4]] | B | RIPK4 activity raises SMAD7's level | lines that do not express RIPK4 (13) vs lines expressing it (37) | 1.59× lower at baseline in the lines without RIPK4 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARCKS]] | B | SMAD7 activity raises MARCKS's level | lines that do not express SMAD7 (5) vs lines expressing it (45) | 6.31× lower at baseline in the lines without SMAD7 | 0.013 | ⚠ within organs, on part of the lines; also absent: SFXN3, KIAA2012, PLSCR2; maybe low, not absent |
| [[LMNA]] | B | SMAD7 activity raises LMNA's level | lines that do not express SMAD7 (5) vs lines expressing it (45) | 2.99× lower at baseline in the lines without SMAD7 | 0.029 | ⚠ within organs, on part of the lines; also absent: SFXN3, KIAA2012, PLSCR2; maybe low, not absent |
| [[BHLHE40]] | B | SMAD7 activity raises BHLHE40's level | lines that do not express SMAD7 (5) vs lines expressing it (45) | 1.97× lower at baseline in the lines without SMAD7 | 0.091 | ⚠ within organs, on part of the lines; also absent: SFXN3, KIAA2012, PLSCR2; maybe low, not absent |
| [[SPTLC1]] | C | SMAD7's natural level weakens SPTLC1's drug response | SMAD7's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.24; direction not clear | 0.016 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[NFKBIA]] | C | SMAD7's natural level strengthens NFKBIA's drug response | SMAD7's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.45; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.9, -2.6); signed map (45.8, 6.1). **Vector** length 87.5, 18.2% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.7 | +18.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +10.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.0 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.7 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.0 | -6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.9 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | +0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | SMAD family member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:48,919,853-48,950,965 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MADH8, MADH7 |
| Gene groups (HGNC) | SMAD family |
| Hallmark sets | TGF_BETA_SIGNALING, UV_RESPONSE_DN, APOPTOSIS |
| Reactome | 14 pathways, smallest: Downregulation of TGF-beta receptor signaling; Signaling by BMP; Downregulation of SMAD2/3:SMAD4 transcriptional activity |
| Matched by | ensembl_id |

**Function**, from UniProt [O15105](https://www.uniprot.org/uniprotkb/O15105) (SMAD family member 7):

> Antagonist of signaling by TGF-beta (transforming growth factor) type 1 receptor superfamily members; has been shown to inhibit TGF-beta (Transforming growth factor) and activin signaling by associating with their receptors thus preventing SMAD2 access. Functions as an adapter to recruit SMURF2 to the TGF-beta receptor complex. Also acts by recruiting the PPP1R15A-PP1 complex to TGFBR1, which promotes its dephosphorylation. Positively regulates PDPK1 kinase activity by stimulating its …

**Summary**, from NCBI Gene [4092](https://www.ncbi.nlm.nih.gov/gene/4092):

> The protein encoded by this gene is a nuclear protein that binds the E3 ubiquitin ligase SMURF2. Upon binding, this complex translocates to the cytoplasm, where it interacts with TGF-beta receptor type-1 (TGFBR1), leading to the degradation of both the encoded protein and TGFBR1. Expression of this gene is induced by TGFBR1. Variations in this gene are a cause of susceptibility to colorectal cancer type 3 (CRCS3). Several transcript variants encoding different isoforms have been found for this …

**Accessions** — [HGNC:6773](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6773) · Entrez [4092](https://www.ncbi.nlm.nih.gov/gene/4092) · UniProt [O15105](https://www.uniprot.org/uniprotkb/O15105) · Ensembl [ENSG00000101665](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101665)

## Data

Gene col 2163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2163); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2163]; `tensor/DDL_lfc|DDL_z.npy` [2163]; `embed/gene_vectors.npy` [2163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2163 or target_col == 2163). Every well: [[SMAD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMAD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
