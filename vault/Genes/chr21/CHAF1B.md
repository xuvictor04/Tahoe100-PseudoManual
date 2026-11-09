---
symbol: "CHAF1B"
type: "gene"
col: 8238
ensembl_id: "ENSG00000159259"
name: "chromatin assembly factor 1 subunit B"
location: "21q22.12-q22.13"
module: 6
arm: "+"
pooled_cpm: 16.44
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CHAF1B

*chromatin assembly factor 1 subunit B* — 21q22.12-q22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +15.7, q 0e+00, up in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.66× (z +7.4, q 8e-12, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.750× (z -6.4, q 1e-07, down in 25 of 47 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.606× (z -4.1, q 0.008, down in 14 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A-427 0.123×, A-172 0.173×, HEC-1-A 0.369×; ⚠ cell-cycle shift, explains ~58% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.300×, HEC-1-A 0.465×; ⚠ cell-cycle shift, explains ~40% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.146×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.0956×); [[PH-797804 (drug)]] 5 µM in 1 line (A-427 0.0670×); [[TAK-901 (drug)]] 5 µM in 1 line (A-427 0.0682×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNA2]] (+0.73, fdr 7e-06), [[CDC6]] (+0.69, fdr 7e-06), [[CLSPN]] (+0.69, fdr 7e-06); moves opposite to [[CHURC1]] (-0.59, fdr 1e-05), [[XPA]] (-0.59, fdr 2e-05), [[DHFR2]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8238.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.05×** | +15.7 | 0e+00 | 39/46 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **2.17×** | +12.0 | 8e-31 | 40/48 (A498, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.89×** | +9.3 | 2e-18 | 41/48 (A498, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.84×** | +9.0 | 2e-17 | 28/42 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.76×** | +8.7 | 2e-16 | 34/47 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.76×** | +8.7 | 2e-16 | 35/47 (A498, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.73×** | +8.5 | 2e-15 | 34/47 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +7.4 | 8e-12 | 31/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.64×** | +7.4 | 1e-11 | 26/45 (HOP62, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.58×** | +7.1 | 1e-10 | 21/41 (A498, NCI-H1573, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.57×** | +6.7 | 1e-09 | 27/46 (C32, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +6.4 | 6e-09 | 24/47 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +5.1 | 1e-05 | 23/46 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.40×** | +5.0 | 2e-05 | 14/25 (A498, NCI-H2347, …) | all doses, flat | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.38×** | +5.0 | 3e-05 | 17/48 (HOP62, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.004 | 11/47 (Panc 03.27, RKO, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.019 | 11/44 (SW480, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.4 | 0.022 | 9/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.035 | 3/48 (H4, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.057 | 6/48 (MIA PaCa-2, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8238.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A-427 0.123×, A-172 0.173×, HEC-1-A 0.369×; ⚠ cell-cycle shift, explains ~58% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.300×, HEC-1-A 0.465×; ⚠ cell-cycle shift, explains ~40% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.146×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.0956×); [[PH-797804 (drug)]] 5 µM in 1 line (A-427 0.0670×); [[TAK-901 (drug)]] 5 µM in 1 line (A-427 0.0682×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.750×** | -6.4 | 1e-07 | 25/47 (A-427, HEC-1-A, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.748×** | -4.5 | 0.002 | 16/46 (A-427, A-172, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.606×** | -4.1 | 0.008 | 14/48 (A-427, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.797×** | -3.6 | 0.053 | 16/47 (AN3 CA, SK-MEL-2, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.805× | -3.3 | 0.11 | 13/46 (COLO 205, NCI-H2030, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.672× | -3.2 | 0.11 | 11/43 (A-427, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.88 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 28.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -14.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0670× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 33.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -9.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.3 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -12.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[AsPC-1 (line)]] | alt | 7.94 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.52× (z +10.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[C-33 A (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 10.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +9.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HepG2_C3A (line)]] | wt | 9.83 | 0 | 1 (1 ⚠) | — | [[Larotrectinib sulfate (drug)]] 0.5 µM 0.0848× (z -9.6) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 13.9 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +9.6) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[LoVo (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 11.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +11.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +9.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SNU-1 (line)]] | wt | 9.34 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.5 µM 0.0671× (z -9.3) |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0956× (z -11.2) |
| [[SW480 (line)]] | alt | 19.7 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.59× (z +10.9) ⚠ toxic; cell-cycle shift, explains ~53% of this change | — |
| [[A498 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNA2]] | +0.73 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[CDC6]] | +0.69 | +0.70 / +0.68 | both halves | 7e-06 | STRING 519 |
| [[CLSPN]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 | STRING 537 |
| [[MND1]] | +0.69 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[CDC45]] | +0.69 | +0.70 / +0.68 | both halves | 7e-06 | STRING 852 |
| [[FANCA]] | +0.68 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[PCLAF]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.67 | +0.68 / +0.66 | both halves | 7e-06 | STRING 459 |
| [[E2F1]] | +0.67 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[WDR76]] | +0.66 | +0.68 / +0.67 | both halves | 7e-06 | same gene group; STRING 584 |
| [[XRCC3]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[POLE]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 | STRING 611 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHURC1]] | -0.59 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[XPA]] | -0.59 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[DHFR2]] | -0.55 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[ETFRF1]] | -0.54 | -0.62 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises CHAF1B's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.58× lower at baseline in the lines without E2F2 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.0, -48.0); signed map (-37.5, -45.0). **Vector** length 102, 23.7% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.54 to 28); *DNA Replication* (reactome, mean cos +0.55 to 40); *Synthesis of DNA* (reactome, mean cos +0.55 to 37).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.9 | +8.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.2 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.1 | +15.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | +4.4 | +9.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.6 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -6.3 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.3 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -2.2 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | chromatin assembly factor 1 subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.12-q22.13 — chr21:36,385,392-36,419,015 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAF1P60, CAF-1, CAF1, CAF1A, MPP7, MPHOSPH7 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13112](https://www.uniprot.org/uniprotkb/Q13112) (Chromatin assembly factor 1 subunit B):

> Acts as a component of the histone chaperone complex chromatin assembly factor 1 (CAF-1), which assembles histone octamers onto DNA during replication and repair. CAF-1 performs the first step of the nucleosome assembly process, bringing newly synthesized histones H3 and H4 to replicating DNA; histones H2A/H2B can bind to this chromatin precursor subsequent to DNA replication to complete the histone octamer.

**Summary**, from NCBI Gene [8208](https://www.ncbi.nlm.nih.gov/gene/8208):

> Chromatin assembly factor I (CAF-I) is required for the assembly of histone octamers onto newly-replicated DNA. CAF-I is composed of three protein subunits, p50, p60, and p150. The protein encoded by this gene corresponds to the p60 subunit and is required for chromatin assembly after replication. The encoded protein is differentially phosphorylated in a cell cycle-dependent manner. In addition, it is normally found in the nucleus except during mitosis, when it is released into the cytoplasm. …

**Accessions** — [HGNC:1911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1911) · Entrez [8208](https://www.ncbi.nlm.nih.gov/gene/8208) · UniProt [Q13112](https://www.uniprot.org/uniprotkb/Q13112) · Ensembl [ENSG00000159259](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159259)

## Data

Gene col 8238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8238); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8238]; `tensor/DDL_lfc|DDL_z.npy` [8238]; `embed/gene_vectors.npy` [8238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8238 or target_col == 8238). Every well: [[CHAF1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHAF1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
