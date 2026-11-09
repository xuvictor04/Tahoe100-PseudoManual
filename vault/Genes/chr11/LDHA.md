---
symbol: "LDHA"
type: "gene"
col: 5550
ensembl_id: "ENSG00000134333"
name: "lactate dehydrogenase A"
location: "11p15.1"
module: 99
arm: "+"
pooled_cpm: 753.82
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# LDHA

*lactate dehydrogenase A* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.76× (z +6.3, q 2e-07, up in 46 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 5 lines (NCI-H460 4.67×, COLO 205 3.05×, AsPC-1 2.51×, SW480 2.56×, …; ⚠ cell-cycle shift, explains ~75% of this change); [[TAK-901 (drug)]] 5 µM in 4 lines (COLO 205 6.70×, SNU-1 6.49×, NCI-H1573 6.77×, NCI-H23 4.21×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H460 3.95×, SW480 2.38×; ⚠ cell-cycle shift, explains ~89% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.219× (z -25.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENO1]] (+0.82, fdr 7e-06), [[PGK1]] (+0.74, fdr 7e-06), [[ALDOA]] (+0.66, fdr 7e-06); moves opposite to [[MSTO1]] (-0.55, fdr 2e-05), [[MAFG]] (-0.49, fdr 4e-05), [[PPP1R26-AS1]] (-0.48, fdr 1e-04).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NEDD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5550.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 5 lines (NCI-H460 4.67×, COLO 205 3.05×, AsPC-1 2.51×, SW480 2.56×, …; ⚠ cell-cycle shift, explains ~75% of this change); [[TAK-901 (drug)]] 5 µM in 4 lines (COLO 205 6.70×, SNU-1 6.49×, NCI-H1573 6.77×, NCI-H23 4.21×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H460 3.95×, SW480 2.38×; ⚠ cell-cycle shift, explains ~89% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.76×** | +6.3 | 2e-07 | 46/49 (COLO 205, SNU-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.1 | 1e-04 | 2/50 (MIA PaCa-2, NCI-H2122) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.43×** | +4.2 | 0.005 | 35/48 (NCI-H460, COLO 205, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | 1.31× | +3.2 | 0.21 | 30/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.30× | +3.1 | 0.25 | 29/48 (COLO 205, NCI-H1792, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5550.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.219×** | -25.3 | 0e+00 | 48/48 (MIA PaCa-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.503×** | -11.5 | 6e-28 | 45/49 (BT-474, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.494×** | -8.0 | 2e-13 | 47/47 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.508×** | -8.0 | 2e-13 | 40/48 (RKO, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.555×** | -6.7 | 3e-09 | 37/48 (RKO, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.609×** | -5.6 | 2e-06 | 41/47 (C-33 A, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.622×** | -5.6 | 2e-06 | 34/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.658×** | -4.9 | 6e-05 | 33/48 (HT-29, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.661×** | -4.7 | 2e-04 | 42/48 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.482×** | -4.5 | 4e-04 | 46/49 (A-427, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.780×** | -4.1 | 0.002 | 32/48 (J82, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.710×** | -4.0 | 0.003 | 43/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.726×** | -3.6 | 0.013 | 27/44 (SK-MEL-2, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.742×** | -3.5 | 0.018 | 32/48 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.700×** | -3.5 | 0.018 | 32/48 (LOX-IMVI, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.751×** | -3.4 | 0.025 | 28/48 (C-33 A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.777×** | -3.0 | 0.088 | 27/48 (HT-29, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.619×** | -3.0 | 0.088 | 32/49 (LoVo, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5550. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 708 | 6 (6 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.67× (z +14.7) ⚠ cell-cycle shift, explains ~75% of this change | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -21.4) |
| [[AsPC-1 (line)]] | alt | 770 | 1 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +10.5) ⚠ cell-cycle shift, explains ~75% of this change | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -22.2) |
| [[NCI-H1573 (line)]] | alt | 985 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.77× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.0871× (z -30.6) |
| [[C-33 A (line)]] | alt | 694 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -29.2) |
| [[HEC-1-A (line)]] | alt | 849 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -22.6) |
| [[HT-29 (line)]] | alt | 845 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -23.8) |
| [[LoVo (line)]] | wt | 745 | 1 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +9.3) ⚠ cell-cycle shift, explains ~75% of this change | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -24.5) |
| [[SNU-1 (line)]] | wt | 803 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.49× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -26.0) |
| [[SW480 (line)]] | alt | 740 | 2 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +9.5) ⚠ cell-cycle shift, explains ~75% of this change | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -26.2) |
| [[HCT15 (line)]] | alt | 997 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -31.4) |
| [[LOX-IMVI (line)]] | wt | 978 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -28.5) |
| [[LS 180 (line)]] | wt | 1,009 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -20.1) |
| [[MIA PaCa-2 (line)]] | alt | 887 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0900× (z -39.2) |
| [[RKO (line)]] | wt | 572 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -22.8) |
| [[SW48 (line)]] | wt | 885 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -22.6) |
| [[A-172 (line)]] | wt | 882 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -17.0) |
| [[AN3 CA (line)]] | alt | 678 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -21.7) |
| [[BT-474 (line)]] | alt | 568 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -24.0) |
| [[C32 (line)]] | wt | 639 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -12.9) |
| [[COLO 205 (line)]] | alt | 443 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +11.8) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.70× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -14.5) |
| [[Hs 766T (line)]] | wt | 949 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -25.7) |
| [[KATO III (line)]] | alt | 375 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -26.4) |
| [[NCI-H2030 (line)]] | alt | 739 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -24.9) |
| [[PANC-1 (line)]] | alt | 593 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -17.6) |
| [[RPMI-7951 (line)]] | alt | 819 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -24.4) |
| [[SK-MEL-2 (line)]] | alt | 716 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -23.8) |
| [[SW 1271 (line)]] | alt | 1,382 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -20.8) |
| [[A-427 (line)]] | wt | 513 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -23.9) |
| [[CFPAC-1 (line)]] | alt | 681 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -21.5) |
| [[H4 (line)]] | wt | 1,104 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -21.4) |
| [[HepG2_C3A (line)]] | wt | 626 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -24.3) |
| [[HOP62 (line)]] | alt | 886 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -15.0) |
| [[HS-578T (line)]] | alt | 1,101 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -17.9) |
| [[J82 (line)]] | alt | 965 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 600 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 430 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.21× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -21.6) |
| [[NCI-H661 (line)]] | alt | 507 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -17.2) |
| [[Panc 03.27 (line)]] | alt | 989 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -23.9) |
| [[SHP-77 (line)]] | alt | 303 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -20.6) |
| [[SNU-423 (line)]] | alt | 1,099 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -20.9) |
| [[SW1417 (line)]] | alt | 593 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -14.4) |
| [[A549 (line)]] | wt | 945 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -19.0) |
| [[CHP-212 (line)]] | wt | 318 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -17.2) |
| [[hTERT-HPNE (line)]] | wt | 841 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 923 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -23.0) |
| [[SW 1088 (line)]] | alt | 849 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.2) |
| [[SW 900 (line)]] | alt | 350 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -20.3) |
| [[A498 (line)]] | wt | 503 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 590 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 656 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5550), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENO1]] | +0.82 | +0.85 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 924 |
| [[PGK1]] | +0.74 | +0.78 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 923 |
| [[ALDOA]] | +0.66 | +0.70 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM; STRING 973 |
| [[BNIP3]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 | STRING 642 |
| [[BCKDK]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[C4orf3]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[TPI1]] | +0.57 | +0.64 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 913 |
| [[UQCRC1]] ⚠ | +0.57 | +0.56 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 464; ⚠ in the vector space only through flagged drug-doses |
| [[PKM]] | +0.56 | +0.63 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS; STRING 997 |
| [[EGLN1]] | +0.56 | +0.64 / +0.55 | both halves | 1e-05 | STRING 551 |
| [[EIF4A3]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[EFNA3]] | +0.55 | +0.59 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[MPI]] | +0.55 | +0.50 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSTO1]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[MAFG]] | -0.49 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[PPP1R26-AS1]] | -0.48 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[LINC01772]] | -0.48 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[POU6F1]] | -0.48 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[C8orf44-SGK3]] | -0.47 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[ZC3H3]] | -0.47 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[UPF3A]] | -0.45 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[AGER]] | -0.45 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[ZNF213-AS1]] | -0.45 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[IQCK]] | -0.44 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[GTF3C2-AS2]] | -0.44 | -0.39 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEDD9]] | B | NEDD9 activity weakens LDHA's drug response | lines that do not express NEDD9 (16) vs lines expressing it (34) | the lines without NEDD9 respond 1.20× as strongly (z diff -1.54); strongest at Harringtonine 5 µM: 0.43x vs 0.65x (z diff -3.9) | 0.091 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.2, -15.4); signed map (-37.2, 28.4). **Vector** length 152, 63.6% of its response variance represented; |z| ≥ 3 in 1,232 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glycolysis* (reactome, mean cos +0.56 to 10); *Glucose metabolism* (reactome, mean cos +0.56 to 10); *Metabolism of carbohydrates and carbohydrate derivatives* (reactome, mean cos +0.56 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +10.0 | -3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +9.0 | -5.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.7 | -4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +6.1 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +1.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +4.2 | +1.5 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | +4.1 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.3 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -25.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.5 | -5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.5 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.9 | -1.9 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -3.8 | -1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | lactate dehydrogenase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:18,394,560-18,408,425 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | L-lactate dehydrogenase family |
| Hallmark sets | FATTY_ACID_METABOLISM, GLYCOLYSIS, HYPOXIA, MTORC1_SIGNALING, MYC_TARGETS_V1, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Regulation of pyruvate metabolism; Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P00338](https://www.uniprot.org/uniprotkb/P00338) (L-lactate dehydrogenase A chain):

> Interconverts simultaneously and stereospecifically pyruvate and lactate with concomitant interconversion of NADH and NAD(+). Can also use 2-oxoglutarate as substrate and catalyze the reduction of 2-oxoglutarate to L-2-hydroxyglutarate.

**Summary**, from NCBI Gene [3939](https://www.ncbi.nlm.nih.gov/gene/3939):

> This gene encodes the A subunit of lactate dehydrogenase enzyme which catalyzes the reversible conversion of pyruvate to lactate with the concomitant oxidation of NADH to NAD in anaerobic glycolysis. The protein is found predominantly in skeletal muscle and belongs to the lactate dehydrogenase family. Mutations in this gene have been linked to exertional myoglobinuria. The human genome contains several non-transcribed pseudogenes of this gene. [provided by RefSeq, Sep 2023]

**Accessions** — [HGNC:6535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6535) · Entrez [3939](https://www.ncbi.nlm.nih.gov/gene/3939) · UniProt [P00338](https://www.uniprot.org/uniprotkb/P00338) · Ensembl [ENSG00000134333](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134333)

## Data

Gene col 5550: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5550); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5550, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5550]; `tensor/DDL_lfc|DDL_z.npy` [5550]; `embed/gene_vectors.npy` [5550]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5550 or target_col == 5550). Every well: [[LDHA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LDHA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
