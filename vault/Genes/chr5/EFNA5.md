---
symbol: "EFNA5"
type: "gene"
col: 11522
ensembl_id: "ENSG00000184349"
name: "ephrin A5"
location: "5q21.3"
module: 174
arm: "+"
pooled_cpm: 623.77
n_lines_expressing: 39
n_dd_up: 0
n_dd_down: 43
n_dd_up_clean: 0
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# EFNA5

*ephrin A5* — 5q21.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 1 line (LS 180 2.40×); [[Tucidinostat (drug)]] 0.5 µM in 1 line (LS 180 2.73×; ⚠ cell-cycle shift, explains ~21% of this change); [[Clobetasol propionate (drug)]] 5 µM in 1 line (Hs 766T 2.46×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (Hs 766T 2.46×).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.342× (z -16.1, q 0e+00, down in 36 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PITPNC1]] (+0.68, fdr 7e-06), [[DOCK5]] (+0.64, fdr 7e-06), [[RGS17]] (+0.62, fdr 7e-06); moves opposite to [[GPRC5B]] (-0.48, fdr 7e-05), [[EPB41]] (-0.44, fdr 4e-05), [[CGNL1]] (-0.43, fdr 6e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MARCHF3]] → it (grade B ⚠); 2 go from it, the strongest it → [[NIBAN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11522.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 1 line (LS 180 2.40×); [[Tucidinostat (drug)]] 0.5 µM in 1 line (LS 180 2.73×; ⚠ cell-cycle shift, explains ~21% of this change); [[Clobetasol propionate (drug)]] 5 µM in 1 line (Hs 766T 2.46×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (Hs 766T 2.46×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Afatinib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.98 | 17/38 (NCI-H2347, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11522.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.342×** | -16.1 | 0e+00 | 36/37 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.352×** | -15.6 | 0e+00 | 36/37 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.522×** | -13.8 | 8e-41 | 33/37 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.435×** | -12.0 | 6e-31 | 29/34 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.449×** | -11.5 | 1e-28 | 34/36 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.466×** | -10.6 | 4e-24 | 28/34 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.497×** | -10.1 | 6e-22 | 28/37 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.511×** | -10.0 | 7e-22 | 30/37 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.525×** | -9.6 | 3e-20 | 33/37 (SHP-77, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.516×** | -9.1 | 6e-18 | 31/38 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.589×** | -7.9 | 1e-13 | 35/37 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.616×** | -7.2 | 2e-11 | 29/37 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.711×** | -7.2 | 3e-11 | 28/37 (NCI-H1573, SHP-77, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.632×** | -6.9 | 3e-10 | 30/37 (NCI-H460, SW 900, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.655×** | -6.3 | 1e-08 | 22/37 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.777×** | -5.3 | 3e-06 | 26/38 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.697×** | -4.9 | 2e-05 | 23/37 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.545×** | -4.7 | 6e-05 | 33/37 (A-172, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.559×** | -4.5 | 1e-04 | 28/37 (SW 900, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.585×** | -4.2 | 7e-04 | 27/37 (H4, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.759×** | -4.1 | 9e-04 | 22/37 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.759×** | -4.1 | 9e-04 | 25/37 (CFPAC-1, Panc 03.27, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11522. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2,891 | 0 | 37 (17 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -31.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -26.2) |
| [[HOP62 (line)]] | alt | 580 | 0 | 22 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -23.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0924× (z -21.4) |
| [[LOX-IMVI (line)]] | wt | 2,160 | 0 | 21 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -27.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0909× (z -24.8) |
| [[NCI-H1792 (line)]] | alt | 1,398 | 0 | 19 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -22.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.199× (z -15.2) |
| [[SW 900 (line)]] | alt | 894 | 0 | 19 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -21.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.141× (z -19.4) |
| [[A549 (line)]] | wt | 1,821 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -26.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -26.3) |
| [[SHP-77 (line)]] | alt | 639 | 0 | 15 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -21.1) |
| [[AsPC-1 (line)]] | alt | 1,351 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -30.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.129× (z -22.2) |
| [[A-172 (line)]] | wt | 493 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -18.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 839 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -24.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -16.6) |
| [[HS-578T (line)]] | alt | 422 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -18.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -17.3) |
| [[PANC-1 (line)]] | alt | 483 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.460× (z -10.2) |
| [[A-427 (line)]] | wt | 346 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.356× (z -14.9) |
| [[BT-474 (line)]] | alt | 354 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -13.0) |
| [[C-33 A (line)]] | alt | 509 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -17.6) |
| [[CFPAC-1 (line)]] | alt | 1,002 | 0 | 7 (2 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.220× (z -11.2) |
| [[Hs 766T (line)]] | wt | 489 | 2 | 5 (3 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 2.46× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.309× (z -11.3) |
| [[KATO III (line)]] | alt | 378 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -16.6) |
| [[MIA PaCa-2 (line)]] | alt | 464 | 0 | 7 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.134× (z -18.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.207× (z -15.3) |
| [[HT-29 (line)]] | alt | 429 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -15.0) |
| [[SNU-1 (line)]] | wt | 822 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.253× (z -15.1) |
| [[NCI-H2347 (line)]] | alt | 705 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -12.6) |
| [[J82 (line)]] | alt | 271 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.352× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 548 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.316× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 583 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -12.1) |
| [[LS 180 (line)]] | wt | 158 | 2 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.40× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.435× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 252 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 367 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.387× (z -9.0) |
| [[C32 (line)]] | wt | 200 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.261× (z -11.1) |
| [[COLO 205 (line)]] | alt | 211 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 248 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -11.4) |
| [[A498 (line)]] | wt | 426 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 104 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 353 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 287 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 110 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 60.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 48.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 120 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 103 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 578 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 687 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 121 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 50.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 447 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 355 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 62.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11522), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNC1]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[DOCK5]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[RGS17]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[MAP3K5]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[NPAS2]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[MAML3]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[HMGA2]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[TREM1]] | +0.56 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ADGRE2]] | +0.56 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[RTN1]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TBC1D8]] | +0.54 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[HS3ST3B1]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRC5B]] | -0.48 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[EPB41]] | -0.44 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[CGNL1]] | -0.43 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[MTMR9LP]] | -0.43 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[MAPK3]] | -0.42 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[NDRG4]] | -0.42 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ENTHD1]] | -0.42 | -0.36 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARCHF3]] | B | MARCHF3 activity raises EFNA5's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 2.76× lower at baseline in the lines without MARCHF3 | 0.064 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[LINC01950]] | C | LINC01950 activity raises EFNA5's level | lines that do not express LINC01950 (13) vs lines expressing it (37) | 4.38× lower at baseline in the lines without LINC01950 | 0.007 | ⚠ within organs, on part of the lines; also absent: EFNA5, TLR1, ENSG00000289526; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIBAN2]] | B | EFNA5 activity raises NIBAN2's level | lines that do not express EFNA5 (11) vs lines expressing it (39) | 1.39× lower at baseline in the lines without EFNA5 | 0.092 | ⚠ within organs, on part of the lines; also absent: LINC01950; maybe low, not absent |
| [[LINC01950]] | C | EFNA5 activity raises LINC01950's level | lines that do not express EFNA5 (11) vs lines expressing it (39) | 3.09× lower at baseline in the lines without EFNA5 | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC01950; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.3, 6.1); signed map (8.3, 48.7). **Vector** length 108, 35.6% of its response variance represented; |z| ≥ 3 in 1,636 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | -0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | -0.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.2 | -0.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.0 | +0.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.4 | -7.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.1 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.1 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.8 | -3.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.7 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ephrin A5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q21.3 — chr5:107,376,894-107,670,937 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AF1, LERK7; previously EPLG7 |
| Gene groups (HGNC) | Ephrins |
| Hallmark sets | APICAL_SURFACE, G2M_CHECKPOINT |
| Reactome | 5 pathways, smallest: EPHA-mediated growth cone collapse; EPH-ephrin mediated repulsion of cells; EPH-Ephrin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P52803](https://www.uniprot.org/uniprotkb/P52803) (Ephrin-A5):

> Cell surface GPI-bound ligand for Eph receptors, a family of receptor tyrosine kinases which are crucial for migration, repulsion and adhesion during neuronal, vascular and epithelial development. Binds promiscuously Eph receptors residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as …

**Summary**, from NCBI Gene [1946](https://www.ncbi.nlm.nih.gov/gene/1946):

> Ephrin-A5, a member of the ephrin gene family, prevents axon bundling in cocultures of cortical neurons with astrocytes, a model of late stage nervous system development and differentiation. The EPH and EPH-related receptors comprise the largest subfamily of receptor protein-tyrosine kinases and have been implicated in mediating developmental events, particularly in the nervous system. EPH receptors typically have a single kinase domain and an extracellular region containing a Cys-rich domain …

**Accessions** — [HGNC:3225](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3225) · Entrez [1946](https://www.ncbi.nlm.nih.gov/gene/1946) · UniProt [P52803](https://www.uniprot.org/uniprotkb/P52803) · Ensembl [ENSG00000184349](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184349)

## Data

Gene col 11522: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11522); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11522, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11522]; `tensor/DDL_lfc|DDL_z.npy` [11522]; `embed/gene_vectors.npy` [11522]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11522 or target_col == 11522). Every well: [[EFNA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFNA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
