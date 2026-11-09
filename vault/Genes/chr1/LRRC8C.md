---
symbol: "LRRC8C"
type: "gene"
col: 10119
ensembl_id: "ENSG00000171488"
name: "leucine rich repeat containing 8 VRAC subunit C"
location: "1p22.2"
module: 110
arm: "+"
pooled_cpm: 61.23
n_lines_expressing: 42
n_dd_up: 3
n_dd_down: 42
n_dd_up_clean: 1
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 16
direction_downstream: 14
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# LRRC8C

*leucine rich repeat containing 8 VRAC subunit C* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.40× (z +5.5, q 2e-05, up in 22 of 40 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.26× (z +3.7, q 0.047, up in 16 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (LoVo 2.49×, SW48 4.87×, SNU-1 2.85×, HEC-1-A 1.83×, …; ⚠ cell-cycle shift, explains ~2% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SW480 2.49×).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.394× (z -15.1, q 0e+00, down in 35 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 0.631× (z -7.1, q 1e-10, down in 25 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA1549L]] (+0.77, fdr 7e-06), [[CORO2B]] (+0.72, fdr 7e-06), [[TMEM158]] (+0.71, fdr 7e-06); moves opposite to [[ARFGEF2]] (-0.55, fdr 1e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[BCL2A1]] → it (grade B ⚠); 14 go from it, the strongest it → [[TSPAN5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10119.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (LoVo 2.49×, SW48 4.87×, SNU-1 2.85×, HEC-1-A 1.83×, …; ⚠ cell-cycle shift, explains ~2% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SW480 2.49×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.40×** | +5.5 | 2e-05 | 22/40 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.33×** | +4.6 | 1e-03 | 19/39 (CFPAC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.047 | 16/39 (CFPAC-1, SW 900, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.4 | 0.080 | 13/41 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.22× | +3.3 | 0.10 | 18/40 (SW480, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.1 | 0.16 | 14/40 (SW480, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10119.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.394×** | -15.1 | 0e+00 | 35/41 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.444×** | -12.6 | 5e-34 | 27/33 (NCI-H1792, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.618×** | -7.2 | 1e-10 | 25/37 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.631×** | -7.1 | 1e-10 | 25/40 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.668×** | -6.5 | 7e-09 | 26/40 (HS-578T, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.696×** | -6.5 | 7e-09 | 24/40 (NCI-H1573, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.669×** | -6.5 | 7e-09 | 24/41 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.681×** | -6.5 | 7e-09 | 24/42 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.678×** | -6.3 | 2e-08 | 25/40 (A549, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.696×** | -5.8 | 3e-07 | 25/40 (Hs 766T, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.771×** | -5.7 | 6e-07 | 23/41 (NCI-H1573, HepG2/C3A, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.735×** | -5.0 | 3e-05 | 22/40 (H4, NCI-H23, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.737×** | -4.9 | 4e-05 | 23/40 (SK-MEL-2, H4, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.805×** | -4.9 | 4e-05 | 23/40 (RKO, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.741×** | -4.9 | 4e-05 | 23/41 (NCI-H1573, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.788×** | -4.4 | 3e-04 | 19/40 (NCI-H1573, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.543×** | -4.4 | 3e-04 | 19/39 (SW48, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.745×** | -4.4 | 4e-04 | 17/40 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.757×** | -4.3 | 5e-04 | 17/40 (NCI-H1792, Hs 766T, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 229 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.193× (z -13.6) |
| [[RKO (line)]] | wt | 174 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0458× (z -30.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.437× (z -11.6) |
| [[HS-578T (line)]] | alt | 127 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.284× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 204 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.298× (z -10.4) |
| [[HOP62 (line)]] | alt | 99.7 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.224× (z -13.0) |
| [[A549 (line)]] | wt | 98.5 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -13.6) |
| [[LOX-IMVI (line)]] | wt | 171 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.204× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 115 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.223× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 64.3 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.6) ⚠ cell-cycle shift, explains ~2% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -14.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 41.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -14.5) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.440× (z -9.4) |
| [[A-427 (line)]] | wt | 52.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -15.8) ⚠ cell-cycle shift, explains ~2% of this change |
| [[C-33 A (line)]] | alt | 109 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -15.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 92.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.111× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 67.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0981× (z -19.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 70.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0998× (z -15.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 55.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -12.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 43.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +13.1) ⚠ cell-cycle shift, explains ~2% of this change | [[Dinaciclib (drug)]] 5 µM 0.373× (z -9.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 96.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -17.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 42.6 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.297× (z -9.7) |
| [[C32 (line)]] | wt | 71.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.5) ⚠ cell-cycle shift, explains ~2% of this change | — |
| [[RPMI-7951 (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.283× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~13% of this change |
| [[SNU-1 (line)]] | wt | 45.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.7) ⚠ cell-cycle shift, explains ~2% of this change | — |
| [[SW48 (line)]] | wt | 27.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +10.4) ⚠ cell-cycle shift, explains ~2% of this change | — |
| [[SW480 (line)]] | alt | 23.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.49× (z +8.6) | — |
| [[A498 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 79.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.57 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.78 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1549L]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CORO2B]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[TMEM158]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[ANTXR2]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[ARHGAP22]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[BCL2A1]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[STC1]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[NLRP3]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ITGA2]] | +0.67 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[EFL1]] | +0.67 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[FXYD5]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[RPSAP52]] | +0.65 | +0.64 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFGEF2]] | -0.55 | -0.49 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2A1]] | B | BCL2A1 activity raises LRRC8C's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.42× lower at baseline in the lines without BCL2A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[KCNMA1]] | B | KCNMA1 activity raises LRRC8C's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.23× lower at baseline in the lines without KCNMA1 | 0.015 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[TSPAN5]] | B | TSPAN5 activity raises LRRC8C's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 2.18× lower at baseline in the lines without TSPAN5 | 0.031 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[UBASH3B]] | B | UBASH3B activity raises LRRC8C's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 3.13× lower at baseline in the lines without UBASH3B | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[SGIP1]] | B | SGIP1 activity raises LRRC8C's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 2.19× lower at baseline in the lines without SGIP1 | 0.037 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[KLF12]] | B | KLF12 activity raises LRRC8C's level | lines that do not express KLF12 (9) vs lines expressing it (41) | 2.28× lower at baseline in the lines without KLF12 | 0.039 | ⚠ within organs, on part of the lines; also absent: RHOBTB1, ZC3H12C, GNAI1 |
| [[RASSF8]] | B | RASSF8 activity raises LRRC8C's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 2.69× lower at baseline in the lines without RASSF8 | 0.049 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| [[STC1]] | B | STC1 activity raises LRRC8C's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without STC1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[ARHGAP31]] | B | ARHGAP31 activity raises LRRC8C's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 2.63× lower at baseline in the lines without ARHGAP31 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[MIR100HG]] | B | MIR100HG activity raises LRRC8C's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.33× lower at baseline in the lines without MIR100HG | 0.065 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[INSYN2B]] | B | INSYN2B activity raises LRRC8C's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.21× lower at baseline in the lines without INSYN2B | 0.067 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[PYGL]] | B | PYGL activity raises LRRC8C's level | lines that do not express PYGL (7) vs lines expressing it (43) | 3.83× lower at baseline in the lines without PYGL | 0.075 | ⚠ within organs, on part of the lines; also absent: FAM229B, ANKRD44, WHAMMP3; maybe low, not absent |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN5]] | B | LRRC8C activity raises TSPAN5's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 2.33× lower at baseline in the lines without LRRC8C | 0.042 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[TPBG]] | B | LRRC8C activity raises TPBG's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 2.59× lower at baseline in the lines without LRRC8C | 0.054 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[TSHZ3]] | B | LRRC8C activity raises TSHZ3's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 4.56× lower at baseline in the lines without LRRC8C | 0.057 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[MARCHF4]] | B | LRRC8C activity raises MARCHF4's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 3.03× lower at baseline in the lines without LRRC8C | 0.059 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[KLF12]] | B | LRRC8C activity raises KLF12's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 3.15× lower at baseline in the lines without LRRC8C | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[ARSJ]] | B | LRRC8C activity raises ARSJ's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 2.25× lower at baseline in the lines without LRRC8C | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[STC1]] | B | LRRC8C activity raises STC1's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 5.07× lower at baseline in the lines without LRRC8C | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[CHD1L]] | B | LRRC8C activity raises CHD1L's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 1.98× lower at baseline in the lines without LRRC8C | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[CSNK1E]] | B | LRRC8C activity raises CSNK1E's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without LRRC8C | 0.067 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[RASA3]] | B | LRRC8C activity raises RASA3's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without LRRC8C | 0.083 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[ARHGAP31]] | B | LRRC8C activity raises ARHGAP31's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 3.18× lower at baseline in the lines without LRRC8C | 0.085 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[SPOCK1]] | B | LRRC8C activity raises SPOCK1's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 3.78× lower at baseline in the lines without LRRC8C | 0.091 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.0, 3.8); signed map (3.6, 47.8). **Vector** length 112, 31.0% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +6.0 | +3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | -1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.3 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | -0.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.9 | -0.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.5 | -6.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.5 | -6.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -4.1 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.0 | -7.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.9 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 8 VRAC subunit C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.2 — chr1:89,633,072-89,769,903 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AD158 |
| Gene groups (HGNC) | Volume regulated anion channel subunits |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDW0](https://www.uniprot.org/uniprotkb/Q8TDW0) (Volume-regulated anion channel subunit LRRC8C):

> Non-essential component of the volume-regulated anion channel (VRAC, also named VSOAC channel), an anion channel required to maintain a constant cell volume in response to extracellular or intracellular osmotic changes. The VRAC channel conducts iodide better than chloride and can also conduct organic osmolytes like taurine. Plays a redundant role in the efflux of amino acids, such as aspartate and glutamate, in response to osmotic stress. The VRAC channel also mediates transport of …

**Summary**, from NCBI Gene [84230](https://www.ncbi.nlm.nih.gov/gene/84230):

> Enables volume-sensitive anion channel activity. Involved in cyclic-GMP-AMP transmembrane import across plasma membrane and monoatomic anion transmembrane transport. Located in cytoplasm and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25075) · Entrez [84230](https://www.ncbi.nlm.nih.gov/gene/84230) · UniProt [Q8TDW0](https://www.uniprot.org/uniprotkb/Q8TDW0) · Ensembl [ENSG00000171488](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171488)

## Data

Gene col 10119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10119); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10119]; `tensor/DDL_lfc|DDL_z.npy` [10119]; `embed/gene_vectors.npy` [10119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10119 or target_col == 10119). Every well: [[LRRC8C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC8C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
