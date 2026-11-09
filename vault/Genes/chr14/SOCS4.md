---
symbol: "SOCS4"
type: "gene"
col: 11075
ensembl_id: "ENSG00000180008"
name: "suppressor of cytokine signaling 4"
location: "14q22.3"
module: 3
arm: "-"
pooled_cpm: 39.68
n_lines_expressing: 50
n_dd_up: 47
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SOCS4

*suppressor of cytokine signaling 4* — 14q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (21 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.62× (z +20.2, q 0e+00, up in 43 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +18.3, q 0e+00, up in 42 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Malotilate (drug)]] 0.05 µM in 1 line (NCI-H661 0.0414×); [[GSK1059615 (drug)]] 0.5 µM in 1 line (A498 0.280×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PURB]] (+0.64, fdr 1e-05), [[ZNF655]] (+0.63, fdr 1e-05), [[ARSB]] (+0.63, fdr 3e-05); moves opposite to [[HEATR5B]] (-0.70, fdr 3e-05), [[AFMID]] (-0.69, fdr 1e-05), [[ELP2]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 59 in all, 27 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11075.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.62×** | +20.2 | 0e+00 | 43/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +18.3 | 0e+00 | 42/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.06×** | +15.8 | 0e+00 | 46/47 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +15.5 | 0e+00 | 44/47 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.02×** | +14.7 | 0e+00 | 38/43 (NCI-H1573, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.02×** | +14.2 | 5e-44 | 36/45 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.89×** | +14.0 | 2e-42 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.85×** | +13.5 | 2e-39 | 43/47 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.84×** | +13.4 | 7e-39 | 38/47 (NCI-H2347, KATO III, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.13×** | +13.1 | 3e-37 | 45/49 (A498, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.49×** | +12.3 | 4e-33 | 33/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +12.1 | 8e-32 | 40/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +11.1 | 3e-27 | 34/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +10.6 | 2e-24 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.61×** | +10.4 | 1e-23 | 41/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +9.8 | 3e-21 | 35/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +9.6 | 3e-20 | 40/48 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +8.6 | 2e-16 | 35/47 (LS 180, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +7.5 | 2e-12 | 28/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +7.2 | 1e-11 | 37/48 (NCI-H23, RKO, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.22×** | +6.0 | 3e-08 | 20/48 (A549, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11075.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Malotilate (drug)]] 0.05 µM in 1 line (NCI-H661 0.0414×); [[GSK1059615 (drug)]] 0.5 µM in 1 line (A498 0.280×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.731× | -3.6 | 0.17 | 17/48 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.749× | -3.4 | 0.23 | 9/46 (SNU-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | 0.907× | -3.1 | 0.27 | 8/48 (HCT15, KATO III, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.823× | -3.1 | 0.27 | 16/47 (RKO, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11075. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 58.1 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +16.3) | — |
| [[NCI-H460 (line)]] | wt | 44.5 | 8 (6 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +13.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.75× (z +9.4) | — |
| [[A498 (line)]] | wt | 30.6 | 4 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 7.70× (z +11.7) | [[GSK1059615 (drug)]] 0.5 µM 0.280× (z -10.0) |
| [[A549 (line)]] | wt | 44.6 | 5 (1 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.38× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 25.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.2) | — |
| [[KATO III (line)]] | alt | 27.9 | 4 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.80× (z +12.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.34× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 29.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.8) | — |
| [[C32 (line)]] | wt | 30.3 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.84× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.6) | — |
| [[LoVo (line)]] | wt | 51.3 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.57× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 30.0 | 3 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.29× (z +11.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 32.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +14.2) | — |
| [[NCI-H2347 (line)]] | alt | 31.1 | 3 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.84× (z +9.4) ⚠ toxic | — |
| [[PANC-1 (line)]] | alt | 37.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.6) | — |
| [[A-172 (line)]] | wt | 28.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[C-33 A (line)]] | alt | 49.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 36.7 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.51× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 43.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H23 (line)]] | alt | 79.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +12.6) | — |
| [[RKO (line)]] | wt | 57.8 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.67× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 48.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HEC-1-A (line)]] | alt | 37.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.76× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 32.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 27.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +12.0) | — |
| [[HT-29 (line)]] | alt | 35.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.75× (z +8.9) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 25.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +8.9) | — |
| [[NCI-H661 (line)]] | alt | 40.7 | 0 | 1 | — | [[Malotilate (drug)]] 0.05 µM 0.0414× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 49.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.93× (z +9.2) ⚠ toxic | — |
| [[SNU-1 (line)]] | wt | 47.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.15× (z +9.6) ⚠ toxic | — |
| [[SNU-423 (line)]] | alt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 46.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.93× (z +8.8) | — |
| [[A-427 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11075), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PURB]] | +0.64 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ZNF655]] | +0.63 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ARSB]] | +0.63 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[AP5M1]] | +0.61 | +0.66 / +0.43 | both halves | 4e-05 |  |
| [[PSME3]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ANAPC7]] | +0.58 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[PRDM5]] | +0.58 | +0.50 / +0.36 | both halves | 1e-04 |  |
| [[MTA2]] | +0.57 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[SNX19]] | +0.57 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TARDBP]] | +0.57 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[CPSF2]] | +0.56 | +0.68 / +0.30 | both halves | 2e-04 |  |
| [[RNASEH1]] | +0.56 | +0.46 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 5 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEATR5B]] | -0.70 | -0.74 / -0.45 | both halves | 3e-05 |  |
| [[AFMID]] | -0.69 | -0.70 / -0.52 | both halves | 1e-05 |  |
| [[ELP2]] | -0.65 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[SNHG7]] | -0.64 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[PMM1]] | -0.62 | -0.43 / -0.57 | both halves | 4e-05 |  |
| [[CNNM4]] | -0.61 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[PPP1R2]] | -0.60 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[CDK7]] | -0.60 | -0.54 / -0.65 | both halves | 1e-05 | pathway: Transcriptional regulation by RUNX1 |
| [[MPND]] | -0.58 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[RANBP10]] | -0.58 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[LCMT1]] | -0.57 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[MPST]] | -0.57 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SOCS4's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.1% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.546). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.9, -18.5); signed map (19.5, -27.8). **Vector** length 93.6, 25.1% of its response variance represented; |z| ≥ 3 in 1,348 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.0 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +5.1 | +14.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +5.0 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +20.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +12.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +7.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.9 | +6.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +3.4 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | -6.5 | +7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | -5.5 | +6.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -4.1 | +9.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.7 | -2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | suppressor of cytokine signaling 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.3 — chr14:55,027,230-55,049,489 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SOCS7 |
| Gene groups (HGNC) | SH2 domain containing; Suppressors of cytokine signaling |
| Reactome | 2 pathways, smallest: RUNX1 regulates transcription of genes involved in differentiation of keratinocytes; Transcriptional regulation by RUNX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXH5](https://www.uniprot.org/uniprotkb/Q8WXH5) (Suppressor of cytokine signaling 4):

> SOCS family proteins form part of a classical negative feedback system that regulates cytokine signal transduction. Substrate-recognition component of a SCF-like ECS (Elongin BC-CUL2/5-SOCS-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Inhibits EGF signaling by mediating the degradation of the Tyr-phosphorylated EGF receptor/EGFR.

**Summary**, from NCBI Gene [122809](https://www.ncbi.nlm.nih.gov/gene/122809):

> The protein encoded by this gene contains a SH2 domain and a SOCS BOX domain. The protein thus belongs to the suppressor of cytokine signaling (SOCS), also known as STAT-induced STAT inhibitor (SSI), protein family. SOCS family members are known to be cytokine-inducible negative regulators of cytokine signaling. Two alternatively spliced transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19392](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19392) · Entrez [122809](https://www.ncbi.nlm.nih.gov/gene/122809) · UniProt [Q8WXH5](https://www.uniprot.org/uniprotkb/Q8WXH5) · Ensembl [ENSG00000180008](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180008)

## Data

Gene col 11075: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11075); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11075, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11075]; `tensor/DDL_lfc|DDL_z.npy` [11075]; `embed/gene_vectors.npy` [11075]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11075 or target_col == 11075). Every well: [[SOCS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOCS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
