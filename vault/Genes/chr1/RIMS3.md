---
symbol: "RIMS3"
type: "gene"
col: 3868
ensembl_id: "ENSG00000117016"
name: "regulating synaptic membrane exocytosis 3"
location: "1p34.2"
module: 82
arm: "+"
pooled_cpm: 3.38
n_lines_expressing: 41
n_dd_up: 16
n_dd_down: 18
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 16
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# RIMS3

*regulating synaptic membrane exocytosis 3* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.41× (z +17.4, q 0e+00, up in 32 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.315× (z -13.0, q 5e-36, down in 25 of 33 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA4F]] (+0.73, fdr 7e-06), [[SLC29A4]] (+0.73, fdr 1e-05), [[RAB6B]] (+0.72, fdr 7e-06); moves opposite to [[MCPH1]] (-0.72, fdr 1e-05), [[GTF2H1]] (-0.71, fdr 1e-05), [[WARS2-AS1]] (-0.69, fdr 1e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 16 go from it, the strongest it → [[ZNF483]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3868.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.41×** | +17.4 | 0e+00 | 32/37 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.92×** | +16.0 | 0e+00 | 32/38 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.30×** | +14.0 | 3e-42 | 29/37 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +10.9 | 1e-25 | 26/37 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.45×** | +10.5 | 1e-23 | 27/37 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.10×** | +8.7 | 3e-16 | 16/33 (LS 180, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.89×** | +7.4 | 9e-12 | 13/26 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.03×** | +6.8 | 8e-10 | 11/34 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.9 | 3e-07 | 0/5 | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +4.9 | 6e-05 | 6/37 (RKO, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +3.8 | 0.008 | 1/14 (LOX-IMVI) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.011 | 7/36 (J82, MIA PaCa-2, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.024 | 5/37 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.035 | 3/32 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.33×** | +3.3 | 0.035 | 3/36 (J82, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3868.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.315×** | -13.0 | 5e-36 | 25/33 (HS-578T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.406×** | -10.6 | 1e-23 | 23/36 (HS-578T, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.471×** | -8.8 | 2e-16 | 22/37 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.522×** | -7.6 | 4e-12 | 18/28 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.528×** | -7.5 | 7e-12 | 18/37 (HS-578T, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.641×** | -7.4 | 2e-11 | 16/29 (HS-578T, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.645×** | -5.1 | 2e-05 | 15/35 (HS-578T, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.658×** | -4.9 | 6e-05 | 13/25 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -4.7 | 2e-04 | 11/25 (HS-578T, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.762×** | -4.5 | 4e-04 | 16/38 (NCI-H2030, NCI-H2347, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.686×** | -4.4 | 5e-04 | 10/36 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.723×** | -3.8 | 0.007 | 11/36 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.734×** | -3.6 | 0.012 | 6/34 (HS-578T, Panc 03.27, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.571×** | -3.4 | 0.024 | 9/34 (HS-578T, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.741×** | -3.4 | 0.027 | 8/20 (HS-578T, A-427, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.579×** | -3.4 | 0.028 | 9/27 (HS-578T, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -3.2 | 0.043 | 11/29 (HS-578T, COLO 205, …) | top dose only | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3868. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 29.3 | 0 | 17 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0148× (z -23.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0559× (z -15.4) |
| [[NCI-H2030 (line)]] | alt | 6.34 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.117× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 6.01 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -10.8) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -9.0) |
| [[A-172 (line)]] | wt | 4.78 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0533× (z -11.5) |
| [[PANC-1 (line)]] | alt | 2.53 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0733× (z -15.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -8.7) |
| [[A-427 (line)]] | wt | 7.35 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.120× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 5.25 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -9.4) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW480 (line)]] | alt | 2.17 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.5× (z +8.8) | — |
| [[A498 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.697 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.775 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.989 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3868), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA4F]] | +0.73 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[SLC29A4]] | +0.73 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[RAB6B]] | +0.72 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[USP35]] | +0.71 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PEDS1]] | +0.71 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[DNMT3B]] | +0.70 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[GNAZ]] | +0.70 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[TSPAN33]] | +0.70 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ASAP3]] | +0.69 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[MAST3]] | +0.69 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[LMX1B]] | +0.68 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.67 | +0.59 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCPH1]] | -0.72 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[GTF2H1]] | -0.71 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.69 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[INO80D]] | -0.69 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.68 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[ASH1L]] | -0.68 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[ST7L]] | -0.67 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[ITPA]] | -0.66 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[C11orf58]] | -0.66 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[TRMT13]] | -0.65 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[AEBP2]] | -0.65 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[MZF1-AS1]] | -0.64 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RIMS3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LHX6]] | B | LHX6 activity raises RIMS3's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 1.87× lower at baseline in the lines without LHX6 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF483]] | B | RIMS3 activity raises ZNF483's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 1.47× lower at baseline in the lines without RIMS3 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[RALGPS1]] | B | RIMS3 activity raises RALGPS1's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 2.00× lower at baseline in the lines without RIMS3 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[LMX1B]] | B | RIMS3 activity raises LMX1B's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 2.88× lower at baseline in the lines without RIMS3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[IL17RD]] | B | RIMS3 activity raises IL17RD's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 2.43× lower at baseline in the lines without RIMS3 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[CROCCP3]] | B | RIMS3 activity raises CROCCP3's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 1.49× lower at baseline in the lines without RIMS3 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[SEPTIN3]] | B | RIMS3 activity raises SEPTIN3's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 2.07× lower at baseline in the lines without RIMS3 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[ARHGAP44]] | B | RIMS3 activity raises ARHGAP44's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 1.89× lower at baseline in the lines without RIMS3 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[LRFN3]] | B | RIMS3 activity raises LRFN3's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 1.41× lower at baseline in the lines without RIMS3 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[SBK1]] | B | RIMS3 activity raises SBK1's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 2.16× lower at baseline in the lines without RIMS3 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[MGME1]] | B | RIMS3 activity raises MGME1's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 1.30× lower at baseline in the lines without RIMS3 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[L1CAM]] | B | RIMS3 activity raises L1CAM's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 2.98× lower at baseline in the lines without RIMS3 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[STOX2]] | B | RIMS3 activity raises STOX2's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 2.69× lower at baseline in the lines without RIMS3 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.8, -0.2); signed map (-38.9, -6.3). **Vector** length 65.2, 11.1% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +10.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +17.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +16.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +8.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +14.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +6.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +2.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.1 | +1.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.2 | -13.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -5.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.3 | -3.6 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | regulating synaptic membrane exocytosis 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:40,620,680-40,665,682 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RIM3, NIM3 |
| Gene groups (HGNC) | Regulating synaptic membrane exocytosis family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJD0](https://www.uniprot.org/uniprotkb/Q9UJD0) (Regulating synaptic membrane exocytosis protein 3):

> Regulates synaptic membrane exocytosis.

**Summary**, from NCBI Gene [9783](https://www.ncbi.nlm.nih.gov/gene/9783):

> Predicted to enable transmembrane transporter binding activity. Predicted to be a structural constituent of presynaptic active zone. Predicted to be involved in several processes, including regulated exocytosis; regulation of synapse organization; and regulation of synaptic vesicle exocytosis. Predicted to be located in presynaptic active zone. Predicted to be active in several cellular components, including postsynaptic cytosol; presynaptic active zone cytoplasmic component; and presynaptic …

**Accessions** — [HGNC:21292](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21292) · Entrez [9783](https://www.ncbi.nlm.nih.gov/gene/9783) · UniProt [Q9UJD0](https://www.uniprot.org/uniprotkb/Q9UJD0) · Ensembl [ENSG00000117016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117016)

## Data

Gene col 3868: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3868); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3868, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3868]; `tensor/DDL_lfc|DDL_z.npy` [3868]; `embed/gene_vectors.npy` [3868]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3868 or target_col == 3868). Every well: [[RIMS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIMS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
