---
symbol: "MED24"
type: "gene"
col: 180
ensembl_id: "ENSG00000008838"
name: "mediator complex subunit 24"
location: "17q21.1"
module: 46
arm: "+"
pooled_cpm: 35.27
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# MED24

*mediator complex subunit 24* — 17q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.31× (z +7.8, q 5e-12, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.551× (z -12.1, q 1e-30, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM94]] (+0.71, fdr 7e-06), [[VPS52]] (+0.68, fdr 1e-05), [[EIF2D]] (+0.65, fdr 1e-05); moves opposite to [[EHD4]] (-0.60, fdr 4e-05), [[ZSWIM6]] (-0.57, fdr 2e-05), [[ACTG1]] (-0.54, fdr 6e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 180.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +7.8 | 5e-12 | 28/47 (NCI-H1792, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +7.3 | 6e-11 | 30/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.4 | 3e-08 | 27/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.24×** | +6.1 | 1e-07 | 26/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +6.0 | 2e-07 | 29/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +5.6 | 3e-06 | 20/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.4 | 6e-06 | 14/48 (HEC-1-A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +4.8 | 1e-04 | 19/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +4.7 | 2e-04 | 23/48 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +4.6 | 2e-04 | 23/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +4.5 | 3e-04 | 20/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +4.3 | 8e-04 | 17/48 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.007 | 15/48 (J82, PANC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.007 | 16/47 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.20× | +3.5 | 0.020 | 13/48 (PANC-1, A-427, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.020 | 6/48 (PANC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.18× | +3.3 | 0.033 | 4/48 (A498, A549, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.076 | 7/46 (SHP-77, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 180.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.551×** | -12.1 | 1e-30 | 39/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.638×** | -9.1 | 3e-17 | 37/48 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.646×** | -8.8 | 2e-16 | 38/48 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.739×** | -8.7 | 6e-16 | 35/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.655×** | -8.6 | 1e-15 | 34/48 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.740×** | -6.1 | 1e-07 | 29/47 (COLO 205, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.650×** | -4.6 | 4e-04 | 25/48 (NCI-H460, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.817×** | -4.1 | 0.003 | 17/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.831×** | -3.8 | 0.011 | 16/48 (C-33 A, BT-474, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.851× | -3.3 | 0.058 | 7/48 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Furosemide (drug)]] 0.5 µM |  | 0.860× | -3.1 | 0.11 | 14/48 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.862× | -3.0 | 0.12 | 12/48 (SW 1271, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.397× (z -10.6) |
| [[LoVo (line)]] | wt | 23.3 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.79× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 33.1 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.464× (z -9.3) |
| [[RKO (line)]] | wt | 43.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 36.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +11.8) | — |
| [[A-172 (line)]] | wt | 33.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 37.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 32.3 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.0731× (z -8.8) |
| [[CHP-212 (line)]] | wt | 82.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 22.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -9.2) |
| [[HOP62 (line)]] | alt | 28.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.399× (z -9.3) |
| [[HS-578T (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 31.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +17.6) | — |
| [[RPMI-7951 (line)]] | alt | 31.8 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.0976× (z -8.7) |
| [[SHP-77 (line)]] | alt | 30.1 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.233× (z -10.3) |
| [[A-427 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM94]] | +0.71 | +0.61 / +0.72 | both halves | 7e-06 | same gene group |
| [[VPS52]] | +0.68 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[EIF2D]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[GPALPP1]] | +0.63 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[TSTD3]] | +0.63 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[RCC1L]] | +0.63 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[CDC23]] | +0.63 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[PGAP3]] | +0.63 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[QTRT1]] | +0.62 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[SH2B1]] | +0.62 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[MAIP1]] | +0.60 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[TIAL1]] | +0.60 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD4]] | -0.60 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ZSWIM6]] | -0.57 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[ACTG1]] | -0.54 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[DUSP5]] | -0.53 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[AREG]] | -0.52 | -0.39 / -0.42 | both halves | 6e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[GPRIN1]] | -0.52 | -0.25 / -0.41 | both halves | 4e-04 |  |
| [[RMC1]] | -0.51 | -0.41 / -0.22 | both halves | 6e-04 |  |
| [[CBL]] | -0.51 | -0.35 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MED24's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises MED24's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF675]] | B | ZNF675 activity raises MED24's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 1.41× lower at baseline in the lines without ZNF675 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-11.0, 8.3); signed map (22.5, -22.9). **Vector** length 89.0, 18.6% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +7.4 | +6.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.7 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.2 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.6 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | -0.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.0 | +3.3 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -5.5 | -8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -8.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.2 | -12.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.9 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | -8.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -4.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[Adagrasib (drug)]] 5 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.1 — chr17:40,019,097-40,061,215 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRAP100, KIAA0130, DRIP100, CRSP100, MED5; previously THRAP4, CRSP4 |
| Gene groups (HGNC) | Mediator complex; MicroRNA protein coding host genes; Small nucleolar RNA protein coding host genes |
| Hallmark sets | GLYCOLYSIS, ESTROGEN_RESPONSE_EARLY |
| Reactome | 13 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [O75448](https://www.uniprot.org/uniprotkb/O75448) (Mediator of RNA polymerase II transcription subunit 24):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [9862](https://www.ncbi.nlm.nih.gov/gene/9862):

> This gene encodes a component of the mediator complex (also known as TRAP, SMCC, DRIP, or ARC), a transcriptional coactivator complex thought to be required for the expression of almost all genes. The mediator complex is recruited by transcriptional activators or nuclear receptors to induce gene expression, possibly by interacting with RNA polymerase II and promoting the formation of a transcriptional pre-initiation complex. Multiple transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:22963](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22963) · Entrez [9862](https://www.ncbi.nlm.nih.gov/gene/9862) · UniProt [O75448](https://www.uniprot.org/uniprotkb/O75448) · Ensembl [ENSG00000008838](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008838)

## Data

Gene col 180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 180); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 180]; `tensor/DDL_lfc|DDL_z.npy` [180]; `embed/gene_vectors.npy` [180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 180 or target_col == 180). Every well: [[MED24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
