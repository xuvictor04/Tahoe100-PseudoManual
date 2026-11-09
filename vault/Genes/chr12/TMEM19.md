---
symbol: "TMEM19"
type: "gene"
col: 6288
ensembl_id: "ENSG00000139291"
name: "fatty acid amide binding transmembrane protein"
location: "12q21.1"
module: 29
arm: "+"
pooled_cpm: 11.97
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# TMEM19

*fatty acid amide binding transmembrane protein* — 12q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.81× (z +18.1, q 0e+00, up in 19 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.43× (z +4.1, q 0.006, up in 16 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.483× (z -12.4, q 3e-32, down in 34 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGK]] (+0.63, fdr 1e-05), [[BANF1]] (+0.62, fdr 1e-05), [[LBR]] (+0.62, fdr 1e-05); moves opposite to [[INAFM1]] (-0.64, fdr 1e-05), [[SNHG12]] (-0.63, fdr 1e-05), [[EPB41L4A-AS1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PTGFRN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6288.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.81×** | +18.1 | 0e+00 | 19/21 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.72×** | +15.7 | 0e+00 | 31/35 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.72×** | +11.1 | 3e-26 | 22/27 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.006 | 16/46 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.40×** | +4.1 | 0.006 | 15/48 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.37×** | +3.8 | 0.015 | 14/47 (HEC-1-A, A498, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.026 | 14/48 (RKO, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.034 | 11/48 (SW1417, A-172, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +3.4 | 0.037 | 16/48 (HEC-1-A, A-427, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.32×** | +3.3 | 0.046 | 14/38 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.051 | 7/47 (HepG2/C3A, NCI-H2030, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.21×** | +3.2 | 0.059 | 18/46 (BT-474, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.086 | 10/48 (A-172, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6288.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.483×** | -12.4 | 3e-32 | 34/44 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.483×** | -8.7 | 7e-16 | 29/44 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.629×** | -5.6 | 5e-06 | 21/47 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.646×** | -5.3 | 2e-05 | 24/47 (LoVo, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.648×** | -5.2 | 2e-05 | 22/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.765×** | -4.6 | 5e-04 | 23/48 (SW 900, HEC-1-A, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.491×** | -4.5 | 6e-04 | 19/45 (LS 180, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.693×** | -4.4 | 7e-04 | 21/45 (PANC-1, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.526×** | -4.0 | 0.003 | 14/46 (C-33 A, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.722×** | -3.8 | 0.009 | 17/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.738×** | -3.7 | 0.013 | 13/47 (SK-MEL-2, PANC-1, …) | two highest doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.762×** | -3.1 | 0.080 | 11/47 (NCI-H1573, Panc 03.27, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.778× | -3.0 | 0.11 | 16/47 (AN3 CA, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6288. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 27.4 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +15.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -16.7) |
| [[LoVo (line)]] | wt | 22.3 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -18.8) |
| [[NCI-H460 (line)]] | wt | 10.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.159× (z -11.6) |
| [[A498 (line)]] | wt | 10.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.84× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -11.5) |
| [[A-172 (line)]] | wt | 9.59 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.4× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 12.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.91× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 31.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -10.1) |
| [[A-427 (line)]] | wt | 36.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -18.3) |
| [[C-33 A (line)]] | alt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 5.09 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0901× (z -9.3) |
| [[COLO 205 (line)]] | alt | 6.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0528× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 11.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -9.0) |
| [[HOP62 (line)]] | alt | 8.65 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 6.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 9.80 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +8.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 9.70 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.66× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 4.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0710× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0487× (z -20.7) |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.234× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 7.27 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.56× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6288), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGK]] | +0.63 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[BANF1]] | +0.62 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[LBR]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[CDKN2AIPNL]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[EMB]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ICMT]] | +0.59 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[HNRNPA3]] | +0.58 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[VMA21]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[FOXM1]] | +0.56 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[FUCA2]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[STMP1]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[MAPRE1]] | +0.55 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INAFM1]] | -0.64 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[SNHG12]] | -0.63 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | -0.60 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[SNHG8]] | -0.59 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ZNF766]] | -0.57 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[ZNF415]] | -0.57 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ZRSR2]] | -0.56 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[SNHG7]] | -0.56 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[NKAP]] | -0.56 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[ARRDC2]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.55 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ZNF593]] | -0.55 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGFRN]] | B | PTGFRN activity lowers TMEM19's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 1.35× higher at baseline in the lines without PTGFRN | 0.071 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-39.2, -29.6); signed map (-23.1, -41.6). **Vector** length 74.8, 14.0% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +18.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +11.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | -1.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.1 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -12.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -8.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -1.7 | -4.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | fatty acid amide binding transmembrane protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.1 — chr12:71,686,082-71,705,047 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10936; previously TMEM19 |
| Matched by | ensembl_id |

UniProt [Q96HH6](https://www.uniprot.org/uniprotkb/Q96HH6) carries no function annotation.

**Summary**, from NCBI Gene [55266](https://www.ncbi.nlm.nih.gov/gene/55266):

> Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25605) · Entrez [55266](https://www.ncbi.nlm.nih.gov/gene/55266) · UniProt [Q96HH6](https://www.uniprot.org/uniprotkb/Q96HH6) · Ensembl [ENSG00000139291](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139291)

## Data

Gene col 6288: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6288); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6288, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6288]; `tensor/DDL_lfc|DDL_z.npy` [6288]; `embed/gene_vectors.npy` [6288]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6288 or target_col == 6288). Every well: [[TMEM19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
