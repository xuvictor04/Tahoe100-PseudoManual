---
symbol: "PGM1"
type: "gene"
col: 1263
ensembl_id: "ENSG00000079739"
name: "phosphoglucomutase 1"
location: "1p31.3"
module: 29
arm: "+"
pooled_cpm: 42.51
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PGM1

*phosphoglucomutase 1* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.34× (z +5.7, q 9e-06, up in 20 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.29× (z +4.9, q 3e-04, up in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 2.47×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.250× (z -39.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK4]] (+0.65, fdr 7e-06), [[CDK2AP1]] (+0.61, fdr 1e-05), [[STRADB]] (+0.61, fdr 9e-05); moves opposite to [[CNKSR1]] (-0.57, fdr 3e-05), [[NSUN5]] (-0.56, fdr 2e-05), [[IL18]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1263.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 2.47×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.7 | 9e-06 | 20/36 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +4.9 | 3e-04 | 21/47 (HOP62, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.4 | 0.002 | 20/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.026 | 19/48 (HOP62, HepG2/C3A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.20× | +3.6 | 0.030 | 19/45 (KATO III, NCI-H460, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.078 | 13/47 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.090 | 6/48 (J82, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1263.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.250×** | -39.3 | 0e+00 | 46/48 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.202×** | -32.1 | 0e+00 | 47/48 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.213×** | -31.1 | 0e+00 | 47/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.241×** | -28.6 | 0e+00 | 47/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.305×** | -22.9 | 0e+00 | 45/48 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.403×** | -18.3 | 0e+00 | 40/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.428×** | -17.0 | 0e+00 | 45/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.447×** | -16.1 | 0e+00 | 42/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.623×** | -9.1 | 5e-18 | 32/47 (SNU-1, AN3 CA, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.733×** | -8.8 | 9e-17 | 30/48 (C32, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.440×** | -8.6 | 4e-16 | 36/48 (HOP62, C32, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.674×** | -7.6 | 1e-12 | 27/45 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.713×** | -6.8 | 5e-10 | 32/48 (Hs 766T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.771×** | -5.2 | 8e-06 | 28/48 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.799×** | -4.2 | 8e-04 | 20/48 (HEC-1-A, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.811×** | -4.2 | 1e-03 | 17/48 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.700×** | -3.7 | 0.006 | 16/48 (Panc 03.27, AN3 CA, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1263. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 85.3 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -20.8) |
| [[C32 (line)]] | wt | 59.3 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -20.5) |
| [[NCI-H1792 (line)]] | alt | 64.7 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -27.1) |
| [[NCI-H460 (line)]] | wt | 21.5 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -20.4) |
| [[HOP62 (line)]] | alt | 78.3 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -31.6) |
| [[Hs 766T (line)]] | wt | 46.8 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -26.2) |
| [[J82 (line)]] | alt | 46.3 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -20.3) |
| [[SNU-423 (line)]] | alt | 65.7 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -26.8) |
| [[SW480 (line)]] | alt | 34.7 | 0 | 8 | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -24.5) |
| [[A-172 (line)]] | wt | 44.4 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0903× (z -35.2) |
| [[HS-578T (line)]] | alt | 47.9 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -21.4) |
| [[NCI-H2347 (line)]] | alt | 50.2 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -22.1) |
| [[RPMI-7951 (line)]] | alt | 67.0 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -20.8) |
| [[SW 900 (line)]] | alt | 47.1 | 0 | 7 | — | [[Belinostat (drug)]] 5 µM 0.154× (z -16.5) |
| [[A498 (line)]] | wt | 39.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 32.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -25.0) |
| [[CFPAC-1 (line)]] | alt | 85.2 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -25.8) |
| [[H4 (line)]] | wt | 55.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -21.8) |
| [[HepG2_C3A (line)]] | wt | 40.0 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.0684× (z -18.3) |
| [[hTERT-HPNE (line)]] | wt | 33.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 56.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -25.8) |
| [[Panc 03.27 (line)]] | alt | 56.2 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -20.4) |
| [[PANC-1 (line)]] | alt | 40.3 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -25.4) |
| [[A549 (line)]] | wt | 33.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -18.7) |
| [[HCT15 (line)]] | alt | 93.2 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -19.2) |
| [[LoVo (line)]] | wt | 22.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -16.1) |
| [[LS 180 (line)]] | wt | 21.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -16.0) |
| [[MIA PaCa-2 (line)]] | alt | 55.4 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0919× (z -22.0) |
| [[NCI-H23 (line)]] | alt | 36.9 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -14.2) |
| [[RKO (line)]] | wt | 28.4 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 35.9 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -14.7) |
| [[HT-29 (line)]] | alt | 20.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -15.0) |
| [[SHP-77 (line)]] | alt | 39.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -13.5) |
| [[SNU-1 (line)]] | wt | 35.1 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0942× (z -12.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.242× (z -11.1) |
| [[AN3 CA (line)]] | alt | 49.6 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0977× (z -11.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.124× (z -9.9) |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -9.2) |
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 16.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -17.7) |
| [[NCI-H2030 (line)]] | alt | 52.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -22.2) |
| [[KATO III (line)]] | alt | 11.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -8.9) |
| [[SW 1088 (line)]] | alt | 58.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -8.8) |
| [[SW1417 (line)]] | alt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.0) |
| [[SW48 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0721× (z -11.9) ⚠ toxic; unreliable plate only |
| [[A-427 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1263), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK4]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[CDK2AP1]] | +0.61 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[STRADB]] | +0.61 | +0.36 / +0.54 | both halves | 9e-05 |  |
| [[BPNT2]] | +0.57 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[PRDM10]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PNISR-AS1]] | +0.56 | +0.17 / +0.55 | ⚠ one half (not replicated) | 0.001 |  |
| [[BCL2L2]] | +0.56 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[EPHX1]] | +0.55 | +0.27 / +0.30 | both halves | 3e-04 |  |
| [[NCSTN]] | +0.54 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[CMPK1]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS; STRING 706 |
| [[PGRMC1]] | +0.54 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[HCFC1]] | +0.53 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[EDEM1]] | +0.52 | +0.39 / +0.54 | both halves | 5e-05 | pathway: HALLMARK_MTORC1_SIGNALING |

