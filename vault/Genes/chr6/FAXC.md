---
symbol: "FAXC"
type: "gene"
col: 7080
ensembl_id: "ENSG00000146267"
name: "failed axon connections homolog, metaxin like GST domain containing"
location: "6q16.2"
module: 10
arm: "+"
pooled_cpm: 6.08
n_lines_expressing: 39
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 16
direction_downstream: 31
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FAXC

*failed axon connections homolog, metaxin like GST domain containing* — 6q16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.63× (z +8.0, q 7e-13, up in 19 of 34 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.73× (z +6.3, q 7e-08, up in 14 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.529× (z -7.4, q 9e-11, down in 20 of 33 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.594× (z -6.0, q 3e-07, down in 19 of 35 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPLD1]] (+0.72, fdr 7e-06), [[PCDHA6]] (+0.66, fdr 1e-05), [[MSI1]] (+0.61, fdr 1e-05); moves opposite to [[EFHC1]] (-0.55, fdr 2e-04), [[CETN2]] (-0.53, fdr 2e-04), [[TOM1L2]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[SLC4A3]] → it (grade B ⚠); 31 go from it, the strongest it → [[SLC4A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7080.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.63×** | +8.0 | 7e-13 | 19/34 (C32, RKO, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +6.3 | 7e-08 | 14/33 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +6.0 | 4e-07 | 15/35 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +5.4 | 7e-06 | 13/34 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.50×** | +4.7 | 3e-04 | 8/34 (SW 900, NCI-H1573, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.6 | 4e-04 | 11/32 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +3.7 | 0.015 | 5/11 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.034 | 6/33 (AN3 CA, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.039 | 9/34 (MIA PaCa-2, A549, …) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.051 | 2/35 (LoVo, A498) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7080.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.529×** | -7.4 | 9e-11 | 20/33 (SHP-77, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.535×** | -7.3 | 1e-10 | 21/35 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.594×** | -6.0 | 3e-07 | 19/35 (C-33 A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.623×** | -5.5 | 6e-06 | 17/35 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.624×** | -5.5 | 6e-06 | 15/33 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.655×** | -4.9 | 9e-05 | 18/35 (J82, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.671×** | -4.5 | 7e-04 | 14/34 (RKO, Panc 03.27, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.715×** | -3.9 | 0.007 | 15/33 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM |  | **0.796×** | -3.7 | 0.012 | 12/35 (H4, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.732×** | -3.6 | 0.017 | 11/35 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.735×** | -3.6 | 0.018 | 16/35 (SHP-77, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.759×** | -3.2 | 0.067 | 3/34 (BT-474, SW 900, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.768×** | -3.1 | 0.096 | 9/35 (BT-474, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7080. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 18.3 | 0 | 5 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.250× (z -9.4) |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.146× (z -10.2) |
| [[SW48 (line)]] | wt | 17.6 | 0 | 3 (1 ⚠) | — | [[Pioglitazone (drug)]] 0.5 µM 0.0672× (z -11.1) |
| [[C-33 A (line)]] | alt | 20.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0681× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 9.30 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.122× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[SW480 (line)]] | alt | 20.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 5.58 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0819× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 5.21 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0608× (z -10.2) ⚠ transcription drop; unreliable plate only |
| [[NCI-H460 (line)]] | wt | 2.54 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0600× (z -10.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RKO (line)]] | wt | 8.48 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0760× (z -9.3) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A-172 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.770 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7080), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPLD1]] | +0.72 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[PCDHA6]] | +0.66 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[MSI1]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[DHRS4L2]] | +0.60 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[USP46]] | +0.59 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[LRRN2]] | +0.59 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[GRID1]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[SLC25A21]] | +0.58 | +0.61 / +0.37 | both halves | 9e-05 |  |
| [[SRSF12]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[LINC02026]] | +0.57 | +0.51 / +0.24 | both halves | 5e-04 |  |
| [[PM20D2]] | +0.56 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[TGFBRAP1]] | +0.56 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFHC1]] | -0.55 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[CETN2]] | -0.53 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[TOM1L2]] | -0.51 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[PIN1]] | -0.48 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[KRBOX4]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[RNF24]] | -0.47 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[SPAG9]] | -0.47 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[UBA6]] | -0.47 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[KIAA0319L]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ALDOA]] | -0.46 | -0.42 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A3]] | B | SLC4A3 activity raises FAXC's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.76× lower at baseline in the lines without SLC4A3 | 0.008 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[FAM184A]] | B | FAM184A activity raises FAXC's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.12× lower at baseline in the lines without FAM184A | 0.013 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[EMID1]] | B | EMID1 activity raises FAXC's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 2.24× lower at baseline in the lines without EMID1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[EBF4]] | B | EBF4 activity raises FAXC's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 2.29× lower at baseline in the lines without EBF4 | 0.032 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[MSI1]] | B | MSI1 activity raises FAXC's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.16× lower at baseline in the lines without MSI1 | 0.040 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[GPLD1]] | B | GPLD1 activity raises FAXC's level | lines that do not express GPLD1 (5) vs lines expressing it (45) | 2.68× lower at baseline in the lines without GPLD1 | 0.046 | ⚠ within organs, on part of the lines; also absent: PDE5A, ALDH5A1, CCDC144CP; maybe low, not absent |
| [[TBX1]] | B | TBX1 activity raises FAXC's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without TBX1 | 0.048 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1 |
| [[TMEM150C]] | B | TMEM150C activity raises FAXC's level | lines that do not express TMEM150C (13) vs lines expressing it (37) | 2.28× lower at baseline in the lines without TMEM150C | 0.053 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent |
| [[ALDH5A1]] | B | ALDH5A1 activity raises FAXC's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 2.18× lower at baseline in the lines without ALDH5A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ; its own permutation p |
| [[ZNF618]] | B | ZNF618 activity raises FAXC's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 2.44× lower at baseline in the lines without ZNF618 | 0.071 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |
| [[FAM66C]] | B | FAM66C activity raises FAXC's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without FAM66C | 0.075 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[MRAS]] | B | MRAS activity raises FAXC's level | lines that do not express MRAS (11) vs lines expressing it (39) | 2.22× lower at baseline in the lines without MRAS | 0.084 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 31, C 0. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A3]] | B | FAXC activity raises SLC4A3's level | lines that do not express FAXC (11) vs lines expressing it (39) | 2.32× lower at baseline in the lines without FAXC | 0.005 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[PM20D2]] | B | FAXC activity raises PM20D2's level | lines that do not express FAXC (11) vs lines expressing it (39) | 2.45× lower at baseline in the lines without FAXC | 0.006 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[LARP1]] | B | FAXC activity raises LARP1's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.29× lower at baseline in the lines without FAXC | 0.009 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[ATP6V1E2]] | B | FAXC activity raises ATP6V1E2's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.86× lower at baseline in the lines without FAXC | 0.016 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[RAVER2]] | B | FAXC activity raises RAVER2's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without FAXC | 0.017 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[USP46]] | B | FAXC activity raises USP46's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without FAXC | 0.029 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[DIS3L]] | B | FAXC activity raises DIS3L's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without FAXC | 0.029 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[FAM66C]] | B | FAXC activity raises FAM66C's level | lines that do not express FAXC (11) vs lines expressing it (39) | 2.06× lower at baseline in the lines without FAXC | 0.030 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[PKN3]] | B | FAXC activity raises PKN3's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without FAXC | 0.037 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[RAD51D]] | B | FAXC activity raises RAD51D's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.47× lower at baseline in the lines without FAXC | 0.037 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[GINS3]] | B | FAXC activity raises GINS3's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.56× lower at baseline in the lines without FAXC | 0.038 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[ULK2]] | B | FAXC activity raises ULK2's level | lines that do not express FAXC (11) vs lines expressing it (39) | 3.81× lower at baseline in the lines without FAXC | 0.041 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.382). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.3, 33.1); signed map (39.0, -10.9). **Vector** length 59.8, 10.7% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.3 | +1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.9 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +3.8 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +5.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.9 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +3.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.5 | -6.0 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.8 | -7.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | failed axon connections homolog, metaxin like GST domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.2 — chr6:99,271,168-99,350,062 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2817, dJ273F20; previously C6orf168 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TGI0](https://www.uniprot.org/uniprotkb/Q5TGI0) (Failed axon connections homolog):

> May play a role in axonal development.

**Summary**, from NCBI Gene [84553](https://www.ncbi.nlm.nih.gov/gene/84553):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20742](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20742) · Entrez [84553](https://www.ncbi.nlm.nih.gov/gene/84553) · UniProt [Q5TGI0](https://www.uniprot.org/uniprotkb/Q5TGI0) · Ensembl [ENSG00000146267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146267)

## Data

Gene col 7080: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7080); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7080, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7080]; `tensor/DDL_lfc|DDL_z.npy` [7080]; `embed/gene_vectors.npy` [7080]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7080 or target_col == 7080). Every well: [[FAXC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAXC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
