---
symbol: "FTSJ3"
type: "gene"
col: 2974
ensembl_id: "ENSG00000108592"
name: "FtsJ RNA 2'-O-methyltransferase 3"
location: "17q23.3"
module: 7
arm: "+"
pooled_cpm: 32.29
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# FTSJ3

*FtsJ RNA 2'-O-methyltransferase 3* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.73× (z +14.4, q 3e-44, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.12× (z +12.0, q 1e-30, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.0943×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (SW 900 0.236×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LSG1]] (+0.67, fdr 1e-05), [[CCDC137]] (+0.67, fdr 7e-06), [[BRMS1]] (+0.65, fdr 1e-05); moves opposite to [[SLC25A40]] (-0.56, fdr 3e-05), [[LCORL]] (-0.53, fdr 3e-04), [[ZNF706]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2974.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.73×** | +14.4 | 3e-44 | 48/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +12.0 | 1e-30 | 48/48 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.30×** | +11.9 | 2e-30 | 46/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.91×** | +9.3 | 3e-18 | 44/47 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.86×** | +8.5 | 2e-15 | 41/48 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +8.3 | 1e-14 | 40/47 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +8.1 | 6e-14 | 41/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.66×** | +7.2 | 3e-11 | 35/45 (SNU-423, A498, …) | two highest doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +7.1 | 7e-11 | 38/47 (HOP62, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +7.1 | 9e-11 | 36/47 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.53×** | +6.8 | 5e-10 | 33/47 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.63×** | +6.8 | 7e-10 | 38/48 (SW480, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +6.6 | 2e-09 | 38/48 (HOP62, HT-29, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.60×** | +6.5 | 4e-09 | 32/47 (SW480, HEC-1-A, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +5.8 | 2e-07 | 29/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.4 | 2e-06 | 30/48 (CFPAC-1, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +5.1 | 1e-05 | 31/48 (KATO III, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 8e-04 | 27/48 (HS-578T, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.003 | 23/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.017 | 18/47 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.020 | 19/47 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.47×** | +2.9 | 0.077 | 14/47 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2974.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.0943×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (SW 900 0.236×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | 0.764× | -3.7 | 0.10 | 20/47 (HOP62, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.784× | -3.5 | 0.12 | 20/48 (CHP-212, HOP62, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.806× | -3.1 | 0.34 | 6/48 (NCI-H1792, HS-578T, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.812× | -3.0 | 0.34 | 11/48 (H4, RKO, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 26.6 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.21× (z +10.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.8) | — |
| [[SW480 (line)]] | alt | 38.1 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.01× (z +13.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.5) | — |
| [[A549 (line)]] | wt | 24.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 41.1 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +10.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 21.9 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.83× (z +9.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +8.8) | — |
| [[KATO III (line)]] | alt | 43.9 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +8.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 29.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.52× (z +9.1) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2347 (line)]] | alt | 29.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +8.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H460 (line)]] | wt | 25.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.4) | — |
| [[A-172 (line)]] | wt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.27× (z +8.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[LoVo (line)]] | wt | 27.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +9.4) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.93× (z +8.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1792 (line)]] | alt | 27.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.79× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | — |
| [[SW 900 (line)]] | alt | 22.2 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.236× (z -8.5) |
| [[SW48 (line)]] | wt | 41.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0943× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[A-427 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSG1]] | +0.67 | +0.68 / +0.54 | both halves | 1e-05 | STRING 971 |
| [[CCDC137]] | +0.67 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[BRMS1]] | +0.65 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[DNTTIP2]] | +0.65 | +0.70 / +0.60 | both halves | 7e-06 | STRING 704 |
| [[TSSC4]] | +0.64 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[POP4]] | +0.63 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[ZC3H18]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[FLAD1]] | +0.62 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[GRWD1]] | +0.62 | +0.62 / +0.57 | both halves | 9e-06 | STRING 849 |
| [[TACO1]] | +0.62 | +0.73 / +0.46 | both halves | 3e-05 |  |
| [[EMG1]] | +0.61 | +0.65 / +0.51 | both halves | 1e-05 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 721 |
| [[MOCS3]] | +0.61 | +0.69 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A40]] | -0.56 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[LCORL]] | -0.53 | -0.73 / -0.28 | both halves | 3e-04 |  |
| [[ZNF706]] | -0.52 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FTSJ3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-42.3, 1.3); signed map (-4.6, -23.8). **Vector** length 79.4, 19.2% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.3 | +7.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.4 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.4 | -3.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.3 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | FtsJ RNA 2'-O-methyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:63,819,433-63,830,012 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPB1 |
| Gene groups (HGNC) | Armadillo like helical domain containing; 7BS 2'O-ribose DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY81](https://www.uniprot.org/uniprotkb/Q8IY81) (pre-rRNA 2'-O-ribose RNA methyltransferase FTSJ3):

> RNA 2'-O-methyltransferase involved in the processing of the 34S pre-rRNA to 18S rRNA and in 40S ribosomal subunit formation.; (Microbial infection) In case of infection by HIV-1 virus, recruited to HIV-1 RNA and catalyzes 2'-O-methylation of the viral genome, allowing HIV-1 virus to escape the innate immune system. RNA 2'-O-methylation provides a molecular signature for discrimination of self from non-self and is used by HIV-1 to evade innate immune recognition by IFIH1/MDA5. Mediates …

**Summary**, from NCBI Gene [117246](https://www.ncbi.nlm.nih.gov/gene/117246):

> Although the function of this gene is not known, the existence of this gene is supported by mRNA and EST data. A possible function of the encoded protein can be inferred from amino acid sequence similarity to the E.coli FtsJ protein and to a mouse protein possibly involved in embryogenesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17136](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17136) · Entrez [117246](https://www.ncbi.nlm.nih.gov/gene/117246) · UniProt [Q8IY81](https://www.uniprot.org/uniprotkb/Q8IY81) · Ensembl [ENSG00000108592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108592)

## Data

Gene col 2974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2974); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2974]; `tensor/DDL_lfc|DDL_z.npy` [2974]; `embed/gene_vectors.npy` [2974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2974 or target_col == 2974). Every well: [[FTSJ3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FTSJ3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
