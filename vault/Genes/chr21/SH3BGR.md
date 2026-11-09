---
symbol: "SH3BGR"
type: "gene"
col: 11677
ensembl_id: "ENSG00000185437"
name: "SH3 domain binding glutamate rich protein"
location: "21q22.2"
module: 37
arm: "+"
pooled_cpm: 4.36
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 14
n_dd_up_clean: 27
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# SH3BGR

*SH3 domain binding glutamate rich protein* — 21q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.00× (z +12.6, q 7e-34, up in 26 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.381× (z -12.4, q 8e-33, down in 24 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.398× (z -11.9, q 5e-30, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02680]] (+0.62, fdr 1e-05), [[CD247]] (+0.59, fdr 1e-05), [[ADAM20]] (+0.58, fdr 1e-05); moves opposite to [[SNRPB]] (-0.54, fdr 2e-05), [[SMURF1]] (-0.53, fdr 2e-05), [[CDC25A]] (-0.52, fdr 2e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TNNI3K]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11677.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +12.6 | 7e-34 | 26/40 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +9.3 | 4e-18 | 22/35 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.56×** | +8.1 | 8e-14 | 17/47 (A-427, A498, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +7.8 | 7e-13 | 24/46 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +7.7 | 1e-12 | 24/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +7.6 | 3e-12 | 17/39 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +7.2 | 4e-11 | 21/44 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +7.2 | 6e-11 | 23/47 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +7.1 | 8e-11 | 3/9 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +5.7 | 7e-07 | 9/45 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +5.5 | 2e-06 | 16/47 (H4, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +5.1 | 2e-05 | 14/43 (H4, NCI-H23, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.8 | 8e-05 | 7/22 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.37×** | +4.6 | 2e-04 | 7/48 (C32, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.38×** | +4.5 | 2e-04 | 11/48 (SW480, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +4.4 | 3e-04 | 6/46 (SW480, LS 180, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.003 | 6/48 (NCI-H23, SW 1088, …) | all doses, flat |  |
| [[Afatinib (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.006 | 5/47 (A498, H4, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.008 | 6/45 (H4, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11677.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.381×** | -12.4 | 8e-33 | 24/33 (CFPAC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.398×** | -11.9 | 5e-30 | 34/48 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.418×** | -11.2 | 5e-27 | 35/45 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.474×** | -9.6 | 9e-20 | 26/45 (C32, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.419×** | -5.9 | 5e-07 | 10/44 (H4, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.737×** | -5.6 | 2e-06 | 20/40 (SW 900, A498, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.467×** | -5.1 | 2e-05 | 15/39 (KATO III, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.692×** | -4.7 | 1e-04 | 16/45 (H4, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.708×** | -4.4 | 5e-04 | 15/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.714×** | -4.2 | 0.002 | 15/46 (SK-MEL-2, C32, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.734×** | -4.0 | 0.003 | 11/47 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.755×** | -3.6 | 0.014 | 15/44 (SW480, SW 900, …) | two highest doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.837× | -3.2 | 0.053 | 8/48 (A-427, NCI-H460, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.783×** | -3.1 | 0.067 | 3/46 (C-33 A, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Mozavaptan (drug)]] 5 µM |  | **0.781×** | -3.1 | 0.083 | 9/43 (NCI-H2030, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11677. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 7.79 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.101× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 5.05 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0543× (z -9.9) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Acetazolamide (drug)]] 0.5 µM 0.0665× (z -9.6) |
| [[A498 (line)]] | wt | 4.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 3.43 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0655× (z -9.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 5.03 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0743× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 5.82 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0815× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 5.29 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0813× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 4.37 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 4.51 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0968× (z -11.1) ⚠ cell-cycle shift, explains ~93% of this change |
| [[A-172 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11677), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02680]] | +0.62 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CD247]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ADAM20]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[LINC00640]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[INTS4P1]] | +0.57 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[TBX19]] | +0.56 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[PLAC1]] | +0.55 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[EIF2A]] | +0.55 | +0.34 / +0.41 | both halves | 1e-04 |  |
| [[GTF2IP5]] | +0.55 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[LVRN]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ADAM20P1]] | +0.55 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[GOLGA8N]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SMURF1]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[CDC25A]] | -0.52 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[EML4]] | -0.52 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[FAF1]] | -0.52 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[E2F8]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[CTDSP1]] | -0.50 | -0.39 / -0.52 | both halves | 6e-05 | same gene group |
| [[MAP3K5]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[MAP3K14]] | -0.50 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[MTAP]] | -0.50 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[CDCA4]] | -0.50 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[NUP98]] | -0.50 | -0.40 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNNI3K]] | C | TNNI3K activity raises SH3BGR's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without TNNI3K | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.550). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.7, -19.2); signed map (8.8, 4.2). **Vector** length 55.1, 7.00% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.3 | +7.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.8 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.6 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -11.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -11.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.0 | -12.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.1 | -3.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.1 | -1.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain binding glutamate rich protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.2 — chr21:39,445,855-39,515,506 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 21-GARP |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | MYOGENESIS |
| Matched by | ensembl_id |

UniProt [P55822](https://www.uniprot.org/uniprotkb/P55822) carries no function annotation.

**Summary**, from NCBI Gene [6450](https://www.ncbi.nlm.nih.gov/gene/6450):

> Predicted to enable protein-macromolecule adaptor activity. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10822) · Entrez [6450](https://www.ncbi.nlm.nih.gov/gene/6450) · UniProt [P55822](https://www.uniprot.org/uniprotkb/P55822) · Ensembl [ENSG00000185437](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185437)

## Data

Gene col 11677: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11677); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11677, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11677]; `tensor/DDL_lfc|DDL_z.npy` [11677]; `embed/gene_vectors.npy` [11677]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11677 or target_col == 11677). Every well: [[SH3BGR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3BGR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
