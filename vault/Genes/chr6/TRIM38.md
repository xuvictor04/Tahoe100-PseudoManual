---
symbol: "TRIM38"
type: "gene"
col: 3361
ensembl_id: "ENSG00000112343"
name: "tripartite motif containing 38"
location: "6p22.2"
module: 32
arm: "+"
pooled_cpm: 73.71
n_lines_expressing: 44
n_dd_up: 4
n_dd_down: 38
n_dd_up_clean: 3
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 30
direction_downstream: 26
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# TRIM38

*tripartite motif containing 38* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.41× (z +6.2, q 3e-07, up in 32 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.559× (z -14.8, q 0e+00, down in 35 of 42 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.675× (z -7.1, q 1e-10, down in 28 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASP10]] (+0.71, fdr 7e-06), [[BATF2]] (+0.70, fdr 7e-06), [[OAS1]] (+0.70, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[IFI16]] → it (grade B ⚠); 26 go from it, the strongest it → [[GBP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3361.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +6.2 | 3e-07 | 32/42 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.28×** | +4.5 | 0.002 | 23/43 (HT-29, LS 180, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.005 | 21/41 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.20×** | +3.4 | 0.083 | 15/42 (COLO 205, NCI-H2347, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.14× | +3.4 | 0.083 | 14/42 (NCI-H2347, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.14× | +3.3 | 0.083 | 17/42 (LS 180, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.14 | 4/43 (H4, PANC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +3.1 | 0.14 | 13/42 (KATO III, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3361.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.559×** | -14.8 | 0e+00 | 35/42 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.533×** | -11.4 | 2e-27 | 36/43 (RKO, SW 1271, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.542×** | -10.6 | 4e-24 | 31/41 (SNU-423, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.535×** | -10.4 | 2e-23 | 29/38 (NCI-H460, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.375×** | -9.3 | 2e-18 | 25/33 (HS-578T, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.600×** | -8.9 | 8e-17 | 25/37 (NCI-H1573, SNU-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.675×** | -7.1 | 1e-10 | 28/42 (COLO 205, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.765×** | -6.8 | 6e-10 | 23/43 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.688×** | -6.7 | 1e-09 | 25/42 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.771×** | -6.6 | 2e-09 | 25/43 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.698×** | -6.5 | 5e-09 | 28/42 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.703×** | -6.4 | 1e-08 | 25/42 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.785×** | -6.2 | 3e-08 | 25/43 (CFPAC-1, A549, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.715×** | -6.0 | 6e-08 | 29/42 (COLO 205, H4, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.529×** | -6.0 | 7e-08 | 27/43 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.704×** | -6.0 | 8e-08 | 26/42 (COLO 205, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.718×** | -6.0 | 8e-08 | 27/42 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.734×** | -5.6 | 8e-07 | 26/42 (COLO 205, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.583×** | -5.1 | 1e-05 | 25/42 (RKO, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.821×** | -5.0 | 2e-05 | 22/43 (BT-474, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.771×** | -4.7 | 7e-05 | 25/42 (SW 900, NCI-H1573, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.774×** | -4.6 | 9e-05 | 24/43 (A549, SNU-423, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.786×** | -4.3 | 3e-04 | 25/43 (A549, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3361. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 154 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -22.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.131× (z -18.2) |
| [[RKO (line)]] | wt | 131 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -22.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.251× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 48.7 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -18.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.316× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 89.0 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -22.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -8.9) |
| [[SNU-423 (line)]] | alt | 141 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -20.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 69.4 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -19.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 125 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.450× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 91.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -15.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 109 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -23.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.367× (z -10.8) |
| [[PANC-1 (line)]] | alt | 49.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -25.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.248× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 79.2 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.70× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -13.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 77.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.397× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.408× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 120 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -8.6) |
| [[H4 (line)]] | wt | 131 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 121 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -11.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 90.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -11.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 65.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -14.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.266× (z -9.0) |
| [[Hs 766T (line)]] | wt | 121 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HS-578T (line)]] | alt | 75.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -13.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HT-29 (line)]] | alt | 75.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -10.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 68.1 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0774× (z -11.8) ⚠ toxic · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.348× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 80.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.332× (z -9.6) |
| [[SNU-1 (line)]] | wt | 95.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -15.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 87.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -17.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[BT-474 (line)]] | alt | 32.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -9.2) |
| [[C32 (line)]] | wt | 95.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -10.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 52.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -10.5) |
| [[LS 180 (line)]] | wt | 65.8 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.00× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 53.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -13.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 76.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.393× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -11.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 42.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.421× (z -9.7) |
| [[A-427 (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.38 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.78 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.49 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.72 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3361), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASP10]] | +0.71 | +0.63 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[BATF2]] | +0.70 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[OAS1]] | +0.70 | +0.62 / +0.73 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[GBP3]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[IFI16]] | +0.69 | +0.56 / +0.74 | both halves | 1e-05 | STRING 412 |
| [[TRANK1]] | +0.69 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[SP110]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 | STRING 477 |
| [[IFI35]] | +0.68 | +0.58 / +0.72 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[TRIM22]] | +0.67 | +0.58 / +0.70 | both halves | 7e-06 | same gene group; pathway: Interferon Signaling |
| [[TRIM5]] | +0.67 | +0.56 / +0.70 | both halves | 1e-05 | same gene group; pathway: Interferon Signaling |
| [[FBXO39]] | +0.66 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[APOL6]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 25, C 5. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI16]] | B | IFI16 activity raises TRIM38's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.59× lower at baseline in the lines without IFI16 | 0.001 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[IFITM2]] | B | IFITM2 activity raises TRIM38's level | lines that do not express IFITM2 (14) vs lines expressing it (36) | 2.55× lower at baseline in the lines without IFITM2 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with SMARCA4; also absent: CASP10, MX2, MAFB |
| [[NLRC5]] | B | NLRC5 activity raises TRIM38's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 4.22× lower at baseline in the lines without NLRC5 | 0.008 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises TRIM38's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.21× lower at baseline in the lines without RSAD2 | 0.009 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[CD274]] | B | CD274 activity raises TRIM38's level | lines that do not express CD274 (18) vs lines expressing it (32) | 2.38× lower at baseline in the lines without CD274 | 0.009 | ⚠ within organs, on part of the lines; also absent: GBP5, IL1B, PDCD1LG2 |
| [[CTSS]] | B | CTSS activity raises TRIM38's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.00× lower at baseline in the lines without CTSS | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[CASP10]] | B | CASP10 activity raises TRIM38's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.34× lower at baseline in the lines without CASP10 | 0.013 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[CD5L]] | B | CD5L activity raises TRIM38's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.20× lower at baseline in the lines without CD5L | 0.015 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[RNASEL]] | B | RNASEL activity raises TRIM38's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 4.34× lower at baseline in the lines without RNASEL | 0.021 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent |
| [[TRANK1]] | B | TRANK1 activity raises TRIM38's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 2.62× lower at baseline in the lines without TRANK1 | 0.024 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SAMD9L]] | B | SAMD9L activity raises TRIM38's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.23× lower at baseline in the lines without SAMD9L | 0.025 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[OASL]] | B | OASL activity raises TRIM38's level | lines that do not express OASL (10) vs lines expressing it (40) | 1.74× lower at baseline in the lines without OASL | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 21, C 5. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP3]] | B | TRIM38 activity raises GBP3's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 5.13× lower at baseline in the lines without TRIM38 | 0.014 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[CASP8]] | B | TRIM38 activity raises CASP8's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 2.59× lower at baseline in the lines without TRIM38 | 0.014 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[CASP10]] | B | TRIM38 activity raises CASP10's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 5.03× lower at baseline in the lines without TRIM38 | 0.023 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[IFI44]] | B | TRIM38 activity raises IFI44's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 4.02× lower at baseline in the lines without TRIM38 | 0.032 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[GBP1]] | B | TRIM38 activity raises GBP1's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 5.67× lower at baseline in the lines without TRIM38 | 0.035 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[SLFN5]] | B | TRIM38 activity raises SLFN5's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 3.64× lower at baseline in the lines without TRIM38 | 0.044 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[SAMD9]] | B | TRIM38 activity raises SAMD9's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 4.64× lower at baseline in the lines without TRIM38 | 0.045 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[TRANK1]] | B | TRIM38 activity raises TRANK1's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 2.76× lower at baseline in the lines without TRIM38 | 0.048 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[CFB]] | B | TRIM38 activity raises CFB's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 5.57× lower at baseline in the lines without TRIM38 | 0.054 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[TNFSF10]] | B | TRIM38 activity raises TNFSF10's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 4.10× lower at baseline in the lines without TRIM38 | 0.058 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[GBP4]] | B | TRIM38 activity raises GBP4's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 4.50× lower at baseline in the lines without TRIM38 | 0.061 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[B2M]] | B | TRIM38 activity raises B2M's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 2.53× lower at baseline in the lines without TRIM38 | 0.061 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.708). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.3, 54.6); signed map (62.4, 31.3). **Vector** length 123, 39.9% of its response variance represented; |z| ≥ 3 in 1,415 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.59 to 56); *interferon gamma response* (hallmark, mean cos +0.60 to 60); *interferon* (control, mean cos +0.63 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.6 | +6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | +3.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +4.2 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -7.4 | -6.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -6.3 | -6.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -6.1 | -6.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.1 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.8 | -14.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.3 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:25,962,802-25,991,231 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RORET; previously RNF15 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [O00635](https://www.uniprot.org/uniprotkb/O00635) (E3 ubiquitin-protein ligase TRIM38):

