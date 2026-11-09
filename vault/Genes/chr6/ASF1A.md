---
symbol: "ASF1A"
type: "gene"
col: 3297
ensembl_id: "ENSG00000111875"
name: "anti-silencing function 1A histone chaperone"
location: "6q22.31"
module: 16
arm: "+"
pooled_cpm: 10.1
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ASF1A

*anti-silencing function 1A histone chaperone* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.82× (z +18.8, q 0e+00, up in 42 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (NCI-H2030 0.128×, PANC-1 0.258×, HepG2/C3A 0.0755×, Hs 766T 0.0786×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 0.136×, SW1417 0.177×, KATO III 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.132×, KATO III 0.182×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Naproxen (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.103×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7]] (+0.74, fdr 7e-06), [[METTL18]] (+0.74, fdr 7e-06), [[ERCC4]] (+0.73, fdr 7e-06); moves opposite to [[PMS2P3-1]] (-0.63, fdr 1e-05), [[BCL7C]] (-0.63, fdr 1e-05), [[CD81]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TLR6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CLCN3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3297.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.82×** | +18.8 | 0e+00 | 42/43 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.38×** | +15.6 | 0e+00 | 41/42 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.96×** | +13.4 | 1e-38 | 43/45 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.15×** | +9.8 | 1e-20 | 38/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +7.4 | 2e-11 | 32/47 (J82, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.68×** | +6.7 | 2e-09 | 30/47 (LoVo, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +6.4 | 1e-08 | 27/46 (LoVo, LS 180, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.61×** | +6.1 | 8e-08 | 22/39 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.60×** | +6.1 | 9e-08 | 28/47 (LoVo, J82, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.59×** | +6.0 | 1e-07 | 15/36 (NCI-H1792, J82, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +5.6 | 1e-06 | 21/46 (LoVo, HT-29, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.56×** | +5.5 | 2e-06 | 8/22 (A498, NCI-H2347, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +5.5 | 2e-06 | 27/45 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.5 | 2e-06 | 19/48 (HEC-1-A, BT-474, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +5.2 | 6e-06 | 18/46 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +4.4 | 3e-04 | 16/47 (LoVo, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +4.4 | 3e-04 | 17/45 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +4.1 | 0.001 | 7/47 (SW480, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.003 | 9/46 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.027 | 3/47 (NCI-H2030, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3297.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (NCI-H2030 0.128×, PANC-1 0.258×, HepG2/C3A 0.0755×, Hs 766T 0.0786×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 0.136×, SW1417 0.177×, KATO III 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.132×, KATO III 0.182×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Naproxen (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.103×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.896× | -4.7 | 0.002 | 8/48 (HT-29, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.769× | -3.3 | 0.17 | 17/45 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.771× | -3.3 | 0.17 | 10/46 (NCI-H2030, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3297. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[NCI-H2030 (line)]] | alt | 16.3 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.128× (z -12.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 19.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 18.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0755× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Naproxen (drug)]] 0.05 µM 0.103× (z -9.0) |
| [[PANC-1 (line)]] | alt | 15.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.258× (z -11.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 6.28 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0786× (z -10.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +9.3) | — |
| [[LoVo (line)]] | wt | 6.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +10.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.10 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.81× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[A-172 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3297), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7]] | +0.74 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[METTL18]] | +0.74 | +0.81 / +0.65 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.73 | +0.81 / +0.61 | both halves | 7e-06 |  |
| [[UBQLN2]] | +0.71 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[ZNF155]] | +0.71 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[THAP5]] | +0.71 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.68 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[RTL6]] | +0.67 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[GSPT2]] | +0.67 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[ZBTB6]] | +0.66 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.65 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[TRIM16L-1]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P3-1]] | -0.63 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[BCL7C]] | -0.63 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[CD81]] | -0.60 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[CERS5]] | -0.59 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[ZNF710-AS1]] | -0.59 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SMG1P5]] | -0.59 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[PMPCA]] | -0.59 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[SEC11A]] | -0.59 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[SHQ1]] | -0.59 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[ATP6AP2]] | -0.58 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[SPATA33]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[NME2]] | -0.58 | -0.70 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLR6]] | B | TLR6 activity lowers ASF1A's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 1.51× higher at baseline in the lines without TLR6 | 0.091 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLCN3]] | C | ASF1A's natural level weakens CLCN3's drug response | ASF1A's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.17; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.3, 8.1); signed map (1.7, -22.9). **Vector** length 80.0, 15.2% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +13.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +15.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +18.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +5.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.7 | +2.4 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.9 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.5 | -0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.3 | +5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | -3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +2.2 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.4 | -1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | anti-silencing function 1A histone chaperone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31 — chr6:118,894,152-118,909,171 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP547E2110, CIA |
| Hallmark sets | E2F_TARGETS |
| Reactome | 5 pathways, smallest: Formation of Senescence-Associated Heterochromatin Foci (SAHF); DNA Damage/Telomere Stress Induced Senescence; Cellular Senescence |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y294](https://www.uniprot.org/uniprotkb/Q9Y294) (Histone chaperone ASF1A):

> Histone chaperone that facilitates histone deposition and histone exchange and removal during nucleosome assembly and disassembly. Cooperates with chromatin assembly factor 1 (CAF-1) to promote replication-dependent chromatin assembly and with HIRA to promote replication-independent chromatin assembly. Promotes homologous recombination-mediated repair of double-strand breaks (DSBs) at stalled or collapsed replication forks: acts by mediating histone replacement at DSBs, leading to recruitment …

**Summary**, from NCBI Gene [25842](https://www.ncbi.nlm.nih.gov/gene/25842):

> This gene encodes a member of the H3/H4 family of histone chaperone proteins and is similar to the anti-silencing function-1 gene in yeast. The protein is a key component of a histone donor complex that functions in nucleosome assembly. It interacts with histones H3 and H4, and functions together with a chromatin assembly factor during DNA replication and repair. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20995) · Entrez [25842](https://www.ncbi.nlm.nih.gov/gene/25842) · UniProt [Q9Y294](https://www.uniprot.org/uniprotkb/Q9Y294) · Ensembl [ENSG00000111875](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111875)

## Data

Gene col 3297: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3297); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3297, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3297]; `tensor/DDL_lfc|DDL_z.npy` [3297]; `embed/gene_vectors.npy` [3297]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3297 or target_col == 3297). Every well: [[ASF1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASF1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
