---
symbol: "MIR31HG"
type: "gene"
col: 10182
ensembl_id: "ENSG00000171889"
name: "MIR31 host gene"
location: "9p21.3"
module: 116
arm: "+"
pooled_cpm: 256.72
n_lines_expressing: 34
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 8
direction_downstream: 7
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# MIR31HG

*MIR31 host gene* — 9p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.73× (z +6.3, q 2e-07, up in 18 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.50× (z +5.1, q 1e-04, up in 22 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 0.5 µM in 3 lines (NCI-H460 3.33×, NCI-H1573 3.19×, HT-29 2.54×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (COLO 205 11.8×, HT-29 3.65×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H460 3.45×, NCI-H1573 2.86×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H460 3.07×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.582× (z -9.5, q 5e-19, down in 26 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGB1-DT]] (+0.67, fdr 8e-06), [[BMAL2]] (+0.64, fdr 7e-06), [[C6orf141]] (+0.63, fdr 7e-06); moves opposite to [[ZNF451]] (-0.54, fdr 4e-05), [[HAUS4]] (-0.53, fdr 2e-05), [[MTMR4]] (-0.52, fdr 2e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC00707]] → it (grade B ⚠); 7 go from it, the strongest it → [[BMAL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10182.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 0.5 µM in 3 lines (NCI-H460 3.33×, NCI-H1573 3.19×, HT-29 2.54×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (COLO 205 11.8×, HT-29 3.65×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H460 3.45×, NCI-H1573 2.86×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H460 3.07×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +6.3 | 2e-07 | 18/31 (NCI-H460, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +5.1 | 1e-04 | 22/32 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.006 | 21/32 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.65× | +3.3 | 0.16 | 13/25 (NCI-H1573, A498, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.21 | 18/32 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10182.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.582×** | -9.5 | 5e-19 | 26/32 (NCI-H1573, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.583×** | -9.5 | 5e-19 | 26/33 (SW48, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.542×** | -7.7 | 4e-12 | 24/32 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.559×** | -7.0 | 4e-10 | 22/30 (Panc 03.27, SW48, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.617×** | -6.0 | 2e-07 | 22/32 (RKO, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.656×** | -5.3 | 1e-05 | 22/32 (A-427, NCI-H1573, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.759×** | -4.9 | 9e-05 | 24/32 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.679×** | -4.8 | 9e-05 | 23/33 (A-427, RKO, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -4.4 | 7e-04 | 4/34 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.720×** | -3.9 | 0.004 | 20/33 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.720×** | -3.9 | 0.004 | 18/32 (SW48, RKO, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.731×** | -3.9 | 0.004 | 21/32 (HOP62, SW48, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.563×** | -3.8 | 0.008 | 22/33 (HOP62, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.757×** | -3.5 | 0.020 | 17/32 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.751×** | -3.4 | 0.022 | 19/32 (NCI-H23, RKO, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.771×** | -3.2 | 0.039 | 14/32 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.775×** | -3.2 | 0.045 | 17/32 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.615×** | -3.2 | 0.045 | 19/32 (SW48, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.801×** | -3.1 | 0.064 | 16/32 (AsPC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 912 | 3 (1 ⚠) | 28 (6 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.19× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -26.9) |
| [[HOP62 (line)]] | alt | 715 | 0 | 14 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.521× (z -17.8) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.220× (z -16.8) |
| [[SW48 (line)]] | wt | 2,129 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -25.9) |
| [[AsPC-1 (line)]] | alt | 504 | 0 | 11 (4 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.280× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 128 | 0 | 10 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.389× (z -22.5) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -13.1) |
| [[RKO (line)]] | wt | 1,096 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -24.4) |
| [[A-427 (line)]] | wt | 666 | 0 | 9 (8 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -16.7) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.441× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 192 | 8 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 8.40× (z +19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.45× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 399 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -11.4) |
| [[HT-29 (line)]] | alt | 326 | 3 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.65× (z +12.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.54× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -12.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 279 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -13.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -8.9) |
| [[Hs 766T (line)]] | wt | 749 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HEC-1-A (line)]] | alt | 255 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 263 | 2 (1 ⚠) | 1 | [[Pitavastatin (Calcium) (drug)]] 5 µM 4.27× (z +10.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.35× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -8.8) |
| [[A549 (line)]] | wt | 352 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -14.2) |
| [[COLO 205 (line)]] | alt | 196 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 11.8× (z +22.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[KATO III (line)]] | alt | 85.7 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.54× (z +9.2) | — |
| [[LoVo (line)]] | wt | 363 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 210 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -13.1) |
| [[SW480 (line)]] | alt | 102 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.12× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 72.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.60× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 239 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -11.2) |
| [[HS-578T (line)]] | alt | 237 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 143 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -8.5) |
| [[A-172 (line)]] | wt | 21.7 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 46.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 27.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 28.0 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 24.3 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 23.2 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 55.5 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB1-DT]] | +0.67 | +0.58 / +0.71 | both halves | 8e-06 |  |
| [[BMAL2]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[C6orf141]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CDCP1]] | +0.60 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[TBILA]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[DUSP5-DT]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.59 | +0.57 / +0.65 | both halves | 8e-06 |  |
| [[LINC00707]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[CLCF1]] | +0.58 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[NAV3]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[B4GALT6]] | +0.56 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF451]] | -0.54 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[HAUS4]] | -0.53 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[MTMR4]] | -0.52 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[EDN2]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ATF2]] | -0.48 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[MLLT10]] | -0.48 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[SNX2]] | -0.48 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ECH1]] | -0.48 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[CEPT1]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SSBP2]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[PHF21A]] | -0.47 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[TSC22D3]] | -0.47 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00707]] | B | LINC00707 activity raises MIR31HG's level | lines that do not express LINC00707 (26) vs lines expressing it (24) | 2.29× lower at baseline in the lines without LINC00707 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000285845, ENSG00000285743, LINP1 |
| [[RPSAP52]] | B | RPSAP52 activity raises MIR31HG's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 1.93× lower at baseline in the lines without RPSAP52 | 0.025 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[ITGB1-DT]] | B | ITGB1-DT activity raises MIR31HG's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 2.28× lower at baseline in the lines without ITGB1-DT | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[NT5E]] | B | NT5E activity raises MIR31HG's level | lines that do not express NT5E (14) vs lines expressing it (36) | 2.58× lower at baseline in the lines without NT5E | 0.049 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[ITGA2]] | B | ITGA2 activity raises MIR31HG's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.55× lower at baseline in the lines without ITGA2 | 0.055 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[BMAL2]] | B | BMAL2 activity raises MIR31HG's level | lines that do not express BMAL2 (7) vs lines expressing it (43) | 5.22× lower at baseline in the lines without BMAL2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SMCO2, STXBP2, PDLIM1; maybe low, not absent; its own permutation p |
| [[C6orf141]] | B | C6orf141 activity raises MIR31HG's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 1.82× lower at baseline in the lines without C6orf141 | 0.094 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[ITGA2-AS1]] | C | ITGA2-AS1 activity raises MIR31HG's level | lines that do not express ITGA2-AS1 (4) vs lines expressing it (46) | 4.92× lower at baseline in the lines without ITGA2-AS1 | 0.024 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ZNF827, NABP1; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMAL2]] | B | MIR31HG activity raises BMAL2's level | lines that do not express MIR31HG (16) vs lines expressing it (34) | 3.15× lower at baseline in the lines without MIR31HG | 0.003 | ⚠ within organs, on part of the lines; also absent: SMCO2, POU5F1, PLA2R1 |
| [[SEPTIN10]] | B | MIR31HG activity raises SEPTIN10's level | lines that do not express MIR31HG (16) vs lines expressing it (34) | 1.44× lower at baseline in the lines without MIR31HG | 0.020 | ⚠ within organs, on part of the lines; also absent: SMCO2, POU5F1, PLA2R1 |
| [[ITPRID2]] | B | MIR31HG activity raises ITPRID2's level | lines that do not express MIR31HG (16) vs lines expressing it (34) | 1.54× lower at baseline in the lines without MIR31HG | 0.040 | ⚠ within organs, on part of the lines; also absent: SMCO2, POU5F1, PLA2R1 |
| [[RPSAP52]] | B | MIR31HG activity raises RPSAP52's level | lines that do not express MIR31HG (16) vs lines expressing it (34) | 2.05× lower at baseline in the lines without MIR31HG | 0.079 | ⚠ within organs, on part of the lines; also absent: SMCO2, POU5F1, PLA2R1 |
| [[KISS1]] | B | MIR31HG activity raises KISS1's level | lines that do not express MIR31HG (16) vs lines expressing it (34) | 1.82× lower at baseline in the lines without MIR31HG | 0.082 | ⚠ within organs, on part of the lines; also absent: SMCO2, POU5F1, PLA2R1 |
| [[ITGA2]] | B | MIR31HG activity raises ITGA2's level | lines that do not express MIR31HG (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without MIR31HG | 0.084 | ⚠ within organs, on part of the lines; also absent: SMCO2, POU5F1, PLA2R1 |
| [[WNT7B]] | B | MIR31HG activity raises WNT7B's level | lines that do not express MIR31HG (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without MIR31HG | 0.088 | ⚠ within organs, on part of the lines; also absent: SMCO2, POU5F1, PLA2R1 |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.7, 8.1); signed map (7.0, 42.5). **Vector** length 131, 40.8% of its response variance represented; |z| ≥ 3 in 1,260 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM |  | +6.5 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.1 | +5.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | +2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +4.6 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +1.4 |
| fall | [[Budesonide (drug)]] 0.05 µM |  | -4.0 | -2.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -4.0 | -3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -9.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -4.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.8 | -3.1 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -3.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | MIR31 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9p21.3 — chr9:21,380,073-21,559,891 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LOC554202, hsa-lnc-31, LncHIFCAR |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [554202](https://www.ncbi.nlm.nih.gov/gene/554202):

> This gene produces a long non-coding RNA that acts as a host gene for miR-31. This transcript may be involved in cellular pluripotency and regulate the differentiation of myoblasts and other tissues. This RNA was found to interact with Polycomb repressive proteins to repression transcription of genes involves in cell senescence. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:37187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37187) · Entrez [554202](https://www.ncbi.nlm.nih.gov/gene/554202) · Ensembl [ENSG00000171889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171889)

## Data

Gene col 10182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10182); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10182]; `tensor/DDL_lfc|DDL_z.npy` [10182]; `embed/gene_vectors.npy` [10182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10182 or target_col == 10182). Every well: [[MIR31HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR31HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
