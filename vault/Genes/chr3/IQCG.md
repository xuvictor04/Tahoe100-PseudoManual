---
symbol: "IQCG"
type: "gene"
col: 3557
ensembl_id: "ENSG00000114473"
name: "dynein regulatory complex subunit 9"
location: "3q29"
module: 54
arm: "-"
pooled_cpm: 22.11
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# IQCG

*dynein regulatory complex subunit 9* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.12× (z +20.5, q 0e+00, up in 25 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.69× (z +9.8, q 1e-20, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.782× (z -4.6, q 0.003, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.145×, RKO 0.337×; ⚠ cell-cycle shift, explains ~17% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.226×, SNU-1 0.128×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.292×; ⚠ cell-cycle shift, would explain all of this change); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (HCT15 0.0909×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (HCT15 0.104×); [[Radotinib (drug)]] 5 µM in 1 line (RKO 0.400×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFSD1]] (+0.54, fdr 2e-05), [[RNF32]] (+0.51, fdr 3e-05), [[CCDC200]] (+0.49, fdr 1e-04); moves opposite to [[MRPL34]] (-0.50, fdr 9e-05), [[ASB13]] (-0.49, fdr 4e-05), [[SLC35A1]] (-0.48, fdr 3e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3557.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.12×** | +20.5 | 0e+00 | 25/28 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +18.6 | 0e+00 | 37/39 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +12.4 | 3e-33 | 30/36 (SW 900, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +9.8 | 1e-20 | 36/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +7.2 | 8e-11 | 24/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +7.0 | 2e-10 | 24/47 (SW480, SW1417, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +6.6 | 3e-09 | 25/48 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +5.2 | 2e-05 | 21/47 (SNU-423, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +5.2 | 2e-05 | 20/48 (SK-MEL-2, LOX-IMVI, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.9 | 0.006 | 13/48 (SW1417, LOX-IMVI, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.16× | +3.9 | 0.006 | 13/48 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.22×** | +3.6 | 0.013 | 14/48 (COLO 205, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.013 | 15/48 (NCI-H1573, NCI-H2347, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.13× | +3.4 | 0.031 | 15/48 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.1 | 0.064 | 5/48 (PANC-1, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3557.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.145×, RKO 0.337×; ⚠ cell-cycle shift, explains ~17% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.226×, SNU-1 0.128×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.292×; ⚠ cell-cycle shift, would explain all of this change); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (HCT15 0.0909×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (HCT15 0.104×); [[Radotinib (drug)]] 5 µM in 1 line (RKO 0.400×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.782×** | -4.6 | 0.003 | 18/48 (SW480, BT-474, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.857× | -4.0 | 0.016 | 18/48 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.677×** | -3.8 | 0.027 | 16/46 (SNU-1, H4, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.868× | -3.7 | 0.028 | 16/48 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.821×** | -3.7 | 0.028 | 15/47 (NCI-H1573, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.830×** | -3.5 | 0.051 | 16/48 (J82, SNU-423, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | **0.832×** | -3.4 | 0.052 | 15/47 (COLO 205, MIA PaCa-2, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.717×** | -3.2 | 0.084 | 8/45 (RKO, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3557. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 21.3 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.50× (z +8.5) | [[Digitoxin (drug)]] 0.5 µM 0.380× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 22.5 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.92× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 95.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -11.2) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.400× (z -9.4) |
| [[SW 900 (line)]] | alt | 12.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.54× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 13.5 | 0 | 2 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0909× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 15.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.39× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 12.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.46× (z +12.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 22.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -13.3) ⚠ cell-cycle shift, explains ~17% of this change |
| [[A498 (line)]] | wt | 10.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 11.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 6.89 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.64× (z +9.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 37.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.171× (z -8.9) ⚠ transcription drop; unreliable plate only |
| [[LoVo (line)]] | wt | 11.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.05× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.128× (z -9.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3557), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD1]] | +0.54 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[RNF32]] | +0.51 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[CCDC200]] | +0.49 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[LMLN]] | +0.48 | +0.45 / +0.45 | both halves | 3e-05 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[DNAL1]] | +0.48 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[ZSCAN30]] | +0.48 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[SDCBP2-AS1]] | +0.47 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[PEX19]] | +0.47 | +0.30 / +0.47 | both halves | 2e-04 |  |
| [[DBNL]] | +0.46 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[SUMF1]] | +0.46 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[BLOC1S6]] | +0.46 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[EXOC7]] | +0.46 | +0.34 / +0.43 | both halves | 1e-04 |  |
| [[CLASP1-AS1]] | +0.45 | +0.32 / +0.44 | both halves | 2e-04 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL34]] | -0.50 | -0.37 / -0.55 | both halves | 9e-05 |  |
| [[ASB13]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SLC35A1]] | -0.48 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[WDR75]] | -0.48 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[SAC3D1]] | -0.47 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[C15orf61]] ⚠ | -0.47 | -0.37 / -0.48 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PET117]] | -0.46 | -0.32 / -0.51 | both halves | 1e-04 |  |
| [[C6orf136]] | -0.46 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[KLHL8]] | -0.46 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[EPB41L4B]] | -0.45 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[TADA1]] | -0.44 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[SHROOM2]] | -0.44 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[POP7]] | -0.44 | -0.24 / -0.51 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.421). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.9, 19.0); signed map (32.0, -11.4). **Vector** length 78.1, 13.9% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | +18.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +20.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +12.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +5.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.2 | +3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | dynein regulatory complex subunit 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:197,889,077-197,960,142 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434B227, DRC9, CFAP122; previously IQCG |
| Gene groups (HGNC) | Dynein regulatory complex; Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H095](https://www.uniprot.org/uniprotkb/Q9H095) (Dynein regulatory complex protein 9):

> Component of the nexin-dynein regulatory complex (N-DRC), a key regulator of ciliary/flagellar motility which maintains the alignment and integrity of the distal axoneme and regulates microtubule sliding in motile axonemes. Binds calmodulin when cellular Ca(2+) levels are low and thereby contributes to the regulation of calcium and calmodulin-dependent protein kinase IV (CAMK4) activity; contributes to the regulation of CAMK4 signaling cascades. Required for normal axoneme assembly in sperm …

**Summary**, from NCBI Gene [84223](https://www.ncbi.nlm.nih.gov/gene/84223):

> Enables Hsp70 protein binding activity and calmodulin binding activity. Predicted to be involved in sperm axoneme assembly. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25251](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25251) · Entrez [84223](https://www.ncbi.nlm.nih.gov/gene/84223) · UniProt [Q9H095](https://www.uniprot.org/uniprotkb/Q9H095) · Ensembl [ENSG00000114473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114473)

## Data

Gene col 3557: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3557); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3557, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3557]; `tensor/DDL_lfc|DDL_z.npy` [3557]; `embed/gene_vectors.npy` [3557]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3557 or target_col == 3557). Every well: [[IQCG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQCG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
