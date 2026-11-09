---
symbol: "SLC43A2"
type: "gene"
col: 9524
ensembl_id: "ENSG00000167703"
name: "solute carrier family 43 member 2"
location: "17p13.3"
module: 94
arm: "+"
pooled_cpm: 12.5
n_lines_expressing: 47
n_dd_up: 54
n_dd_down: 0
n_dd_up_clean: 46
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# SLC43A2

*solute carrier family 43 member 2* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 54 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.29× (z +36.1, q 0e+00, up in 41 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (Panc 03.27 0.0896×, COLO 205 0.185×; ⚠ toxic; transcription drop); [[Pemigatinib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0697×); [[Pimozide (drug)]] 0.5 µM in 1 line (AN3 CA 0.131×; ⚠ transcription drop); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (NCI-H661 0.0883×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF433]] (+0.79, fdr 7e-06), [[ZNF442]] (+0.78, fdr 7e-06), [[ZNF44]] (+0.70, fdr 7e-06); moves opposite to [[GNB1L]] (-0.55, fdr 9e-05), [[AP3M2]] (-0.53, fdr 1e-04), [[SCART1]] (-0.51, fdr 1e-04).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[ZNF44]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 8 with an alert ⚠; shown: the 15 strongest. 54 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9524.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.29×** | +36.1 | 0e+00 | 41/41 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.98×** | +35.1 | 0e+00 | 40/41 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.92×** | +21.1 | 0e+00 | 39/44 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.47×** | +20.8 | 0e+00 | 35/40 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **4.12×** | +19.7 | 0e+00 | 44/44 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.21×** | +19.2 | 0e+00 | 41/43 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **3.50×** | +17.4 | 0e+00 | 43/44 (SW480, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **3.43×** | +17.1 | 0e+00 | 39/44 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +14.9 | 0e+00 | 32/39 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.69×** | +13.2 | 4e-38 | 34/42 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.85×** | +12.0 | 1e-31 | 30/45 (A-172, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.21×** | +11.0 | 2e-26 | 29/44 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.11×** | +10.4 | 1e-23 | 28/44 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.91×** | +9.0 | 1e-17 | 28/44 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +8.5 | 6e-16 | 23/44 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9524.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (Panc 03.27 0.0896×, COLO 205 0.185×; ⚠ toxic; transcription drop); [[Pemigatinib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0697×); [[Pimozide (drug)]] 0.5 µM in 1 line (AN3 CA 0.131×; ⚠ transcription drop); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (NCI-H661 0.0883×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.763× | -3.6 | 0.10 | 12/41 (Panc 03.27, COLO 205, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.776× | -3.5 | 0.10 | 11/44 (SW 900, HepG2/C3A, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.781× | -3.4 | 0.10 | 8/44 (A498, A-172, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.776× | -3.4 | 0.10 | 11/44 (SW 900, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9524. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.7 | 12 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +23.3) | — |
| [[PANC-1 (line)]] | alt | 12.9 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.87× (z +17.9) | — |
| [[A-172 (line)]] | wt | 8.73 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.67× (z +13.5) | — |
| [[HOP62 (line)]] | alt | 4.98 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +14.1) | — |
| [[KATO III (line)]] | alt | 18.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +17.5) | — |
| [[LoVo (line)]] | wt | 9.18 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +15.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 5 | 0 | [[Selinexor (drug)]] 5 µM 9.66× (z +14.5) | — |
| [[A549 (line)]] | wt | 8.54 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.2× (z +17.3) | — |
| [[Panc 03.27 (line)]] | alt | 23.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0896× (z -14.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 9.20 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +12.8) | — |
| [[C32 (line)]] | wt | 7.26 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +13.1) | — |
| [[HEC-1-A (line)]] | alt | 4.10 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +13.5) | — |
| [[HS-578T (line)]] | alt | 12.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +14.5) | — |
| [[J82 (line)]] | alt | 18.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +15.6) | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.88× (z +18.0) | — |
| [[RKO (line)]] | wt | 8.87 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.04× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 20.6 | 3 | 0 | [[Selinexor (drug)]] 5 µM 3.49× (z +10.2) | — |
| [[SW1417 (line)]] | alt | 17.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +17.8) | — |
| [[A498 (line)]] | wt | 30.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 38.3 | 0 | 2 (1 ⚠) | — | [[Pemigatinib (drug)]] 0.05 µM 0.0697× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 5.53 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +13.3) | — |
| [[BT-474 (line)]] | alt | 15.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.81× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 9.67 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +14.2) | — |
| [[HT-29 (line)]] | alt | 18.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 5.65 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.1× (z +11.4) | — |
| [[LS 180 (line)]] | wt | 3.69 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +12.1) | — |
| [[NCI-H661 (line)]] | alt | 51.9 | 0 | 2 (1 ⚠) | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0883× (z -8.9) |
| [[SNU-423 (line)]] | alt | 8.00 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.09× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 43.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +12.7) | — |
| [[SW48 (line)]] | wt | 6.75 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 16.5 | 1 | 0 | [[Selinexor (drug)]] 5 µM 4.48× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 55.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -8.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 5.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 33.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 3.69 | 1 | 0 | [[Selinexor (drug)]] 5 µM 8.74× (z +10.3) | — |
| [[SNU-1 (line)]] | wt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.30× (z +8.6) | — |
| [[A-427 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9524), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF433]] | +0.79 | +0.70 / +0.78 | both halves | 7e-06 |  |
| [[ZNF442]] | +0.78 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[ZNF44]] | +0.70 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[SDSL]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[CLN5]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[ZNF441]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[BTN2A1]] | +0.66 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[ZNF563]] | +0.66 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ZNF627]] | +0.65 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[TCEAL4]] | +0.64 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ZNF101]] | +0.64 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[DUSP15]] | +0.63 | +0.52 / +0.77 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB1L]] | -0.55 | -0.50 / -0.37 | both halves | 9e-05 |  |
| [[AP3M2]] | -0.53 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[SCART1]] | -0.51 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[TREX2]] | -0.49 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[NPHP4]] | -0.49 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[SMYD3]] | -0.49 | -0.48 / -0.18 | ⚠ not reproduced | 1e-03 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC43A2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 10.1% of all compounds | 0.022 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ZNF441]] | B | ZNF441 activity raises SLC43A2's level | lines that do not express ZNF441 (7) vs lines expressing it (43) | 2.23× lower at baseline in the lines without ZNF441 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000286098, ZNF442, ZNF433 |
| [[BATF]] | B | BATF activity raises SLC43A2's level | lines that do not express BATF (33) vs lines expressing it (17) | 1.58× lower at baseline in the lines without BATF | 0.093 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF44]] | C | SLC43A2 activity raises ZNF44's level | lines that do not express SLC43A2 (3) vs lines expressing it (47) | 4.94× lower at baseline in the lines without SLC43A2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CTDSPL, ZNF44, ITGA9-AS1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SLC2A6]] | C | SLC43A2 activity raises SLC2A6's level | lines that do not express SLC43A2 (3) vs lines expressing it (47) | 2.56× lower at baseline in the lines without SLC43A2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CTDSPL, ZNF44, ITGA9-AS1; maybe low, not absent; its own permutation p |
| [[ZNF20]] | C | SLC43A2 activity raises ZNF20's level | lines that do not express SLC43A2 (3) vs lines expressing it (47) | 2.59× lower at baseline in the lines without SLC43A2 | 0.091 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CTDSPL, ZNF44, ITGA9-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.0, 23.6); signed map (16.3, -16.9). **Vector** length 96.1, 22.8% of its response variance represented; |z| ≥ 3 in 1,338 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.8 | +21.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +9.5 | +17.1 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +7.9 | +19.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +36.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +19.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.1 | +17.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +12.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +2.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.4 | +10.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | +8.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | +11.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.7 | -1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | +7.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | +2.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | +1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 43 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,569,268-1,628,886 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC34680 |
| Gene groups (HGNC) | Solute carrier family 43 |
| Reactome | 4 pathways, smallest: Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N370](https://www.uniprot.org/uniprotkb/Q8N370) (Large neutral amino acids transporter small subunit 4):

> Uniporter that mediates the transport of the stereospecific L-phenylalanine, L-methionine and L-branched-chain amino acids, between the extracellular space and the cytoplasm and may control the transepithelial (re)absorption of neutral amino acid in kidney and small intestine. The transport activity is mediated through facilitated diffusion and is sodium ions-, chloride ions- and pH-independent Mediates the efflux of 3,3'-diiodo-L-thyronine (3,3'-T2) and 3-iodo-L-tyrosine (MIT).

**Summary**, from NCBI Gene [124935](https://www.ncbi.nlm.nih.gov/gene/124935):

> This gene encodes a member of the L-amino acid transporter-3 or SLC43 family of transporters. The encoded protein mediates sodium-, chloride-, and pH-independent transport of L-isomers of neutral amino acids, including leucine, phenylalanine, valine and methionine. This protein may contribute to the transfer of amino acids across the placental membrane to the fetus. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:23087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23087) · Entrez [124935](https://www.ncbi.nlm.nih.gov/gene/124935) · UniProt [Q8N370](https://www.uniprot.org/uniprotkb/Q8N370) · Ensembl [ENSG00000167703](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167703)

## Data

Gene col 9524: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9524); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9524, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9524]; `tensor/DDL_lfc|DDL_z.npy` [9524]; `embed/gene_vectors.npy` [9524]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9524 or target_col == 9524). Every well: [[SLC43A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC43A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
