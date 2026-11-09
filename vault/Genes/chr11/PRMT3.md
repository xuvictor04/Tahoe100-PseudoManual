---
symbol: "PRMT3"
type: "gene"
col: 11644
ensembl_id: "ENSG00000185238"
name: "protein arginine methyltransferase 3"
location: "11p15.1"
module: 5
arm: "+"
pooled_cpm: 44.45
n_lines_expressing: 48
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PRMT3

*protein arginine methyltransferase 3* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.12× (z +14.7, q 0e+00, up in 40 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.570×; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.477×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (PANC-1 0.478×; ⚠ transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR4]] (+0.76, fdr 7e-06), [[ATR]] (+0.76, fdr 7e-06), [[METTL8]] (+0.75, fdr 7e-06); moves opposite to [[RNASE4]] (-0.69, fdr 7e-06), [[ANG]] (-0.67, fdr 7e-06), [[VPS37D]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[HLCS]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11644.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +14.7 | 0e+00 | 40/46 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.92×** | +8.7 | 7e-16 | 32/45 (HOP62, HS-578T, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.84×** | +8.5 | 4e-15 | 40/46 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +7.0 | 4e-10 | 28/46 (NCI-H460, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +6.5 | 1e-08 | 25/46 (MIA PaCa-2, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.58×** | +6.3 | 3e-08 | 24/46 (AsPC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.56×** | +6.1 | 7e-08 | 23/46 (HOP62, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.47×** | +5.4 | 5e-06 | 24/45 (HOP62, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.49×** | +5.3 | 6e-06 | 23/45 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +5.2 | 9e-06 | 24/45 (NCI-H1573, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.45×** | +5.0 | 3e-05 | 25/46 (HOP62, Panc 03.27, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.7 | 1e-04 | 24/45 (HT-29, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.40×** | +4.7 | 1e-04 | 22/45 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.41×** | +4.5 | 2e-04 | 19/37 (NCI-H2347, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +4.5 | 2e-04 | 26/45 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +4.5 | 3e-04 | 21/46 (NCI-H460, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.4 | 3e-04 | 23/46 (H4, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +4.4 | 3e-04 | 22/46 (HOP62, A549, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.79×** | +4.2 | 7e-04 | 27/45 (MIA PaCa-2, A498, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.35×** | +4.1 | 1e-03 | 17/45 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 1e-03 | 25/45 (NCI-H1573, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.004 | 21/45 (NCI-H1573, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.004 | 20/46 (HOP62, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.63×** | +3.5 | 0.010 | 18/45 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.570×; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.477×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (PANC-1 0.478×; ⚠ transcription drop; cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11644. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 50.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +18.9) | — |
| [[Hs 766T (line)]] | wt | 31.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 64.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.73× (z +10.2) ⚠ unreliable plate only · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.64× (z +9.5) | [[Adagrasib (drug)]] 0.05 µM 0.570× (z -15.1) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 25.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 22.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 103 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.19× (z +8.9) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 21.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +13.8) | — |
| [[HS-578T (line)]] | alt | 20.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +12.0) | — |
| [[A-172 (line)]] | wt | 25.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +8.5) | — |
| [[A498 (line)]] | wt | 36.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 39.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +13.1) | — |
| [[hTERT-HPNE (line)]] | wt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +9.0) | — |
| [[J82 (line)]] | alt | 49.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.7) | — |
| [[LoVo (line)]] | wt | 59.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 34.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 25.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +12.2) | — |
| [[SW1417 (line)]] | alt | 56.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.5) | — |
| [[A-427 (line)]] | wt | 93.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 94.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 86.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11644), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR4]] | +0.76 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[ATR]] | +0.76 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[METTL8]] | +0.75 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.73 | +0.75 / +0.72 | both halves | 7e-06 | STRING 444 |
| [[LETM1]] | +0.72 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.72 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[PUM3]] | +0.72 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[GART]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[SPOPL-DT]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[ALG8]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[UTP20]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[ABCF2]] | +0.71 | +0.67 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNASE4]] | -0.69 | -0.70 / -0.62 | both halves | 7e-06 |  |
| [[ANG]] | -0.67 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[VPS37D]] | -0.63 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[CDKN2D]] | -0.63 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[AHDC1]] | -0.63 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[SIRT2]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[AFTPH]] | -0.62 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[HDAC5]] | -0.62 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[DBP]] | -0.62 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[ARL3]] | -0.61 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[PJA2]] | -0.61 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[SECISBP2L]] | -0.61 | -0.61 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRMT3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC17A7]] | B | SLC17A7 activity raises PRMT3's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.59× lower at baseline in the lines without SLC17A7 | 0.084 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[PALD1]] | B | PALD1 activity raises PRMT3's level | lines that do not express PALD1 (16) vs lines expressing it (34) | 1.49× lower at baseline in the lines without PALD1 | 0.098 | ⚠ within organs, on part of the lines; also absent: NKD2, ADRA2C, IGSF9B |
| [[MTHFD1L]] | C | MTHFD1L activity raises PRMT3's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.26× lower at baseline in the lines without MTHFD1L | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLCS]] | C | PRMT3's natural level strengthens HLCS's drug response | PRMT3's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.22; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.821). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-12.2, -33.4); signed map (0.1, -50.7). **Vector** length 125, 36.8% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.55 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.55 to 19); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.53 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.2 | +8.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.0 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +14.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +4.5 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.1 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.9 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.8 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -3.7 | +6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | protein arginine methyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:20,387,558-20,509,338 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HRMT1L3 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; 7BS protein arginine methyltranferases; Arginine methyltransferases |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 4 pathways, smallest: Protein methylation; RMTs methylate histone arginines; Chromatin modifying enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [O60678](https://www.uniprot.org/uniprotkb/O60678) (Protein arginine N-methyltransferase 3):

> Protein-arginine N-methyltransferase that catalyzes both the monomethylation and asymmetric dimethylation of the guanidino nitrogens of arginine residues in target proteins, and therefore falls into the group of type I methyltransferases. Catalyzes the asymmetric arginine dimethylation at multiple sites in the Arg/Gly-rich region of small ribosomal subunit protein uS5/RPS2. Also appears to methylate other ribosomal proteins (By similarity). May regulate retinoic acid synthesis and signaling by …

**Summary**, from NCBI Gene [10196](https://www.ncbi.nlm.nih.gov/gene/10196):

> This gene belongs to the protein arginine methyltransferase (PRMT) family. The encoded enzyme catalyzes the methylation of guanidino nitrogens of arginyl residues of proteins. The enzyme acts on 40S ribosomal protein S2 (rpS2), which is its major in-vivo substrate, and is involved in the proper maturation of the 80S ribosome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:30163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30163) · Entrez [10196](https://www.ncbi.nlm.nih.gov/gene/10196) · UniProt [O60678](https://www.uniprot.org/uniprotkb/O60678) · Ensembl [ENSG00000185238](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185238)

## Data

Gene col 11644: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11644); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11644, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11644]; `tensor/DDL_lfc|DDL_z.npy` [11644]; `embed/gene_vectors.npy` [11644]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11644 or target_col == 11644). Every well: [[PRMT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRMT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
