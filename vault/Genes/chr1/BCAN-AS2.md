---
symbol: "BCAN-AS2"
type: "gene"
col: 13722
ensembl_id: "ENSG00000229953"
name: "BCAN antisense RNA 2"
location: "1q23.1"
module: 158
arm: "+"
pooled_cpm: 6.65
n_lines_expressing: 41
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# BCAN-AS2

*BCAN antisense RNA 2* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.88× (z +7.4, q 6e-11, up in 22 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.474× (z -8.7, q 1e-15, down in 28 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCAN-AS1]] (+0.74, fdr 7e-06, ⚠ same locus), [[FOSL1]] (+0.69, fdr 7e-06), [[LINC00460]] (+0.69, fdr 7e-06), [[ZNF697]] (+0.69, fdr 7e-06); moves opposite to [[HIGD2A]] (-0.60, fdr 1e-05), [[NCOA1]] (-0.57, fdr 2e-05), [[TMEM59]] (-0.56, fdr 1e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 6 go from it, the strongest it → [[DIO3OS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13722.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +7.4 | 6e-11 | 22/33 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +4.5 | 0.002 | 15/36 (A498, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +4.1 | 0.009 | 10/35 (A-172, KATO III, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +3.6 | 0.046 | 13/32 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.046 | 14/35 (RPMI-7951, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +3.4 | 0.066 | 16/38 (A498, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.069 | 14/34 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13722.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.474×** | -8.7 | 1e-15 | 28/33 (MIA PaCa-2, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.408×** | -7.4 | 3e-11 | 25/31 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.441×** | -6.5 | 1e-08 | 25/31 (NCI-H23, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.459×** | -6.4 | 2e-08 | 26/36 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.463×** | -6.4 | 2e-08 | 25/38 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.495×** | -5.8 | 6e-07 | 21/36 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.573×** | -5.5 | 3e-06 | 21/36 (SW480, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.512×** | -5.3 | 7e-06 | 20/35 (C32, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.516×** | -4.7 | 2e-04 | 18/37 (C32, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.574×** | -4.6 | 3e-04 | 16/37 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.630×** | -4.4 | 6e-04 | 14/36 (SW480, C32, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.652×** | -4.4 | 6e-04 | 17/37 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.591×** | -4.2 | 0.001 | 15/30 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.700×** | -3.7 | 0.007 | 14/37 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -3.5 | 0.015 | 15/34 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.641×** | -3.5 | 0.015 | 17/35 (MIA PaCa-2, LoVo, …) | rises with dose | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.681×** | -3.0 | 0.077 | 9/35 (A-172, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13722. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.6 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0994× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -9.1) |
| [[C32 (line)]] | wt | 9.32 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0656× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.0590× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 9.16 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0464× (z -16.5) |
| [[SHP-77 (line)]] | alt | 13.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0702× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -9.3) |
| [[A-172 (line)]] | wt | 6.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +9.1) | — |
| [[A549 (line)]] | wt | 7.27 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0894× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 3.75 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0646× (z -8.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -10.0) |
| [[PANC-1 (line)]] | alt | 4.16 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0994× (z -8.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0654× (z -11.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 6.70 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -10.9) |
| [[A-427 (line)]] | wt | 0.987 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.929 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13722), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAN-AS1]] | +0.74 | +0.77 / +0.65 | both halves | 7e-06 | same gene group; ⚠ same locus (5.5 kb, same strand: neighbours can correlate without regulation) |
| [[FOSL1]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[LINC00460]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[ZNF697]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[SERPINB8]] | +0.64 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[ZKSCAN2]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[PRKG2-AS1]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 | same gene group |
| [[CSRP1]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SLC45A3]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[MYEOV]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ERCC1]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[EGR3]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[FAM83G]] | +0.59 | +0.63 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIGD2A]] | -0.60 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[NCOA1]] | -0.57 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[TMEM59]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[NPEPPS]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[SOS1]] | -0.54 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[FBXL20]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[MAP3K2]] | -0.53 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.53 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[APTR]] | -0.53 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ZDHHC24]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PPP1R12B]] | -0.52 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[CNNM2]] | -0.52 | -0.48 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises BCAN-AS2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers BCAN-AS2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[TOP2A]] | B | TOP2A activity raises BCAN-AS2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[BCAN-AS1]] | C | BCAN-AS1 activity raises BCAN-AS2's level | lines that do not express BCAN-AS1 (11) vs lines expressing it (39) | 3.61× lower at baseline in the lines without BCAN-AS1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS2, ETV7; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIO3OS]] | B | BCAN-AS2 activity raises DIO3OS's level | lines that do not express BCAN-AS2 (9) vs lines expressing it (41) | 1.72× lower at baseline in the lines without BCAN-AS2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS1, ARHGAP18 |
| [[SUMO2]] | B | BCAN-AS2 activity lowers SUMO2's level | lines that do not express BCAN-AS2 (9) vs lines expressing it (41) | 1.17× higher at baseline in the lines without BCAN-AS2 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS1, ARHGAP18 |
| [[NTSR1]] | B | BCAN-AS2 activity raises NTSR1's level | lines that do not express BCAN-AS2 (9) vs lines expressing it (41) | 3.66× lower at baseline in the lines without BCAN-AS2 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS1, ARHGAP18 |
| [[LINC02320]] | B | BCAN-AS2 activity raises LINC02320's level | lines that do not express BCAN-AS2 (9) vs lines expressing it (41) | 3.10× lower at baseline in the lines without BCAN-AS2 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS1, ARHGAP18 |
| [[PRKG2]] | B | BCAN-AS2 activity raises PRKG2's level | lines that do not express BCAN-AS2 (9) vs lines expressing it (41) | 1.76× lower at baseline in the lines without BCAN-AS2 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS1, ARHGAP18 |
| [[BCAN-AS1]] | C | BCAN-AS2 activity raises BCAN-AS1's level | lines that do not express BCAN-AS2 (9) vs lines expressing it (41) | 3.60× lower at baseline in the lines without BCAN-AS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS1, ARHGAP18; co-absent with the target |

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.0, 2.1); signed map (7.9, 39.9). **Vector** length 86.7, 20.4% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +7.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.8 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.3 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +2.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | -7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.6 | -6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.4 | -5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.1 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.9 | -4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.6 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.3 | -5.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.3 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | BCAN antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q23.1 — chr1:156,646,507-156,661,424 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ENST869, AL590666.2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56267](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56267) · Entrez [126568844](https://www.ncbi.nlm.nih.gov/gene/126568844) · Ensembl [ENSG00000229953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229953)

## Data

Gene col 13722: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13722); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13722, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13722]; `tensor/DDL_lfc|DDL_z.npy` [13722]; `embed/gene_vectors.npy` [13722]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13722 or target_col == 13722). Every well: [[BCAN-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCAN-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
