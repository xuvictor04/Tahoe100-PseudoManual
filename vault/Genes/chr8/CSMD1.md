---
symbol: "CSMD1"
type: "gene"
col: 11372
ensembl_id: "ENSG00000183117"
name: "CUB and Sushi multiple domains 1"
location: "8p23.2"
module: 140
arm: "+"
pooled_cpm: 9.39
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# CSMD1

*CUB and Sushi multiple domains 1* — 8p23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.66× (z +26.0, q 0e+00, up in 33 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.170×); [[Allantoin (drug)]] 0.05 µM in 1 line (AsPC-1 0.0681×; ⚠ transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (HS-578T 0.230×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.213×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTN5]] (+0.80, fdr 7e-06), [[SLC27A6]] (+0.77, fdr 7e-06), [[SYNM-AS1]] (+0.75, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11372.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.66×** | +26.0 | 0e+00 | 33/40 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.85×** | +21.5 | 0e+00 | 10/12 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.41×** | +21.0 | 0e+00 | 23/29 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +16.0 | 0e+00 | 32/40 (SK-MEL-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.01×** | +14.4 | 6e-45 | 8/16 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.79×** | +8.0 | 2e-13 | 23/45 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.9 | 4e-10 | 15/45 (C32, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.8 | 4e-07 | 10/40 (COLO 205, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.4 | 4e-06 | 9/37 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.6 | 3e-04 | 8/25 (A549, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +4.5 | 3e-04 | 12/45 (HCT15, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.3 | 9e-04 | 9/48 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.0 | 0.003 | 0/14 | top dose only | noisy plate (z scaled) |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.010 | 5/41 (Hs 766T, RKO, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.011 | 7/39 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.011 | 10/38 (LOX-IMVI, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.031 | 3/37 (HT-29, HCT15, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.045 | 7/47 (HS-578T, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.51×** | +3.1 | 0.063 | 3/43 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.069 | 1/44 (NCI-H2030) | inconsistent across doses | position effect removed |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.23×** | +2.9 | 0.089 | 0/46 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11372.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.170×); [[Allantoin (drug)]] 0.05 µM in 1 line (AsPC-1 0.0681×; ⚠ transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (HS-578T 0.230×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.213×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -4.1 | 0.023 | 11/48 (NCI-H1792, COLO 205, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.860× | -3.1 | 0.60 | 7/45 (SK-MEL-2, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11372. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 96.0 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 3.13 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +12.6) | — |
| [[A498 (line)]] | wt | 2.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.99× (z +10.4) | — |
| [[A549 (line)]] | wt | 2.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.26× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 3.74 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0681× (z -9.2) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 5.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.96× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 3.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.73× (z +9.7) | — |
| [[LoVo (line)]] | wt | 3.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.45× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 3.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +8.8) | — |
| [[A-172 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11372), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTN5]] | +0.80 | +0.65 / +0.83 | both halves | 7e-06 | STRING 480 |
| [[SLC27A6]] | +0.77 | +0.61 / +0.78 | both halves | 7e-06 |  |
| [[SYNM-AS1]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.75 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.74 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[USH2A]] | +0.74 | +0.70 / +0.72 | both halves | 7e-06 | STRING 438 |
| [[LINC00861]] | +0.74 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[G2E3-AS1]] | +0.73 | +0.57 / +0.72 | both halves | 9e-06 |  |
| [[TTN]] | +0.73 | +0.62 / +0.76 | both halves | 7e-06 | STRING 454 |
| [[PKD2L2]] | +0.73 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.72 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[LRRC4C]] | +0.72 | +0.64 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CSMD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GABRA3]] | B | GABRA3 activity raises CSMD1's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 2.32× lower at baseline in the lines without GABRA3 | 0.046 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4 |
| [[SLCO1C1]] | C | SLCO1C1 activity lowers CSMD1's level | lines that do not express SLCO1C1 (4) vs lines expressing it (46) | 1.90× higher at baseline in the lines without SLCO1C1 | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GNA14; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.782). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.7, 28.4); signed map (33.2, 12.2). **Vector** length 56.4, 7.61% of its response variance represented; |z| ≥ 3 in 851 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +26.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.8 | +21.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.4 | +21.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +14.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +16.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -4.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | CUB and Sushi multiple domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.2 — chr8:2,935,353-4,994,972 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1890, PPP1R24 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Sushi domain containing; Complement system regulators and receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PZ7](https://www.uniprot.org/uniprotkb/Q96PZ7) (CUB and sushi domain-containing protein 1):

> Potential suppressor of squamous cell carcinomas.

**Summary**, from NCBI Gene [64478](https://www.ncbi.nlm.nih.gov/gene/64478):

> Predicted to act upstream of or within several processes, including learning or memory; mammary gland branching involved in pregnancy; and reproductive structure development. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14026](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14026) · Entrez [64478](https://www.ncbi.nlm.nih.gov/gene/64478) · UniProt [Q96PZ7](https://www.uniprot.org/uniprotkb/Q96PZ7) · Ensembl [ENSG00000183117](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183117)

## Data

Gene col 11372: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11372); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11372, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11372]; `tensor/DDL_lfc|DDL_z.npy` [11372]; `embed/gene_vectors.npy` [11372]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11372 or target_col == 11372). Every well: [[CSMD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSMD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
