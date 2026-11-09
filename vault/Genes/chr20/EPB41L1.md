---
symbol: "EPB41L1"
type: "gene"
col: 1531
ensembl_id: "ENSG00000088367"
name: "erythrocyte membrane protein band 4.1 like 1"
location: "20q11.23"
module: 31
arm: "+"
pooled_cpm: 99.63
n_lines_expressing: 46
n_dd_up: 3
n_dd_down: 43
n_dd_up_clean: 2
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 29
direction_downstream: 1
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# EPB41L1

*erythrocyte membrane protein band 4.1 like 1* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.25× (z +4.5, q 0.004, up in 20 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.22× (z +3.9, q 0.023, up in 17 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A-427 3.17×, A498 2.59×, NCI-H460 2.79×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 2.77×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 3.27×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 2.11×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (Hs 766T 2.48×); [[Binimetinib (drug)]] 0.5 µM in 1 line (AsPC-1 1.97×).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.401× (z -25.6, q 0e+00, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANXA11]] (+0.67, fdr 7e-06), [[RHPN2]] (+0.63, fdr 7e-06), [[KIAA1522]] (+0.62, fdr 1e-05); moves opposite to [[ST3GAL3]] (-0.55, fdr 1e-05), [[CLMP]] (-0.48, fdr 5e-05), [[CNRIP1]] (-0.47, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 29 arrows point to it, the strongest [[PCDH1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[KIF13B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1531.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A-427 3.17×, A498 2.59×, NCI-H460 2.79×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 2.77×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 3.27×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 2.11×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (Hs 766T 2.48×); [[Binimetinib (drug)]] 0.5 µM in 1 line (AsPC-1 1.97×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.5 | 0.004 | 20/45 (A498, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.023 | 17/44 (A549, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.20×** | +3.7 | 0.040 | 14/44 (HS-578T, J82, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.6 | 0.040 | 13/44 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.19× | +3.4 | 0.072 | 13/44 (A498, HEC-1-A, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.11 | 14/44 (CFPAC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.15 | 12/44 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | 1.17× | +3.0 | 0.15 | 9/44 (CFPAC-1, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.15 | 13/43 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.11× | +3.0 | 0.15 | 9/45 (CFPAC-1, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1531.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.401×** | -25.6 | 0e+00 | 40/44 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.341×** | -20.4 | 0e+00 | 40/44 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.370×** | -19.6 | 0e+00 | 40/44 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.381×** | -19.1 | 0e+00 | 38/44 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.492×** | -14.0 | 2e-42 | 36/44 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.533×** | -12.4 | 2e-33 | 34/44 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.544×** | -12.0 | 2e-31 | 34/44 (NCI-H1792, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.584×** | -10.6 | 2e-24 | 31/44 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.382×** | -10.0 | 2e-21 | 38/45 (KATO III, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.630×** | -9.1 | 4e-18 | 26/44 (LoVo, SW1417, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.630×** | -9.1 | 5e-18 | 33/44 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.666×** | -7.7 | 6e-13 | 29/44 (SW480, RKO, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.677×** | -7.7 | 7e-13 | 26/44 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.493×** | -7.3 | 1e-11 | 30/44 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.692×** | -7.3 | 1e-11 | 29/44 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.793×** | -6.5 | 3e-09 | 24/44 (C32, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.733×** | -6.1 | 2e-08 | 25/43 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.803×** | -6.1 | 3e-08 | 23/45 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.694×** | -6.0 | 4e-08 | 24/44 (LoVo, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1531. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 212 | 0 | 19 (9 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0443× (z -29.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.114× (z -29.1) |
| [[CFPAC-1 (line)]] | alt | 172 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -24.5) |
| [[KATO III (line)]] | alt | 387 | 0 | 15 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -19.4) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.300× (z -16.9) |
| [[Hs 766T (line)]] | wt | 481 | 1 | 12 (6 ⚠) | [[Cobimetinib (drug)]] 0.5 µM 2.48× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -24.9) |
| [[SW1417 (line)]] | alt | 392 | 0 | 13 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -27.6) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.506× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 118 | 0 | 12 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -15.5) |
| [[COLO 205 (line)]] | alt | 326 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0864× (z -30.4) |
| [[HEC-1-A (line)]] | alt | 177 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -20.0) |
| [[LS 180 (line)]] | wt | 88.9 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -19.9) |
| [[BT-474 (line)]] | alt | 89.7 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -20.5) |
| [[A-172 (line)]] | wt | 96.5 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -22.4) |
| [[AsPC-1 (line)]] | alt | 179 | 3 (1 ⚠) | 5 (4 ⚠) | [[Trametinib (drug)]] 0.5 µM 2.11× (z +9.1) | [[Belinostat (drug)]] 5 µM 0.156× (z -19.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.410× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 37.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0570× (z -21.5) |
| [[Panc 03.27 (line)]] | alt | 115 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -16.2) |
| [[SW480 (line)]] | alt | 80.8 | 0 | 8 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.209× (z -17.4) |
| [[HOP62 (line)]] | alt | 50.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -13.6) |
| [[A498 (line)]] | wt | 68.7 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -18.0) |
| [[NCI-H1573 (line)]] | alt | 63.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 57.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -11.1) |
| [[RKO (line)]] | wt | 60.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -13.5) |
| [[A549 (line)]] | wt | 90.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -22.9) |
| [[HS-578T (line)]] | alt | 41.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 86.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -24.2) |
| [[NCI-H460 (line)]] | wt | 26.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 0.05 µM 0.316× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 40.4 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.205× (z -11.0) |
| [[A-427 (line)]] | wt | 55.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.300× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 45.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 3.27× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -10.2) |
| [[C32 (line)]] | wt | 28.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -9.2) |
| [[HCT15 (line)]] | alt | 72.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 121 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -15.7) |
| [[HT-29 (line)]] | alt | 82.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -17.3) |
| [[J82 (line)]] | alt | 44.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -11.0) |
| [[SNU-423 (line)]] | alt | 57.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.0) |
| [[AN3 CA (line)]] | alt | 64.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -9.5) |
| [[SW 900 (line)]] | alt | 52.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.209× (z -13.2) |
| [[SW48 (line)]] | wt | 60.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.298× (z -8.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[C-33 A (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1531), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA11]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[RHPN2]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[KIAA1522]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[PTPRR]] | +0.61 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[ITGB6]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[JUP]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[ST14]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[TC2N]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[EPS8L1]] | +0.55 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[MYO18A]] | +0.55 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[TJP2]] | +0.54 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[TMPRSS2]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL3]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[CLMP]] | -0.48 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[CNRIP1]] | -0.47 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[C10orf88]] | -0.44 | -0.48 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 29, C 0. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH1]] | B | PCDH1 activity raises EPB41L1's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.50× lower at baseline in the lines without PCDH1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[HSD17B2]] | B | HSD17B2 activity raises EPB41L1's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 3.01× lower at baseline in the lines without HSD17B2 | 0.013 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[RBM47]] | B | RBM47 activity raises EPB41L1's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.62× lower at baseline in the lines without RBM47 | 0.019 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[C6orf132]] | B | C6orf132 activity raises EPB41L1's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 2.74× lower at baseline in the lines without C6orf132 | 0.022 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[ITGB4]] | B | ITGB4 activity raises EPB41L1's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 2.71× lower at baseline in the lines without ITGB4 | 0.022 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[LGALS9]] | B | LGALS9 activity raises EPB41L1's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.66× lower at baseline in the lines without LGALS9 | 0.024 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[ATP8B1]] | B | ATP8B1 activity raises EPB41L1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.27× lower at baseline in the lines without ATP8B1 | 0.024 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[TSPAN1]] | B | TSPAN1 activity raises EPB41L1's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 2.59× lower at baseline in the lines without TSPAN1 | 0.037 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[INAVA]] | B | INAVA activity raises EPB41L1's level | lines that do not express INAVA (29) vs lines expressing it (21) | 2.39× lower at baseline in the lines without INAVA | 0.040 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[PTPRB]] | B | PTPRB activity raises EPB41L1's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 1.96× lower at baseline in the lines without PTPRB | 0.042 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[SULF2]] | B | SULF2 activity raises EPB41L1's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 2.08× lower at baseline in the lines without SULF2 | 0.044 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[CLIC5]] | B | CLIC5 activity weakens EPB41L1's drug response | lines that do not express CLIC5 (33) vs lines expressing it (12) | the lines without CLIC5 respond 1.01× as strongly (z diff -0.29); strongest at Digitoxin 0.5 µM: 0.47x vs 0.73x (z diff -3.4) | 0.045 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF13B]] | C | EPB41L1 activity raises KIF13B's level | lines that do not express EPB41L1 (4) vs lines expressing it (46) | 2.58× lower at baseline in the lines without EPB41L1 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KCP, PAOX, ENSG00000257489; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.1, 56.6); signed map (57.8, -6.8). **Vector** length 96.9, 28.6% of its response variance represented; |z| ≥ 3 in 1,588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.5 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +4.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +3.7 | -7.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.6 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.0 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -7.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -5.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.8 | -6.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -4.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | erythrocyte membrane protein band 4.1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:36,091,504-36,232,799 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0338, 4.1N |
| Gene groups (HGNC) | Erythrocyte membrane protein band 4.1; FERM domain containing |
| Reactome | 11 pathways, smallest: Glutamate binding, activation of AMPA receptors and synaptic plasticity; Trafficking of AMPA receptors; Sensory processing of sound by outer hair cells of the cochlea |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4G0](https://www.uniprot.org/uniprotkb/Q9H4G0) (Band 4.1-like protein 1):

> May function to confer stability and plasticity to neuronal membrane via multiple interactions, including the spectrin-actin-based cytoskeleton, integral membrane channels and membrane-associated guanylate kinases.

**Summary**, from NCBI Gene [2036](https://www.ncbi.nlm.nih.gov/gene/2036):

> Erythrocyte membrane protein band 4.1 (EPB41) is a multifunctional protein that mediates interactions between the erythrocyte cytoskeleton and the overlying plasma membrane. The encoded protein binds and stabilizes D2 and D3 dopamine receptors at the neuronal plasma membrane. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:3378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3378) · Entrez [2036](https://www.ncbi.nlm.nih.gov/gene/2036) · UniProt [Q9H4G0](https://www.uniprot.org/uniprotkb/Q9H4G0) · Ensembl [ENSG00000088367](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088367)

## Data

Gene col 1531: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1531); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1531, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1531]; `tensor/DDL_lfc|DDL_z.npy` [1531]; `embed/gene_vectors.npy` [1531]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1531 or target_col == 1531). Every well: [[EPB41L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPB41L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
