---
symbol: "KREMEN2"
type: "gene"
col: 5228
ensembl_id: "ENSG00000131650"
name: "kringle containing transmembrane protein 2"
location: "16p13.3"
module: 100
arm: "+"
pooled_cpm: 2.82
n_lines_expressing: 37
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 19
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# KREMEN2

*kringle containing transmembrane protein 2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.06× (z +13.9, q 5e-41, up in 16 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0517×); [[Panobinostat (drug)]] 5 µM in 1 line (A-427 0.150×; ⚠ cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0851×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLIS2]] (+0.60, fdr 8e-06), [[CBFA2T3]] (+0.58, fdr 1e-05), [[ICAM5]] (+0.58, fdr 1e-05); moves opposite to [[AGAP9]] (-0.45, fdr 5e-04), [[AGAP13P]] (-0.44, fdr 1e-04), [[AGAP5]] (-0.43, fdr 2e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ELFN1]] → it (grade B ⚠); 19 go from it, the strongest it → [[XRCC5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5228.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.06×** | +13.9 | 5e-41 | 16/25 (A549, A498, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.28×** | +10.2 | 4e-22 | 13/28 (HepG2/C3A, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.48×** | +7.7 | 4e-12 | 1/3 (PANC-1) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.26×** | +6.9 | 9e-10 | 14/31 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.14×** | +6.7 | 3e-09 | 3/10 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +5.9 | 3e-07 | 4/14 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +5.7 | 9e-07 | 10/33 (LoVo, HCT15, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.88×** | +5.5 | 2e-06 | 9/34 (RKO, A549, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.87×** | +5.5 | 3e-06 | 5/18 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.86×** | +5.4 | 3e-06 | 12/32 (HT-29, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +4.9 | 6e-05 | 10/31 (SNU-1, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.72×** | +4.4 | 6e-04 | 2/5 (A498, PANC-1) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.60×** | +4.1 | 0.002 | 5/33 (RKO, HCT15, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +4.0 | 0.003 | 3/14 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.8 | 0.005 | 3/23 (A-427, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +3.5 | 0.015 | 5/29 (LoVo, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.049 | 4/33 (A498, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5228.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0517×); [[Panobinostat (drug)]] 5 µM in 1 line (A-427 0.150×; ⚠ cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0851×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | 0.654× | -3.5 | 0.24 | 10/32 (SW1417, J82, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.686× | -3.3 | 0.26 | 11/33 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5228. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 26.6 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -12.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[MIA PaCa-2 (line)]] | alt | 8.03 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0517× (z -12.8) |
| [[A498 (line)]] | wt | 5.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +9.1) | — |
| [[A549 (line)]] | wt | 1.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 1.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.0× (z +8.5) | — |
| [[A-172 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.959 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.944 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.901 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.972 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5228), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLIS2]] | +0.60 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[CBFA2T3]] | +0.58 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[ICAM5]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[NRTN]] | +0.56 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[ACHE]] | +0.55 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[PDE4A]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TCF7L1]] | +0.55 | +0.43 / +0.51 | both halves | 3e-05 | pathway: Signaling by WNT |
| [[PPFIA3]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[HIP1]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[ATP23]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[PRICKLE3]] | +0.53 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[RPS6KA1]] | +0.53 | +0.46 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP9]] | -0.45 | -0.23 / -0.42 | both halves | 5e-04 |  |
| [[AGAP13P]] | -0.44 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[AGAP5]] | -0.43 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[RPRD1A]] | -0.43 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[BMS1P2]] | -0.41 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[XRCC5]] | -0.41 | -0.30 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELFN1]] | B | ELFN1 activity raises KREMEN2's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.69× lower at baseline in the lines without ELFN1 | 0.025 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[CBFA2T3]] | B | CBFA2T3 activity raises KREMEN2's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.85× lower at baseline in the lines without CBFA2T3 | 0.031 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[SEMA6B]] | B | SEMA6B activity raises KREMEN2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.97× lower at baseline in the lines without SEMA6B | 0.037 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[KCNQ2]] | B | KCNQ2 activity raises KREMEN2's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 1.73× lower at baseline in the lines without KCNQ2 | 0.056 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[ACHE]] | C | ACHE activity raises KREMEN2's level | lines that do not express ACHE (17) vs lines expressing it (33) | 1.62× lower at baseline in the lines without ACHE | 0.083 | ⚠ within organs, on part of the lines; also absent: DKK1, KREMEN2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 18, C 1. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XRCC5]] | B | KREMEN2 activity raises XRCC5's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without KREMEN2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[ZNF57]] | B | KREMEN2 activity raises ZNF57's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without KREMEN2 | 0.016 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[SEMA6B]] | B | KREMEN2 activity raises SEMA6B's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without KREMEN2 | 0.016 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[C16orf87]] | B | KREMEN2 activity raises C16orf87's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without KREMEN2 | 0.016 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[SLC26A11]] | B | KREMEN2 activity raises SLC26A11's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without KREMEN2 | 0.030 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[CACNA2D2]] | B | KREMEN2 activity raises CACNA2D2's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without KREMEN2 | 0.051 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[NFIX]] | B | KREMEN2 activity weakens NFIX's drug response | lines that do not express KREMEN2 (11) vs lines expressing it (30) | the lines without KREMEN2 respond 1.25× as strongly (z diff -0.75); strongest at Dinaciclib 5 µM: 2.52x vs 1.37x (z diff -5.6) | 0.060 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[CBFA2T3]] | B | KREMEN2 activity raises CBFA2T3's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.85× lower at baseline in the lines without KREMEN2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[AGAP3]] | B | KREMEN2 activity raises AGAP3's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without KREMEN2 | 0.062 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[MAST1]] | B | KREMEN2 activity raises MAST1's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 2.05× lower at baseline in the lines without KREMEN2 | 0.067 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[TLE2]] | B | KREMEN2 activity raises TLE2's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.43× lower at baseline in the lines without KREMEN2 | 0.073 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[LRP1]] | B | KREMEN2 activity lowers LRP1's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.58× higher at baseline in the lines without KREMEN2 | 0.079 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.5, -4.4); signed map (21.5, 20.6). **Vector** length 42.8, 6.07% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +13.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +10.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.2 | +6.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +1.8 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.8 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.8 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.8 | +1.3 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | kringle containing transmembrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,964,216-2,968,380 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10791, KRM2 |
| Gene groups (HGNC) | Kringle domain containing |
| Reactome | 6 pathways, smallest: Signaling by LRP5 mutants; Negative regulation of TCF-dependent signaling by WNT ligand antagonists; Signaling by WNT in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCW0](https://www.uniprot.org/uniprotkb/Q8NCW0) (Kremen protein 2):

> Receptor for Dickkopf proteins. Cooperates with DKK1/2 to inhibit Wnt/beta-catenin signaling by promoting the endocytosis of Wnt receptors LRP5 and LRP6. Plays a role in limb development; attenuates Wnt signaling in the developing limb to allow normal limb patterning and can also negatively regulate bone formation.

**Summary**, from NCBI Gene [79412](https://www.ncbi.nlm.nih.gov/gene/79412):

> This gene encodes a high-affinity dickkopf homolog 1 (DKK1) transmembrane receptor. A similar protein in mouse functions interacts with with DKK1 to block wingless (WNT)/beta-catenin signaling. The encoded protein forms a ternary membrane complex with DKK1 and the WNT receptor lipoprotein receptor-related protein 6 (LRP6), and induces rapid endocytosis and removal of LRP6 from the plasma membrane. It contains extracellular kringle, WSC, and CUB domains. Alternatively spliced transcript variants …

**Accessions** — [HGNC:18797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18797) · Entrez [79412](https://www.ncbi.nlm.nih.gov/gene/79412) · UniProt [Q8NCW0](https://www.uniprot.org/uniprotkb/Q8NCW0) · Ensembl [ENSG00000131650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131650)

## Data

Gene col 5228: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5228); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5228, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5228]; `tensor/DDL_lfc|DDL_z.npy` [5228]; `embed/gene_vectors.npy` [5228]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5228 or target_col == 5228). Every well: [[KREMEN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KREMEN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
