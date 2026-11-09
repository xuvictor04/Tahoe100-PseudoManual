---
symbol: "ACTL6A"
type: "gene"
col: 5873
ensembl_id: "ENSG00000136518"
name: "actin like 6A"
location: "3q26.33"
module: 6
arm: "+"
pooled_cpm: 47.5
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ACTL6A

*actin like 6A* — 3q26.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.43× (z +15.2, q 0e+00, up in 37 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +12.5, q 1e-33, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.525× (z -11.5, q 9e-28, down in 44 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 5 lines (NCI-H2347 0.354×, SW480 0.434×, A498 0.449×, A-427 0.411×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.220×, C-33 A 0.296×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.130×; ⚠ cell-cycle shift, would explain all of this change); [[Tadalafil (drug)]] 5 µM in 1 line (SW 1271 0.0559×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEDD1]] (+0.69, fdr 7e-06), [[VRK1]] (+0.66, fdr 7e-06), [[MRE11]] (+0.64, fdr 7e-06); moves opposite to [[AP5Z1]] (-0.63, fdr 7e-06), [[CACFD1]] (-0.61, fdr 3e-05), [[OSGIN1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF165]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5873.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.43×** | +15.2 | 0e+00 | 37/41 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.26×** | +14.5 | 1e-45 | 45/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +12.5 | 1e-33 | 39/48 (SW1417, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.67×** | +8.8 | 2e-16 | 37/47 (A-427, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.61×** | +8.2 | 3e-14 | 37/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.43×** | +6.4 | 2e-08 | 31/48 (A-172, C32, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.3 | 2e-08 | 25/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +5.9 | 3e-07 | 33/47 (CFPAC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.39×** | +5.8 | 3e-07 | 29/48 (A549, LOX-IMVI, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.38×** | +5.8 | 5e-07 | 32/48 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **1.34×** | +5.3 | 8e-06 | 25/46 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +4.8 | 6e-05 | 25/48 (A-172, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **1.33×** | +4.8 | 9e-05 | 27/43 (KATO III, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~75% of this change | **1.29×** | +4.4 | 4e-04 | 23/47 (LS 180, LOX-IMVI, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +4.0 | 0.003 | 20/48 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.010 | 14/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.19× | +3.0 | 0.076 | 13/48 (PANC-1, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5873.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 5 lines (NCI-H2347 0.354×, SW480 0.434×, A498 0.449×, A-427 0.411×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.220×, C-33 A 0.296×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.130×; ⚠ cell-cycle shift, would explain all of this change); [[Tadalafil (drug)]] 5 µM in 1 line (SW 1271 0.0559×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.525×** | -11.5 | 9e-28 | 44/48 (NCI-H2347, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.827×** | -4.8 | 5e-04 | 19/48 (J82, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -4.0 | 0.012 | 3/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.809×** | -3.6 | 0.042 | 15/47 (SK-MEL-2, A498, …) | rises with dose |  |
| [[Posaconazole (drug)]] 5 µM |  | 0.828× | -3.2 | 0.14 | 11/48 (PANC-1, A-172, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5873. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 58.6 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Auranofin (drug)]] 5 µM 0.449× (z -9.3) |
| [[PANC-1 (line)]] | alt | 65.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +9.2) | — |
| [[SW480 (line)]] | alt | 60.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Auranofin (drug)]] 5 µM 0.434× (z -10.6) |
| [[A-172 (line)]] | wt | 53.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A-427 (line)]] | wt | 93.5 | 1 (1 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.2) ⚠ cell-cycle shift, explains ~27% of this change | [[Auranofin (drug)]] 5 µM 0.411× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 31.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 38.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[KATO III (line)]] | alt | 64.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LS 180 (line)]] | wt | 37.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 63.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H460 (line)]] | wt | 27.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SNU-423 (line)]] | alt | 24.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +9.4) | — |
| [[A549 (line)]] | wt | 28.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[AN3 CA (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.130× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 27.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[C-33 A (line)]] | alt | 53.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HEC-1-A (line)]] | alt | 53.7 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HS-578T (line)]] | alt | 65.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.374× (z -9.0) |
| [[J82 (line)]] | alt | 81.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 28.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[LOX-IMVI (line)]] | wt | 31.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 66.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.354× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 59.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +10.2) | — |
| [[SK-MEL-2 (line)]] | alt | 57.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW 1271 (line)]] | alt | 49.1 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0559× (z -8.7) |
| [[SW1417 (line)]] | alt | 61.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5873), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEDD1]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[VRK1]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[MRE11]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[GMPS]] | +0.63 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[SETD3]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 | pathway: Chromatin modifying enzymes |
| [[ILF2]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[CEP78]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[MAD2L1]] | +0.62 | +0.65 / +0.63 | both halves | 7e-06 | STRING 414 |
| [[NCAPD3]] | +0.61 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[NUP93]] | +0.61 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MCM6]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[DDIAS]] | +0.60 | +0.66 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP5Z1]] | -0.63 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[CACFD1]] | -0.61 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[OSGIN1]] | -0.61 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[UAP1L1]] | -0.61 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[SLC26A11]] | -0.60 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[SHC2]] | -0.59 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[CELF6]] | -0.59 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[CDK3]] | -0.58 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[SLC31A2]] | -0.58 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ADNP2]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 | pathway: ATP-dependent chromatin remodelers |
| [[ABAT]] | -0.55 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[CRYM]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF165]] | B | ZNF165 activity raises ACTL6A's level | lines that do not express ZNF165 (19) vs lines expressing it (31) | 1.24× lower at baseline in the lines without ZNF165 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ENSG00000224621, ESRP2, CNKSR1 |
| [[TOP2A]] | B | TOP2A activity lowers ACTL6A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-30.8, -41.7); signed map (-32.8, -44.4). **Vector** length 103, 27.5% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +12.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.5 | +8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.5 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +2.4 | +14.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +6.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.8 | +0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.7 | +1.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.6 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -12.4 | -11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -1.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | actin like 6A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.33 — chr3:179,562,886-179,588,407 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Actl6, BAF53A, Arp4, Baf53a, INO80K, SMARCN1 |
| Gene groups (HGNC) | INO80 complex subunits; SRCAP complex subunits; Actin related proteins; BAF complex subunits; PBAF complex subunits; GBAF complex subunits |
| Reactome | 29 pathways, smallest: Formation of the non-canonical BAF (ncBAF) complex; Formation of the canonical BAF (cBAF) complex; Formation of the polybromo-BAF (pBAF) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O96019](https://www.uniprot.org/uniprotkb/O96019) (Actin-like protein 6A):

> Involved in transcriptional activation and repression of select genes by chromatin remodeling (alteration of DNA-nucleosome topology). Component of SWI/SNF chromatin remodeling complexes that carry out key enzymatic activities, changing chromatin structure by altering DNA-histone contacts within a nucleosome in an ATP-dependent manner. Required for maximal ATPase activity of SMARCA4/BRG1/BAF190A and for association of the SMARCA4/BRG1/BAF190A containing remodeling complex BAF with …

**Summary**, from NCBI Gene [86](https://www.ncbi.nlm.nih.gov/gene/86):

> This gene encodes a family member of actin-related proteins (ARPs), which share significant amino acid sequence identity to conventional actins. Both actins and ARPs have an actin fold, which is an ATP-binding cleft, as a common feature. The ARPs are involved in diverse cellular processes, including vesicular transport, spindle orientation, nuclear migration and chromatin remodeling. This gene encodes a 53 kDa subunit protein of the BAF (BRG1/brm-associated factor) complex in mammals, which is …

**Accessions** — [HGNC:24124](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24124) · Entrez [86](https://www.ncbi.nlm.nih.gov/gene/86) · UniProt [O96019](https://www.uniprot.org/uniprotkb/O96019) · Ensembl [ENSG00000136518](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136518)

## Data

Gene col 5873: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5873); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5873, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5873]; `tensor/DDL_lfc|DDL_z.npy` [5873]; `embed/gene_vectors.npy` [5873]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5873 or target_col == 5873). Every well: [[ACTL6A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTL6A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
