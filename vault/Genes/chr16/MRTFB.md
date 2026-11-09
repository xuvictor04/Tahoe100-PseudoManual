---
symbol: "MRTFB"
type: "gene"
col: 11797
ensembl_id: "ENSG00000186260"
name: "myocardin related transcription factor B"
location: "16p13.12"
module: 18
arm: "+"
pooled_cpm: 88.93
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MRTFB

*myocardin related transcription factor B* — 16p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.31× (z +5.9, q 2e-06, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.457× (z -17.1, q 0e+00, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.644× (z -9.6, q 1e-19, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPECC1L]] (+0.67, fdr 7e-06), [[VWA8]] (+0.65, fdr 7e-06), [[CDIN1]] (+0.63, fdr 7e-06); moves opposite to [[ZNF490]] (-0.64, fdr 1e-05), [[ZNF547]] (-0.59, fdr 1e-05), [[LINC01772]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11797.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +5.9 | 2e-06 | 34/48 (A-172, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.015 | 25/48 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.9 | 0.021 | 24/48 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +3.7 | 0.022 | 23/49 (AsPC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +3.7 | 0.022 | 26/50 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.022 | 24/47 (SW480, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.022 | 24/48 (AsPC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.036 | 23/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.045 | 21/48 (AsPC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.045 | 20/48 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.10 | 20/49 (Hs 766T, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11797.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.457×** | -17.1 | 0e+00 | 42/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.536×** | -9.6 | 1e-19 | 39/48 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -9.6 | 1e-19 | 38/49 (HEC-1-A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.540×** | -9.5 | 3e-19 | 40/48 (NCI-H23, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.551×** | -8.5 | 2e-15 | 34/45 (NCI-H23, LoVo, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.587×** | -7.9 | 2e-13 | 36/48 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.613×** | -7.6 | 3e-12 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.581×** | -7.4 | 6e-12 | 31/49 (COLO 205, A-427, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.618×** | -7.4 | 6e-12 | 35/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.634×** | -6.8 | 7e-10 | 29/44 (LS 180, KATO III, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -6.5 | 4e-09 | 34/47 (SW48, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.671×** | -6.2 | 3e-08 | 33/48 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.572×** | -4.5 | 3e-04 | 30/49 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.760×** | -4.3 | 9e-04 | 28/48 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.771×** | -4.0 | 0.002 | 26/48 (SNU-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.780×** | -3.8 | 0.004 | 24/48 (AN3 CA, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.812×** | -3.1 | 0.063 | 23/50 (HEC-1-A, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.814×** | -3.0 | 0.079 | 22/48 (SHP-77, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 81.2 | 0 | 11 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -19.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.320× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 139 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -15.1) |
| [[NCI-H1573 (line)]] | alt | 195 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -26.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -11.4) |
| [[PANC-1 (line)]] | alt | 146 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -16.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -10.1) |
| [[RKO (line)]] | wt | 61.1 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.323× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 49.7 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -22.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 142 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.386× (z -10.8) |
| [[SNU-1 (line)]] | wt | 73.7 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.150× (z -14.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.191× (z -12.7) |
| [[SW480 (line)]] | alt | 76.3 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.296× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.349× (z -12.6) |
| [[A-427 (line)]] | wt | 123 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.374× (z -12.4) |
| [[LoVo (line)]] | wt | 110 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -15.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 134 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -20.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 40.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0576× (z -21.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 98.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0774× (z -24.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.283× (z -13.2) |
| [[A-172 (line)]] | wt | 66.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -10.1) |
| [[A549 (line)]] | wt | 131 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 94.2 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.140× (z -16.9) ⚠ toxic |
| [[J82 (line)]] | alt | 71.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -16.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.0) |
| [[KATO III (line)]] | alt | 115 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 58.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -16.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 105 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.367× (z -11.2) ⚠ toxic |
| [[SW48 (line)]] | wt | 112 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 72.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -14.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 137 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.422× (z -8.8) |
| [[COLO 205 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0626× (z -24.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 137 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.376× (z -9.2) |
| [[HOP62 (line)]] | alt | 46.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -15.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Hs 766T (line)]] | wt | 43.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[hTERT-HPNE (line)]] | wt | 47.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -11.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 65.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -21.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 48.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -12.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SK-MEL-2 (line)]] | alt | 54.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -11.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 62.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -12.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.2) |
| [[AN3 CA (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0800× (z -15.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 60.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -11.3) |
| [[BT-474 (line)]] | alt | 146 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -8.7) |
| [[C32 (line)]] | wt | 46.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 61.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -14.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 55.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -14.1) |
| [[NCI-H661 (line)]] | alt | 86.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.132× (z -9.3) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 82.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -9.4) |
| [[SHP-77 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.405× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 64.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -13.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CHP-212 (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPECC1L]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[VWA8]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[CDIN1]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[CLASP2]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[EXT2]] | +0.59 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[CARMIL1]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[XPR1]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[KPNA3]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[VANGL1]] | +0.58 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[MAP3K4]] | +0.57 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[PTPN4]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[DTNB]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF490]] | -0.64 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ZNF547]] | -0.59 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[LINC01772]] | -0.59 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[C14orf28]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[KLC4]] | -0.56 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[IKZF4]] | -0.55 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[C12orf57]] | -0.54 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[METTL21EP-1]] | -0.53 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[ZNF550]] | -0.53 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TMEM106A]] | -0.52 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[TXNL4B]] | -0.51 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[FAM117A]] | -0.51 | -0.33 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers MRTFB's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ZNF618]] | B | ZNF618 activity lowers MRTFB's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 1.30× higher at baseline in the lines without ZNF618 | 0.087 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.366). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.4, -34.3); signed map (-13.5, -50.7). **Vector** length 90.1, 27.6% of its response variance represented; |z| ≥ 3 in 1,114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +2.9 | -6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | -0.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +0.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.0 | -17.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.2 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.9 | -7.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | myocardin related transcription factor B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.12 — chr16:14,071,319-14,266,773 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRTF-B, FLJ31823; previously MKL2 |
| Gene groups (HGNC) | Myocardin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULH7](https://www.uniprot.org/uniprotkb/Q9ULH7) (Myocardin-related transcription factor B):

> Acts as a transcriptional coactivator of serum response factor (SRF). Required for skeletal myogenic differentiation.

**Summary**, from NCBI Gene [57496](https://www.ncbi.nlm.nih.gov/gene/57496):

> Enables transcription coactivator activity. Involved in positive regulation of miRNA transcription; positive regulation of striated muscle tissue development; and positive regulation of transcription by RNA polymerase II. Located in nuclear speck. Implicated in syndromic intellectual disability. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29819](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29819) · Entrez [57496](https://www.ncbi.nlm.nih.gov/gene/57496) · UniProt [Q9ULH7](https://www.uniprot.org/uniprotkb/Q9ULH7) · Ensembl [ENSG00000186260](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186260)

## Data

Gene col 11797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11797); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11797]; `tensor/DDL_lfc|DDL_z.npy` [11797]; `embed/gene_vectors.npy` [11797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11797 or target_col == 11797). Every well: [[MRTFB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRTFB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
