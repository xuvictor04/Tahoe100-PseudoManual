---
symbol: "FAM222A"
type: "gene"
col: 6308
ensembl_id: "ENSG00000139438"
name: "family with sequence similarity 222 member A"
location: "12q24.11"
module: 93
arm: "+"
pooled_cpm: 11.05
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# FAM222A

*family with sequence similarity 222 member A* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.64× (z +19.1, q 0e+00, up in 43 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.140×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0885×; ⚠ toxic; cell-cycle shift, explains ~48% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 900 0.0700×); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (NCI-H2030 0.0772×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TENT5C]] (+0.82, fdr 7e-06), [[FOSB]] (+0.78, fdr 7e-06), [[FOS]] (+0.70, fdr 7e-06); moves opposite to [[NDUFAF5]] (-0.54, fdr 4e-05), [[AAGAB]] (-0.54, fdr 4e-05), [[PGS1]] (-0.53, fdr 1e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PRKCG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.64×** | +19.1 | 0e+00 | 43/44 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **13.0×** | +17.0 | 0e+00 | 47/47 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **7.18×** | +13.1 | 7e-37 | 47/47 (PANC-1, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **6.22×** | +11.7 | 2e-29 | 41/45 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **9.62×** | +10.5 | 8e-24 | 46/47 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.08×** | +9.3 | 8e-19 | 32/42 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.59×** | +8.9 | 3e-17 | 37/45 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.72×** | +6.3 | 2e-08 | 33/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.54×** | +6.2 | 4e-08 | 32/47 (NCI-H460, LoVo, …) | inconsistent across doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.48×** | +5.8 | 4e-07 | 27/36 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **2.29×** | +5.5 | 2e-06 | 34/47 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +5.2 | 9e-06 | 29/48 (HepG2/C3A, A-427, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.82×** | +3.8 | 0.005 | 15/37 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +3.8 | 0.005 | 21/46 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.010 | 20/47 (J82, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +3.4 | 0.026 | 20/47 (NCI-H460, SW48, …) | top dose only |  |
| [[Artemether (drug)]] 0.05 µM |  | **1.69×** | +3.3 | 0.029 | 13/47 (SW480, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.64×** | +3.3 | 0.029 | 19/47 (SW480, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.029 | 14/48 (J82, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6308.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.140×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0885×; ⚠ toxic; cell-cycle shift, explains ~48% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 900 0.0700×); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (NCI-H2030 0.0772×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Benproperine (phosphate) (drug)]] 5 µM |  | 0.599× | -3.3 | 0.28 | 21/47 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.592× | -3.2 | 0.28 | 19/47 (CFPAC-1, HS-578T, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.602× | -3.2 | 0.28 | 18/47 (SW48, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.632× | -3.0 | 0.33 | 19/46 (NCI-H1573, SK-MEL-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.88 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.05 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +15.0) | — |
| [[PANC-1 (line)]] | alt | 8.34 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 24.5× (z +15.2) | — |
| [[A498 (line)]] | wt | 5.42 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.1× (z +17.0) | — |
| [[A549 (line)]] | wt | 6.81 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 43.1× (z +12.1) | — |
| [[NCI-H2030 (line)]] | alt | 9.21 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 26.3× (z +11.2) | [[Vortioxetine (drug)]] 5 µM 0.0773× (z -8.8) ⚠ toxic · without an alert: [[Benproperine (phosphate) (drug)]] 5 µM 0.0772× (z -8.5) |
| [[SW480 (line)]] | alt | 15.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.67× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 14.3 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 20.7× (z +14.6) | — |
| [[J82 (line)]] | alt | 10.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +11.2) | — |
| [[LoVo (line)]] | wt | 25.8 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 14.2× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 14.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +15.0) | — |
| [[SNU-423 (line)]] | alt | 5.07 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +11.9) | — |
| [[A-172 (line)]] | wt | 3.06 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 5.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +13.6) | — |
| [[HEC-1-A (line)]] | alt | 6.70 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.28× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 4.04 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 15.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +10.0) | — |
| [[KATO III (line)]] | alt | 10.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 12.9× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 6.92 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 7.10 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.92× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 6.42 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 29.5× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 13.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +9.4) | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0700× (z -8.9) |
| [[SW1417 (line)]] | alt | 29.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 8.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +13.2) | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +15.7) | — |
| [[COLO 205 (line)]] | alt | 4.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.6× (z +10.5) | — |
| [[HepG2_C3A (line)]] | wt | 35.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0885× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~48% of this change |
| [[HOP62 (line)]] | alt | 7.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +14.4) | — |
| [[Hs 766T (line)]] | wt | 3.22 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 27.5× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 4.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.6× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.05 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 21.5× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 9.32 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 26.8× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 9.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 8.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +9.2) | — |
| [[RKO (line)]] | wt | 11.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 12.4× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TENT5C]] | +0.82 | +0.82 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[FOSB]] | +0.78 | +0.78 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[FOS]] | +0.70 | +0.71 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[IQCN]] | +0.70 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[TEX14]] | +0.68 | +0.82 / +0.65 | both halves | 7e-06 |  |
| [[PRKCG]] | +0.66 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[WDR47]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[LRRC23]] | +0.65 | +0.74 / +0.58 | both halves | 8e-06 |  |
| [[FAM53C]] | +0.65 | +0.73 / +0.58 | both halves | 8e-06 |  |
| [[KLHL15]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[FGF18]] | +0.64 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.64 | +0.71 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF5]] | -0.54 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[AAGAB]] | -0.54 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[PGS1]] | -0.53 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[CCNY-AS1]] | -0.53 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[TRMT61B]] | -0.52 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[PSMF1]] | -0.52 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[C8orf76]] | -0.52 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[PMS2P1]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[NIPSNAP3A]] | -0.51 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[GTPBP10]] | -0.49 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[FAM86HP]] | -0.49 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[NAPB]] | -0.49 | -0.56 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKCG]] | B | PRKCG activity raises FAM222A's level | lines that do not express PRKCG (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without PRKCG | 0.052 | ⚠ within organs, on part of the lines; also absent: SLC36A4, DBN1, CEP41; maybe low, not absent |
| [[VASN]] | B | VASN activity raises FAM222A's level | lines that do not express VASN (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without VASN | 0.075 | ⚠ within organs, on part of the lines; also absent: PAQR7, DBN1, C5AR1; maybe low, not absent |
| [[HAP1]] | B | HAP1 activity raises FAM222A's level | lines that do not express HAP1 (12) vs lines expressing it (38) | 1.59× lower at baseline in the lines without HAP1 | 0.092 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.843). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.6, -27.5); signed map (2.9, 17.9). **Vector** length 94.7, 24.7% of its response variance represented; |z| ≥ 3 in 1,271 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +19.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.8 | +2.3 |
|  | [[Artemether (drug)]] 0.05 µM |  | +2.7 | +3.3 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +0.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -1.1 |
|  | [[Carbamazepine (drug)]] 0.5 µM |  | -3.0 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.6 | -0.3 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 222 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:109,713,825-109,770,495 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14721; previously C12orf34 |
| Matched by | ensembl_id |

UniProt [Q5U5X8](https://www.uniprot.org/uniprotkb/Q5U5X8) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25915](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25915) · Entrez [84915](https://www.ncbi.nlm.nih.gov/gene/84915) · UniProt [Q5U5X8](https://www.uniprot.org/uniprotkb/Q5U5X8) · Ensembl [ENSG00000139438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139438)

## Data

Gene col 6308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6308); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6308]; `tensor/DDL_lfc|DDL_z.npy` [6308]; `embed/gene_vectors.npy` [6308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6308 or target_col == 6308). Every well: [[FAM222A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM222A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
