---
symbol: "FBXO48"
type: "gene"
col: 12935
ensembl_id: "ENSG00000204923"
name: "F-box protein 48"
location: "2p13.3"
module: 80
arm: "+"
pooled_cpm: 3.05
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# FBXO48

*F-box protein 48* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.31× (z +15.9, q 0e+00, up in 34 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.498× (z -5.4, q 5e-05, down in 24 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMC9]] (+0.66, fdr 7e-06), [[PDCL3P4]] (+0.66, fdr 2e-05), [[BOLA1]] (+0.65, fdr 7e-06); moves opposite to [[CPSF4]] (-0.63, fdr 1e-05), [[STRAP]] (-0.60, fdr 1e-05), [[DUXAP9]] (-0.59, fdr 1e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02175]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12935.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.31×** | +15.9 | 0e+00 | 34/34 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.26×** | +12.8 | 4e-35 | 34/36 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.65×** | +9.5 | 3e-19 | 4/5 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.10×** | +8.7 | 6e-16 | 10/14 (A549, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.88×** | +7.8 | 7e-13 | 36/41 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.59×** | +7.3 | 3e-11 | 34/46 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.57×** | +7.2 | 4e-11 | 34/44 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.56×** | +7.2 | 4e-11 | 32/44 (A549, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.63×** | +7.1 | 7e-11 | 17/30 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +5.6 | 1e-06 | 3/4 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.91×** | +5.0 | 4e-05 | 19/46 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +4.8 | 6e-05 | 17/33 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +4.6 | 2e-04 | 16/34 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +4.1 | 0.002 | 3/45 (SW480, NCI-H23, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.70×** | +4.0 | 0.002 | 16/44 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.025 | 3/44 (KATO III, SW48, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.039 | 10/46 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.059 | 6/41 (A-172, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12935.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.498×** | -5.4 | 5e-05 | 24/43 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.531×** | -4.9 | 3e-04 | 18/46 (C-33 A, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.577×** | -4.2 | 0.004 | 16/47 (NCI-H23, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -3.8 | 0.024 | 18/42 (PANC-1, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.450× | -3.2 | 0.13 | 11/28 (NCI-H23, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.660× | -3.2 | 0.13 | 15/41 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.666× | -3.1 | 0.14 | 13/40 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.653× | -3.1 | 0.14 | 14/41 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12935. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.14 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.24× (z +11.7) | — |
| [[A-427 (line)]] | wt | 6.08 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0435× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 3.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 4.29 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0812× (z -8.5) |
| [[SW480 (line)]] | alt | 3.22 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0398× (z -13.5) |
| [[A-172 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12935), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC9]] | +0.66 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[PDCL3P4]] | +0.66 | +0.79 / +0.47 | both halves | 2e-05 |  |
| [[BOLA1]] | +0.65 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[CCDC148]] | +0.64 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[GPR137C]] | +0.63 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[APLF]] | +0.63 | +0.75 / +0.56 | both halves | 1e-05 | ⚠ same locus (0.3 kb: neighbours can correlate without regulation) |
| [[DLX2]] | +0.63 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[LETM2]] | +0.62 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[MAD2L1BP]] | +0.62 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[LINC02307]] | +0.62 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[SIX5]] | +0.62 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[ENO3]] | +0.62 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[TRIM59]] | +0.61 | +0.68 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF4]] | -0.63 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[STRAP]] | -0.60 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[DUXAP9]] | -0.59 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[UBAC2]] | -0.58 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[ACTR5]] | -0.58 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[WDR5]] | -0.58 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.58 | -0.73 / -0.46 | both halves | 3e-05 |  |
| [[ERI3]] | -0.58 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[DFFB]] | -0.57 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TOMM5]] | -0.57 | -0.65 / -0.30 | both halves | 2e-04 |  |
| [[ADAT2]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[URB1]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02175]] | B | LINC02175 activity raises FBXO48's level | lines that do not express LINC02175 (7) vs lines expressing it (43) | 1.12× lower at baseline in the lines without LINC02175 | 0.024 | ⚠ within organs, on part of the lines; also absent: CEP41, LRRIQ3, FAM182B; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FBXO48's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[S100A3]] | B | S100A3 activity lowers FBXO48's level | lines that do not express S100A3 (15) vs lines expressing it (35) | 1.24× higher at baseline in the lines without S100A3 | 0.031 | ⚠ within organs, on part of the lines; also absent: S100A4; maybe low, not absent |
| [[DUXAP9]] | B | DUXAP9 activity raises FBXO48's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.52× lower at baseline in the lines without DUXAP9 | 0.040 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.7, 9.9); signed map (19.4, -9.5). **Vector** length 56.2, 8.41% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +12.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.2 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +15.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +4.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | +2.4 | +3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +3.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.8 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -2.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 48 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:68,459,422-68,467,294 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | F-boxes other |
| Matched by | ensembl_id |

UniProt [Q5FWF7](https://www.uniprot.org/uniprotkb/Q5FWF7) carries no function annotation.

**Summary**, from NCBI Gene [554251](https://www.ncbi.nlm.nih.gov/gene/554251):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Predicted to be involved in SCF-dependent proteasomal ubiquitin-dependent protein catabolic process. Predicted to be part of SCF ubiquitin ligase complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33857) · Entrez [554251](https://www.ncbi.nlm.nih.gov/gene/554251) · UniProt [Q5FWF7](https://www.uniprot.org/uniprotkb/Q5FWF7) · Ensembl [ENSG00000204923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204923)

## Data

Gene col 12935: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12935); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12935, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12935]; `tensor/DDL_lfc|DDL_z.npy` [12935]; `embed/gene_vectors.npy` [12935]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12935 or target_col == 12935). Every well: [[FBXO48 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO48.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
