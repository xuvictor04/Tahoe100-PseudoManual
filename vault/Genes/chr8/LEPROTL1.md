---
symbol: "LEPROTL1"
type: "gene"
col: 2479
ensembl_id: "ENSG00000104660"
name: "leptin receptor overlapping transcript like 1"
location: "8p12"
module: 183
arm: "+"
pooled_cpm: 41.35
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# LEPROTL1

*leptin receptor overlapping transcript like 1* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.94× (z +9.1, q 4e-17, up in 37 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.697× (z -9.2, q 3e-17, down in 29 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AN3 CA 0.0806×, RKO 0.243×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 0.526×, NCI-H2030 0.572×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.195×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[LJI308 (drug)]] 0.05 µM in 1 line (AN3 CA 0.112×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JKAMP]] (+0.62, fdr 7e-06), [[MOB4]] (+0.61, fdr 1e-05), [[PIGB]] (+0.60, fdr 1e-05); moves opposite to [[NEMP1]] (-0.49, fdr 6e-05), [[RELL1]] (-0.49, fdr 4e-05), [[SRGAP2]] (-0.47, fdr 9e-05).
> It is in [[Module 183]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Celecoxib (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2479.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +9.1 | 4e-17 | 37/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +8.1 | 9e-14 | 32/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +8.1 | 9e-14 | 32/47 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +7.7 | 2e-12 | 31/48 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +7.4 | 1e-11 | 28/46 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +6.6 | 3e-09 | 22/48 (Panc 03.27, KATO III, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +6.0 | 1e-07 | 25/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +5.1 | 3e-05 | 22/48 (HOP62, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | 1.19× | +4.6 | 3e-04 | 19/47 (hTERT-HPNE, HOP62, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.2 | 0.002 | 16/43 (HS-578T, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.011 | 12/48 (HOP62, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +3.7 | 0.011 | 11/48 (J82, HCT15, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | 1.16× | +3.6 | 0.012 | 19/45 (A-427, RKO, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.013 | 12/48 (H4, SNU-1, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.13× | +3.3 | 0.035 | 14/46 (SW480, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2479.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AN3 CA 0.0806×, RKO 0.243×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 0.526×, NCI-H2030 0.572×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.195×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[LJI308 (drug)]] 0.05 µM in 1 line (AN3 CA 0.112×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -9.2 | 3e-17 | 29/46 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -6.7 | 5e-09 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -6.5 | 2e-08 | 25/49 (SNU-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -4.7 | 3e-04 | 20/48 (SW480, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.876× | -3.5 | 0.053 | 16/48 (KATO III, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2479. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 62.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0806× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[LJI308 (drug)]] 0.05 µM 0.112× (z -12.3) |
| [[A-427 (line)]] | wt | 48.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 49.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | — |
| [[NCI-H2030 (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 45.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[A-172 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 72.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 55.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2479), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JKAMP]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MOB4]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PIGB]] | +0.60 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ALKBH8]] | +0.59 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[CDC40]] | +0.58 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[NDUFAF5]] | +0.57 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.57 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[ZFP64]] | +0.57 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[NRDE2]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[PSMC1]] | +0.56 | +0.60 / +0.43 | both halves | 4e-05 |  |
| [[IRAK1BP1]] | +0.56 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[ZNF383]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEMP1]] | -0.49 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[RELL1]] | -0.49 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[SRGAP2]] | -0.47 | -0.37 / -0.45 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises LEPROTL1's level | compounds that target TOP2A: 2 of 5 lower it (Doxorubicin, Epirubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers LEPROTL1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Celecoxib (drug)]] 0.05 µM | C | LEPROTL1's natural level raises the cells' numbers under Celecoxib 0.05 µM (protects the cells) | LEPROTL1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.317 over the table, 0.095 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.5, -0.9); signed map (-21.4, -20.7). **Vector** length 77.2, 13.8% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.9 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.5 | +7.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.2 | +7.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +3.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -9.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -6.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | leptin receptor overlapping transcript like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:30,095,408-30,177,208 (+) |
| Ensembl biotype | protein_coding |
| Also known as | my047, Vps55 |
| Matched by | ensembl_id |

**Function**, from UniProt [O95214](https://www.uniprot.org/uniprotkb/O95214) (Leptin receptor overlapping transcript-like 1):

> Negatively regulates growth hormone (GH) receptor cell surface expression in liver. May play a role in liver resistance to GH during periods of reduced nutrient availability.

**Summary**, from NCBI Gene [23484](https://www.ncbi.nlm.nih.gov/gene/23484):

> Enables identical protein binding activity. Predicted to be involved in late endosome to vacuole transport via multivesicular body sorting pathway and negative regulation of growth hormone receptor signaling pathway. Predicted to be located in membrane. Predicted to be active in endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:6555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6555) · Entrez [23484](https://www.ncbi.nlm.nih.gov/gene/23484) · UniProt [O95214](https://www.uniprot.org/uniprotkb/O95214) · Ensembl [ENSG00000104660](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104660)

## Data

Gene col 2479: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2479); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2479, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2479]; `tensor/DDL_lfc|DDL_z.npy` [2479]; `embed/gene_vectors.npy` [2479]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2479 or target_col == 2479). Every well: [[LEPROTL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LEPROTL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
