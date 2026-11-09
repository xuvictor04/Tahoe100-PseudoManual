---
symbol: "COPS8"
type: "gene"
col: 12628
ensembl_id: "ENSG00000198612"
name: "COP9 signalosome subunit 8"
location: "2q37.3"
module: 104
arm: "+"
pooled_cpm: 39.31
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 1
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# COPS8

*COP9 signalosome subunit 8* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.17× (z +15.0, q 0e+00, up in 43 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.33× (z +8.5, q 1e-15, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.807× (z -4.2, q 0.015, down in 19 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.264×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (SW 1088 0.0835×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPD]] (+0.71, fdr 7e-06), [[MAOA]] (+0.69, fdr 7e-06), [[CCND3]] (+0.68, fdr 7e-06); moves opposite to [[ACVR1C]] (-0.62, fdr 1e-05), [[PTHLH]] (-0.61, fdr 9e-06), [[SLIT2]] (-0.58, fdr 1e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC02220]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 20 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12628.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.17×** | +15.0 | 0e+00 | 43/47 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.12×** | +14.5 | 3e-45 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.09×** | +14.3 | 5e-44 | 46/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.13×** | +14.1 | 9e-43 | 34/39 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.94×** | +12.8 | 1e-35 | 44/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.85×** | +11.0 | 6e-26 | 34/43 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.33×** | +8.5 | 1e-15 | 37/48 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.48×** | +7.5 | 4e-12 | 33/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.45×** | +7.1 | 7e-11 | 27/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +7.0 | 2e-10 | 32/47 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +6.6 | 2e-09 | 29/48 (NCI-H1573, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.40×** | +6.4 | 6e-09 | 31/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.26×** | +6.3 | 1e-08 | 26/47 (A549, NCI-H460, …) | rises with dose | composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | **1.26×** | +6.2 | 2e-08 | 22/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.39×** | +6.1 | 5e-08 | 32/48 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[Budesonide (drug)]] 0.05 µM |  | **1.36×** | +5.9 | 1e-07 | 26/48 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.36×** | +5.9 | 1e-07 | 24/48 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.34×** | +5.6 | 7e-07 | 23/48 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.35×** | +5.5 | 1e-06 | 26/48 (NCI-H1792, H4, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.30×** | +5.1 | 1e-05 | 25/48 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.33×** | +5.1 | 1e-05 | 23/47 (NCI-H1792, LOX-IMVI, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.9 | 2e-05 | 23/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.28×** | +4.8 | 5e-05 | 24/48 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 9e-05 | 23/48 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.27×** | +4.5 | 1e-04 | 22/48 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.26×** | +4.4 | 2e-04 | 23/48 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12628.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.264×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (SW 1088 0.0835×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.807×** | -4.2 | 0.015 | 19/48 (A498, NCI-H460, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.881× | -3.5 | 0.11 | 15/48 (A498, MIA PaCa-2, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12628. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 36.1 | 22 (3 ⚠) | 0 | [[Budesonide (drug)]] 0.5 µM 3.99× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 63.1 | 19 (2 ⚠) | 0 | [[Triamcinolone (drug)]] 5 µM 2.54× (z +12.1) | — |
| [[NCI-H460 (line)]] | wt | 34.7 | 7 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +11.0) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Dexamethasone (drug)]] 0.5 µM 2.23× (z +8.6) | — |
| [[SW480 (line)]] | alt | 41.7 | 6 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +11.9) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[LOX-IMVI (line)]] | wt | 29.0 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.05 µM 3.29× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 39.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LoVo (line)]] | wt | 21.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 42.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 46.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.34× (z +8.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HOP62 (line)]] | alt | 40.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LS 180 (line)]] | wt | 26.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[RKO (line)]] | wt | 43.4 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.09× (z +9.5) ⚠ toxic | — |
| [[A-427 (line)]] | wt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[H4 (line)]] | wt | 48.9 | 1 | 0 | [[Betamethasone dipropionate (drug)]] 5 µM 4.19× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 54.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H23 (line)]] | alt | 44.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SHP-77 (line)]] | alt | 53.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0835× (z -8.7) |
| [[A498 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12628), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPD]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[MAOA]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[CCND3]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[FKBP5]] | +0.62 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[BBS2]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TLR2]] | +0.61 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[IRAK3]] | +0.61 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[FAH]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TNS2]] | +0.60 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ACSL1]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[STOM]] | +0.60 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[TSC22D3]] | +0.59 | +0.61 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACVR1C]] | -0.62 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[PTHLH]] | -0.61 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[SLIT2]] | -0.58 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[HMGN2P46]] | -0.55 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[LINC01828]] | -0.55 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[LHX1]] | -0.54 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[SLAMF7]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[LINC00536]] | -0.54 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[ANXA10]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[POU2F2]] | -0.53 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[SYNJ2]] | -0.53 | -0.54 / -0.56 | both halves | 1e-05 | pathway: Clathrin-mediated endocytosis |
| [[RPS6KA3]] | -0.52 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02220]] | B | LINC02220 activity strengthens COPS8's drug response | lines that do not express LINC02220 (22) vs lines expressing it (26) | the lines without LINC02220 respond 0.76× as strongly (z diff +0.67); strongest at Panobinostat 0.5 µM: 1.91x vs 2.20x (z diff +1.3) | 0.047 | ⚠ within organs, on part of the lines; also absent: COL16A1, SEMA5A, ANKRD30B; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[RNF175]] | B | RNF175 activity raises COPS8's level | lines that do not express RNF175 (30) vs lines expressing it (20) | 1.32× lower at baseline in the lines without RNF175 | 0.049 | ⚠ within organs, on part of the lines; also absent: SCG2, ENSG00000266450, MIR493HG |
| [[LIX1L]] | B | LIX1L activity raises COPS8's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 1.50× lower at baseline in the lines without LIX1L | 0.060 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[NR3C1]] | B | NR3C1 activity raises COPS8's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.3% of all compounds | 0.099 | ⚠ off-target possible; 3 compounds |
| [[HDAC9]] | B | HDAC9 activity raises COPS8's level | lines that do not express HDAC9 (9) vs lines expressing it (41) | 1.41× lower at baseline in the lines without HDAC9 | 0.099 | ⚠ within organs, on part of the lines; also absent: CCDC88A, ETS1, AFAP1L1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.2, 15.6); signed map (17.1, 30.7). **Vector** length 104, 29.3% of its response variance represented; |z| ≥ 3 in 1,237 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dexamethasone (drug)]] 0.5 µM |  | +6.6 | +5.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +6.1 | +5.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +6.0 | +4.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +5.7 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.4 | +5.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.3 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | +0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.2 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | COP9 signalosome subunit 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:237,085,882-237,100,474 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COP9, CSN8, MGC1297, SGN8 |
| Gene groups (HGNC) | COP9 signalosome |
| Reactome | 11 pathways, smallest: DNA Damage Recognition in GG-NER; Formation of TC-NER Pre-Incision Complex; Transcription-Coupled Nucleotide Excision Repair (TC-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99627](https://www.uniprot.org/uniprotkb/Q99627) (COP9 signalosome complex subunit 8):

> Component of the COP9 signalosome (CSN), a master regulator of the ubiquitin conjugation pathway. CSN mediates the deneddylation of the cullin subunits of all cullin-RING ligases. By reversing the activating neddylation on the cullin-RING ligase, the COP9 signalosome restores the ligase to its inactive state and resets it for substrate recognition. CSN is also involved in phosphorylation of p53/TP53, c-jun/JUN, IkappaBalpha/NFKBIA, ITPK1 and IRF8/ICSBP, possibly via its association with CK2 and …

**Summary**, from NCBI Gene [10920](https://www.ncbi.nlm.nih.gov/gene/10920):

> The protein encoded by this gene is one of the eight subunits of COP9 signalosome, a highly conserved protein complex that functions as an important regulator in multiple signaling pathways. The structure and function of COP9 signalosome is similar to that of the 19S regulatory particle of 26S proteasome. COP9 signalosome has been shown to interact with SCF-type E3 ubiquitin ligases and act as a positive regulator of E3 ubiquitin ligases. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:24335](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24335) · Entrez [10920](https://www.ncbi.nlm.nih.gov/gene/10920) · UniProt [Q99627](https://www.uniprot.org/uniprotkb/Q99627) · Ensembl [ENSG00000198612](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198612)

## Data

Gene col 12628: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12628); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12628, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12628]; `tensor/DDL_lfc|DDL_z.npy` [12628]; `embed/gene_vectors.npy` [12628]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12628 or target_col == 12628). Every well: [[COPS8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPS8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
