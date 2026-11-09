---
symbol: "GK5"
type: "gene"
col: 10558
ensembl_id: "ENSG00000175066"
name: "glycerol kinase 5"
location: "3q23"
module: 175
arm: "+"
pooled_cpm: 48.48
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# GK5

*glycerol kinase 5* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.53× (z +9.9, q 2e-20, up in 27 of 41 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 2.28×, SW480 2.25×, PANC-1 1.84×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 2.70×, NCI-H2347 2.43×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.446× (z -27.6, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCB10]] (+0.70, fdr 7e-06), [[ANAPC5]] (+0.69, fdr 7e-06), [[FAR1]] (+0.65, fdr 7e-06); moves opposite to [[ADNP2]] (-0.60, fdr 1e-05), [[EIF4EBP3]] (-0.58, fdr 2e-05), [[KDM5A]] (-0.56, fdr 1e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → cells under [[Betamethasone dipropionate (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10558.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 2.28×, SW480 2.25×, PANC-1 1.84×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 2.70×, NCI-H2347 2.43×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +9.9 | 2e-20 | 27/41 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +9.1 | 2e-17 | 27/47 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.18× | +4.0 | 0.011 | 12/48 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.018 | 18/43 (CFPAC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | 1.11× | +3.7 | 0.028 | 11/48 (NCI-H1573, RKO, …) | rises with dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.13× | +3.0 | 0.24 | 11/48 (A498, NCI-H1792, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10558.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.446×** | -27.6 | 0e+00 | 40/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.465×** | -17.8 | 0e+00 | 40/48 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.544×** | -14.7 | 0e+00 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.559×** | -14.1 | 6e-43 | 34/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.338×** | -13.7 | 8e-41 | 42/49 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.586×** | -12.9 | 3e-36 | 40/47 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.597×** | -12.5 | 6e-34 | 36/48 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.706×** | -11.9 | 9e-31 | 36/48 (HS-578T, SNU-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.689×** | -9.0 | 1e-17 | 32/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.694×** | -8.8 | 6e-17 | 26/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.694×** | -8.5 | 1e-15 | 26/47 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.542×** | -7.7 | 4e-13 | 30/48 (LS 180, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -7.6 | 9e-13 | 21/47 (KATO III, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.741×** | -7.2 | 2e-11 | 25/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.756×** | -6.8 | 5e-10 | 28/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.768×** | -6.4 | 6e-09 | 25/48 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.799×** | -3.9 | 0.003 | 16/46 (A498, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10558. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 64.3 | 1 (1 ⚠) | 10 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.84× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -29.5) |
| [[NCI-H1573 (line)]] | alt | 36.5 | 1 (1 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -18.6) |
| [[NCI-H460 (line)]] | wt | 35.4 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -22.1) |
| [[HS-578T (line)]] | alt | 82.1 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -20.0) |
| [[SNU-1 (line)]] | wt | 47.1 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.285× (z -12.0) |
| [[SW480 (line)]] | alt | 43.2 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.25× (z +9.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.275× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -14.3) |
| [[NCI-H2030 (line)]] | alt | 51.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -19.3) |
| [[A498 (line)]] | wt | 64.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -21.8) |
| [[A549 (line)]] | wt | 42.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -16.9) |
| [[HOP62 (line)]] | alt | 32.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -18.9) |
| [[LoVo (line)]] | wt | 63.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -17.2) |
| [[RKO (line)]] | wt | 41.7 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.141× (z -15.5) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.9) |
| [[J82 (line)]] | alt | 46.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -25.6) |
| [[KATO III (line)]] | alt | 71.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 37.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 44.6 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.133× (z -16.4) |
| [[A-172 (line)]] | wt | 42.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -15.1) |
| [[LOX-IMVI (line)]] | wt | 28.8 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.346× (z -9.4) |
| [[LS 180 (line)]] | wt | 57.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +9.7) ⚠ toxic; transcription drop | [[TAK-901 (drug)]] 5 µM 0.159× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 75.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -20.0) |
| [[SW48 (line)]] | wt | 52.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -12.0) |
| [[A-427 (line)]] | wt | 114 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.410× (z -13.3) |
| [[BT-474 (line)]] | alt | 58.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.340× (z -10.4) |
| [[C-33 A (line)]] | alt | 71.6 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.349× (z -10.5) |
| [[C32 (line)]] | wt | 25.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -11.9) |
| [[HT-29 (line)]] | alt | 50.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -11.5) |
| [[AN3 CA (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.128× (z -8.5) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 30.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -10.5) |
| [[CHP-212 (line)]] | wt | 21.9 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0801× (z -8.8) |
| [[H4 (line)]] | wt | 40.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.8) |
| [[HCT15 (line)]] | alt | 35.1 | 0 | 1 | — | [[Pimitespib (drug)]] 5 µM 0.0837× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 62.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.609× (z -9.3) |
| [[Hs 766T (line)]] | wt | 35.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 35.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 51.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 37.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.261× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -13.0) |
| [[SW1417 (line)]] | alt | 74.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.577× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10558), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB10]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[ANAPC5]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[FAR1]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ALG6]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ZNF341]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ACTR5]] | +0.61 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[RWDD4]] | +0.61 | +0.57 / +0.63 | both halves | 8e-06 |  |
| [[CMTM4]] | +0.61 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[GCSH]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[DFFB]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[NOMO2]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ATPAF1]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADNP2]] | -0.60 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[EIF4EBP3]] | -0.58 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[KDM5A]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[SON]] | -0.56 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[FBXO48]] | -0.56 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[RNF103-CHMP3]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[LINC01239]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[COLQ]] | -0.54 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[ANKHD1-EIF4EBP3]] | -0.54 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[TRIM69]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[NFAT5]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Betamethasone dipropionate (drug)]] 5 µM | C | GK5's natural level raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | GK5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.333 over the table, 0.074 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | GK5's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | GK5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.4, -13.9); signed map (-38.6, -15.0). **Vector** length 105, 26.8% of its response variance represented; |z| ≥ 3 in 1,145 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +9.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.5 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.6 | +2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.5 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.0 | -12.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.5 | -13.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -27.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -17.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.3 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -7.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | glycerol kinase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:142,157,527-142,225,592 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC40579 |
| Gene groups (HGNC) | Glycerol kinase family; FGGY kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZS86](https://www.uniprot.org/uniprotkb/Q6ZS86) (Glycerol kinase 5):

> Skin-specific kinase that plays a key role in glycerol metabolism, catalyzing its phosphorylation to produce sn-glycerol 3-phosphate. Involved in skin-specific regulation of sterol regulatory element-binding protein (SREBP) processing and lipid biosynthesis.

**Summary**, from NCBI Gene [256356](https://www.ncbi.nlm.nih.gov/gene/256356):

> Predicted to enable glycerol kinase activity. Predicted to be involved in glycerol metabolic process; glycerol-3-phosphate biosynthetic process; and triglyceride metabolic process. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28635](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28635) · Entrez [256356](https://www.ncbi.nlm.nih.gov/gene/256356) · UniProt [Q6ZS86](https://www.uniprot.org/uniprotkb/Q6ZS86) · Ensembl [ENSG00000175066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175066)

## Data

Gene col 10558: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10558); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10558, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10558]; `tensor/DDL_lfc|DDL_z.npy` [10558]; `embed/gene_vectors.npy` [10558]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10558 or target_col == 10558). Every well: [[GK5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GK5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
