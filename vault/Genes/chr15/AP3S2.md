---
symbol: "AP3S2"
type: "gene"
col: 8103
ensembl_id: "ENSG00000157823"
name: "adaptor related protein complex 3 subunit sigma 2"
location: "15q26.1"
module: 12
arm: "+"
pooled_cpm: 57.22
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# AP3S2

*adaptor related protein complex 3 subunit sigma 2* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 1.62× (z +10.8, q 8e-25, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.583× (z -12.0, q 2e-30, down in 37 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.721× (z -10.3, q 2e-22, down in 31 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1573 0.110×, A549 0.143×, RPMI-7951 0.138×, PANC-1 0.242×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (H4 0.182×, SK-MEL-2 0.398×, LS 180 0.586×, A498 0.599×, …); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H2030 0.300×, PANC-1 0.324×, C32 0.268×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK5RAP1]] (+0.72, fdr 7e-06), [[PUS3]] (+0.68, fdr 9e-06), [[TAB1]] (+0.67, fdr 1e-05); moves opposite to [[PTBP1]] (-0.58, fdr 1e-05), [[DDX3X]] (-0.56, fdr 1e-05), [[EPB41L2]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +10.8 | 8e-25 | 38/48 (HOP62, COLO 205, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +10.8 | 8e-25 | 41/48 (A549, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +9.7 | 4e-20 | 40/48 (COLO 205, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +7.8 | 1e-12 | 38/48 (SHP-77, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +7.6 | 3e-12 | 37/47 (LOX-IMVI, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +6.0 | 2e-07 | 26/48 (COLO 205, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +5.9 | 2e-07 | 31/48 (COLO 205, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.59×** | +5.4 | 5e-06 | 31/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +5.0 | 4e-05 | 24/48 (A-427, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.005 | 17/49 (A-427, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.11× | +3.4 | 0.031 | 6/48 (A549, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.032 | 16/48 (NCI-H1573, SNU-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.034 | 13/48 (LoVo, SW48, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.15× | +3.2 | 0.063 | 13/48 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.064 | 14/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.073 | 18/48 (LS 180, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8103.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1573 0.110×, A549 0.143×, RPMI-7951 0.138×, PANC-1 0.242×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (H4 0.182×, SK-MEL-2 0.398×, LS 180 0.586×, A498 0.599×, …); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H2030 0.300×, PANC-1 0.324×, C32 0.268×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.583×** | -12.0 | 2e-30 | 37/49 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.602×** | -10.5 | 3e-23 | 30/45 (Panc 03.27, RKO, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -10.3 | 2e-22 | 31/49 (H4, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.664×** | -8.8 | 2e-16 | 27/43 (NCI-H1573, A549, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -6.9 | 5e-10 | 1/49 (C-33 A) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.798×** | -5.0 | 5e-05 | 25/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.831×** | -4.1 | 0.003 | 21/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | **0.826×** | -4.1 | 0.003 | 20/47 (A-172, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.887× | -3.8 | 0.010 | 13/48 (NCI-H1792, NCI-H2347, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.856× | -3.5 | 0.029 | 11/48 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.899× | -3.4 | 0.039 | 12/48 (A-172, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 81.5 | 1 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.28× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -22.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 59.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 50.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.28× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 57.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.27× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 69.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -17.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 35.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.92× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -11.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 59.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.597× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -9.5) |
| [[LoVo (line)]] | wt | 80.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -11.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 81.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 63.1 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.43× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.110× (z -22.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 72.1 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.41× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 98.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -16.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 60.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -15.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 68.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 53.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -11.5) |
| [[C-33 A (line)]] | alt | 55.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -10.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 54.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -17.4) |
| [[HCT15 (line)]] | alt | 65.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -17.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 64.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.401× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 52.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -9.2) |
| [[KATO III (line)]] | alt | 62.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.446× (z -8.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 38.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 60.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -15.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 53.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -11.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 59.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.474× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK5RAP1]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[PUS3]] | +0.68 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[TAB1]] | +0.67 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[DHX57]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[CRYZL1]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[EYA3]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ZNF329]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[FLYWCH1]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[RPP21]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ACOT8]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[GTF2H2]] | +0.63 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[LSM10]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTBP1]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 | same gene group |
| [[DDX3X]] | -0.56 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.56 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[CHD4]] | -0.56 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[SLC12A2]] | -0.55 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[KLHL15]] | -0.54 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[CD164]] | -0.54 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[SEPTIN11]] | -0.53 | -0.42 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.481). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-35.2, -8.3); signed map (-16.8, -13.9). **Vector** length 111, 28.1% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.1 | +10.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.9 | +9.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.9 | +10.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.7 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +3.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.7 | -10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | -12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | -8.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | -5.6 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.5 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 3 subunit sigma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:89,830,599-89,894,638 (-) |
| Ensembl biotype | protein_coding |
| Also known as | sigma3b |
| Gene groups (HGNC) | Adaptor related protein complex 3; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P59780](https://www.uniprot.org/uniprotkb/P59780) (AP-3 complex subunit sigma-2):

> Part of the AP-3 complex, an adaptor-related complex which is not clathrin-associated. The complex is associated with the Golgi region as well as more peripheral structures. It facilitates the budding of vesicles from the Golgi membrane and may be directly involved in trafficking to lysosomes. In concert with the BLOC-1 complex, AP-3 is required to target cargos into vesicles assembled at cell bodies for delivery into neurites and nerve terminals.

**Summary**, from NCBI Gene [10239](https://www.ncbi.nlm.nih.gov/gene/10239):

> Predicted to be involved in anterograde synaptic vesicle transport and vesicle-mediated transport. Part of AP-3 adaptor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:571](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:571) · Entrez [10239](https://www.ncbi.nlm.nih.gov/gene/10239) · UniProt [P59780](https://www.uniprot.org/uniprotkb/P59780) · Ensembl [ENSG00000157823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157823)

## Data

Gene col 8103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8103); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8103]; `tensor/DDL_lfc|DDL_z.npy` [8103]; `embed/gene_vectors.npy` [8103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8103 or target_col == 8103). Every well: [[AP3S2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP3S2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
