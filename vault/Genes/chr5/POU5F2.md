---
symbol: "POU5F2"
type: "gene"
col: 14541
ensembl_id: "ENSG00000248483"
name: "POU domain class 5, transcription factor 2"
location: "5q15"
module: 185
arm: "+"
pooled_cpm: 3.56
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# POU5F2

*POU domain class 5, transcription factor 2* — 5q15

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.436× (z -11.3, q 9e-27, down in 30 of 36 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.473× (z -10.2, q 8e-22, down in 29 of 38 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR70]] (+0.57, fdr 3e-04), [[VPS13B]] (+0.56, fdr 6e-05), [[DIS3L2]] (+0.52, fdr 3e-04); moves opposite to [[ATP23]] (-0.53, fdr 1e-04), [[RARG]] (-0.47, fdr 7e-05), [[PDE4A]] (-0.46, fdr 7e-05).
> It is in [[Module 185]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PDGFB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14541.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.44× | +3.5 | 0.10 | 11/35 (NCI-H23, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.43× | +3.5 | 0.10 | 1/45 (NCI-H460) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.45× | +3.5 | 0.10 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.40× | +3.3 | 0.16 | 7/41 (A-172, COLO 205, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.25× | +3.1 | 0.25 | 1/44 (SK-MEL-2) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14541.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.436×** | -11.3 | 9e-27 | 30/36 (NCI-H1573, HOP62, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.473×** | -10.2 | 8e-22 | 29/38 (SHP-77, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.411×** | -8.5 | 2e-15 | 32/44 (LOX-IMVI, RKO, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.422×** | -8.0 | 2e-13 | 30/42 (PANC-1, LOX-IMVI, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.456×** | -7.5 | 5e-12 | 23/34 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.467×** | -7.3 | 3e-11 | 18/33 (LoVo, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.235×** | -7.3 | 3e-11 | 29/41 (A-172, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.457×** | -7.2 | 3e-11 | 15/21 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.485×** | -7.0 | 2e-10 | 24/42 (HOP62, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.516×** | -6.3 | 1e-08 | 23/45 (HT-29, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.533×** | -5.8 | 3e-07 | 18/27 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.613×** | -4.7 | 1e-04 | 16/42 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.650×** | -4.1 | 0.002 | 14/43 (NCI-H2030, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.663×** | -3.9 | 0.003 | 15/44 (HOP62, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.673×** | -3.8 | 0.005 | 12/44 (RPMI-7951, A549, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.674×** | -3.8 | 0.005 | 13/41 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.737×** | -2.9 | 0.088 | 3/45 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Irinotecan (drug)]] 5 µM |  | **0.562×** | -2.9 | 0.093 | 4/44 (MIA PaCa-2, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.563×** | -2.9 | 0.094 | 11/33 (MIA PaCa-2, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.36 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -11.3) |
| [[PANC-1 (line)]] | alt | 4.40 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A549 (line)]] | wt | 3.04 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0735× (z -11.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 1.91 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0516× (z -8.5) |
| [[HOP62 (line)]] | alt | 3.39 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0324× (z -12.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LoVo (line)]] | wt | 3.63 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0934× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 5.20 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0813× (z -14.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 3.61 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0641× (z -9.3) |
| [[SHP-77 (line)]] | alt | 7.18 | 0 | 2 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.178× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 6.15 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0714× (z -9.8) |
| [[A-172 (line)]] | wt | 3.69 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0705× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 3.61 | 0 | 1 | — | [[Rutin (trihydrate) (drug)]] 5 µM 0.0528× (z -9.4) |
| [[HT-29 (line)]] | alt | 2.73 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0399× (z -9.4) ⚠ cell-cycle shift, explains ~41% of this change |
| [[LOX-IMVI (line)]] | wt | 4.18 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0787× (z -8.7) |
| [[LS 180 (line)]] | wt | 4.00 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0409× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 6.64 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0650× (z -11.3) |
| [[RKO (line)]] | wt | 3.89 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0618× (z -8.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-427 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.714 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 9 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR70]] | +0.57 | +0.27 / +0.57 | both halves | 3e-04 |  |
| [[VPS13B]] | +0.56 | +0.39 / +0.60 | both halves | 6e-05 |  |
| [[DIS3L2]] | +0.52 | +0.27 / +0.59 | both halves | 3e-04 |  |
| [[FAM172A]] | +0.51 | +0.38 / +0.61 | both halves | 7e-05 | STRING 612; ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of FAM172A on the same strand (can correlate by spillover, not regulation) |
| [[HERC2P9-1]] | +0.51 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[FAF1]] | +0.50 | +0.31 / +0.46 | both halves | 2e-04 |  |
| [[VTI1A]] | +0.49 | +0.37 / +0.54 | both halves | 9e-05 |  |
| [[SPATA5]] | +0.46 | +0.29 / +0.48 | both halves | 2e-04 |  |
| [[COMMD10]] | +0.46 | +0.32 / +0.60 | both halves | 2e-04 |  |
| [[RBM6]] | +0.46 | +0.41 / +0.27 | both halves | 3e-04 |  |
| [[TASP1]] | +0.46 | +0.31 / +0.42 | both halves | 2e-04 |  |
| [[HERC2]] | +0.45 | +0.28 / +0.43 | both halves | 3e-04 |  |
| [[PRH1]] | +0.45 | +0.27 / +0.58 | both halves | 3e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP23]] | -0.53 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[RARG]] | -0.47 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[PDE4A]] | -0.46 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[NABP2]] | -0.46 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[NFKBID]] | -0.44 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[BPNT1]] | -0.43 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[ZNF821]] | -0.43 | -0.22 / -0.39 | both halves | 6e-04 |  |
| [[ZBTB18]] | -0.43 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[ITGA1]] | -0.43 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[INTS6L]] | -0.42 | -0.20 / -0.43 | both halves | 7e-04 |  |
| [[CCDC170]] | -0.42 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[PLB1]] | -0.42 | -0.36 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFB]] | B | PDGFB activity lowers POU5F2's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 1.44× higher at baseline in the lines without PDGFB | 0.044 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[TOP1]] | B | TOP1 activity raises POU5F2's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CACNG2]] | B | CACNG2 activity lowers POU5F2's level | lines that do not express CACNG2 (9) vs lines expressing it (41) | 1.32× higher at baseline in the lines without CACNG2 | 0.079 | ⚠ within organs, on part of the lines; also absent: FRMD3, NFATC2, ENSG00000285082; maybe low, not absent |
| [[CD70]] | B | CD70 activity raises POU5F2's level | lines that do not express CD70 (21) vs lines expressing it (29) | 1.24× lower at baseline in the lines without CD70 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, MEG8, MEG3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-26.6, 29.0); signed map (-14.3, -48.2). **Vector** length 41.9, 4.20% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.9 | +0.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +0.8 | -3.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +0.7 | +2.7 |
|  | [[Dapagliflozin (drug)]] 0.05 µM |  | +0.7 | +1.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.2 | -11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.1 | -7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | POU domain class 5, transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:93,733,220-93,741,600 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPRM-1, FLJ25680 |
| Gene groups (HGNC) | POU class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N7G0](https://www.uniprot.org/uniprotkb/Q8N7G0) (POU domain, class 5, transcription factor 2):

> Transcription factor that binds preferentially to the octamer motif (5'-ATGTTAAT-3'). May exert a regulatory function in meiotic events that are required for terminal differentiation of male germ cell (By similarity).

**Summary**, from NCBI Gene [134187](https://www.ncbi.nlm.nih.gov/gene/134187):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in chromatin. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26367) · Entrez [134187](https://www.ncbi.nlm.nih.gov/gene/134187) · UniProt [Q8N7G0](https://www.uniprot.org/uniprotkb/Q8N7G0) · Ensembl [ENSG00000248483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248483)

## Data

Gene col 14541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14541); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14541]; `tensor/DDL_lfc|DDL_z.npy` [14541]; `embed/gene_vectors.npy` [14541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14541 or target_col == 14541). Every well: [[POU5F2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POU5F2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
