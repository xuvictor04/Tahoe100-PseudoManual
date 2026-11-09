---
symbol: "DMD"
type: "gene"
col: 12751
ensembl_id: "ENSG00000198947"
name: "dystrophin"
location: "Xp21.2-p21.1"
module: 9
arm: "+"
pooled_cpm: 22.18
n_lines_expressing: 32
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 5
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# DMD

*dystrophin* — Xp21.2-p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.45× (z +31.9, q 0e+00, up in 22 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.284×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.313×); [[Dinaciclib (drug)]] 5 µM in 1 line (H4 0.144×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGFEM1P]] (+0.72, fdr 7e-06), [[FMN2]] (+0.72, fdr 7e-06), [[PIEZO2]] (+0.71, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[NREP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12751.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.45×** | +31.9 | 0e+00 | 22/29 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.84×** | +26.9 | 0e+00 | 16/28 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.81×** | +18.9 | 0e+00 | 18/26 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +17.9 | 0e+00 | 19/30 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +14.6 | 0e+00 | 12/23 (HOP62, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +13.9 | 4e-42 | 15/27 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.16×** | +13.5 | 1e-39 | 16/27 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +12.9 | 2e-36 | 8/23 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.86×** | +11.3 | 8e-28 | 19/28 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +10.6 | 2e-24 | 12/27 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +10.5 | 4e-24 | 10/21 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +9.0 | 1e-17 | 14/27 (BT-474, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +7.8 | 3e-13 | 12/30 (HOP62, A-427, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +6.9 | 2e-10 | 15/26 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +6.7 | 9e-10 | 12/29 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +6.1 | 4e-08 | 14/29 (BT-474, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.4 | 2e-06 | 13/28 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.9 | 3e-05 | 10/27 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12751.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.284×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.313×); [[Dinaciclib (drug)]] 5 µM in 1 line (H4 0.144×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.822× | -3.4 | 0.35 | 8/27 (RPMI-7951, A-172, …) | top dose only |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.884× | -3.2 | 0.42 | 5/29 (SW 1088, PANC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.954× | -3.1 | 0.42 | 0/30 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12751. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 45.1 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 29.1× (z +36.0) | — |
| [[C32 (line)]] | wt | 113 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +11.3) | — |
| [[BT-474 (line)]] | alt | 21.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +15.4) | — |
| [[HS-578T (line)]] | alt | 28.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +18.2) | — |
| [[LOX-IMVI (line)]] | wt | 16.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.2× (z +28.3) | — |
| [[A498 (line)]] | wt | 9.59 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +12.3) | — |
| [[HOP62 (line)]] | alt | 6.85 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +12.6) | — |
| [[NCI-H2030 (line)]] | alt | 119 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 62.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.32× (z +18.7) | — |
| [[A-427 (line)]] | wt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.87× (z +9.3) | — |
| [[H4 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -11.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 42.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +8.5) | — |
| [[J82 (line)]] | alt | 5.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.36× (z +11.8) | — |
| [[NCI-H23 (line)]] | alt | 38.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 5.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +16.0) | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +9.5) | — |
| [[A-172 (line)]] | wt | 91.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.30 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 355 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.32 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.53 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.18 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12751), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGFEM1P]] | +0.72 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[FMN2]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[PIEZO2]] | +0.71 | +0.63 / +0.65 | both halves | 7e-06 | same gene group |
| [[EPHA5]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[RALYL]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[HMCN1]] | +0.65 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[UNC5C]] | +0.65 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[CDH18]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[LINC00882]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[PPP2R2B]] | +0.64 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[MAPK10]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 | same gene group |
| [[SOX5]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DMD's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ROBO2]] | B | ROBO2 activity raises DMD's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 2.86× lower at baseline in the lines without ROBO2 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205 |
| [[ZNF595]] | B | ZNF595 activity lowers DMD's level | lines that do not express ZNF595 (11) vs lines expressing it (39) | 1.19× higher at baseline in the lines without ZNF595 | 0.078 | ⚠ within organs, on part of the lines; also absent: TIGD7, ZNF530, MSN |
| [[SLCO3A1]] | B | SLCO3A1 activity lowers DMD's level | lines that do not express SLCO3A1 (13) vs lines expressing it (37) | 1.16× higher at baseline in the lines without SLCO3A1 | 0.082 | ⚠ within organs, on part of the lines; also absent: BEX2, PRKAA2, NHS |
| [[FAM133A]] | C | FAM133A activity raises DMD's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 4.21× lower at baseline in the lines without FAM133A | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |
| [[SCN2A]] | C | SCN2A activity raises DMD's level | lines that do not express SCN2A (26) vs lines expressing it (24) | 3.72× lower at baseline in the lines without SCN2A | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTPRN, ENSG00000286251, EDA2R; maybe low, not absent; co-absent with the target |
| [[ERBB4]] | C | ERBB4 activity raises DMD's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 3.17× lower at baseline in the lines without ERBB4 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[TRPC4]] | C | TRPC4 activity raises DMD's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 3.72× lower at baseline in the lines without TRPC4 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NREP]] | C | DMD activity raises NREP's level | lines that do not express DMD (18) vs lines expressing it (32) | 6.23× lower at baseline in the lines without DMD | 4e-04 | ⚠ within organs, on part of the lines; also absent: KCTD16, NREP, PRKD1; maybe low, not absent; co-absent with the target |
| [[NEGR1]] | C | DMD activity raises NEGR1's level | lines that do not express DMD (18) vs lines expressing it (32) | 4.31× lower at baseline in the lines without DMD | 0.039 | ⚠ within organs, on part of the lines; also absent: KCTD16, NREP, PRKD1; maybe low, not absent; co-absent with the target |
| [[LINC00882]] | C | DMD activity raises LINC00882's level | lines that do not express DMD (18) vs lines expressing it (32) | 3.55× lower at baseline in the lines without DMD | 0.046 | ⚠ within organs, on part of the lines; also absent: KCTD16, NREP, PRKD1; maybe low, not absent; co-absent with the target |
| [[TRPC4]] | C | DMD activity raises TRPC4's level | lines that do not express DMD (18) vs lines expressing it (32) | 4.00× lower at baseline in the lines without DMD | 0.066 | ⚠ within organs, on part of the lines; also absent: KCTD16, NREP, PRKD1; maybe low, not absent; co-absent with the target |
| [[FAM133A]] | C | DMD activity raises FAM133A's level | lines that do not express DMD (18) vs lines expressing it (32) | 2.12× lower at baseline in the lines without DMD | 0.087 | ⚠ within organs, on part of the lines; also absent: KCTD16, NREP, PRKD1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.6, 29.9); signed map (39.2, 31.3). **Vector** length 73.1, 17.4% of its response variance represented; |z| ≥ 3 in 734 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.3 | +14.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.5 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +31.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.9 | +12.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +17.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +7.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +6.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +4.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -1.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | dystrophin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp21.2-p21.1 — chrX:31,097,677-33,339,609 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BMD, DXS142, DXS164, DXS206, DXS230, DXS239, DXS268, DXS269; previously MRX85 |
| Gene groups (HGNC) | Zinc fingers ZZ-type; MicroRNA protein coding host genes; Spectrin repeat containing |
| Hallmark sets | MYOGENESIS, G2M_CHECKPOINT |
| Reactome | 5 pathways, smallest: Striated Muscle Contraction; Formation of the dystrophin-glycoprotein complex (DGC); Non-integrin membrane-ECM interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P11532](https://www.uniprot.org/uniprotkb/P11532) (Dystrophin):

> Anchors the extracellular matrix to the cytoskeleton via F-actin. Ligand for dystroglycan. Component of the dystrophin-associated glycoprotein complex which accumulates at the neuromuscular junction (NMJ) and at a variety of synapses in the peripheral and central nervous systems and has a structural function in stabilizing the sarcolemma. Also implicated in signaling events and synaptic transmission.

**Summary**, from NCBI Gene [1756](https://www.ncbi.nlm.nih.gov/gene/1756):

> This gene spans a genomic range of greater than 2 Mb and encodes a large protein containing an N-terminal actin-binding domain and multiple spectrin repeats. The encoded protein forms a component of the dystrophin-glycoprotein complex (DGC), which bridges the inner cytoskeleton and the extracellular matrix. Deletions, duplications, and point mutations at this gene locus may cause Duchenne muscular dystrophy (DMD), Becker muscular dystrophy (BMD), or cardiomyopathy. Alternative promoter usage …

**Accessions** — [HGNC:2928](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2928) · Entrez [1756](https://www.ncbi.nlm.nih.gov/gene/1756) · UniProt [P11532](https://www.uniprot.org/uniprotkb/P11532) · Ensembl [ENSG00000198947](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198947)

## Data

Gene col 12751: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12751); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12751, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12751]; `tensor/DDL_lfc|DDL_z.npy` [12751]; `embed/gene_vectors.npy` [12751]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12751 or target_col == 12751). Every well: [[DMD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
