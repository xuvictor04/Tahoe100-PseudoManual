---
symbol: "LAT"
type: "gene"
col: 13124
ensembl_id: "ENSG00000213658"
name: "linker for activation of T cells"
location: "16p11.2"
module: 34
arm: "+"
pooled_cpm: 6.13
n_lines_expressing: 43
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# LAT

*linker for activation of T cells* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.58× (z +9.8, q 1e-19, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.36× (z +9.2, q 2e-17, up in 21 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.668× (z -4.3, q 0.008, down in 8 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TM4SF19-DYNLT2B]] (+0.64, fdr 1e-05), [[PLEKHM1]] (+0.62, fdr 9e-06), [[TM4SF19]] (+0.60, fdr 1e-05); moves opposite to [[ALDH1A1]] (-0.52, fdr 1e-05), [[ATRAID]] (-0.50, fdr 6e-05), [[COQ2]] (-0.50, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CARD11]] → it (grade B ⚠); 3 go from it, the strongest it → [[DYNLT2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13124.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +9.8 | 1e-19 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.36×** | +9.2 | 2e-17 | 21/34 (SW480, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +7.3 | 6e-11 | 12/27 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +6.5 | 9e-09 | 4/15 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +6.0 | 3e-07 | 10/30 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.5 | 4e-06 | 3/14 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +4.8 | 1e-04 | 10/36 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.72×** | +4.1 | 0.003 | 4/31 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +3.9 | 0.006 | 1/7 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.7 | 0.012 | 2/14 (NCI-H1573, A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.012 | 5/38 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.020 | 4/38 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.023 | 4/22 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.025 | 7/38 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.025 | 5/37 (HT-29, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.029 | 2/22 (NCI-H1573, HT-29) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.048 | 2/37 (A-172, NCI-H460) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.056 | 1/36 (MIA PaCa-2) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.72×** | +3.0 | 0.076 | 3/28 (SW480, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13124.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -4.3 | 0.008 | 8/37 (HOP62, H4, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.682×** | -3.7 | 0.067 | 6/37 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.708×** | -3.6 | 0.067 | 10/30 (A-172, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.810× | -3.2 | 0.19 | 9/37 (CFPAC-1, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13124. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.2 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -10.3) |
| [[A-172 (line)]] | wt | 36.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -10.5) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.224× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 7.73 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0814× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.209× (z -10.2) |
| [[A-427 (line)]] | wt | 2.64 | 0 | 1 (1 ⚠) | — | [[olaparib (drug)]] 0.05 µM 0.0553× (z -8.7) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 16.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 2.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +9.7) | — |
| [[A498 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.858 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13124), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM4SF19-DYNLT2B]] | +0.64 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[PLEKHM1]] | +0.62 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[TM4SF19]] | +0.60 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[PLEKHM1P1]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[BACE2]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SIRT7]] | +0.55 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[FMNL1-DT]] | +0.55 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[BIN3]] | +0.55 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[ARHGAP27]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ZNF778]] | +0.55 | +0.27 / +0.59 | both halves | 3e-04 |  |
| [[LPAR2]] | +0.55 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[C19orf25]] | +0.55 | +0.43 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH1A1]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ATRAID]] | -0.50 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[COQ2]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[PCCB]] | -0.49 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ATP5F1A]] | -0.49 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[CAND1]] | -0.48 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[SH3BGRL2]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[PIGK]] | -0.48 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[TMEM123]] | -0.48 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[CD99L2]] | -0.47 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[TOP2B]] | -0.47 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[PYURF]] | -0.46 | -0.49 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD11]] | B | CARD11 activity raises LAT's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.62× lower at baseline in the lines without CARD11 | 0.071 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[MAP2K1]] | B | MAP2K1 activity raises LAT's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNLT2B]] | B | LAT activity raises DYNLT2B's level | lines that do not express LAT (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without LAT | 0.038 | ⚠ within organs, on part of the lines; also absent: FRG1BP; maybe low, not absent |
| [[SPRED3]] | B | LAT activity raises SPRED3's level | lines that do not express LAT (7) vs lines expressing it (43) | 1.59× lower at baseline in the lines without LAT | 0.093 | ⚠ within organs, on part of the lines; also absent: FRG1BP; maybe low, not absent |
| [[CTNS]] | B | LAT activity raises CTNS's level | lines that do not express LAT (7) vs lines expressing it (43) | 1.19× lower at baseline in the lines without LAT | 0.098 | ⚠ within organs, on part of the lines; also absent: FRG1BP; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.3, 54.2); signed map (0.5, 36.1). **Vector** length 46.5, 5.95% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.8 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.7 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +7.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.4 | +4.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.1 | +3.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | linker for activation of T cells |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:28,984,826-28,990,784 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LAT1 |
| Reactome | 15 pathways, smallest: Generation of second messenger molecules; DAP12 signaling; FCERI mediated Ca+2 mobilization |
| Matched by | ensembl_id |

**Function**, from UniProt [O43561](https://www.uniprot.org/uniprotkb/O43561) (Linker for activation of T-cells family member 1):

> Required for TCR (T-cell antigen receptor)- and pre-TCR-mediated signaling, both in mature T-cells and during their development. Involved in FCGR3 (low affinity immunoglobulin gamma Fc region receptor III)-mediated signaling in natural killer cells and FCER1 (high affinity immunoglobulin epsilon receptor)-mediated signaling in mast cells. Couples activation of these receptors and their associated kinases with distal intracellular events such as mobilization of intracellular calcium stores, PKC …

**Summary**, from NCBI Gene [27040](https://www.ncbi.nlm.nih.gov/gene/27040):

> The protein encoded by this gene is phosphorylated by ZAP-70/Syk protein tyrosine kinases following activation of the T-cell antigen receptor (TCR) signal transduction pathway. This transmembrane protein localizes to lipid rafts and acts as a docking site for SH2 domain-containing proteins. Upon phosphorylation, this protein recruits multiple adaptor proteins and downstream signaling molecules into multimolecular signaling complexes located near the site of TCR engagement. Alternative splicing …

**Accessions** — [HGNC:18874](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18874) · Entrez [27040](https://www.ncbi.nlm.nih.gov/gene/27040) · UniProt [O43561](https://www.uniprot.org/uniprotkb/O43561) · Ensembl [ENSG00000213658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213658)

## Data

Gene col 13124: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13124); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13124, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13124]; `tensor/DDL_lfc|DDL_z.npy` [13124]; `embed/gene_vectors.npy` [13124]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13124 or target_col == 13124). Every well: [[LAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