> E3 ubiquitin-protein and E3 SUMO-protein ligase that acts as a regulator of innate immunity. Acts as a negative regulator of type I interferon IFN-beta production by catalyzing 'Lys-48'-linked polyubiquitination of AZI2/NAP1, leading to its degradation (By similarity). Mediates 'Lys-48'-linked polyubiquitination and proteasomal degradation of the critical TLR adapter TICAM1, inhibiting TLR3-mediated type I interferon signaling. Acts as positive regulator of the cGAS-STING pathway by acting as a …

**Summary**, from NCBI Gene [10475](https://www.ncbi.nlm.nih.gov/gene/10475):

> This gene encodes a member of the tripartite motif (TRIM) family. The encoded protein contains a RING-type zinc finger, B box-type zinc finger and SPRY domain. The function of this protein has not been identified. A pseudogene of this gene is located on the long arm of chromosome 4. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:10059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10059) · Entrez [10475](https://www.ncbi.nlm.nih.gov/gene/10475) · UniProt [O00635](https://www.uniprot.org/uniprotkb/O00635) · Ensembl [ENSG00000112343](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112343)

## Data

Gene col 3361: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3361); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3361, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3361]; `tensor/DDL_lfc|DDL_z.npy` [3361]; `embed/gene_vectors.npy` [3361]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3361 or target_col == 3361). Every well: [[TRIM38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
