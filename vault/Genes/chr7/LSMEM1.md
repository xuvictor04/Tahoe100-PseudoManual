---
symbol: "LSMEM1"
type: "gene"
col: 11156
ensembl_id: "ENSG00000181016"
name: "leucine rich single-pass membrane protein 1"
location: "7q31.1"
module: 37
arm: "+"
pooled_cpm: 7.94
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 30
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# LSMEM1

*leucine rich single-pass membrane protein 1* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.90× (z +21.0, q 0e+00, up in 43 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Naproxen (drug)]] 0.05 µM in 2 lines (LS 180 0.0746×, NCI-H23 0.0781×); [[Busulfan (drug)]] 0.05 µM in 1 line (Hs 766T 0.0660×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HT-29 0.117×; ⚠ toxic; transcription drop); [[Decitabine (drug)]] 0.05 µM in 1 line (LS 180 0.0822×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASS4]] (+0.79, fdr 8e-06), [[LINC00880]] (+0.78, fdr 7e-06), [[LINC02955]] (+0.78, fdr 7e-06); moves opposite to [[BRD7]] (-0.66, fdr 1e-05), [[TRIM35]] (-0.63, fdr 3e-05), [[TECPR1]] (-0.62, fdr 2e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11156.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.90×** | +21.0 | 0e+00 | 43/44 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **7.53×** | +13.7 | 2e-40 | 46/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.14×** | +13.6 | 4e-40 | 44/44 (PANC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.06×** | +12.2 | 3e-32 | 39/42 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.22×** | +9.8 | 2e-20 | 39/46 (C32, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **4.14×** | +9.3 | 2e-18 | 38/45 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **3.94×** | +9.0 | 1e-17 | 43/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.76×** | +9.0 | 2e-17 | 38/41 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **3.78×** | +8.8 | 1e-16 | 43/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.17×** | +7.4 | 6e-12 | 34/48 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +6.5 | 5e-09 | 32/40 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +6.0 | 7e-08 | 28/42 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +5.3 | 6e-06 | 24/36 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **2.13×** | +5.1 | 1e-05 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.8 | 5e-05 | 22/47 (PANC-1, SW1417, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.03×** | +4.8 | 6e-05 | 26/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +4.4 | 4e-04 | 23/47 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11156.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Naproxen (drug)]] 0.05 µM in 2 lines (LS 180 0.0746×, NCI-H23 0.0781×); [[Busulfan (drug)]] 0.05 µM in 1 line (Hs 766T 0.0660×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HT-29 0.117×; ⚠ toxic; transcription drop); [[Decitabine (drug)]] 0.05 µM in 1 line (LS 180 0.0822×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbamazepine (drug)]] 5 µM |  | 0.593× | -3.6 | 0.14 | 20/47 (SNU-423, HT-29, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.603× | -3.5 | 0.14 | 18/47 (SW 900, SW480, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.503× | -3.4 | 0.14 | 16/46 (SW 900, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 0.05 µM |  | 0.603× | -3.3 | 0.15 | 15/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.614× | -3.2 | 0.18 | 14/47 (HEC-1-A, NCI-H23, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.643× | -3.0 | 0.23 | 14/47 (SK-MEL-2, SHP-77, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11156. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.50 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +16.2) | — |
| [[C32 (line)]] | wt | 16.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.0× (z +16.3) | — |
| [[SW480 (line)]] | alt | 8.64 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.96× (z +13.0) | — |
| [[LoVo (line)]] | wt | 9.21 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +13.8) | — |
| [[LS 180 (line)]] | wt | 8.85 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.91× (z +8.7) | [[Naproxen (drug)]] 0.05 µM 0.0746× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 5.42 | 3 | 0 | [[Selinexor (drug)]] 5 µM 7.08× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 5.19 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +12.5) | — |
| [[SW 900 (line)]] | alt | 8.32 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +9.4) | — |
| [[A498 (line)]] | wt | 8.55 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +16.7) | — |
| [[A549 (line)]] | wt | 4.88 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.99× (z +10.5) | [[Gemfibrozil (drug)]] 0.5 µM 0.0816× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 5.57 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +12.5) | — |
| [[HEC-1-A (line)]] | alt | 7.89 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.23× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 19.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -8.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 11.4 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 10.3× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 8.63 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.95× (z +11.5) | [[Naproxen (drug)]] 0.05 µM 0.0781× (z -8.8) |
| [[PANC-1 (line)]] | alt | 5.78 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.21× (z +12.7) | — |
| [[SK-MEL-2 (line)]] | alt | 6.64 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +12.4) | — |
| [[SW1417 (line)]] | alt | 17.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +12.6) | — |
| [[A-172 (line)]] | wt | 4.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 5.28 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.5 µM 0.0620× (z -8.7) |
| [[COLO 205 (line)]] | alt | 5.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.1× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 4.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 5.87 | 0 | 1 | — | [[Busulfan (drug)]] 0.05 µM 0.0660× (z -8.9) |
| [[HS-578T (line)]] | alt | 5.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 9.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +11.3) | — |
| [[J82 (line)]] | alt | 3.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 5.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 8.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 9.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 5.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 7.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.88× (z +9.7) | — |
| [[A-427 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11156), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASS4]] | +0.79 | +0.77 / +0.58 | both halves | 8e-06 |  |
| [[LINC00880]] | +0.78 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.78 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.75 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[SNX31]] | +0.74 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[PXDNL]] | +0.73 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[LRP2BP]] | +0.73 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[MGAM]] | +0.72 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[STPG4]] | +0.72 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[LINC01004]] | +0.71 | +0.69 / +0.34 | both halves | 1e-04 |  |
| [[ADCY10]] | +0.71 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[GIPC2]] | +0.71 | +0.60 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRD7]] | -0.66 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TRIM35]] | -0.63 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TECPR1]] | -0.62 | -0.46 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LSMEM1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.5, -13.9); signed map (20.0, 2.3). **Vector** length 79.3, 18.1% of its response variance represented; |z| ≥ 3 in 1,416 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.0 | +9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +13.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.2 | +7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +0.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | +1.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.6 | +3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +3.3 |
|  | [[Lonafarnib (drug)]] 0.05 µM |  | -1.9 | -3.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.9 | -3.5 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -1.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich single-pass membrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:112,480,853-112,491,062 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39575; previously C7orf53 |
| Matched by | ensembl_id |

UniProt [Q8N8F7](https://www.uniprot.org/uniprotkb/Q8N8F7) carries no function annotation.

**Summary**, from NCBI Gene [286006](https://www.ncbi.nlm.nih.gov/gene/286006):

> Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22036) · Entrez [286006](https://www.ncbi.nlm.nih.gov/gene/286006) · UniProt [Q8N8F7](https://www.uniprot.org/uniprotkb/Q8N8F7) · Ensembl [ENSG00000181016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181016)

## Data

Gene col 11156: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11156); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11156, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11156]; `tensor/DDL_lfc|DDL_z.npy` [11156]; `embed/gene_vectors.npy` [11156]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11156 or target_col == 11156). Every well: [[LSMEM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSMEM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
