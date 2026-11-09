---
symbol: "ABCG2"
type: "gene"
col: 4017
ensembl_id: "ENSG00000118777"
name: "ATP binding cassette subfamily G member 2 (JR blood group)"
location: "4q22.1"
module: 14
arm: "+"
pooled_cpm: 3.58
n_lines_expressing: 35
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ABCG2

*ATP binding cassette subfamily G member 2 (JR blood group)* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (20 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.73× (z +19.1, q 0e+00, up in 17 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Naproxen (drug)]] 0.05 µM in 1 line (LoVo 0.0607×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD83]] (+0.57, fdr 3e-05), [[ZDHHC23]] (+0.56, fdr 1e-05), [[TSPAN2]] (+0.56, fdr 1e-05); moves opposite to [[MEF2B]] (-0.53, fdr 2e-04), [[SENP5]] (-0.48, fdr 4e-05), [[YIPF1]] (-0.47, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RASGRF1]] → it (grade B ⚠); 2 go from it, the strongest it → [[LGALS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4017.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.73×** | +19.1 | 0e+00 | 17/22 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.65×** | +17.8 | 0e+00 | 11/14 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.37×** | +17.6 | 0e+00 | 20/23 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.71×** | +17.2 | 0e+00 | 7/7 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.06×** | +13.3 | 3e-38 | 6/8 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +10.4 | 3e-23 | 22/30 (LoVo, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.50×** | +9.4 | 6e-19 | 17/24 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.26×** | +8.0 | 7e-14 | 17/26 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.15×** | +7.9 | 3e-13 | 16/27 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +7.2 | 3e-11 | 10/17 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.82×** | +6.1 | 5e-08 | 13/31 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.0 | 1e-07 | 6/30 (NCI-H2347, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.77×** | +5.9 | 2e-07 | 3/16 (Hs 766T, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.9 | 4e-05 | 3/18 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.61×** | +4.9 | 4e-05 | 9/30 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +4.9 | 4e-05 | 2/30 (NCI-H2347, NCI-H23) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +4.6 | 1e-04 | 6/30 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +4.2 | 7e-04 | 3/28 (NCI-H23, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.004 | 12/30 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.5 | 0.013 | 2/16 (NCI-H1792, LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.015 | 9/30 (SW 900, Hs 766T, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.1 | 0.039 | 6/29 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +2.8 | 0.095 | 7/29 (AsPC-1, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4017.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Naproxen (drug)]] 0.05 µM in 1 line (LoVo 0.0607×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 0.5 µM |  | 0.734× | -3.2 | 0.65 | 5/28 (Hs 766T, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4017. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.12 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +10.7) | — |
| [[A549 (line)]] | wt | 12.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.44× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.50× (z +9.4) | — |
| [[A498 (line)]] | wt | 6.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +10.8) | — |
| [[LoVo (line)]] | wt | 3.46 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0607× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 12.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.31× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 2.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.18× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 2.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +9.1) | — |
| [[A-172 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.739 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.556 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4017), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD83]] | +0.57 | +0.46 / +0.64 | both halves | 3e-05 | same gene group |
| [[ZDHHC23]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TSPAN2]] | +0.56 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[TSPAN15]] | +0.56 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.54 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[ABLIM1]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[SLCO2B1]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 | pathway: Drug ADME; STRING 775 |
| [[RARG]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[GATM]] | +0.52 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[RASGRP1]] | +0.52 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[SERTAD4]] | +0.52 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[NTRK2]] | +0.52 | +0.37 / +0.55 | both halves | 8e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEF2B]] | -0.53 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[SENP5]] | -0.48 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[YIPF1]] | -0.47 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[SDF2]] | -0.47 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[BFAR]] | -0.47 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[GBA2]] | -0.46 | -0.48 / -0.40 | both halves | 5e-05 | pathway: Sphingolipid metabolism |
| [[ZNF500]] | -0.46 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[HERC2P3]] | -0.46 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[FAM83A]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[C19orf25]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ACOX3]] | -0.46 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[GPR89A]] | -0.46 | -0.43 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGRF1]] | B | RASGRF1 activity lowers ABCG2's level | lines that do not express RASGRF1 (18) vs lines expressing it (32) | 1.72× higher at baseline in the lines without RASGRF1 | 0.026 | ⚠ within organs, on part of the lines; also absent: RORC, MIR4280HG, TMEM40; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ABCG2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ALDH3A1]] | B | ALDH3A1 activity raises ABCG2's level | lines that do not express ALDH3A1 (36) vs lines expressing it (14) | 1.50× lower at baseline in the lines without ALDH3A1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS3]] | B | ABCG2 activity raises LGALS3's level | lines that do not express ABCG2 (15) vs lines expressing it (35) | 2.34× lower at baseline in the lines without ABCG2 | 0.086 | ⚠ within organs, on part of the lines; also absent: C1R, GBP4, CDK18; maybe low, not absent |
| [[STAT5A]] | B | ABCG2 activity raises STAT5A's level | lines that do not express ABCG2 (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without ABCG2 | 0.088 | ⚠ within organs, on part of the lines; also absent: C1R, GBP4, CDK18; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.3, 10.6); signed map (47.2, 5.2). **Vector** length 49.9, 8.86% of its response variance represented; |z| ≥ 3 in 677 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +17.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +17.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +13.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +0.6 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -1.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily G member 2 (JR blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:88,090,150-88,231,628 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EST157481, MXR, BCRP, ABCP, CD338 |
| Gene groups (HGNC) | Blood group antigens; CD molecules; ATP binding cassette subfamily G |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 19 pathways, smallest: Ciprofloxacin ADME; Abacavir transmembrane transport; Abacavir ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNQ0](https://www.uniprot.org/uniprotkb/Q9UNQ0) (Broad substrate specificity ATP-binding cassette transporter ABCG2):

> Broad substrate specificity ATP-dependent transporter of the ATP-binding cassette (ABC) family that actively extrudes a wide variety of physiological compounds, dietary toxins and xenobiotics from cells. Involved in porphyrin homeostasis, mediating the export of protoporphyrin IX (PPIX) from both mitochondria to cytosol and cytosol to extracellular space, it also functions in the cellular export of heme. Also mediates the efflux of sphingosine-1-P from cells. Acts as a urate exporter …

**Summary**, from NCBI Gene [9429](https://www.ncbi.nlm.nih.gov/gene/9429):

> The membrane-associated protein encoded by this gene is included in the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the White subfamily. Alternatively referred to as a breast cancer resistance protein, this protein functions as a xenobiotic transporter which may play a …

**Accessions** — [HGNC:74](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:74) · Entrez [9429](https://www.ncbi.nlm.nih.gov/gene/9429) · UniProt [Q9UNQ0](https://www.uniprot.org/uniprotkb/Q9UNQ0) · Ensembl [ENSG00000118777](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118777)

## Data

Gene col 4017: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4017); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4017, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4017]; `tensor/DDL_lfc|DDL_z.npy` [4017]; `embed/gene_vectors.npy` [4017]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4017 or target_col == 4017). Every well: [[ABCG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
