---
symbol: "LTB4R"
type: "gene"
col: 13145
ensembl_id: "ENSG00000213903"
name: "leukotriene B4 receptor"
location: "14q12"
module: 15
arm: "+"
pooled_cpm: 13.84
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# LTB4R

*leukotriene B4 receptor* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.79× (z +18.3, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.731× (z -13.7, q 4e-40, down in 45 of 47 measured lines) ⚠ position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 4 lines (MIA PaCa-2 0.639×, A-172 0.643×, SW480 0.731×, NCI-H23 0.699×; ⚠ position not correctable); [[Docetaxel (drug)]] 0.05 µM in 2 lines (J82 0.109×, HS-578T 0.132×; ⚠ transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 0.255×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RABL2A]] (+0.56, fdr 1e-05), [[WDR20]] (+0.55, fdr 2e-04), [[GLUD1P3]] (+0.53, fdr 1e-04); moves opposite to [[C12orf29]] (-0.49, fdr 0.002, ⚠ one half only (not replicated)), [[COMMD8]] (-0.49, fdr 3e-04), [[RPAP3]] (-0.49, fdr 4e-04), [[ZNF639]] (-0.48, fdr 6e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13145.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +18.3 | 0e+00 | 43/45 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.47×** | +11.4 | 1e-27 | 46/47 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.21×** | +10.0 | 4e-21 | 41/46 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.19×** | +9.9 | 9e-21 | 42/46 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +7.9 | 4e-13 | 34/46 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +7.1 | 9e-11 | 26/41 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +6.3 | 3e-08 | 26/47 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.60×** | +5.9 | 2e-07 | 22/37 (A-172, HEC-1-A, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.54×** | +5.2 | 1e-05 | 14/25 (LoVo, HEC-1-A, …) | all doses, flat | composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.0 | 3e-05 | 25/47 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.45×** | +4.3 | 9e-04 | 14/32 (HT-29, SW1417, …) | all doses, flat | composition shift; position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 1e-03 | 17/42 (KATO III, SW 900, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.006 | 20/47 (hTERT-HPNE, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.013 | 9/46 (H4, SW480, …) | top dose only | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.4 | 0.025 | 9/46 (NCI-H23, SW480, …) | top dose only | position effect removed |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.029 | 11/43 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.037 | 6/46 (A498, SW48, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.041 | 6/45 (NCI-H23, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.19× | +3.2 | 0.044 | 12/47 (CFPAC-1, A498, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.047 | 12/46 (HEC-1-A, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13145.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 4 lines (MIA PaCa-2 0.639×, A-172 0.643×, SW480 0.731×, NCI-H23 0.699×; ⚠ position not correctable); [[Docetaxel (drug)]] 0.05 µM in 2 lines (J82 0.109×, HS-578T 0.132×; ⚠ transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 0.255×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.731×** | -13.7 | 4e-40 | 45/47 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.683×** | -4.8 | 5e-04 | 21/40 (J82, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Cysteamine (hydrochloride) (drug)]] 0.5 µM |  | 0.763× | -3.4 | 0.13 | 14/46 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13145. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 7.93 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +9.9) | [[Docetaxel (drug)]] 0.05 µM 0.109× (z -11.0) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 16.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[MIA PaCa-2 (line)]] | alt | 29.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.72× (z +9.2) | [[Adagrasib (drug)]] 0.05 µM 0.639× (z -11.1) ⚠ position not correctable |
| [[SW480 (line)]] | alt | 19.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +13.3) | — |
| [[A-172 (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.643× (z -10.4) ⚠ position not correctable |
| [[BT-474 (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.89× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +11.7) | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.132× (z -9.5) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 8.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 13.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +9.2) | — |
| [[A-427 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13145), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABL2A]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[WDR20]] | +0.55 | +0.29 / +0.52 | both halves | 2e-04 |  |
| [[GLUD1P3]] | +0.53 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[FAAP20]] | +0.53 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[SENP5]] | +0.53 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[GOLGA8B]] | +0.53 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[KIAA2026]] | +0.53 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[CHIC2]] | +0.52 | +0.36 / +0.46 | both halves | 9e-05 |  |
| [[DNAJC4]] | +0.51 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[NFATC2IP-AS1]] | +0.51 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[OTUD5]] | +0.51 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[SOS2]] | +0.50 | +0.30 / +0.55 | both halves | 2e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf29]] | -0.49 | -0.12 / -0.52 | ⚠ one half (not replicated) | 0.002 |  |
| [[COMMD8]] | -0.49 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[RPAP3]] | -0.49 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[ZNF639]] | -0.48 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[SSX2IP]] | -0.48 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[DGAT2]] | -0.47 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[KBTBD6]] | -0.47 | -0.24 / -0.36 | both halves | 5e-04 |  |
| [[DLD]] | -0.46 | -0.24 / -0.59 | both halves | 5e-04 |  |
| [[ZFP1]] | -0.46 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[ZNF260]] | -0.46 | -0.20 / -0.61 | both halves | 7e-04 |  |
| [[SLC25A30]] | -0.46 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[LGALSL]] | -0.45 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[SOGA3]] | -0.45 | -0.27 / -0.45 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LTB4R's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.2, 23.0); signed map (3.9, 1.2). **Vector** length 63.4, 10.2% of its response variance represented; |z| ≥ 3 in 806 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +18.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +2.6 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +7.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +5.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.4 | +0.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.4 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +0.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | leukotriene B4 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,311,450-24,318,036 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BLTR, P2Y7, LTB4R1; previously P2RY7, GPR16, CMKRL1 |
| Gene groups (HGNC) | Leukotriene receptors |
| Reactome | 6 pathways, smallest: Eicosanoid ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15722](https://www.uniprot.org/uniprotkb/Q15722) (Leukotriene B4 receptor 1):

> Receptor for extracellular ATP > UTP and ADP. The activity of this receptor is mediated by G proteins which activate a phosphatidylinositol-calcium second messenger system. May be the cardiac P2Y receptor involved in the regulation of cardiac muscle contraction through modulation of L-type calcium currents. Is a receptor for leukotriene B4, a potent chemoattractant involved in inflammation and immune response.

**Summary**, from NCBI Gene [1241](https://www.ncbi.nlm.nih.gov/gene/1241):

> Predicted to enable G protein-coupled peptide receptor activity and leukotriene B4 receptor activity. Predicted to be involved in neuropeptide signaling pathway. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6713) · Entrez [1241](https://www.ncbi.nlm.nih.gov/gene/1241) · UniProt [Q15722](https://www.uniprot.org/uniprotkb/Q15722) · Ensembl [ENSG00000213903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213903)

## Data

Gene col 13145: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13145); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13145, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13145]; `tensor/DDL_lfc|DDL_z.npy` [13145]; `embed/gene_vectors.npy` [13145]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13145 or target_col == 13145). Every well: [[LTB4R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LTB4R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
