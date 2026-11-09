---
symbol: "EGFR"
type: "gene"
col: 7109
ensembl_id: "ENSG00000146648"
name: "epidermal growth factor receptor"
location: "7p11.2"
module: 116
arm: "+"
pooled_cpm: 580.87
n_lines_expressing: 43
n_dd_up: 4
n_dd_down: 33
n_dd_up_clean: 3
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# EGFR

*epidermal growth factor receptor* — 7p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.34× (z +4.8, q 0.001, up in 25 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.242× (z -23.1, q 0e+00, down in 41 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETS1]] (+0.73, fdr 7e-06), [[ASAP1]] (+0.64, fdr 1e-05), [[FRMD6]] (+0.63, fdr 7e-06); moves opposite to [[C20orf96]] (-0.58, fdr 1e-05), [[CDC42SE2]] (-0.58, fdr 1e-05), [[SCAI]] (-0.55, fdr 1e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAMLD1]] → it (grade B ⚠); 5 go from it, the strongest it → [[NABP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7109.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.8 | 0.001 | 25/41 (MIA PaCa-2, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.29×** | +4.1 | 0.010 | 20/41 (HT-29, COLO 205, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.019 | 26/41 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.031 | 22/42 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +3.4 | 0.086 | 11/41 (LoVo, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7109.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.242×** | -23.1 | 0e+00 | 41/41 (NCI-H1792, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.252×** | -22.4 | 0e+00 | 41/41 (NCI-H1792, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.481×** | -16.8 | 0e+00 | 40/42 (A549, SW48, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.374×** | -16.0 | 0e+00 | 41/41 (J82, SW48, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.555×** | -9.2 | 4e-18 | 36/40 (NCI-H1573, SNU-1, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.615×** | -7.9 | 3e-13 | 34/41 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.606×** | -7.8 | 4e-13 | 32/40 (BT-474, H4, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.638×** | -7.3 | 2e-11 | 30/41 (PANC-1, H4, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.656×** | -6.9 | 4e-10 | 28/41 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.670×** | -6.5 | 4e-09 | 28/42 (NCI-H1573, SNU-1, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.688×** | -6.1 | 6e-08 | 26/41 (PANC-1, H4, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.710×** | -5.2 | 1e-05 | 24/38 (A-172, NCI-H1792, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.803×** | -5.1 | 2e-05 | 24/41 (J82, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.728×** | -5.0 | 3e-05 | 26/41 (HEC-1-A, RPMI-7951, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.737×** | -5.0 | 3e-05 | 26/41 (SNU-1, SW48, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.622×** | -4.0 | 0.002 | 24/41 (AsPC-1, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.787×** | -3.9 | 0.003 | 24/41 (H4, SW48, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.776×** | -3.9 | 0.003 | 27/41 (A549, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.795×** | -3.7 | 0.005 | 25/41 (BT-474, SW48, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.651×** | -3.6 | 0.006 | 24/41 (SW48, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.661×** | -3.5 | 0.009 | 22/41 (AsPC-1, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.677×** | -3.3 | 0.018 | 20/41 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7109. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 274 | 18 (4 ⚠) | 2 | [[Adagrasib (drug)]] 0.05 µM 1.99× (z +25.8) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.63× (z +20.1) | [[Panobinostat (drug)]] 5 µM 0.298× (z -12.9) |
| [[H4 (line)]] | wt | 885 | 0 | 15 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -14.3) |
| [[BT-474 (line)]] | alt | 456 | 0 | 13 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -16.5) |
| [[SNU-1 (line)]] | wt | 1,197 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -19.9) |
| [[KATO III (line)]] | alt | 257 | 6 (2 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.97× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.266× (z -18.3) |
| [[SW48 (line)]] | wt | 1,571 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0658× (z -23.1) |
| [[A-172 (line)]] | wt | 786 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -19.3) |
| [[HT-29 (line)]] | alt | 252 | 6 (3 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +16.0) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.260× (z -15.9) |
| [[LOX-IMVI (line)]] | wt | 338 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -22.4) |
| [[NCI-H23 (line)]] | alt | 378 | 2 (1 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.1) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.186× (z -18.7) |
| [[PANC-1 (line)]] | alt | 670 | 1 | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.259× (z -16.0) |
| [[AsPC-1 (line)]] | alt | 1,678 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -20.0) |
| [[LoVo (line)]] | wt | 471 | 5 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +14.5) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.42× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.154× (z -21.6) |
| [[NCI-H1573 (line)]] | alt | 5,990 | 1 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -23.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.188× (z -21.1) |
| [[HEC-1-A (line)]] | alt | 565 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -19.1) |
| [[NCI-H1792 (line)]] | alt | 737 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -24.0) |
| [[NCI-H460 (line)]] | wt | 178 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -16.0) |
| [[Panc 03.27 (line)]] | alt | 656 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -16.4) |
| [[J82 (line)]] | alt | 500 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -22.9) |
| [[SW 900 (line)]] | alt | 353 | 3 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.29× (z +14.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.398× (z -10.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.447× (z -9.6) |
| [[A549 (line)]] | wt | 919 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0766× (z -21.4) |
| [[CFPAC-1 (line)]] | alt | 310 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +8.8) ⚠ cell-cycle shift, explains ~91% of this change | [[Panobinostat (drug)]] 5 µM 0.304× (z -13.4) |
| [[Hs 766T (line)]] | wt | 321 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +17.8) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.199× (z -15.8) |
| [[HS-578T (line)]] | alt | 626 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 4.64× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.124× (z -22.3) |
| [[LS 180 (line)]] | wt | 315 | 1 | 4 | [[BAY1125976 (drug)]] 5 µM 5.51× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.294× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 560 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -16.1) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 340 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -12.2) |
| [[SHP-77 (line)]] | alt | 154 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -10.8) |
| [[SNU-423 (line)]] | alt | 462 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -22.1) |
| [[A-427 (line)]] | wt | 217 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.344× (z -10.7) |
| [[COLO 205 (line)]] | alt | 190 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 3.63× (z +13.0) | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -14.5) |
| [[HOP62 (line)]] | alt | 402 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -15.6) |
| [[hTERT-HPNE (line)]] | wt | 699 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -11.5) |
| [[SW 1088 (line)]] | alt | 987 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -11.2) |
| [[AN3 CA (line)]] | alt | 434 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.176× (z -12.7) |
| [[RKO (line)]] | wt | 155 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -11.5) |
| [[A498 (line)]] | wt | 439 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -9.4) |
| [[HCT15 (line)]] | alt | 335 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.312× (z -11.1) |
| [[C-33 A (line)]] | alt | 66.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 59.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 107 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 64.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 600 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 719 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 353 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 140 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7109), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETS1]] | +0.73 | +0.73 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 545 |
| [[ASAP1]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[FRMD6]] | +0.63 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[CYFIP1]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SRGAP1]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[AXL]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 | STRING 792 |
| [[MIR4435-2HG]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[BACH1]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[CYTOR]] | +0.60 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[TNFRSF12A]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[RASAL2]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[ANAPC1P4]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C20orf96]] | -0.58 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[CDC42SE2]] | -0.58 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[SCAI]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[NDUFAF7]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[SEC61A2]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[INPP5B]] | -0.54 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[CC2D1A]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 | STRING 494 |
| [[IDH1]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS; STRING 795 |
| [[ATPAF2]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[ALG9]] | -0.52 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[DNASE2]] | -0.52 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[NFATC3]] | -0.51 | -0.45 / -0.47 | both halves | 3e-05 | STRING 473 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAMLD1]] | B | MAMLD1 activity raises EGFR's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 2.45× lower at baseline in the lines without MAMLD1 | 0.015 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[C11orf91]] | B | C11orf91 activity raises EGFR's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 3.12× lower at baseline in the lines without C11orf91 | 0.039 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[SMAD3]] | B | SMAD3 activity raises EGFR's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 3.18× lower at baseline in the lines without SMAD3 | 0.052 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[CD59]] | B | CD59 activity raises EGFR's level | lines that do not express CD59 (7) vs lines expressing it (43) | 3.04× lower at baseline in the lines without CD59 | 0.070 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NABP1]] | B | EGFR activity raises NABP1's level | lines that do not express EGFR (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without EGFR | 0.038 | ⚠ within organs, on part of the lines; also absent: C1RL-AS1, PSD4, RNASEL |
| [[HRH1]] | B | EGFR activity raises HRH1's level | lines that do not express EGFR (7) vs lines expressing it (43) | 3.22× lower at baseline in the lines without EGFR | 0.042 | ⚠ within organs, on part of the lines; also absent: C1RL-AS1, PSD4, RNASEL |
| [[NFATC3]] | B | EGFR activity lowers NFATC3's level | lines that do not express EGFR (7) vs lines expressing it (43) | 1.68× higher at baseline in the lines without EGFR | 0.044 | ⚠ within organs, on part of the lines; also absent: C1RL-AS1, PSD4, RNASEL |
| [[CAB39]] | B | EGFR activity raises CAB39's level | lines that do not express EGFR (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without EGFR | 0.091 | ⚠ within organs, on part of the lines; also absent: C1RL-AS1, PSD4, RNASEL |
| [[MAP3K20]] | B | EGFR activity raises MAP3K20's level | lines that do not express EGFR (7) vs lines expressing it (43) | 1.97× lower at baseline in the lines without EGFR | 0.095 | ⚠ within organs, on part of the lines; also absent: C1RL-AS1, PSD4, RNASEL |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.576). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.9, 10.5); signed map (12.2, 40.7). **Vector** length 119, 39.4% of its response variance represented; |z| ≥ 3 in 1,661 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.1 | +4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +10.4 | -0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +8.2 | +0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.9 | +1.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.2 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | -0.2 |
| fall | [[venetoclax (drug)]] 5 µM |  | -4.1 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.1 | -7.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.7 | -3.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.0 | -7.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | epidermal growth factor receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p11.2 — chr7:55,019,017-55,211,628 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ERBB1, ERRP; previously ERBB |
| Gene groups (HGNC) | Erb-b2 receptor tyrosine kinases |
| Hallmark sets | PROTEIN_SECRETION, PI3K_AKT_MTOR_SIGNALING, ALLOGRAFT_REJECTION, APICAL_JUNCTION, GLYCOLYSIS, HYPOXIA |
| Reactome | 67 pathways, smallest: PLCG1 events in ERBB2 signaling; PTK6 promotes HIF1A stabilization; EGFR Transactivation by Gastrin |
| Matched by | ensembl_id |

