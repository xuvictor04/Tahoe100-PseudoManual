---
symbol: "CAMK2N1"
type: "gene"
col: 8532
ensembl_id: "ENSG00000162545"
name: "calcium/calmodulin dependent protein kinase II inhibitor 1"
location: "1p36.12"
module: 4
arm: "-"
pooled_cpm: 35.04
n_lines_expressing: 42
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CAMK2N1

*calcium/calmodulin dependent protein kinase II inhibitor 1* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.55× (z +7.8, q 3e-12, up in 30 of 35 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 6.46×, SNU-423 5.08×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-423 4.52×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.577× (z -7.4, q 1e-10, down in 27 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETHE1]] (+0.53, fdr 3e-05), [[BAIAP2L1]] (+0.52, fdr 4e-05), [[RHOD]] (+0.50, fdr 4e-04); moves opposite to [[XRCC6]] (-0.59, fdr 1e-05), [[GATB]] (-0.54, fdr 2e-05), [[RPTOR]] (-0.52, fdr 4e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MUC3A]] → it (grade B ⚠); 4 go from it, the strongest it → [[DUS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8532.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 6.46×, SNU-423 5.08×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-423 4.52×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +7.8 | 3e-12 | 30/35 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +7.5 | 1e-11 | 20/30 (SNU-423, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +4.9 | 2e-04 | 23/33 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.8 | 0.022 | 19/38 (RPMI-7951, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | 1.41× | +3.3 | 0.11 | 17/38 (A-172, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.38× | +3.1 | 0.18 | 17/39 (NCI-H1573, C32, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.37× | +3.0 | 0.22 | 19/40 (NCI-H2347, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8532.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.577×** | -7.4 | 1e-10 | 27/39 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.502×** | -6.5 | 2e-08 | 28/40 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.518×** | -6.2 | 9e-08 | 28/40 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.377×** | -4.8 | 2e-04 | 28/38 (LoVo, HT-29, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.575×** | -4.8 | 2e-04 | 31/39 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.587×** | -4.6 | 4e-04 | 26/39 (HepG2/C3A, HOP62, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.622×** | -4.5 | 5e-04 | 22/38 (HS-578T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.623×** | -4.5 | 5e-04 | 27/40 (A498, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.665×** | -3.9 | 0.007 | 23/40 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.678×** | -3.7 | 0.013 | 21/40 (A498, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.772×** | -3.4 | 0.029 | 18/40 (A549, HS-578T, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.679×** | -3.4 | 0.034 | 15/40 (KATO III, J82, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.519×** | -3.2 | 0.052 | 20/40 (HS-578T, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.526×** | -3.2 | 0.059 | 22/40 (HS-578T, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **0.528×** | -3.2 | 0.059 | 16/40 (Panc 03.27, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8532. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 73.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -15.6) |
| [[LoVo (line)]] | wt | 85.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -18.2) |
| [[A549 (line)]] | wt | 55.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 256 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -13.9) |
| [[HT-29 (line)]] | alt | 81.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -11.5) |
| [[KATO III (line)]] | alt | 83.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -16.5) |
| [[A498 (line)]] | wt | 75.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 76.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 19.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -10.0) |
| [[LS 180 (line)]] | wt | 46.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.7) |
| [[SNU-423 (line)]] | alt | 33.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 76.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -12.9) |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0605× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 17.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.46× (z +9.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 64.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -10.1) |
| [[A-172 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.67 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.76 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.94 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8532), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETHE1]] | +0.53 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[BAIAP2L1]] | +0.52 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[RHOD]] | +0.50 | +0.26 / +0.52 | both halves | 4e-04 |  |
| [[NOL4L]] | +0.49 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[DNAJC1]] | +0.47 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[BBLN]] | +0.47 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[HEBP2]] | +0.47 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[MYO6]] | +0.47 | +0.50 / +0.29 | both halves | 2e-04 |  |
| [[MUC12]] | +0.47 | +0.32 / +0.43 | both halves | 2e-04 |  |
| [[SVIP]] | +0.46 | +0.37 / +0.35 | both halves | 1e-04 |  |
| [[CDKN2D]] | +0.46 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[GPX4]] | +0.46 | +0.31 / +0.45 | both halves | 2e-04 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRCC6]] | -0.59 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[GATB]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[RPTOR]] | -0.52 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[DDX56]] | -0.52 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[TAS2R30]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[CCT7]] | -0.50 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[USP5]] | -0.48 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[MTX1]] | -0.48 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[COX10]] | -0.48 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[MRPS27]] | -0.47 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[EMG1]] | -0.47 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[TSR1]] | -0.47 | -0.43 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC3A]] | B | MUC3A activity raises CAMK2N1's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without MUC3A | 0.022 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[PKDCC]] | B | PKDCC activity strengthens CAMK2N1's drug response | lines that do not express PKDCC (19) vs lines expressing it (21) | the lines without PKDCC respond 0.87× as strongly (z diff +0.91); strongest at Panobinostat 0.5 µM: 0.61x vs 0.30x (z diff +3.8) | 0.089 | ⚠ within organs, on part of the lines; also absent: CHD5, CCDC144NL-AS1, LINC02864; target measured in part of the lines; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUS2]] | B | CAMK2N1 activity lowers DUS2's level | lines that do not express CAMK2N1 (8) vs lines expressing it (42) | 1.66× higher at baseline in the lines without CAMK2N1 | 0.007 | ⚠ within organs, on part of the lines; also absent: RPLP0P2; maybe low, not absent |
| [[LARS2]] | B | CAMK2N1 activity lowers LARS2's level | lines that do not express CAMK2N1 (8) vs lines expressing it (42) | 1.35× higher at baseline in the lines without CAMK2N1 | 0.066 | ⚠ within organs, on part of the lines; also absent: RPLP0P2; maybe low, not absent |
| [[TFEB]] | B | CAMK2N1 activity raises TFEB's level | lines that do not express CAMK2N1 (8) vs lines expressing it (42) | 1.49× lower at baseline in the lines without CAMK2N1 | 0.067 | ⚠ within organs, on part of the lines; also absent: RPLP0P2; maybe low, not absent |
| [[SMARCAL1]] | B | CAMK2N1 activity lowers SMARCAL1's level | lines that do not express CAMK2N1 (8) vs lines expressing it (42) | 1.31× higher at baseline in the lines without CAMK2N1 | 0.074 | ⚠ within organs, on part of the lines; also absent: RPLP0P2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.374). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.8, 38.5); signed map (47.8, -3.1). **Vector** length 68.1, 16.5% of its response variance represented; |z| ≥ 3 in 712 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.8 | -0.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | -2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.4 | +0.1 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +1.4 | -0.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.2 | +1.0 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.7 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.7 | -4.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | calcium/calmodulin dependent protein kinase II inhibitor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:20,482,391-20,486,210 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CaMKIINalpha |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7J9](https://www.uniprot.org/uniprotkb/Q7Z7J9) (Calcium/calmodulin-dependent protein kinase II inhibitor 1):

