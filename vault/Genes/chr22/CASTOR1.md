---
symbol: "CASTOR1"
type: "gene"
col: 14186
ensembl_id: "ENSG00000239282"
name: "cytosolic arginine sensor for mTORC1 subunit 1"
location: "22q12.2"
module: 161
arm: "+"
pooled_cpm: 3.55
n_lines_expressing: 42
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# CASTOR1

*cytosolic arginine sensor for mTORC1 subunit 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.07× (z +6.3, q 1e-07, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.57× (z +4.1, q 0.012, up in 3 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.385× (z -8.6, q 3e-15, down in 22 of 37 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D10A]] (+0.61, fdr 1e-05, ⚠ read-through risk), [[CIB1]] (+0.61, fdr 1e-05), [[ATOSB]] (+0.61, fdr 3e-05), [[DNAAF3]] (+0.57, fdr 6e-05); moves opposite to [[RCN1]] (-0.56, fdr 1e-04), [[FUBP1]] (-0.56, fdr 1e-04), [[PRRC2B]] (-0.54, fdr 9e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14186.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +6.3 | 1e-07 | 0/6 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +4.1 | 0.012 | 3/23 (LoVo, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.44× | +3.3 | 0.17 | 2/12 (HEC-1-A, A549) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.61× | +3.1 | 0.24 | 3/22 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.61× | +3.1 | 0.24 | 2/25 (PANC-1, RPMI-7951) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.40× | +3.0 | 0.24 | 2/21 (CFPAC-1, PANC-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14186.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.385×** | -8.6 | 3e-15 | 22/37 (SHP-77, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.454×** | -7.1 | 3e-10 | 16/33 (SHP-77, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.533×** | -5.7 | 2e-06 | 20/27 (A549, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.551×** | -5.4 | 1e-05 | 20/33 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.367×** | -4.8 | 2e-04 | 16/26 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.603×** | -4.6 | 4e-04 | 15/33 (A498, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.588×** | -4.5 | 4e-04 | 18/32 (HS-578T, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.423×** | -4.1 | 0.003 | 15/29 (SHP-77, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.650×** | -3.9 | 0.006 | 12/37 (MIA PaCa-2, HS-578T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.671×** | -3.6 | 0.017 | 7/33 (NCI-H1573, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.676×** | -3.5 | 0.020 | 12/32 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.657×** | -3.5 | 0.020 | 10/37 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -3.4 | 0.025 | 17/28 (A549, HS-578T, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.689×** | -3.4 | 0.031 | 12/36 (HS-578T, A498, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.683×** | -3.2 | 0.054 | 4/34 (HCT15, LoVo, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 0.5 µM |  | **0.715×** | -3.0 | 0.083 | 1/27 (AsPC-1) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14186. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 7.50 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0871× (z -10.5) |
| [[SHP-77 (line)]] | alt | 19.8 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0430× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.153× (z -8.7) |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0720× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.196× (z -8.7) |
| [[A498 (line)]] | wt | 10.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0792× (z -15.2) |
| [[PANC-1 (line)]] | alt | 4.34 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.792 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.810 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.623 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14186), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D10A]] | +0.61 | +0.52 / +0.49 | both halves | 1e-05 | ⚠ **readthrough risk**: this gene lies 2.4 kb 3′ of TBC1D10A on the same strand (can correlate by spillover, not regulation) |
| [[CIB1]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ATOSB]] | +0.61 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[DNAAF3]] | +0.57 | +0.51 / +0.39 | both halves | 6e-05 |  |
| [[SMOX]] | +0.56 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[TRPT1]] | +0.56 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[ETHE1]] | +0.55 | +0.49 / +0.32 | both halves | 1e-04 |  |
| [[ING1]] | +0.54 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[FAM89B]] | +0.54 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[CARD19]] | +0.54 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[POLD4]] | +0.53 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[CDKN2D]] | +0.53 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[ZNRF1]] | +0.52 | +0.52 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCN1]] | -0.56 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[FUBP1]] | -0.56 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[PRRC2B]] | -0.54 | -0.42 / -0.37 | both halves | 9e-05 |  |
| [[COMT]] | -0.53 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[MTA3]] | -0.52 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[CRPPA]] | -0.52 | -0.47 / -0.21 | both halves | 6e-04 |  |
| [[SETD7]] | -0.50 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[ZMYND11]] | -0.50 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[LARP4]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[MGST1]] | -0.50 | -0.39 / -0.32 | both halves | 1e-04 |  |
| [[EWSR1]] | -0.50 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[ZFX]] | -0.50 | -0.47 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STC1]] | B | STC1 activity raises CASTOR1's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.72× lower at baseline in the lines without STC1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.3, 3.1); signed map (-28.1, 17.8). **Vector** length 58.3, 10.2% of its response variance represented; |z| ≥ 3 in 857 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +2.5 | +4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | +1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | -1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.4 | +0.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.1 | +2.3 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +0.9 | +2.0 |
|  | [[Vilanterol (drug)]] 5 µM |  | +0.9 | +0.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.0 | -5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -3.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -7.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | cytosolic arginine sensor for mTORC1 subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,285,117-30,289,622 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GATSL3 |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WTX7](https://www.uniprot.org/uniprotkb/Q8WTX7) (Cytosolic arginine sensor for mTORC1 subunit 1):

> Functions as an intracellular arginine sensor within the amino acid-sensing branch of the TORC1 signaling pathway. As a homodimer or a heterodimer with CASTOR2, binds and inhibits the GATOR subcomplex GATOR2 and thereby mTORC1. Binding of arginine to CASTOR1 allosterically disrupts the interaction of CASTOR1-containing dimers with GATOR2 which can in turn activate mTORC1 and the TORC1 signaling pathway.

**Summary**, from NCBI Gene [652968](https://www.ncbi.nlm.nih.gov/gene/652968):

> Enables several functions, including arginine binding activity; identical protein binding activity; and protein sequestering activity. Involved in cellular response to L-arginine; cellular response to amino acid starvation; and regulation of TORC1 signaling. Located in GATOR2 complex and cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34423) · Entrez [652968](https://www.ncbi.nlm.nih.gov/gene/652968) · UniProt [Q8WTX7](https://www.uniprot.org/uniprotkb/Q8WTX7) · Ensembl [ENSG00000239282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239282)

## Data

Gene col 14186: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14186); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14186, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14186]; `tensor/DDL_lfc|DDL_z.npy` [14186]; `embed/gene_vectors.npy` [14186]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14186 or target_col == 14186). Every well: [[CASTOR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASTOR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
