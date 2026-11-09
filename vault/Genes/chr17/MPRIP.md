---
symbol: "MPRIP"
type: "gene"
col: 5406
ensembl_id: "ENSG00000133030"
name: "myosin phosphatase Rho interacting protein"
location: "17p11.2"
module: 34
arm: "+"
pooled_cpm: 213.04
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# MPRIP

*myosin phosphatase Rho interacting protein* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.60× (z +9.4, q 3e-18, up in 31 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.41× (z +3.8, q 0.010, up in 24 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (MIA PaCa-2 2.61×, PANC-1 2.18×, HS-578T 2.40×, NCI-H1792 3.67×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (MIA PaCa-2 2.01×, HS-578T 1.79×, HepG2/C3A 2.08×); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HS-578T 2.30×, MIA PaCa-2 2.24×, SNU-423 2.53×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.694× (z -10.8, q 2e-24, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC42BPB]] (+0.70, fdr 7e-06), [[MICAL2]] (+0.67, fdr 7e-06), [[ACTN4]] (+0.67, fdr 7e-06); moves opposite to [[ZNF766]] (-0.59, fdr 1e-05), [[ZNF563]] (-0.58, fdr 1e-05), [[DNAJC27]] (-0.57, fdr 2e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[F3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5406.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (MIA PaCa-2 2.61×, PANC-1 2.18×, HS-578T 2.40×, NCI-H1792 3.67×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (MIA PaCa-2 2.01×, HS-578T 1.79×, HepG2/C3A 2.08×); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HS-578T 2.30×, MIA PaCa-2 2.24×, SNU-423 2.53×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.60×** | +9.4 | 3e-18 | 31/44 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.60×** | +7.4 | 5e-11 | 28/49 (HS-578T, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.46×** | +7.3 | 5e-11 | 35/45 (HS-578T, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.23×** | +4.4 | 0.001 | 24/48 (HCT15, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.21×** | +4.0 | 0.006 | 21/48 (A-172, A549, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.22×** | +4.0 | 0.006 | 23/47 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.20×** | +3.8 | 0.010 | 21/48 (SNU-423, HCT15, …) | all doses, flat | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.010 | 24/49 (MIA PaCa-2, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.017 | 23/48 (NCI-H1573, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.16× | +3.2 | 0.079 | 19/48 (SNU-423, A-172, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 1.16× | +3.0 | 0.11 | 23/48 (HCT15, SHP-77, …) | all doses, flat | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | 1.32× | +3.0 | 0.11 | 19/49 (NCI-H460, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5406.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.694×** | -10.8 | 2e-24 | 31/48 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.603×** | -10.6 | 1e-23 | 34/48 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.726×** | -9.4 | 6e-19 | 37/48 (NCI-H1573, SW48, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.730×** | -6.3 | 4e-08 | 29/47 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.767×** | -5.5 | 3e-06 | 30/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.770×** | -5.2 | 1e-05 | 29/48 (AsPC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.759×** | -4.3 | 0.001 | 26/48 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.838× | -4.2 | 0.002 | 19/48 (AsPC-1, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -4.2 | 0.002 | 22/49 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.833×** | -3.8 | 0.007 | 21/48 (SW1417, NCI-H2030, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.827×** | -3.8 | 0.007 | 24/47 (AsPC-1, CFPAC-1, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.851× | -3.8 | 0.007 | 20/48 (AsPC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.841× | -3.7 | 0.008 | 24/50 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.882× | -3.6 | 0.015 | 18/49 (AsPC-1, LS 180, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.861× | -3.5 | 0.016 | 20/49 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.737×** | -3.3 | 0.030 | 21/47 (LoVo, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 0.894× | -3.3 | 0.033 | 7/48 (A498, HS-578T, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.765×** | -2.9 | 0.099 | 18/48 (J82, LoVo, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5406. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 609 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -25.0) |
| [[HS-578T (line)]] | alt | 138 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.0) | [[Selinexor (drug)]] 5 µM 0.598× (z -9.6) |
| [[LoVo (line)]] | wt | 574 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -17.3) |
| [[LOX-IMVI (line)]] | wt | 214 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.11× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -21.3) |
| [[A-427 (line)]] | wt | 99.1 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 1.91× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -19.1) |
| [[Hs 766T (line)]] | wt | 334 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -15.4) |
| [[MIA PaCa-2 (line)]] | alt | 90.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.7) | — |
| [[CFPAC-1 (line)]] | alt | 155 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -13.5) |
| [[HOP62 (line)]] | alt | 431 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.419× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 176 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 113 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 278 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -13.3) |
| [[SW1417 (line)]] | alt | 227 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -13.2) |
| [[A549 (line)]] | wt | 194 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Selinexor (drug)]] 5 µM 0.545× (z -8.9) |
| [[HCT15 (line)]] | alt | 218 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.17× (z +9.3) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[KATO III (line)]] | alt | 335 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.434× (z -12.7) |
| [[LS 180 (line)]] | wt | 365 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 96.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 155 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -16.8) |
| [[NCI-H2347 (line)]] | alt | 158 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.26× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -9.3) |
| [[PANC-1 (line)]] | alt | 90.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.18× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.514× (z -10.4) |
| [[SNU-423 (line)]] | alt | 83.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW48 (line)]] | wt | 474 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.436× (z -10.1) |
| [[C32 (line)]] | wt | 130 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 205 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 366 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 76.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.3) | — |
| [[J82 (line)]] | alt | 202 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -9.4) |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.194× (z -9.4) |
| [[RKO (line)]] | wt | 127 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 61.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -11.6) |
| [[SNU-1 (line)]] | wt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 310 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 174 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 146 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 174 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 201 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 194 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 196 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5406), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42BPB]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 | STRING 532 |
| [[MICAL2]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[ACTN4]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ITGA6]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[DIAPH1]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ANO1]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ATG16L1]] | +0.64 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[ACOT7]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SCEL]] | +0.63 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[NCOR2]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[ASAP2]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[NIBAN2]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF766]] | -0.59 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[ZNF563]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[DNAJC27]] | -0.57 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[ZNF226]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[YJU2B]] | -0.57 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[PIGP]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[COIL]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[GTF2IRD2B]] | -0.56 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[SETDB1]] | -0.55 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[THAP6]] | -0.55 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[C11orf52]] | -0.54 | -0.35 / -0.67 | both halves | 1e-04 |  |
| [[YBEY]] | -0.54 | -0.42 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity raises MPRIP's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.66× lower at baseline in the lines without F3 | 0.012 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[TINAGL1]] | B | TINAGL1 activity raises MPRIP's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.59× lower at baseline in the lines without TINAGL1 | 0.028 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[P2RY2]] | B | P2RY2 activity raises MPRIP's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 1.57× lower at baseline in the lines without P2RY2 | 0.041 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[SCEL]] | B | SCEL activity raises MPRIP's level | lines that do not express SCEL (35) vs lines expressing it (15) | 1.77× lower at baseline in the lines without SCEL | 0.046 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[SCEL]] | B | SCEL activity weakens MPRIP's drug response | lines that do not express SCEL (35) vs lines expressing it (14) | the lines without SCEL respond 1.05× as strongly (z diff -0.27); strongest at Dinaciclib 5 µM: 1.81x vs 1.07x (z diff -5.3) | 0.067 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1; target measured in part of the lines; both ways; artifact flags |
| [[P2RY2]] | B | P2RY2 activity weakens MPRIP's drug response | lines that do not express P2RY2 (27) vs lines expressing it (22) | the lines without P2RY2 respond 1.09× as strongly (z diff -0.47); strongest at Dinaciclib 5 µM: 1.86x vs 1.24x (z diff -3.9) | 0.068 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223; target measured in part of the lines; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers MPRIP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KRT6A]] | B | KRT6A activity weakens MPRIP's drug response | lines that do not express KRT6A (41) vs lines expressing it (8) | the lines without KRT6A respond 1.04× as strongly (z diff -0.16); strongest at Belinostat 5 µM: 1.23x vs 0.73x (z diff -5.9) | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588; target measured in part of the lines; both ways; artifact flags |
| [[KRT6A]] | B | KRT6A activity raises MPRIP's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 1.83× lower at baseline in the lines without KRT6A | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[TGFA]] | B | TGFA activity weakens MPRIP's drug response | lines that do not express TGFA (17) vs lines expressing it (32) | the lines without TGFA respond 1.13× as strongly (z diff -0.33); strongest at Dinaciclib 5 µM: 1.90x vs 1.38x (z diff -4.1) | 0.090 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1; target measured in part of the lines; both ways; artifact flags |
| [[SERPINB5]] | B | SERPINB5 activity raises MPRIP's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 1.64× lower at baseline in the lines without SERPINB5 | 0.099 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.4, 6.9); signed map (-10.6, 37.4). **Vector** length 154, 51.3% of its response variance represented; |z| ≥ 3 in 1,373 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +8.1 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +8.1 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +6.8 | +7.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.6 | +3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +5.6 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.1 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.7 | -10.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -7.2 | -5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -10.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.1 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.6 | -3.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.6 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.5 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | myosin phosphatase Rho interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:17,042,457-17,217,679 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RHOIP3, M-RIP, p116Rip |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Reactome | 3 pathways, smallest: Signaling by BRAF and RAF1 fusions; Oncogenic MAPK signaling; Diseases of signal transduction by growth factor receptors and second messengers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6WCQ1](https://www.uniprot.org/uniprotkb/Q6WCQ1) (Myosin phosphatase Rho-interacting protein):

> Targets myosin phosphatase to the actin cytoskeleton. Required for the regulation of the actin cytoskeleton by RhoA and ROCK1. Depletion leads to an increased number of stress fibers in smooth muscle cells through stabilization of actin fibers by phosphorylated myosin. Overexpression of MRIP as well as its F-actin-binding region leads to disassembly of stress fibers in neuronal cells.

**Summary**, from NCBI Gene [23164](https://www.ncbi.nlm.nih.gov/gene/23164):

> Enables identical protein binding activity. Located in actin cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30321) · Entrez [23164](https://www.ncbi.nlm.nih.gov/gene/23164) · UniProt [Q6WCQ1](https://www.uniprot.org/uniprotkb/Q6WCQ1) · Ensembl [ENSG00000133030](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133030)

## Data

Gene col 5406: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5406); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5406, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5406]; `tensor/DDL_lfc|DDL_z.npy` [5406]; `embed/gene_vectors.npy` [5406]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5406 or target_col == 5406). Every well: [[MPRIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPRIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
