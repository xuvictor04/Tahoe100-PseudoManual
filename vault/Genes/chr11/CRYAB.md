---
symbol: "CRYAB"
type: "gene"
col: 3087
ensembl_id: "ENSG00000109846"
name: "crystallin alpha B"
location: "11q23.1"
module: 60
arm: "+"
pooled_cpm: 3.78
n_lines_expressing: 18
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# CRYAB

*crystallin alpha B* — 11q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 18.5× (z +15.0, q 0e+00, up in 13 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0307×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.0573×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.0602×; ⚠ cell-cycle shift, explains ~89% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPB1]] (+0.69, fdr 7e-06), [[ST13]] (+0.57, fdr 1e-05), [[HSPA1B]] (+0.56, fdr 1e-05); moves opposite to [[STAMBPL1]] (-0.57, fdr 1e-05), [[KBTBD2]] (-0.54, fdr 2e-05), [[SPRED1]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GSG1L2]] → it (grade C ⚠); 7 go from it, the strongest it → [[SCLT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **18.5×** | +15.0 | 0e+00 | 13/13 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **13.7×** | +13.5 | 8e-39 | 11/13 (A498, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **11.7×** | +11.9 | 1e-30 | 13/13 (A498, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **9.90×** | +11.8 | 6e-30 | 12/13 (C32, SK-MEL-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **57.8×** | +10.9 | 1e-25 | 6/6 (C32, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.36×** | +8.3 | 1e-14 | 2/3 (A498, C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **19.8×** | +8.2 | 2e-14 | 11/13 (C32, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.80×** | +8.0 | 6e-14 | 4/8 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.38×** | +5.8 | 5e-07 | 2/5 (A498, SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **2.70×** | +5.3 | 8e-06 | 9/14 (NCI-H460, AN3 CA, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.96×** | +4.8 | 8e-05 | 5/13 (SW1417, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.64×** | +4.8 | 9e-05 | 3/7 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +4.7 | 1e-04 | 3/11 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 5 µM |  | **5.22×** | +4.4 | 4e-04 | 7/12 (A498, C32, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +3.8 | 0.006 | 1/8 (A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.70×** | +3.7 | 0.007 | 7/13 (C32, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **2.07×** | +3.6 | 0.012 | 6/11 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.97×** | +3.5 | 0.013 | 8/15 (NCI-H460, C32, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **3.42×** | +3.3 | 0.027 | 4/8 (A498, C32, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.91×** | +3.1 | 0.044 | 4/13 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.83×** | +3.1 | 0.052 | 5/8 (C32, SK-MEL-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3087.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0307×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.0573×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.0602×; ⚠ cell-cycle shift, explains ~89% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.513× | -3.4 | 0.44 | 4/13 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.556× | -3.1 | 0.53 | 2/14 (HEC-1-A, SW1417) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 37.4 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 51.8× (z +16.2) | — |
| [[NCI-H460 (line)]] | wt | 14.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0307× (z -11.9) |
| [[A498 (line)]] | wt | 27.9 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 21.3× (z +14.4) | — |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 36.6× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 5.57 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 67.4× (z +10.4) | — |
| [[A-172 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.947 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.678 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.878 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.706 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.991 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.519 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPB1]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 | same gene group; pathway: Cellular response to heat stress; STRING 940 |
| [[ST13]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 | pathway: Cellular response to heat stress |
| [[HSPA1B]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 | pathway: Cellular response to heat stress; STRING 687 |
| [[HSP90AB2P]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[SOD1]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 | STRING 639 |
| [[FTL]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[HSPA1A]] | +0.51 | +0.42 / +0.52 | both halves | 4e-05 | pathway: Cellular response to heat stress; STRING 690 |
| [[KIF1B]] | +0.51 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[ATP2C1]] | +0.50 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[FXR1]] | +0.50 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[AKR1C1]] | +0.50 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[MLLT11]] | +0.49 | +0.57 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAMBPL1]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[KBTBD2]] | -0.54 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[SPRED1]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[LINC00623]] | -0.51 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[VGF]] | -0.51 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[HIVEP3]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[PHLDA1]] | -0.50 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[NFE2L3]] | -0.49 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ETV4]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[EGR3]] | -0.48 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[ETV1]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ITGA3]] | -0.46 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSG1L2]] | C | GSG1L2 activity raises CRYAB's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 4.02× lower at baseline in the lines without GSG1L2 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[DCT]] | C | DCT activity raises CRYAB's level | lines that do not express DCT (42) vs lines expressing it (8) | 5.43× lower at baseline in the lines without DCT | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[USP9Y]] | C | USP9Y activity raises CRYAB's level | lines that do not express USP9Y (30) vs lines expressing it (20) | 1.57× lower at baseline in the lines without USP9Y | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises CRYAB's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 2.98× lower at baseline in the lines without SLC15A5 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCLT1]] | B | CRYAB activity lowers SCLT1's level | lines that do not express CRYAB (32) vs lines expressing it (18) | 1.08× higher at baseline in the lines without CRYAB | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, S100A1, AMBP |
| [[OSBPL10]] | B | CRYAB activity raises OSBPL10's level | lines that do not express CRYAB (32) vs lines expressing it (18) | 1.70× lower at baseline in the lines without CRYAB | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, S100A1, AMBP |
| [[ZFAND2A]] | B | CRYAB activity raises ZFAND2A's level | lines that do not express CRYAB (32) vs lines expressing it (18) | 1.55× lower at baseline in the lines without CRYAB | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, S100A1, AMBP |
| [[ETV4]] | B | CRYAB activity raises ETV4's level | lines that do not express CRYAB (32) vs lines expressing it (18) | 1.45× lower at baseline in the lines without CRYAB | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, S100A1, AMBP |
| [[VGF]] | C | CRYAB activity raises VGF's level | lines that do not express CRYAB (32) vs lines expressing it (18) | 2.77× lower at baseline in the lines without CRYAB | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, S100A1, AMBP; co-absent with the target |
| [[ETV4]] | C | CRYAB activity strengthens ETV4's drug response | lines that do not express CRYAB (31) vs lines expressing it (15) | the lines without CRYAB respond 0.93× as strongly (z diff +1.60); strongest at Trametinib (DMSO_TF solvate) 0.05 µM: 0.34x vs 0.31x (z diff +1.9) | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, S100A1, AMBP; target measured in part of the lines; rests on the correction |
| [[DCT]] | C | CRYAB activity raises DCT's level | lines that do not express CRYAB (32) vs lines expressing it (18) | 2.29× lower at baseline in the lines without CRYAB | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, S100A1, AMBP; co-absent with the target |

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.502). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-17.4, -11.3); signed map (-23.9, -27.8). **Vector** length 43.1, 12.7% of its response variance represented; |z| ≥ 3 in 359 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.5 | +11.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.4 | +15.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +11.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +13.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.1 | +10.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +5.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +8.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -1.0 | -0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -0.9 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | -1.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.6 | -2.3 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -0.6 | -1.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.6 | -2.1 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | crystallin alpha B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.1 — chr11:111,908,564-111,923,722 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPB5; previously CRYA2 |
| Gene groups (HGNC) | Small heat shock proteins |
| Hallmark sets | MYOGENESIS |
| Reactome | 4 pathways, smallest: HSF1-dependent transactivation; Cellular response to heat stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [P02511](https://www.uniprot.org/uniprotkb/P02511) (Alpha-crystallin B chain):

> May contribute to the transparency and refractive index of the lens. Has chaperone-like activity, preventing aggregation of various proteins under a wide range of stress conditions. In lens epithelial cells, stabilizes the ATP6V1A protein, preventing its degradation by the proteasome (By similarity).

**Summary**, from NCBI Gene [1410](https://www.ncbi.nlm.nih.gov/gene/1410):

> Mammalian lens crystallins are divided into alpha, beta, and gamma families. Alpha crystallins are composed of two gene products: alpha-A and alpha-B, for acidic and basic, respectively. Alpha crystallins can be induced by heat shock and are members of the small heat shock protein (HSP20) family. They act as molecular chaperones although they do not renature proteins and release them in the fashion of a true chaperone; instead they hold them in large soluble aggregates. These heterogeneous …

**Accessions** — [HGNC:2389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2389) · Entrez [1410](https://www.ncbi.nlm.nih.gov/gene/1410) · UniProt [P02511](https://www.uniprot.org/uniprotkb/P02511) · Ensembl [ENSG00000109846](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109846)

## Data

Gene col 3087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3087); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3087]; `tensor/DDL_lfc|DDL_z.npy` [3087]; `embed/gene_vectors.npy` [3087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3087 or target_col == 3087). Every well: [[CRYAB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRYAB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
