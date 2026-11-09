---
symbol: "SORCS1"
type: "gene"
col: 2910
ensembl_id: "ENSG00000108018"
name: "sortilin related VPS10 domain containing receptor 1"
location: "10q25.1"
module: 166
arm: "+"
pooled_cpm: 5.95
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# SORCS1

*sortilin related VPS10 domain containing receptor 1* — 10q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.05× (z +16.8, q 0e+00, up in 27 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.203×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.193×; ⚠ cell-cycle shift, explains ~21% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.255×); [[Bestatin (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0544×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OBI1-AS1]] (+0.83, fdr 7e-06), [[CNBD1]] (+0.83, fdr 7e-06), [[CNTN4]] (+0.81, fdr 7e-06).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LINC01320]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2910.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +16.8 | 0e+00 | 27/35 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.67×** | +14.8 | 0e+00 | 34/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.76×** | +14.1 | 8e-43 | 11/17 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.49×** | +13.8 | 6e-41 | 24/35 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.22×** | +12.0 | 6e-31 | 1/4 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.87×** | +11.2 | 3e-27 | 28/41 (C32, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +8.0 | 1e-13 | 1/6 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.99×** | +7.3 | 2e-11 | 22/39 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +5.9 | 3e-07 | 16/45 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +5.8 | 5e-07 | 16/45 (NCI-H23, A-172, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +4.9 | 5e-05 | 13/41 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +4.6 | 2e-04 | 2/15 (PANC-1, KATO III) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +4.2 | 0.001 | 8/39 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.002 | 10/44 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.021 | 9/42 (A-172, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.025 | 12/43 (A-172, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.049 | 4/39 (A-427, CFPAC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.065 | 10/46 (A-172, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.066 | 10/44 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2910.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.203×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.193×; ⚠ cell-cycle shift, explains ~21% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.255×); [[Bestatin (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0544×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.896× | -4.2 | 0.018 | 16/47 (H4, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2910. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.95 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.37× (z +11.9) | — |
| [[A-172 (line)]] | wt | 24.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 8.63× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 71.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -10.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 102 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.41× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 1.75 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.7× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 3.16 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.18× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 1.52 | 0 | 1 | — | [[Bestatin (hydrochloride) (drug)]] 0.5 µM 0.0544× (z -8.5) |
| [[PANC-1 (line)]] | alt | 1.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.89× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 2.68 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.71× (z +8.7) | — |
| [[SW480 (line)]] | alt | 1.82 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.7× (z +12.3) | — |
| [[A-427 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2910), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OBI1-AS1]] | +0.83 | +0.76 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[CNBD1]] | +0.83 | +0.67 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[CNTN4]] | +0.81 | +0.68 / +0.85 | both halves | 7e-06 | STRING 550 |
| [[ESR1]] | +0.80 | +0.77 / +0.81 | both halves | 7e-06 |  |
| [[DCC]] | +0.79 | +0.65 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[PTPRT]] | +0.77 | +0.65 / +0.79 | both halves | 7e-06 |  |
| [[PWRN1]] | +0.76 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[ST8SIA1]] | +0.76 | +0.73 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SYN3]] | +0.75 | +0.64 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[LINC02208]] | +0.75 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[LUZP2]] | +0.75 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.75 | +0.69 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01320]] | B | LINC01320 activity raises SORCS1's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 3.08× lower at baseline in the lines without LINC01320 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168 |
| [[STXBP5L]] | B | STXBP5L activity raises SORCS1's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 1.79× lower at baseline in the lines without STXBP5L | 0.030 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent |
| [[LINC02055]] | B | LINC02055 activity raises SORCS1's level | lines that do not express LINC02055 (30) vs lines expressing it (20) | 2.20× lower at baseline in the lines without LINC02055 | 0.032 | ⚠ within organs, on part of the lines; also absent: BAGE2, LINC01446, ENSG00000234352; maybe low, not absent |
| [[LINC02220]] | B | LINC02220 activity raises SORCS1's level | lines that do not express LINC02220 (22) vs lines expressing it (28) | 1.70× lower at baseline in the lines without LINC02220 | 0.036 | ⚠ within organs, on part of the lines; also absent: COL16A1, SEMA5A, ANKRD30B; maybe low, not absent |
| [[RERGL]] | B | RERGL activity raises SORCS1's level | lines that do not express RERGL (9) vs lines expressing it (41) | 1.75× lower at baseline in the lines without RERGL | 0.041 | ⚠ within organs, on part of the lines; also absent: DPYS, TUSC3; maybe low, not absent |
| [[MIR3681HG]] | B | MIR3681HG activity raises SORCS1's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 2.24× lower at baseline in the lines without MIR3681HG | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[TRPM8]] | B | TRPM8 activity raises SORCS1's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 1.85× lower at baseline in the lines without TRPM8 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent |
| [[DGKB]] | B | DGKB activity raises SORCS1's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without DGKB | 0.074 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[PTPRN]] | B | PTPRN activity raises SORCS1's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 2.69× lower at baseline in the lines without PTPRN | 0.077 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.867). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.2, 29.2); signed map (32.7, 15.7). **Vector** length 58.7, 8.49% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +14.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +16.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +14.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +2.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -4.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | sortilin related VPS10 domain containing receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.1 — chr10:106,573,663-107,164,706 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q8WY21](https://www.uniprot.org/uniprotkb/Q8WY21) carries no function annotation.

**Summary**, from NCBI Gene [114815](https://www.ncbi.nlm.nih.gov/gene/114815):

> This gene encodes one family member of vacuolar protein sorting 10 (VPS10) domain-containing receptor proteins. The VPS10 domain name comes from the yeast carboxypeptidase Y sorting receptor Vps10 protein. Members of this gene family are large with many exons but the CDS lengths are usually less than 3700 nt. Very large introns typically separate the exons encoding the VPS10 domain; the remaining exons are separated by much smaller-sized introns. These genes are strongly expressed in the …

**Accessions** — [HGNC:16697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16697) · Entrez [114815](https://www.ncbi.nlm.nih.gov/gene/114815) · UniProt [Q8WY21](https://www.uniprot.org/uniprotkb/Q8WY21) · Ensembl [ENSG00000108018](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108018)

## Data

Gene col 2910: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2910); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2910, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2910]; `tensor/DDL_lfc|DDL_z.npy` [2910]; `embed/gene_vectors.npy` [2910]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2910 or target_col == 2910). Every well: [[SORCS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SORCS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
