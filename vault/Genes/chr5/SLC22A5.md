---
symbol: "SLC22A5"
type: "gene"
col: 12390
ensembl_id: "ENSG00000197375"
name: "solute carrier family 22 member 5"
location: "5q31.1"
module: 13
arm: "+"
pooled_cpm: 11.67
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SLC22A5

*solute carrier family 22 member 5* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.31× (z +3.9, q 0.034, up in 2 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.617× (z -7.0, q 1e-09, down in 23 of 46 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.493× (z -5.4, q 1e-05, down in 17 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTARC2]] (+0.53, fdr 1e-05), [[GSEC]] (+0.53, fdr 1e-05), [[MIR3936HG]] (+0.52, fdr 1e-05, ⚠ same locus), [[JDP2]] (+0.51, fdr 4e-05); moves opposite to [[BZW1]] (-0.52, fdr 1e-05), [[WWTR1]] (-0.51, fdr 3e-05), [[WFDC3]] (-0.51, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12390.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.034 | 2/46 (HOP62, A-172) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.034 | 10/37 (A-427, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +3.7 | 0.034 | 5/47 (NCI-H460, NCI-H2347, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.7 | 0.035 | 12/47 (J82, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +3.5 | 0.048 | 5/21 (A549, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.048 | 10/47 (NCI-H460, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.048 | 5/46 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.17× | +3.2 | 0.11 | 5/47 (PANC-1, Panc 03.27, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.25× | +3.1 | 0.12 | 9/45 (NCI-H460, HepG2/C3A, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.12 | 12/45 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.12 | 7/45 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.24× | +3.0 | 0.12 | 9/44 (NCI-H460, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12390.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.617×** | -7.0 | 1e-09 | 23/46 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.683×** | -5.5 | 9e-06 | 20/44 (NCI-H460, RKO, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.493×** | -5.4 | 1e-05 | 17/44 (A-427, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.707×** | -5.0 | 7e-05 | 18/46 (A498, RKO, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.755×** | -4.1 | 0.005 | 17/46 (NCI-H23, Panc 03.27, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.752×** | -4.0 | 0.006 | 12/42 (A-172, H4, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.609×** | -3.8 | 0.014 | 15/42 (HT-29, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.839× | -3.6 | 0.022 | 20/44 (NCI-H460, LoVo, …) | top dose only | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.855× | -3.2 | 0.075 | 20/47 (SW48, Hs 766T, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.857× | -3.2 | 0.075 | 7/47 (A498, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.804×** | -3.2 | 0.075 | 17/46 (NCI-H460, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.805×** | -3.2 | 0.075 | 12/46 (SW 1271, HOP62, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.811× | -3.0 | 0.10 | 7/47 (A498, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12390. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 6 (6 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.149× (z -13.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 24.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.101× (z -9.3) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.188× (z -8.8) |
| [[A-172 (line)]] | wt | 9.46 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -12.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 1 | — | [[Dexmedetomidine (drug)]] 0.05 µM 0.0539× (z -8.9) |
| [[H4 (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Hs 766T (line)]] | wt | 8.68 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.101× (z -9.2) |
| [[KATO III (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 4.28 | 0 | 1 | — | [[Adenine (drug)]] 0.5 µM 0.0660× (z -8.6) |
| [[SW48 (line)]] | wt | 15.1 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.239× (z -8.7) |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12390), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTARC2]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[GSEC]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[MIR3936HG]] | +0.52 | +0.51 / +0.61 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[JDP2]] | +0.51 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[SLC39A14]] | +0.50 | +0.44 / +0.51 | both halves | 3e-05 | pathway: SLC-mediated transmembrane transport |
| [[TPD52L1]] | +0.50 | +0.44 / +0.46 | both halves | 3e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[ZFAND1]] | +0.50 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[TRIM29]] | +0.49 | +0.40 / +0.44 | both halves | 5e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[PRDM16]] | +0.49 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[FBXW8]] | +0.48 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[ACSS1]] | +0.48 | +0.55 / +0.40 | both halves | 5e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[PIK3C2B]] | +0.48 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[PPA2]] | +0.48 | +0.37 / +0.49 | both halves | 8e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BZW1]] | -0.52 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[WWTR1]] | -0.51 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[WFDC3]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[WFDC10B]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[NT5E]] | -0.48 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[ITGA2-AS1]] | -0.47 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[CD59]] | -0.46 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ARPC2]] | -0.45 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[FKBP3]] | -0.45 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[ITGA2]] | -0.45 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[DCBLD2]] | -0.44 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[TPI1]] | -0.44 | -0.42 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STC1]] | B | STC1 activity lowers SLC22A5's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.31× higher at baseline in the lines without STC1 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction -0.242). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.6, 39.0); signed map (40.3, -13.5). **Vector** length 69.1, 10.9% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +2.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.3 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.8 | +2.8 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.5 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.0 | -5.0 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | -1.9 | -3.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.8 | -3.2 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -2.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 22 member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:132,369,710-132,395,613 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OCTN2, SCD; previously CDSP |
| Gene groups (HGNC) | Solute carrier family 22 |
| Hallmark sets | FATTY_ACID_METABOLISM, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 8 pathways, smallest: SLC-mediated transport of organic cations; Carnitine shuttle; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [O76082](https://www.uniprot.org/uniprotkb/O76082) (Organic cation/carnitine transporter 2):

> Sodium-ion dependent, high affinity carnitine transporter. Involved in the active cellular uptake of carnitine. Transports one sodium ion with one molecule of carnitine. Also transports organic cations such as tetraethylammonium (TEA) without the involvement of sodium. Relative uptake activity ratio of carnitine to TEA is 11.3. In intestinal epithelia, transports the quorum-sensing pentapeptide CSF (competence and sporulation factor) from B.subtilis which induces cytoprotective heat shock …

**Summary**, from NCBI Gene [6584](https://www.ncbi.nlm.nih.gov/gene/6584):

> Polyspecific organic cation transporters in the liver, kidney, intestine, and other organs are critical for elimination of many endogenous small organic cations as well as a wide array of drugs and environmental toxins. The encoded protein is a plasma integral membrane protein which functions both as an organic cation transporter and as a sodium-dependent high affinity carnitine transporter. The encoded protein is involved in the active cellular uptake of carnitine. Mutations in this gene are …

**Accessions** — [HGNC:10969](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10969) · Entrez [6584](https://www.ncbi.nlm.nih.gov/gene/6584) · UniProt [O76082](https://www.uniprot.org/uniprotkb/O76082) · Ensembl [ENSG00000197375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197375)

## Data

Gene col 12390: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12390); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12390, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12390]; `tensor/DDL_lfc|DDL_z.npy` [12390]; `embed/gene_vectors.npy` [12390]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12390 or target_col == 12390). Every well: [[SLC22A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC22A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
