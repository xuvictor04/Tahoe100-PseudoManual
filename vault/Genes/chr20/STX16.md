---
symbol: "STX16"
type: "gene"
col: 4505
ensembl_id: "ENSG00000124222"
name: "syntaxin 16"
location: "20q13.32"
module: 25
arm: "+"
pooled_cpm: 87.22
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# STX16

*syntaxin 16* — 20q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.65× (z +9.4, q 5e-18, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.794× (z -4.2, q 0.017, down in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1573 0.496×, AsPC-1 0.408×, PANC-1 0.540×, H4 0.434×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.278×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.239×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (HCT15 0.350×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBQLN1]] (+0.72, fdr 7e-06), [[GPN1]] (+0.70, fdr 1e-05), [[MFN2]] (+0.69, fdr 1e-05); moves opposite to [[LAGE3]] (-0.62, fdr 5e-05), [[RPL36AL]] (-0.62, fdr 1e-04, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[SNHG9]] (-0.61, fdr 2e-05), [[MARCHF9]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4505.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +9.4 | 5e-18 | 41/48 (HEC-1-A, COLO 205, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +9.2 | 1e-17 | 36/44 (A-427, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +7.1 | 2e-10 | 39/48 (A-427, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +6.6 | 4e-09 | 30/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +6.3 | 3e-08 | 36/49 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +5.8 | 5e-07 | 29/48 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.24×** | +5.5 | 4e-06 | 29/49 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +5.1 | 3e-05 | 27/45 (RKO, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.7 | 2e-04 | 0/50 | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.25×** | +4.0 | 0.003 | 26/48 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.008 | 22/47 (RKO, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.7 | 0.009 | 19/48 (A-172, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.040 | 18/48 (CFPAC-1, HT-29, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.40×** | +3.3 | 0.044 | 18/45 (LoVo, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.14× | +3.2 | 0.044 | 13/48 (LoVo, LS 180, …) | top dose only | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.060 | 11/48 (SW480, HS-578T, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.065 | 14/48 (SW480, RKO, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.1 | 0.065 | 13/47 (AsPC-1, A-172, …) | top dose only | position effect removed |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 1.19× | +2.9 | 0.091 | 15/48 (NCI-H2347, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4505.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1573 0.496×, AsPC-1 0.408×, PANC-1 0.540×, H4 0.434×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.278×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.239×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (HCT15 0.350×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.794×** | -4.2 | 0.017 | 25/48 (NCI-H1792, PANC-1, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.820×** | -3.6 | 0.091 | 21/47 (NCI-H2030, CHP-212, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.871× | -3.5 | 0.091 | 20/48 (NCI-H1573, AsPC-1, …) | top dose only | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.836× | -3.4 | 0.11 | 16/48 (SK-MEL-2, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.879× | -3.1 | 0.19 | 10/48 (HT-29, J82, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.885× | -3.1 | 0.20 | 6/48 (NCI-H23, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | 0.852× | -3.0 | 0.21 | 22/48 (BT-474, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4505. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 217 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.278× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 56.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.48× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 62.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 92.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.21× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 79.4 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.239× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 71.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.11× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 58.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 70.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -9.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 70.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 159 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +11.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 72.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +12.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.85× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 98.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 86.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 71.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 96.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 99.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4505), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBQLN1]] | +0.72 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[GPN1]] | +0.70 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[MFN2]] | +0.69 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[USP39]] | +0.69 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[PEX19]] | +0.68 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[BPNT2]] | +0.68 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.67 | +0.43 / +0.74 | both halves | 3e-05 |  |
| [[USP5]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[TWF1]] | +0.67 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[AP3M1]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.66 | +0.43 / +0.70 | both halves | 3e-05 |  |
| [[EIF4H]] | +0.66 | +0.46 / +0.72 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAGE3]] | -0.62 | -0.40 / -0.65 | both halves | 5e-05 |  |
| [[RPL36AL]] ⚠ | -0.62 | -0.36 / -0.66 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG9]] | -0.61 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[MARCHF9]] | -0.61 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[ACAP1]] | -0.61 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.60 | -0.38 / -0.63 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[KRT10]] ⚠ | -0.60 | -0.43 / -0.61 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[INAFM1]] | -0.60 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.59 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[MED19]] | -0.59 | -0.39 / -0.67 | both halves | 6e-05 |  |
| [[COX5A]] ⚠ | -0.58 | -0.45 / -0.58 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CNNM4]] | -0.58 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[FOXA2]] | -0.58 | -0.30 / -0.67 | both halves | 2e-04 |  |
| [[PIM3]] | -0.58 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[WIPF2]] | -0.58 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[CCDC85B]] | -0.57 | -0.32 / -0.66 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers STX16's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.716). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.9, -21.5); signed map (-17.3, -35.8). **Vector** length 123, 34.4% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.5 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.4 | +5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.1 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.6 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +3.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.6 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.5 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.7 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -4.7 | -4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -1.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.8 | -1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.32 — chr20:58,651,272-58,679,526 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hsyn16, SYN16, SYN-16 |
| Gene groups (HGNC) | Syntaxins |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 5 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [O14662](https://www.uniprot.org/uniprotkb/O14662) (Syntaxin-16):

> SNARE involved in vesicular transport from the late endosomes to the trans-Golgi network.

**Summary**, from NCBI Gene [8675](https://www.ncbi.nlm.nih.gov/gene/8675):

> This gene encodes a protein that is a member of the syntaxin or t-SNARE (target-SNAP receptor) family. These proteins are found on cell membranes and serve as the targets for V-SNARES (vesicle-SNAP receptors) permitting specific synaptic vesicle docking and fusion. A microdeletion in the region of chromosome 20 where this gene is located has been associated with pseudohypoparathyroidism type Ib. Multiple transcript variants have been found for this gene. Read-through transcription also exists …

**Accessions** — [HGNC:11431](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11431) · Entrez [8675](https://www.ncbi.nlm.nih.gov/gene/8675) · UniProt [O14662](https://www.uniprot.org/uniprotkb/O14662) · Ensembl [ENSG00000124222](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124222)

## Data

Gene col 4505: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4505); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4505, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4505]; `tensor/DDL_lfc|DDL_z.npy` [4505]; `embed/gene_vectors.npy` [4505]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4505 or target_col == 4505). Every well: [[STX16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
