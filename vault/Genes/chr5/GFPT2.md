---
symbol: "GFPT2"
type: "gene"
col: 5210
ensembl_id: "ENSG00000131459"
name: "glutamine--fructose-6-phosphate transaminase 2"
location: "5q35.3"
module: 13
arm: "+"
pooled_cpm: 67.91
n_lines_expressing: 27
n_dd_up: 11
n_dd_down: 32
n_dd_up_clean: 10
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 16
direction_downstream: 22
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# GFPT2

*glutamine--fructose-6-phosphate transaminase 2* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.71× (z +14.6, q 1e-45, up in 21 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.640× (z -9.2, q 2e-17, down in 19 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNK3]] (+0.62, fdr 1e-05), [[SERPINE1]] (+0.62, fdr 1e-05), [[MARCHF3]] (+0.57, fdr 1e-05); moves opposite to [[ATP6V0D1-DT]] (-0.48, fdr 7e-05), [[RAB11FIP2]] (-0.47, fdr 7e-05), [[PANK1]] (-0.44, fdr 7e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[ABL1]] → it (grade B ⚠); 22 go from it, the strongest it → [[CD44]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5210.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.71×** | +14.6 | 1e-45 | 21/25 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.53×** | +13.6 | 7e-40 | 21/25 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.88×** | +13.1 | 5e-37 | 21/25 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +8.2 | 2e-14 | 15/25 (SK-MEL-2, C32, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.66×** | +7.1 | 1e-10 | 18/24 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +6.5 | 7e-09 | 12/25 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +6.4 | 1e-08 | 16/25 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.44×** | +5.4 | 6e-06 | 18/24 (NCI-H460, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +4.5 | 3e-04 | 10/25 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +4.5 | 4e-04 | 10/25 (C32, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.20×** | +3.9 | 0.006 | 5/24 (C32, SW 1271, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5210.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.640×** | -9.2 | 2e-17 | 19/25 (RKO, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.611×** | -7.2 | 1e-10 | 20/25 (RKO, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.630×** | -6.8 | 2e-09 | 21/25 (RKO, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.624×** | -6.6 | 4e-09 | 20/22 (Panc 03.27, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.479×** | -5.6 | 2e-06 | 18/24 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.682×** | -5.6 | 2e-06 | 15/25 (RKO, HOP62, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.777×** | -5.2 | 1e-05 | 16/25 (RKO, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.705×** | -5.1 | 2e-05 | 18/25 (RKO, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.709×** | -5.0 | 3e-05 | 17/25 (H4, HOP62, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.703×** | -5.0 | 4e-05 | 17/23 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.788×** | -4.9 | 4e-05 | 18/25 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.731×** | -4.6 | 2e-04 | 9/24 (H4, HOP62, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.749×** | -4.2 | 0.001 | 15/25 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.751×** | -4.2 | 0.001 | 11/25 (RKO, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.743×** | -4.2 | 0.001 | 12/25 (RKO, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.759×** | -4.0 | 0.002 | 15/25 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -3.9 | 0.003 | 14/26 (RKO, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.784×** | -3.6 | 0.012 | 14/25 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.852× | -3.3 | 0.027 | 14/26 (NCI-H2347, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5210. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 212 | 0 | 27 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0412× (z -25.3) |
| [[NCI-H460 (line)]] | wt | 127 | 5 (1 ⚠) | 3 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.90× (z +12.3) | [[Selinexor (drug)]] 5 µM 0.431× (z -11.2) |
| [[A549 (line)]] | wt | 200 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.189× (z -11.0) |
| [[H4 (line)]] | wt | 169 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0923× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0943× (z -13.8) |
| [[HOP62 (line)]] | alt | 252 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.298× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 47.8 | 3 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.73× (z +13.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -8.8) |
| [[Hs 766T (line)]] | wt | 80.3 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.19× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.255× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -9.2) |
| [[SW 900 (line)]] | alt | 79.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.07× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 426 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -12.4) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 35.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +12.7) | [[Selinexor (drug)]] 5 µM 0.355× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 83.6 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.21× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.209× (z -9.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.254× (z -9.0) |
| [[A498 (line)]] | wt | 126 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.382× (z -9.6) ⚠ toxic |
| [[C32 (line)]] | wt | 20.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +15.6) | — |
| [[HS-578T (line)]] | alt | 241 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.323× (z -8.7) |
| [[SNU-423 (line)]] | alt | 192 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.313× (z -9.7) |
| [[A-172 (line)]] | wt | 118 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -10.0) |
| [[AN3 CA (line)]] | alt | 84.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0832× (z -12.0) |
| [[C-33 A (line)]] | alt | 19.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.26× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 55.7 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.284× (z -150.0) |
| [[A-427 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.63 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.31 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.48 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.61 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.43 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 74.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.25 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.49 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.43 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.88 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.04 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5210), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNK3]] | +0.62 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SERPINE1]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[MARCHF3]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TNS1]] | +0.55 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[ELL2]] | +0.55 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[APCDD1L]] | +0.55 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[APCDD1L-DT]] | +0.54 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[VAT1L]] | +0.54 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[COL5A3]] | +0.54 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[MYO10]] | +0.54 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[TIMP1]] | +0.53 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[NAV1]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V0D1-DT]] | -0.48 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[RAB11FIP2]] | -0.47 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[PANK1]] | -0.44 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[HOXB6]] | -0.44 | -0.31 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 4, C 12. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | ABL1 activity raises GFPT2's level | compounds that target ABL1: 4 of 6 lower it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 6.4% of all compounds | 0.081 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SMOX]] | B | SMOX activity raises GFPT2's level | lines that do not express SMOX (6) vs lines expressing it (44) | 3.15× lower at baseline in the lines without SMOX | 0.091 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GFPT2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers GFPT2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SERPINE1]] | C | SERPINE1 activity raises GFPT2's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 5.73× lower at baseline in the lines without SERPINE1 | 0.003 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises GFPT2's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 6.19× lower at baseline in the lines without COL5A1 | 0.006 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[SPOCD1]] | C | SPOCD1 activity raises GFPT2's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 5.19× lower at baseline in the lines without SPOCD1 | 0.013 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises GFPT2's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 8.70× lower at baseline in the lines without LINC01411 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises GFPT2's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 5.01× lower at baseline in the lines without APCDD1L | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[COL5A3]] | C | COL5A3 activity raises GFPT2's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 3.91× lower at baseline in the lines without COL5A3 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises GFPT2's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 4.93× lower at baseline in the lines without SPOCK1 | 0.063 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[SLFN11]] | C | SLFN11 activity raises GFPT2's level | lines that do not express SLFN11 (28) vs lines expressing it (22) | 3.54× lower at baseline in the lines without SLFN11 | 0.069 | ⚠ within organs, on part of the lines; also absent: IGF2BP1, INSYN2B, DPY19L2; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 13, C 9. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD44]] | B | GFPT2 activity raises CD44's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 4.19× lower at baseline in the lines without GFPT2 | 0.004 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[METRNL]] | B | GFPT2 activity raises METRNL's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 1.84× lower at baseline in the lines without GFPT2 | 0.012 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[SMOX]] | B | GFPT2 activity raises SMOX's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 2.23× lower at baseline in the lines without GFPT2 | 0.018 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[CLIC4]] | B | GFPT2 activity raises CLIC4's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 1.63× lower at baseline in the lines without GFPT2 | 0.021 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[SH2B3]] | B | GFPT2 activity raises SH2B3's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 2.26× lower at baseline in the lines without GFPT2 | 0.028 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[RAI14]] | B | GFPT2 activity raises RAI14's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 2.86× lower at baseline in the lines without GFPT2 | 0.028 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[MYO10]] | B | GFPT2 activity raises MYO10's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 1.80× lower at baseline in the lines without GFPT2 | 0.035 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[MYO9B]] | B | GFPT2 activity raises MYO9B's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without GFPT2 | 0.038 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[TIMP1]] | B | GFPT2 activity raises TIMP1's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without GFPT2 | 0.047 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[ZNF385A]] | B | GFPT2 activity raises ZNF385A's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 1.90× lower at baseline in the lines without GFPT2 | 0.076 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[HRH1]] | B | GFPT2 activity raises HRH1's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 1.84× lower at baseline in the lines without GFPT2 | 0.083 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[TGFB1]] | B | GFPT2 activity raises TGFB1's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 2.37× lower at baseline in the lines without GFPT2 | 0.089 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.1, 13.6); signed map (14.4, 37.0). **Vector** length 103, 30.5% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +13.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +6.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +14.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +13.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +5.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | -1.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.8 | -9.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.5 | -5.1 |
|  | [[NG25 (drug)]] 5 µM |  | -3.8 | -5.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -5.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.0 | -4.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.8 | -2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | glutamine--fructose-6-phosphate transaminase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:180,300,698-180,353,336 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GFAT2 |
| Gene groups (HGNC) | Glutamine--fructose-6-phosphate transaminase family |
| Hallmark sets | KRAS_SIGNALING_UP, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 4 pathways, smallest: Synthesis of UDP-N-acetyl-glucosamine; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [O94808](https://www.uniprot.org/uniprotkb/O94808) (Glutamine--fructose-6-phosphate aminotransferase):

> Rate-limiting enzyme of the hexosamine biosynthetic pathway (HBP) that catalyzes the formation of glucosamine-6-phosphate from fructose-6-phosphate and glutamine, thereby controlling the flux of glucose into this pathway. Via control of the HPB, likely regulates the availability of precursors for N- and O-linked protein glycosylation (By similarity). Exhibits feedback inhibition by UDP-N-acetylglucosamine (UDP-GlcNAc), although to a lesser extent than GFPT1.

**Summary**, from NCBI Gene [9945](https://www.ncbi.nlm.nih.gov/gene/9945):

> Enables L-glutamine:D-fructose-6-phosphate transaminase (isomerizing) activity. Involved in UDP-N-acetylglucosamine biosynthetic process and fructose 6-phosphate metabolic process. Predicted to be located in cytosol. Implicated in type 2 diabetes mellitus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4242](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4242) · Entrez [9945](https://www.ncbi.nlm.nih.gov/gene/9945) · UniProt [O94808](https://www.uniprot.org/uniprotkb/O94808) · Ensembl [ENSG00000131459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131459)

## Data

Gene col 5210: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5210); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5210, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5210]; `tensor/DDL_lfc|DDL_z.npy` [5210]; `embed/gene_vectors.npy` [5210]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5210 or target_col == 5210). Every well: [[GFPT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GFPT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
