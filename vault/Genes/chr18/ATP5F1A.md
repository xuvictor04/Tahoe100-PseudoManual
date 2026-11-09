---
symbol: "ATP5F1A"
type: "gene"
col: 7606
ensembl_id: "ENSG00000152234"
name: "ATP synthase F1 subunit alpha"
location: "18q21.1"
module: 29
arm: "+"
pooled_cpm: 83.33
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ATP5F1A

*ATP synthase F1 subunit alpha* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.78× (z +18.9, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.19× (z +3.6, q 0.018, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A549 7.98×, NCI-H460 6.36×, SW480 4.67×, PANC-1 4.77×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (MIA PaCa-2 7.37×, NCI-H460 5.76×, NCI-H1792 7.41×, J82 4.85×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.303×, AN3 CA 0.245×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5F1B]] (+0.72, fdr 7e-06), [[DLD]] (+0.70, fdr 7e-06), [[PRKDC]] (+0.69, fdr 7e-06); moves opposite to [[SPATC1]] (-0.65, fdr 1e-05), [[ZBTB43]] (-0.64, fdr 7e-06), [[MSX1]] (-0.61, fdr 1e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLS3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7606.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A549 7.98×, NCI-H460 6.36×, SW480 4.67×, PANC-1 4.77×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (MIA PaCa-2 7.37×, NCI-H460 5.76×, NCI-H1792 7.41×, J82 4.85×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.78×** | +18.9 | 0e+00 | 48/49 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.17×** | +15.7 | 0e+00 | 43/44 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.50×** | +10.8 | 6e-25 | 44/45 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **1.43×** | +5.1 | 6e-05 | 34/47 (SW480, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **1.43×** | +4.9 | 1e-04 | 30/47 (LoVo, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.38×** | +4.6 | 3e-04 | 35/48 (AsPC-1, RKO, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.38×** | +4.5 | 6e-04 | 27/50 (MIA PaCa-2, A-427, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.35×** | +4.3 | 0.001 | 34/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.34×** | +4.1 | 0.002 | 31/48 (RKO, AsPC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.018 | 22/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 1.18× | +3.4 | 0.031 | 15/48 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +3.3 | 0.039 | 22/48 (LoVo, LS 180, …) | top dose only | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.26×** | +3.3 | 0.039 | 24/48 (NCI-H1792, A549, …) | two highest doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.039 | 21/48 (A-172, HS-578T, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.072 | 21/48 (Hs 766T, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7606.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.303×, AN3 CA 0.245×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.914× | -4.1 | 0.026 | 2/50 (SW 1271, NCI-H2122) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.658× | -3.1 | 0.44 | 25/49 (LoVo, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rifaximin (drug)]] 5 µM |  | 0.797× | -3.0 | 0.44 | 24/48 (hTERT-HPNE, A-172, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7606. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 91.3 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.37× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 42.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A549 (line)]] | wt | 61.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.98× (z +17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[CFPAC-1 (line)]] | alt | 61.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 75.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 54.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 71.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.36× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 78.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 142 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 76.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.49× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[PANC-1 (line)]] | alt | 69.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.77× (z +16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 60.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 109 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -18.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 58.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AsPC-1 (line)]] | alt | 43.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.31× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C32 (line)]] | wt | 62.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HCT15 (line)]] | alt | 126 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HepG2_C3A (line)]] | wt | 77.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HOP62 (line)]] | alt | 35.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 85.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 119 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 81.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2347 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 67.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Panc 03.27 (line)]] | alt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 66.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 41.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.05× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 135 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C-33 A (line)]] | alt | 199 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[COLO 205 (line)]] | alt | 39.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 69.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 82.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 142 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 66.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SHP-77 (line)]] | alt | 166 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW 900 (line)]] | alt | 36.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW1417 (line)]] | alt | 63.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW48 (line)]] | wt | 172 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[CHP-212 (line)]] | wt | 99.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 103 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7606), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1B]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[DLD]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 917 |
| [[PRKDC]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[AIFM1]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 605 |
| [[NONO]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TMX1]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[DHX9]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[COPS6]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[FAM98B]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[COX11]] | +0.64 | +0.67 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[MRPL19]] | +0.64 | +0.58 / +0.67 | both halves | 8e-06 | STRING 508 |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATC1]] | -0.65 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[ZBTB43]] | -0.64 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[MSX1]] | -0.61 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[MAFG]] | -0.60 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[TMEM106A]] | -0.60 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[C19orf25]] | -0.60 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.59 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[PCF11-AS1]] | -0.59 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[LINC00685]] | -0.59 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[PP2D1]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[EIF3J-DT]] | -0.58 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[VPS39-DT]] | -0.58 | -0.55 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLS3]] | C | PLS3 activity lowers ATP5F1A's level | lines that do not express PLS3 (4) vs lines expressing it (46) | 1.94× higher at baseline in the lines without PLS3 | 0.049 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.0, -17.8); signed map (-18.6, -43.8). **Vector** length 85.5, 25.0% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.1 | -0.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.0 | +0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.0 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -1.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.3 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase F1 subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:46,080,248-46,104,334 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATP5A, hATP1, OMR, ORM; previously ATP5AL2, ATPM, ATP5A1 |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits; ATPase F1/V1 alpha/A and beta/B subunit family |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 8 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [P25705](https://www.uniprot.org/uniprotkb/P25705) (ATP synthase F(1) complex subunit alpha, mitochondrial):

> Subunit alpha, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain (Probable). ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) region and …

**Summary**, from NCBI Gene [498](https://www.ncbi.nlm.nih.gov/gene/498):

> This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic portion of mitochondrial ATP synthase consists of 5 different subunits (alpha, beta, gamma, delta, …

**Accessions** — [HGNC:823](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:823) · Entrez [498](https://www.ncbi.nlm.nih.gov/gene/498) · UniProt [P25705](https://www.uniprot.org/uniprotkb/P25705) · Ensembl [ENSG00000152234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152234)

## Data

Gene col 7606: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7606); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7606, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7606]; `tensor/DDL_lfc|DDL_z.npy` [7606]; `embed/gene_vectors.npy` [7606]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7606 or target_col == 7606). Every well: [[ATP5F1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5F1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
