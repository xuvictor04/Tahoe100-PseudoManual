---
symbol: "NIPAL2"
type: "gene"
col: 2448
ensembl_id: "ENSG00000104361"
name: "NIPA like domain containing 2"
location: "8q22.2"
module: 137
arm: "+"
pooled_cpm: 10.39
n_lines_expressing: 44
n_dd_up: 13
n_dd_down: 25
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# NIPAL2

*NIPA like domain containing 2* — 8q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.95× (z +8.2, q 2e-13, up in 14 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +5.5, q 7e-06, up in 18 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.199× (z -20.4, q 0e+00, down in 40 of 41 measured lines).
> Its strongest partners by |cos| (75 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RXYLT1]] (+0.72, fdr 3e-05), [[FAIM]] (+0.69, fdr 1e-05), [[KLHL42]] (+0.66, fdr 8e-05); moves opposite to [[DNAAF3]] (-0.71, fdr 5e-05), [[SLC27A1]] (-0.70, fdr 1e-04), [[RAB3A]] (-0.69, fdr 4e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00571]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2448.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +8.2 | 2e-13 | 14/20 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.54×** | +7.7 | 3e-12 | 23/42 (LS 180, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +5.6 | 4e-06 | 15/33 (NCI-H2347, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.5 | 7e-06 | 18/36 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +4.7 | 3e-04 | 14/39 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.29×** | +4.6 | 5e-04 | 12/42 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.42×** | +4.5 | 7e-04 | 14/40 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.37×** | +4.0 | 0.004 | 9/37 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +3.7 | 0.012 | 12/40 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.020 | 13/37 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.027 | 10/42 (KATO III, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.049 | 8/39 (Panc 03.27, Hs 766T, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +3.1 | 0.090 | 6/38 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.27× | +3.0 | 0.10 | 4/41 (H4, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2448.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.199×** | -20.4 | 0e+00 | 40/41 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.254×** | -17.3 | 0e+00 | 38/42 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.255×** | -17.3 | 0e+00 | 39/42 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.489×** | -12.8 | 2e-35 | 31/38 (NCI-H1573, LoVo, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.369×** | -12.6 | 2e-34 | 35/42 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.381×** | -12.2 | 3e-32 | 32/37 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.385×** | -11.2 | 5e-27 | 35/42 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.447×** | -10.2 | 2e-22 | 30/38 (COLO 205, HepG2/C3A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.502×** | -8.7 | 2e-16 | 27/41 (LoVo, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.295×** | -8.1 | 4e-14 | 33/39 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.332×** | -7.3 | 2e-11 | 26/37 (RKO, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.564×** | -7.2 | 2e-11 | 27/40 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.582×** | -6.8 | 4e-10 | 27/42 (HCT15, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.607×** | -6.3 | 1e-08 | 22/40 (HCT15, HepG2/C3A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.403×** | -6.0 | 7e-08 | 26/40 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.659×** | -5.0 | 2e-05 | 21/39 (SW480, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.792×** | -4.2 | 0.001 | 20/41 (LS 180, KATO III, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.546×** | -4.0 | 0.002 | 16/37 (KATO III, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.750×** | -3.6 | 0.008 | 10/42 (NCI-H2030, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.684×** | -3.4 | 0.017 | 8/41 (CHP-212, HCT15, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 45.5 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0586× (z -18.8) |
| [[LoVo (line)]] | wt | 18.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -17.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0937× (z -16.9) |
| [[NCI-H1573 (line)]] | alt | 23.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -18.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.200× (z -11.0) |
| [[RKO (line)]] | wt | 22.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -13.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.102× (z -12.9) |
| [[SW480 (line)]] | alt | 7.29 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0870× (z -15.2) |
| [[HS-578T (line)]] | alt | 27.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0998× (z -14.6) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.133× (z -12.8) |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0843× (z -12.1) |
| [[HCT15 (line)]] | alt | 21.1 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0773× (z -12.1) |
| [[KATO III (line)]] | alt | 14.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -12.2) |
| [[LS 180 (line)]] | wt | 17.8 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.118× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0976× (z -15.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0948× (z -11.4) |
| [[C32 (line)]] | wt | 20.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0829× (z -12.7) |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.202× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 8.56 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -10.3) ⚠ cell-cycle shift, explains ~44% of this change |
| [[RPMI-7951 (line)]] | alt | 17.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -9.5) |
| [[SW1417 (line)]] | alt | 9.11 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0638× (z -13.3) |
| [[SW48 (line)]] | wt | 24.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0832× (z -11.1) |
| [[A-427 (line)]] | wt | 4.07 | 0 | 1 | — | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0617× (z -8.7) |
| [[A549 (line)]] | wt | 5.82 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0719× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0683× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[hTERT-HPNE (line)]] | wt | 21.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.146× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 4.87 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0481× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 7.72 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0660× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 3.99 | 0 | 1 | — | [[Verteporfin (drug)]] 0.5 µM 0.0742× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 3.70 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.121× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -8.9) |
| [[PANC-1 (line)]] | alt | 4.10 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.112× (z -10.5) |
| [[A-172 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 21 of them with an alert (⚠; 21 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RXYLT1]] | +0.72 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[FAIM]] | +0.69 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[KLHL42]] | +0.66 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[NINJ2]] | +0.64 | +0.51 / +0.20 | both halves | 7e-04 |  |
| [[SPRY3]] | +0.64 | +0.36 / +0.37 | both halves | 1e-04 |  |
| [[DPH5-DT]] | +0.64 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[MYLK4]] | +0.63 | +0.44 / +0.23 | both halves | 5e-04 |  |
| [[AVEN]] | +0.63 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[YARS2]] | +0.62 | +0.34 / +0.39 | both halves | 1e-04 |  |
| [[ARSD]] | +0.62 | +0.46 / +0.25 | both halves | 4e-04 |  |
| [[PBLD]] | +0.62 | +0.32 / +0.29 | both halves | 2e-04 |  |
| [[TMCO4]] | +0.62 | +0.50 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF3]] | -0.71 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[SLC27A1]] | -0.70 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[RAB3A]] | -0.69 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[GNAI2]] | -0.68 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[PEDS1]] | -0.66 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[CFD]] | -0.66 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[MAST1]] | -0.64 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[AHDC1]] | -0.62 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[SEPTIN6]] | -0.60 | -0.48 / -0.26 | both halves | 4e-04 |  |
| [[ABCB9]] | -0.60 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[FCHO1]] | -0.60 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[CDON]] | -0.59 | -0.47 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00571]] | B | LINC00571 activity raises NIPAL2's level | lines that do not express LINC00571 (5) vs lines expressing it (45) | 2.42× lower at baseline in the lines without LINC00571 | 0.085 | ⚠ within organs, on part of the lines; also absent: KIFC3, NDRG1, DELEC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.756). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (6.0, -2.3); signed map (24.2, -27.2). **Vector** length 83.2, 17.6% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.3 | +2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +6.0 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.5 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +3.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +2.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -12.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.6 | -11.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -17.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -20.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | -17.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -3.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.4 | -1.9 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.2 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | NIPA like domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.2 — chr8:98,189,826-98,294,393 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13955, SLC57A4; previously NPAL2 |
| Gene groups (HGNC) | Solute carrier family 57, NIPA-like magnesium transporters |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

UniProt [Q9H841](https://www.uniprot.org/uniprotkb/Q9H841) carries no function annotation.

**Summary**, from NCBI Gene [79815](https://www.ncbi.nlm.nih.gov/gene/79815):

> Predicted to enable magnesium ion transmembrane transporter activity. Predicted to be involved in magnesium ion transport. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25854) · Entrez [79815](https://www.ncbi.nlm.nih.gov/gene/79815) · UniProt [Q9H841](https://www.uniprot.org/uniprotkb/Q9H841) · Ensembl [ENSG00000104361](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104361)

## Data

Gene col 2448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2448); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2448]; `tensor/DDL_lfc|DDL_z.npy` [2448]; `embed/gene_vectors.npy` [2448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2448 or target_col == 2448). Every well: [[NIPAL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIPAL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
