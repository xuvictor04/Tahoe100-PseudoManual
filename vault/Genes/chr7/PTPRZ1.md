---
symbol: "PTPRZ1"
type: "gene"
col: 2739
ensembl_id: "ENSG00000106278"
name: "protein tyrosine phosphatase receptor type Z1"
location: "7q31.32"
module: 87
arm: "+"
pooled_cpm: 15.68
n_lines_expressing: 10
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 22
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# PTPRZ1

*protein tyrosine phosphatase receptor type Z1* — 7q31.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.47× (z +15.5, q 0e+00, up in 1 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.172×, SW1417 0.282×, SW480 0.312×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (C32 0.248×, SW1417 0.325×, Hs 766T 0.218×); [[Belinostat (drug)]] 5 µM in 2 lines (SW480 0.163×, A-427 0.333×); [[Panobinostat (drug)]] 5 µM in 1 line (A-427 0.259×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LEF1-AS1]] (+0.68, fdr 1e-05), [[LEF1]] (+0.67, fdr 1e-05), [[GLDC]] (+0.63, fdr 7e-06).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[APCDD1]] → it (grade C ⚠); 22 go from it, the strongest it → [[SH3TC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2739.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.47×** | +15.5 | 0e+00 | 1/8 (SK-MEL-2) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.93×** | +13.5 | 4e-39 | 2/6 (SW480, C32) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.06×** | +12.3 | 1e-32 | 2/7 (MIA PaCa-2, Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.79×** | +8.3 | 1e-14 | 2/6 (MIA PaCa-2, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +6.9 | 6e-10 | 3/8 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.94×** | +5.8 | 5e-07 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.84×** | +5.3 | 7e-06 | 1/8 (SK-MEL-2) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +4.9 | 6e-05 | 0/7 | top dose only | cell-cycle shift (explains ~4% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.80×** | +3.7 | 0.014 | 1/8 (MIA PaCa-2) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +3.5 | 0.023 | 1/7 (SK-MEL-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.07×** | +3.3 | 0.042 | 1/4 (A-427) | inconsistent across doses | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.3 | 0.046 | 0/8 | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2739.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.172×, SW1417 0.282×, SW480 0.312×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (C32 0.248×, SW1417 0.325×, Hs 766T 0.218×); [[Belinostat (drug)]] 5 µM in 2 lines (SW480 0.163×, A-427 0.333×); [[Panobinostat (drug)]] 5 µM in 1 line (A-427 0.259×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 0.05 µM |  | 0.672× | -3.3 | 0.30 | 0/8 | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.670× | -3.3 | 0.30 | 0/8 | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.705× | -3.1 | 0.30 | 0/8 | two highest doses |  |
| [[Lopinavir (drug)]] 0.5 µM |  | 0.713× | -3.0 | 0.30 | 0/8 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 365 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -21.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.259× (z -11.4) |
| [[C32 (line)]] | wt | 170 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -10.7) |
| [[SW1417 (line)]] | alt | 74.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -10.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -9.3) |
| [[SW480 (line)]] | alt | 8.06 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.163× (z -10.0) |
| [[Hs 766T (line)]] | wt | 41.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -8.8) |
| [[A-172 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.62 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEF1-AS1]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[LEF1]] | +0.67 | +0.52 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[GLDC]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MIR3681HG]] | +0.62 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[FKBP9P1-1]] | +0.62 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[LAMC3]] | +0.61 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[ST6GAL1]] | +0.60 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[SHROOM4]] | +0.60 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[COL19A1]] | +0.58 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[C10orf90]] | +0.57 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[CSMD3]] | +0.57 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[LINC01205]] | +0.56 | +0.14 / +0.53 | ⚠ one half (not replicated) | 0.002 |  |
| [[OPRD1]] | +0.56 | +0.30 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APCDD1]] | C | APCDD1 activity raises PTPRZ1's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 3.17× lower at baseline in the lines without APCDD1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751; co-absent with the target |
| [[AGMO]] | C | AGMO activity raises PTPRZ1's level | lines that do not express AGMO (30) vs lines expressing it (20) | 2.63× lower at baseline in the lines without AGMO | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657; co-absent with the target |
| [[VSNL1]] | C | VSNL1 activity raises PTPRZ1's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.08× lower at baseline in the lines without VSNL1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 11, C 11. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3TC2]] | B | PTPRZ1 activity raises SH3TC2's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.96× lower at baseline in the lines without PTPRZ1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[LINC02981]] | B | PTPRZ1 activity raises LINC02981's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 1.80× lower at baseline in the lines without PTPRZ1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[ETV4]] | B | PTPRZ1 activity raises ETV4's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 1.82× lower at baseline in the lines without PTPRZ1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[NKD2]] | B | PTPRZ1 activity raises NKD2's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.10× lower at baseline in the lines without PTPRZ1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[ANKRD20A1]] | B | PTPRZ1 activity raises ANKRD20A1's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.55× lower at baseline in the lines without PTPRZ1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[CNTNAP3P2]] | B | PTPRZ1 activity raises CNTNAP3P2's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.01× lower at baseline in the lines without PTPRZ1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[SDC3]] | B | PTPRZ1 activity raises SDC3's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.12× lower at baseline in the lines without PTPRZ1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[AKAP6]] | B | PTPRZ1 activity raises AKAP6's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.54× lower at baseline in the lines without PTPRZ1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[PARVG]] | B | PTPRZ1 activity raises PARVG's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.37× lower at baseline in the lines without PTPRZ1 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[EFR3B]] | B | PTPRZ1 activity raises EFR3B's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.57× lower at baseline in the lines without PTPRZ1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[ENTREP2]] | B | PTPRZ1 activity raises ENTREP2's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 1.94× lower at baseline in the lines without PTPRZ1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[APCDD1]] | C | PTPRZ1 activity raises APCDD1's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 3.28× lower at baseline in the lines without PTPRZ1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.662). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.7, 29.3); signed map (28.4, 37.9). **Vector** length 33.6, 12.1% of its response variance represented; |z| ≥ 3 in 226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +15.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +2.3 |
|  | [[EX229 (drug)]] 5 µM |  | +0.7 | +1.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.7 | +3.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.0 | -1.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.8 | +0.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -3.1 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.7 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type Z1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.32 — chr7:121,873,089-122,062,036 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTP18, RPTPB, phosphacan; previously PTPZ, PTPRZ |
| Gene groups (HGNC) | Fibronectin type III domain containing; Protein tyrosine phosphatases receptor type |
| Reactome | 6 pathways, smallest: MDK and PTN in ALK signaling; Other interleukin signaling; Signaling by ALK |
| Matched by | ensembl_id |

