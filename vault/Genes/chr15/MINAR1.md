---
symbol: "MINAR1"
type: "gene"
col: 9796
ensembl_id: "ENSG00000169330"
name: "membrane integral NOTCH2 associated receptor 1"
location: "15q25.1"
module: 49
arm: "+"
pooled_cpm: 4.86
n_lines_expressing: 46
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# MINAR1

*membrane integral NOTCH2 associated receptor 1* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.66× (z +9.0, q 2e-16, up in 2 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.20× (z +7.5, q 2e-11, up in 27 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.448× (z -7.3, q 1e-10, down in 23 of 38 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.552× (z -5.6, q 3e-06, down in 15 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED3]] (+0.71, fdr 7e-06, ⚠ read-through risk), [[CDRT4]] (+0.64, fdr 1e-05), [[ZNF587]] (+0.59, fdr 1e-05), [[APRG1]] (+0.58, fdr 2e-05); moves opposite to [[TERF1]] (-0.52, fdr 2e-05), [[PLPP1]] (-0.48, fdr 3e-05), [[COX20]] (-0.46, fdr 3e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ANKFN1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9796.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +9.0 | 2e-16 | 2/8 (RPMI-7951, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.20×** | +7.5 | 2e-11 | 27/38 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.7 | 5e-04 | 7/43 (NCI-H1573, SW48, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.52×** | +4.0 | 0.010 | 4/38 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +3.9 | 0.010 | 1/10 (NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +3.9 | 0.010 | 15/41 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +3.4 | 0.053 | 2/22 (NCI-H2030, LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.28×** | +3.3 | 0.070 | 9/41 (A549, A498, …) | top dose only | low cells (technical?) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.095 | 6/38 (RPMI-7951, C32, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.37× | +3.0 | 0.14 | 6/36 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9796.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.448×** | -7.3 | 1e-10 | 23/38 (LoVo, H4, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.581×** | -7.3 | 1e-10 | 26/34 (A498, HS-578T, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.511×** | -6.4 | 4e-08 | 21/34 (LoVo, hTERT-HPNE, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.552×** | -5.6 | 3e-06 | 15/39 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.552×** | -5.4 | 7e-06 | 16/24 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -5.1 | 4e-05 | 18/34 (LoVo, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.598×** | -4.9 | 9e-05 | 19/43 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.397×** | -4.6 | 3e-04 | 16/37 (LoVo, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.630×** | -4.4 | 7e-04 | 16/39 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.632×** | -4.3 | 8e-04 | 16/40 (LoVo, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.670×** | -3.8 | 0.008 | 12/42 (LoVo, COLO 205, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.706×** | -3.2 | 0.073 | 6/40 (NCI-H2347, HepG2/C3A, …) | top dose only | plate-row cell shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.718×** | -3.1 | 0.077 | 10/41 (H4, NCI-H460, …) | rises with dose |  |
| [[5-Fluorouracil (drug)]] 5 µM |  | **0.723×** | -3.1 | 0.089 | 4/41 (RKO, AN3 CA, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 24.3 | 0 | 11 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -17.4) |
| [[H4 (line)]] | wt | 19.7 | 0 | 3 (2 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0914× (z -9.8) |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0418× (z -14.7) ⚠ cell-cycle shift, explains ~86% of this change |
| [[A498 (line)]] | wt | 12.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -15.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H23 (line)]] | alt | 5.14 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0632× (z -9.7) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Cyclosporin A (drug)]] 0.5 µM 0.0719× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0576× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 2.51 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0761× (z -9.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[COLO 205 (line)]] | alt | 6.14 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0478× (z -9.2) ⚠ cell-cycle shift, explains ~75% of this change |
| [[HEC-1-A (line)]] | alt | 3.79 | 0 | 1 | — | [[Dimethyl fumarate (drug)]] 0.05 µM 0.0738× (z -8.6) |
| [[KATO III (line)]] | alt | 6.29 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -8.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.335 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED3]] | +0.71 | +0.65 / +0.78 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 4.9 kb 3′ of TMED3 on the same strand (can correlate by spillover, not regulation) |
| [[CDRT4]] | +0.64 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[ZNF587]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[APRG1]] | +0.58 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[CORIN]] | +0.57 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[CUTC]] | +0.57 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[FAM98A]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[GABRR2]] | +0.56 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[LRRC59]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TICAM2]] | +0.55 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[SND1]] | +0.55 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[LINC02804]] | +0.54 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[LINC02885]] | +0.54 | +0.35 / +0.60 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF1]] | -0.52 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[PLPP1]] | -0.48 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[COX20]] | -0.46 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[TMEM107]] | -0.45 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[CEP68]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[RCOR3]] | -0.45 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[CCDC24]] | -0.45 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[GAB1]] | -0.45 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[TTC21B]] | -0.44 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[PHF21A]] | -0.44 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[EZH1]] | -0.43 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKFN1]] | B | ANKFN1 activity raises MINAR1's level | lines that do not express ANKFN1 (8) vs lines expressing it (42) | 2.25× lower at baseline in the lines without ANKFN1 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000214803, LINC00298; maybe low, not absent |
| [[DDR2]] | B | DDR2 activity raises MINAR1's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.72× lower at baseline in the lines without DDR2 | 0.067 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[SERP1]] | C | SERP1's natural level strengthens MINAR1's drug response | SERP1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.70, reverse -0.30; direction not clear | 0.031 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[TMED3]] | C | TMED3's natural level strengthens MINAR1's drug response | TMED3's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.59; direction not clear | 0.037 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[IL20RB]] | C | IL20RB's natural level strengthens MINAR1's drug response | IL20RB's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.36; direction not clear | 0.068 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | MINAR1's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | MINAR1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.440 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.424). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.9, -33.5); signed map (8.6, 9.4). **Vector** length 70.9, 12.2% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +7.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +2.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.6 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | membrane integral NOTCH2 associated receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:79,432,336-79,472,304 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBTOR; previously KIAA1024 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPX6](https://www.uniprot.org/uniprotkb/Q9UPX6) (Major intrinsically disordered Notch2-binding receptor 1):

> Intrinsically disordered protein which may negatively regulate mTOR signaling pathway by stabilizing the mTOR complex component DEPTOR. Negatively regulates angiogenesis. Negatively regulates cell growth. Negatively regulates neurite outgrowth in hippocampal neurons (By similarity).

**Summary**, from NCBI Gene [23251](https://www.ncbi.nlm.nih.gov/gene/23251):

> Involved in several processes, including negative regulation of TOR signaling; negative regulation of angiogenesis; and negative regulation of protein ubiquitination. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29172) · Entrez [23251](https://www.ncbi.nlm.nih.gov/gene/23251) · UniProt [Q9UPX6](https://www.uniprot.org/uniprotkb/Q9UPX6) · Ensembl [ENSG00000169330](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169330)

## Data

Gene col 9796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9796); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9796]; `tensor/DDL_lfc|DDL_z.npy` [9796]; `embed/gene_vectors.npy` [9796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9796 or target_col == 9796). Every well: [[MINAR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MINAR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
