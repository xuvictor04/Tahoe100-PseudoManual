---
symbol: "ACBD3"
type: "gene"
col: 11330
ensembl_id: "ENSG00000182827"
name: "acyl-CoA binding domain containing 3"
location: "1q42.12"
module: 41
arm: "+"
pooled_cpm: 282.76
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ACBD3

*acyl-CoA binding domain containing 3* — 1q42.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.79× (z +9.0, q 1e-16, up in 46 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 6 lines (A-427 4.15×, SW480 4.75×, LOX-IMVI 5.35×, hTERT-HPNE 4.39×, …).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.351× (z -16.8, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.712× (z -7.7, q 3e-12, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRP54]] (+0.90, fdr 7e-06), [[SSR2]] (+0.84, fdr 7e-06), [[SPTY2D1]] (+0.83, fdr 7e-06); moves opposite to [[PRRC2B]] (-0.70, fdr 7e-06), [[VMA21]] (-0.66, fdr 7e-06), [[HNRNPK]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CREG2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GOLPH3L]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11330.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 6 lines (A-427 4.15×, SW480 4.75×, LOX-IMVI 5.35×, hTERT-HPNE 4.39×, …).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.79×** | +9.0 | 1e-16 | 46/49 (A-427, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 1.44× | +3.2 | 0.39 | 24/48 (HEC-1-A, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11330.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.351×** | -16.8 | 0e+00 | 43/44 (H4, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.469×** | -11.7 | 4e-29 | 43/45 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.360×** | -11.2 | 1e-26 | 44/49 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.712×** | -7.7 | 3e-12 | 29/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.758×** | -6.3 | 3e-08 | 34/49 (A498, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.677×** | -6.2 | 5e-08 | 39/48 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.768×** | -6.0 | 1e-07 | 39/48 (HOP62, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.704×** | -5.6 | 1e-06 | 32/48 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.730×** | -5.2 | 1e-05 | 31/48 (HT-29, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.800×** | -5.0 | 3e-05 | 29/48 (hTERT-HPNE, RPMI-7951, …) | top dose only | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.732×** | -4.9 | 5e-05 | 32/47 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.748×** | -4.6 | 2e-04 | 28/48 (A-172, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.753×** | -4.5 | 3e-04 | 31/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.783×** | -4.0 | 0.002 | 26/48 (LoVo, C32, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.793×** | -3.8 | 0.005 | 28/48 (NCI-H1573, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.811×** | -3.5 | 0.018 | 27/48 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.802×** | -3.5 | 0.018 | 25/47 (H4, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.821×** | -3.3 | 0.032 | 23/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.830×** | -3.1 | 0.056 | 23/48 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | **0.831×** | -3.1 | 0.056 | 26/49 (COLO 205, C32, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.832×** | -3.0 | 0.060 | 21/48 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.834× | -3.0 | 0.066 | 22/48 (SW 900, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.837× | -2.9 | 0.075 | 21/49 (HCT15, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11330. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 325 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.525× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 413 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -19.1) |
| [[HS-578T (line)]] | alt | 289 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.363× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.588× (z -9.7) |
| [[HT-29 (line)]] | alt | 290 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.551× (z -12.5) |
| [[A-172 (line)]] | wt | 383 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.589× (z -10.2) |
| [[A498 (line)]] | wt | 596 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.534× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 369 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.489× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 463 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.433× (z -16.4) |
| [[H4 (line)]] | wt | 370 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0599× (z -28.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.6) |
| [[hTERT-HPNE (line)]] | wt | 336 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.39× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.579× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 323 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.443× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.594× (z -9.5) |
| [[Hs 766T (line)]] | wt | 341 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.494× (z -10.9) |
| [[SW 900 (line)]] | alt | 553 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -20.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 256 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 254 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.503× (z -10.4) |
| [[A-427 (line)]] | wt | 148 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.15× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -22.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 300 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.6) |
| [[COLO 205 (line)]] | alt | 346 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.526× (z -8.6) |
| [[HCT15 (line)]] | alt | 373 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -17.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 160 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.18× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 246 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.388× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 296 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 268 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -13.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 330 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -14.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 329 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -9.3) ⚠ cell-cycle shift, explains ~19% of this change |
| [[J82 (line)]] | alt | 235 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -12.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 144 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.35× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 272 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -11.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 249 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -14.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 223 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -10.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 220 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.47× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -18.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 241 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.396× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 244 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.425× (z -9.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 251 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.423× (z -10.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 261 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -11.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 186 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.75× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 160 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 123 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 203 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 162 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 224 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 220 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 332 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 188 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11330), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54]] | +0.90 | +0.90 / +0.87 | both halves | 7e-06 |  |
| [[SSR2]] | +0.84 | +0.81 / +0.80 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.83 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.83 | +0.80 / +0.83 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.82 | +0.83 / +0.75 | both halves | 7e-06 |  |
| [[OSBP]] | +0.81 | +0.83 / +0.74 | both halves | 7e-06 | STRING 786 |
| [[COG6]] | +0.81 | +0.85 / +0.70 | both halves | 7e-06 |  |
| [[YIPF5]] | +0.81 | +0.78 / +0.82 | both halves | 7e-06 |  |
| [[SEC61B]] | +0.80 | +0.73 / +0.81 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.79 | +0.85 / +0.71 | both halves | 7e-06 |  |
| [[TMEM208]] | +0.79 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[COPB1]] | +0.79 | +0.87 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC2B]] | -0.70 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[VMA21]] | -0.66 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.66 | -0.54 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREG2]] | B | CREG2 activity raises ACBD3's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without CREG2 | 0.040 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity raises ACBD3's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.43× lower at baseline in the lines without TMEM92-AS1 | 0.047 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[AGR2]] | B | AGR2 activity raises ACBD3's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.25× lower at baseline in the lines without AGR2 | 0.053 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GOLPH3L]] | C | ACBD3's natural level strengthens GOLPH3L's drug response | ACBD3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.17; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.861). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.6, -34.8); signed map (-50.2, 12.3). **Vector** length 157, 63.4% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intra-Golgi and retrograde Golgi-to-ER traffic* (reactome, mean cos +0.57 to 12); *Asparagine N-linked glycosylation* (reactome, mean cos +0.58 to 12); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.63 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.8 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +5.5 | -2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.9 | -5.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +9.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.2 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | -1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.6 | +0.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +3.4 | +1.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.4 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.6 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -8.3 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.4 | -2.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.3 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.4 | -6.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.4 | -4.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -4.2 | -4.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -3.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA binding domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.12 — chr1:226,144,679-226,186,741 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCP60, PAP7; previously GOLPH1, GOCAP1 |
| Gene groups (HGNC) | A-kinase anchoring proteins |
| Reactome | 4 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3P7](https://www.uniprot.org/uniprotkb/Q9H3P7) (Golgi resident protein GCP60):

> Involved in the maintenance of Golgi structure by interacting with giantin, affecting protein transport between the endoplasmic reticulum and Golgi. Involved in hormone-induced steroid biosynthesis in testicular Leydig cells (By similarity). Recruits PI4KB to the Golgi apparatus membrane; enhances the enzyme activity of PI4KB activity via its membrane recruitment thereby increasing the local concentration of the substrate in the vicinity of the kinase.; (Microbial infection) Plays an essential …

**Summary**, from NCBI Gene [64746](https://www.ncbi.nlm.nih.gov/gene/64746):

> The Golgi complex plays a key role in the sorting and modification of proteins exported from the endoplasmic reticulum. The protein encoded by this gene is involved in the maintenance of Golgi structure and function through its interaction with the integral membrane protein giantin. It may also be involved in the hormonal regulation of steroid formation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15453) · Entrez [64746](https://www.ncbi.nlm.nih.gov/gene/64746) · UniProt [Q9H3P7](https://www.uniprot.org/uniprotkb/Q9H3P7) · Ensembl [ENSG00000182827](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182827)

## Data

Gene col 11330: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11330); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11330, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11330]; `tensor/DDL_lfc|DDL_z.npy` [11330]; `embed/gene_vectors.npy` [11330]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11330 or target_col == 11330). Every well: [[ACBD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACBD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