**Function**, from UniProt [P23471](https://www.uniprot.org/uniprotkb/P23471) (Receptor-type tyrosine-protein phosphatase zeta):

> Protein tyrosine phosphatase that negatively regulates oligodendrocyte precursor proliferation in the embryonic spinal cord. Required for normal differentiation of the precursor cells into mature, fully myelinating oligodendrocytes. May play a role in protecting oligondendrocytes against apoptosis. May play a role in the establishment of contextual memory, probably via the dephosphorylation of proteins that are part of important signaling cascades (By similarity).

**Summary**, from NCBI Gene [5803](https://www.ncbi.nlm.nih.gov/gene/5803):

> This gene encodes a member of the receptor protein tyrosine phosphatase family. Expression of this gene is restricted to the central nervous system (CNS), and it may be involved in the regulation of specific developmental processes in the CNS. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, May 2011]

**Accessions** — [HGNC:9685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9685) · Entrez [5803](https://www.ncbi.nlm.nih.gov/gene/5803) · UniProt [P23471](https://www.uniprot.org/uniprotkb/P23471) · Ensembl [ENSG00000106278](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106278)

## Data

Gene col 2739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2739); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2739]; `tensor/DDL_lfc|DDL_z.npy` [2739]; `embed/gene_vectors.npy` [2739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2739 or target_col == 2739). Every well: [[PTPRZ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRZ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
