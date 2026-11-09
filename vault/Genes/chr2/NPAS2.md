---
symbol: "NPAS2"
type: "gene"
col: 9962
ensembl_id: "ENSG00000170485"
name: "neuronal PAS domain protein 2"
location: "2q11.2"
module: 174
arm: "+"
pooled_cpm: 280.31
n_lines_expressing: 43
n_dd_up: 0
n_dd_down: 57
n_dd_up_clean: 0
n_dd_down_clean: 41
in_vector_space: true
direction_upstream: 12
direction_downstream: 29
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# NPAS2

*neuronal PAS domain protein 2* — 2q11.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 1.71×, Hs 766T 1.89×).
> Pooled over the cell lines (median), lowered significantly by 57 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.284× (z -31.6, q 0e+00, down in 37 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PITPNC1]] (+0.78, fdr 7e-06), [[HMGA2]] (+0.74, fdr 7e-06), [[ITGB5]] (+0.74, fdr 7e-06); moves opposite to [[GPRIN2]] (-0.53, fdr 1e-04), [[PALS1]] (-0.50, fdr 1e-05), [[CD24]] (-0.49, fdr 6e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[HTR7]] → it (grade B ⚠); 29 go from it, the strongest it → [[TIMP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9962.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 1.71×, Hs 766T 1.89×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.21× | +3.5 | 0.28 | 15/41 (NCI-H2030, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 67 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 57 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9962.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.284×** | -31.6 | 0e+00 | 37/41 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.185×** | -30.0 | 0e+00 | 41/41 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.240×** | -25.4 | 0e+00 | 40/41 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.259×** | -24.0 | 0e+00 | 40/41 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.332×** | -19.6 | 0e+00 | 35/41 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.334×** | -18.7 | 0e+00 | 33/41 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.511×** | -11.5 | 2e-28 | 28/37 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.556×** | -11.4 | 2e-28 | 34/43 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.528×** | -11.3 | 5e-28 | 29/42 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.610×** | -10.8 | 2e-25 | 35/41 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.537×** | -10.2 | 1e-22 | 28/38 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.589×** | -9.4 | 3e-19 | 34/42 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.592×** | -9.3 | 7e-19 | 27/41 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **0.633×** | -9.0 | 1e-17 | 32/42 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.616×** | -8.6 | 3e-16 | 34/41 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.611×** | -8.4 | 2e-15 | 32/41 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.640×** | -7.9 | 8e-14 | 28/41 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.645×** | -7.8 | 2e-13 | 26/41 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.697×** | -7.7 | 5e-13 | 30/41 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9962. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 909 | 0 | 43 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0892× (z -39.0) |
| [[C32 (line)]] | wt | 1,015 | 0 | 21 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -29.3) |
| [[HepG2_C3A (line)]] | wt | 799 | 0 | 21 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -27.6) |
| [[NCI-H1573 (line)]] | alt | 556 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0843× (z -40.9) |
| [[PANC-1 (line)]] | alt | 414 | 0 | 19 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -27.8) |
| [[SNU-1 (line)]] | wt | 654 | 0 | 19 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0583× (z -26.0) |
| [[SK-MEL-2 (line)]] | alt | 296 | 0 | 18 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -32.6) |
| [[MIA PaCa-2 (line)]] | alt | 568 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -26.0) |
| [[NCI-H1792 (line)]] | alt | 536 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -33.8) |
| [[SW 900 (line)]] | alt | 538 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -20.4) |
| [[RPMI-7951 (line)]] | alt | 653 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -25.5) |
| [[A549 (line)]] | wt | 511 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0834× (z -31.8) |
| [[SW480 (line)]] | alt | 298 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0951× (z -26.9) |
| [[AsPC-1 (line)]] | alt | 313 | 0 | 12 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -21.8) |
| [[RKO (line)]] | wt | 136 | 1 | 11 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -35.4) |
| [[CFPAC-1 (line)]] | alt | 422 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -34.8) |
| [[CHP-212 (line)]] | wt | 458 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -14.3) |
| [[hTERT-HPNE (line)]] | wt | 281 | 0 | 10 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.147× (z -18.3) |
| [[LS 180 (line)]] | wt | 236 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -25.3) |
| [[NCI-H23 (line)]] | alt | 152 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -17.9) |
| [[LoVo (line)]] | wt | 97.0 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -25.3) |
| [[NCI-H2030 (line)]] | alt | 215 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -23.4) |
| [[LOX-IMVI (line)]] | wt | 109 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -21.2) |
| [[Panc 03.27 (line)]] | alt | 123 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -19.7) |
| [[SNU-423 (line)]] | alt | 124 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -18.6) |
| [[A498 (line)]] | wt | 120 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.307× (z -14.6) |
| [[HOP62 (line)]] | alt | 150 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -20.3) |
| [[HS-578T (line)]] | alt | 152 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -23.8) |
| [[H4 (line)]] | wt | 203 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -12.2) |
| [[Hs 766T (line)]] | wt | 172 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.185× (z -15.7) |
| [[KATO III (line)]] | alt | 150 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -23.0) |
| [[BT-474 (line)]] | alt | 84.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -12.1) |
| [[C-33 A (line)]] | alt | 76.6 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.177× (z -13.2) |
| [[SW1417 (line)]] | alt | 180 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -15.3) |
| [[SW48 (line)]] | wt | 78.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.9) |
| [[COLO 205 (line)]] | alt | 224 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -12.5) |
| [[HT-29 (line)]] | alt | 72.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -9.0) |
| [[SW 1271 (line)]] | alt | 233 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -10.6) |
| [[A-172 (line)]] | wt | 51.7 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 52.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 24.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 35.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 143 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9962), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNC1]] | +0.78 | +0.79 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[HMGA2]] | +0.74 | +0.77 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ITGB5]] | +0.74 | +0.78 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[SPRY4-AS1]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.73 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[PHC2]] | +0.72 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[ST3GAL1]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.65 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[NHSL1]] | +0.65 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[PTPN12]] | +0.65 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[ETV4]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[RGS17]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRIN2]] | -0.53 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[PALS1]] | -0.50 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CD24]] | -0.49 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[CKB]] | -0.48 | -0.41 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HTR7]] | B | HTR7 activity raises NPAS2's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 2.68× lower at baseline in the lines without HTR7 | 0.011 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[ITPRIP]] | B | ITPRIP activity raises NPAS2's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 2.99× lower at baseline in the lines without ITPRIP | 0.015 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[DIO3OS]] | B | DIO3OS activity raises NPAS2's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 1.98× lower at baseline in the lines without DIO3OS | 0.021 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |
| [[ADGRE2]] | B | ADGRE2 activity raises NPAS2's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without ADGRE2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3 |
| [[EGR3]] | B | EGR3 activity raises NPAS2's level | lines that do not express EGR3 (9) vs lines expressing it (41) | 3.17× lower at baseline in the lines without EGR3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000261026 |
| [[MAP2K1]] | B | MAP2K1 activity raises NPAS2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 9.8% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ALDH3B1]] | B | ALDH3B1 activity raises NPAS2's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 1.98× lower at baseline in the lines without ALDH3B1 | 0.060 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[CEMIP]] | B | CEMIP activity raises NPAS2's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without CEMIP | 0.065 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[WWTR1]] | B | WWTR1 activity raises NPAS2's level | lines that do not express WWTR1 (7) vs lines expressing it (43) | 1.85× lower at baseline in the lines without WWTR1 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ZNF585A, LGALS1, EBI3 |
| [[BCAR3]] | B | BCAR3 activity raises NPAS2's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 1.96× lower at baseline in the lines without BCAR3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[BMERB1]] | B | BMERB1 activity raises NPAS2's level | lines that do not express BMERB1 (17) vs lines expressing it (33) | 1.95× lower at baseline in the lines without BMERB1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000259363, NRG1, NPTX1 |
| [[SPRY4-AS1]] | C | SPRY4-AS1 activity raises NPAS2's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 3.31× lower at baseline in the lines without SPRY4-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 29, C 0. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TIMP1]] | B | NPAS2 activity raises TIMP1's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 2.68× lower at baseline in the lines without NPAS2 | 0.015 | ⚠ within organs, on part of the lines |
| [[STX1A]] | B | NPAS2 activity raises STX1A's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without NPAS2 | 0.018 | ⚠ within organs, on part of the lines |
| [[ADGRE2]] | B | NPAS2 activity raises ADGRE2's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 2.58× lower at baseline in the lines without NPAS2 | 0.019 | ⚠ within organs, on part of the lines |
| [[LINC03009-1]] | B | NPAS2 activity raises LINC03009-1's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.46× lower at baseline in the lines without NPAS2 | 0.023 | ⚠ within organs, on part of the lines |
| [[BLZF2P]] | B | NPAS2 activity raises BLZF2P's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without NPAS2 | 0.024 | ⚠ within organs, on part of the lines |
| [[HTR7]] | B | NPAS2 activity raises HTR7's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 2.56× lower at baseline in the lines without NPAS2 | 0.026 | ⚠ within organs, on part of the lines |
| [[ITGB5]] | B | NPAS2 activity raises ITGB5's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.67× lower at baseline in the lines without NPAS2 | 0.029 | ⚠ within organs, on part of the lines |
| [[ITPRIP]] | B | NPAS2 activity raises ITPRIP's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 2.40× lower at baseline in the lines without NPAS2 | 0.030 | ⚠ within organs, on part of the lines |
| [[ACTN1]] | B | NPAS2 activity raises ACTN1's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without NPAS2 | 0.035 | ⚠ within organs, on part of the lines |
| [[EVA1C]] | B | NPAS2 activity raises EVA1C's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 2.46× lower at baseline in the lines without NPAS2 | 0.036 | ⚠ within organs, on part of the lines |
| [[SPRED1]] | B | NPAS2 activity raises SPRED1's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.44× lower at baseline in the lines without NPAS2 | 0.050 | ⚠ within organs, on part of the lines |
| [[SMOX]] | B | NPAS2 activity raises SMOX's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 2.60× lower at baseline in the lines without NPAS2 | 0.050 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.0, 6.3); signed map (8.4, 47.9). **Vector** length 114, 38.5% of its response variance represented; |z| ≥ 3 in 1,893 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | -7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | -4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.0 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | -5.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | -0.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -11.1 | -11.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -10.2 | -10.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -9.2 | -9.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -8.9 | -9.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -8.5 | -8.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -8.4 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | neuronal PAS domain protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:100,820,139-100,996,829 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MOP4, PASD4, bHLHe9 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; PAS domain containing |
| Reactome | 11 pathways, smallest: The CRY:PER:kinase complex represses transactivation by the BMAL:CLOCK (ARNTL:CLOCK) complex; Phosphorylated BMAL1:CLOCK (ARNTL:CLOCK) activates expression of core clock genes; BMAL1:CLOCK,NPAS2 activates circadian expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99743](https://www.uniprot.org/uniprotkb/Q99743) (Neuronal PAS domain-containing protein 2):

> Transcriptional activator which forms a core component of the circadian clock. The circadian clock, an internal time-keeping system, regulates various physiological processes through the generation of approximately 24 hour circadian rhythms in gene expression, which are translated into rhythms in metabolism and behavior. It is derived from the Latin roots 'circa' (about) and 'diem' (day) and acts as an important regulator of a wide array of physiological functions including metabolism, sleep, …

**Summary**, from NCBI Gene [4862](https://www.ncbi.nlm.nih.gov/gene/4862):

> The protein encoded by this gene is a member of the basic helix-loop-helix (bHLH)-PAS family of transcription factors. A similar mouse protein may play a regulatory role in the acquisition of specific types of memory. It also may function as a part of a molecular clock operative in the mammalian forebrain. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7895](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7895) · Entrez [4862](https://www.ncbi.nlm.nih.gov/gene/4862) · UniProt [Q99743](https://www.uniprot.org/uniprotkb/Q99743) · Ensembl [ENSG00000170485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170485)

## Data

Gene col 9962: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9962); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9962, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9962]; `tensor/DDL_lfc|DDL_z.npy` [9962]; `embed/gene_vectors.npy` [9962]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9962 or target_col == 9962). Every well: [[NPAS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPAS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
