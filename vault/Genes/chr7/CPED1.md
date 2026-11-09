---
symbol: "CPED1"
type: "gene"
col: 2712
ensembl_id: "ENSG00000106034"
name: "cadherin like and PC-esterase domain containing 1"
location: "7q31.31"
module: 19
arm: "+"
pooled_cpm: 35.79
n_lines_expressing: 26
n_dd_up: 36
n_dd_down: 2
n_dd_up_clean: 27
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CPED1

*cadherin like and PC-esterase domain containing 1* — 7q31.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.82× (z +40.0, q 0e+00, up in 21 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.753× (z -4.4, q 0.007, down in 10 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SNU-1 0.382×, CHP-212 0.217×, NCI-H460 0.367×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.170×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.159×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.337×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (CHP-212 0.155×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02241]] (+0.70, fdr 7e-06), [[ABCC9]] (+0.67, fdr 7e-06), [[FSTL5]] (+0.63, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EPHA5]] → it (grade C ⚠); 9 go from it, the strongest it → [[LINC01885]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2712.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.82×** | +40.0 | 0e+00 | 21/24 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.53×** | +21.1 | 0e+00 | 20/24 (C-33 A, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.71×** | +21.0 | 0e+00 | 18/24 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +19.8 | 0e+00 | 13/24 (HepG2/C3A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.80×** | +15.9 | 0e+00 | 18/24 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +14.4 | 8e-45 | 9/21 (A-172, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.32×** | +13.5 | 1e-39 | 16/23 (A-172, HS-578T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.13×** | +12.1 | 6e-32 | 19/23 (C-33 A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +10.3 | 4e-23 | 10/19 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +9.7 | 1e-20 | 11/24 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +8.6 | 5e-16 | 7/19 (Panc 03.27, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +8.1 | 3e-14 | 14/24 (HS-578T, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +7.1 | 4e-11 | 10/24 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +6.5 | 3e-09 | 10/24 (C32, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +6.3 | 1e-08 | 11/24 (C32, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.02×** | +5.9 | 1e-07 | 11/25 (NCI-H1792, RPMI-7951, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.4 | 2e-06 | 8/24 (A-172, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.4 | 2e-06 | 6/23 (C32, HS-578T, …) | top dose only | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2712.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SNU-1 0.382×, CHP-212 0.217×, NCI-H460 0.367×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.170×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.159×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.337×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (CHP-212 0.155×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.753×** | -4.4 | 0.007 | 10/22 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.798×** | -3.6 | 0.082 | 11/24 (NCI-H460, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.806× | -3.4 | 0.11 | 7/22 (H4, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 22.5 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +22.2) | — |
| [[C32 (line)]] | wt | 271 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +13.2) | — |
| [[HS-578T (line)]] | alt | 26.4 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +20.6) | — |
| [[SNU-1 (line)]] | wt | 1,172 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -12.7) |
| [[CHP-212 (line)]] | wt | 321 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 71.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.93× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 35.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.72× (z +15.3) | — |
| [[SK-MEL-2 (line)]] | alt | 75.5 | 4 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.49× (z +10.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.88× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 59.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +19.7) | — |
| [[KATO III (line)]] | alt | 20.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 79.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -10.0) |
| [[SNU-423 (line)]] | alt | 27.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +21.8) | — |
| [[A498 (line)]] | wt | 65.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +15.8) | — |
| [[LOX-IMVI (line)]] | wt | 34.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +14.9) | — |
| [[NCI-H1792 (line)]] | alt | 44.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +17.6) | — |
| [[A-427 (line)]] | wt | 20.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.10× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 14.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.2× (z +12.4) | — |
| [[A549 (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.77 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.04 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.40 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.27 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.94 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.26 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.77 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.99 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02241]] | +0.70 | +0.72 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[ABCC9]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[FSTL5]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[PDE1A]] | +0.62 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[CDH11]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[DNAH11]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ALPK2]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[CAVIN2-AS1]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[RIMS1]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[NLGN4Y]] | +0.60 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[ITGBL1]] | +0.60 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[LINC02945]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA5]] | C | EPHA5 activity raises CPED1's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 2.49× lower at baseline in the lines without EPHA5 | 0.034 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[PCDH18]] | C | PCDH18 activity raises CPED1's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 2.75× lower at baseline in the lines without PCDH18 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |
| [[COL4A6]] | C | COL4A6 activity raises CPED1's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 1.84× lower at baseline in the lines without COL4A6 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |
| [[PYDC2-AS1]] | C | PYDC2-AS1 activity raises CPED1's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 3.55× lower at baseline in the lines without PYDC2-AS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2; co-absent with the target |
| [[NR1H4]] | C | NR1H4 activity raises CPED1's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 2.45× lower at baseline in the lines without NR1H4 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01885]] | C | CPED1 activity raises LINC01885's level | lines that do not express CPED1 (24) vs lines expressing it (26) | 4.04× lower at baseline in the lines without CPED1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CCNYL2, LINC01885, ENSG00000291032; maybe low, not absent; co-absent with the target |
| [[FRMPD4]] | C | CPED1 activity raises FRMPD4's level | lines that do not express CPED1 (24) vs lines expressing it (26) | 3.15× lower at baseline in the lines without CPED1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CCNYL2, LINC01885, ENSG00000291032; maybe low, not absent; co-absent with the target |
| [[MSR1]] | C | CPED1 activity raises MSR1's level | lines that do not express CPED1 (24) vs lines expressing it (26) | 3.77× lower at baseline in the lines without CPED1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CCNYL2, LINC01885, ENSG00000291032; maybe low, not absent; co-absent with the target |
| [[LINC02241]] | C | CPED1 activity raises LINC02241's level | lines that do not express CPED1 (24) vs lines expressing it (26) | 3.03× lower at baseline in the lines without CPED1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CCNYL2, LINC01885, ENSG00000291032; maybe low, not absent; co-absent with the target |
| [[SERPINB2]] | C | CPED1 activity raises SERPINB2's level | lines that do not express CPED1 (24) vs lines expressing it (26) | 2.66× lower at baseline in the lines without CPED1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CCNYL2, LINC01885, ENSG00000291032; maybe low, not absent; co-absent with the target |
| [[TENM1]] | C | CPED1 activity raises TENM1's level | lines that do not express CPED1 (24) vs lines expressing it (26) | 3.63× lower at baseline in the lines without CPED1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CCNYL2, LINC01885, ENSG00000291032; maybe low, not absent; co-absent with the target |
| [[KCNK2]] | C | CPED1 activity raises KCNK2's level | lines that do not express CPED1 (24) vs lines expressing it (26) | 1.94× lower at baseline in the lines without CPED1 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CCNYL2, LINC01885, ENSG00000291032; maybe low, not absent; co-absent with the target |
| [[BAGE2]] | C | CPED1 activity raises BAGE2's level | lines that do not express CPED1 (24) vs lines expressing it (26) | 2.97× lower at baseline in the lines without CPED1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CCNYL2, LINC01885, ENSG00000291032; maybe low, not absent; co-absent with the target |
| [[HECW2]] | C | CPED1 activity raises HECW2's level | lines that do not express CPED1 (24) vs lines expressing it (26) | 2.94× lower at baseline in the lines without CPED1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CCNYL2, LINC01885, ENSG00000291032; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.0, 26.3); signed map (41.3, 27.3). **Vector** length 80.7, 20.9% of its response variance represented; |z| ≥ 3 in 814 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +21.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +40.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +13.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +1.5 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.2 | -4.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cadherin like and PC-esterase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.31 — chr7:120,988,697-121,297,442 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21986; previously C7orf58 |
| Matched by | ensembl_id |

UniProt [A4D0V7](https://www.uniprot.org/uniprotkb/A4D0V7) carries no function annotation.

**Summary**, from NCBI Gene [79974](https://www.ncbi.nlm.nih.gov/gene/79974):

> Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26159](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26159) · Entrez [79974](https://www.ncbi.nlm.nih.gov/gene/79974) · UniProt [A4D0V7](https://www.uniprot.org/uniprotkb/A4D0V7) · Ensembl [ENSG00000106034](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106034)

## Data

Gene col 2712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2712); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2712]; `tensor/DDL_lfc|DDL_z.npy` [2712]; `embed/gene_vectors.npy` [2712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2712 or target_col == 2712). Every well: [[CPED1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPED1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
