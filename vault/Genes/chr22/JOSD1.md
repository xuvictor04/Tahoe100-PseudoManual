---
symbol: "JOSD1"
type: "gene"
col: 1895
ensembl_id: "ENSG00000100221"
name: "Josephin domain containing 1"
location: "22q13.1"
module: 101
arm: "+"
pooled_cpm: 44.81
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# JOSD1

*Josephin domain containing 1* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.62× (z +11.1, q 8e-26, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.433× (z -10.1, q 4e-21, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL21]] (+0.63, fdr 7e-06), [[FAM83G]] (+0.60, fdr 1e-05), [[DUSP5-DT]] (+0.58, fdr 1e-05); moves opposite to [[FASTKD3]] (-0.54, fdr 1e-05), [[TNRC6A]] (-0.54, fdr 2e-05), [[RBM26]] (-0.53, fdr 1e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00520]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1895.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +11.1 | 8e-26 | 40/48 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +9.9 | 1e-20 | 30/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +9.6 | 2e-19 | 30/42 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +6.1 | 2e-07 | 19/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +5.6 | 2e-06 | 20/42 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +4.9 | 1e-04 | 19/48 (CFPAC-1, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.22×** | +4.6 | 4e-04 | 20/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.20×** | +4.2 | 0.002 | 19/47 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +4.2 | 0.002 | 11/48 (NCI-H2030, H4, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +4.0 | 0.003 | 20/47 (RKO, LS 180, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.18× | +3.8 | 0.006 | 13/48 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.18× | +3.7 | 0.009 | 19/47 (RKO, NCI-H460, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.019 | 12/48 (SW48, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.022 | 11/48 (HOP62, A-427, …) | rises with dose | position effect removed |
| [[Infigratinib (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.025 | 12/48 (AsPC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.044 | 17/48 (NCI-H460, HCT15, …) | inconsistent across doses |  |
| [[Rimonabant (drug)]] 5 µM |  | 1.10× | +3.1 | 0.066 | 5/48 (Panc 03.27, PANC-1, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.073 | 4/48 (SW48, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.092 | 15/47 (SNU-423, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1895.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.433×** | -10.1 | 4e-21 | 40/49 (SW48, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.490×** | -8.6 | 3e-15 | 37/48 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.582×** | -6.5 | 1e-08 | 27/43 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -5.1 | 5e-05 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.704×** | -4.2 | 0.003 | 15/34 (HOP62, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.743×** | -3.6 | 0.030 | 14/47 (H4, SW48, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.857× | -3.6 | 0.030 | 16/48 (LoVo, AsPC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.874× | -3.1 | 0.12 | 10/48 (SNU-423, LS 180, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.867× | -3.1 | 0.12 | 18/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.911× | -3.1 | 0.13 | 10/48 (LoVo, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1895. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.6 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.77× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 104 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.45× (z +11.6) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.186× (z -8.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 43.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.41× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 26.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.50× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 38.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.63× (z +8.8) | — |
| [[A498 (line)]] | wt | 40.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 67.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +10.4) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 46.5 | 0 | 1 | — | [[NG25 (drug)]] 5 µM 0.0720× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 53.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.42× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 39.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.241× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 43.9 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.0794× (z -9.7) |
| [[LoVo (line)]] | wt | 76.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.05× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 61.3 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.224× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 57.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.44× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 61.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -13.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 70.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0794× (z -10.4) |
| [[A549 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 39.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1895), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL21]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[FAM83G]] | +0.60 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[DUSP5-DT]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[WDR45]] | +0.57 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[MAFK]] | +0.56 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SOWAHC]] | +0.55 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[WNT9A]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[NOP14-AS1]] | +0.55 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[PEA15]] | +0.54 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[AGO2]] | +0.54 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[GNG4]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[TBILA]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FASTKD3]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[TNRC6A]] | -0.54 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[RBM26]] | -0.53 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[MED23]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[SLC25A12]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[TENT2]] | -0.52 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[PTCD3]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[MRPL22]] | -0.52 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[NUP54]] | -0.51 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[MTF2]] | -0.50 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SPATA7]] | -0.50 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[TADA1]] | -0.50 | -0.38 / -0.51 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00520]] | B | LINC00520 activity raises JOSD1's level | lines that do not express LINC00520 (31) vs lines expressing it (19) | 1.31× lower at baseline in the lines without LINC00520 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, LINC00589, LINC02930 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.9, -3.9); signed map (3.8, 33.2). **Vector** length 103, 23.3% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.6 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +5.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.4 | +4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.1 | +4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.5 | -10.1 |
|  | [[NG25 (drug)]] 5 µM |  | -5.0 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -8.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -3.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.5 | -4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | Josephin domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,685,543-38,701,556 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0063 |
| Gene groups (HGNC) | JOSD family MJD deubiquinating enzymes |
| Reactome | 2 pathways, smallest: Josephin domain DUBs; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15040](https://www.uniprot.org/uniprotkb/Q15040) (Josephin-1):

> Deubiquitinates monoubiquitinated probes (in vitro). When ubiquitinated, cleaves 'Lys-63'-linked and 'Lys-48'-linked poly-ubiquitin chains (in vitro), hence may act as a deubiquitinating enzyme. May increase macropinocytosis and suppress clathrin- and caveolae-mediated endocytosis. May enhance membrane dynamics and cell motility independently of its catalytic activity.

**Summary**, from NCBI Gene [9929](https://www.ncbi.nlm.nih.gov/gene/9929):

> Predicted to enable cysteine-type deubiquitinase activity. Predicted to be involved in proteolysis. Predicted to act upstream of or within several processes, including endocytosis; membrane biogenesis; and protein deubiquitination. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28953](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28953) · Entrez [9929](https://www.ncbi.nlm.nih.gov/gene/9929) · UniProt [Q15040](https://www.uniprot.org/uniprotkb/Q15040) · Ensembl [ENSG00000100221](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100221)

## Data

Gene col 1895: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1895); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1895, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1895]; `tensor/DDL_lfc|DDL_z.npy` [1895]; `embed/gene_vectors.npy` [1895]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1895 or target_col == 1895). Every well: [[JOSD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JOSD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
