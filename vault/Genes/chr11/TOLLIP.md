---
symbol: "TOLLIP"
type: "gene"
col: 1237
ensembl_id: "ENSG00000078902"
name: "toll interacting protein"
location: "11p15.5"
module: 59
arm: "+"
pooled_cpm: 22.77
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# TOLLIP

*toll interacting protein* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.42× (z +18.0, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.572× (z -8.2, q 1e-13, down in 28 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SNU-423 0.154×, HT-29 0.209×, SW480 0.266×, A-172 0.256×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2030 0.130×, A-172 0.218×, HT-29 0.279×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AsPC-1 0.267×, SNU-423 0.263×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Vilanterol (drug)]] 0.05 µM in 1 line (SNU-1 0.0760×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.271×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.153×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEU1]] (+0.63, fdr 8e-06), [[UAP1L1]] (+0.61, fdr 1e-05), [[SAT2]] (+0.61, fdr 1e-05); moves opposite to [[TMX3]] (-0.62, fdr 1e-05), [[PSMD14]] (-0.57, fdr 9e-06), [[XRCC5]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1237.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.42×** | +18.0 | 0e+00 | 42/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.24×** | +11.8 | 1e-29 | 40/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.15×** | +11.2 | 8e-27 | 42/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +9.2 | 3e-18 | 41/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +8.7 | 4e-16 | 36/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +8.1 | 7e-14 | 35/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +7.8 | 5e-13 | 34/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +7.6 | 2e-12 | 30/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +6.5 | 5e-09 | 28/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.1 | 2e-05 | 21/46 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +5.1 | 2e-05 | 25/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.4 | 5e-04 | 20/44 (SNU-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.74×** | +4.3 | 9e-04 | 21/48 (NCI-H23, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.5 | 0.017 | 17/48 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.026 | 14/46 (NCI-H2030, A-172, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.043 | 8/47 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.16× | +3.0 | 0.080 | 9/48 (SW480, PANC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1237.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SNU-423 0.154×, HT-29 0.209×, SW480 0.266×, A-172 0.256×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2030 0.130×, A-172 0.218×, HT-29 0.279×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AsPC-1 0.267×, SNU-423 0.263×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Vilanterol (drug)]] 0.05 µM in 1 line (SNU-1 0.0760×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.271×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.153×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.572×** | -8.2 | 1e-13 | 28/37 (AsPC-1, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.617×** | -6.8 | 3e-09 | 27/32 (SNU-423, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.911× | -4.7 | 5e-04 | 6/48 (NCI-H23, H4, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.712×** | -4.6 | 6e-04 | 19/36 (NCI-H2030, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.799× | -3.3 | 0.11 | 11/48 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.813× | -3.0 | 0.22 | 10/48 (HCT15, Hs 766T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1237. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 36.8 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +21.0) | — |
| [[SW480 (line)]] | alt | 21.7 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.55× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 30.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 42.0 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.271× (z -9.7) |
| [[HT-29 (line)]] | alt | 33.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 17.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +17.9) | — |
| [[Hs 766T (line)]] | wt | 29.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +10.5) | [[Palmatine (chloride) (drug)]] 0.5 µM 0.232× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 13.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 25.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 28.6 | 0 | 1 | — | [[Almonertinib (mesylate) (drug)]] 0.05 µM 0.0637× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +12.0) | — |
| [[H4 (line)]] | wt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.153× (z -9.4) |
| [[HOP62 (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +10.2) | — |
| [[J82 (line)]] | alt | 30.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +13.9) | — |
| [[KATO III (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 18.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +13.3) | — |
| [[NCI-H1792 (line)]] | alt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +11.9) | — |
| [[NCI-H2347 (line)]] | alt | 36.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.9) | — |
| [[RKO (line)]] | wt | 25.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 16.2 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0760× (z -10.1) |
| [[A-427 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1237), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEU1]] | +0.63 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[UAP1L1]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[SAT2]] | +0.61 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[FLCN]] | +0.61 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[TMEM120A]] | +0.60 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[ZFYVE1]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[BRI3]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[GRINA]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ZSWIM8]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[MCRIP1]] | +0.57 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[LSM14B]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMX3]] | -0.62 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[PSMD14]] | -0.57 | -0.57 / -0.58 | both halves | 9e-06 | pathway: Interleukin-1 family signaling |
| [[XRCC5]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[CSE1L]] | -0.52 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[PSMD1]] | -0.52 | -0.53 / -0.52 | both halves | 1e-05 | pathway: Interleukin-1 family signaling |
| [[PTGES3]] | -0.51 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[HNRNPA2B1]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[NUDT5]] | -0.51 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[BANF1]] | -0.50 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[CEP78]] | -0.50 | -0.58 / -0.37 | both halves | 9e-05 |  |
| [[RRM1]] | -0.50 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[NUP155]] | -0.50 | -0.51 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.509). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-9.3, -48.9); signed map (-10.2, 3.0). **Vector** length 73.5, 14.3% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Amino acids regulate mTORC1* (reactome, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +18.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.1 | +0.3 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +1.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.8 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.6 | +8.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +1.8 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | +0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.9 | +0.1 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.5 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | +0.3 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | toll interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:1,274,371-1,309,654 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IL-1RAcPIP |
| Gene groups (HGNC) | C2 domain containing; CUE domain containing |
| Reactome | 6 pathways, smallest: Interleukin-1 signaling; Interleukin-1 family signaling; Signaling by Interleukins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0E2](https://www.uniprot.org/uniprotkb/Q9H0E2) (Toll-interacting protein):

> Component of the signaling pathway of IL-1 and Toll-like receptors. Inhibits cell activation by microbial products. Recruits IRAK1 to the IL-1 receptor complex. Inhibits IRAK1 phosphorylation and kinase activity. Connects the ubiquitin pathway to autophagy by functioning as a ubiquitin-ATG8 family adapter and thus mediating autophagic clearance of ubiquitin conjugates. The TOLLIP-dependent selective autophagy pathway plays an important role in clearance of cytotoxic polyQ proteins aggregates. …

**Summary**, from NCBI Gene [54472](https://www.ncbi.nlm.nih.gov/gene/54472):

> This gene encodes a ubiquitin-binding protein that interacts with several Toll-like receptor (TLR) signaling cascade components. The encoded protein regulates inflammatory signaling and is involved in interleukin-1 receptor trafficking and in the turnover of IL1R-associated kinase. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:16476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16476) · Entrez [54472](https://www.ncbi.nlm.nih.gov/gene/54472) · UniProt [Q9H0E2](https://www.uniprot.org/uniprotkb/Q9H0E2) · Ensembl [ENSG00000078902](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078902)

## Data

Gene col 1237: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1237); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1237, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1237]; `tensor/DDL_lfc|DDL_z.npy` [1237]; `embed/gene_vectors.npy` [1237]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1237 or target_col == 1237). Every well: [[TOLLIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOLLIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
