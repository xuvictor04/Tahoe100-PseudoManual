---
symbol: "FLVCR1"
type: "gene"
col: 8575
ensembl_id: "ENSG00000162769"
name: "FLVCR choline and heme transporter 1"
location: "1q32.3"
module: 10
arm: "-"
pooled_cpm: 40.74
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FLVCR1

*FLVCR choline and heme transporter 1* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 1.25× (z +6.1, q 6e-07, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.670× (z -8.0, q 1e-12, down in 27 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.710× (z -6.8, q 3e-09, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL8]] (+0.58, fdr 5e-05), [[EEF2K]] (+0.58, fdr 1e-05), [[TXNL4A]] (+0.57, fdr 4e-05); moves opposite to [[LINC01376]] (-0.55, fdr 5e-05), [[TMEM232]] (-0.52, fdr 3e-04), [[SLC38A4-AS1]] (-0.51, fdr 2e-04).
> It sits in the **-** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8575.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **1.25×** | +6.1 | 6e-07 | 23/48 (C-33 A, NCI-H2030, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +5.9 | 8e-07 | 24/47 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.33×** | +5.6 | 4e-06 | 25/48 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +5.5 | 4e-06 | 25/48 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.31×** | +5.3 | 2e-05 | 23/48 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.9 | 1e-04 | 23/47 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.8 | 1e-04 | 20/48 (CFPAC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.28×** | +4.6 | 3e-04 | 25/46 (AsPC-1, SW480, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | 1.18× | +4.6 | 3e-04 | 18/49 (C-33 A, NCI-H2030, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.4 | 5e-04 | 19/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.3 | 8e-04 | 17/47 (HEC-1-A, C-33 A, …) | top dose only | plate-row cell shift |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.005 | 18/48 (NCI-H460, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.008 | 18/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.20× | +3.5 | 0.018 | 13/47 (CFPAC-1, J82, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.021 | 8/48 (NCI-H460, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Lopinavir (drug)]] 5 µM |  | 1.18× | +3.2 | 0.047 | 7/47 (J82, SW480, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.33×** | +2.9 | 0.096 | 9/48 (MIA PaCa-2, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8575.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.670×** | -8.0 | 1e-12 | 27/45 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.710×** | -6.8 | 3e-09 | 30/47 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.742×** | -5.7 | 2e-06 | 26/47 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.786×** | -4.8 | 2e-04 | 20/46 (Hs 766T, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.856× | -4.4 | 0.001 | 24/48 (A498, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.813×** | -4.1 | 0.003 | 20/48 (A498, C32, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.808×** | -4.1 | 0.003 | 21/40 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.810×** | -3.9 | 0.007 | 19/47 (HCT15, COLO 205, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[DTP3 (drug)]] 5 µM |  | 0.742× | -3.1 | 0.11 | 11/46 (SW 900, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.856× | -3.1 | 0.11 | 14/47 (A-172, NCI-H661, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.858× | -3.1 | 0.11 | 9/48 (A498, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 65.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.535× (z -10.1) |
| [[SW48 (line)]] | wt | 46.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -9.2) |
| [[C-33 A (line)]] | alt | 78.2 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 2.58× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 60.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.401× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 46.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -11.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 49.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 28.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.261× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 38.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.253× (z -10.3) ⚠ transcription drop; cell-cycle shift, explains ~23% of this change |
| [[NCI-H460 (line)]] | wt | 66.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 63.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -16.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -11.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL8]] | +0.58 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[EEF2K]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[TXNL4A]] | +0.57 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[NT5M]] | +0.54 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[PNPLA3]] | +0.54 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TRAP1]] | +0.54 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[SLC25A32]] | +0.54 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[SQLE]] | +0.54 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[MAP3K21]] | +0.54 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[MMAB]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[XYLB]] | +0.52 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[RABEPK]] | +0.52 | +0.46 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01376]] | -0.55 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[TMEM232]] | -0.52 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[SLC38A4-AS1]] | -0.51 | -0.29 / -0.59 | both halves | 2e-04 |  |
| [[PDCL3P4]] | -0.50 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[CHMP1B]] | -0.50 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[RAP2C-AS1]] | -0.49 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[EFCAB6]] | -0.49 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[KDM5A]] | -0.49 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[CAPN3]] | -0.48 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[TIGD6]] | -0.47 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[STPG2]] | -0.47 | -0.32 / -0.49 | both halves | 1e-04 |  |
| [[ZRANB2-DT]] | -0.47 | -0.30 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity weakens FLVCR1's drug response | lines that do not express NT5M (7) vs lines expressing it (41) | the lines without NT5M respond 1.54× as strongly (z diff -0.96); strongest at Homoharringtonine 5 µM: 1.57x vs 1.05x (z diff -4.1) | 0.036 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG; target measured in part of the lines; artifact flags |
| [[NT5M]] | B | NT5M activity raises FLVCR1's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without NT5M | 0.051 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[PCSK9]] | B | PCSK9 activity lowers FLVCR1's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 1.27× higher at baseline in the lines without PCSK9 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.455). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (18.8, -43.2); signed map (-48.9, -2.2). **Vector** length 98.3, 22.5% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +4.2 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.5 | +3.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.3 | +6.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.0 | +4.9 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.5 | +3.4 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -3.9 | -4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | FLVCR choline and heme transporter 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:212,858,275-212,899,363 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLVCR, MFSD7B, PCA, SLC49A1; previously AXPC1 |
| Gene groups (HGNC) | Solute carrier family 49 |
| Reactome | 4 pathways, smallest: Heme biosynthesis; Metabolism of porphyrins; Iron uptake and transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5Y0](https://www.uniprot.org/uniprotkb/Q9Y5Y0) (Choline/ethanolamine transporter FLVCR1):

> Uniporter that mediates the transport of extracellular choline and ethanolamine into cells, thereby playing a key role in phospholipid biosynthesis. Choline and ethanolamine are the precursors of phosphatidylcholine and phosphatidylethanolamine, respectively, the two most abundant phospholipids. Transport is not coupled with proton transport and is exclusively driven by the choline (or ethanolamine) gradient across the plasma membrane. Also acts as a heme b transporter that mediates heme efflux …

**Summary**, from NCBI Gene [28982](https://www.ncbi.nlm.nih.gov/gene/28982):

> This gene encodes a member of the major facilitator superfamily of transporter proteins. The encoded protein is a heme transporter that may play a critical role in erythropoiesis by protecting developing erythroid cells from heme toxicity. This gene may play a role in posterior column ataxia with retinitis pigmentosa and the hematological disorder Diamond-Blackfan syndrome. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:24682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24682) · Entrez [28982](https://www.ncbi.nlm.nih.gov/gene/28982) · UniProt [Q9Y5Y0](https://www.uniprot.org/uniprotkb/Q9Y5Y0) · Ensembl [ENSG00000162769](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162769)

## Data

Gene col 8575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8575); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8575]; `tensor/DDL_lfc|DDL_z.npy` [8575]; `embed/gene_vectors.npy` [8575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8575 or target_col == 8575). Every well: [[FLVCR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLVCR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
