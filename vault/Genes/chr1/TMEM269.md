---
symbol: "TMEM269"
type: "gene"
col: 15817
ensembl_id: "ENSG00000274386"
name: "transmembrane protein 269"
location: "1p34.2"
module: 37
arm: "+"
pooled_cpm: 5.51
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# TMEM269

*transmembrane protein 269* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.17× (z +21.2, q 0e+00, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.474× (z -4.1, q 0.021, down in 12 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.0997×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (KATO III 0.0553×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (H4 0.0473×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0713×); [[Brimonidine (drug)]] 0.5 µM in 1 line (BT-474 0.0736×); [[Pyridoxine (drug)]] 0.05 µM in 1 line (SHP-77 0.0765×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIWIL2]] (+0.79, fdr 7e-06), [[CFAP53]] (+0.79, fdr 7e-06), [[SNX31]] (+0.77, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.17×** | +21.2 | 0e+00 | 40/40 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.64×** | +19.2 | 0e+00 | 32/40 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.71×** | +13.8 | 7e-41 | 44/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.34×** | +12.2 | 6e-32 | 25/34 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.75×** | +10.6 | 3e-24 | 38/47 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.70×** | +9.4 | 4e-19 | 24/40 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +9.3 | 9e-19 | 31/39 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.61×** | +9.1 | 1e-17 | 37/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +6.2 | 3e-08 | 0/7 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **3.07×** | +6.1 | 4e-08 | 20/45 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.9 | 2e-07 | 16/31 (HT-29, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +4.8 | 9e-05 | 14/47 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +4.8 | 9e-05 | 13/46 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.7 | 1e-04 | 16/47 (A-172, SW1417, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.7 | 0.009 | 8/43 (SNU-423, HOP62, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.009 | 9/45 (LS 180, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.024 | 10/44 (SK-MEL-2, SW48, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.034 | 8/46 (LS 180, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15817.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.0997×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (KATO III 0.0553×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (H4 0.0473×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0713×); [[Brimonidine (drug)]] 0.5 µM in 1 line (BT-474 0.0736×); [[Pyridoxine (drug)]] 0.05 µM in 1 line (SHP-77 0.0765×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.474×** | -4.1 | 0.021 | 12/36 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.729× | -3.4 | 0.16 | 10/46 (SNU-1, HEC-1-A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.731× | -3.3 | 0.16 | 13/47 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.730× | -3.2 | 0.18 | 15/43 (LoVo, RPMI-7951, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.751× | -3.1 | 0.25 | 10/48 (KATO III, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.97 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.30× (z +11.2) | — |
| [[H4 (line)]] | wt | 11.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +9.0) | [[Digitoxin (drug)]] 0.5 µM 0.0473× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 2.97 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 4.39 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 6.28 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.92× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 5.68 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0762× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0713× (z -8.9) |
| [[PANC-1 (line)]] | alt | 2.20 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.62× (z +11.4) | — |
| [[SW480 (line)]] | alt | 13.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0997× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.07× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 6.81 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0736× (z -8.5) |
| [[C32 (line)]] | wt | 3.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.1× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 7.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 4.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +10.0) | — |
| [[KATO III (line)]] | alt | 6.10 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0553× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 6.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 4.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 4.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.61× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 3.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 4.79 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.05 µM 0.0765× (z -8.5) |
| [[A-427 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIWIL2]] | +0.79 | +0.86 / +0.73 | both halves | 7e-06 |  |
| [[CFAP53]] | +0.79 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[SNX31]] | +0.77 | +0.84 / +0.70 | both halves | 7e-06 |  |
| [[TEX29]] | +0.75 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[TMEM225B]] | +0.74 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.74 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[ADCY10]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[WDR49]] | +0.73 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[CASS4]] | +0.73 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[TNXB]] | +0.72 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.71 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[UBAP1L]] | +0.71 | +0.77 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMEM269's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01482]] | B | LINC01482 activity raises TMEM269's level | lines that do not express LINC01482 (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without LINC01482 | 0.074 | ⚠ within organs, on part of the lines; also absent: MAP7D2, SLC35F4, ENSG00000226965; maybe low, not absent |
| [[WDR49]] | C | WDR49 activity raises TMEM269's level | lines that do not express WDR49 (3) vs lines expressing it (47) | 2.15× lower at baseline in the lines without WDR49 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FOXP1, ENSG00000286952, CORIN; maybe low, not absent; its own permutation p |
| [[C4orf47]] | C | C4orf47 activity raises TMEM269's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 1.74× lower at baseline in the lines without C4orf47 | 0.070 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.851). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.9, -17.8); signed map (11.4, 5.1). **Vector** length 68.7, 11.5% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +21.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +19.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.7 | +9.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +6.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +3.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.5 | +3.7 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.0 | -1.5 |
|  | [[NG25 (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -1.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 269 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:42,784,991-42,816,619 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [A0A1B0GVZ9](https://www.uniprot.org/uniprotkb/A0A1B0GVZ9) carries no function annotation.

**Summary**, from NCBI Gene [100129924](https://www.ncbi.nlm.nih.gov/gene/100129924):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:52381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52381) · Entrez [100129924](https://www.ncbi.nlm.nih.gov/gene/100129924) · UniProt [A0A1B0GVZ9](https://www.uniprot.org/uniprotkb/A0A1B0GVZ9) · Ensembl [ENSG00000274386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274386)

## Data

Gene col 15817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15817); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15817]; `tensor/DDL_lfc|DDL_z.npy` [15817]; `embed/gene_vectors.npy` [15817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15817 or target_col == 15817). Every well: [[TMEM269 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM269.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
