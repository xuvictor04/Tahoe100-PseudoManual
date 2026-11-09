---
symbol: "COPS6"
type: "gene"
col: 9597
ensembl_id: "ENSG00000168090"
name: "COP9 signalosome subunit 6"
location: "7q22.1"
module: 25
arm: "+"
pooled_cpm: 36.1
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# COPS6

*COP9 signalosome subunit 6* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.81× (z +16.9, q 0e+00, up in 46 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.37× (z +4.0, q 0.004, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.793× (z -3.9, q 0.047, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.114×; ⚠ cell-cycle shift, explains ~94% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX11]] (+0.72, fdr 7e-06), [[SNX17]] (+0.70, fdr 7e-06), [[GPS1]] (+0.70, fdr 9e-06); moves opposite to [[ZBTB7A]] (-0.69, fdr 7e-06), [[INAFM1]] (-0.66, fdr 7e-06), [[LINC00685]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9597.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.81×** | +16.9 | 0e+00 | 46/46 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.68×** | +15.8 | 0e+00 | 39/39 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.69×** | +11.6 | 1e-28 | 40/44 (SW480, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.54×** | +5.4 | 8e-06 | 32/47 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.47×** | +4.8 | 2e-04 | 32/48 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.48×** | +4.7 | 2e-04 | 31/47 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.46×** | +4.5 | 5e-04 | 28/48 (MIA PaCa-2, SNU-423, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.1 | 0.003 | 2/48 (MIA PaCa-2, NCI-H661) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.1 | 0.003 | 26/46 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.004 | 26/48 (C32, PANC-1, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.38×** | +3.8 | 0.008 | 26/48 (NCI-H460, HT-29, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.7 | 0.010 | 24/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.017 | 22/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.33×** | +3.5 | 0.017 | 20/48 (C32, LS 180, …) | inconsistent across doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.23×** | +3.5 | 0.018 | 21/48 (HOP62, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.029 | 22/48 (A549, A498, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.036 | 15/46 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.089 | 11/48 (NCI-H460, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9597.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.114×; ⚠ cell-cycle shift, explains ~94% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.793×** | -3.9 | 0.047 | 24/47 (Panc 03.27, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | 0.776× | -3.1 | 0.48 | 19/48 (SW 1088, Panc 03.27, …) | top dose only | position effect removed |
| [[Bergenin (drug)]] 5 µM |  | 0.845× | -3.0 | 0.48 | 16/48 (MIA PaCa-2, BT-474, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9597. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 55.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 38.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 40.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 29.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 42.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 38.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.24× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A549 (line)]] | wt | 27.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.50× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HCT15 (line)]] | alt | 40.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HEC-1-A (line)]] | alt | 40.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 24.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Hs 766T (line)]] | wt | 44.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HS-578T (line)]] | alt | 34.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HT-29 (line)]] | alt | 35.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 45.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LOX-IMVI (line)]] | wt | 37.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 30.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1573 (line)]] | alt | 23.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.35× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 27.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.07× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 39.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RPMI-7951 (line)]] | alt | 32.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.08× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 38.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[CFPAC-1 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[CHP-212 (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.114× (z -8.9) ⚠ cell-cycle shift, explains ~94% of this change |
| [[hTERT-HPNE (line)]] | wt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 21.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 29.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2347 (line)]] | alt | 43.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.3) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[Panc 03.27 (line)]] | alt | 35.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.35× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 37.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-1 (line)]] | wt | 35.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW 900 (line)]] | alt | 34.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.35× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW48 (line)]] | wt | 32.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.84× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9597), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX11]] | +0.72 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[SNX17]] | +0.70 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[GPS1]] | +0.70 | +0.74 / +0.57 | both halves | 9e-06 | same gene group; pathway: Cargo recognition for clathrin-mediated endocytosis; STRING 999 |
| [[AP2M1]] | +0.70 | +0.67 / +0.64 | both halves | 7e-06 | pathway: Cargo recognition for clathrin-mediated endocytosis |
| [[GOT2]] | +0.70 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[TAF6]] | +0.69 | +0.62 / +0.71 | both halves | 7e-06 | ⚠ same locus (14.7 kb: neighbours can correlate without regulation) |
| [[DLD]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[XRCC6]] | +0.68 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[DCTN1]] | +0.68 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[RPE]] | +0.66 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SF3B4]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[EIF4H]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[RBBP9]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB7A]] | -0.69 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.66 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[LINC00685]] | -0.64 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[UBE2CP5]] | -0.64 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.63 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[EIF1B]] | -0.62 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.61 | -0.69 / -0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CROCCP2-1]] | -0.60 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[CCDC65]] | -0.59 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[TNRC6C]] | -0.58 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[HIC2]] | -0.58 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.57 | -0.41 / -0.51 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SPATC1]] | -0.57 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[POLR2J4]] | -0.57 | -0.65 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.751). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.9, -18.4); signed map (-18.8, -41.3). **Vector** length 67.3, 14.9% of its response variance represented; |z| ≥ 3 in 668 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *oxidative phosphorylation* (hallmark, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.4 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.1 | +15.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +2.9 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +2.8 | +11.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.6 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.8 | -0.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.7 | -0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | COP9 signalosome subunit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,088,969-100,092,187 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MOV34-34KD, CSN6 |
| Gene groups (HGNC) | COP9 signalosome; JAMM/MPN+ metallopeptidase family |
| Reactome | 11 pathways, smallest: DNA Damage Recognition in GG-NER; Formation of TC-NER Pre-Incision Complex; Transcription-Coupled Nucleotide Excision Repair (TC-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L5N1](https://www.uniprot.org/uniprotkb/Q7L5N1) (COP9 signalosome complex subunit 6):

> Component of the COP9 signalosome (CSN), a master regulator of the ubiquitin conjugation pathway. CSN mediates the deneddylation of the cullin subunits of all cullin-RING ligases. By reversing the activating neddylation on the cullin-RING ligase, the COP9 signalosome restores the ligase to its inactive state and resets it for substrate recognition. CSN is also involved in phosphorylation of p53/TP53, c-jun/JUN, IkappaBalpha/NFKBIA, ITPK1 and IRF8/ICSBP, possibly via its association with CK2 and …

**Summary**, from NCBI Gene [10980](https://www.ncbi.nlm.nih.gov/gene/10980):

> The protein encoded by this gene is one of the eight subunits of COP9 signalosome, a highly conserved protein complex that functions as an important regulator in multiple signaling pathways. The structure and function of COP9 signalosome is similar to that of the 19S regulatory particle of 26S proteasome. COP9 signalosome has been shown to interact with SCF-type E3 ubiquitin ligases and act as a positive regulator of E3 ubiquitin ligases. This protein belongs to translation initiation factor 3 …

**Accessions** — [HGNC:21749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21749) · Entrez [10980](https://www.ncbi.nlm.nih.gov/gene/10980) · UniProt [Q7L5N1](https://www.uniprot.org/uniprotkb/Q7L5N1) · Ensembl [ENSG00000168090](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168090)

## Data

Gene col 9597: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9597); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9597, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9597]; `tensor/DDL_lfc|DDL_z.npy` [9597]; `embed/gene_vectors.npy` [9597]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9597 or target_col == 9597). Every well: [[COPS6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPS6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
