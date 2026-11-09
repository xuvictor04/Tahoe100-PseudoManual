---
symbol: "MAPRE2"
type: "gene"
col: 9398
ensembl_id: "ENSG00000166974"
name: "microtubule associated protein RP/EB family member 2"
location: "18q12.1-q12.2"
module: 44
arm: "+"
pooled_cpm: 37.75
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# MAPRE2

*microtubule associated protein RP/EB family member 2* — 18q12.1-q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.43× (z +23.6, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (CHP-212 0.0898×, LS 180 0.251×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.370×, hTERT-HPNE 0.242×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.347×; ⚠ cell-cycle shift, explains ~0% of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (H4 0.0625×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.247×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAT]] (+0.67, fdr 2e-05), [[CXADR]] (+0.67, fdr 1e-05), [[MPP1]] (+0.61, fdr 3e-05); moves opposite to [[MOSMO]] (-0.63, fdr 1e-05), [[TIMM23B-AGAP6]] (-0.61, fdr 1e-05), [[TECPR2]] (-0.60, fdr 3e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NR3C2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9398.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.43×** | +23.6 | 0e+00 | 48/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.86×** | +22.1 | 0e+00 | 48/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.12×** | +19.7 | 0e+00 | 48/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +13.2 | 1e-37 | 45/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +13.0 | 2e-36 | 39/47 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.52×** | +12.9 | 5e-36 | 46/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.11×** | +7.6 | 2e-12 | 43/49 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +7.0 | 2e-10 | 38/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +5.7 | 9e-07 | 30/48 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +5.6 | 1e-06 | 29/48 (SK-MEL-2, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +5.5 | 2e-06 | 32/48 (C32, A-172, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +5.3 | 6e-06 | 31/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.1 | 1e-05 | 26/47 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +4.3 | 6e-04 | 24/48 (NCI-H2347, A-172, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.007 | 19/48 (SK-MEL-2, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9398.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (CHP-212 0.0898×, LS 180 0.251×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.370×, hTERT-HPNE 0.242×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.347×; ⚠ cell-cycle shift, explains ~0% of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (H4 0.0625×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.247×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.777× | -3.5 | 0.19 | 19/48 (SW 1271, AsPC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.847× | -3.3 | 0.19 | 19/49 (SHP-77, CHP-212, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.796× | -3.2 | 0.19 | 20/48 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.796× | -3.2 | 0.19 | 11/47 (AN3 CA, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 54.1 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -9.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 21.8 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 13.1× (z +19.0) | — |
| [[RKO (line)]] | wt | 21.5 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 9.37× (z +13.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.225× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 50.3 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 6.16× (z +14.3) | — |
| [[A-172 (line)]] | wt | 30.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.65× (z +14.7) | — |
| [[BT-474 (line)]] | alt | 13.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 12.4× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 34.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.04× (z +16.1) | — |
| [[SK-MEL-2 (line)]] | alt | 40.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 9.37× (z +17.1) | — |
| [[SW1417 (line)]] | alt | 40.8 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.23× (z +14.1) | — |
| [[AsPC-1 (line)]] | alt | 34.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.77× (z +13.1) | — |
| [[C32 (line)]] | wt | 50.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.65× (z +13.7) | — |
| [[HEC-1-A (line)]] | alt | 39.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.76× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 20.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +12.5) | — |
| [[J82 (line)]] | alt | 37.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.05× (z +13.9) | — |
| [[NCI-H23 (line)]] | alt | 18.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.26× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.37× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 15.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.9× (z +19.2) | — |
| [[A498 (line)]] | wt | 23.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.08× (z +13.3) | — |
| [[A549 (line)]] | wt | 24.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.22× (z +14.2) | — |
| [[CFPAC-1 (line)]] | alt | 52.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.57× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 44.9 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.69× (z +9.2) | [[XRK3F2 (drug)]] 0.5 µM 0.0625× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 71.9 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.03× (z +9.9) | [[Hydroxyurea (drug)]] 0.05 µM 0.247× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 37.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.71× (z +13.3) | — |
| [[NCI-H1573 (line)]] | alt | 50.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.29× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 51.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.99× (z +16.1) | — |
| [[NCI-H2030 (line)]] | alt | 20.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.37× (z +13.8) | — |
| [[Panc 03.27 (line)]] | alt | 50.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.44× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 17.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.84× (z +11.1) | — |
| [[SW48 (line)]] | wt | 37.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.98× (z +11.6) | — |
| [[SW480 (line)]] | alt | 27.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.97× (z +12.6) | — |
| [[HCT15 (line)]] | alt | 35.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.91× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 45.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.58× (z +8.9) | — |
| [[KATO III (line)]] | alt | 69.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.60 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 14.4× (z +12.1) | — |
| [[SHP-77 (line)]] | alt | 138 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 33.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.88× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0898× (z -11.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 93.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.278× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[HS-578T (line)]] | alt | 67.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.77× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 20.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.87× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 26.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.80× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAT]] | +0.67 | +0.46 / +0.71 | both halves | 2e-05 |  |
| [[CXADR]] | +0.67 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[MPP1]] | +0.61 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[GALM]] | +0.61 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[USP2]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ATP8B1]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[KLHL32]] | +0.60 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[GDE1]] | +0.59 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[TUFT1]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[STARD5]] | +0.59 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[AMOT]] | +0.58 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[VWA5A]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOSMO]] | -0.63 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | -0.61 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TECPR2]] | -0.60 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[MLYCD]] | -0.59 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[STARD7-AS1]] | -0.59 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[MTG2]] | -0.58 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[PGS1]] | -0.58 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[DHX34]] | -0.57 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SMIM12]] | -0.57 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[PTPN9]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[FAM86HP]] | -0.56 | -0.29 / -0.39 | both halves | 2e-04 |  |
| [[GABPB1]] | -0.56 | -0.41 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C2]] | B | NR3C2 activity raises MAPRE2's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.69× lower at baseline in the lines without NR3C2 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[LNX1]] | B | LNX1 activity raises MAPRE2's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.59× lower at baseline in the lines without LNX1 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[ADD3]] | B | ADD3 activity raises MAPRE2's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 2.44× lower at baseline in the lines without ADD3 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[ONECUT2]] | B | ONECUT2 activity strengthens MAPRE2's drug response | lines that do not express ONECUT2 (10) vs lines expressing it (39) | the lines without ONECUT2 respond 0.75× as strongly (z diff +1.26); strongest at Homoharringtonine 5 µM: 1.39x vs 2.01x (z diff +2.6) | 0.039 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ATP8B1]] | B | ATP8B1 activity raises MAPRE2's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 1.34× lower at baseline in the lines without ATP8B1 | 0.047 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[PLSCR4]] | B | PLSCR4 activity raises MAPRE2's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.47× lower at baseline in the lines without PLSCR4 | 0.082 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.409). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.5, 1.1); signed map (-2.1, 18.4). **Vector** length 108, 31.0% of its response variance represented; |z| ≥ 3 in 1,211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.1 | +13.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.7 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.7 | -1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | -2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.3 | +12.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.5 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +5.5 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +3.3 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +7.6 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -5.3 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +0.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.2 | -3.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein RP/EB family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.1-q12.2 — chr18:34,976,928-35,143,470 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP1, EB1, EB2 |
| Gene groups (HGNC) | Microtubule associated protein RP/EB family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15555](https://www.uniprot.org/uniprotkb/Q15555) (Microtubule-associated protein RP/EB family member 2):

> Adapter protein that is involved in microtubule polymerization, and spindle function by stabilizing microtubules and anchoring them at centrosomes. Therefore, ensures mitotic progression and genome stability. Acts as a central regulator of microtubule reorganization in apico-basal epithelial differentiation (By similarity). Plays a role during oocyte meiosis by regulating microtubule dynamics (By similarity). Participates in neurite growth by interacting with plexin B3/PLXNB3 and microtubule …

**Summary**, from NCBI Gene [10982](https://www.ncbi.nlm.nih.gov/gene/10982):

> The protein encoded by this gene shares significant homology to the adenomatous polyposis coli (APC) protein-binding EB1 gene family. This protein is a microtubule-associated protein that is necessary for spindle symmetry during mitosis. It is thought to play a role in the tumorigenesis of colorectal cancers and the proliferative control of normal cells. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:6891](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6891) · Entrez [10982](https://www.ncbi.nlm.nih.gov/gene/10982) · UniProt [Q15555](https://www.uniprot.org/uniprotkb/Q15555) · Ensembl [ENSG00000166974](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166974)

## Data

Gene col 9398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9398); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9398]; `tensor/DDL_lfc|DDL_z.npy` [9398]; `embed/gene_vectors.npy` [9398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9398 or target_col == 9398). Every well: [[MAPRE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPRE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
