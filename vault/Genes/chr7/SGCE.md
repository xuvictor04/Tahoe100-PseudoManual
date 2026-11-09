---
symbol: "SGCE"
type: "gene"
col: 4853
ensembl_id: "ENSG00000127990"
name: "sarcoglycan epsilon"
location: "7q21.3"
module: 45
arm: "+"
pooled_cpm: 43.08
n_lines_expressing: 38
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# SGCE

*sarcoglycan epsilon* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.35× (z +5.6, q 2e-05, up in 24 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.541× (z -11.1, q 4e-26, down in 35 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3BGRL]] (+0.62, fdr 1e-05), [[CAT]] (+0.62, fdr 7e-06), [[PRCP]] (+0.61, fdr 6e-05); moves opposite to [[RRP7BP-1]] (-0.60, fdr 1e-05), [[LMF1]] (-0.59, fdr 1e-05), [[LINC02804]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[ELAPOR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4853.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +5.6 | 2e-05 | 24/36 (NCI-H2347, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[NG25 (drug)]] 5 µM |  | **1.63×** | +4.7 | 8e-04 | 22/35 (CFPAC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.3 | 0.003 | 16/36 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.17× | +4.1 | 0.005 | 7/36 (SW 900, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.005 | 15/35 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.15× | +3.8 | 0.014 | 13/36 (C32, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.21×** | +3.6 | 0.029 | 15/36 (LOX-IMVI, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.046 | 8/36 (A549, NCI-H23, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.046 | 11/36 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.2 | 0.071 | 7/36 (PANC-1, AsPC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.073 | 13/36 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.073 | 5/36 (CFPAC-1, J82, …) | inconsistent across doses |  |
| [[Bexarotene (drug)]] 5 µM |  | 1.18× | +3.1 | 0.091 | 5/36 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.091 | 5/36 (SW 900, C-33 A, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.095 | 9/35 (J82, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4853.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.541×** | -11.1 | 4e-26 | 35/36 (SNU-423, H4, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.548×** | -10.9 | 3e-25 | 28/36 (A498, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.559×** | -10.6 | 9e-24 | 30/36 (A549, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.621×** | -8.6 | 8e-16 | 26/36 (A498, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.729×** | -8.1 | 8e-14 | 22/36 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.674×** | -7.1 | 9e-11 | 23/36 (RPMI-7951, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.704×** | -6.1 | 9e-08 | 23/35 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -5.4 | 4e-06 | 1/36 (SW 1271) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.751×** | -5.2 | 1e-05 | 24/36 (SK-MEL-2, HepG2/C3A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.761×** | -4.9 | 5e-05 | 19/36 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.755×** | -4.9 | 6e-05 | 19/36 (NCI-H1792, A498, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.763×** | -4.7 | 1e-04 | 14/36 (AN3 CA, H4, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.796×** | -4.1 | 0.002 | 17/36 (SW 900, H4, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.814×** | -3.7 | 0.009 | 14/36 (J82, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.816×** | -3.7 | 0.009 | 14/36 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.866× | -3.6 | 0.009 | 10/36 (A549, H4, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.828×** | -3.4 | 0.024 | 12/35 (A549, CHP-212, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.723×** | -3.1 | 0.063 | 14/36 (LOX-IMVI, CHP-212, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4853. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 148 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -13.6) |
| [[A-172 (line)]] | wt | 34.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -9.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 81.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.425× (z -9.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 166 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[H4 (line)]] | wt | 121 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -14.2) |
| [[HOP62 (line)]] | alt | 37.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -17.3) |
| [[NCI-H1792 (line)]] | alt | 83.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -15.3) |
| [[RPMI-7951 (line)]] | alt | 79.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -11.7) |
| [[SHP-77 (line)]] | alt | 90.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 79.4 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.302× (z -10.7) |
| [[A-427 (line)]] | wt | 55.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.7) | — |
| [[CFPAC-1 (line)]] | alt | 60.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 41.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 36.5 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.07× (z +8.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[Panc 03.27 (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 47.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.282× (z -9.9) |
| [[SW 1088 (line)]] | alt | 104 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.5 µM 0.0889× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.36 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.75 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.50 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.58 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.63 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 29.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4853), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3BGRL]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CAT]] | +0.62 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[PRCP]] | +0.61 | +0.39 / +0.68 | both halves | 6e-05 |  |
| [[RCOR3]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[TMEM38B]] | +0.57 | +0.33 / +0.57 | both halves | 1e-04 |  |
| [[SCPEP1]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SGCB]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 | same gene group; pathway: Extracellular matrix organization; STRING 993 |
| [[SKIC3]] | +0.55 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[GXYLT2]] | +0.54 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[TMEM14A]] | +0.54 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ATP6V1A]] | +0.54 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[KATNAL1]] | +0.54 | +0.59 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7BP-1]] | -0.60 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[LMF1]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[LINC02804]] | -0.58 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[RRP7A]] | -0.58 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ATG7]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[KCNJ14]] | -0.56 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | -0.54 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[AGO2]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[CHMP6]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PPIEL-1]] | -0.52 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[PPP1R10]] | -0.52 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[WNT2B]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELAPOR2]] | B | SGCE activity raises ELAPOR2's level | lines that do not express SGCE (12) vs lines expressing it (38) | 2.76× lower at baseline in the lines without SGCE | 0.0998 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CHST10, HSPA2 |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.563). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (6.1, -10.6); signed map (-27.3, -7.7). **Vector** length 89.6, 23.7% of its response variance represented; |z| ≥ 3 in 704 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.6 | +0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.3 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.6 | -11.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -5.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.8 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | sarcoglycan epsilon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:94,524,204-94,656,572 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DYT11 |
| Gene groups (HGNC) | Sarcoglycans |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 3 pathways, smallest: Formation of the dystrophin-glycoprotein complex (DGC); Non-integrin membrane-ECM interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O43556](https://www.uniprot.org/uniprotkb/O43556) (Epsilon-sarcoglycan):

> Component of the sarcoglycan complex, a subcomplex of the dystrophin-glycoprotein complex which forms a link between the F-actin cytoskeleton and the extracellular matrix.

**Summary**, from NCBI Gene [8910](https://www.ncbi.nlm.nih.gov/gene/8910):

> This gene encodes the epsilon member of the sarcoglycan family. Sarcoglycans are transmembrane proteins that are components of the dystrophin-glycoprotein complex, which link the actin cytoskeleton to the extracellular matrix. Unlike other family members which are predominantly expressed in striated muscle, the epsilon sarcoglycan is more broadly expressed. Mutations in this gene are associated with myoclonus-dystonia syndrome. This gene is imprinted, with preferential expression from the …

**Accessions** — [HGNC:10808](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10808) · Entrez [8910](https://www.ncbi.nlm.nih.gov/gene/8910) · UniProt [O43556](https://www.uniprot.org/uniprotkb/O43556) · Ensembl [ENSG00000127990](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127990)

## Data

Gene col 4853: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4853); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4853, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4853]; `tensor/DDL_lfc|DDL_z.npy` [4853]; `embed/gene_vectors.npy` [4853]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4853 or target_col == 4853). Every well: [[SGCE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGCE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
