---
symbol: "RUNX3"
type: "gene"
col: 323
ensembl_id: "ENSG00000020633"
name: "RUNX family transcription factor 3"
location: "1p36.11"
module: 13
arm: "+"
pooled_cpm: 16.26
n_lines_expressing: 21
n_dd_up: 9
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# RUNX3

*RUNX family transcription factor 3* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +7.7, q 5e-12, up in 6 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.622× (z -4.4, q 0.006, down in 12 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETBP1]] (+0.61, fdr 1e-05), [[CTHRC1]] (+0.58, fdr 1e-05), [[TLE3]] (+0.58, fdr 3e-05); moves opposite to [[LPGAT1]] (-0.50, fdr 5e-05), [[BMS1P2]] (-0.49, fdr 5e-05), [[ATL3]] (-0.48, fdr 3e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[UPK1A-AS1]] → it (grade C ⚠); 3 go from it, the strongest it → [[RHBDF2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 323.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +7.7 | 5e-12 | 6/19 (A549, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +6.6 | 1e-08 | 1/12 (NCI-H2030) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +6.3 | 5e-08 | 3/16 (NCI-H2030, A549, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +5.8 | 9e-07 | 0/15 | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.025 | 8/19 (HOP62, Panc 03.27, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.4 | 0.061 | 11/18 (C-33 A, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.061 | 5/19 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.88×** | +3.2 | 0.082 | 5/17 (NCI-H1573, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.86×** | +3.2 | 0.091 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 323.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.622×** | -4.4 | 0.006 | 12/19 (NCI-H1573, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.673×** | -3.7 | 0.071 | 10/19 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.663×** | -3.5 | 0.083 | 0/19 | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.678× | -3.3 | 0.12 | 1/19 (NCI-H23) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.690× | -3.2 | 0.12 | 3/19 (SK-MEL-2, C-33 A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.711× | -3.2 | 0.12 | 11/18 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Encorafenib (drug)]] 5 µM |  | 0.496× | -3.2 | 0.12 | 1/19 (SW480) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.695× | -3.1 | 0.12 | 2/19 (RPMI-7951, NCI-H23) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.715× | -3.1 | 0.12 | 2/18 (RPMI-7951, C32) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 323. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 70.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -9.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 116 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0368× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.206× (z -8.8) |
| [[A-427 (line)]] | wt | 31.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0982× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -9.3) |
| [[A549 (line)]] | wt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.215× (z -8.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H23 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0953× (z -14.8) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SW480 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.932 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.927 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 323), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETBP1]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[CTHRC1]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[TLE3]] | +0.58 | +0.44 / +0.61 | both halves | 3e-05 | same gene group; pathway: Formation of the beta-catenin:TCF transactivating complex; STRING 597 |
| [[BCL11B]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 | STRING 528 |
| [[GPR68]] | +0.55 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[RHBDF2]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[LINC03047]] | +0.54 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[FAM43A]] | +0.54 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[APCDD1L-DT]] | +0.54 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[NPAS1]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PDLIM4]] | +0.53 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[CYGB]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPGAT1]] | -0.50 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[BMS1P2]] | -0.49 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[ATL3]] | -0.48 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[NCKAP1]] | -0.47 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[DPY19L4]] | -0.46 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[ARPP19]] | -0.46 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[CD99L2]] | -0.44 | -0.32 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UPK1A-AS1]] | C | UPK1A-AS1 activity raises RUNX3's level | lines that do not express UPK1A-AS1 (18) vs lines expressing it (32) | 4.31× lower at baseline in the lines without UPK1A-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: CERS4, SUSD5, WIPF1; co-absent with the target |
| [[VAT1L]] | C | VAT1L activity raises RUNX3's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 4.31× lower at baseline in the lines without VAT1L | 0.039 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent; co-absent with the target |
| [[TSHZ3]] | C | TSHZ3 activity raises RUNX3's level | lines that do not express TSHZ3 (25) vs lines expressing it (25) | 3.23× lower at baseline in the lines without TSHZ3 | 0.051 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |
| [[FMNL1-DT]] | C | FMNL1-DT activity raises RUNX3's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 3.39× lower at baseline in the lines without FMNL1-DT | 0.085 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent; co-absent with the target |
| [[GYPC]] | C | GYPC activity raises RUNX3's level | lines that do not express GYPC (35) vs lines expressing it (15) | 3.75× lower at baseline in the lines without GYPC | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHBDF2]] | B | RUNX3 activity raises RHBDF2's level | lines that do not express RUNX3 (29) vs lines expressing it (21) | 1.68× lower at baseline in the lines without RUNX3 | 0.064 | ⚠ within organs, on part of the lines; also absent: SLC6A15, IGF2BP1, ENSG00000286385 |
| [[NR2F2-AS1]] | B | RUNX3 activity raises NR2F2-AS1's level | lines that do not express RUNX3 (29) vs lines expressing it (21) | 2.14× lower at baseline in the lines without RUNX3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC6A15, IGF2BP1, ENSG00000286385 |
| [[FMNL1-DT]] | C | RUNX3 activity raises FMNL1-DT's level | lines that do not express RUNX3 (29) vs lines expressing it (21) | 2.76× lower at baseline in the lines without RUNX3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SLC6A15, IGF2BP1, ENSG00000286385; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.4, 12.5); signed map (20.2, 43.2). **Vector** length 49.7, 14.2% of its response variance represented; |z| ≥ 3 in 358 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.4 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +1.3 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.0 | +1.8 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -1.3 | -2.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.3 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | RUNX family transcription factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:24,899,511-24,965,121 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AML2, PEBP2A3; previously CBFA3 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Runt-related transcription factors |
| Reactome | 16 pathways, smallest: RUNX3 regulates RUNX1-mediated transcription; RUNX3 Regulates Immune Response and Cell Migration; RUNX3 regulates BCL2L11 (BIM) transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13761](https://www.uniprot.org/uniprotkb/Q13761) (Runt-related transcription factor 3):

> Forms the heterodimeric complex core-binding factor (CBF) with CBFB. RUNX members modulate the transcription of their target genes through recognizing the core consensus binding sequence 5'-TGTGGT-3', or very rarely, 5'-TGCGGT-3', within their regulatory regions via their runt domain, while CBFB is a non-DNA-binding regulatory subunit that allosterically enhances the sequence-specific DNA-binding capacity of RUNX. The heterodimers bind to the core site of a number of enhancers and promoters, …

**Summary**, from NCBI Gene [864](https://www.ncbi.nlm.nih.gov/gene/864):

> This gene encodes a member of the runt domain-containing family of transcription factors. A heterodimer of this protein and a beta subunit forms a complex that binds to the core DNA sequence 5'-PYGPYGGT-3' found in a number of enhancers and promoters, and can either activate or suppress transcription. It also interacts with other transcription factors. It functions as a tumor suppressor, and the gene is frequently deleted or transcriptionally silenced in cancer. Alternative splicing results in …

**Accessions** — [HGNC:10473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10473) · Entrez [864](https://www.ncbi.nlm.nih.gov/gene/864) · UniProt [Q13761](https://www.uniprot.org/uniprotkb/Q13761) · Ensembl [ENSG00000020633](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000020633)

## Data

Gene col 323: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 323); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 323, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 323]; `tensor/DDL_lfc|DDL_z.npy` [323]; `embed/gene_vectors.npy` [323]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 323 or target_col == 323). Every well: [[RUNX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUNX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
