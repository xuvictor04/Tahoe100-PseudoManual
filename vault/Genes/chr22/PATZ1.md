---
symbol: "PATZ1"
type: "gene"
col: 1869
ensembl_id: "ENSG00000100105"
name: "POZ/BTB and AT hook containing zinc finger 1"
location: "22q12.2"
module: 1
arm: "+"
pooled_cpm: 7.39
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PATZ1

*POZ/BTB and AT hook containing zinc finger 1* — 22q12.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.235× (z -17.8, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF3C4]] (+0.69, fdr 7e-06), [[TGFBRAP1]] (+0.64, fdr 1e-05), [[QTRT2]] (+0.64, fdr 1e-05); moves opposite to [[SPAG9]] (-0.65, fdr 1e-05), [[NBEAL1]] (-0.64, fdr 1e-05), [[AP3S1]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF32]] → it (grade C ⚠); 1 goes from it, the strongest it → [[FEM1A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1869.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.34× | +3.6 | 0.12 | 8/46 (KATO III, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | 1.33× | +3.5 | 0.12 | 0/46 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1869.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.235×** | -17.8 | 0e+00 | 44/46 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.272×** | -16.0 | 0e+00 | 43/46 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.290×** | -15.2 | 0e+00 | 40/46 (SW48, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.444×** | -10.0 | 3e-21 | 33/46 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.472×** | -9.2 | 4e-18 | 32/46 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.600×** | -8.9 | 8e-17 | 29/43 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.531×** | -7.8 | 6e-13 | 29/44 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.535×** | -7.7 | 1e-12 | 32/45 (Hs 766T, PANC-1, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.643×** | -7.7 | 1e-12 | 28/46 (HT-29, SW1417, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.557×** | -7.2 | 4e-11 | 27/44 (NCI-H23, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.413×** | -5.7 | 7e-07 | 20/46 (NCI-H23, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.658×** | -4.9 | 4e-05 | 20/44 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.673×** | -4.9 | 5e-05 | 17/42 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -4.2 | 0.001 | 17/42 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.703×** | -4.2 | 0.001 | 18/38 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.722×** | -4.0 | 0.002 | 14/43 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.729×** | -3.9 | 0.004 | 13/46 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1869. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.27 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.169× (z -10.9) |
| [[BT-474 (line)]] | alt | 16.3 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0970× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0728× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.0780× (z -14.5) |
| [[SW480 (line)]] | alt | 6.88 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.130× (z -13.4) |
| [[A498 (line)]] | wt | 6.02 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.118× (z -11.4) |
| [[C-33 A (line)]] | alt | 32.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -13.6) |
| [[MIA PaCa-2 (line)]] | alt | 8.29 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0749× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 6.32 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -10.0) |
| [[A-427 (line)]] | wt | 9.44 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0469× (z -15.4) |
| [[A549 (line)]] | wt | 6.48 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.121× (z -9.1) |
| [[J82 (line)]] | alt | 5.89 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0442× (z -13.2) |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 5.04 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0325× (z -12.1) |
| [[SW48 (line)]] | wt | 16.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0242× (z -15.9) |
| [[CFPAC-1 (line)]] | alt | 5.34 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0559× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 8.20 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -9.2) |
| [[HOP62 (line)]] | alt | 4.91 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0757× (z -11.3) |
| [[Hs 766T (line)]] | wt | 4.63 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0863× (z -8.5) |
| [[HS-578T (line)]] | alt | 3.66 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0274× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 7.51 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0950× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[LS 180 (line)]] | wt | 8.90 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0718× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 8.12 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0833× (z -13.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 6.17 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0549× (z -11.3) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SNU-423 (line)]] | alt | 4.99 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0424× (z -10.9) |
| [[A-172 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1869), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C4]] | +0.69 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[TGFBRAP1]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[QTRT2]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[DUS3L]] | +0.64 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ZNF507]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 | same gene group |
| [[ZBTB45]] | +0.62 | +0.51 / +0.57 | both halves | 1e-05 | same gene group |
| [[NUDT19]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[FIZ1]] | +0.62 | +0.48 / +0.56 | both halves | 2e-05 | same gene group |
| [[JADE2]] | +0.62 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[HNRNPF]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ZNF362]] | +0.61 | +0.54 / +0.47 | both halves | 2e-05 | same gene group |
| [[SMAD1]] | +0.61 | +0.53 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | -0.65 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[NBEAL1]] | -0.64 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[AP3S1]] | -0.61 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[F11R]] | -0.59 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PPP1R21]] | -0.58 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[SLC17A7]] | -0.57 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[MAGT1]] | -0.56 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[CAST]] | -0.56 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[RRAS]] | -0.55 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[ARFGAP3]] | -0.55 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[CCNI]] | -0.55 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[SYP]] | -0.54 | -0.35 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF32]] | C | ZNF32 activity raises PATZ1's level | lines that do not express ZNF32 (4) vs lines expressing it (46) | 1.85× lower at baseline in the lines without ZNF32 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF221, ZNF540; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FEM1A]] | C | PATZ1's natural level weakens FEM1A's drug response | PATZ1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.37; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-7.3, 9.7); signed map (3.9, -40.0). **Vector** length 68.3, 11.5% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.0 | +3.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.2 | -1.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +1.8 | -4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.4 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -3.8 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.8 | -4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | +0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -7.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | POZ/BTB and AT hook containing zinc finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:31,325,804-31,346,346 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAZR, dJ400N23, ZBTB19, ZSG, RIAZ, PATZ; previously ZNF278 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBE1](https://www.uniprot.org/uniprotkb/Q9HBE1) (POZ-, AT hook-, and zinc finger-containing protein 1):

> Transcriptional regulator that plays a role in many biological processes such as embryogenesis, senescence, T-cell development or neurogenesis. Interacts with the TP53 protein to control genes that are important in proliferation and in the DNA-damage response. Mechanistically, the interaction inhibits the DNA binding and transcriptional activity of TP53/p53. Part of the transcriptional network modulating regulatory T-cell development and controls the generation of the regulatory T-cell pool …

**Summary**, from NCBI Gene [23598](https://www.ncbi.nlm.nih.gov/gene/23598):

> The protein encoded by this gene contains an A-T hook DNA binding motif which usually binds to other DNA binding structures to play an important role in chromatin modeling and transcription regulation. Its Poz domain is thought to function as a site for protein-protein interaction and is required for transcriptional repression, and the zinc-fingers comprise the DNA binding domain. Since the encoded protein has typical features of a transcription factor, it is postulated to be a repressor of …

**Accessions** — [HGNC:13071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13071) · Entrez [23598](https://www.ncbi.nlm.nih.gov/gene/23598) · UniProt [Q9HBE1](https://www.uniprot.org/uniprotkb/Q9HBE1) · Ensembl [ENSG00000100105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100105)

## Data

Gene col 1869: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1869); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1869, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1869]; `tensor/DDL_lfc|DDL_z.npy` [1869]; `embed/gene_vectors.npy` [1869]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1869 or target_col == 1869). Every well: [[PATZ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PATZ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