## Genes that move opposite

*34 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNKSR1]] | -0.57 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[NSUN5]] | -0.56 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[IL18]] | -0.55 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[DDX19B]] | -0.53 | -0.23 / -0.52 | both halves | 5e-04 |  |
| [[MAPKBP1]] | -0.53 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[FAM133B]] | -0.52 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[RIOK1]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[COMMD2]] | -0.52 | -0.21 / -0.48 | both halves | 6e-04 |  |
| [[TICAM1]] | -0.51 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[ACTG1]] | -0.51 | -0.21 / -0.51 | both halves | 7e-04 |  |
| [[PUS3]] | -0.51 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[VEZT]] | -0.51 | -0.26 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-11.7, 15.6); signed map (-18.2, -35.7). **Vector** length 91.5, 23.0% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.2 | +4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.2 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -8.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -22.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.4 | -5.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.4 | -16.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.5 | -17.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.0 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | phosphoglucomutase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:63,593,411-63,660,245 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | HYPOXIA, ADIPOGENESIS, MTORC1_SIGNALING |
| Reactome | 10 pathways, smallest: Galactose catabolism; Glycogen synthesis; Diseases associated with glycosylation precursor biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P36871](https://www.uniprot.org/uniprotkb/P36871) (Phosphoglucomutase-1):

> Catalyzes the reversible isomerization of alpha-D-glucose 1-phosphate to alpha-D-glucose 6-phosphate. The mechanism proceeds via the intermediate compound alpha-D-glucose 1,6-bisphosphate (Probable). This enzyme participates in both the breakdown and synthesis of glucose.

**Summary**, from NCBI Gene [5236](https://www.ncbi.nlm.nih.gov/gene/5236):

> The protein encoded by this gene is an isozyme of phosphoglucomutase (PGM) and belongs to the phosphohexose mutase family. There are several PGM isozymes, which are encoded by different genes and catalyze the transfer of phosphate between the 1 and 6 positions of glucose. In most cell types, this PGM isozyme is predominant, representing about 90% of total PGM activity. In red cells, PGM2 is a major isozyme. This gene is highly polymorphic. Mutations in this gene cause glycogen storage disease …

**Accessions** — [HGNC:8905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8905) · Entrez [5236](https://www.ncbi.nlm.nih.gov/gene/5236) · UniProt [P36871](https://www.uniprot.org/uniprotkb/P36871) · Ensembl [ENSG00000079739](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079739)

## Data

Gene col 1263: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1263); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1263, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1263]; `tensor/DDL_lfc|DDL_z.npy` [1263]; `embed/gene_vectors.npy` [1263]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1263 or target_col == 1263). Every well: [[PGM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
