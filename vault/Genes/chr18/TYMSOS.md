---
symbol: "TYMSOS"
type: "gene"
col: 10765
ensembl_id: "ENSG00000176912"
name: "TYMS opposite strand RNA"
location: "18p11.32"
module: 62
arm: "+"
pooled_cpm: 4.86
n_lines_expressing: 47
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 7
direction_downstream: 7
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# TYMSOS

*TYMS opposite strand RNA* — 18p11.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.95× (z +22.7, q 0e+00, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.464× (z -7.0, q 2e-09, down in 23 of 43 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTA2]] (+0.76, fdr 7e-06), [[FAS]] (+0.71, fdr 3e-05), [[EFCAB5]] (+0.70, fdr 1e-05); moves opposite to [[STUB1]] (-0.60, fdr 0.005, ⚠ one half only (not replicated)), [[SH3PXD2B]] (-0.58, fdr 8e-04, ⚠ one half only (not replicated)), [[SMYD3]] (-0.57, fdr 6e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[ACER2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10765.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.95×** | +22.7 | 0e+00 | 37/38 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.18×** | +14.3 | 1e-43 | 29/31 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.76×** | +11.5 | 4e-28 | 31/33 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.56×** | +11.4 | 4e-28 | 18/22 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.33×** | +10.4 | 2e-23 | 5/5 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +8.1 | 5e-14 | 8/12 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +7.4 | 1e-11 | 18/37 (NCI-H23, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.78×** | +7.3 | 2e-11 | 22/43 (A498, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.7 | 1e-04 | 15/26 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +4.3 | 0.001 | 7/27 (J82, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.002 | 13/43 (H4, A-172, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.012 | 8/42 (A-172, HT-29, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.54×** | +3.6 | 0.014 | 6/30 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.036 | 9/41 (A498, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.098 | 7/41 (A-172, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10765.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.464×** | -7.0 | 2e-09 | 23/43 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.512×** | -6.1 | 3e-07 | 19/41 (H4, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.499×** | -6.0 | 5e-07 | 23/40 (A-172, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.559×** | -5.3 | 2e-05 | 17/42 (NCI-H23, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.617×** | -4.4 | 0.001 | 18/43 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.649×** | -3.8 | 0.014 | 10/41 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.663×** | -3.8 | 0.014 | 16/42 (LoVo, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.687×** | -3.4 | 0.044 | 12/43 (SNU-1, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | 0.720× | -3.0 | 0.17 | 15/43 (Panc 03.27, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10765. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 3.66 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 32.2× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 4.29 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.63× (z +13.5) | — |
| [[A-172 (line)]] | wt | 7.32 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.74× (z +10.4) | [[Mozavaptan (drug)]] 5 µM 0.0788× (z -9.4) |
| [[A498 (line)]] | wt | 6.37 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.80× (z +12.4) | — |
| [[HepG2_C3A (line)]] | wt | 8.94 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.44× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.0721× (z -8.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 5.26 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.101× (z -8.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 7.44 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +12.7) | — |
| [[LOX-IMVI (line)]] | wt | 4.53 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.14× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 6.34 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.43× (z +9.8) | [[Ixazomib citrate (drug)]] 5 µM 0.0534× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 5.64 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 7.72 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.183× (z -9.9) |
| [[SW480 (line)]] | alt | 5.08 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.98× (z +10.0) | — |
| [[A549 (line)]] | wt | 7.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.30× (z +10.8) | — |
| [[C32 (line)]] | wt | 4.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.44× (z +9.2) | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0411× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 6.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 2.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.5× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.67 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 5.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.61× (z +10.1) | — |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.996 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10765), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTA2]] | +0.76 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[FAS]] | +0.71 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[EFCAB5]] | +0.70 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[DDB2]] | +0.67 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[SPATA18]] | +0.67 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CPEB2-DT]] | +0.67 | +0.68 / +0.35 | both halves | 1e-04 |  |
| [[SEPTIN7-DT]] | +0.67 | +0.72 / +0.35 | both halves | 1e-04 |  |
| [[DNAI3]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[INKA2]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.65 | +0.68 / +0.39 | both halves | 5e-05 |  |
| [[RAD9B]] | +0.65 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[NEK8]] | +0.64 | +0.69 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | -0.60 | -0.50 / -0.04 | ⚠ one half (not replicated) | 0.005 |  |
| [[SH3PXD2B]] | -0.58 | -0.60 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[SMYD3]] | -0.57 | -0.53 / -0.22 | both halves | 6e-04 |  |
| [[ST6GALNAC4]] | -0.57 | -0.53 / -0.12 | ⚠ one half (not replicated) | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TYMSOS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PURPL]] | B | PURPL activity raises TYMSOS's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without PURPL | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[GREB1]] | B | GREB1 activity raises TYMSOS's level | lines that do not express GREB1 (6) vs lines expressing it (44) | 2.10× lower at baseline in the lines without GREB1 | 0.032 | ⚠ within organs, on part of the lines; also absent: PRKN, SLC17A7, ENSG00000232855; maybe low, not absent |
| [[PINCR]] | B | PINCR activity strengthens TYMSOS's drug response | lines that do not express PINCR (25) vs lines expressing it (18) | the lines without PINCR respond 0.84× as strongly (z diff +0.58); strongest at Mitoxantrone (dihydrochloride) 5 µM: 1.42x vs 1.94x (z diff +2.1) | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[LIF-AS2]] | B | LIF-AS2 activity lowers TYMSOS's level | lines that do not express LIF-AS2 (13) vs lines expressing it (37) | 1.55× higher at baseline in the lines without LIF-AS2 | 0.081 | ⚠ within organs, on part of the lines; also absent: STING1, CFB; maybe low, not absent |
| [[PURPL]] | B | PURPL activity strengthens TYMSOS's drug response | lines that do not express PURPL (20) vs lines expressing it (23) | the lines without PURPL respond 0.82× as strongly (z diff +0.88); strongest at Mitoxantrone (dihydrochloride) 5 µM: 1.47x vs 1.76x (z diff +1.7) | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1; target measured in part of the lines; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises TYMSOS's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACER2]] | C | TYMSOS activity raises ACER2's level | lines that do not express TYMSOS (3) vs lines expressing it (47) | 2.29× lower at baseline in the lines without TYMSOS | 0.024 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: FOXP4-AS1, ENSG00000261341, CCNP; maybe low, not absent |
| [[XPC]] | C | TYMSOS activity raises XPC's level | lines that do not express TYMSOS (3) vs lines expressing it (47) | 2.11× lower at baseline in the lines without TYMSOS | 0.041 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: FOXP4-AS1, ENSG00000261341, CCNP; maybe low, not absent |
| [[ZMAT3]] | C | TYMSOS activity raises ZMAT3's level | lines that do not express TYMSOS (3) vs lines expressing it (47) | 4.23× lower at baseline in the lines without TYMSOS | 0.047 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: FOXP4-AS1, ENSG00000261341, CCNP; maybe low, not absent; co-absent with the target |
| [[BAX]] | C | TYMSOS activity raises BAX's level | lines that do not express TYMSOS (3) vs lines expressing it (47) | 2.01× lower at baseline in the lines without TYMSOS | 0.051 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: FOXP4-AS1, ENSG00000261341, CCNP; maybe low, not absent |
| [[FBXO22]] | C | TYMSOS activity raises FBXO22's level | lines that do not express TYMSOS (3) vs lines expressing it (47) | 1.77× lower at baseline in the lines without TYMSOS | 0.079 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: FOXP4-AS1, ENSG00000261341, CCNP; maybe low, not absent |
| [[TRAF3IP2-AS1]] | C | TYMSOS activity raises TRAF3IP2-AS1's level | lines that do not express TYMSOS (3) vs lines expressing it (47) | 2.49× lower at baseline in the lines without TYMSOS | 0.099 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: FOXP4-AS1, ENSG00000261341, CCNP; maybe low, not absent |
| [[POLH]] | C | TYMSOS activity raises POLH's level | lines that do not express TYMSOS (3) vs lines expressing it (47) | 1.84× lower at baseline in the lines without TYMSOS | 0.099 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: FOXP4-AS1, ENSG00000261341, CCNP; maybe low, not absent |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.6, 35.7); signed map (41.2, -22.7). **Vector** length 78.2, 15.1% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 targets up* (control, mean cos +0.52 to 26).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +22.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +14.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +7.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +3.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.1 | -7.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.5 | -3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.5 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | TYMS opposite strand RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 18p11.32 — chr18:630,886-658,350 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C18orf56 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

UniProt [Q8TAI1](https://www.uniprot.org/uniprotkb/Q8TAI1) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29553](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29553) · Entrez [494514](https://www.ncbi.nlm.nih.gov/gene/494514) · UniProt [Q8TAI1](https://www.uniprot.org/uniprotkb/Q8TAI1) · Ensembl [ENSG00000176912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176912)

## Data

Gene col 10765: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10765); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10765, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10765]; `tensor/DDL_lfc|DDL_z.npy` [10765]; `embed/gene_vectors.npy` [10765]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10765 or target_col == 10765). Every well: [[TYMSOS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TYMSOS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