> Potent and specific inhibitor of CaM-kinase II (CAMK2) (By similarity). Plays a role in the maintenance of long-term retrieval-induced memory in response to contextual fear (By similarity). Modulates blood pressure and vascular reactivity via regulation of CAMK2 activity in addition to regulation of left ventricular mass (By similarity). Mediates the NLRP3 inflammasome in cardiomyocytes via acting as an inhibitor of the MAPK14/p38 and MAPK8/JNK pathways, thereby regulating ventricular …

**Summary**, from NCBI Gene [55450](https://www.ncbi.nlm.nih.gov/gene/55450):

> Predicted to enable calcium-dependent protein kinase inhibitor activity and protein kinase binding activity. Predicted to be involved in long-term memory and positive regulation of inflammatory response. Predicted to be located in neuronal cell body and synapse. Implicated in ovarian cancer; ovarian carcinoma; and prostate adenocarcinoma. Biomarker of hepatocellular carcinoma; oral squamous cell carcinoma; papillary thyroid carcinoma; and prostate cancer. [provided by Alliance of Genome …

**Accessions** — [HGNC:24190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24190) · Entrez [55450](https://www.ncbi.nlm.nih.gov/gene/55450) · UniProt [Q7Z7J9](https://www.uniprot.org/uniprotkb/Q7Z7J9) · Ensembl [ENSG00000162545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162545)

## Data

Gene col 8532: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8532); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8532, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8532]; `tensor/DDL_lfc|DDL_z.npy` [8532]; `embed/gene_vectors.npy` [8532]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8532 or target_col == 8532). Every well: [[CAMK2N1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMK2N1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
