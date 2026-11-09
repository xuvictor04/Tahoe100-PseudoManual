---
symbol: "ATXN1L"
type: "gene"
col: 13399
ensembl_id: "ENSG00000224470"
name: "ataxin 1 like"
location: "16q22.2"
module: 35
arm: "+"
pooled_cpm: 27.11
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ATXN1L

*ataxin 1 like* — 16q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.81× (z +42.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.727× (z -8.6, q 4e-15, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE3B]] (+0.77, fdr 7e-06), [[MMADHC-DT]] (+0.77, fdr 1e-05), [[PBLD]] (+0.77, fdr 8e-06); moves opposite to [[PAFAH1B3]] (-0.71, fdr 3e-05), [[RSAD1]] (-0.68, fdr 2e-05), [[ARL6]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13399.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.81×** | +42.2 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.77×** | +15.4 | 0e+00 | 38/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +15.0 | 0e+00 | 40/47 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +14.9 | 0e+00 | 41/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +10.2 | 2e-22 | 39/48 (SW480, HCT15, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +10.2 | 2e-22 | 36/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +10.0 | 1e-21 | 34/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +9.5 | 2e-19 | 33/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +6.7 | 1e-09 | 24/47 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +6.5 | 4e-09 | 28/48 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.25×** | +6.0 | 1e-07 | 27/48 (HEC-1-A, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.7 | 5e-07 | 25/48 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +5.4 | 3e-06 | 23/46 (LOX-IMVI, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +5.4 | 3e-06 | 22/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +4.9 | 4e-05 | 22/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.53×** | +4.2 | 9e-04 | 15/48 (A498, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.003 | 19/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.005 | 11/48 (KATO III, SW480, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.007 | 18/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13399.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.727×** | -8.6 | 4e-15 | 35/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.661×** | -7.9 | 9e-13 | 35/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.688×** | -7.1 | 2e-10 | 31/48 (RPMI-7951, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.634×** | -4.5 | 8e-04 | 18/48 (CFPAC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.796×** | -4.3 | 0.002 | 20/48 (CFPAC-1, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.825×** | -3.7 | 0.022 | 17/48 (AsPC-1, NCI-H1573, …) | two highest doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.895× | -3.0 | 0.20 | 5/48 (SHP-77, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.5 | 8 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +20.8) | — |
| [[SNU-1 (line)]] | wt | 27.5 | 7 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +12.8) | [[Resveratrol (drug)]] 0.05 µM 0.158× (z -10.5) |
| [[HOP62 (line)]] | alt | 29.6 | 5 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.30× (z +23.7) | [[Lonafarnib (drug)]] 5 µM 0.122× (z -10.1) ⚠ toxic · without an alert: [[Tucidinostat (drug)]] 5 µM 0.520× (z -8.5) |
| [[SW480 (line)]] | alt | 38.8 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +28.5) | — |
| [[BT-474 (line)]] | alt | 29.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.02× (z +15.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 44.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.80× (z +24.3) | — |
| [[HEC-1-A (line)]] | alt | 27.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.89× (z +25.0) | — |
| [[HT-29 (line)]] | alt | 25.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.62× (z +22.9) | — |
| [[NCI-H1573 (line)]] | alt | 31.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.22× (z +21.1) | — |
| [[SK-MEL-2 (line)]] | alt | 26.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 21.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +13.4) | — |
| [[A-427 (line)]] | wt | 19.2 | 1 | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.27× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 18.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.33× (z +15.7) | — |
| [[CHP-212 (line)]] | wt | 43.1 | 0 | 2 (1 ⚠) | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0741× (z -10.2) |
| [[HCT15 (line)]] | alt | 38.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +15.9) | — |
| [[HepG2_C3A (line)]] | wt | 27.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +11.4) | [[Hydroxyurea (drug)]] 0.05 µM 0.111× (z -12.1) |
| [[Hs 766T (line)]] | wt | 38.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +17.5) | — |
| [[HS-578T (line)]] | alt | 17.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +13.7) | — |
| [[LS 180 (line)]] | wt | 21.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.26× (z +21.2) | — |
| [[NCI-H2030 (line)]] | alt | 24.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +19.2) | — |
| [[NCI-H23 (line)]] | alt | 31.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +14.6) | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +15.8) | [[Lonafarnib (drug)]] 5 µM 0.115× (z -8.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 15.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +21.4) | — |
| [[RKO (line)]] | wt | 46.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 28.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +19.7) | — |
| [[A498 (line)]] | wt | 40.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +13.9) | — |
| [[A549 (line)]] | wt | 23.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +15.4) | — |
| [[AN3 CA (line)]] | alt | 27.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.35× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 33.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +15.9) | — |
| [[C-33 A (line)]] | alt | 24.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 24.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +20.5) | — |
| [[COLO 205 (line)]] | alt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +14.2) | — |
| [[H4 (line)]] | wt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +13.3) | — |
| [[J82 (line)]] | alt | 26.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +14.8) | — |
| [[KATO III (line)]] | alt | 33.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.91× (z +19.9) | — |
| [[LoVo (line)]] | wt | 28.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +20.0) | — |
| [[LOX-IMVI (line)]] | wt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 32.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +16.1) | — |
| [[Panc 03.27 (line)]] | alt | 23.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +17.4) | — |
| [[RPMI-7951 (line)]] | alt | 38.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +15.0) | — |
| [[SHP-77 (line)]] | alt | 19.0 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.115× (z -9.5) |
| [[SNU-423 (line)]] | alt | 25.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +14.9) | — |
| [[SW 900 (line)]] | alt | 23.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.03× (z +15.3) | — |
| [[SW48 (line)]] | wt | 21.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.80× (z +11.9) | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE3B]] | +0.77 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[MMADHC-DT]] | +0.77 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[PBLD]] | +0.77 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[ZFHX2-AS1]] | +0.76 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[LINC01004]] | +0.74 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[LINC00571]] | +0.73 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[WDR45]] | +0.73 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[AKT1S1]] | +0.73 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[SIAH2-AS1]] | +0.73 | +0.56 / +0.36 | both halves | 1e-04 |  |
| [[AP4S1]] | +0.72 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.72 | +0.61 / +0.33 | both halves | 1e-04 |  |
| [[MYLK4]] | +0.72 | +0.55 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAFAH1B3]] | -0.71 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[RSAD1]] | -0.68 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ARL6]] | -0.68 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[RADX]] | -0.68 | -0.46 / -0.60 | both halves | 2e-05 |  |
| [[REPS1]] | -0.66 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[SMYD3]] | -0.66 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[CAMK2G]] | -0.65 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SPATA6]] | -0.65 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[ATG4C]] | -0.65 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[HMGN3]] | -0.65 | -0.43 / -0.67 | both halves | 3e-05 |  |
| [[ANTKMT]] | -0.64 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[CDC14B]] | -0.64 | -0.58 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATXN1L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RAB3IP]] | B | RAB3IP activity lowers ATXN1L's level | lines that do not express RAB3IP (8) vs lines expressing it (42) | 1.43× higher at baseline in the lines without RAB3IP | 0.039 | ⚠ within organs, on part of the lines; also absent: TBC1D30, CXCL16, ENSG00000288591; maybe low, not absent |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises ATXN1L's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.27× lower at baseline in the lines without ZNF341-AS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ATXN1L's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ATXN1L's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZHX2]] | B | ZHX2 activity raises ATXN1L's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.25× lower at baseline in the lines without ZHX2 | 0.084 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (7.8, 10.7); signed map (22.4, -7.5). **Vector** length 104, 24.8% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.5 | +42.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.2 | +15.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +14.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +10.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.7 | -8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.8 | -7.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -6.8 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.5 | -7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.5 | -4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -1.4 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -2.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ataxin 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.2 — chr16:71,808,439-71,885,268 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BOAT1 |
| Gene groups (HGNC) | Ataxin 1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [P0C7T5](https://www.uniprot.org/uniprotkb/P0C7T5) (Ataxin-1-like):

> Chromatin-binding factor that repress Notch signaling in the absence of Notch intracellular domain by acting as a CBF1 corepressor. Binds to the HEY promoter and might assist, along with NCOR2, RBPJ-mediated repression. Can suppress ATXN1 cytotoxicity in spinocerebellar ataxia type 1 (SCA1). In concert with CIC and ATXN1, involved in brain development (By similarity).

**Summary**, from NCBI Gene [342371](https://www.ncbi.nlm.nih.gov/gene/342371):

> Predicted to enable RNA binding activity and chromatin binding activity. Predicted to be involved in several processes, including learning or memory; negative regulation of transcription by RNA polymerase II; and social behavior. Predicted to act upstream of or within extracellular matrix organization; lung alveolus development; and positive regulation of hematopoietic stem cell proliferation. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33279](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33279) · Entrez [342371](https://www.ncbi.nlm.nih.gov/gene/342371) · UniProt [P0C7T5](https://www.uniprot.org/uniprotkb/P0C7T5) · Ensembl [ENSG00000224470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224470)

## Data

Gene col 13399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13399); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13399]; `tensor/DDL_lfc|DDL_z.npy` [13399]; `embed/gene_vectors.npy` [13399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13399 or target_col == 13399). Every well: [[ATXN1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATXN1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
