---
symbol: "SMIM3"
type: "gene"
col: 14985
ensembl_id: "ENSG00000256235"
name: "small integral membrane protein 3"
location: "5q33.1"
module: 54
arm: "+"
pooled_cpm: 18.56
n_lines_expressing: 39
n_dd_up: 1
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# SMIM3

*small integral membrane protein 3* — 5q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.43× (z +4.0, q 0.040, up in 15 of 34 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~39% of this change.
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.377× (z -15.3, q 0e+00, down in 29 of 34 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POP7]] (+0.62, fdr 4e-05), [[NCBP2AS2]] (+0.59, fdr 1e-04), [[MALSU1]] (+0.58, fdr 3e-05); moves opposite to [[ELK4]] (-0.53, fdr 3e-05), [[LIN7C]] (-0.50, fdr 1e-04), [[FLII]] (-0.50, fdr 2e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[RILPL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14985.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.43×** | +4.0 | 0.040 | 15/34 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.34× | +3.2 | 0.36 | 13/35 (SNU-423, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14985.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.377×** | -15.3 | 0e+00 | 29/34 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.322×** | -12.5 | 1e-33 | 29/37 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.530×** | -10.0 | 5e-21 | 24/34 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.442×** | -9.1 | 2e-17 | 26/36 (A-172, SW48, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.453×** | -8.8 | 2e-16 | 26/34 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.508×** | -7.5 | 6e-12 | 25/37 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.521×** | -7.0 | 3e-10 | 23/37 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.528×** | -6.8 | 7e-10 | 19/24 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.658×** | -4.6 | 2e-04 | 19/37 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.675×** | -4.3 | 8e-04 | 16/37 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.690×** | -4.1 | 0.002 | 21/27 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -3.9 | 0.005 | 19/34 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.785×** | -3.8 | 0.007 | 19/36 (A-172, AN3 CA, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -3.8 | 0.007 | 19/34 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.715×** | -3.7 | 0.008 | 18/36 (SW48, HCT15, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.659×** | -3.6 | 0.012 | 19/37 (A-172, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.758×** | -3.1 | 0.067 | 11/36 (SW48, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14985. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 53.9 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0526× (z -34.5) |
| [[LOX-IMVI (line)]] | wt | 51.3 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -20.2) |
| [[H4 (line)]] | wt | 63.5 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.0549× (z -18.6) |
| [[HS-578T (line)]] | alt | 65.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0690× (z -29.2) |
| [[hTERT-HPNE (line)]] | wt | 42.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -15.0) |
| [[SW48 (line)]] | wt | 79.0 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0389× (z -20.0) |
| [[AN3 CA (line)]] | alt | 78.0 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0506× (z -14.9) |
| [[HOP62 (line)]] | alt | 27.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0681× (z -25.2) |
| [[PANC-1 (line)]] | alt | 24.2 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -14.6) |
| [[A498 (line)]] | wt | 30.9 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0945× (z -18.8) |
| [[C32 (line)]] | wt | 43.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -22.2) |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0275× (z -15.1) |
| [[HCT15 (line)]] | alt | 43.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -15.7) |
| [[LS 180 (line)]] | wt | 60.7 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0822× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.104× (z -15.5) |
| [[RPMI-7951 (line)]] | alt | 42.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0607× (z -23.9) |
| [[CHP-212 (line)]] | wt | 40.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0573× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 6.31 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0880× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.211× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 26.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -14.9) |
| [[SNU-423 (line)]] | alt | 6.65 | 0 | 2 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0802× (z -9.2) |
| [[SW1417 (line)]] | alt | 38.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -9.4) |
| [[KATO III (line)]] | alt | 17.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -10.9) |
| [[RKO (line)]] | wt | 11.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -10.7) |
| [[A-427 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14985), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 18 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP7]] | +0.62 | +0.40 / +0.71 | both halves | 4e-05 |  |
| [[NCBP2AS2]] | +0.59 | +0.34 / +0.70 | both halves | 1e-04 |  |
| [[MALSU1]] | +0.58 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[MINCR]] | +0.57 | +0.29 / +0.64 | both halves | 2e-04 |  |
| [[SDHAF1]] | +0.57 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[AP2S1]] | +0.55 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[CHCHD1]] | +0.55 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[FAM104A]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[CCDC107]] | +0.52 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[RNF145]] | +0.52 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[C15orf61]] ⚠ | +0.52 | +0.29 / +0.57 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PGF]] | +0.52 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[DDIT4]] | +0.52 | +0.44 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK4]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[LIN7C]] | -0.50 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[FLII]] | -0.50 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[LPGAT1]] | -0.49 | -0.24 / -0.54 | both halves | 5e-04 |  |
| [[SERPINB2]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.48 | -0.17 / -0.55 | ⚠ one half (not replicated) | 0.001 |  |
| [[CCDC200]] | -0.48 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[WDR1]] | -0.48 | -0.18 / -0.58 | ⚠ one half (not replicated) | 1e-03 |  |
| [[MAPRE1]] | -0.46 | -0.16 / -0.57 | ⚠ one half (not replicated) | 0.001 |  |
| [[CHMP3]] | -0.46 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[SBDS]] | -0.45 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[LEPROT]] | -0.45 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[MOB1A]] | -0.45 | -0.23 / -0.48 | both halves | 5e-04 |  |
| [[TARDBP]] | -0.45 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[PSMD6-AS1]] | -0.45 | -0.40 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SMIM3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SNHG18]] | B | SNHG18 activity raises SMIM3's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 2.29× lower at baseline in the lines without SNHG18 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[GYPC]] | B | GYPC activity raises SMIM3's level | lines that do not express GYPC (35) vs lines expressing it (15) | 2.32× lower at baseline in the lines without GYPC | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RILPL2]] | B | SMIM3 activity raises RILPL2's level | lines that do not express SMIM3 (11) vs lines expressing it (39) | 1.37× lower at baseline in the lines without SMIM3 | 0.008 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FAM193B]] | B | SMIM3 activity raises FAM193B's level | lines that do not express SMIM3 (11) vs lines expressing it (39) | 1.23× lower at baseline in the lines without SMIM3 | 0.047 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.2, -12.6); signed map (-34.9, 4.4). **Vector** length 79.5, 18.7% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -0.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +0.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.8 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | -1.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +0.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.2 | -4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.1 | -6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.8 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -3.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.1 — chr5:150,778,757-150,796,734 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MSTP150, NID67; previously C5orf62 |
| Matched by | ensembl_id |

UniProt [Q9BZL3](https://www.uniprot.org/uniprotkb/Q9BZL3) carries no function annotation.

**Summary**, from NCBI Gene [85027](https://www.ncbi.nlm.nih.gov/gene/85027):

> Enables identical protein binding activity. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30248](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30248) · Entrez [85027](https://www.ncbi.nlm.nih.gov/gene/85027) · UniProt [Q9BZL3](https://www.uniprot.org/uniprotkb/Q9BZL3) · Ensembl [ENSG00000256235](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256235)

## Data

Gene col 14985: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14985); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14985, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14985]; `tensor/DDL_lfc|DDL_z.npy` [14985]; `embed/gene_vectors.npy` [14985]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14985 or target_col == 14985). Every well: [[SMIM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
