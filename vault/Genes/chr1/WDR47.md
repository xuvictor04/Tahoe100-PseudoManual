---
symbol: "WDR47"
type: "gene"
col: 1426
ensembl_id: "ENSG00000085433"
name: "WD repeat domain 47"
location: "1p13.3"
module: 93
arm: "+"
pooled_cpm: 34.17
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# WDR47

*WD repeat domain 47* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.86× (z +15.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.441× (z -8.8, q 8e-16, down in 32 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SK-MEL-2 0.0852×, A-172 0.250×, A-427 0.226×, NCI-H2030 0.246×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW 900 0.0939×, H4 0.121×, KATO III 0.184×, SK-MEL-2 0.194×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (SK-MEL-2 0.0891×, NCI-H23 0.176×, MIA PaCa-2 0.178×, KATO III 0.191×, …; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (COLO 205 0.130×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HCT15 0.247×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM53C]] (+0.68, fdr 7e-06), [[FAM222A]] (+0.66, fdr 7e-06), [[BCORL1]] (+0.65, fdr 7e-06); moves opposite to [[HSPA4]] (-0.58, fdr 3e-05), [[FAM86HP]] (-0.54, fdr 9e-05), [[PRMT3]] (-0.52, fdr 4e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1426.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.86×** | +15.7 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.57×** | +15.5 | 0e+00 | 45/48 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.04×** | +12.9 | 6e-36 | 48/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.83×** | +12.1 | 2e-31 | 48/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +6.9 | 4e-10 | 38/48 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +6.4 | 2e-08 | 43/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +6.4 | 2e-08 | 35/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +6.2 | 4e-08 | 32/48 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.4 | 3e-06 | 30/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.37×** | +5.2 | 1e-05 | 32/48 (SW480, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.57×** | +5.1 | 2e-05 | 31/48 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +4.6 | 2e-04 | 30/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.6 | 2e-04 | 28/48 (J82, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.45×** | +4.1 | 0.002 | 26/45 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.26×** | +3.8 | 0.006 | 23/47 (LOX-IMVI, AsPC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +3.4 | 0.027 | 20/48 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.67×** | +3.1 | 0.062 | 14/48 (SW480, HT-29, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1426.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SK-MEL-2 0.0852×, A-172 0.250×, A-427 0.226×, NCI-H2030 0.246×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW 900 0.0939×, H4 0.121×, KATO III 0.184×, SK-MEL-2 0.194×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (SK-MEL-2 0.0891×, NCI-H23 0.176×, MIA PaCa-2 0.178×, KATO III 0.191×, …; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (COLO 205 0.130×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HCT15 0.247×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.441×** | -8.8 | 8e-16 | 32/40 (SK-MEL-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.527×** | -7.4 | 3e-11 | 33/45 (SK-MEL-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.518×** | -7.4 | 4e-11 | 29/37 (SW 900, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 22.9 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +14.5) | — |
| [[AsPC-1 (line)]] | alt | 18.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +12.9) | — |
| [[KATO III (line)]] | alt | 20.6 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 6.17× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -10.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 31.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.42× (z +13.6) | — |
| [[LOX-IMVI (line)]] | wt | 32.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 43.0 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.28× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -12.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 56.0 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0852× (z -15.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 42.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -9.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 25.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.37× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 18.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 40.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.74× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -9.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 19.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.54× (z +12.6) | — |
| [[SW480 (line)]] | alt | 29.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +16.4) | — |
| [[C32 (line)]] | wt | 41.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 29.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +10.7) | — |
| [[J82 (line)]] | alt | 40.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.87× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 34.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +16.5) | — |
| [[A-427 (line)]] | wt | 21.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.89× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 42.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +11.8) | — |
| [[A549 (line)]] | wt | 29.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.86× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -9.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 13.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +8.8) | [[Thymol (drug)]] 0.5 µM 0.130× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 22.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +13.1) | — |
| [[RKO (line)]] | wt | 38.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.00× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 27.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +9.5) | — |
| [[A-172 (line)]] | wt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -11.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 41.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +14.4) | — |
| [[H4 (line)]] | wt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -10.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 40.1 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.247× (z -8.5) |
| [[HOP62 (line)]] | alt | 24.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +12.8) | — |
| [[HS-578T (line)]] | alt | 54.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 56.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 37.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 44.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +12.2) | — |
| [[SHP-77 (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 34.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0939× (z -14.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 79.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM53C]] | +0.68 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[FAM222A]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[BCORL1]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[CNNM4]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[GTF2B]] | +0.63 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[OAT]] | +0.63 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[CHCHD7]] | +0.62 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[APAF1]] | +0.60 | +0.51 / +0.51 | both halves | 1e-05 | same gene group |
| [[DALRD3]] | +0.60 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[KATNA1]] | +0.60 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[FSCN1]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TENT5C]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA4]] | -0.58 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[FAM86HP]] | -0.54 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[PRMT3]] | -0.52 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[TMEM147-AS1]] | -0.51 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[TMEM33]] | -0.50 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[DNAJC11]] | -0.50 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[SCO1]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[AAGAB]] | -0.48 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[MRRF]] | -0.48 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[DMAC2L]] | -0.48 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[JPX]] | -0.47 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[ATE1]] | -0.47 | -0.45 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.4, -27.0); signed map (2.6, 17.0). **Vector** length 82.6, 21.8% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | +2.7 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +4.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.2 | +1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +2.0 | +1.9 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.0 | +1.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | +5.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 47 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:108,970,214-109,042,113 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0893 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

UniProt [O94967](https://www.uniprot.org/uniprotkb/O94967) carries no function annotation.

**Summary**, from NCBI Gene [22911](https://www.ncbi.nlm.nih.gov/gene/22911):

> Predicted to act upstream of or within several processes, including detection of hot stimulus involved in thermoception; neuronal stem cell population maintenance; and telencephalon development. Located in cytoplasm and microtubule. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29141) · Entrez [22911](https://www.ncbi.nlm.nih.gov/gene/22911) · UniProt [O94967](https://www.uniprot.org/uniprotkb/O94967) · Ensembl [ENSG00000085433](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085433)

## Data

Gene col 1426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1426); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1426]; `tensor/DDL_lfc|DDL_z.npy` [1426]; `embed/gene_vectors.npy` [1426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1426 or target_col == 1426). Every well: [[WDR47 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR47.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
