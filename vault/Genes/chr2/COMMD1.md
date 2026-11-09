---
symbol: "COMMD1"
type: "gene"
col: 10348
ensembl_id: "ENSG00000173163"
name: "copper metabolism domain containing 1"
location: "2p15"
module: 114
arm: "+"
pooled_cpm: 86.24
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# COMMD1

*copper metabolism domain containing 1* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.34× (z +8.7, q 2e-15, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.22× (z +5.9, q 1e-06, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.609× (z -10.1, q 5e-21, down in 36 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.838× (z -5.3, q 1e-05, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SHP-77 0.118×, A549 0.222×, NCI-H23 0.379×, SK-MEL-2 0.202×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1792 0.195×, NCI-H23 0.226×, Panc 03.27 0.240×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H1792 0.292×, A-427 0.303×, KATO III 0.319×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.346×, NCI-H1792 0.627×); [[Cytarabine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0791×); [[Gefitinib (drug)]] 5 µM in 1 line (NCI-H460 0.507×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3HC1]] (+0.60, fdr 1e-05), [[YJU2]] (+0.59, fdr 1e-05), [[PEX14]] (+0.58, fdr 1e-04); moves opposite to [[TMEM170B]] (-0.62, fdr 1e-05), [[GUCY1B1]] (-0.52, fdr 5e-05), [[TENT4A]] (-0.52, fdr 1e-05).
> It is in [[Module 114]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10348.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.34×** | +8.7 | 2e-15 | 37/48 (Hs 766T, J82, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +5.9 | 1e-06 | 24/48 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 3e-05 | 24/48 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +4.7 | 4e-04 | 21/48 (NCI-H23, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +4.4 | 0.001 | 22/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.23×** | +4.4 | 0.001 | 24/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.21×** | +4.0 | 0.006 | 21/48 (Panc 03.27, Hs 766T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.4 | 0.042 | 12/48 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.051 | 12/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.061 | 12/49 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.061 | 13/50 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.061 | 12/48 (NCI-H1573, SNU-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.19× | +3.2 | 0.066 | 14/50 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.11× | +3.1 | 0.080 | 2/48 (LOX-IMVI, NCI-H2347) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10348.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SHP-77 0.118×, A549 0.222×, NCI-H23 0.379×, SK-MEL-2 0.202×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1792 0.195×, NCI-H23 0.226×, Panc 03.27 0.240×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H1792 0.292×, A-427 0.303×, KATO III 0.319×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.346×, NCI-H1792 0.627×); [[Cytarabine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0791×); [[Gefitinib (drug)]] 5 µM in 1 line (NCI-H460 0.507×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.609×** | -10.1 | 5e-21 | 36/47 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.637×** | -9.5 | 5e-19 | 33/49 (NCI-H1792, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -8.6 | 1e-15 | 30/44 (SHP-77, A549, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.651×** | -8.4 | 8e-15 | 32/45 (NCI-H1792, A-427, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.728×** | -6.7 | 2e-09 | 35/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -5.3 | 1e-05 | 21/48 (NCI-H1792, NCI-H23, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.674×** | -4.3 | 0.001 | 22/38 (LOX-IMVI, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.817×** | -4.3 | 0.001 | 24/48 (LS 180, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.820×** | -4.2 | 0.002 | 23/49 (C32, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.707×** | -3.8 | 0.007 | 24/48 (SW 900, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.837× | -3.8 | 0.008 | 19/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.837× | -3.7 | 0.008 | 19/47 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.861× | -3.0 | 0.10 | 13/49 (RKO, NCI-H1792, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10348. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 110 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.401× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 81.6 | 1 | 5 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.70× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.399× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Gefitinib (drug)]] 5 µM 0.507× (z -8.8) |
| [[HOP62 (line)]] | alt | 84.9 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.359× (z -10.9) ⚠ toxic |
| [[KATO III (line)]] | alt | 84.6 | 1 (1 ⚠) | 4 (4 ⚠) | [[Selinexor (drug)]] 5 µM 1.68× (z +8.5) ⚠ cell-cycle shift, explains ~47% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -12.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 117 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -11.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 75.4 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 202 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -24.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.627× (z -9.7) |
| [[SW480 (line)]] | alt | 70.5 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.453× (z -10.8) ⚠ cell-cycle shift, explains ~87% of this change |
| [[A-427 (line)]] | wt | 171 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 58.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -10.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 93.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -11.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -17.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 79.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.326× (z -12.3) ⚠ toxic |
| [[HCT15 (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 218 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -23.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 58.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 62.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.3) | — |
| [[A498 (line)]] | wt | 89.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 75.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 81.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.8) |
| [[COLO 205 (line)]] | alt | 65.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 73.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.416× (z -11.0) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 40.2 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.30× (z +9.9) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[J82 (line)]] | alt | 36.8 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.01× (z +9.0) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 91.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.431× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 82.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 71.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.6) | — |
| [[SHP-77 (line)]] | alt | 79.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -22.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 59.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -14.6) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 109 | 0 | 1 | — | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM 0.0791× (z -9.4) |
| [[SW 1271 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.106× (z -10.4) ⚠ transcription drop; cell-cycle shift, explains ~44% of this change |
| [[AN3 CA (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 95.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 56.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10348), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3HC1]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[YJU2]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[PEX14]] | +0.58 | +0.36 / +0.60 | both halves | 1e-04 |  |
| [[DOHH]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CES2]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[MRPL27]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[TEFM]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[ALKBH1]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[FDX2]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[FRS2]] | +0.53 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[NKAPD1]] | +0.53 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[ZCCHC10]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM170B]] | -0.62 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[GUCY1B1]] | -0.52 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[TENT4A]] | -0.52 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SLC6A6]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[DPYSL2]] | -0.51 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[CDCA7L]] | -0.51 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[LBR]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SUN1]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SEPTIN3]] | -0.49 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[NFE2L3]] | -0.48 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[TPD52]] | -0.48 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ATP1A3]] | -0.48 | -0.25 / -0.41 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.7, 7.6); signed map (-6.3, -16.6). **Vector** length 110, 29.4% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.3 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.3 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +5.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +4.0 | +4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +0.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.2 | -5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.3 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.6 | -10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.5 | -4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | -8.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.7 | -0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.4 | -1.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.3 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | copper metabolism domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:61,888,724-62,147,247 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MURR1, MGC27155; previously C2orf5 |
| Gene groups (HGNC) | COMM domain containing; CCC complex |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N668](https://www.uniprot.org/uniprotkb/Q8N668) (COMM domain-containing protein 1):

> Scaffold protein in the commander complex that is essential for endosomal recycling of transmembrane cargos; the commander complex is composed of the CCC subcomplex and the retriever subcomplex. Can modulate activity of cullin-RING E3 ubiquitin ligase (CRL) complexes by displacing CAND1; in vitro promotes CRL E3 activity and dissociates CAND1 from CUL1 and CUL2. Promotes ubiquitination of NF-kappa-B subunit RELA and its subsequent proteasomal degradation. Down-regulates NF-kappa-B activity. …

**Summary**, from NCBI Gene [150684](https://www.ncbi.nlm.nih.gov/gene/150684):

> Enables several functions, including phosphatidylinositol-3,4-bisphosphate binding activity; phospholipid binding activity; and protein homodimerization activity. Involved in several processes, including Golgi to plasma membrane transport; negative regulation of protein localization to cell surface; and regulation of protein metabolic process. Acts upstream of or within negative regulation of transcription by RNA polymerase II. Located in cytosol; endosome; and nucleoplasm. Part of Cul2-RING …

**Accessions** — [HGNC:23024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23024) · Entrez [150684](https://www.ncbi.nlm.nih.gov/gene/150684) · UniProt [Q8N668](https://www.uniprot.org/uniprotkb/Q8N668) · Ensembl [ENSG00000173163](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173163)

## Data

Gene col 10348: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10348); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10348, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10348]; `tensor/DDL_lfc|DDL_z.npy` [10348]; `embed/gene_vectors.npy` [10348]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10348 or target_col == 10348). Every well: [[COMMD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COMMD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
