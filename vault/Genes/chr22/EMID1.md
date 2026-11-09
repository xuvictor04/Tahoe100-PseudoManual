---
symbol: "EMID1"
type: "gene"
col: 11876
ensembl_id: "ENSG00000186998"
name: "EMI domain containing 1"
location: "22q12.2"
module: 115
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 31
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 18
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# EMID1

*EMI domain containing 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.77× (z +10.8, q 1e-24, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.93× (z +7.9, q 6e-13, up in 10 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.491× (z -6.1, q 8e-07, down in 11 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTPA]] (+0.69, fdr 7e-06), [[MYT1]] (+0.64, fdr 7e-06), [[PRKCQ]] (+0.63, fdr 8e-06).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SEPTIN3]] → it (grade B ⚠); 18 go from it, the strongest it → [[SGSM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11876.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.77×** | +10.8 | 1e-24 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.91×** | +8.4 | 2e-14 | 1/3 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +7.9 | 6e-13 | 10/25 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +7.7 | 2e-12 | 5/17 (PANC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +7.3 | 4e-11 | 1/4 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.87×** | +5.3 | 1e-05 | 8/20 (BT-474, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.37×** | +5.2 | 1e-05 | 1/6 (SW48) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +3.9 | 0.008 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.7 | 0.013 | 5/10 (SW480, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.59×** | +3.6 | 0.018 | 6/14 (LoVo, SW48, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11876.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.491×** | -6.1 | 8e-07 | 11/16 (SW480, RKO, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.507×** | -5.6 | 8e-06 | 14/22 (SW480, LoVo, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.540×** | -5.2 | 3e-05 | 15/26 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -4.7 | 3e-04 | 13/23 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.596×** | -4.4 | 0.001 | 6/18 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.622×** | -4.0 | 0.005 | 13/20 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.627×** | -4.0 | 0.005 | 11/27 (SW480, RKO, …) | all doses, stronger at high dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11876. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 8.14 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -16.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0950× (z -13.3) |
| [[A-427 (line)]] | wt | 6.59 | 0 | 2 | — | [[Pemetrexed (drug)]] 5 µM 0.0558× (z -11.9) |
| [[SW48 (line)]] | wt | 8.40 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0431× (z -10.3) |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0781× (z -9.4) |
| [[LoVo (line)]] | wt | 6.07 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 6.02 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0565× (z -10.6) |
| [[A-172 (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.603 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.346 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.624 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.558 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.418 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.688 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.596 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.351 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.794 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11876), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTPA]] | +0.69 | +0.60 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[MYT1]] | +0.64 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PRKCQ]] | +0.63 | +0.65 / +0.57 | both halves | 8e-06 |  |
| [[TMEM98]] | +0.61 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[LAMC3]] | +0.61 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[MSI1]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[EPHX4]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[FGF20]] | +0.58 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[DGCR5]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ENTREP2]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SEPTIN3]] | +0.56 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPTIN3]] | B | SEPTIN3 activity raises EMID1's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.83× lower at baseline in the lines without SEPTIN3 | 0.007 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[EBF4]] | B | EBF4 activity raises EMID1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.90× lower at baseline in the lines without EBF4 | 0.009 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[SEMA6B]] | B | SEMA6B activity raises EMID1's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without SEMA6B | 0.037 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[FAXC]] | B | FAXC activity raises EMID1's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.96× lower at baseline in the lines without FAXC | 0.061 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[KCND3]] | B | KCND3 activity raises EMID1's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 1.65× lower at baseline in the lines without KCND3 | 0.066 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[RET]] | B | RET activity raises EMID1's level | lines that do not express RET (28) vs lines expressing it (22) | 1.55× lower at baseline in the lines without RET | 0.070 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[NKAIN1]] | C | NKAIN1 activity raises EMID1's level | lines that do not express NKAIN1 (4) vs lines expressing it (46) | 1.93× lower at baseline in the lines without NKAIN1 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 17, C 1. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGSM1]] | B | EMID1 activity raises SGSM1's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 1.99× lower at baseline in the lines without EMID1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[DGCR5]] | B | EMID1 activity raises DGCR5's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 2.57× lower at baseline in the lines without EMID1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[FAXC]] | B | EMID1 activity raises FAXC's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 2.24× lower at baseline in the lines without EMID1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[GPLD1]] | B | EMID1 activity raises GPLD1's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 1.60× lower at baseline in the lines without EMID1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[STOX1]] | B | EMID1 activity raises STOX1's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 2.22× lower at baseline in the lines without EMID1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[NMNAT3]] | B | EMID1 activity raises NMNAT3's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without EMID1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[SLIT1]] | B | EMID1 activity raises SLIT1's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 2.10× lower at baseline in the lines without EMID1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[SEPTIN3]] | B | EMID1 activity raises SEPTIN3's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without EMID1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[PTK7]] | B | EMID1 activity raises PTK7's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 2.46× lower at baseline in the lines without EMID1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[DLX6-AS1]] | B | EMID1 activity raises DLX6-AS1's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 1.52× lower at baseline in the lines without EMID1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[ALDH5A1]] | B | EMID1 activity raises ALDH5A1's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without EMID1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[NKAIN1]] | B | EMID1 activity raises NKAIN1's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 1.62× lower at baseline in the lines without EMID1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.0, 39.3); signed map (24.8, 26.7). **Vector** length 40.9, 7.15% of its response variance represented; |z| ≥ 3 in 625 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +10.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +3.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.6 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.3 | -6.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.2 | -4.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.8 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | EMI domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:29,205,896-29,259,597 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EMU1, hEmu1, EMI5 |
| Gene groups (HGNC) | EMI domain containing |
| Reactome | 1 pathways, smallest: O-linked glycosylation |
| Matched by | ensembl_id |

UniProt [Q96A84](https://www.uniprot.org/uniprotkb/Q96A84) carries no function annotation.

**Summary**, from NCBI Gene [129080](https://www.ncbi.nlm.nih.gov/gene/129080):

> Predicted to be located in endoplasmic reticulum lumen. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18036) · Entrez [129080](https://www.ncbi.nlm.nih.gov/gene/129080) · UniProt [Q96A84](https://www.uniprot.org/uniprotkb/Q96A84) · Ensembl [ENSG00000186998](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186998)

## Data

Gene col 11876: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11876); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11876, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11876]; `tensor/DDL_lfc|DDL_z.npy` [11876]; `embed/gene_vectors.npy` [11876]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11876 or target_col == 11876). Every well: [[EMID1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMID1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
