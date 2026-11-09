---
symbol: "POLA1"
type: "gene"
col: 2182
ensembl_id: "ENSG00000101868"
name: "DNA polymerase alpha 1, catalytic subunit"
location: "Xp22.11-p21.3"
module: 6
arm: "+"
pooled_cpm: 120.56
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# POLA1

*DNA polymerase alpha 1, catalytic subunit* — Xp22.11-p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.72× (z +15.3, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.75× (z +4.5, q 4e-04, up in 32 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.734× (z -6.7, q 1e-08, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Entrectinib (drug)]] 5 µM: 0.733× (z -4.8, q 5e-04, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM3]] (+0.87, fdr 7e-06), [[FANCA]] (+0.86, fdr 7e-06), [[CDC45]] (+0.84, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2182.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.72×** | +15.3 | 0e+00 | 48/48 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **2.19×** | +12.0 | 1e-30 | 48/48 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **2.06×** | +11.0 | 8e-26 | 47/48 (NCI-H1573, A549, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.49×** | +5.8 | 1e-06 | 32/47 (NCI-H1573, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.39×** | +5.0 | 5e-05 | 31/48 (C32, SNU-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.39×** | +5.0 | 5e-05 | 29/48 (HOP62, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.39×** | +5.0 | 5e-05 | 31/48 (SK-MEL-2, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.37×** | +4.8 | 1e-04 | 27/48 (HOP62, C32, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.5 | 4e-04 | 31/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +4.5 | 4e-04 | 32/49 (LOX-IMVI, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +4.3 | 8e-04 | 27/48 (HS-578T, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.32×** | +4.2 | 0.001 | 30/47 (SNU-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.30×** | +3.8 | 0.006 | 27/48 (A-427, SW480, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.19× | +3.7 | 0.010 | 18/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.011 | 26/48 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.56×** | +3.5 | 0.013 | 24/49 (SW48, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.022 | 20/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.088 | 15/47 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +2.9 | 0.094 | 17/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2182.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.734×** | -6.7 | 1e-08 | 31/48 (A498, LoVo, …) | rises with dose | composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **0.733×** | -4.8 | 5e-04 | 30/48 (RKO, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.752×** | -4.4 | 0.002 | 28/48 (MIA PaCa-2, AN3 CA, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -4.1 | 0.005 | 27/48 (KATO III, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.757×** | -4.1 | 0.005 | 27/47 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.833×** | -4.0 | 0.006 | 24/49 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.833×** | -4.0 | 0.006 | 28/48 (KATO III, COLO 205, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.8 | 0.009 | 22/48 (A-427, C32, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.802×** | -3.3 | 0.047 | 22/49 (A-427, HOP62, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.817×** | -3.3 | 0.047 | 20/48 (A-427, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.806×** | -3.3 | 0.047 | 24/48 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[palbociclib (drug)]] 0.05 µM |  | **0.804×** | -3.2 | 0.070 | 19/48 (A498, SW480, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.675×** | -3.2 | 0.070 | 20/48 (A-427, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.815×** | -3.1 | 0.078 | 19/48 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.812×** | -3.1 | 0.078 | 21/48 (PANC-1, SK-MEL-2, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.84 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 92.8 | 2 (2 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.52× (z +12.0) ⚠ cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -9.7) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 55.0 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.48× (z +15.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A-427 (line)]] | wt | 206 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.423× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.422× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 108 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.08× (z +14.0) ⚠ cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -9.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H460 (line)]] | wt | 131 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.60× (z +13.3) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A498 (line)]] | wt | 70.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.78× (z +9.7) ⚠ cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.9) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -8.9) |
| [[A549 (line)]] | wt | 96.6 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.91× (z +16.2) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[AsPC-1 (line)]] | alt | 43.6 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.01× (z +11.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[C32 (line)]] | wt | 71.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.20× (z +12.0) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[H4 (line)]] | wt | 80.2 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.68× (z +10.8) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[LOX-IMVI (line)]] | wt | 47.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.98× (z +12.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 104 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.05× (z +12.7) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[HepG2_C3A (line)]] | wt | 53.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.45× (z +9.1) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[HS-578T (line)]] | alt | 58.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.39× (z +11.7) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 40.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.06× (z +9.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 231 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.74× (z +9.6) ⚠ cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -11.3) ⚠ cell-cycle shift, explains ~64% of this change |
| [[NCI-H23 (line)]] | alt | 157 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 172 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +8.6) ⚠ cell-cycle shift, explains ~50% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 95.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.16× (z +10.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SW 900 (line)]] | alt | 54.4 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +10.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A-172 (line)]] | wt | 99.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.14× (z +9.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[CFPAC-1 (line)]] | alt | 61.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +9.0) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[HEC-1-A (line)]] | alt | 174 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -9.8) |
| [[HOP62 (line)]] | alt | 64.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.3) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[Hs 766T (line)]] | wt | 102 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.88× (z +10.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[J82 (line)]] | alt | 261 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.7) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H2030 (line)]] | alt | 84.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +8.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H2347 (line)]] | alt | 47.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.84× (z +9.8) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.170× (z -8.9) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 89.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +10.1) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SNU-423 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +10.7) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SW480 (line)]] | alt | 284 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.35× (z +9.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[AN3 CA (line)]] | alt | 153 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 202 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 161 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM3]] | +0.87 | +0.86 / +0.86 | both halves | 7e-06 | pathway: Activation of the pre-replicative complex; STRING 988 |
| [[FANCA]] | +0.86 | +0.86 / +0.83 | both halves | 7e-06 |  |
| [[CDC45]] | +0.84 | +0.85 / +0.81 | both halves | 7e-06 | pathway: Activation of the pre-replicative complex; STRING 964 |
| [[DDX11]] | +0.82 | +0.79 / +0.82 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.82 | +0.82 / +0.80 | both halves | 7e-06 |  |
| [[MCM8]] | +0.81 | +0.84 / +0.82 | both halves | 7e-06 | pathway: Activation of the pre-replicative complex; STRING 824 |
| [[CENPK]] | +0.81 | +0.78 / +0.79 | both halves | 7e-06 | pathway: Chromosome Maintenance |
| [[RANBP1]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[WDR76]] | +0.80 | +0.78 / +0.78 | both halves | 7e-06 | STRING 480 |
| [[EXO1]] | +0.80 | +0.80 / +0.76 | both halves | 7e-06 | STRING 846 |
| [[DDX12P]] | +0.80 | +0.74 / +0.79 | both halves | 7e-06 |  |
| [[FANCI]] | +0.80 | +0.78 / +0.78 | both halves | 7e-06 | STRING 552 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises POLA1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.80× lower at baseline in the lines without E2F2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises POLA1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.19× lower at baseline in the lines without DSCC1 | 0.052 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises POLA1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.26× lower at baseline in the lines without MYBL2 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.852). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.3, -43.6); signed map (-36.1, -44.0). **Vector** length 154, 56.1% of its response variance represented; |z| ≥ 3 in 1,270 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.63 to 65); *Cell Cycle Checkpoints* (reactome, mean cos +0.67 to 45); *Activation of ATR in response to replication stress* (reactome, mean cos +0.71 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +6.6 | +15.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | +5.7 | +5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +5.4 | +12.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.2 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.1 | -0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +2.3 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +3.0 | +2.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.9 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.8 | +2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.6 | +3.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -11.5 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -9.8 | -4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.6 | -3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -6.0 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.7 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.1 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.0 | -3.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | -4.0 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase alpha 1, catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.11-p21.3 — chrX:24,693,873-24,996,986 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p180; previously POLA, NSX |
| Gene groups (HGNC) | DNA polymerases |
| Hallmark sets | DNA_REPAIR |
| Reactome | 27 pathways, smallest: DNA replication initiation; Inhibition of replication initiation of damaged DNA by RB1/E2F1; Telomere C-strand synthesis initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [P09884](https://www.uniprot.org/uniprotkb/P09884) (DNA polymerase alpha catalytic subunit):

> Catalytic subunit of the DNA polymerase alpha complex (also known as the alpha DNA polymerase-primase complex) which plays an essential role in the initiation of DNA synthesis. During the S phase of the cell cycle, the DNA polymerase alpha complex (composed of a catalytic subunit POLA1, a regulatory subunit POLA2 and two primase subunits PRIM1 and PRIM2) is recruited to DNA at the replicative forks via direct interactions with MCM10 and WDHD1. The primase subunit of the polymerase alpha complex …

**Summary**, from NCBI Gene [5422](https://www.ncbi.nlm.nih.gov/gene/5422):

> This gene encodes the catalytic subunit of DNA polymerase, which together with a regulatory and two primase subunits, forms the DNA polymerase alpha complex. The catalytic subunit plays an essential role in the initiation of DNA replication. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:9173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9173) · Entrez [5422](https://www.ncbi.nlm.nih.gov/gene/5422) · UniProt [P09884](https://www.uniprot.org/uniprotkb/P09884) · Ensembl [ENSG00000101868](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101868)

## Data

Gene col 2182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2182); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2182]; `tensor/DDL_lfc|DDL_z.npy` [2182]; `embed/gene_vectors.npy` [2182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2182 or target_col == 2182). Every well: [[POLA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
