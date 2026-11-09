---
symbol: "NBPF12"
type: "gene"
col: 15587
ensembl_id: "ENSG00000268043"
name: "NBPF member 12"
location: "1q21.1"
module: 20
arm: "-"
pooled_cpm: 35.91
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# NBPF12

*NBPF member 12* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.77× (z +6.1, q 7e-07, up in 23 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.406× (z -18.4, q 0e+00, down in 38 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.552× (z -12.1, q 1e-31, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF11]] (+0.92, fdr 7e-06), [[SUGP1]] (+0.67, fdr 7e-06), [[NPHP3]] (+0.66, fdr 7e-06); moves opposite to [[VMA21]] (-0.65, fdr 7e-06), [[MAT2A]] (-0.61, fdr 1e-05), [[EIF5A]] (-0.58, fdr 2e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15587.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +6.1 | 7e-07 | 23/49 (SHP-77, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.63×** | +5.2 | 5e-05 | 24/48 (LoVo, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +4.0 | 0.010 | 11/48 (Hs 766T, HCT15, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.8 | 0.018 | 17/47 (NCI-H2347, HEC-1-A, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.020 | 19/47 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.19× | +3.4 | 0.062 | 13/47 (LoVo, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.16× | +3.1 | 0.16 | 17/48 (A498, NCI-H1573, …) | all doses, flat |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.16 | 2/48 (RKO, NCI-H1573) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15587.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.406×** | -18.4 | 0e+00 | 38/46 (A-172, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.441×** | -16.1 | 0e+00 | 31/40 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.487×** | -13.6 | 1e-39 | 33/44 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.552×** | -12.1 | 1e-31 | 37/48 (A-172, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.652×** | -8.7 | 3e-16 | 32/48 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.685×** | -7.7 | 1e-12 | 27/46 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.676×** | -7.7 | 1e-12 | 29/47 (SK-MEL-2, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.747×** | -6.0 | 2e-07 | 24/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.748×** | -5.9 | 2e-07 | 24/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.769×** | -5.3 | 5e-06 | 24/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.833×** | -5.2 | 1e-05 | 21/48 (SNU-1, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.779×** | -4.9 | 5e-05 | 22/46 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.801×** | -4.5 | 3e-04 | 21/48 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.801×** | -4.5 | 3e-04 | 22/48 (PANC-1, HEC-1-A, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **0.802×** | -4.5 | 3e-04 | 23/46 (PANC-1, A-172, …) | all doses, flat | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.837× | -3.6 | 0.010 | 8/48 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.832×** | -3.6 | 0.010 | 18/48 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.836× | -3.4 | 0.022 | 16/47 (C32, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.892× | -3.3 | 0.032 | 17/48 (LOX-IMVI, SHP-77, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.741×** | -3.2 | 0.037 | 7/48 (MIA PaCa-2, NCI-H661, …) | top dose only | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | 0.856× | -3.2 | 0.038 | 9/48 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Cilostazol (drug)]] 0.05 µM |  | 0.845× | -3.2 | 0.038 | 11/47 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.903× | -2.9 | 0.076 | 8/48 (Panc 03.27, KATO III, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.905× | -2.8 | 0.083 | 6/48 (NCI-H1573, A-427, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.871× | -2.8 | 0.088 | 8/49 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15587. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 46.3 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.310× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 50.8 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HOP62 (line)]] | alt | 48.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 76.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0865× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.323× (z -10.6) |
| [[A549 (line)]] | wt | 50.7 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.288× (z -12.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SK-MEL-2 (line)]] | alt | 41.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.325× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 31.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 28.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +13.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.367× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[PANC-1 (line)]] | alt | 37.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 31.2 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.369× (z -10.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 18.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 35.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 35.1 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.304× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[Hs 766T (line)]] | wt | 32.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 27.0 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.247× (z -10.6) |
| [[KATO III (line)]] | alt | 29.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 69.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-1 (line)]] | wt | 42.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.407× (z -8.7) |
| [[SNU-423 (line)]] | alt | 38.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CHP-212 (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 37.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[hTERT-HPNE (line)]] | wt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LOX-IMVI (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 30.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.227× (z -9.1) |
| [[SW 900 (line)]] | alt | 43.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15587), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF11]] | +0.92 | +0.89 / +0.91 | both halves | 7e-06 | same gene group; STRING 786 |
| [[SUGP1]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[NPHP3]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[CDK7]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[MTIF3]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[HADHB]] | +0.61 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SUMO4]] | +0.59 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[LRRC37B]] | +0.58 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[NRBF2]] | +0.58 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[YJU2B]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.65 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[MAT2A]] | -0.61 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[EIF5A]] | -0.58 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[PSME3]] | -0.55 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[EFR3A]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[FAT1]] | -0.54 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[RBBP7]] | -0.53 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[C1GALT1C1]] | -0.52 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[TARDBP]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[HNRNPA3]] | -0.51 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[HNRNPAB]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[LINC02595]] | -0.51 | -0.55 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-26.7, -31.3); signed map (-15.4, 2.8). **Vector** length 87.0, 19.0% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.9 | -0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.4 | -12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.9 | -13.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.7 | -6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -3.2 | -18.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -3.1 | -7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.0 | -3.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | NBPF member 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:146,938,324-146,996,202 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COAS1; previously KIAA1245 |
| Gene groups (HGNC) | NBPF members |
| Matched by | ensembl_id |

UniProt [Q5TAG4](https://www.uniprot.org/uniprotkb/Q5TAG4) carries no function annotation.

**Summary**, from NCBI Gene [149013](https://www.ncbi.nlm.nih.gov/gene/149013):

> This gene is a member of the neuroblastoma breakpoint family (NBPF) which consists of dozens of recently duplicated genes primarily located in segmental duplications on human chromosome 1. This gene family has experienced its greatest expansion within the human lineage and has expanded, to a lesser extent, among primates in general. Members of this gene family are characterized by tandemly repeated copies of DUF1220 protein domains. Gene copy number variations in the human chromosomal region …

**Accessions** — [HGNC:24297](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24297) · Entrez [149013](https://www.ncbi.nlm.nih.gov/gene/149013) · UniProt [Q5TAG4](https://www.uniprot.org/uniprotkb/Q5TAG4) · Ensembl [ENSG00000268043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000268043)

## Data

Gene col 15587: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15587); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15587, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15587]; `tensor/DDL_lfc|DDL_z.npy` [15587]; `embed/gene_vectors.npy` [15587]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15587 or target_col == 15587). Every well: [[NBPF12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBPF12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
