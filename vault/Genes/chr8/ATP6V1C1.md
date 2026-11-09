---
symbol: "ATP6V1C1"
type: "gene"
col: 7870
ensembl_id: "ENSG00000155097"
name: "ATPase H+ transporting V1 subunit C1"
location: "8q22.3"
module: 122
arm: "+"
pooled_cpm: 70.63
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 31
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# ATP6V1C1

*ATPase H+ transporting V1 subunit C1* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.61× (z +32.8, q 0e+00, up in 43 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.286×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASHC2C]] (+0.76, fdr 7e-06), [[WASHC2A]] (+0.73, fdr 7e-06), [[IGF2R]] (+0.70, fdr 7e-06); moves opposite to [[POLG]] (-0.60, fdr 1e-05), [[TUBGCP5]] (-0.57, fdr 3e-05), [[PSME4]] (-0.52, fdr 9e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPNMB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 66 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7870.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.61×** | +32.8 | 0e+00 | 43/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.45×** | +21.7 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +16.6 | 0e+00 | 45/48 (A498, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +16.5 | 0e+00 | 45/48 (C32, RKO, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.77×** | +13.8 | 3e-41 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.72×** | +13.2 | 1e-37 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +12.4 | 1e-33 | 40/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +11.6 | 2e-29 | 34/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.24×** | +11.3 | 6e-28 | 40/49 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +11.0 | 2e-26 | 43/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +10.6 | 2e-24 | 41/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +10.4 | 8e-24 | 33/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +9.3 | 5e-19 | 30/44 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.53×** | +8.9 | 2e-17 | 33/48 (NCI-H2347, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +8.9 | 2e-17 | 39/48 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.54×** | +8.9 | 2e-17 | 37/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +6.8 | 4e-10 | 22/49 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7870.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.286×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.877× | -4.6 | 0.003 | 16/48 (HOP62, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.7 | 0.065 | 19/49 (HOP62, SW480, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.865× | -3.6 | 0.065 | 18/47 (NCI-H661, SW1417, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7870. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 58.0 | 16 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +43.5) | — |
| [[A498 (line)]] | wt | 80.2 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +25.3) | — |
| [[PANC-1 (line)]] | alt | 72.2 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +21.2) | — |
| [[NCI-H1573 (line)]] | alt | 80.9 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.24× (z +28.3) | — |
| [[NCI-H23 (line)]] | alt | 77.1 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +21.2) | — |
| [[HS-578T (line)]] | alt | 93.6 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +21.3) | — |
| [[NCI-H2347 (line)]] | alt | 107 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +33.2) | — |
| [[BT-474 (line)]] | alt | 59.2 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.73× (z +15.0) | — |
| [[J82 (line)]] | alt | 81.9 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.23× (z +25.6) | — |
| [[KATO III (line)]] | alt | 70.9 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.20× (z +18.2) | — |
| [[HOP62 (line)]] | alt | 47.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.1) | — |
| [[hTERT-HPNE (line)]] | wt | 67.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +18.7) | — |
| [[LOX-IMVI (line)]] | wt | 73.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +15.7) | — |
| [[RKO (line)]] | wt | 173 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.6) | — |
| [[SW480 (line)]] | alt | 53.6 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +12.7) | — |
| [[A-427 (line)]] | wt | 55.8 | 4 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.97× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 58.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +21.5) | — |
| [[COLO 205 (line)]] | alt | 76.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +23.6) | — |
| [[Hs 766T (line)]] | wt | 78.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +24.3) | — |
| [[RPMI-7951 (line)]] | alt | 96.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +18.3) | — |
| [[SNU-423 (line)]] | alt | 115 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +24.6) | — |
| [[SW 900 (line)]] | alt | 70.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +13.2) | — |
| [[SW1417 (line)]] | alt | 104 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +14.9) | — |
| [[A-172 (line)]] | wt | 58.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +24.9) | — |
| [[HT-29 (line)]] | alt | 58.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +15.1) | — |
| [[SK-MEL-2 (line)]] | alt | 73.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +21.8) | — |
| [[LoVo (line)]] | wt | 42.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.51× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 76.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +15.8) | — |
| [[NCI-H1792 (line)]] | alt | 50.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.3) | — |
| [[Panc 03.27 (line)]] | alt | 85.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +16.0) | — |
| [[SNU-1 (line)]] | wt | 84.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.4) | — |
| [[A549 (line)]] | wt | 47.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +14.3) | — |
| [[C32 (line)]] | wt | 109 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.12× (z +14.7) | — |
| [[CFPAC-1 (line)]] | alt | 46.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 41.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.77× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 54.0 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.286× (z -8.7) |
| [[LS 180 (line)]] | wt | 36.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 64.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +20.9) | — |
| [[AN3 CA (line)]] | alt | 130 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7870), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASHC2C]] | +0.76 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[WASHC2A]] | +0.73 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[IGF2R]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[HEXA]] | +0.70 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[TPP1]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[VPS41]] | +0.68 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[RRAGB]] | +0.67 | +0.68 / +0.68 | both halves | 7e-06 | pathway: Amino acids regulate mTORC1; STRING 554 |
| [[GBA1]] | +0.66 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[ATP6V1G1]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 998 |
| [[VPS11]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[MED28]] | +0.64 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[GNPDA1]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLG]] | -0.60 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[TUBGCP5]] | -0.57 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[PSME4]] | -0.52 | -0.57 / -0.36 | both halves | 9e-05 |  |
| [[MFSD2A]] | -0.52 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[OSBPL6]] | -0.52 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[C11orf24]] | -0.51 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[SRA1]] | -0.50 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[MYO19]] | -0.49 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[WDFY2]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[HM13]] | -0.49 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[KRT15]] | -0.49 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[ATG101]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPNMB]] | B | GPNMB activity raises ATP6V1C1's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 1.19× lower at baseline in the lines without GPNMB | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6 |
| [[KRT15]] | B | KRT15 activity lowers ATP6V1C1's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 1.28× higher at baseline in the lines without KRT15 | 0.090 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.823). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-19.1, 13.9); signed map (-9.9, -19.5). **Vector** length 112, 35.0% of its response variance represented; |z| ≥ 3 in 1,239 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +11.4 | +16.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.8 | +16.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +8.6 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +8.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +3.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.3 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +4.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +4.1 | +3.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | +4.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.6 | -0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V1 subunit C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:103,021,063-103,073,051 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VATC, Vma5; previously ATP6D, ATP6C |
| Gene groups (HGNC) | V-type ATPase subunits |
| Hallmark sets | UV_RESPONSE_UP, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 16 pathways, smallest: Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Insulin receptor recycling; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [P21283](https://www.uniprot.org/uniprotkb/P21283) (V-type proton ATPase subunit C 1):

> Subunit of the V1 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it promotes acidification of the extracellular environment (By similarity). The V-ATPase complex also acts as an activator for mTORC1 on …

**Summary**, from NCBI Gene [528](https://www.ncbi.nlm.nih.gov/gene/528):

> This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of intracellular compartments of eukaryotic cells. V-ATPase dependent acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 domain and a transmembrane V0 domain. The V1 domain consists of three A and three B subunits, two G …

**Accessions** — [HGNC:856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:856) · Entrez [528](https://www.ncbi.nlm.nih.gov/gene/528) · UniProt [P21283](https://www.uniprot.org/uniprotkb/P21283) · Ensembl [ENSG00000155097](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155097)

## Data

Gene col 7870: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7870); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7870, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7870]; `tensor/DDL_lfc|DDL_z.npy` [7870]; `embed/gene_vectors.npy` [7870]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7870 or target_col == 7870). Every well: [[ATP6V1C1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V1C1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
