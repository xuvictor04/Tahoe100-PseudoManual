---
symbol: "PRKCD"
type: "gene"
col: 8813
ensembl_id: "ENSG00000163932"
name: "protein kinase C delta"
location: "3p21.1"
module: 218
arm: "+"
pooled_cpm: 21.66
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/218"]
generated_by: "tahoemap"
---

# PRKCD

*protein kinase C delta* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.55× (z +7.7, q 6e-12, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.556× (z -10.7, q 6e-24, down in 29 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.762× (z -5.0, q 1e-04, down in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (C32 0.103×, SK-MEL-2 0.186×, SNU-423 0.121×, hTERT-HPNE 0.0934×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HOP62 0.179×, HEC-1-A 0.240×, CFPAC-1 0.263×, SNU-423 0.230×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0340×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (COLO 205 0.110×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.229×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTN2]] (+0.66, fdr 1e-05), [[RBM38]] (+0.65, fdr 1e-05), [[RHOG]] (+0.65, fdr 1e-05); moves opposite to [[FUBP1]] (-0.53, fdr 3e-05), [[SUCLG2]] (-0.52, fdr 4e-05), [[PPWD1]] (-0.51, fdr 4e-05).
> It is in [[Module 218]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8813.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +7.7 | 6e-12 | 27/46 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +7.6 | 6e-12 | 25/46 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +6.0 | 4e-07 | 22/44 (PANC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.6 | 4e-06 | 22/41 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +5.3 | 2e-05 | 19/47 (NCI-H2347, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.29×** | +4.5 | 6e-04 | 13/45 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 0.002 | 12/43 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.003 | 18/46 (SK-MEL-2, HOP62, …) | rises with dose | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.074 | 13/43 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.099 | 15/44 (MIA PaCa-2, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.099 | 4/45 (Panc 03.27, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.10 | 6/44 (HEC-1-A, NCI-H1573, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | 1.18× | +3.0 | 0.10 | 11/42 (AsPC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8813.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (C32 0.103×, SK-MEL-2 0.186×, SNU-423 0.121×, hTERT-HPNE 0.0934×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HOP62 0.179×, HEC-1-A 0.240×, CFPAC-1 0.263×, SNU-423 0.230×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0340×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (COLO 205 0.110×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.229×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.556×** | -10.7 | 6e-24 | 29/40 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.568×** | -9.9 | 1e-20 | 23/31 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.762×** | -5.0 | 1e-04 | 18/47 (LOX-IMVI, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.748×** | -4.9 | 1e-04 | 18/35 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.860× | -3.9 | 0.012 | 18/47 (HOP62, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.834× | -3.2 | 0.14 | 16/46 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.837× | -3.0 | 0.21 | 11/44 (LOX-IMVI, A-172, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8813. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.94 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.58× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.25× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 26.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -12.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 11.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +17.8) | — |
| [[SK-MEL-2 (line)]] | alt | 61.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -14.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 25.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -14.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 38.6 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.60× (z +13.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 28.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -12.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 18.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0340× (z -18.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 14.6 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.84× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 31.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -9.1) |
| [[A549 (line)]] | wt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.65× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -14.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -10.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.110× (z -9.8) |
| [[HS-578T (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -9.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0934× (z -14.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -12.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 9.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.277× (z -9.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8813), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTN2]] | +0.66 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[RBM38]] | +0.65 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[RHOG]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[SPATA2L]] | +0.63 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[SLC66A2]] | +0.61 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[METRNL]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TMEM120A]] | +0.57 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[GPR153]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[NRTN]] | +0.57 | +0.54 / +0.38 | both halves | 7e-05 |  |
| [[KIFC2]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[MLXIP]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[RHBDF2]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUBP1]] | -0.53 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SUCLG2]] | -0.52 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[PPWD1]] | -0.51 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[EWSR1]] | -0.51 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[BCLAF1]] | -0.50 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[TAS2R30]] | -0.50 | -0.34 / -0.47 | both halves | 1e-04 | pathway: G alpha (i) signalling events |
| [[XRCC5]] | -0.49 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[MBTPS2]] | -0.49 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[PTGR2]] | -0.49 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[FUCA2]] | -0.48 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[SNX5]] | -0.48 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[HNRNPR]] | -0.48 | -0.33 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 218]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.761). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.8, 1.0); signed map (-26.8, 16.0). **Vector** length 99.7, 22.1% of its response variance represented; |z| ≥ 3 in 908 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.6 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +7.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.6 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.3 | +2.8 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -3.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -2.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.4 | -0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -1.8 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -2.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase C delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:53,156,009-53,192,717 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PKCδ |
| Gene groups (HGNC) | C2 domain containing protein kinases; Protein kinase C family |
| Hallmark sets | UV_RESPONSE_UP, COMPLEMENT |
| Reactome | 46 pathways, smallest: HuR (ELAVL1) binds and stabilizes mRNA; RHO GTPases Activate NADPH Oxidases; VEGFR2 mediated cell proliferation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05655](https://www.uniprot.org/uniprotkb/Q05655) (Protein kinase C delta type):

> Calcium-independent, phospholipid- and diacylglycerol (DAG)-dependent serine/threonine-protein kinase that plays contrasting roles in cell death and cell survival by functioning as a pro-apoptotic protein during DNA damage-induced apoptosis, but acting as an anti-apoptotic protein during cytokine receptor-initiated cell death, is involved in tumor suppression as well as survival of several cancers, is required for oxygen radical production by NADPH oxidase and acts as positive or negative …

**Summary**, from NCBI Gene [5580](https://www.ncbi.nlm.nih.gov/gene/5580):

> The protein encoded by this gene is a member of the protein kinase C family of serine- and threonine-specific protein kinases. The encoded protein is activated by diacylglycerol and is both a tumor suppressor and a positive regulator of cell cycle progression. Also, this protein can positively or negatively regulate apoptosis. Defects in this gene are a cause of autoimmune lymphoproliferative syndrome. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:9399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9399) · Entrez [5580](https://www.ncbi.nlm.nih.gov/gene/5580) · UniProt [Q05655](https://www.uniprot.org/uniprotkb/Q05655) · Ensembl [ENSG00000163932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163932)

## Data

Gene col 8813: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8813); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8813, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8813]; `tensor/DDL_lfc|DDL_z.npy` [8813]; `embed/gene_vectors.npy` [8813]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8813 or target_col == 8813). Every well: [[PRKCD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKCD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