**Function**, from UniProt [P00533](https://www.uniprot.org/uniprotkb/P00533) (Epidermal growth factor receptor):

> Receptor tyrosine kinase binding ligands of the EGF family and activating several signaling cascades to convert extracellular cues into appropriate cellular responses. Known ligands include EGF, TGFA/TGF-alpha, AREG, epigen/EPGN, BTC/betacellulin, epiregulin/EREG and HBEGF/heparin-binding EGF. Ligand binding triggers receptor homo- and/or heterodimerization and autophosphorylation on key cytoplasmic residues. The phosphorylated receptor recruits adapter proteins like GRB2 which in turn …

**Summary**, from NCBI Gene [1956](https://www.ncbi.nlm.nih.gov/gene/1956):

> The protein encoded by this gene is a transmembrane glycoprotein that is a member of the protein kinase superfamily. This protein is a receptor for members of the epidermal growth factor family. EGFR is a cell surface protein that binds to epidermal growth factor, thus inducing receptor dimerization and tyrosine autophosphorylation leading to cell proliferation. Mutations in this gene are associated with lung cancer. EGFR is a component of the cytokine storm which contributes to a severe form …

**Accessions** — [HGNC:3236](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3236) · Entrez [1956](https://www.ncbi.nlm.nih.gov/gene/1956) · UniProt [P00533](https://www.uniprot.org/uniprotkb/P00533) · Ensembl [ENSG00000146648](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146648)

## Data

Gene col 7109: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7109); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7109, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7109]; `tensor/DDL_lfc|DDL_z.npy` [7109]; `embed/gene_vectors.npy` [7109]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7109 or target_col == 7109). Every well: [[EGFR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EGFR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
