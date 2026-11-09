---
symbol: "SLC35D1"
type: "gene"
col: 3826
ensembl_id: "ENSG00000116704"
name: "solute carrier family 35 member D1"
location: "1p31.3"
module: 186
arm: "+"
pooled_cpm: 28.55
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# SLC35D1

*solute carrier family 35 member D1* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.31× (z +4.3, q 0.007, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.692× (z -5.9, q 2e-06, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHPT1]] (+0.64, fdr 9e-06), [[DRAM2]] (+0.58, fdr 2e-05), [[PANK1]] (+0.57, fdr 1e-05); moves opposite to [[ZDHHC11]] (-0.54, fdr 2e-05), [[TTN-AS1]] (-0.54, fdr 3e-05), [[SSUH2]] (-0.53, fdr 1e-05).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SOBP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3826.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.007 | 22/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.007 | 23/48 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.015 | 16/47 (NCI-H460, C32, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.034 | 19/48 (SW48, C32, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.034 | 16/48 (A-172, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.059 | 18/48 (SW1417, Panc 03.27, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +3.4 | 0.062 | 20/46 (LS 180, LoVo, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.16× | +3.3 | 0.070 | 8/48 (LS 180, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.070 | 20/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.070 | 18/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.070 | 12/48 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.081 | 12/48 (C32, HT-29, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.21× | +3.0 | 0.10 | 11/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.0 | 0.10 | 16/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3826.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.692×** | -5.9 | 2e-06 | 25/48 (H4, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.717×** | -5.3 | 2e-05 | 27/48 (C32, AN3 CA, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.717×** | -5.3 | 2e-05 | 27/44 (C-33 A, C32, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.703×** | -5.2 | 3e-05 | 22/43 (NCI-H2030, J82, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.717×** | -5.1 | 3e-05 | 26/47 (NCI-H460, CHP-212, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.735×** | -4.9 | 7e-05 | 23/48 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.773×** | -4.0 | 0.006 | 18/37 (SHP-77, A-427, …) | all doses, flat | composition shift |
| [[Thymol (drug)]] 5 µM |  | 0.846× | -3.8 | 0.011 | 15/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.807×** | -3.3 | 0.059 | 15/48 (C32, LoVo, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -3.1 | 0.11 | 1/48 (HCT15) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.820× | -3.1 | 0.12 | 11/48 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 40.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -10.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 71.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.201× (z -8.6) |
| [[C-33 A (line)]] | alt | 41.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0959× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[C32 (line)]] | wt | 48.2 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.185× (z -12.4) |
| [[CHP-212 (line)]] | wt | 28.3 | 0 | 2 (1 ⚠) | — | [[Gemfibrozil (drug)]] 0.05 µM 0.0705× (z -9.7) |
| [[J82 (line)]] | alt | 23.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 24.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.312× (z -9.7) ⚠ toxic |
| [[A-427 (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 35.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.403× (z -8.5) |
| [[LoVo (line)]] | wt | 21.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 48.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 28.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[RPMI-7951 (line)]] | alt | 27.2 | 0 | 1 | — | [[CP21R7 (drug)]] 5 µM 0.0610× (z -9.0) |
| [[SHP-77 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW 900 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -9.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHPT1]] | +0.64 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[DRAM2]] | +0.58 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[PANK1]] | +0.57 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TM7SF3]] | +0.56 | +0.53 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[HOXA10]] | +0.56 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[RHOBTB1]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[USP46]] | +0.55 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[FGD1]] | +0.55 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[AKAP7]] | +0.54 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[POMZP3]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[RFX7]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[SMAD5]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC11]] | -0.54 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[TTN-AS1]] | -0.54 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SSUH2]] | -0.53 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[PITPNB]] | -0.51 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[LRGUK]] | -0.51 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[DNAH1]] | -0.50 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[BACH1]] | -0.50 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SMG1]] | -0.49 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[CDC37]] | -0.49 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[CFAP299]] | -0.49 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[TBILA]] | -0.49 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[RNF32-AS1]] | -0.48 | -0.46 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOBP]] | B | SOBP activity raises SLC35D1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.56× lower at baseline in the lines without SOBP | 0.041 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[RNF220]] | B | RNF220 activity raises SLC35D1's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 1.63× lower at baseline in the lines without RNF220 | 0.047 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[DZIP1L]] | B | DZIP1L activity raises SLC35D1's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without DZIP1L | 0.074 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[POMZP3]] | C | POMZP3's natural level strengthens SLC35D1's drug response | POMZP3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.08; direction not clear | 0.059 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[ANAPC1P4]] | C | ANAPC1P4 activity raises SLC35D1's level | lines that do not express ANAPC1P4 (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without ANAPC1P4 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP19, MIR4435-2HG, MSX1; maybe low, not absent |
| [[EOLA2-DT]] | C | EOLA2-DT's natural level weakens SLC35D1's drug response | EOLA2-DT's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.49; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.9, 15.5); signed map (-29.0, -18.5). **Vector** length 91.6, 19.7% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.9 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.9 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +1.9 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.3 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.0 | -5.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.7 | -4.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.2 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member D1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:66,999,350-67,054,148 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UGTREL7, KIAA0260 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Hallmark sets | XENOBIOTIC_METABOLISM, P53_PATHWAY |
| Reactome | 10 pathways, smallest: Formation of the active cofactor, UDP-glucuronate; Transport of nucleotide sugars; Glucuronidation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTN3](https://www.uniprot.org/uniprotkb/Q9NTN3) (Nucleotide sugar transporter SLC35D1):

> Antiporter that transports nucleotide sugars across the endoplasmic reticulum (ER) membrane in exchange for either their cognate nucleoside monophosphate or another nucleotide sugar. Transports various UDP-sugars including UDP-N-acetyl-alpha-D-glucosamine (UDP-GlcNAc), UDP-N-acetyl-alpha-D-galactosamine (UDP-GalNAc) and UDP-alpha-D-glucuronate (UDP-GlcA), which are used by ER glucosyltransferases as sugar donors for the synthesis of sugar chains of glycoproteins, glycolipids and …

**Summary**, from NCBI Gene [23169](https://www.ncbi.nlm.nih.gov/gene/23169):

> Glycosylation of cellular glycoconjugates occurs in the endoplasmic reticulum (ER) and Golgi compartment, and requires transport of nucleotide sugars from the cytosol into the lumen of the ER and Golgi by specific transporters. The protein encoded by this gene resides in the ER, and transports both UDP-glucuronic acid (UDP-GlcA) and UDP-N-acetylgalactosamine (UDP-GalNAc) from the cytoplasm to the ER lumen. It may participate in glucuronidation and/or chondroitin sulfate biosynthesis. Mutations …

**Accessions** — [HGNC:20800](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20800) · Entrez [23169](https://www.ncbi.nlm.nih.gov/gene/23169) · UniProt [Q9NTN3](https://www.uniprot.org/uniprotkb/Q9NTN3) · Ensembl [ENSG00000116704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116704)

## Data

Gene col 3826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3826); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3826]; `tensor/DDL_lfc|DDL_z.npy` [3826]; `embed/gene_vectors.npy` [3826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3826 or target_col == 3826). Every well: [[SLC35D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
