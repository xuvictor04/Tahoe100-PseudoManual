---
symbol: "TNFRSF25"
type: "gene"
col: 13275
ensembl_id: "ENSG00000215788"
name: "TNF receptor superfamily member 25"
location: "1p36.31"
module: 34
arm: "+"
pooled_cpm: 4.65
n_lines_expressing: 46
n_dd_up: 5
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# TNFRSF25

*TNF receptor superfamily member 25* — 1p36.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.80× (z +4.8, q 0.001, up in 1 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 2.34× (z +4.5, q 0.002, up in 12 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.466× (z -9.2, q 2e-17, down in 26 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHG5]] (+0.78, fdr 7e-06, ⚠ same locus), [[LTBP4]] (+0.66, fdr 7e-06), [[PLA2G4B]] (+0.64, fdr 1e-05), [[SIGIRR]] (+0.62, fdr 1e-05); moves opposite to [[CASD1]] (-0.57, fdr 3e-05), [[TBC1D5]] (-0.56, fdr 2e-05), [[MBNL3]] (-0.52, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLEKHG5]] → it (grade C ⚠); 2 go from it, the strongest it → cells under [[Radotinib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13275.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +4.8 | 0.001 | 1/8 (PANC-1) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.34×** | +4.5 | 0.002 | 12/34 (NCI-H23, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **2.04×** | +3.7 | 0.036 | 8/34 (HOP62, A-172, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.59×** | +3.6 | 0.042 | 10/30 (NCI-H2030, Hs 766T, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.069 | 14/37 (NCI-H460, HOP62, …) | two highest doses | low cells (technical?); position effect removed |
| [[PH-797804 (drug)]] 0.5 µM |  | 1.86× | +3.3 | 0.10 | 4/33 (LoVo, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 2.29× | +3.2 | 0.13 | 4/12 (HOP62, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.80× | +3.1 | 0.15 | 3/31 (NCI-H1573, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13275.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.466×** | -9.2 | 2e-17 | 26/35 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.330×** | -9.1 | 4e-17 | 27/38 (SW48, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.487×** | -8.6 | 9e-16 | 27/36 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.362×** | -8.6 | 9e-16 | 27/38 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.475×** | -6.3 | 3e-08 | 24/42 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.212×** | -5.9 | 3e-07 | 24/35 (HCT15, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.498×** | -5.9 | 3e-07 | 19/41 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.549×** | -5.1 | 2e-05 | 18/31 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.531×** | -5.1 | 3e-05 | 21/34 (NCI-H2030, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.664×** | -4.9 | 5e-05 | 16/41 (CFPAC-1, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.575×** | -4.5 | 3e-04 | 19/34 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.578×** | -4.5 | 3e-04 | 17/32 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.601×** | -4.3 | 6e-04 | 22/40 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.582×** | -4.3 | 6e-04 | 14/40 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.368×** | -3.8 | 0.005 | 13/33 (NCI-H1573, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.667×** | -3.2 | 0.046 | 5/41 (C-33 A, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 25.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.2) |
| [[LoVo (line)]] | wt | 8.01 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 8.80 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0526× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 7.47 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 7.58 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 6.93 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0682× (z -10.8) |
| [[A498 (line)]] | wt | 3.08 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0228× (z -13.3) |
| [[COLO 205 (line)]] | alt | 6.36 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0583× (z -8.7) |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0478× (z -12.2) |
| [[HOP62 (line)]] | alt | 7.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -9.2) |
| [[HT-29 (line)]] | alt | 4.78 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0796× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 3.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0505× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 3.45 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -11.8) |
| [[SW48 (line)]] | wt | 7.91 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0431× (z -9.1) |
| [[A-172 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHG5]] | +0.78 | +0.80 / +0.75 | both halves | 7e-06 | ⚠ same locus (0.9 kb, same strand: neighbours can correlate without regulation) |
| [[LTBP4]] | +0.66 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PLA2G4B]] | +0.64 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[SIGIRR]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PEAR1]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[GDPD5]] | +0.60 | +0.59 / +0.38 | both halves | 7e-05 |  |
| [[FCHSD1]] | +0.60 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[LYPD3]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SEMA3F]] | +0.59 | +0.57 / +0.43 | both halves | 4e-05 |  |
| [[GPSM1]] | +0.59 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[GDI1]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[TCIRG1]] | +0.57 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[MAPK11]] | +0.56 | +0.59 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASD1]] | -0.57 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[TBC1D5]] | -0.56 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[MBNL3]] | -0.52 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[NCOA4]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ZMYND11]] | -0.52 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[YAP1]] | -0.51 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[ATRAID]] | -0.51 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[CHRAC1]] | -0.50 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[ZRANB2-DT]] | -0.50 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[LEPROT]] | -0.49 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[ENOSF1]] | -0.49 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[PTGR2]] | -0.49 | -0.39 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG5]] | C | PLEKHG5's natural level strengthens TNFRSF25's drug response | PLEKHG5's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.58; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Radotinib (drug)]] 5 µM | C | TNFRSF25 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express TNFRSF25 (4) vs lines expressing it (44) | the lines without TNFRSF25: 0.81× the cells of the other lines | 0.014 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PLEKHG5, ENSG00000284716 |
| cells under [[Ixazomib citrate (drug)]] 0.5 µM | C | TNFRSF25 activity raises the cells' numbers under Ixazomib citrate 0.5 µM (protects the cells) | lines that do not express TNFRSF25 (4) vs lines expressing it (44) | the lines without TNFRSF25: 0.63× the cells of the other lines | 0.024 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PLEKHG5, ENSG00000284716 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, -2.6); signed map (-6.6, 46.1). **Vector** length 68.1, 12.6% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | -2.4 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.2 | +3.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.2 | +4.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.0 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +3.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -8.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.9 | -3.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:6,460,786-6,466,175 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DR3, TRAMP, WSL-1, LARD, WSL-LR, DDR3, TR3, APO-3; previously TNFRSF12 |
| Gene groups (HGNC) | Tumor necrosis factor receptor superfamily |
| Reactome | 3 pathways, smallest: TNFs bind their physiological receptors; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93038](https://www.uniprot.org/uniprotkb/Q93038) (Tumor necrosis factor receptor superfamily member 25):

> Receptor for TNFSF12/APO3L/TWEAK. Interacts directly with the adapter TRADD. Mediates activation of NF-kappa-B and induces apoptosis. May play a role in regulating lymphocyte homeostasis.

**Summary**, from NCBI Gene [8718](https://www.ncbi.nlm.nih.gov/gene/8718):

> The protein encoded by this gene is a member of the TNF-receptor superfamily. This receptor is expressed preferentially in the tissues enriched in lymphocytes, and it may play a role in regulating lymphocyte homeostasis. This receptor has been shown to stimulate NF-kappa B activity and regulate cell apoptosis. The signal transduction of this receptor is mediated by various death domain containing adaptor proteins. Knockout studies in mice suggested the role of this gene in the removal of …

**Accessions** — [HGNC:11910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11910) · Entrez [8718](https://www.ncbi.nlm.nih.gov/gene/8718) · UniProt [Q93038](https://www.uniprot.org/uniprotkb/Q93038) · Ensembl [ENSG00000215788](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215788)

## Data

Gene col 13275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13275); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13275]; `tensor/DDL_lfc|DDL_z.npy` [13275]; `embed/gene_vectors.npy` [13275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13275 or target_col == 13275). Every well: [[TNFRSF25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
