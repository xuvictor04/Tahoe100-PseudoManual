---
symbol: "ALDH4A1"
type: "gene"
col: 8254
ensembl_id: "ENSG00000159423"
name: "aldehyde dehydrogenase 4 family member A1"
location: "1p36.13"
module: 154
arm: "+"
pooled_cpm: 4.87
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# ALDH4A1

*aldehyde dehydrogenase 4 family member A1* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.86× (z +23.5, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.678× (z -4.7, q 0.001, down in 11 of 44 measured lines).
> Its strongest partners by |cos| (63 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 38 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTN4]] (+0.52, fdr 1e-04), [[ADCK5]] (+0.52, fdr 3e-04), [[RMC1]] (+0.51, fdr 2e-04); moves opposite to [[ARMCX5-GPRASP2]] (-0.55, fdr 0.003, ⚠ not reproduced), [[ZNF616]] (-0.50, fdr 0.001, ⚠ not reproduced), [[MTRF1]] (-0.49, fdr 0.003, ⚠ not reproduced), [[POLR1HASP]] (-0.48, fdr 1e-04), [[TMEM161B-DT]] (-0.45, fdr 1e-04), [[VPS13B-DT]] (-0.44, fdr 2e-04).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MYO1E]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8254.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.86×** | +23.5 | 0e+00 | 44/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.61×** | +21.0 | 0e+00 | 42/44 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.02×** | +19.7 | 0e+00 | 39/44 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +16.5 | 0e+00 | 31/38 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.20×** | +14.2 | 1e-43 | 20/20 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.35×** | +14.2 | 1e-43 | 4/6 (BT-474, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.77×** | +12.4 | 1e-33 | 36/45 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.69×** | +11.2 | 5e-27 | 9/12 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +9.3 | 1e-18 | 19/39 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.97×** | +8.3 | 7e-15 | 22/37 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.72×** | +6.4 | 9e-09 | 9/44 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.67×** | +6.0 | 8e-08 | 9/25 (LoVo, A-427, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.56×** | +5.2 | 1e-05 | 12/35 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +4.4 | 5e-04 | 12/44 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.43×** | +4.3 | 6e-04 | 10/44 (LS 180, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.008 | 9/44 (LS 180, HOP62, …) | top dose only | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.031 | 5/44 (A549, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.044 | 7/42 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8254.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.678×** | -4.7 | 0.001 | 11/44 (HepG2/C3A, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.706×** | -4.2 | 0.006 | 7/46 (HepG2/C3A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.752×** | -3.5 | 0.100 | 10/43 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mifepristone (drug)]] 5 µM |  | 0.762× | -3.2 | 0.19 | 10/43 (AsPC-1, SK-MEL-2, …) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | 0.776× | -3.1 | 0.19 | 3/36 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.704× | -3.0 | 0.19 | 3/46 (SW480, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.781× | -3.0 | 0.19 | 14/42 (HepG2/C3A, SNU-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.624× | -3.0 | 0.19 | 5/44 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8254. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.31 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.37× (z +10.1) | — |
| [[C32 (line)]] | wt | 5.02 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0755× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 3.03 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0686× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 57.9 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.364× (z -9.3) |
| [[LS 180 (line)]] | wt | 4.17 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.5× (z +8.7) | — |
| [[SW480 (line)]] | alt | 4.60 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.12× (z +8.8) | — |
| [[A-172 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8254), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 20 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTN4]] | +0.52 | +0.36 / +0.36 | both halves | 1e-04 |  |
| [[ADCK5]] | +0.52 | +0.27 / +0.38 | both halves | 3e-04 |  |
| [[RMC1]] | +0.51 | +0.32 / +0.34 | both halves | 2e-04 |  |
| [[LIPE]] | +0.51 | +0.36 / +0.40 | both halves | 9e-05 |  |
| [[RHPN1]] | +0.50 | +0.26 / +0.35 | both halves | 4e-04 |  |
| [[DAG1]] | +0.50 | +0.32 / +0.44 | both halves | 2e-04 |  |
| [[MAPKAPK2]] | +0.49 | +0.21 / +0.44 | both halves | 6e-04 |  |
| [[CHTF18]] | +0.49 | +0.27 / +0.38 | both halves | 3e-04 |  |
| [[MIIP]] | +0.48 | +0.27 / +0.35 | both halves | 3e-04 | same gene group |
| [[WFS1]] | +0.48 | +0.31 / +0.40 | both halves | 2e-04 |  |
| [[IFFO2]] | +0.48 | +0.44 / +0.44 | both halves | 3e-05 | ⚠ same locus (1.6 kb, same strand: neighbours can correlate without regulation) |
| [[FGFR4]] | +0.48 | +0.44 / +0.36 | both halves | 1e-04 |  |
| [[PCYT2]] | +0.48 | +0.35 / +0.42 | both halves | 1e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMCX5-GPRASP2]] | -0.55 | -0.08 / -0.45 | ⚠ not reproduced | 0.003 |  |
| [[ZNF616]] | -0.50 | -0.15 / -0.42 | ⚠ not reproduced | 0.001 |  |
| [[MTRF1]] | -0.49 | -0.10 / -0.42 | ⚠ not reproduced | 0.003 |  |
| [[POLR1HASP]] | -0.48 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[TAS2R4]] | -0.47 | -0.09 / -0.42 | ⚠ not reproduced | 0.003 |  |
| [[TMEM161B-DT]] | -0.45 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[VPS13B-DT]] | -0.44 | -0.34 / -0.29 | both halves | 2e-04 |  |
| [[THAP6]] | -0.44 | -0.07 / -0.35 | ⚠ not reproduced | 0.004 |  |
| [[NSMCE1-DT]] | -0.44 | +0.00 / -0.30 | ⚠ not reproduced | 1.00 |  |
| [[ZNF234]] | -0.43 | -0.09 / -0.45 | ⚠ not reproduced | 0.003 |  |
| [[HOXA11]] | -0.43 | -0.35 / -0.25 | both halves | 4e-04 |  |
| [[MCPH1]] | -0.43 | -0.10 / -0.36 | ⚠ not reproduced | 0.003 |  |
| [[PAAF1]] | -0.42 | -0.22 / -0.33 | both halves | 6e-04 |  |
| [[LVRN]] | -0.41 | -0.30 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1E]] | B | MYO1E activity lowers ALDH4A1's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.66× higher at baseline in the lines without MYO1E | 0.091 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.350). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.0, -0.6); signed map (-24.3, 29.3). **Vector** length 51.6, 6.38% of its response variance represented; |z| ≥ 3 in 1,068 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +14.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +23.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +11.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +21.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +0.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -3.0 |
|  | [[Afatinib (drug)]] 5 µM |  | -1.1 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 4 family member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:18,871,430-18,902,724 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P5CDh; previously ALDH4 |
| Gene groups (HGNC) | Aldehyde dehydrogenases; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: Glyoxylate metabolism and glycine degradation; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P30038](https://www.uniprot.org/uniprotkb/P30038) (Delta-1-pyrroline-5-carboxylate dehydrogenase, mitochondrial):

> Irreversible conversion of delta-1-pyrroline-5-carboxylate (P5C), derived either from proline or ornithine, to glutamate. This is a necessary step in the pathway interconnecting the urea and tricarboxylic acid cycles. The preferred substrate is glutamic gamma-semialdehyde, other substrates include succinic, glutaric and adipic semialdehydes.

**Summary**, from NCBI Gene [8659](https://www.ncbi.nlm.nih.gov/gene/8659):

> This protein belongs to the aldehyde dehydrogenase family of proteins. This enzyme is a mitochondrial matrix NAD-dependent dehydrogenase which catalyzes the second step of the proline degradation pathway, converting pyrroline-5-carboxylate to glutamate. Deficiency of this enzyme is associated with type II hyperprolinemia, an autosomal recessive disorder characterized by accumulation of delta-1-pyrroline-5-carboxylate (P5C) and proline. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:406) · Entrez [8659](https://www.ncbi.nlm.nih.gov/gene/8659) · UniProt [P30038](https://www.uniprot.org/uniprotkb/P30038) · Ensembl [ENSG00000159423](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159423)

## Data

Gene col 8254: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8254); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8254, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8254]; `tensor/DDL_lfc|DDL_z.npy` [8254]; `embed/gene_vectors.npy` [8254]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8254 or target_col == 8254). Every well: [[ALDH4A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH4A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
