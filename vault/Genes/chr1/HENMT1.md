---
symbol: "HENMT1"
type: "gene"
col: 8551
ensembl_id: "ENSG00000162639"
name: "HEN methyltransferase 1"
location: "1p13.3"
module: 10
arm: "+"
pooled_cpm: 2.79
n_lines_expressing: 33
n_dd_up: 9
n_dd_down: 25
n_dd_up_clean: 4
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 0
direction_downstream: 9
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# HENMT1

*HEN methyltransferase 1* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.73× (z +10.2, q 7e-22, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +5.9, q 8e-07, up in 12 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.466× (z -11.4, q 2e-27, down in 21 of 27 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.393× (z -9.9, q 1e-20, down in 22 of 30 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00466]] (+0.65, fdr 5e-05), [[AMER1]] (+0.60, fdr 5e-05), [[SMC1B]] (+0.59, fdr 5e-05); moves opposite to [[POLR2J4]] (-0.54, fdr 6e-05), [[RASA4B]] (-0.53, fdr 3e-05), [[INAFM1]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 9 go from it, the strongest it → [[UBE2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8551.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +10.2 | 7e-22 | 2/2 (J82, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +7.9 | 6e-13 | 8/11 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.9 | 8e-07 | 12/26 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.43×** | +5.4 | 8e-06 | 10/31 (NCI-H23, SW480, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +5.0 | 6e-05 | 1/2 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +4.7 | 3e-04 | 9/30 (MIA PaCa-2, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.47×** | +4.1 | 0.003 | 3/29 (NCI-H2030, Panc 03.27, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +4.1 | 0.003 | 4/31 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.39×** | +3.4 | 0.051 | 2/13 (NCI-H2030, LoVo) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.23× | +3.1 | 0.11 | 4/29 (SW480, CFPAC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8551.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.466×** | -11.4 | 2e-27 | 21/27 (PANC-1, HOP62, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.365×** | -10.6 | 5e-24 | 15/21 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.393×** | -9.9 | 1e-20 | 22/30 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.428×** | -9.0 | 5e-17 | 18/30 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.451×** | -8.4 | 5e-15 | 20/30 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.516×** | -7.0 | 3e-10 | 17/30 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.529×** | -6.7 | 1e-09 | 13/29 (PANC-1, HT-29, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.575×** | -5.9 | 3e-07 | 15/30 (PANC-1, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.572×** | -5.7 | 9e-07 | 10/30 (NCI-H23, PANC-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.576×** | -5.6 | 1e-06 | 9/18 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.610×** | -5.2 | 9e-06 | 14/29 (C-33 A, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.638×** | -4.7 | 1e-04 | 10/28 (RPMI-7951, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.472×** | -4.1 | 0.001 | 5/29 (LS 180, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.676×** | -4.1 | 0.001 | 3/30 (SK-MEL-2, A-427, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.666×** | -4.0 | 0.002 | 12/29 (LOX-IMVI, HCT15, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.774×** | -3.8 | 0.005 | 6/29 (HS-578T, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.786×** | -3.6 | 0.012 | 6/29 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.706×** | -3.5 | 0.017 | 9/28 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.728×** | -3.3 | 0.024 | 9/31 (NCI-H1792, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8551. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.79 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 21.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.95 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 10.6 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.100× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 3.64 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0720× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 4.69 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0789× (z -9.8) ⚠ transcription drop; unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 3.74 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0501× (z -8.9) |
| [[A-172 (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.205 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.233 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.258 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.224 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.230 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.283 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.240 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.241 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8551), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00466]] | +0.65 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[AMER1]] | +0.60 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[SMC1B]] | +0.59 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[FTCDNL1]] | +0.58 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[DARS2]] | +0.58 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[C1QTNF6]] | +0.57 | +0.51 / +0.31 | both halves | 2e-04 |  |
| [[SIRT5]] | +0.57 | +0.47 / +0.31 | both halves | 2e-04 |  |
| [[ZNF514]] | +0.57 | +0.52 / +0.29 | both halves | 3e-04 |  |
| [[FAIM]] | +0.57 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[TKFC]] | +0.56 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[HOTAIR]] | +0.56 | +0.46 / +0.32 | both halves | 2e-04 |  |
| [[EXO5]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2J4]] | -0.54 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[RASA4B]] | -0.53 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[INAFM1]] | -0.50 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ZNF235]] | -0.50 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[ABAT]] | -0.50 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[SIRT2]] | -0.49 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[TOM1L2]] | -0.48 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[PMM1]] | -0.48 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[UBE2B]] | -0.48 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[COPE]] | -0.47 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[PPFIA1]] | -0.47 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[POLR2J]] ⚠ | -0.46 | -0.31 / -0.29 | both halves | 2e-04 | pathway: Gene Silencing by RNA; ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2B]] | B | HENMT1 activity raises UBE2B's level | lines that do not express HENMT1 (17) vs lines expressing it (33) | 1.12× lower at baseline in the lines without HENMT1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |
| cells under [[Nimesulide (drug)]] 5 µM | B | HENMT1 activity raises the cells' numbers under Nimesulide 5 µM (protects the cells) | lines that do not express HENMT1 (17) vs lines expressing it (31) | the lines without HENMT1: 0.81× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748; cell counts less trustworthy |
| [[SLC35G1]] | B | HENMT1 activity lowers SLC35G1's level | lines that do not express HENMT1 (17) vs lines expressing it (33) | 1.30× higher at baseline in the lines without HENMT1 | 0.057 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |
| cells under [[Rutin (trihydrate) (drug)]] 0.05 µM | B | HENMT1 activity lowers the cells' numbers under Rutin (trihydrate) 0.05 µM (makes them more sensitive) | lines that do not express HENMT1 (17) vs lines expressing it (31) | the lines without HENMT1: 1.19× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |
| [[NUDT7]] | B | HENMT1 activity raises NUDT7's level | lines that do not express HENMT1 (17) vs lines expressing it (33) | 1.19× lower at baseline in the lines without HENMT1 | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |
| [[THNSL2]] | B | HENMT1 activity raises THNSL2's level | lines that do not express HENMT1 (17) vs lines expressing it (33) | 2.17× lower at baseline in the lines without HENMT1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |
| [[TOR1A]] | B | HENMT1 activity lowers TOR1A's level | lines that do not express HENMT1 (17) vs lines expressing it (33) | 1.18× higher at baseline in the lines without HENMT1 | 0.082 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |
| cells under [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM | B | HENMT1 activity raises the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.05 µM (protects the cells) | lines that do not express HENMT1 (17) vs lines expressing it (31) | the lines without HENMT1: 0.87× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |
| cells under [[Pasireotide (acetate) (drug)]] 5 µM | B | HENMT1 activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express HENMT1 (17) vs lines expressing it (31) | the lines without HENMT1: 0.91× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.446). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.5, 27.2); signed map (29.6, -30.6). **Vector** length 40.0, 5.21% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +2.9 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | +2.1 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.8 | +3.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -9.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.5 | -9.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.5 | -7.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.4 | -10.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -6.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -3.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -0.7 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | HEN methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:108,648,290-108,661,526 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30525, HEN1; previously C1orf59 |
| Gene groups (HGNC) | 7BS 2'O-ribose DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 2 pathways, smallest: PIWI-interacting RNA (piRNA) biogenesis; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T8I9](https://www.uniprot.org/uniprotkb/Q5T8I9) (Small RNA 2'-O-methyltransferase):

> Methyltransferase that adds a 2'-O-methyl group at the 3'-end of piRNAs, a class of 24 to 30 nucleotide RNAs that are generated by a Dicer-independent mechanism and are primarily derived from transposons and other repeated sequence elements. This probably protects the 3'-end of piRNAs from uridylation activity and subsequent degradation. Stabilization of piRNAs is essential for gametogenesis.

**Summary**, from NCBI Gene [113802](https://www.ncbi.nlm.nih.gov/gene/113802):

> Enables small RNA 2'-O-ribose methyltransferase activity. Involved in RNA methylation. Predicted to be located in P granule. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26400](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26400) · Entrez [113802](https://www.ncbi.nlm.nih.gov/gene/113802) · UniProt [Q5T8I9](https://www.uniprot.org/uniprotkb/Q5T8I9) · Ensembl [ENSG00000162639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162639)

## Data

Gene col 8551: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8551); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8551, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8551]; `tensor/DDL_lfc|DDL_z.npy` [8551]; `embed/gene_vectors.npy` [8551]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8551 or target_col == 8551). Every well: [[HENMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HENMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
