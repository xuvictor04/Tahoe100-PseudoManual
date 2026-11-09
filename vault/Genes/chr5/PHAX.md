---
symbol: "PHAX"
type: "gene"
col: 9026
ensembl_id: "ENSG00000164902"
name: "phosphorylated adaptor for RNA export"
location: "5q23.2"
module: 12
arm: "+"
pooled_cpm: 46.16
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PHAX

*phosphorylated adaptor for RNA export* — 5q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +13.9, q 3e-41, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.41× (z +13.3, q 1e-37, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.621× (z -7.2, q 5e-10, down in 37 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.771× (z -3.7, q 0.021, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSMCE3]] (+0.85, fdr 7e-06), [[COIL]] (+0.84, fdr 7e-06), [[C1orf131]] (+0.82, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9026.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.95×** | +13.9 | 3e-41 | 46/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.41×** | +13.3 | 1e-37 | 46/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.27×** | +12.4 | 7e-33 | 47/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.35×** | +12.4 | 7e-33 | 48/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.15×** | +11.5 | 2e-28 | 47/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.52×** | +9.9 | 5e-21 | 46/49 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.25×** | +6.4 | 1e-08 | 36/48 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.53×** | +5.9 | 3e-07 | 38/47 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.4 | 4e-06 | 34/47 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +4.3 | 0.001 | 27/48 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.005 | 21/48 (MIA PaCa-2, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **1.27×** | +3.6 | 0.014 | 24/48 (HS-578T, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.16× | +3.1 | 0.075 | 11/48 (RKO, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9026.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.621×** | -7.2 | 5e-10 | 37/48 (NCI-H2030, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.731×** | -4.5 | 0.002 | 25/42 (A-427, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.807×** | -4.4 | 0.002 | 26/48 (AsPC-1, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.736×** | -4.3 | 0.003 | 26/44 (SK-MEL-2, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -3.7 | 0.021 | 23/48 (HOP62, C-33 A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.796×** | -3.4 | 0.056 | 20/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.790×** | -3.4 | 0.056 | 21/48 (HS-578T, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.801×** | -3.3 | 0.056 | 19/48 (A498, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Irinotecan (drug)]] 0.5 µM |  | **0.735×** | -3.3 | 0.056 | 17/48 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.803×** | -3.3 | 0.056 | 23/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 72.6 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +13.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 50.6 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 39.4 | 3 (1 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.49× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.336× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 43.2 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +18.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.86× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.418× (z -9.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 52.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.58× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 60.8 | 2 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.09× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -12.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 64.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.13× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -13.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 48.6 | 5 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.50× (z +9.9) | — |
| [[A549 (line)]] | wt | 40.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +17.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.13× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 47.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 37.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.36× (z +10.1) | — |
| [[A-172 (line)]] | wt | 54.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +8.9) | — |
| [[A498 (line)]] | wt | 55.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -9.0) ⚠ cell-cycle shift, explains ~15% of this change |
| [[AsPC-1 (line)]] | alt | 38.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -11.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 37.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 5 µM 0.267× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 49.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.71× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 45.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.54× (z +8.6) | — |
| [[LoVo (line)]] | wt | 50.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.51× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 31.2 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.45× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 46.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.31× (z +11.0) | — |
| [[RKO (line)]] | wt | 42.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.9) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 52.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 79.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -11.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 27.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[CHP-212 (line)]] | wt | 50.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -8.5) ⚠ cell-cycle shift, explains ~15% of this change |
| [[H4 (line)]] | wt | 40.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +9.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[J82 (line)]] | alt | 37.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[KATO III (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LS 180 (line)]] | wt | 42.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -9.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 52.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-1 (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 82.9 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0771× (z -11.0) |
| [[SW48 (line)]] | wt | 47.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[C-33 A (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSMCE3]] | +0.85 | +0.80 / +0.83 | both halves | 7e-06 |  |
| [[COIL]] | +0.84 | +0.79 / +0.88 | both halves | 7e-06 | STRING 734 |
| [[C1orf131]] | +0.82 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[PEX12]] | +0.80 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.80 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[SNW1]] | +0.80 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[RP9]] | +0.78 | +0.84 / +0.79 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.78 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.78 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.77 | +0.69 / +0.83 | both halves | 7e-06 |  |
| [[ASNSD1]] | +0.76 | +0.83 / +0.69 | both halves | 7e-06 |  |
| [[PDRG1]] | +0.76 | +0.77 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PHAX's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.861). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-34.9, 3.9); signed map (0.7, -19.8). **Vector** length 132, 40.9% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA Splicing - Major Pathway* (reactome, mean cos +0.53 to 17); *mRNA Splicing* (reactome, mean cos +0.53 to 17); *Processing of Capped Intron-Containing Pre-mRNA* (reactome, mean cos +0.51 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.9 | +13.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +10.3 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +9.4 | +11.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.8 | +12.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +8.8 | +13.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.8 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +1.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.9 | -7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.9 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -7.3 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.1 | -2.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | -3.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -2.1 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -2.0 | -3.3 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphorylated adaptor for RNA export |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.2 — chr5:126,600,925-126,627,252 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13193; previously RNUXA |
| Reactome | 4 pathways, smallest: Metabolism of non-coding RNA; snRNP Assembly; RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H814](https://www.uniprot.org/uniprotkb/Q9H814) (Phosphorylated adapter RNA export protein):

> A phosphoprotein adapter involved in the XPO1-mediated U snRNA export from the nucleus. Bridge components required for U snRNA export, the cap binding complex (CBC)-bound snRNA on the one hand and the GTPase Ran in its active GTP-bound form together with the export receptor XPO1 on the other. Its phosphorylation in the nucleus is required for U snRNA export complex assembly and export, while its dephosphorylation in the cytoplasm causes export complex disassembly. It is recycled back to the …

**Summary**, from NCBI Gene [51808](https://www.ncbi.nlm.nih.gov/gene/51808):

> Enables mRNA cap binding complex binding activity. Involved in RNA stabilization. Located in nucleoplasm. Part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10241](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10241) · Entrez [51808](https://www.ncbi.nlm.nih.gov/gene/51808) · UniProt [Q9H814](https://www.uniprot.org/uniprotkb/Q9H814) · Ensembl [ENSG00000164902](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164902)

## Data

Gene col 9026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9026); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9026]; `tensor/DDL_lfc|DDL_z.npy` [9026]; `embed/gene_vectors.npy` [9026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9026 or target_col == 9026). Every well: [[PHAX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHAX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
