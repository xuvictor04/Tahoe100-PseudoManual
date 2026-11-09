---
symbol: "BRAP"
type: "gene"
col: 1579
ensembl_id: "ENSG00000089234"
name: "BRCA1 associated protein"
location: "12q24.12"
module: 149
arm: "+"
pooled_cpm: 47.73
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# BRAP

*BRCA1 associated protein* — 12q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +19.3, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.756× (z -9.7, q 2e-19, down in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.461×, NCI-H1792 0.406×, HS-578T 0.355×, A-172 0.414×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.220×, LS 180 0.299×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.410×, Panc 03.27 0.369×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH1]] (+0.80, fdr 7e-06), [[TTF1]] (+0.75, fdr 7e-06), [[SLC4A1AP]] (+0.73, fdr 7e-06); moves opposite to [[DPY19L1]] (-0.59, fdr 1e-05).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF419]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1579.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +19.3 | 0e+00 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +17.4 | 0e+00 | 43/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.78×** | +13.6 | 1e-39 | 41/49 (SW480, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.43×** | +11.8 | 9e-30 | 37/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +8.4 | 7e-15 | 36/48 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +7.1 | 1e-10 | 26/48 (HEC-1-A, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +7.1 | 1e-10 | 27/48 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +7.0 | 1e-10 | 30/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +6.9 | 3e-10 | 24/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +6.7 | 1e-09 | 24/47 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +5.7 | 5e-07 | 22/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +5.5 | 2e-06 | 22/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +4.7 | 1e-04 | 18/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.20×** | +4.6 | 1e-04 | 20/48 (SW480, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.6 | 1e-04 | 18/43 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.008 | 14/49 (SW480, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.015 | 8/48 (SW 900, CFPAC-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +3.4 | 0.015 | 9/48 (SW480, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1579.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.461×, NCI-H1792 0.406×, HS-578T 0.355×, A-172 0.414×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.220×, LS 180 0.299×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.410×, Panc 03.27 0.369×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.756×** | -9.7 | 2e-19 | 37/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.736×** | -7.7 | 3e-12 | 32/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.784×** | -6.0 | 3e-07 | 27/49 (NCI-H2347, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.794×** | -5.8 | 8e-07 | 23/48 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -4.2 | 0.002 | 17/48 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.840× | -4.2 | 0.002 | 20/42 (SK-MEL-2, LS 180, …) | two highest doses | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 0.865× | -3.5 | 0.037 | 12/48 (SK-MEL-2, RKO, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.879× | -3.2 | 0.083 | 6/48 (NCI-H1573, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 53.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +14.3) | — |
| [[LS 180 (line)]] | wt | 38.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 50.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.9) | — |
| [[LoVo (line)]] | wt | 48.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 52.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.9) | — |
| [[NCI-H1792 (line)]] | alt | 52.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -9.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 39.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 44.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 68.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.9) | — |
| [[NCI-H2347 (line)]] | alt | 67.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.410× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 46.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 52.1 | 0 | 2 (2 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.113× (z -10.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 44.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +10.0) | — |
| [[A549 (line)]] | wt | 43.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 34.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -9.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 39.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.2) | — |
| [[KATO III (line)]] | alt | 40.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 49.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 53.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1579), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH1]] | +0.80 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[TTF1]] | +0.75 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[SLC4A1AP]] | +0.73 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[EAPP]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[TRIM23]] | +0.70 | +0.74 / +0.65 | both halves | 7e-06 | same gene group |
| [[ANKRD49]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[TRIM4]] | +0.69 | +0.74 / +0.59 | both halves | 7e-06 | same gene group |
| [[CCDC174]] | +0.69 | +0.80 / +0.54 | both halves | 1e-05 |  |
| [[CWF19L1]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[GOSR1]] | +0.68 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[CIR1]] | +0.68 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[TTI2]] | +0.68 | +0.70 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L1]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF419]] | C | ZNF419 activity lowers BRAP's level | lines that do not express ZNF419 (4) vs lines expressing it (46) | 1.28× higher at baseline in the lines without ZNF419 | 0.045 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: UBA6-DT, ENSG00000251379, ZNF264 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.840). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.8, 4.9); signed map (-7.7, -12.0). **Vector** length 94.6, 22.0% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +17.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +13.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +19.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +11.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +5.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +5.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.8 | -9.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -6.2 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.8 | -7.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[EX229 (drug)]] 0.05 µM |  | -2.3 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | BRCA1 associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.12 — chr12:111,642,146-111,685,956 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BRAP2, RNF52, IMP |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 11 pathways, smallest: RAF activation; Negative regulation of MAPK pathway; Paradoxical activation of RAF signaling by kinase inactive BRAF |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z569](https://www.uniprot.org/uniprotkb/Q7Z569) (BRCA1-associated protein):

> Negatively regulates MAP kinase activation by limiting the formation of Raf/MEK complexes probably by inactivation of the KSR1 scaffold protein. Also acts as a Ras responsive E3 ubiquitin ligase that, on activation of Ras, is modified by auto-polyubiquitination resulting in the release of inhibition of Raf/MEK complex formation. May also act as a cytoplasmic retention protein with a role in regulating nuclear transport.

**Summary**, from NCBI Gene [8315](https://www.ncbi.nlm.nih.gov/gene/8315):

> The protein encoded by this gene was identified by its ability to bind to the nuclear localization signal of BRCA1 and other proteins. It is a cytoplasmic protein which may regulate nuclear targeting by retaining proteins with a nuclear localization signal in the cytoplasm. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1099](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1099) · Entrez [8315](https://www.ncbi.nlm.nih.gov/gene/8315) · UniProt [Q7Z569](https://www.uniprot.org/uniprotkb/Q7Z569) · Ensembl [ENSG00000089234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089234)

## Data

Gene col 1579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1579); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1579, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1579]; `tensor/DDL_lfc|DDL_z.npy` [1579]; `embed/gene_vectors.npy` [1579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1579 or target_col == 1579). Every well: [[BRAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
