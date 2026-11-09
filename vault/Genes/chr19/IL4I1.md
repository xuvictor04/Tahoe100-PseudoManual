---
symbol: "IL4I1"
type: "gene"
col: 2527
ensembl_id: "ENSG00000104951"
name: "interleukin 4 induced 1"
location: "19q13.33"
module: 16
arm: "+"
pooled_cpm: 16.08
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# IL4I1

*interleukin 4 induced 1* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.51× (z +24.2, q 0e+00, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.674× (z -7.3, q 1e-10, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IKBKE]] (+0.65, fdr 7e-06), [[NUP62]] (+0.62, fdr 1e-05, ⚠ same locus), [[GBP5]] (+0.62, fdr 7e-06), [[ZNF180]] (+0.60, fdr 7e-06); moves opposite to [[ATP11B]] (-0.51, fdr 3e-05), [[CBLB]] (-0.49, fdr 4e-05), [[RAB2A]] (-0.48, fdr 8e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZSCAN12]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2527.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.51×** | +24.2 | 0e+00 | 36/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.32×** | +16.2 | 0e+00 | 45/47 (PANC-1, J82, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.11×** | +13.7 | 1e-40 | 34/43 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +9.6 | 1e-19 | 29/46 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +7.1 | 1e-10 | 23/47 (HT-29, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.8 | 7e-07 | 18/44 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +5.5 | 2e-06 | 16/47 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 1e-04 | 18/47 (SW480, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.52×** | +4.1 | 0.003 | 9/42 (A498, COLO 205, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.23×** | +3.9 | 0.005 | 5/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.014 | 16/46 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.025 | 0/45 | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2527.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.674×** | -7.3 | 1e-10 | 24/48 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.789×** | -6.2 | 1e-07 | 20/45 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.731×** | -5.8 | 1e-06 | 20/38 (C-33 A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.729×** | -5.6 | 2e-06 | 12/23 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.745×** | -5.5 | 6e-06 | 18/47 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.747×** | -5.4 | 6e-06 | 23/47 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.781×** | -4.6 | 4e-04 | 17/47 (A-172, SNU-423, …) | rises with dose |  |
| [[Pimozide (drug)]] 0.05 µM |  | **0.783×** | -4.5 | 4e-04 | 14/45 (A-427, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -4.4 | 6e-04 | 20/47 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.792×** | -4.2 | 0.002 | 16/46 (A-172, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.803×** | -4.1 | 0.002 | 13/46 (HCT15, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.835× | -3.4 | 0.038 | 13/46 (A-172, SNU-423, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.838× | -3.3 | 0.047 | 8/45 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.841× | -3.2 | 0.053 | 10/46 (AN3 CA, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.887× | -3.1 | 0.066 | 9/48 (SK-MEL-2, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2527. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 51.7 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.0775× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.192× (z -10.9) |
| [[PANC-1 (line)]] | alt | 12.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +16.9) | — |
| [[SNU-423 (line)]] | alt | 35.5 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.151× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 14.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 2 | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.108× (z -9.8) |
| [[SW 900 (line)]] | alt | 20.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -10.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -10.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 10.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.132× (z -8.7) |
| [[H4 (line)]] | wt | 15.3 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0894× (z -10.5) |
| [[HS-578T (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +13.2) | — |
| [[HT-29 (line)]] | alt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 9.40 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0708× (z -10.8) |
| [[J82 (line)]] | alt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +16.3) | — |
| [[LOX-IMVI (line)]] | wt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0974× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[NCI-H2347 (line)]] | alt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2527), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IKBKE]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[NUP62]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 | STRING 868; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[GBP5]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ZNF180]] | +0.60 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[YJU2]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[ZNF620]] | +0.58 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[C1QTNF1]] | +0.57 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[SENP1]] | +0.56 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[MRM2]] | +0.56 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[ZNF625]] | +0.56 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[ZNF136]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[DHX58]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ZNF107]] | +0.54 | +0.45 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP11B]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[CBLB]] | -0.49 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[RAB2A]] | -0.48 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[SNX25]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[GAN]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[SEL1L]] | -0.47 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[LMBR1]] | -0.47 | -0.47 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZSCAN12]] | B | ZSCAN12 activity raises IL4I1's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.05× lower at baseline in the lines without ZSCAN12 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[CCL2]] | B | CCL2 activity raises IL4I1's level | lines that do not express CCL2 (34) vs lines expressing it (16) | 1.41× lower at baseline in the lines without CCL2 | 0.040 | ⚠ within organs, on part of the lines; also absent: KIRREL3, ITGA8, VCAM1 |
| [[TOP2A]] | B | TOP2A activity raises IL4I1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF502]] | B | ZNF502 activity raises IL4I1's level | lines that do not express ZNF502 (18) vs lines expressing it (32) | 1.43× lower at baseline in the lines without ZNF502 | 0.068 | ⚠ within organs, on part of the lines; also absent: CXCR4, LINC01611, ZNF506 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (24.5, 7.3); signed map (2.4, -24.2). **Vector** length 87.9, 17.2% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +16.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +24.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +9.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +13.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.4 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +2.8 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.6 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +1.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.6 | -7.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 4 induced 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,889,654-49,929,539 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FIG1 |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 3 pathways, smallest: Phenylalanine metabolism; Phenylalanine and tyrosine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RQ9](https://www.uniprot.org/uniprotkb/Q96RQ9) (L-amino-acid oxidase):

> Secreted L-amino-acid oxidase that acts as a key immunoregulator. Has preference for L-aromatic amino acids: converts phenylalanine (Phe), tyrosine (Tyr) and tryptophan (Trp) to phenylpyruvic acid (PP), hydroxyphenylpyruvic acid (HPP), and indole-3-pyruvic acid (I3P), respectively. Also has weak L-arginine oxidase activity. Acts as a negative regulator of anti-tumor immunity by mediating Trp degradation via an indole pyruvate pathway that activates the transcription factor AHR. IL4I1-mediated …

**Summary**, from NCBI Gene [259307](https://www.ncbi.nlm.nih.gov/gene/259307):

> This gene encodes a secreted L-amino acid oxidase protein which primarily catabolizes L-phenylalanine and, to a lesser extent, L-arginine. The expression of this gene is induced by the cytokine interleukin 4 in B cells. This gene is also expressed in macrophages and dendritic cells. This protein may play a role immune system escape as it is expressed in tumor-associated macrophages and suppresses T-cell responses. This protein also contains domains thought to be involved in the binding of …

**Accessions** — [HGNC:19094](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19094) · Entrez [259307](https://www.ncbi.nlm.nih.gov/gene/259307) · UniProt [Q96RQ9](https://www.uniprot.org/uniprotkb/Q96RQ9) · Ensembl [ENSG00000104951](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104951)

## Data

Gene col 2527: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2527); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2527, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2527]; `tensor/DDL_lfc|DDL_z.npy` [2527]; `embed/gene_vectors.npy` [2527]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2527 or target_col == 2527). Every well: [[IL4I1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL4I1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
