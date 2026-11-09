---
symbol: "NAAA"
type: "gene"
col: 6223
ensembl_id: "ENSG00000138744"
name: "N-acylethanolamine acid amidase"
location: "4q21.1"
module: 26
arm: "+"
pooled_cpm: 9.98
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# NAAA

*N-acylethanolamine acid amidase* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.09× (z +18.7, q 0e+00, up in 30 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.02× (z +16.5, q 0e+00, up in 35 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.711× (z -5.2, q 1e-04, down in 21 of 44 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POU6F1]] (+0.59, fdr 5e-05), [[PRC1-AS1]] (+0.55, fdr 3e-05), [[VSIG10]] (+0.54, fdr 3e-05); moves opposite to [[RING1]] (-0.54, fdr 8e-05), [[ZNF184]] (-0.53, fdr 4e-04), [[INIP]] (-0.52, fdr 2e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6223.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.09×** | +18.7 | 0e+00 | 30/31 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.94×** | +16.5 | 0e+00 | 15/16 (RPMI-7951, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +16.5 | 0e+00 | 35/43 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +12.2 | 7e-32 | 19/24 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.64×** | +7.5 | 6e-12 | 17/35 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.62×** | +7.4 | 2e-11 | 17/40 (HS-578T, C32, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.4 | 2e-11 | 19/46 (HOP62, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +7.1 | 6e-11 | 18/43 (C32, LS 180, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +7.1 | 6e-11 | 20/46 (NCI-H2347, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +5.2 | 1e-05 | 11/43 (HOP62, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.34×** | +4.9 | 5e-05 | 12/46 (SW480, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.8 | 6e-05 | 13/46 (A498, LS 180, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +4.6 | 2e-04 | 13/45 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.6 | 0.012 | 12/43 (BT-474, NCI-H1573, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.24×** | +3.6 | 0.014 | 8/46 (LoVo, A-172, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.021 | 12/40 (SW48, A498, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.029 | 5/47 (AsPC-1, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.036 | 7/45 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.038 | 3/45 (RKO, NCI-H23, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.045 | 3/46 (AsPC-1, SW480, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.046 | 3/46 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.051 | 5/45 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.058 | 4/44 (LoVo, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6223.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.711×** | -5.2 | 1e-04 | 21/44 (A498, SNU-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.771×** | -4.3 | 0.004 | 12/46 (PANC-1, HCT15, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.808×** | -3.5 | 0.071 | 17/45 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.811×** | -3.5 | 0.071 | 10/46 (Panc 03.27, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.801×** | -3.4 | 0.071 | 14/43 (SW48, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.816×** | -3.4 | 0.071 | 14/43 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | 0.692× | -3.2 | 0.12 | 10/46 (SW480, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Bergenin (drug)]] 0.5 µM |  | 0.832× | -3.1 | 0.16 | 9/44 (SW 1271, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6223. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 18.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.326× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 8.85 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Canagliflozin (drug)]] 5 µM 0.156× (z -8.7) |
| [[PANC-1 (line)]] | alt | 9.97 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.0) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.291× (z -9.1) |
| [[A-172 (line)]] | wt | 5.27 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0884× (z -9.0) |
| [[A549 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 12.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.243× (z -8.5) |
| [[LS 180 (line)]] | wt | 13.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +8.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 7.86 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.140× (z -9.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 9.79 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.20× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 4.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +8.9) | — |
| [[RKO (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 27.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.146× (z -9.3) |
| [[SW48 (line)]] | wt | 15.2 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0837× (z -9.5) |
| [[A-427 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6223), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POU6F1]] | +0.59 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[PRC1-AS1]] | +0.55 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[VSIG10]] | +0.54 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[C2orf88]] | +0.54 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[FAM184B]] | +0.53 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[LAMTOR5-AS1]] | +0.52 | +0.42 / +0.37 | both halves | 8e-05 |  |
| [[SARM1]] | +0.51 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[ABCC4]] | +0.51 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[NSMAF]] | +0.51 | +0.35 / +0.36 | both halves | 1e-04 |  |
| [[MRPL11]] | +0.50 | +0.35 / +0.41 | both halves | 1e-04 |  |
| [[CTTN-DT]] | +0.50 | +0.46 / +0.46 | both halves | 2e-05 |  |
| [[LAPTM4B]] | +0.50 | +0.28 / +0.59 | both halves | 3e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RING1]] | -0.54 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[ZNF184]] | -0.53 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[INIP]] | -0.52 | -0.29 / -0.37 | both halves | 2e-04 |  |
| [[GALE]] | -0.52 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[DHRS2]] | -0.48 | -0.17 / -0.36 | ⚠ not reproduced | 0.001 |  |
| [[ZMIZ2]] | -0.48 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[H3-3B]] | -0.47 | -0.15 / -0.56 | ⚠ one half (not replicated) | 0.001 |  |
| [[DNAJB5]] | -0.47 | -0.15 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[POLM]] | -0.47 | -0.18 / -0.35 | ⚠ not reproduced | 0.001 |  |
| [[ISCA2]] | -0.46 | -0.21 / -0.33 | both halves | 7e-04 |  |
| [[SNAPIN]] | -0.46 | -0.17 / -0.39 | ⚠ not reproduced | 0.001 |  |
| [[SLFN11]] | -0.45 | -0.24 / -0.31 | both halves | 5e-04 |  |
| [[POLD4]] | -0.44 | -0.30 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NAAA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.327). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-1.9, 24.9); signed map (35.4, -16.8). **Vector** length 59.5, 8.38% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +18.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.9 | +7.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.1 | +3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -1.8 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.0 | -1.2 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -1.0 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | N-acylethanolamine acid amidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:75,913,660-75,941,013 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ASAHL |
| Gene groups (HGNC) | N-arachidonoylethanolamine hydrolases |
| Reactome | 3 pathways, smallest: Neurotransmitter release cycle; Transmission across Chemical Synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02083](https://www.uniprot.org/uniprotkb/Q02083) (N-acylethanolamine-hydrolyzing acid amidase):

> Degrades bioactive fatty acid amides to their corresponding acids, with the following preference: N-palmitoylethanolamine > N-myristoylethanolamine > N-lauroylethanolamine = N-stearoylethanolamine > N-arachidonoylethanolamine > N-oleoylethanolamine. Also exhibits weak hydrolytic activity against the ceramides N-lauroylsphingosine and N-palmitoylsphingosine.

**Summary**, from NCBI Gene [27163](https://www.ncbi.nlm.nih.gov/gene/27163):

> Enables DNA-binding transcription factor binding activity and hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds, in linear amides. Involved in several processes, including N-acylethanolamine metabolic process; N-acylphosphatidylethanolamine metabolic process; and sphingosine metabolic process. Located in lysosome and membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:736) · Entrez [27163](https://www.ncbi.nlm.nih.gov/gene/27163) · UniProt [Q02083](https://www.uniprot.org/uniprotkb/Q02083) · Ensembl [ENSG00000138744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138744)

## Data

Gene col 6223: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6223); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6223, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6223]; `tensor/DDL_lfc|DDL_z.npy` [6223]; `embed/gene_vectors.npy` [6223]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6223 or target_col == 6223). Every well: [[NAAA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAAA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
