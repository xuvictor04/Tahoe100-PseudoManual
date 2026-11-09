---
symbol: "PHKG2"
type: "gene"
col: 8021
ensembl_id: "ENSG00000156873"
name: "phosphorylase kinase catalytic subunit gamma 2"
location: "16p11.2"
module: 38
arm: "+"
pooled_cpm: 14.85
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# PHKG2

*phosphorylase kinase catalytic subunit gamma 2* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.32× (z +25.3, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.829× (z -4.0, q 0.042, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 0.213×, AsPC-1 0.196×, HEC-1-A 0.350×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.142×, SHP-77 0.226×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0770×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.112×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DMPK]] (+0.59, fdr 1e-05), [[SYS1-DBNDD2]] (+0.53, fdr 2e-05), [[PILRA]] (+0.52, fdr 1e-05); moves opposite to [[HDAC2]] (-0.52, fdr 4e-05), [[STRADB]] (-0.51, fdr 9e-05), [[CISD2]] (-0.48, fdr 1e-04).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[KDM1A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8021.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.32×** | +25.3 | 0e+00 | 44/47 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.49×** | +18.6 | 0e+00 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.14×** | +17.1 | 0e+00 | 44/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.63×** | +14.4 | 8e-45 | 43/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +11.4 | 3e-28 | 33/46 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +10.0 | 1e-21 | 29/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +8.9 | 6e-17 | 31/47 (HEC-1-A, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.79×** | +8.6 | 4e-16 | 30/46 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.61×** | +7.1 | 1e-10 | 29/47 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.39×** | +6.9 | 2e-10 | 24/47 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +6.4 | 9e-09 | 26/44 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.53×** | +6.1 | 6e-08 | 22/42 (RPMI-7951, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.49×** | +6.0 | 1e-07 | 23/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +5.2 | 8e-06 | 22/47 (PANC-1, LS 180, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.8 | 6e-05 | 0/48 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +4.2 | 1e-03 | 11/47 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.59×** | +3.6 | 0.007 | 5/45 (HT-29, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.010 | 8/48 (NCI-H1573, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.17× | +3.4 | 0.017 | 3/48 (HOP62, HS-578T, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.019 | 16/47 (LoVo, SW480, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.031 | 3/48 (NCI-H1573, A498, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.050 | 7/48 (SW1417, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8021.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 0.213×, AsPC-1 0.196×, HEC-1-A 0.350×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.142×, SHP-77 0.226×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0770×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.112×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.829×** | -4.0 | 0.042 | 19/48 (SK-MEL-2, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.798× | -3.4 | 0.21 | 12/46 (SW480, SNU-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.806× | -3.1 | 0.38 | 10/27 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8021. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +13.6) | — |
| [[NCI-H460 (line)]] | wt | 8.64 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +15.6) | — |
| [[A-172 (line)]] | wt | 16.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.41× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -9.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 27.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -9.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 11.1 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.67× (z +13.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.24× (z +12.2) | — |
| [[A549 (line)]] | wt | 10.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +13.8) | — |
| [[LoVo (line)]] | wt | 10.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 12.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 29.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +17.5) | — |
| [[RPMI-7951 (line)]] | alt | 12.9 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +8.9) | [[Saquinavir (drug)]] 0.5 µM 0.0770× (z -11.9) |
| [[PANC-1 (line)]] | alt | 11.8 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.21× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 22.5 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.48× (z +9.2) | — |
| [[A498 (line)]] | wt | 25.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -9.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +8.9) | — |
| [[H4 (line)]] | wt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 8.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +14.3) | — |
| [[Hs 766T (line)]] | wt | 11.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.35× (z +8.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HS-578T (line)]] | alt | 9.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 24.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 9.99 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.112× (z -8.8) |
| [[KATO III (line)]] | alt | 11.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.60× (z +9.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[LOX-IMVI (line)]] | wt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.96× (z +14.3) | — |
| [[NCI-H2030 (line)]] | alt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +15.8) | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +11.2) | — |
| [[SW48 (line)]] | wt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +9.6) | — |
| [[A-427 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8021), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMPK]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[SYS1-DBNDD2]] | +0.53 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[PILRA]] | +0.52 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[AMDHD2]] | +0.52 | +0.50 / +0.37 | both halves | 8e-05 |  |
| [[BCL2L12]] | +0.51 | +0.55 / +0.40 | both halves | 4e-05 |  |
| [[MROH6]] | +0.51 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[TTLL3]] | +0.51 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[PITRM1-AS1]] | +0.50 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[TIMM50]] | +0.49 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[CPNE9]] | +0.49 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[TINCR]] | +0.49 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[RALY]] | +0.49 | +0.42 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC2]] | -0.52 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[STRADB]] | -0.51 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[CISD2]] | -0.48 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[NAE1]] | -0.47 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[RPS7]] | -0.47 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[MATR3]] | -0.46 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[RAB11FIP2]] | -0.46 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[BIVM]] | -0.45 | -0.57 / -0.23 | both halves | 5e-04 |  |
| [[ABHD13]] | -0.44 | -0.24 / -0.41 | both halves | 4e-04 |  |
| [[DTD2]] | -0.44 | -0.51 / -0.22 | both halves | 6e-04 |  |
| [[RPS3A]] | -0.43 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[RFXAP]] | -0.42 | -0.55 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDM1A]] | C | PHKG2's natural level weakens KDM1A's drug response | PHKG2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse +0.04; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.430). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.9, -23.6); signed map (12.0, 14.4). **Vector** length 59.8, 9.37% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +25.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.6 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +0.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +1.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.8 | +0.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +1.7 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.3 | +1.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.5 | -3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | phosphorylase kinase catalytic subunit gamma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,748,293-30,761,176 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphorylase kinase subunits; Phosphorylase kinase catalytic subunit gamma family |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 3 pathways, smallest: Glycogen breakdown (glycogenolysis); Glycogen metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P15735](https://www.uniprot.org/uniprotkb/P15735) (Phosphorylase b kinase gamma catalytic chain, liver/testis isoform):

> Catalytic subunit of the phosphorylase b kinase (PHK), which mediates the neural and hormonal regulation of glycogen breakdown (glycogenolysis) by phosphorylating and thereby activating glycogen phosphorylase. May regulate glycogeneolysis in the testis. In vitro, phosphorylates PYGM.

**Summary**, from NCBI Gene [5261](https://www.ncbi.nlm.nih.gov/gene/5261):

> Phosphorylase kinase is a polymer of 16 subunits, four each of alpha, beta, gamma and delta. The alpha subunit includes the skeletal muscle and hepatic isoforms, encoded by two different genes. The beta subunit is the same in both the muscle and hepatic isoforms, and encoded by one gene. The gamma subunit also includes the skeletal muscle and hepatic isoforms, and the hepatic isoform is encoded by this gene. The delta subunit is a calmodulin and can be encoded by three different genes. The …

**Accessions** — [HGNC:8931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8931) · Entrez [5261](https://www.ncbi.nlm.nih.gov/gene/5261) · UniProt [P15735](https://www.uniprot.org/uniprotkb/P15735) · Ensembl [ENSG00000156873](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156873)

## Data

Gene col 8021: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8021); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8021, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8021]; `tensor/DDL_lfc|DDL_z.npy` [8021]; `embed/gene_vectors.npy` [8021]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8021 or target_col == 8021). Every well: [[PHKG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHKG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
