---
symbol: "TENT5C"
type: "gene"
col: 11412
ensembl_id: "ENSG00000183508"
name: "terminal nucleotidyltransferase 5C"
location: "1p12"
module: 93
arm: "+"
pooled_cpm: 6.98
n_lines_expressing: 45
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# TENT5C

*terminal nucleotidyltransferase 5C* — 1p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.77× (z +19.3, q 0e+00, up in 32 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.131×, LS 180 0.126×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (Hs 766T 0.0737×, PANC-1 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Bimatoprost (drug)]] 0.5 µM in 1 line (SW 900 0.0840×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HOP62 0.0854×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM222A]] (+0.82, fdr 7e-06), [[STARD5]] (+0.67, fdr 7e-06), [[IQCN]] (+0.66, fdr 7e-06); moves opposite to [[TIMM23B]] (-0.58, fdr 1e-05), [[EMC8]] (-0.56, fdr 1e-05), [[AAGAB]] (-0.55, fdr 4e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EPHB3]] → it (grade B ⚠); 2 go from it, the strongest it → [[LINC01291]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11412.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.77×** | +19.3 | 0e+00 | 32/34 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **7.06×** | +15.2 | 0e+00 | 41/42 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.10×** | +11.0 | 7e-26 | 38/42 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.68×** | +10.6 | 6e-24 | 37/40 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.82×** | +10.4 | 2e-23 | 23/34 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.09×** | +8.5 | 3e-15 | 25/36 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +6.9 | 6e-10 | 24/41 (SK-MEL-2, SHP-77, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.48×** | +6.8 | 6e-10 | 14/27 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.30×** | +6.5 | 5e-09 | 20/38 (LoVo, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.12×** | +5.8 | 3e-07 | 25/42 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.94×** | +5.2 | 1e-05 | 19/40 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.91×** | +5.1 | 2e-05 | 21/42 (NCI-H460, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.56×** | +4.9 | 4e-05 | 16/33 (NCI-H460, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.4 | 5e-04 | 10/41 (J82, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +4.3 | 6e-04 | 17/41 (SW480, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +4.0 | 0.002 | 15/41 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +3.8 | 0.004 | 15/40 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11412.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.131×, LS 180 0.126×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (Hs 766T 0.0737×, PANC-1 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Bimatoprost (drug)]] 0.5 µM in 1 line (SW 900 0.0840×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HOP62 0.0854×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.604× | -3.1 | 0.88 | 12/37 (HOP62, Hs 766T, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11412. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 6.00 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +14.1) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0854× (z -8.8) |
| [[LS 180 (line)]] | wt | 18.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[PANC-1 (line)]] | alt | 11.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.88× (z +12.7) | — |
| [[SW 900 (line)]] | alt | 9.26 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +10.8) | [[Bimatoprost (drug)]] 0.5 µM 0.0840× (z -9.3) |
| [[A498 (line)]] | wt | 2.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +12.1) | — |
| [[C32 (line)]] | wt | 4.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 9.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.63× (z +12.2) | — |
| [[COLO 205 (line)]] | alt | 10.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 3.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0737× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 5.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +10.2) | — |
| [[J82 (line)]] | alt | 7.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +10.0) | — |
| [[KATO III (line)]] | alt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +11.0) | — |
| [[LoVo (line)]] | wt | 7.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 7.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 1.94 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 54.0× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[NCI-H460 (line)]] | wt | 3.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.51× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 5.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +9.0) | — |
| [[SW480 (line)]] | alt | 7.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +8.7) | — |
| [[A-172 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.923 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11412), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM222A]] | +0.82 | +0.82 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[STARD5]] | +0.67 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[IQCN]] | +0.66 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[MYLIP]] | +0.65 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[FOSB]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[LGMN]] | +0.63 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[HSPA2]] | +0.62 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[OSR2]] | +0.62 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[BPGM]] | +0.62 | +0.57 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM; STRING 557 |
| [[SNAI1]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[FAM53C]] | +0.61 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[FOS]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B]] | -0.58 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[EMC8]] | -0.56 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[AAGAB]] | -0.55 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[PGS1]] | -0.54 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[SCO1]] | -0.54 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[RRP36]] | -0.52 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[ARMC8]] | -0.52 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[NDUFS6]] | -0.52 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[NDUFAF5]] | -0.51 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[TIMM23]] | -0.51 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[TRMT61B]] | -0.51 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[KPNA1]] | -0.50 | -0.55 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHB3]] | B | EPHB3 activity raises TENT5C's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 2.13× lower at baseline in the lines without EPHB3 | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[ATP1B1]] | B | ATP1B1 activity raises TENT5C's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 2.32× lower at baseline in the lines without ATP1B1 | 0.028 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[NEDD9]] | B | NEDD9 activity raises TENT5C's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.84× lower at baseline in the lines without NEDD9 | 0.082 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01291]] | B | TENT5C activity raises LINC01291's level | lines that do not express TENT5C (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without TENT5C | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000258695, CTSD, BRME1; maybe low, not absent |
| [[VASN]] | B | TENT5C activity raises VASN's level | lines that do not express TENT5C (5) vs lines expressing it (45) | 2.51× lower at baseline in the lines without TENT5C | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000258695, CTSD, BRME1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.2, -28.3); signed map (0.6, 18.2). **Vector** length 80.6, 17.4% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +19.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.0 | +1.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +1.0 |
| fall | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.0 | -3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +1.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -1.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | terminal nucleotidyltransferase 5C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p12 — chr1:117,606,048-117,628,389 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20202; previously FAM46C |
| Gene groups (HGNC) | Terminal nucleotidyltransferases |
| Hallmark sets | KRAS_SIGNALING_DN, HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VWP2](https://www.uniprot.org/uniprotkb/Q5VWP2) (Terminal nucleotidyltransferase 5C):

> Catalyzes the transfer of one adenosine molecule from an ATP to an mRNA poly(A) tail bearing a 3'-OH terminal group and enhances mRNA stability and gene expression. Can also elongate RNA oligos ending with uridine molecule, provided that the sequence is adenosine-rich. Mainly targets mRNAs encoding endoplasmic reticulum-targeted protein.; (Microbial infection) Seems to enhance replication of some viruses, including yellow fever virus, in response to type I interferon.

**Summary**, from NCBI Gene [54855](https://www.ncbi.nlm.nih.gov/gene/54855):

> Enables poly(A) RNA polymerase activity. Involved in mRNA stabilization and negative regulation of cell differentiation. Located in centrosome; cytoplasm; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24712](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24712) · Entrez [54855](https://www.ncbi.nlm.nih.gov/gene/54855) · UniProt [Q5VWP2](https://www.uniprot.org/uniprotkb/Q5VWP2) · Ensembl [ENSG00000183508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183508)

## Data

Gene col 11412: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11412); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11412, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11412]; `tensor/DDL_lfc|DDL_z.npy` [11412]; `embed/gene_vectors.npy` [11412]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11412 or target_col == 11412). Every well: [[TENT5C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TENT5C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
