---
symbol: "ENTREP1"
type: "gene"
col: 5644
ensembl_id: "ENSG00000135063"
name: "endosomal transmembrane epsin interactor 1"
location: "9q21.12"
module: 61
arm: "+"
pooled_cpm: 4.41
n_lines_expressing: 32
n_dd_up: 20
n_dd_down: 14
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 11
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# ENTREP1

*endosomal transmembrane epsin interactor 1* — 9q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.02× (z +10.1, q 2e-21, up in 20 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.464× (z -7.9, q 2e-12, down in 18 of 29 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.491× (z -3.8, q 0.012, down in 3 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCAS4]] (+0.59, fdr 1e-05), [[CYRIA]] (+0.58, fdr 1e-05), [[NDRG4]] (+0.57, fdr 1e-05); moves opposite to [[ELP4]] (-0.49, fdr 1e-04), [[IFT43]] (-0.49, fdr 4e-05), [[C2CD3]] (-0.48, fdr 1e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RRAGD]] → it (grade B ⚠); 11 go from it, the strongest it → [[SLC26A5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5644.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +10.1 | 2e-21 | 20/29 (NCI-H460, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.66×** | +10.0 | 4e-21 | 19/27 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +9.4 | 8e-19 | 11/24 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +8.7 | 7e-16 | 11/24 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +7.1 | 2e-10 | 10/24 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.86×** | +6.3 | 3e-08 | 14/29 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.74×** | +5.7 | 1e-06 | 14/29 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.36×** | +4.4 | 7e-04 | 9/28 (SW1417, SW480, …) | all doses, flat | low cells (technical?) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.53×** | +4.3 | 9e-04 | 10/29 (SW480, SW1417, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.12×** | +4.0 | 0.003 | 0/13 | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.006 | 7/27 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.45×** | +3.8 | 0.008 | 9/27 (SW1417, SW480, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.98×** | +3.6 | 0.012 | 5/26 (LoVo, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.5 | 0.017 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.41×** | +3.5 | 0.017 | 4/28 (Hs 766T, C32, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.053 | 2/25 (NCI-H2347, NCI-H1573) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.062 | 5/24 (KATO III, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.066 | 6/29 (C32, A-427, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.066 | 3/26 (SW 900, J82, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5644.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.464×** | -7.9 | 2e-12 | 18/29 (SNU-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.611×** | -5.1 | 1e-04 | 13/20 (HEC-1-A, SW 900, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.619×** | -4.9 | 2e-04 | 15/29 (A549, BT-474, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.638×** | -4.6 | 6e-04 | 11/25 (SNU-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.654×** | -4.4 | 0.001 | 7/25 (A-427, SW 900, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.491×** | -3.8 | 0.012 | 3/26 (A498, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -3.8 | 0.012 | 8/29 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.694×** | -3.8 | 0.012 | 9/27 (A-427, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.782×** | -3.6 | 0.021 | 6/29 (A498, Hs 766T, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **0.792×** | -3.4 | 0.038 | 10/28 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.720×** | -3.4 | 0.038 | 2/29 (CHP-212, Hs 766T) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.796×** | -3.3 | 0.042 | 6/29 (H4, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.730×** | -3.2 | 0.054 | 6/28 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.736×** | -3.2 | 0.066 | 4/27 (A-427, SHP-77, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 5 µM |  | **0.807×** | -3.1 | 0.067 | 8/27 (NCI-H23, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5644. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 16.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -11.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0543× (z -11.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A549 (line)]] | wt | 4.05 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0537× (z -9.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[C32 (line)]] | wt | 6.90 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0530× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 6.26 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 3.28 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0719× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 4.77 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.649 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.998 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.457 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5644), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAS4]] | +0.59 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[CYRIA]] | +0.58 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[NDRG4]] | +0.57 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[STK32A]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CCDC85A]] | +0.56 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[APBA1]] | +0.54 | +0.50 / +0.60 | both halves | 1e-05 | STRING 555; ⚠ same locus (35.0 kb: neighbours can correlate without regulation) |
| [[SNAP91]] | +0.54 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[WIPF3]] | +0.54 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[NEURL1]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[TBC1D9]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[CELF4]] | +0.53 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[EPHA10]] | +0.52 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[NRXN1]] | +0.52 | +0.43 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP4]] | -0.49 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[IFT43]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[C2CD3]] | -0.48 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[ATG7]] | -0.45 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[PRH1]] | -0.45 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[MZF1]] | -0.45 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[ZNF407]] | -0.45 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[KATNIP]] | -0.45 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[HDAC4]] | -0.44 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[MYCBP]] | -0.42 | -0.47 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRAGD]] | B | RRAGD activity raises ENTREP1's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 2.73× lower at baseline in the lines without RRAGD | 0.006 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[STK32A]] | B | STK32A activity raises ENTREP1's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.92× lower at baseline in the lines without STK32A | 0.030 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[EPB41L4A]] | C | EPB41L4A activity raises ENTREP1's level | lines that do not express EPB41L4A (26) vs lines expressing it (24) | 1.99× lower at baseline in the lines without EPB41L4A | 0.095 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, ANKRD20A11P; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC26A5]] | B | ENTREP1 activity raises SLC26A5's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.15× lower at baseline in the lines without ENTREP1 | 0.023 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[ADAP2]] | B | ENTREP1 activity raises ADAP2's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.86× lower at baseline in the lines without ENTREP1 | 0.028 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[HRK]] | B | ENTREP1 activity raises HRK's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.71× lower at baseline in the lines without ENTREP1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[STK32A]] | B | ENTREP1 activity raises STK32A's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 2.30× lower at baseline in the lines without ENTREP1 | 0.035 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[WIPF3]] | B | ENTREP1 activity raises WIPF3's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without ENTREP1 | 0.047 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[TPD52L1]] | B | ENTREP1 activity raises TPD52L1's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.33× lower at baseline in the lines without ENTREP1 | 0.057 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[ZNF385B]] | B | ENTREP1 activity raises ZNF385B's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.97× lower at baseline in the lines without ENTREP1 | 0.074 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[TMCC2]] | B | ENTREP1 activity raises TMCC2's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.67× lower at baseline in the lines without ENTREP1 | 0.083 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[EPHA10]] | B | ENTREP1 activity raises EPHA10's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.53× lower at baseline in the lines without ENTREP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[SLAIN1]] | C | ENTREP1 activity raises SLAIN1's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 2.81× lower at baseline in the lines without ENTREP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4; co-absent with the target |
| [[EPB41L4A]] | C | ENTREP1 activity raises EPB41L4A's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 3.90× lower at baseline in the lines without ENTREP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.9, 22.1); signed map (33.3, 21.4). **Vector** length 49.1, 8.54% of its response variance represented; |z| ≥ 3 in 701 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +9.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +3.0 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -1.6 | -4.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.6 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.4 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -1.3 | -4.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -3.8 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.0 | -3.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.9 | -0.9 |
|  | [[Thymol (drug)]] 5 µM |  | -0.9 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | endosomal transmembrane epsin interactor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.12 — chr9:69,324,567-69,392,558 (+) |
| Ensembl biotype | protein_coding |
| Also known as | X123, ENTREP; previously C9orf61, FAM189A2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15884](https://www.uniprot.org/uniprotkb/Q15884) (Endosomal transmembrane epsin interactor 1):

> Functions as an activator of the E3 ubiquitin protein ligase ITCH in the ubiquitination of the CXCL12-activated CXCR4 receptor. Thereby, triggers CXCR4 endocytosis and desensitization, negatively regulating the CXCL12/CXCR4 signaling pathway.

**Summary**, from NCBI Gene [9413](https://www.ncbi.nlm.nih.gov/gene/9413):

> Enables ubiquitin ligase activator activity. Involved in CXCL12-activated CXCR4 signaling pathway and negative adaptation of signaling pathway. Located in endosome membrane and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24820](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24820) · Entrez [9413](https://www.ncbi.nlm.nih.gov/gene/9413) · UniProt [Q15884](https://www.uniprot.org/uniprotkb/Q15884) · Ensembl [ENSG00000135063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135063)

## Data

Gene col 5644: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5644); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5644, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5644]; `tensor/DDL_lfc|DDL_z.npy` [5644]; `embed/gene_vectors.npy` [5644]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5644 or target_col == 5644). Every well: [[ENTREP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENTREP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
