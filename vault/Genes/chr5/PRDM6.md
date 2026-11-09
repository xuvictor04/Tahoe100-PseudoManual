---
symbol: "PRDM6"
type: "gene"
col: 699
ensembl_id: "ENSG00000061455"
name: "PR/SET domain 6"
location: "5q23.2"
module: 150
arm: "+"
pooled_cpm: 3.7
n_lines_expressing: 42
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# PRDM6

*PR/SET domain 6* — 5q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.15× (z +29.5, q 0e+00, up in 27 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.697× (z -3.8, q 0.055, down in 11 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.102×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.127×); [[Belumosudil (drug)]] 5 µM in 1 line (HS-578T 0.0594×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL25A1]] (+0.67, fdr 7e-06), [[LINC02268]] (+0.67, fdr 1e-05), [[SORCS3]] (+0.66, fdr 7e-06); moves opposite to [[HEMK1]] (-0.56, fdr 4e-04), [[GGA1]] (-0.55, fdr 9e-05), [[POLM]] (-0.53, fdr 5e-04).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[LINC01482]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 699.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.15×** | +29.5 | 0e+00 | 27/29 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.14×** | +11.7 | 5e-29 | 13/25 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.93×** | +9.9 | 8e-21 | 14/39 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +9.4 | 1e-18 | 1/5 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +8.7 | 3e-16 | 19/38 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.09×** | +7.8 | 5e-13 | 14/32 (HOP62, RKO, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +7.3 | 2e-11 | 13/30 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +7.2 | 5e-11 | 10/30 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +7.1 | 1e-10 | 10/27 (A-172, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.84×** | +6.4 | 6e-09 | 15/31 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +6.0 | 9e-08 | 16/38 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +5.5 | 2e-06 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.4 | 2e-06 | 2/14 (HOP62, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.38×** | +4.8 | 6e-05 | 3/10 (J82, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +4.8 | 7e-05 | 9/28 (A-172, H4, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.005 | 3/34 (A-172, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.026 | 5/32 (NCI-H2030, BT-474, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +3.1 | 0.052 | 7/32 (Hs 766T, SNU-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.053 | 5/25 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 699.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.102×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.127×); [[Belumosudil (drug)]] 5 µM in 1 line (HS-578T 0.0594×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.697×** | -3.8 | 0.055 | 11/35 (C-33 A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.694×** | -3.7 | 0.055 | 8/32 (A-427, NCI-H23, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.750× | -3.1 | 0.42 | 10/39 (HepG2/C3A, C-33 A, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 699. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +9.0) | — |
| [[A-427 (line)]] | wt | 13.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -10.8) |
| [[A549 (line)]] | wt | 1.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.9× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -11.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 4.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.06× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.40× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 4.70 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0594× (z -9.6) |
| [[HT-29 (line)]] | alt | 2.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +9.6) | — |
| [[LoVo (line)]] | wt | 1.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 8.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +13.7) | — |
| [[SW480 (line)]] | alt | 1.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +9.2) | — |
| [[A498 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.913 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.826 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.972 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.921 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.995 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 699), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL25A1]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[LINC02268]] | +0.67 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[SORCS3]] | +0.66 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PTPRO]] | +0.66 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[HPSE2]] | +0.64 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[SYNPO2]] | +0.64 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[GRID2]] | +0.64 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[GRM8]] | +0.64 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[SAXO1]] | +0.62 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CHODL]] | +0.62 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[C8orf34]] | +0.62 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[FAT3]] | +0.61 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEMK1]] | -0.56 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[GGA1]] | -0.55 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[POLM]] | -0.53 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[C8orf82]] | -0.52 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[FN3KRP]] | -0.51 | -0.43 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRDM6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CPNE4]] | B | CPNE4 activity lowers PRDM6's level | lines that do not express CPNE4 (21) vs lines expressing it (29) | 1.35× higher at baseline in the lines without CPNE4 | 0.033 | ⚠ within organs, on part of the lines; also absent: MIR646HG, TMEM156, BCL2A1; maybe low, not absent |
| [[ADAMTS3]] | B | ADAMTS3 activity lowers PRDM6's level | lines that do not express ADAMTS3 (23) vs lines expressing it (27) | 1.32× higher at baseline in the lines without ADAMTS3 | 0.051 | ⚠ within organs, on part of the lines; also absent: ARMCX1, EYA1, ENSG00000232949 |
| [[RTN4RL1]] | B | RTN4RL1 activity raises PRDM6's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 2.04× lower at baseline in the lines without RTN4RL1 | 0.053 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers PRDM6's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01482]] | B | PRDM6 activity raises LINC01482's level | lines that do not express PRDM6 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without PRDM6 | 0.067 | ⚠ within organs, on part of the lines; also absent: GALNT8, RHBDL3, ASGR1; maybe low, not absent |
| [[GNAL]] | B | PRDM6 activity raises GNAL's level | lines that do not express PRDM6 (8) vs lines expressing it (42) | 2.31× lower at baseline in the lines without PRDM6 | 0.081 | ⚠ within organs, on part of the lines; also absent: GALNT8, RHBDL3, ASGR1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.1, 24.9); signed map (33.3, 13.1). **Vector** length 45.9, 5.90% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +29.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +9.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +4.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | -1.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +1.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -0.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | PR/SET domain 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.2 — chr5:123,089,241-123,194,266 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRISM, KMT8C |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PR/SET domain family; Putative lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQX0](https://www.uniprot.org/uniprotkb/Q9NQX0) (Putative histone-lysine N-methyltransferase PRDM6):

> Putative histone methyltransferase that acts as a transcriptional repressor of smooth muscle gene expression. Promotes the transition from differentiated to proliferative smooth muscle by suppressing differentiation and maintaining the proliferative potential of vascular smooth muscle cells. Also plays a role in endothelial cells by inhibiting endothelial cell proliferation, survival and differentiation. It is unclear whether it has histone methyltransferase activity in vivo. According to some …

**Summary**, from NCBI Gene [93166](https://www.ncbi.nlm.nih.gov/gene/93166):

> The protein encoded by this gene is a transcriptional repressor and a member of the PRDM family. Family members contain a PR domain and multiple zinc-finger domains. The encoded protein is involved in regulation of vascular smooth muscle cells (VSMC) contractile proteins. Mutations in this gene result in patent ductus arteriosus 3 (PDA3). [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:9350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9350) · Entrez [93166](https://www.ncbi.nlm.nih.gov/gene/93166) · UniProt [Q9NQX0](https://www.uniprot.org/uniprotkb/Q9NQX0) · Ensembl [ENSG00000061455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000061455)

## Data

Gene col 699: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 699); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 699, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 699]; `tensor/DDL_lfc|DDL_z.npy` [699]; `embed/gene_vectors.npy` [699]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 699 or target_col == 699). Every well: [[PRDM6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDM6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
