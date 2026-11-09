---
symbol: "CCNT2-AS1"
type: "gene"
col: 13375
ensembl_id: "ENSG00000224043"
name: "CCNT2 antisense RNA 1"
location: "2q21.3"
module: 26
arm: "+"
pooled_cpm: 6.21
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# CCNT2-AS1

*CCNT2 antisense RNA 1* — 2q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 11.3× (z +49.2, q 0e+00, up in 40 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Flutamide (drug)]] 0.5 µM in 1 line (J82 0.0749×); [[Menadione (drug)]] 5 µM in 1 line (RPMI-7951 0.0828×); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.0579×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SECISBP2]] (+0.75, fdr 1e-05), [[NUP210L]] (+0.72, fdr 7e-06), [[UBE2R2-AS1]] (+0.72, fdr 1e-05); moves opposite to [[GPATCH11]] (-0.70, fdr 4e-05), [[PET117]] (-0.68, fdr 2e-05), [[MRPS31P4]] (-0.64, fdr 5e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **11.3×** | +49.2 | 0e+00 | 40/40 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.26×** | +24.0 | 0e+00 | 32/40 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.85×** | +18.6 | 0e+00 | 31/38 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.28×** | +16.4 | 0e+00 | 33/40 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.78×** | +14.7 | 0e+00 | 38/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.06×** | +14.7 | 0e+00 | 29/47 (A-172, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.50×** | +13.2 | 9e-38 | 35/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +12.4 | 2e-33 | 7/11 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.33×** | +12.1 | 4e-32 | 33/45 (HEC-1-A, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.31×** | +12.0 | 1e-31 | 24/41 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +11.6 | 2e-29 | 18/28 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +11.0 | 2e-26 | 14/17 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.94×** | +9.5 | 7e-20 | 29/45 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +8.4 | 2e-15 | 23/47 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +7.8 | 2e-13 | 18/34 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +7.7 | 5e-13 | 27/48 (SW480, SW 900, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +7.5 | 3e-12 | 20/47 (SNU-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.64×** | +7.1 | 3e-11 | 23/47 (NCI-H460, SW 900, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +7.0 | 9e-11 | 14/46 (SW480, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13375.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Flutamide (drug)]] 0.5 µM in 1 line (J82 0.0749×); [[Menadione (drug)]] 5 µM in 1 line (RPMI-7951 0.0828×); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.0579×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.839× | -3.6 | 0.17 | 12/48 (A549, SW480, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.786× | -3.4 | 0.17 | 5/44 (NCI-H23, LoVo, …) | top dose only |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 0.795× | -3.3 | 0.17 | 4/48 (SW 1088, CHP-212, …) | inconsistent across doses | position effect removed |
| [[Levobupivacaine (hydrochloride) (drug)]] 0.5 µM |  | 0.800× | -3.2 | 0.18 | 5/46 (NCI-H2030, SW48, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 4.54 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.7× (z +15.0) | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +20.8) | — |
| [[HOP62 (line)]] | alt | 7.66 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +18.7) | — |
| [[NCI-H460 (line)]] | wt | 7.24 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +21.2) | — |
| [[A-172 (line)]] | wt | 7.72 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +18.7) | — |
| [[J82 (line)]] | alt | 3.73 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +13.7) | [[Flutamide (drug)]] 0.5 µM 0.0749× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 6.18 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.9× (z +16.8) | — |
| [[RPMI-7951 (line)]] | alt | 8.00 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.2× (z +13.6) | [[Menadione (drug)]] 5 µM 0.0828× (z -8.7) |
| [[A498 (line)]] | wt | 3.33 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.3× (z +17.5) | — |
| [[HCT15 (line)]] | alt | 13.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.39× (z +10.5) | — |
| [[LoVo (line)]] | wt | 5.67 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.42× (z +14.7) | — |
| [[NCI-H2030 (line)]] | alt | 4.15 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +13.0) | — |
| [[NCI-H23 (line)]] | alt | 7.33 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +13.3) | — |
| [[SNU-423 (line)]] | alt | 4.73 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.6× (z +13.2) | — |
| [[SW480 (line)]] | alt | 13.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +17.1) | — |
| [[A549 (line)]] | wt | 4.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 4.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +12.7) | — |
| [[BT-474 (line)]] | alt | 7.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +12.8) | — |
| [[C-33 A (line)]] | alt | 9.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.23× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 9.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.87× (z +16.3) | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +14.2) | — |
| [[Hs 766T (line)]] | wt | 3.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 32.6× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 4.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.2× (z +14.1) | — |
| [[HT-29 (line)]] | alt | 5.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.20× (z +13.5) | — |
| [[hTERT-HPNE (line)]] | wt | 5.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.9× (z +11.5) | — |
| [[KATO III (line)]] | alt | 2.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.62× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 5.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.9× (z +15.5) | — |
| [[LS 180 (line)]] | wt | 4.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 3.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.95× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 4.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +12.0) | — |
| [[NCI-H2347 (line)]] | alt | 2.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 5.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.0× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 3.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.7× (z +16.9) | — |
| [[RKO (line)]] | wt | 6.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +11.9) | — |
| [[SNU-1 (line)]] | wt | 8.61 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0579× (z -8.5) |
| [[SW 900 (line)]] | alt | 8.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +13.9) | — |
| [[SW1417 (line)]] | alt | 7.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +16.1) | — |
| [[A-427 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SECISBP2]] | +0.75 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[NUP210L]] | +0.72 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[UBE2R2-AS1]] | +0.72 | +0.55 / +0.68 | both halves | 1e-05 | same gene group |
| [[LINC02955]] | +0.71 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[CPEB2-DT]] | +0.71 | +0.69 / +0.49 | both halves | 2e-05 |  |
| [[DENND6A-AS1]] | +0.70 | +0.65 / +0.61 | both halves | 7e-06 | same gene group |
| [[CCDC90B-AS1]] | +0.70 | +0.74 / +0.49 | both halves | 1e-05 | same gene group |
| [[SIAH2-AS1]] | +0.70 | +0.63 / +0.50 | both halves | 1e-05 | same gene group |
| [[SRSF5]] | +0.70 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[LINC00393]] | +0.69 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TBCE-1]] | +0.69 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[SLC25A53]] | +0.69 | +0.39 / +0.60 | both halves | 5e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH11]] | -0.70 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[PET117]] | -0.68 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[MRPS31P4]] | -0.64 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[WRAP73]] | -0.63 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[ZNF30]] | -0.63 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[MRPS34]] | -0.63 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[RSAD1]] | -0.62 | -0.60 / -0.27 | both halves | 3e-04 |  |
| [[COMMD2]] | -0.61 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[KBTBD6]] | -0.60 | -0.19 / -0.57 | ⚠ one half (not replicated) | 8e-04 |  |
| [[TAMM41]] | -0.59 | -0.50 / -0.37 | both halves | 9e-05 |  |
| [[BBS5]] | -0.59 | -0.32 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCNT2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.3, 20.1); signed map (26.2, -1.4). **Vector** length 64.9, 10.1% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +49.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +14.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +12.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +18.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +12.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +7.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +1.5 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | +3.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.1 | +8.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +0.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.5 | -0.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | CCNT2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q21.3 — chr2:134,735,464-134,918,712 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40130](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40130) · Entrez [100129961](https://www.ncbi.nlm.nih.gov/gene/100129961) · Ensembl [ENSG00000224043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224043)

## Data

Gene col 13375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13375); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13375]; `tensor/DDL_lfc|DDL_z.npy` [13375]; `embed/gene_vectors.npy` [13375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13375 or target_col == 13375). Every well: [[CCNT2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNT2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
