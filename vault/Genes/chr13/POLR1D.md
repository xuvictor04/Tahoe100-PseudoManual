---
symbol: "POLR1D"
type: "gene"
col: 11787
ensembl_id: "ENSG00000186184"
name: "RNA polymerase I and III subunit D"
location: "13q12.2"
module: 43
arm: "+"
pooled_cpm: 54.63
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# POLR1D

*RNA polymerase I and III subunit D* — 13q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +21.4, q 0e+00, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.181×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.220×; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.197×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG29]] (+0.66, fdr 1e-05), [[RPL14]] (+0.66, fdr 1e-05), [[MANBA]] (+0.64, fdr 7e-06); moves opposite to [[SMC1A]] (-0.62, fdr 1e-05), [[DNMT1]] (-0.57, fdr 2e-05), [[CLSPN]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IPO9]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11787.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +21.4 | 0e+00 | 47/48 (LOX-IMVI, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +9.2 | 6e-18 | 32/48 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +9.2 | 6e-18 | 40/45 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +8.6 | 8e-16 | 35/48 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +8.2 | 2e-14 | 36/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +8.0 | 2e-13 | 36/50 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.96×** | +7.2 | 3e-11 | 29/36 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +7.2 | 3e-11 | 34/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +7.0 | 1e-10 | 33/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +6.5 | 6e-09 | 30/47 (AsPC-1, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +6.4 | 8e-09 | 28/49 (COLO 205, HT-29, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +5.5 | 2e-06 | 22/41 (SW 900, LoVo, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.30×** | +5.4 | 2e-06 | 26/48 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +5.3 | 5e-06 | 26/47 (SW1417, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +5.2 | 6e-06 | 21/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +4.8 | 5e-05 | 23/48 (LS 180, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.002 | 18/48 (NCI-H460, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.007 | 19/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.008 | 18/48 (SNU-1, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.6 | 0.009 | 12/48 (COLO 205, LoVo, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.6 | 0.009 | 11/48 (RPMI-7951, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11787.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.181×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.220×; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.197×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | 0.894× | -3.3 | 0.48 | 7/48 (LOX-IMVI, NCI-H2030, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -3.1 | 0.48 | 11/48 (PANC-1, Panc 03.27, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.866× | -3.0 | 0.48 | 11/48 (SW480, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11787. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 42.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +12.1) | — |
| [[NCI-H460 (line)]] | wt | 44.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +16.4) | — |
| [[A-172 (line)]] | wt | 44.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +15.6) | — |
| [[COLO 205 (line)]] | alt | 147 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +19.7) | — |
| [[LOX-IMVI (line)]] | wt | 42.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +17.9) | — |
| [[SW480 (line)]] | alt | 78.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.02× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 52.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +14.8) | — |
| [[HT-29 (line)]] | alt | 159 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +14.7) | — |
| [[J82 (line)]] | alt | 49.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +13.4) | — |
| [[LoVo (line)]] | wt | 71.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 40.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +16.8) | — |
| [[RKO (line)]] | wt | 60.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -16.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 41.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +11.8) | — |
| [[A-427 (line)]] | wt | 35.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.3) | — |
| [[A549 (line)]] | wt | 49.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 40.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 41.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 76.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +13.3) | — |
| [[HepG2_C3A (line)]] | wt | 71.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 37.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 62.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 25.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 57.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +11.0) | — |
| [[KATO III (line)]] | alt | 68.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 72.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 41.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 48.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +13.5) | — |
| [[NCI-H596 (line)]] | alt | 62.2 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.197× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 88.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 38.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +13.5) | — |
| [[SW1417 (line)]] | alt | 61.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +11.7) | — |
| [[SW48 (line)]] | wt | 61.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11787), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 6 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG29]] | +0.66 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[RPL14]] | +0.66 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[MANBA]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[RPL22]] | +0.61 | +0.38 / +0.70 | both halves | 6e-05 |  |
| [[NACA]] ⚠ | +0.58 | +0.57 / +0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS4X]] | +0.56 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[RPL30]] ⚠ | +0.56 | +0.47 / +0.57 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BTF3]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 | STRING 478 |
| [[NSA2]] | +0.55 | +0.56 / +0.49 | both halves | 1e-05 | STRING 404 |
| [[EIF3E]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[RPL37]] ⚠ | +0.55 | +0.44 / +0.60 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL21]] ⚠ | +0.55 | +0.44 / +0.57 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CNGB3]] | +0.54 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[RPL13A]] | +0.54 | +0.30 / +0.64 | both halves | 2e-04 |  |
| [[PARP6]] | +0.54 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[EEF1B2]] | +0.54 | +0.46 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC1A]] | -0.62 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[DNMT1]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 | pathway: Epigenetic regulation of gene expression; STRING 402 |
| [[CLSPN]] | -0.55 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[SNRPB]] | -0.53 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[MCM10]] | -0.52 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[TEDC1]] | -0.51 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[UQCC2]] | -0.50 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[AKIRIN1]] | -0.50 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[FEN1]] | -0.50 | -0.63 / -0.36 | both halves | 1e-04 | pathway: HALLMARK_DNA_REPAIR |
| [[TUBB4B]] | -0.50 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[KIF24]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[ESCO2]] | -0.49 | -0.35 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IPO9]] | C | IPO9's natural level strengthens POLR1D's drug response | IPO9's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.12; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MCM10]] | C | MCM10 activity raises POLR1D's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 1.72× lower at baseline in the lines without MCM10 | 0.070 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.477). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.3, -31.1); signed map (-60.4, -7.7). **Vector** length 91.4, 21.8% of its response variance represented; |z| ≥ 3 in 857 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +21.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +4.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.1 | +7.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.0 | +4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.9 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +3.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -1.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.0 | -1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.0 | -0.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.7 | -2.3 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase I and III subunit D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.2 — chr13:27,620,742-27,744,237 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPAC2, RPA16, RPO1-3, RPA9, MGC9850, AC19 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 19 pathways, smallest: RNA Polymerase III Chain Elongation; RNA Polymerase III Transcription Termination; RNA Polymerase III Transcription Initiation From Type 2 Promoter |
| Matched by | ensembl_id |

UniProt [P0DPB5](https://www.uniprot.org/uniprotkb/P0DPB5) carries no function annotation.

**Summary**, from NCBI Gene [51082](https://www.ncbi.nlm.nih.gov/gene/51082):

> The protein encoded by this gene is a component of the RNA polymerase I and RNA polymerase III complexes, which function in the synthesis of ribosomal RNA precursors and small RNAs, respectively. Mutations in this gene are a cause of Treacher Collins syndrome (TCS), a craniofacial development disorder. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2011]

**Accessions** — [HGNC:20422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20422) · Entrez [51082](https://www.ncbi.nlm.nih.gov/gene/51082) · UniProt [P0DPB5](https://www.uniprot.org/uniprotkb/P0DPB5) · Ensembl [ENSG00000186184](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186184)

## Data

Gene col 11787: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11787); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11787, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11787]; `tensor/DDL_lfc|DDL_z.npy` [11787]; `embed/gene_vectors.npy` [11787]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11787 or target_col == 11787). Every well: [[POLR1D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR1D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
