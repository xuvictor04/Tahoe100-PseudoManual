---
symbol: "PCSK6"
type: "gene"
col: 6417
ensembl_id: "ENSG00000140479"
name: "proprotein convertase subtilisin/kexin type 6"
location: "15q26.3"
module: 1
arm: "+"
pooled_cpm: 42.33
n_lines_expressing: 29
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PCSK6

*proprotein convertase subtilisin/kexin type 6* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +9.1, q 5e-17, up in 13 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.251× (z -23.9, q 0e+00, down in 26 of 27 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAF3]] (+0.60, fdr 2e-05), [[KCNQ4]] (+0.59, fdr 1e-05), [[PHACTR2]] (+0.59, fdr 2e-04); moves opposite to [[ARL3]] (-0.62, fdr 3e-05), [[PCMT1]] (-0.59, fdr 2e-04), [[PLAG1]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ST6GAL1]] → it (grade B ⚠); 8 go from it, the strongest it → [[ST6GAL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6417.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.1 | 5e-17 | 13/26 (A549, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +6.6 | 1e-08 | 16/27 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +6.1 | 3e-07 | 12/27 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +5.3 | 2e-05 | 12/27 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.6 | 4e-04 | 13/27 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.0 | 0.007 | 8/27 (Panc 03.27, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.23×** | +3.6 | 0.031 | 8/26 (A498, Panc 03.27, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.5 | 0.033 | 8/27 (SW1417, A549, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.2 | 0.089 | 6/27 (C32, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6417.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.251×** | -23.9 | 0e+00 | 26/27 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.253×** | -23.7 | 0e+00 | 27/27 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.285×** | -21.7 | 0e+00 | 26/27 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.551×** | -10.3 | 1e-22 | 23/27 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.581×** | -9.4 | 7e-19 | 21/27 (LoVo, SNU-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.597×** | -8.9 | 4e-17 | 25/27 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.423×** | -7.8 | 6e-13 | 25/28 (A-427, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.657×** | -7.3 | 3e-11 | 20/27 (LoVo, NCI-H23, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.764×** | -6.6 | 3e-09 | 14/27 (LoVo, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.500×** | -6.3 | 2e-08 | 20/27 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.713×** | -5.6 | 9e-07 | 17/27 (LoVo, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.753×** | -4.9 | 4e-05 | 14/27 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **0.757×** | -4.8 | 6e-05 | 17/27 (HepG2/C3A, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.765×** | -4.6 | 1e-04 | 17/27 (Panc 03.27, BT-474, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.602×** | -4.6 | 2e-04 | 15/27 (LS 180, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.811×** | -3.6 | 0.008 | 12/27 (C32, HepG2/C3A, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.841× | -3.0 | 0.070 | 6/27 (HT-29, SW1417, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.721×** | -3.0 | 0.074 | 11/27 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.888× | -2.9 | 0.079 | 6/28 (A498, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6417. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 231 | 0 | 17 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0592× (z -30.1) |
| [[RKO (line)]] | wt | 78.2 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -27.8) |
| [[C32 (line)]] | wt | 113 | 0 | 11 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0957× (z -16.8) ⚠ cell-cycle shift, explains ~94% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.204× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 31.4 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 60.0 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0573× (z -25.0) |
| [[A-427 (line)]] | wt | 33.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -17.3) |
| [[SNU-1 (line)]] | wt | 61.1 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.289× (z -11.3) |
| [[HepG2_C3A (line)]] | wt | 167 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -16.2) |
| [[Panc 03.27 (line)]] | alt | 34.4 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +24.0) | [[Belinostat (drug)]] 5 µM 0.236× (z -10.0) |
| [[COLO 205 (line)]] | alt | 150 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0517× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0950× (z -17.2) |
| [[NCI-H1792 (line)]] | alt | 74.2 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.246× (z -14.1) |
| [[A549 (line)]] | wt | 38.1 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.9) | [[Belinostat (drug)]] 5 µM 0.188× (z -13.4) |
| [[HT-29 (line)]] | alt | 77.4 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.177× (z -14.9) |
| [[LS 180 (line)]] | wt | 60.4 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.199× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 46.2 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.146× (z -20.5) |
| [[SW1417 (line)]] | alt | 110 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -13.0) |
| [[A498 (line)]] | wt | 67.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.133× (z -15.4) |
| [[KATO III (line)]] | alt | 31.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.160× (z -11.8) |
| [[SW480 (line)]] | alt | 55.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -21.5) |
| [[A-172 (line)]] | wt | 10.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.173× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 39.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +25.9) | — |
| [[BT-474 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 86.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.296× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~1% of this change |
| [[PANC-1 (line)]] | alt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.69× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 9.48 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.25 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.84 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.03 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.13 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.66 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.92 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.43 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.68 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.20 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6417), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF3]] | +0.60 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[KCNQ4]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[PHACTR2]] | +0.59 | +0.64 / +0.32 | both halves | 2e-04 |  |
| [[TMEM117]] | +0.59 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[TMCO4]] | +0.59 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[DHX37]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[PITX1-AS1]] | +0.58 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[GPATCH4]] | +0.58 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[UTP20]] | +0.58 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[PARD3B]] | +0.58 | +0.55 / +0.39 | both halves | 6e-05 |  |
| [[ZNF124]] | +0.58 | +0.58 / +0.38 | both halves | 7e-05 |  |
| [[DNAJC11]] | +0.58 | +0.58 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL3]] | -0.62 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[PCMT1]] | -0.59 | -0.61 / -0.31 | both halves | 2e-04 |  |
| [[PLAG1]] | -0.59 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[MED30]] | -0.58 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[RRAS]] | -0.57 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[PJA2]] | -0.57 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[PCTP]] | -0.56 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[PLEKHH3]] | -0.56 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[MOSPD3]] | -0.56 | -0.63 / -0.27 | both halves | 3e-04 |  |
| [[PIP4P2]] | -0.53 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[LMBR1L]] | -0.53 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[KLHL7]] | -0.52 | -0.53 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST6GAL1]] | B | ST6GAL1 activity raises PCSK6's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 3.29× lower at baseline in the lines without ST6GAL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| [[SLC16A9]] | B | SLC16A9 activity raises PCSK6's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 1.81× lower at baseline in the lines without SLC16A9 | 0.099 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST6GAL1]] | B | PCSK6 activity raises ST6GAL1's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 2.42× lower at baseline in the lines without PCSK6 | 0.011 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |
| [[PRKAR1B]] | B | PCSK6 activity raises PRKAR1B's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 1.83× lower at baseline in the lines without PCSK6 | 0.048 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |
| [[ZNF439]] | B | PCSK6 activity lowers ZNF439's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 2.88× higher at baseline in the lines without PCSK6 | 0.060 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |
| [[TRIQK]] | B | PCSK6 activity lowers TRIQK's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 1.62× higher at baseline in the lines without PCSK6 | 0.071 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |
| [[HSPB11]] | B | PCSK6 activity lowers HSPB11's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 1.39× higher at baseline in the lines without PCSK6 | 0.081 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |
| [[SRC]] | B | PCSK6 activity raises SRC's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 1.46× lower at baseline in the lines without PCSK6 | 0.082 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |
| [[METTL8]] | B | PCSK6 activity raises METTL8's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 1.45× lower at baseline in the lines without PCSK6 | 0.086 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |
| [[GNAI2]] | B | PCSK6 activity lowers GNAI2's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 1.75× higher at baseline in the lines without PCSK6 | 0.094 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (13.8, 1.8); signed map (25.5, -31.8). **Vector** length 94.3, 26.3% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +6.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +1.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -1.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.3 | -8.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -23.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -23.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.8 | -6.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.7 | -10.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -6.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.5 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | proprotein convertase subtilisin/kexin type 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:101,289,784-101,525,202 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPC4; previously PACE4 |
| Gene groups (HGNC) | Proprotein convertase subtilisin/kexin family |
| Reactome | 19 pathways, smallest: Expression and Processing of Neurotrophins; NGF processing; Assembly of active LPL and LIPC lipase complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [P29122](https://www.uniprot.org/uniprotkb/P29122) (Proprotein convertase subtilisin/kexin type 6):

> Serine endoprotease that processes various proproteins by cleavage at paired basic amino acids, recognizing the RXXX[KR]R consensus motif. Likely functions in the constitutive secretory pathway, with unique restricted distribution in both neuroendocrine and non-neuroendocrine tissues.

**Summary**, from NCBI Gene [5046](https://www.ncbi.nlm.nih.gov/gene/5046):

> This gene encodes a member of the subtilisin-like proprotein convertase family, which includes proteases that process protein and peptide precursors trafficking through regulated or constitutive branches of the secretory pathway. The encoded protein undergoes an initial autocatalytic processing event in the ER to generate a heterodimer which exits the ER and sorts to the trans-Golgi network where a second autocatalytic event takes place and the catalytic activity is acquired. The encoded …

**Accessions** — [HGNC:8569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8569) · Entrez [5046](https://www.ncbi.nlm.nih.gov/gene/5046) · UniProt [P29122](https://www.uniprot.org/uniprotkb/P29122) · Ensembl [ENSG00000140479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140479)

## Data

Gene col 6417: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6417); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6417, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6417]; `tensor/DDL_lfc|DDL_z.npy` [6417]; `embed/gene_vectors.npy` [6417]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6417 or target_col == 6417). Every well: [[PCSK6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCSK6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
