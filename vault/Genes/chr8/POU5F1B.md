---
symbol: "POU5F1B"
type: "gene"
col: 13073
ensembl_id: "ENSG00000212993"
name: "POU class 5 homeobox 1B"
location: "8q24.21"
module: 8
arm: "+"
pooled_cpm: 5.19
n_lines_expressing: 36
n_dd_up: 6
n_dd_down: 26
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 13
direction_downstream: 26
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# POU5F1B

*POU class 5 homeobox 1B* — 8q24.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +8.1, q 2e-13, up in 12 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.366× (z -10.8, q 3e-24, down in 25 of 33 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCAT1]] (+0.93, fdr 7e-06, ⚠ read-through risk), [[SAMD12-AS1]] (+0.68, fdr 7e-06), [[KLHL2P1]] (+0.63, fdr 3e-05), [[GNA14]] (+0.62, fdr 1e-05); moves opposite to [[KATNAL1]] (-0.52, fdr 3e-05), [[ZNF8-DT]] (-0.51, fdr 3e-05), [[PGBD1]] (-0.50, fdr 5e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[SPINT1-AS1]] → it (grade B ⚠); 26 go from it, the strongest it → [[SLC44A3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13073.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +8.1 | 2e-13 | 12/29 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +7.7 | 3e-12 | 1/7 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.75×** | +6.0 | 4e-07 | 9/32 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +5.6 | 2e-06 | 2/10 (MIA PaCa-2, NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +5.3 | 1e-05 | 6/19 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +3.5 | 0.038 | 1/7 (SW1417) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.35× | +3.1 | 0.17 | 6/31 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.22× | +3.0 | 0.19 | 8/33 (MIA PaCa-2, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13073.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.366×** | -10.8 | 3e-24 | 25/33 (NCI-H1573, HT-29, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.430×** | -8.7 | 1e-15 | 17/30 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.469×** | -8.1 | 1e-13 | 24/34 (SW48, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.473×** | -8.0 | 2e-13 | 24/34 (HT-29, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.513×** | -7.1 | 1e-10 | 19/33 (SW1417, CFPAC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.503×** | -7.1 | 1e-10 | 17/22 (HT-29, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.519×** | -7.0 | 2e-10 | 18/25 (HT-29, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.551×** | -6.4 | 1e-08 | 19/34 (HT-29, KATO III, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.555×** | -6.3 | 2e-08 | 19/32 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.571×** | -5.8 | 5e-07 | 15/33 (CFPAC-1, Hs 766T, …) | rises with dose | plate-row cell shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.589×** | -5.7 | 8e-07 | 17/34 (HT-29, SW1417, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.616×** | -5.2 | 1e-05 | 14/33 (HT-29, SHP-77, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.618×** | -5.1 | 1e-05 | 20/31 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.748×** | -4.4 | 5e-04 | 18/28 (NCI-H1573, HT-29, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.462×** | -4.3 | 5e-04 | 13/29 (HT-29, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.651×** | -4.3 | 5e-04 | 16/31 (HT-29, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.754×** | -4.2 | 7e-04 | 17/33 (HT-29, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.694×** | -3.9 | 0.003 | 11/29 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.500×** | -3.9 | 0.003 | 13/30 (HT-29, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.706×** | -3.7 | 0.005 | 8/33 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.708×** | -3.7 | 0.006 | 15/28 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -3.5 | 0.011 | 16/32 (SW48, HT-29, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.793×** | -3.5 | 0.011 | 13/33 (Hs 766T, C32, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.638×** | -3.4 | 0.014 | 2/34 (NCI-H1573, HT-29) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13073. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 15.6 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -15.5) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.101× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 9.87 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -12.3) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.149× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 10.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0607× (z -19.4) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0244× (z -18.2) |
| [[KATO III (line)]] | alt | 12.9 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0590× (z -11.4) ⚠ toxic |
| [[SW48 (line)]] | wt | 21.7 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0186× (z -13.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0412× (z -10.6) |
| [[A498 (line)]] | wt | 6.08 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -11.3) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.137× (z -8.9) |
| [[LoVo (line)]] | wt | 6.55 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0709× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.160× (z -8.5) |
| [[SW1417 (line)]] | alt | 22.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -11.5) ⚠ cell-cycle shift, explains ~74% of this change |
| [[C32 (line)]] | wt | 8.16 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.115× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0814× (z -10.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 3.90 | 0 | 1 | — | [[Sodium Salicylate (drug)]] 0.05 µM 0.0428× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.335× (z -14.8) ⚠ position not correctable |
| [[SHP-77 (line)]] | alt | 4.96 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0390× (z -10.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.63 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0837× (z -8.8) |
| [[A-172 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.999 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.842 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.747 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.932 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.957 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.765 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.903 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13073), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCAT1]] | +0.93 | +0.90 / +0.90 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of PCAT1 on the same strand (can correlate by spillover, not regulation) |
| [[SAMD12-AS1]] | +0.68 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[KLHL2P1]] | +0.63 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[GNA14]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PROM1]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CATSPERB]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[LINC02343]] | +0.60 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[STS]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ANK3]] | +0.58 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[ATP10B]] | +0.58 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[RGS6]] | +0.57 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[SLC44A3-AS1]] | +0.57 | +0.63 / +0.32 | both halves | 1e-04 |  |
| [[STEAP2-AS1]] | +0.56 | +0.55 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KATNAL1]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ZNF8-DT]] | -0.51 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[PGBD1]] | -0.50 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[ACSF2]] | -0.50 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[DNAAF9]] | -0.49 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[MPP2]] | -0.48 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[STARD9]] | -0.47 | -0.41 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPINT1-AS1]] | B | SPINT1-AS1 activity raises POU5F1B's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.03× lower at baseline in the lines without SPINT1-AS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[BTC]] | B | BTC activity raises POU5F1B's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.84× lower at baseline in the lines without BTC | 0.026 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[TNFSF15]] | B | TNFSF15 activity raises POU5F1B's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without TNFSF15 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[ERBB3]] | B | ERBB3 activity raises POU5F1B's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.18× lower at baseline in the lines without ERBB3 | 0.036 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[PRR15L]] | B | PRR15L activity raises POU5F1B's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 2.40× lower at baseline in the lines without PRR15L | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[TMEM30B]] | B | TMEM30B activity raises POU5F1B's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 2.47× lower at baseline in the lines without TMEM30B | 0.042 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[TMEM45B]] | B | TMEM45B activity raises POU5F1B's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 2.25× lower at baseline in the lines without TMEM45B | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[CFTR]] | B | CFTR activity raises POU5F1B's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.08× lower at baseline in the lines without CFTR | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[CCSER1]] | B | CCSER1 activity raises POU5F1B's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 1.79× lower at baseline in the lines without CCSER1 | 0.070 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[ST14]] | B | ST14 activity raises POU5F1B's level | lines that do not express ST14 (32) vs lines expressing it (18) | 2.28× lower at baseline in the lines without ST14 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[TMEM45B]] | B | TMEM45B activity strengthens POU5F1B's drug response | lines that do not express TMEM45B (19) vs lines expressing it (15) | the lines without TMEM45B respond 0.42× as strongly (z diff +2.42); strongest at Panobinostat 5 µM: 0.69x vs 0.20x (z diff +4.8) | 0.091 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; target measured in part of the lines; artifact flags |
| [[ATP10B]] | B | ATP10B activity raises POU5F1B's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 2.41× lower at baseline in the lines without ATP10B | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 24, C 2. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3-AS1]] | B | POU5F1B activity raises SLC44A3-AS1's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 2.55× lower at baseline in the lines without POU5F1B | 0.010 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[CCSER1]] | B | POU5F1B activity raises CCSER1's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 3.54× lower at baseline in the lines without POU5F1B | 0.014 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[SAMD12]] | B | POU5F1B activity raises SAMD12's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 3.59× lower at baseline in the lines without POU5F1B | 0.020 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[TNFSF15]] | B | POU5F1B activity raises TNFSF15's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 3.17× lower at baseline in the lines without POU5F1B | 0.027 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[DNAAF9]] | B | POU5F1B activity lowers DNAAF9's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 2.73× higher at baseline in the lines without POU5F1B | 0.029 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[SPINT1-AS1]] | B | POU5F1B activity raises SPINT1-AS1's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 2.25× lower at baseline in the lines without POU5F1B | 0.036 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[BTC]] | B | POU5F1B activity raises BTC's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 2.12× lower at baseline in the lines without POU5F1B | 0.040 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[BOLA3-DT]] | B | POU5F1B activity lowers BOLA3-DT's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 1.59× higher at baseline in the lines without POU5F1B | 0.047 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[ACTR3C]] | B | POU5F1B activity raises ACTR3C's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 2.72× lower at baseline in the lines without POU5F1B | 0.051 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[ST14]] | B | POU5F1B activity raises ST14's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 4.71× lower at baseline in the lines without POU5F1B | 0.051 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[SYK]] | B | POU5F1B activity raises SYK's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 3.99× lower at baseline in the lines without POU5F1B | 0.055 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[TC2N]] | B | POU5F1B activity raises TC2N's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 3.78× lower at baseline in the lines without POU5F1B | 0.056 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.7, 53.9); signed map (58.8, 0.4). **Vector** length 68.3, 13.1% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +7.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.3 | +2.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.8 | -10.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -1.9 | -7.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -1.8 | -4.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.7 | -3.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.5 | -5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -3.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -3.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.0 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | POU class 5 homeobox 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.21 — chr8:127,322,183-127,420,066 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OTF3C; previously OTF3P1, POU5F1P1 |
| Gene groups (HGNC) | POU class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06416](https://www.uniprot.org/uniprotkb/Q06416) (POU domain, class 5, transcription factor 1B):

> Shows weak transcriptional activator activity.

**Summary**, from NCBI Gene [5462](https://www.ncbi.nlm.nih.gov/gene/5462):

> This intronless gene was thought to be a transcribed pseudogene of POU class 5 homeobox 1, however, it has been reported that this gene can encode a functional protein. The encoded protein is nearly the same length as and highly similar to the POU class 5 homeobox 1 transcription factor, has been shown to be a weak transcriptional activator and may play a role in carcinogenesis and eye development. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:9223](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9223) · Entrez [5462](https://www.ncbi.nlm.nih.gov/gene/5462) · UniProt [Q06416](https://www.uniprot.org/uniprotkb/Q06416) · Ensembl [ENSG00000212993](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000212993)

## Data

Gene col 13073: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13073); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13073, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13073]; `tensor/DDL_lfc|DDL_z.npy` [13073]; `embed/gene_vectors.npy` [13073]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13073 or target_col == 13073). Every well: [[POU5F1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POU5F1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
