---
symbol: "FAM111A-DT"
type: "gene"
col: 14434
ensembl_id: "ENSG00000245571"
name: "FAM111A divergent transcript"
location: "11q12.1"
module: 14
arm: "+"
pooled_cpm: 2.7
n_lines_expressing: 48
n_dd_up: 36
n_dd_down: 7
n_dd_up_clean: 30
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# FAM111A-DT

*FAM111A divergent transcript* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.28× (z +12.0, q 1e-30, up in 21 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.526× (z -6.7, q 1e-08, down in 18 of 42 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.546× (z -6.3, q 1e-07, down in 15 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIFA]] (+0.73, fdr 7e-06), [[PAXIP1-AS2]] (+0.68, fdr 1e-05), [[STAT5A]] (+0.67, fdr 2e-05); moves opposite to [[CAP1]] (-0.62, fdr 1e-05), [[MLXIP]] (-0.60, fdr 5e-05), [[MICAL2]] (-0.59, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ILDR1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CREB3L4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14434.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +12.0 | 1e-30 | 21/28 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +10.1 | 1e-21 | 19/29 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +9.8 | 3e-20 | 1/6 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.71×** | +7.8 | 9e-13 | 10/42 (A-427, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +7.4 | 2e-11 | 17/24 (SNU-423, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.03×** | +7.3 | 2e-11 | 21/42 (KATO III, LS 180, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +6.9 | 3e-10 | 15/31 (RPMI-7951, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +5.8 | 6e-07 | 2/7 (HEC-1-A, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.3 | 8e-06 | 3/13 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +5.2 | 1e-05 | 10/35 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.71×** | +5.0 | 3e-05 | 5/29 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +4.9 | 6e-05 | 13/43 (NCI-H2347, J82, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.7 | 1e-04 | 13/41 (NCI-H2347, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +4.6 | 2e-04 | 10/41 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.64×** | +4.6 | 2e-04 | 5/32 (LoVo, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.41×** | +4.4 | 4e-04 | 9/40 (HEC-1-A, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +4.0 | 0.002 | 5/37 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.003 | 6/43 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14434.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.526×** | -6.7 | 1e-08 | 18/42 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.546×** | -6.3 | 1e-07 | 15/37 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.610×** | -5.1 | 5e-05 | 15/34 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.652×** | -4.4 | 0.001 | 12/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.657×** | -4.4 | 0.001 | 15/36 (SW480, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.458×** | -4.2 | 0.002 | 9/28 (NCI-H1573, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.715×** | -3.5 | 0.039 | 6/41 (RPMI-7951, NCI-H23, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.715× | -3.1 | 0.13 | 7/36 (NCI-H460, Panc 03.27, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.815× | -3.0 | 0.16 | 5/39 (RPMI-7951, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14434. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 4.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 1.20 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0465× (z -8.5) |
| [[PANC-1 (line)]] | alt | 3.40 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.141× (z -8.7) |
| [[SW480 (line)]] | alt | 2.59 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.119× (z -8.6) |
| [[A-172 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.907 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.723 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.819 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.800 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.713 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14434), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIFA]] | +0.73 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[PAXIP1-AS2]] | +0.68 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[STAT5A]] | +0.67 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[ATP23]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.65 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[BTN2A2]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[DENND2B]] | +0.64 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[BTN3A1]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TCEAL1]] | +0.62 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[TAPBPL]] | +0.61 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[CFAP418]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[STAP2]] | +0.60 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAP1]] | -0.62 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[MLXIP]] | -0.60 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[MICAL2]] | -0.59 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[RRP7BP-1]] | -0.58 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[ZBED4]] | -0.58 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[S100A16]] | -0.57 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[TBC1D16]] | -0.57 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[LRRFIP1]] | -0.56 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[ACOT7]] | -0.56 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[SLC27A4]] | -0.56 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[MYO9B]] | -0.55 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[NIBAN2]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ILDR1]] | B | ILDR1 activity raises FAM111A-DT's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 1.53× lower at baseline in the lines without ILDR1 | 0.068 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1 |
| [[FAM111A]] | C | FAM111A activity raises FAM111A-DT's level | lines that do not express FAM111A (3) vs lines expressing it (47) | 2.17× lower at baseline in the lines without FAM111A | 0.062 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREB3L4]] | C | FAM111A-DT's natural level strengthens CREB3L4's drug response | FAM111A-DT's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.15; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.9, 5.3); signed map (43.6, 5.2). **Vector** length 48.7, 6.62% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +7.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.6 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +12.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +5.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +3.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.0 | +2.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -1.6 |
|  | [[EX229 (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | FAM111A divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q12.1 — chr11:59,130,133-59,143,015 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53752) · Entrez [101927204](https://www.ncbi.nlm.nih.gov/gene/101927204) · Ensembl [ENSG00000245571](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245571)

## Data

Gene col 14434: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14434); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14434, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14434]; `tensor/DDL_lfc|DDL_z.npy` [14434]; `embed/gene_vectors.npy` [14434]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14434 or target_col == 14434). Every well: [[FAM111A-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM111A-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
