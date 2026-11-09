---
symbol: "GUSBP18"
type: "gene"
col: 13249
ensembl_id: "ENSG00000215158"
name: "GUSB pseudogene 18"
location: "5p13.2"
module: 83
arm: "-"
pooled_cpm: 28.84
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 42
n_dd_up_clean: 2
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# GUSBP18

*GUSB pseudogene 18* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.33× (z +6.7, q 1e-08, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.322× (z -27.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GUSBP1]] (+0.73, fdr 7e-06), [[HMGN3]] (+0.70, fdr 1e-05), [[ANAPC11]] (+0.66, fdr 1e-04); moves opposite to [[ZNF621]] (-0.71, fdr 2e-05), [[GCNT4]] (-0.68, fdr 7e-05), [[EIF5]] (-0.67, fdr 1e-04).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +6.7 | 1e-08 | 27/48 (A498, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.9 | 0.024 | 20/48 (RKO, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.23×** | +3.5 | 0.088 | 13/48 (LS 180, AsPC-1, …) | inconsistent across doses |  |
| [[Adenosine (drug)]] 5 µM |  | 1.14× | +3.2 | 0.18 | 7/48 (RPMI-7951, A549, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.43× | +3.2 | 0.18 | 8/47 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.21× | +3.1 | 0.18 | 17/47 (SW480, SW 900, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.0 | 0.18 | 2/48 (NCI-H2030, NCI-H1792) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +3.0 | 0.18 | 13/48 (PANC-1, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13249.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.322×** | -27.0 | 0e+00 | 47/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.361×** | -24.2 | 0e+00 | 44/47 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.408×** | -15.0 | 0e+00 | 41/47 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.410×** | -15.0 | 0e+00 | 44/48 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.406×** | -14.6 | 0e+00 | 43/48 (SW 900, A498, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.414×** | -14.3 | 4e-44 | 41/47 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.493×** | -11.9 | 1e-30 | 34/44 (SW480, NCI-H2347, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.500×** | -11.2 | 3e-27 | 40/48 (BT-474, HS-578T, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.519×** | -11.0 | 2e-26 | 40/48 (BT-474, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.525×** | -10.8 | 1e-25 | 40/47 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.534×** | -9.7 | 1e-20 | 29/39 (NCI-H2347, J82, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.566×** | -9.6 | 5e-20 | 30/48 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.581×** | -9.1 | 3e-18 | 36/48 (NCI-H1573, C-33 A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.578×** | -8.8 | 4e-17 | 31/47 (SNU-423, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.586×** | -8.6 | 2e-16 | 27/37 (A-427, NCI-H2030, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.610×** | -8.3 | 3e-15 | 35/48 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.598×** | -8.2 | 9e-15 | 34/48 (NCI-H2030, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.708×** | -5.8 | 2e-07 | 25/48 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.722×** | -5.5 | 1e-06 | 27/47 (Panc 03.27, J82, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 28.9 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -20.8) |
| [[NCI-H2030 (line)]] | alt | 33.2 | 0 | 12 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -15.8) |
| [[H4 (line)]] | wt | 46.3 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0923× (z -20.9) |
| [[NCI-H2347 (line)]] | alt | 60.5 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -22.3) |
| [[SW 900 (line)]] | alt | 47.0 | 0 | 10 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -16.5) |
| [[SW480 (line)]] | alt | 45.6 | 0 | 10 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -17.2) |
| [[NCI-H1573 (line)]] | alt | 33.1 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -16.8) |
| [[Panc 03.27 (line)]] | alt | 56.5 | 0 | 9 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -18.1) |
| [[HS-578T (line)]] | alt | 40.8 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -15.8) |
| [[MIA PaCa-2 (line)]] | alt | 30.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -14.3) |
| [[HT-29 (line)]] | alt | 37.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -17.9) |
| [[SHP-77 (line)]] | alt | 65.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -12.9) |
| [[A-427 (line)]] | wt | 56.7 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -11.0) |
| [[C32 (line)]] | wt | 28.4 | 0 | 5 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0530× (z -17.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.208× (z -13.5) |
| [[HepG2_C3A (line)]] | wt | 35.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -15.1) |
| [[A498 (line)]] | wt | 19.7 | 0 | 4 | — | [[Harringtonine (drug)]] 0.5 µM 0.167× (z -14.5) |
| [[BT-474 (line)]] | alt | 32.5 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0696× (z -17.3) |
| [[HEC-1-A (line)]] | alt | 24.9 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -13.1) |
| [[J82 (line)]] | alt | 25.0 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 27.0 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -20.9) |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -17.5) |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -14.2) |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 21.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -17.8) |
| [[NCI-H23 (line)]] | alt | 63.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -17.3) |
| [[SW48 (line)]] | wt | 38.9 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -11.2) |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -12.0) |
| [[LoVo (line)]] | wt | 19.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -20.5) |
| [[LS 180 (line)]] | wt | 21.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 12.0 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -10.2) |
| [[NCI-H661 (line)]] | alt | 36.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0592× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Vilanterol (drug)]] 0.5 µM 0.0804× (z -8.5) |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -9.8) |
| [[A-172 (line)]] | wt | 12.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -8.7) |
| [[A549 (line)]] | wt | 11.3 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.181× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 21.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -11.3) |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.0) |
| [[Hs 766T (line)]] | wt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -8.5) |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -10.3) |
| [[AN3 CA (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUSBP1]] | +0.73 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[HMGN3]] | +0.70 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ANAPC11]] | +0.66 | +0.62 / +0.34 | both halves | 1e-04 |  |
| [[PAK4]] | +0.65 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[PAFAH1B3]] | +0.64 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[IMMP1L]] | +0.63 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[NEURL1B]] | +0.62 | +0.65 / +0.38 | both halves | 6e-05 |  |
| [[CENPW]] | +0.62 | +0.61 / +0.38 | both halves | 7e-05 |  |
| [[ACACB]] | +0.62 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[C1QTNF3-AMACR]] | +0.61 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[FAM102B]] | +0.61 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[SUFU]] | +0.61 | +0.41 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF621]] | -0.71 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[GCNT4]] | -0.68 | -0.55 / -0.37 | both halves | 7e-05 |  |
| [[EIF5]] | -0.67 | -0.67 / -0.35 | both halves | 1e-04 |  |
| [[UEVLD]] | -0.65 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[CSTF3]] | -0.64 | -0.61 / -0.31 | both halves | 2e-04 |  |
| [[DESI1]] | -0.62 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[ATXN1L]] | -0.61 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[PCBP1-AS1]] | -0.61 | -0.57 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[PPP1R12A-AS2]] | -0.61 | -0.55 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[ZNF337-AS1]] | -0.60 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[CHD1-DT]] | -0.60 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[PBLD]] | -0.60 | -0.52 / -0.22 | both halves | 6e-04 |  |
| [[C8orf33]] | -0.60 | -0.57 / -0.29 | both halves | 2e-04 |  |
| [[FBXO30]] | -0.60 | -0.53 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GUSBP18's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[TOP2A]] | B | TOP2A activity raises GUSBP18's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[C1QTNF3-AMACR]] | C | C1QTNF3-AMACR's natural level strengthens GUSBP18's drug response | C1QTNF3-AMACR's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.60; direction not clear | 0.015 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.4, 6.4); signed map (-28.7, -6.6). **Vector** length 90.2, 22.4% of its response variance represented; |z| ≥ 3 in 1,397 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.0 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | +1.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.1 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.4 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -27.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -14.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -15.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -15.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -11.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -11.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | GUSB pseudogene 18 |
| Locus type | pseudogene |
| Location | 5p13.2 — chr5:34,175,822-34,218,343 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55770](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55770) · Entrez [643373](https://www.ncbi.nlm.nih.gov/gene/643373) · Ensembl [ENSG00000215158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215158)

## Data

Gene col 13249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13249); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13249]; `tensor/DDL_lfc|DDL_z.npy` [13249]; `embed/gene_vectors.npy` [13249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13249 or target_col == 13249). Every well: [[GUSBP18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUSBP18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
