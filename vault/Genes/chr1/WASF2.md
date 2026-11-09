---
symbol: "WASF2"
type: "gene"
col: 8142
ensembl_id: "ENSG00000158195"
name: "WASP family member 2"
location: "1p36.11"
module: 76
arm: "+"
pooled_cpm: 261.19
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 30
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# WASF2

*WASP family member 2* — 1p36.11

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (HOP62 1.25×, MIA PaCa-2 1.37×; ⚠ position not correctable); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 2.30×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.579× (z -16.5, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRAS]] (+0.73, fdr 1e-05), [[F11R]] (+0.70, fdr 1e-05), [[RAB11FIP1]] (+0.70, fdr 4e-05); moves opposite to [[ECHDC1]] (-0.64, fdr 4e-05), [[ABCE1]] (-0.64, fdr 1e-05), [[DNAJC11]] (-0.62, fdr 4e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ATG9B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8142.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (HOP62 1.25×, MIA PaCa-2 1.37×; ⚠ position not correctable); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 2.30×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +7.9 | 1e-12 | 2/50 (HOP62, MIA PaCa-2) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.24× | +3.2 | 0.35 | 24/47 (PANC-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8142.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.579×** | -16.5 | 0e+00 | 47/49 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.589×** | -16.0 | 0e+00 | 44/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.512×** | -14.3 | 6e-44 | 43/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.577×** | -11.3 | 2e-27 | 43/48 (H4, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.581×** | -11.1 | 1e-26 | 41/47 (HOP62, SW 900, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.595×** | -11.1 | 2e-26 | 45/48 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.596×** | -11.0 | 3e-26 | 40/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.602×** | -10.8 | 2e-25 | 41/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.662×** | -8.8 | 9e-17 | 43/48 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.664×** | -8.4 | 2e-15 | 41/48 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.678×** | -8.3 | 6e-15 | 39/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.781×** | -7.5 | 4e-12 | 35/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.706×** | -7.1 | 4e-11 | 39/50 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.729×** | -6.7 | 6e-10 | 36/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.816×** | -6.1 | 3e-08 | 26/48 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.737×** | -5.6 | 9e-07 | 32/48 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.665×** | -4.5 | 2e-04 | 25/48 (A-427, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.676×** | -4.4 | 3e-04 | 31/49 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.812×** | -4.3 | 5e-04 | 25/47 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.685×** | -4.2 | 6e-04 | 30/48 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.686×** | -4.2 | 6e-04 | 31/48 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.815×** | -4.2 | 6e-04 | 26/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8142. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 401 | 0 | 20 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -24.4) |
| [[HOP62 (line)]] | alt | 324 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -17.8) |
| [[CFPAC-1 (line)]] | alt | 263 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -18.1) |
| [[A549 (line)]] | wt | 303 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -18.8) |
| [[Hs 766T (line)]] | wt | 419 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -15.2) |
| [[HT-29 (line)]] | alt | 467 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -16.4) |
| [[SNU-423 (line)]] | alt | 290 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -15.9) |
| [[A-172 (line)]] | wt | 178 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.365× (z -12.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 419 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -21.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 252 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 270 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -14.0) |
| [[LoVo (line)]] | wt | 210 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.576× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 433 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -14.9) |
| [[SW 900 (line)]] | alt | 215 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -12.2) |
| [[H4 (line)]] | wt | 284 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.217× (z -15.4) |
| [[hTERT-HPNE (line)]] | wt | 248 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -15.9) |
| [[MIA PaCa-2 (line)]] | alt | 299 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -16.7) |
| [[SK-MEL-2 (line)]] | alt | 212 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -13.0) |
| [[BT-474 (line)]] | alt | 234 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -12.2) |
| [[HS-578T (line)]] | alt | 402 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -11.4) |
| [[J82 (line)]] | alt | 254 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.483× (z -12.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.609× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 249 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 190 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -11.3) |
| [[COLO 205 (line)]] | alt | 229 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -11.4) |
| [[LS 180 (line)]] | wt | 261 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 172 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.551× (z -9.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.661× (z -9.1) |
| [[PANC-1 (line)]] | alt | 307 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -10.9) |
| [[HCT15 (line)]] | alt | 294 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -9.4) |
| [[KATO III (line)]] | alt | 222 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -11.5) |
| [[SW480 (line)]] | alt | 223 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -9.0) |
| [[A498 (line)]] | wt | 181 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.519× (z -9.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[AN3 CA (line)]] | alt | 200 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.328× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 219 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 299 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -9.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[RPMI-7951 (line)]] | alt | 245 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.496× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[SHP-77 (line)]] | alt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 219 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -12.1) |
| [[SW 1088 (line)]] | alt | 363 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.229× (z -8.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 177 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.510× (z -9.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 230 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 188 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 142 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 301 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 155 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 203 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8142), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAS]] | +0.73 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[F11R]] | +0.70 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[RAB11FIP1]] | +0.70 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[MGST3]] | +0.69 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[SPSB3]] | +0.68 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MTMR14]] | +0.66 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[GET1]] | +0.66 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[MOSPD3]] | +0.66 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[RANBP10]] | +0.66 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[LINC01881]] | +0.66 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[MACO1]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[RIOK3]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECHDC1]] | -0.64 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ABCE1]] | -0.64 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.62 | -0.67 / -0.43 | both halves | 4e-05 |  |
| [[ZNF462]] | -0.62 | -0.68 / -0.35 | both halves | 1e-04 |  |
| [[TRIM44]] | -0.61 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[ANAPC7]] | -0.61 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[PPIL1]] | -0.60 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.60 | -0.71 / -0.45 | both halves | 3e-05 |  |
| [[UTP20]] | -0.59 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[ADCK1]] | -0.59 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[NCR3LG1]] | -0.58 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[ZFP91]] | -0.58 | -0.70 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[LTV1]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATG9B]] | B | ATG9B activity raises WASF2's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.25× lower at baseline in the lines without ATG9B | 0.032 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[TOP2A]] | B | TOP2A activity raises WASF2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.0, -0.5); signed map (-23.8, 14.2). **Vector** length 106, 37.6% of its response variance represented; |z| ≥ 3 in 1,312 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +7.2 | -11.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +7.2 | -14.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +5.9 | -10.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.1 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +1.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.5 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.1 | -8.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -5.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -7.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | WASP family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:27,404,230-27,490,167 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WAVE2, SCAR2 |
| Gene groups (HGNC) | Wiskott-Aldrich Syndrome protein family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 19 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6W5](https://www.uniprot.org/uniprotkb/Q9Y6W5) (Actin-binding protein WASF2):

> Downstream effector molecule involved in the transmission of signals from tyrosine kinase receptors and small GTPases to the actin cytoskeleton. Promotes formation of actin filaments. Part of the WAVE complex that regulates lamellipodia formation. The WAVE complex regulates actin filament reorganization via its interaction with the Arp2/3 complex.

**Summary**, from NCBI Gene [10163](https://www.ncbi.nlm.nih.gov/gene/10163):

> This gene encodes a member of the Wiskott-Aldrich syndrome protein family. The gene product is a protein that forms a multiprotein complex that links receptor kinases and actin. Binding to actin occurs through a C-terminal verprolin homology domain in all family members. The multiprotein complex serves to tranduce signals that involve changes in cell shape, motility or function. The published map location (PMID:10381382) has been changed based on recent genomic sequence comparisons, which …

**Accessions** — [HGNC:12733](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12733) · Entrez [10163](https://www.ncbi.nlm.nih.gov/gene/10163) · UniProt [Q9Y6W5](https://www.uniprot.org/uniprotkb/Q9Y6W5) · Ensembl [ENSG00000158195](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158195)

## Data

Gene col 8142: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8142); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8142, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8142]; `tensor/DDL_lfc|DDL_z.npy` [8142]; `embed/gene_vectors.npy` [8142]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8142 or target_col == 8142). Every well: [[WASF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WASF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
