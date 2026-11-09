---
symbol: "FRG1HP"
type: "gene"
col: 15872
ensembl_id: "ENSG00000276291"
name: "FSHD region gene 1 family member H, pseudogene"
location: "9p11.2"
module: 15
arm: "+"
pooled_cpm: 35.2
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# FRG1HP

*FSHD region gene 1 family member H, pseudogene* — 9p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.53× (z +8.5, q 1e-14, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.58× (z +6.4, q 4e-08, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.489× (z -10.0, q 1e-20, down in 42 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.465× (z -5.6, q 2e-06, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00115]] (+0.71, fdr 7e-06), [[CCNY-AS1]] (+0.69, fdr 7e-06), [[VPS13B-DT]] (+0.65, fdr 7e-06); moves opposite to [[JUN]] (-0.49, fdr 4e-05), [[CRYBG1]] (-0.48, fdr 4e-05), [[FAM222A]] (-0.48, fdr 5e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF529-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.53×** | +8.5 | 1e-14 | 40/48 (RKO, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +6.4 | 4e-08 | 37/48 (SHP-77, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +6.4 | 4e-08 | 41/48 (SHP-77, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +5.1 | 4e-05 | 31/48 (SW48, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.3 | 0.002 | 23/47 (HS-578T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.34×** | +4.1 | 0.004 | 25/48 (J82, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.005 | 23/48 (SW1417, SW48, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.009 | 20/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **1.29×** | +3.5 | 0.033 | 21/47 (Panc 03.27, KATO III, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.11 | 13/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15872.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.489×** | -10.0 | 1e-20 | 42/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.590×** | -7.4 | 6e-11 | 36/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.594×** | -7.0 | 6e-10 | 33/48 (HOP62, NCI-H1792, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.651×** | -6.0 | 3e-07 | 27/47 (RKO, NCI-H23, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.668×** | -5.6 | 2e-06 | 29/47 (SW480, SW 1271, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.465×** | -5.6 | 2e-06 | 38/48 (LOX-IMVI, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.680×** | -5.4 | 6e-06 | 29/48 (A498, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.693×** | -5.1 | 2e-05 | 26/48 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.505×** | -5.0 | 4e-05 | 33/47 (LS 180, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.510×** | -4.9 | 5e-05 | 29/47 (A498, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.702×** | -4.7 | 1e-04 | 21/36 (SW480, SNU-423, …) | two highest doses | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.527×** | -4.7 | 1e-04 | 30/46 (H4, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.703×** | -4.4 | 5e-04 | 24/48 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **0.730×** | -4.2 | 1e-03 | 26/45 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.716×** | -4.2 | 0.001 | 26/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.575×** | -4.0 | 0.002 | 24/47 (SNU-1, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.580×** | -4.0 | 0.002 | 21/47 (Hs 766T, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.680×** | -3.8 | 0.004 | 21/48 (SHP-77, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.714×** | -3.4 | 0.024 | 17/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.780×** | -3.3 | 0.032 | 22/48 (CFPAC-1, SNU-1, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.722×** | -3.2 | 0.033 | 15/48 (AsPC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 50.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 81.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -16.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 43.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 45.5 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -11.3) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H460 (line)]] | wt | 34.8 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.342× (z -9.6) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 52.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.49× (z +10.3) ⚠ cell-cycle shift, explains ~55% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[SW 1271 (line)]] | alt | 68.2 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0639× (z -9.0) ⚠ cell-cycle shift, explains ~72% of this change |
| [[SW480 (line)]] | alt | 54.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[CFPAC-1 (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.13× (z +8.5) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[COLO 205 (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[hTERT-HPNE (line)]] | wt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[J82 (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.243× (z -9.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H23 (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[Panc 03.27 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[PANC-1 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 47.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.251× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~52% of this change |
| [[A-172 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00115]] | +0.71 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[CCNY-AS1]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[VPS13B-DT]] | +0.65 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[C8orf44-SGK3]] | +0.64 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[NUDT16-DT]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[H3-3A-DT]] | +0.61 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[SLC28A2-AS1]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ING4]] | +0.59 | +0.35 / +0.67 | both halves | 1e-04 |  |
| [[LINC01772]] | +0.59 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[FRG1DP]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[MED21]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[ZBTB26]] | +0.58 | +0.45 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUN]] | -0.49 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[CRYBG1]] | -0.48 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[FAM222A]] | -0.48 | -0.50 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF529-AS1]] | B | ZNF529-AS1 activity raises FRG1HP's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 1.55× lower at baseline in the lines without ZNF529-AS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |
| [[HDAC6]] | B | HDAC6 activity lowers FRG1HP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-7.7, 24.1); signed map (1.6, -1.0). **Vector** length 87.7, 20.7% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +6.7 | +8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | +5.7 | +3.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +3.9 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +1.5 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +2.8 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.8 | -0.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -10.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -4.5 | -7.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.2 | -4.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | +0.1 |
|  | [[EX229 (drug)]] 5 µM |  | -3.8 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | FSHD region gene 1 family member H, pseudogene |
| Locus type | pseudogene |
| Location | 9p11.2 — chr9:40,992,426-41,218,410 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51767](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51767) · Entrez [100132352](https://www.ncbi.nlm.nih.gov/gene/100132352) · Ensembl [ENSG00000276291](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000276291)

## Data

Gene col 15872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15872); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15872]; `tensor/DDL_lfc|DDL_z.npy` [15872]; `embed/gene_vectors.npy` [15872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15872 or target_col == 15872). Every well: [[FRG1HP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRG1HP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
