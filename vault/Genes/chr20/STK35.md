---
symbol: "STK35"
type: "gene"
col: 4671
ensembl_id: "ENSG00000125834"
name: "serine/threonine kinase 35"
location: "20p13"
module: 50
arm: "+"
pooled_cpm: 45.38
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# STK35

*serine/threonine kinase 35* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +13.2, q 7e-37, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.717× (z -5.7, q 9e-06, down in 31 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (C-33 A 0.183×, KATO III 0.370×, A549 0.361×, HT-29 0.356×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (BT-474 0.223×, SNU-423 0.357×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change); [[Bendamustine (drug)]] 5 µM in 1 line (SW 1271 0.0828×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VAMP1]] (+0.61, fdr 2e-05), [[GANAB]] (+0.58, fdr 1e-05), [[DIDO1]] (+0.58, fdr 1e-05); moves opposite to [[TIPRL]] (-0.56, fdr 1e-05), [[THOC2]] (-0.55, fdr 3e-05), [[EIF5B]] (-0.55, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4671.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +13.2 | 7e-37 | 41/48 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.70×** | +11.6 | 8e-29 | 47/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.90×** | +9.5 | 5e-19 | 43/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +7.8 | 7e-13 | 35/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +6.5 | 1e-08 | 33/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +4.6 | 3e-04 | 23/48 (A-427, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.5 | 4e-04 | 23/48 (LoVo, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.19× | +4.2 | 0.002 | 22/48 (J82, SNU-1, …) | top dose only | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.003 | 22/48 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4671.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (C-33 A 0.183×, KATO III 0.370×, A549 0.361×, HT-29 0.356×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (BT-474 0.223×, SNU-423 0.357×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change); [[Bendamustine (drug)]] 5 µM in 1 line (SW 1271 0.0828×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.717×** | -5.7 | 9e-06 | 31/49 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.755×** | -4.6 | 0.001 | 23/39 (C-33 A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | **0.806×** | -3.5 | 0.081 | 22/47 (BT-474, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 44.3 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[KATO III (line)]] | alt | 47.1 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -9.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 39.9 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.6× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 42.7 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.21× (z +12.9) | — |
| [[SW480 (line)]] | alt | 82.9 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +10.9) | — |
| [[C-33 A (line)]] | alt | 60.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -13.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 44.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 38.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +8.8) | — |
| [[RKO (line)]] | wt | 55.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.9) | — |
| [[A498 (line)]] | wt | 24.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.4) | — |
| [[A549 (line)]] | wt | 49.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -9.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 47.3 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.70× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 43.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 50.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 85.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[SW 1271 (line)]] | alt | 58.9 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0828× (z -9.6) |
| [[A-172 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4671), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAMP1]] | +0.61 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[GANAB]] | +0.58 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[DIDO1]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[GUCD1]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LDB1]] | +0.56 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ZNF263]] | +0.55 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[PLOD3]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[DDX41]] | +0.54 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[USF1]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[IFT140]] | +0.53 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[PIGS]] | +0.53 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[CRKL]] | +0.53 | +0.61 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIPRL]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[THOC2]] | -0.55 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[EIF5B]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[NEMF]] | -0.52 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[SMC6]] | -0.50 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[MRPS16]] | -0.49 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[SSB]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[CEP290]] | -0.48 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[TRMT10B]] | -0.48 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[EFR3A]] | -0.47 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[ACSL4]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[MRPL12]] | -0.47 | -0.27 / -0.51 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM | C | STK35's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | STK35's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.360 over the table, 0.048 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.8, -55.0); signed map (-23.7, 2.9). **Vector** length 84.5, 18.3% of its response variance represented; |z| ≥ 3 in 851 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +13.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +11.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.2 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +9.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.8 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | -2.8 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -1.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.8 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:2,101,827-2,177,038 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA550O8.2, CLIK1, STK35L1 |
| Gene groups (HGNC) | Serine/threonine kinase 35 family |
| Matched by | ensembl_id |

UniProt [Q8TDR2](https://www.uniprot.org/uniprotkb/Q8TDR2) carries no function annotation.

**Summary**, from NCBI Gene [140901](https://www.ncbi.nlm.nih.gov/gene/140901):

> The protein encoded by this gene is a kinase that is predominantly found in the nucleus. However, it can interact with PDLIM1/CLP-36 in the cytoplasm and localize to actin stress fibers. The encoded protein may be a regulator of actin stress fibers in nonmuscle cells. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16254](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16254) · Entrez [140901](https://www.ncbi.nlm.nih.gov/gene/140901) · UniProt [Q8TDR2](https://www.uniprot.org/uniprotkb/Q8TDR2) · Ensembl [ENSG00000125834](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125834)

## Data

Gene col 4671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4671); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4671, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4671]; `tensor/DDL_lfc|DDL_z.npy` [4671]; `embed/gene_vectors.npy` [4671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4671 or target_col == 4671). Every well: [[STK35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
