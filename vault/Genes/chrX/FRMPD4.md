---
symbol: "FRMPD4"
type: "gene"
col: 9878
ensembl_id: "ENSG00000169933"
name: "FERM and PDZ domain containing 4"
location: "Xp22.2"
module: 19
arm: "+"
pooled_cpm: 22.38
n_lines_expressing: 26
n_dd_up: 23
n_dd_down: 22
n_dd_up_clean: 19
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 39
direction_downstream: 32
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# FRMPD4

*FERM and PDZ domain containing 4* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.96× (z +13.5, q 1e-38, up in 16 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.554× (z -8.4, q 3e-14, down in 20 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01435]] (+0.67, fdr 1e-05), [[MSR1]] (+0.65, fdr 1e-05), [[LINC02476]] (+0.64, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 39 arrows point to it, the strongest [[ABCA13]] → it (grade B ⚠); 32 go from it, the strongest it → [[MCC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9878.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +13.5 | 1e-38 | 16/24 (SW480, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +13.4 | 2e-38 | 8/23 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +9.8 | 3e-20 | 14/23 (SW480, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +7.6 | 4e-12 | 3/22 (A549, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +7.2 | 1e-10 | 12/23 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +7.0 | 3e-10 | 8/23 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.8 | 5e-07 | 9/24 (SW480, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +5.1 | 3e-05 | 1/20 (SW1417) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +4.8 | 1e-04 | 11/23 (A-172, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +4.6 | 2e-04 | 8/23 (A-172, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +4.5 | 3e-04 | 4/23 (H4, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.4 | 6e-04 | 5/22 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.3 | 8e-04 | 2/19 (SW1417, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.9 | 0.004 | 8/22 (H4, SW480, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.010 | 9/23 (H4, RPMI-7951, …) | rises with dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.18× | +3.3 | 0.029 | 6/24 (A-172, A498, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.034 | 0/24 | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.050 | 4/24 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9878.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.554×** | -8.4 | 3e-14 | 20/24 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -8.2 | 8e-14 | 20/22 (SW1417, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.663×** | -5.8 | 1e-06 | 17/22 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.707×** | -4.9 | 1e-04 | 21/23 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.708×** | -4.9 | 1e-04 | 17/24 (SNU-423, J82, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.704×** | -4.4 | 0.001 | 9/22 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.739×** | -4.3 | 0.002 | 9/23 (SNU-423, A498, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.746×** | -4.2 | 0.002 | 10/24 (SNU-423, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.754×** | -4.0 | 0.004 | 6/24 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.762×** | -3.9 | 0.006 | 5/22 (J82, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.762×** | -3.9 | 0.006 | 11/22 (SNU-423, A-172, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.829×** | -3.8 | 0.008 | 8/24 (SNU-423, A498, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.605×** | -3.7 | 0.008 | 11/23 (SK-MEL-2, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.770×** | -3.7 | 0.008 | 10/24 (SNU-423, SHP-77, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.754×** | -3.7 | 0.008 | 4/24 (SHP-77, HEC-1-A, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.752×** | -3.6 | 0.012 | 14/23 (SNU-423, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9878. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 367 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -15.8) |
| [[A-172 (line)]] | wt | 40.0 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +20.8) | [[Dinaciclib (drug)]] 5 µM 0.108× (z -12.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 49.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0799× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.238× (z -8.7) |
| [[SW1417 (line)]] | alt | 10.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.93× (z +15.6) | [[Digitoxin (drug)]] 5 µM 0.0599× (z -13.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 43.8 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +12.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 40.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.7) |
| [[SW480 (line)]] | alt | 8.29 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 5.37× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 23.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -10.2) |
| [[HS-578T (line)]] | alt | 28.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 25.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0928× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 64.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.196× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~82% of this change |
| [[SK-MEL-2 (line)]] | alt | 84.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -9.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.53 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9878), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01435]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[MSR1]] | +0.65 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[LINC02476]] | +0.64 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[BMPER]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[TRIM55]] | +0.63 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[NCKAP5]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[LSAMP]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SLC14A2]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ANGPTL2]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CNTN6]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[LDB2]] | +0.60 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CASC15]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 4, C 35. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA13]] | B | ABCA13 activity raises FRMPD4's level | lines that do not express ABCA13 (19) vs lines expressing it (31) | 2.56× lower at baseline in the lines without ABCA13 | 0.024 | ⚠ within organs, on part of the lines; also absent: SHC4, MIR3681HG, LINC02930; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FRMPD4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NR3C1]] | B | NR3C1 activity lowers FRMPD4's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[LINC00504]] | B | LINC00504 activity raises FRMPD4's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 2.48× lower at baseline in the lines without LINC00504 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474 |
| [[TRPM8]] | C | TRPM8 activity raises FRMPD4's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 3.09× lower at baseline in the lines without TRPM8 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent; co-absent with the target |
| [[LINC01885]] | C | LINC01885 activity raises FRMPD4's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 3.51× lower at baseline in the lines without LINC01885 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383; co-absent with the target |
| [[CPED1]] | C | CPED1 activity raises FRMPD4's level | lines that do not express CPED1 (24) vs lines expressing it (26) | 3.15× lower at baseline in the lines without CPED1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CCNYL2, LINC01885, ENSG00000291032; maybe low, not absent; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises FRMPD4's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 4.97× lower at baseline in the lines without KCNE4 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[TEX41]] | C | TEX41 activity raises FRMPD4's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 3.33× lower at baseline in the lines without TEX41 | 0.024 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12; co-absent with the target |
| [[ADAM12]] | C | ADAM12 activity raises FRMPD4's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 4.30× lower at baseline in the lines without ADAM12 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[LINC02930]] | C | LINC02930 activity raises FRMPD4's level | lines that do not express LINC02930 (33) vs lines expressing it (17) | 3.74× lower at baseline in the lines without LINC02930 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000232053, GYPC, PLPP4; co-absent with the target |
| [[CACNA2D3]] | C | CACNA2D3 activity raises FRMPD4's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 3.09× lower at baseline in the lines without CACNA2D3 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824; co-absent with the target |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 9, C 23. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCC]] | B | FRMPD4 activity raises MCC's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 2.88× lower at baseline in the lines without FRMPD4 | 0.008 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[KCNIP4]] | B | FRMPD4 activity raises KCNIP4's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 1.98× lower at baseline in the lines without FRMPD4 | 0.017 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[FAM13C]] | B | FRMPD4 activity raises FAM13C's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 2.10× lower at baseline in the lines without FRMPD4 | 0.024 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[BACH1]] | B | FRMPD4 activity raises BACH1's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 1.77× lower at baseline in the lines without FRMPD4 | 0.046 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[OFCC1]] | B | FRMPD4 activity raises OFCC1's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 2.39× lower at baseline in the lines without FRMPD4 | 0.052 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[LINC01828]] | B | FRMPD4 activity raises LINC01828's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 2.52× lower at baseline in the lines without FRMPD4 | 0.054 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[AGBL1]] | B | FRMPD4 activity raises AGBL1's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 1.80× lower at baseline in the lines without FRMPD4 | 0.060 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[PLXNA4]] | B | FRMPD4 activity raises PLXNA4's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without FRMPD4 | 0.066 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[BMPER]] | B | FRMPD4 activity raises BMPER's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 3.05× lower at baseline in the lines without FRMPD4 | 0.0997 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[SETBP1]] | C | FRMPD4 activity raises SETBP1's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 4.68× lower at baseline in the lines without FRMPD4 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3; co-absent with the target |
| [[LCP1]] | C | FRMPD4 activity raises LCP1's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 3.14× lower at baseline in the lines without FRMPD4 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3; co-absent with the target |
| [[NTF3]] | C | FRMPD4 activity raises NTF3's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 3.43× lower at baseline in the lines without FRMPD4 | 0.013 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.467). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.2, 26.3); signed map (39.0, 28.2). **Vector** length 80.7, 24.2% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.3 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.6 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.9 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +13.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +5.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.0 | +1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +3.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.2 | -2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.1 | -4.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.0 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -4.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | FERM and PDZ domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:11,822,423-12,724,523 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Preso1, Preso, KIAA0316; previously PDZK10, PDZD10 |
| Gene groups (HGNC) | PDZ domain containing; FERM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14CM0](https://www.uniprot.org/uniprotkb/Q14CM0) (FERM and PDZ domain-containing protein 4):

> Positive regulator of dendritic spine morphogenesis and density. Required for the maintenance of excitatory synaptic transmission. Binds phosphatidylinositol 4,5-bisphosphate.

**Summary**, from NCBI Gene [9758](https://www.ncbi.nlm.nih.gov/gene/9758):

> This gene encodes a multi-domain (WW, PDZ, FERM) containing protein. Through its interaction with other proteins (such as PSD-95), it functions as a positive regulator of dendritic spine morphogenesis and density, and is required for the maintenance of excitatory synaptic transmission. [provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:29007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29007) · Entrez [9758](https://www.ncbi.nlm.nih.gov/gene/9758) · UniProt [Q14CM0](https://www.uniprot.org/uniprotkb/Q14CM0) · Ensembl [ENSG00000169933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169933)

## Data

Gene col 9878: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9878); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9878, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9878]; `tensor/DDL_lfc|DDL_z.npy` [9878]; `embed/gene_vectors.npy` [9878]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9878 or target_col == 9878). Every well: [[FRMPD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRMPD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
