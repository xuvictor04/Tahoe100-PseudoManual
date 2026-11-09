---
symbol: "BLZF2P"
type: "gene"
col: 15115
ensembl_id: "ENSG00000258565"
name: "basic leucine zipper nuclear factor 2, pseudogene"
location: "14q24.1"
module: 47
arm: "+"
pooled_cpm: 7.22
n_lines_expressing: 48
n_dd_up: 0
n_dd_down: 32
n_dd_up_clean: 0
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 8
direction_downstream: 1
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# BLZF2P

*basic leucine zipper nuclear factor 2, pseudogene* — 14q24.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.345× (z -8.6, q 4e-15, down in 30 of 36 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.401× (z -7.7, q 4e-12, down in 35 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C11orf91]] (+0.75, fdr 7e-06), [[CHADL]] (+0.74, fdr 7e-06), [[A3GALT2]] (+0.73, fdr 7e-06); moves opposite to [[RCOR3]] (-0.63, fdr 8e-06), [[FBXO7]] (-0.59, fdr 5e-05), [[MBIP]] (-0.59, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[HTR7]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ACTN1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15115.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | 1.48× | +3.4 | 0.16 | 14/46 (A498, SW480, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.51× | +3.4 | 0.16 | 9/43 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.51× | +3.3 | 0.16 | 12/44 (J82, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15115.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.345×** | -8.6 | 4e-15 | 30/36 (LOX-IMVI, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.401×** | -7.7 | 4e-12 | 35/44 (SW480, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.404×** | -7.6 | 5e-12 | 33/45 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.415×** | -7.4 | 2e-11 | 28/35 (NCI-H23, H4, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.462×** | -6.5 | 9e-09 | 30/45 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.465×** | -6.4 | 1e-08 | 25/30 (J82, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.499×** | -5.8 | 4e-07 | 28/45 (SW480, A-172, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.490×** | -5.8 | 6e-07 | 24/42 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.543×** | -5.5 | 3e-06 | 29/46 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.526×** | -5.4 | 4e-06 | 23/43 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.604×** | -4.9 | 6e-05 | 23/45 (SK-MEL-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.568×** | -4.8 | 1e-04 | 23/44 (HepG2/C3A, C32, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.562×** | -4.7 | 1e-04 | 19/41 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.577×** | -4.6 | 2e-04 | 26/43 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.647×** | -4.6 | 2e-04 | 25/45 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.622×** | -4.5 | 3e-04 | 21/46 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.364×** | -4.4 | 3e-04 | 23/41 (H4, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.600×** | -4.1 | 0.001 | 19/42 (NCI-H1573, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0268× (z -16.6) |
| [[SK-MEL-2 (line)]] | alt | 9.67 | 0 | 5 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0600× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0638× (z -11.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 6.51 | 0 | 4 (2 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0398× (z -11.2) |
| [[J82 (line)]] | alt | 17.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0437× (z -16.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 4.62 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0928× (z -11.0) |
| [[C32 (line)]] | wt | 13.0 | 0 | 2 | — | [[Binimetinib (drug)]] 5 µM 0.0948× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 8.63 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 10.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0820× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0841× (z -10.2) |
| [[SNU-423 (line)]] | alt | 6.46 | 0 | 2 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0478× (z -11.0) |
| [[SW480 (line)]] | alt | 12.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -11.3) |
| [[BT-474 (line)]] | alt | 8.49 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0586× (z -8.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[CFPAC-1 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0895× (z -9.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0976× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 5.06 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -9.6) ⚠ toxic |
| [[RKO (line)]] | wt | 8.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0834× (z -8.5) |
| [[SW1417 (line)]] | alt | 5.83 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0195× (z -13.3) ⚠ cell-cycle shift, explains ~7% of this change |
| [[A-172 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf91]] | +0.75 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[CHADL]] | +0.74 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[A3GALT2]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[WNT2B]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[PARVG]] | +0.70 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[SPTBN5]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.69 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[SLC25A51]] | +0.69 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[MPP4]] | +0.68 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[EPHX3]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[GPATCH2L]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR3]] | -0.63 | -0.57 / -0.62 | both halves | 8e-06 |  |
| [[FBXO7]] | -0.59 | -0.40 / -0.68 | both halves | 5e-05 |  |
| [[MBIP]] | -0.59 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[CAT]] | -0.56 | -0.58 / -0.58 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HTR7]] | B | HTR7 activity raises BLZF2P's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without HTR7 | 0.006 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[NPAS2]] | B | NPAS2 activity raises BLZF2P's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without NPAS2 | 0.024 | ⚠ within organs, on part of the lines |
| [[LINC03004]] | B | LINC03004 activity raises BLZF2P's level | lines that do not express LINC03004 (22) vs lines expressing it (28) | 1.68× lower at baseline in the lines without LINC03004 | 0.052 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, OR4F15, ADAM12; maybe low, not absent |
| [[ARHGAP22]] | B | ARHGAP22 activity raises BLZF2P's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 1.45× lower at baseline in the lines without ARHGAP22 | 0.058 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[NIPAL1]] | B | NIPAL1 activity raises BLZF2P's level | lines that do not express NIPAL1 (5) vs lines expressing it (45) | 1.77× lower at baseline in the lines without NIPAL1 | 0.063 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[ACTN1]] | C | ACTN1's natural level strengthens BLZF2P's drug response | ACTN1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.66; direction not clear | 0.041 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[NABP1]] | C | NABP1 activity raises BLZF2P's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 2.42× lower at baseline in the lines without NABP1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; co-absent with the target; its own permutation p |
| [[MPP4]] | C | MPP4 activity raises BLZF2P's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 2.39× lower at baseline in the lines without MPP4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTN1]] | C | BLZF2P's natural level strengthens ACTN1's drug response | BLZF2P's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.67; direction not clear | 0.042 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.6, -15.4); signed map (15.7, 15.6). **Vector** length 99.2, 22.8% of its response variance represented; |z| ≥ 3 in 1,271 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.1 | +1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +0.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.8 | -5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.9 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.7 | -4.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.7 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.7 | -3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.6 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | basic leucine zipper nuclear factor 2, pseudogene |
| Locus type | pseudogene |
| Location | 14q24.1 — chr14:68,867,857-68,869,951 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:20049](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20049) · Entrez [317729](https://www.ncbi.nlm.nih.gov/gene/317729) · Ensembl [ENSG00000258565](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258565)

## Data

Gene col 15115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15115); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15115]; `tensor/DDL_lfc|DDL_z.npy` [15115]; `embed/gene_vectors.npy` [15115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15115 or target_col == 15115). Every well: [[BLZF2P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLZF2P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
