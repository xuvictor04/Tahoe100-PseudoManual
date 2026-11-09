---
symbol: "CFAP20DC"
type: "gene"
col: 8755
ensembl_id: "ENSG00000163689"
name: "CFAP20 domain containing"
location: "3p14.2"
module: 13
arm: "+"
pooled_cpm: 69.68
n_lines_expressing: 34
n_dd_up: 0
n_dd_down: 43
n_dd_up_clean: 0
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 15
direction_downstream: 6
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CFAP20DC

*CFAP20 domain containing* — 3p14.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 5.87×); [[Selinexor (drug)]] 5 µM in 1 line (J82 2.25×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.285× (z -26.5, q 0e+00, down in 27 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INSYN2B]] (+0.56, fdr 1e-05), [[SPOCD1]] (+0.54, fdr 2e-05), [[DTNA]] (+0.53, fdr 1e-05); moves opposite to [[SHROOM3]] (-0.51, fdr 3e-05), [[PLAC8]] (-0.50, fdr 5e-05), [[RSBN1L]] (-0.47, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[LINC01705]] → it (grade B ⚠); 6 go from it, the strongest it → [[MANCR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8755.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 5.87×); [[Selinexor (drug)]] 5 µM in 1 line (J82 2.25×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.28× | +3.2 | 0.57 | 12/32 (LOX-IMVI, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.24× | +3.1 | 0.57 | 15/32 (NCI-H23, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8755.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.285×** | -26.5 | 0e+00 | 27/32 (H4, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.291×** | -17.7 | 0e+00 | 28/32 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.451×** | -16.8 | 0e+00 | 30/33 (NCI-H1792, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.402×** | -13.6 | 6e-40 | 30/32 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.405×** | -13.0 | 2e-36 | 30/32 (SNU-423, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.201×** | -12.5 | 5e-34 | 32/33 (HOP62, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.437×** | -12.3 | 4e-33 | 29/32 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.470×** | -11.2 | 2e-27 | 28/32 (SNU-423, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.488×** | -10.7 | 7e-25 | 25/32 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.506×** | -10.1 | 2e-22 | 28/32 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.509×** | -10.1 | 4e-22 | 30/32 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.514×** | -9.5 | 8e-20 | 25/30 (SK-MEL-2, HOP62, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.517×** | -9.4 | 2e-19 | 29/32 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.534×** | -9.3 | 4e-19 | 24/32 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.515×** | -9.3 | 4e-19 | 27/32 (HOP62, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.559×** | -8.7 | 2e-16 | 22/32 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.352×** | -8.1 | 1e-14 | 27/32 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.625×** | -7.0 | 7e-11 | 26/32 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.650×** | -6.4 | 4e-09 | 22/32 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8755. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 298 | 0 | 30 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -31.2) |
| [[SK-MEL-2 (line)]] | alt | 390 | 0 | 18 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0306× (z -34.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.110× (z -31.6) |
| [[C32 (line)]] | wt | 188 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -26.4) |
| [[H4 (line)]] | wt | 95.8 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0352× (z -31.8) |
| [[HEC-1-A (line)]] | alt | 97.9 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -26.4) |
| [[LOX-IMVI (line)]] | wt | 142 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -17.8) |
| [[NCI-H1792 (line)]] | alt | 190 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -27.9) |
| [[CFPAC-1 (line)]] | alt | 173 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -19.9) |
| [[SNU-423 (line)]] | alt | 85.2 | 0 | 13 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.139× (z -18.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.290× (z -16.9) |
| [[HS-578T (line)]] | alt | 54.4 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 73.3 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -19.4) |
| [[A-172 (line)]] | wt | 50.8 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -20.2) |
| [[PANC-1 (line)]] | alt | 40.1 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -17.7) |
| [[RPMI-7951 (line)]] | alt | 138 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -21.7) |
| [[LoVo (line)]] | wt | 38.5 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -11.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.267× (z -10.8) |
| [[SW480 (line)]] | alt | 45.5 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.359× (z -11.1) |
| [[COLO 205 (line)]] | alt | 70.9 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.87× (z +13.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0745× (z -18.7) ⚠ toxic · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.405× (z -9.6) |
| [[J82 (line)]] | alt | 55.3 | 1 (1 ⚠) | 4 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.25× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -12.5) |
| [[A-427 (line)]] | wt | 66.2 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.294× (z -12.1) |
| [[A498 (line)]] | wt | 36.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -15.6) |
| [[AsPC-1 (line)]] | alt | 31.1 | 0 | 4 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.220× (z -9.5) |
| [[A549 (line)]] | wt | 39.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 37.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 97.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -15.5) |
| [[NCI-H2347 (line)]] | alt | 87.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -15.8) |
| [[Panc 03.27 (line)]] | alt | 83.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.8) |
| [[SW 900 (line)]] | alt | 60.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 49.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -8.9) |
| [[AN3 CA (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.57 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.70 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.84 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.33 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8755), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INSYN2B]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[SPOCD1]] | +0.54 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[DTNA]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[CALM1]] | +0.53 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[GLYATL2]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[ARHGAP22]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[KIAA1549L]] | +0.52 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[ITPR1]] | +0.52 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CLDN14-AS1]] | +0.51 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[NAV1]] | +0.51 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[RASSF2]] | +0.51 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[ARL10]] | +0.51 | +0.43 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHROOM3]] | -0.51 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[PLAC8]] | -0.50 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[RSBN1L]] | -0.47 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[LTBR]] | -0.46 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[TGFB2]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[SCNN1A]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[MTUS1]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ALDH3B1]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[AK3]] | -0.45 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[SRGN]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[SECTM1]] | -0.44 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[LARP1]] | -0.44 | -0.44 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 12, C 3. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01705]] | B | LINC01705 activity raises CFAP20DC's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 3.08× lower at baseline in the lines without LINC01705 | 0.032 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[RFX8]] | B | RFX8 activity raises CFAP20DC's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.70× lower at baseline in the lines without RFX8 | 0.048 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[RAC2]] | B | RAC2 activity raises CFAP20DC's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 2.30× lower at baseline in the lines without RAC2 | 0.050 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[DTNA]] | B | DTNA activity raises CFAP20DC's level | lines that do not express DTNA (22) vs lines expressing it (28) | 3.73× lower at baseline in the lines without DTNA | 0.053 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553 |
| [[MANCR]] | B | MANCR activity raises CFAP20DC's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without MANCR | 0.061 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[RNF217]] | B | RNF217 activity raises CFAP20DC's level | lines that do not express RNF217 (9) vs lines expressing it (41) | 3.62× lower at baseline in the lines without RNF217 | 0.068 | ⚠ within organs, on part of the lines; also absent: RNF217-AS1, LRP12, BEX3 |
| [[ADAM19]] | B | ADAM19 activity raises CFAP20DC's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.22× lower at baseline in the lines without ADAM19 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[SEMA7A]] | B | SEMA7A activity raises CFAP20DC's level | lines that do not express SEMA7A (13) vs lines expressing it (37) | 2.26× lower at baseline in the lines without SEMA7A | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ARL4C]] | B | ARL4C activity raises CFAP20DC's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 2.55× lower at baseline in the lines without ARL4C | 0.082 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |
| [[GLYATL2]] | B | GLYATL2 activity raises CFAP20DC's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 2.65× lower at baseline in the lines without GLYATL2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476 |
| [[APCDD1L]] | B | APCDD1L activity raises CFAP20DC's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.96× lower at baseline in the lines without APCDD1L | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[C3orf52]] | B | C3orf52 activity raises CFAP20DC's level | lines that do not express C3orf52 (6) vs lines expressing it (44) | 4.57× lower at baseline in the lines without C3orf52 | 0.098 | ⚠ within organs, on part of the lines; also absent: HTATIP2, TBILA, ISG20; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MANCR]] | B | CFAP20DC activity raises MANCR's level | lines that do not express CFAP20DC (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without CFAP20DC | 0.032 | ⚠ within organs, on part of the lines; also absent: RGS17, CHST11, WDR17 |
| [[C3orf52]] | B | CFAP20DC activity raises C3orf52's level | lines that do not express CFAP20DC (16) vs lines expressing it (34) | 1.81× lower at baseline in the lines without CFAP20DC | 0.060 | ⚠ within organs, on part of the lines; also absent: RGS17, CHST11, WDR17 |
| [[CFAP20DC-AS1]] | B | CFAP20DC activity raises CFAP20DC-AS1's level | lines that do not express CFAP20DC (16) vs lines expressing it (34) | 1.31× lower at baseline in the lines without CFAP20DC | 0.063 | ⚠ within organs, on part of the lines; also absent: RGS17, CHST11, WDR17 |
| cells under [[NVP-BHG712 (drug)]] 5 µM | B | CFAP20DC activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express CFAP20DC (16) vs lines expressing it (32) | the lines without CFAP20DC: 0.93× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: RGS17, CHST11, WDR17 |
| [[CAMK4]] | C | CFAP20DC activity raises CAMK4's level | lines that do not express CFAP20DC (16) vs lines expressing it (34) | 3.33× lower at baseline in the lines without CFAP20DC | 0.052 | ⚠ within organs, on part of the lines; also absent: RGS17, CHST11, WDR17; co-absent with the target |
| [[IGFBP3]] | C | CFAP20DC activity raises IGFBP3's level | lines that do not express CFAP20DC (16) vs lines expressing it (34) | 4.35× lower at baseline in the lines without CFAP20DC | 0.065 | ⚠ within organs, on part of the lines; also absent: RGS17, CHST11, WDR17; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.7, 10.7); signed map (15.3, 50.9). **Vector** length 113, 39.1% of its response variance represented; |z| ≥ 3 in 1,351 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.4 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.3 | -8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +3.2 | -9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +3.1 | -7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +2.9 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +0.4 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -8.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.0 | -10.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.7 | -7.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.4 | -4.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.1 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.9 | -1.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | CFAP20 domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.2 — chr3:58,717,365-59,050,084 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ42117, FLJ42930; previously C3orf67 |
| Matched by | ensembl_id |

UniProt [Q6ZVT6](https://www.uniprot.org/uniprotkb/Q6ZVT6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:24763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24763) · Entrez [200844](https://www.ncbi.nlm.nih.gov/gene/200844) · UniProt [Q6ZVT6](https://www.uniprot.org/uniprotkb/Q6ZVT6) · Ensembl [ENSG00000163689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163689)

## Data

Gene col 8755: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8755); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8755, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8755]; `tensor/DDL_lfc|DDL_z.npy` [8755]; `embed/gene_vectors.npy` [8755]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8755 or target_col == 8755). Every well: [[CFAP20DC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP20DC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
