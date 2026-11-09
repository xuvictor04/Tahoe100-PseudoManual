---
symbol: "KBTBD8"
type: "gene"
col: 8679
ensembl_id: "ENSG00000163376"
name: "kelch repeat and BTB domain containing 8"
location: "3p14.1"
module: 110
arm: "+"
pooled_cpm: 2.99
n_lines_expressing: 46
n_dd_up: 61
n_dd_down: 9
n_dd_up_clean: 40
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 11
direction_downstream: 2
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# KBTBD8

*kelch repeat and BTB domain containing 8* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 61 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 13.2× (z +33.3, q 0e+00, up in 33 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.627× (z -4.2, q 0.011, down in 9 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIPAL1]] (+0.71, fdr 7e-06), [[ADTRP]] (+0.69, fdr 7e-06), [[LINC01204]] (+0.68, fdr 1e-05); moves opposite to [[RCOR3]] (-0.57, fdr 3e-05), [[TNRC6A]] (-0.55, fdr 3e-05), [[SUMF2]] (-0.54, fdr 4e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[IL11]] → it (grade B ⚠); 2 go from it, the strongest it → [[ITGA2-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 61 in all, 21 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 61 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8679.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **13.2×** | +33.3 | 0e+00 | 33/33 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **9.65×** | +20.8 | 0e+00 | 39/41 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **9.62×** | +20.8 | 0e+00 | 30/30 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.92×** | +20.5 | 0e+00 | 29/30 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **8.88×** | +20.1 | 0e+00 | 35/38 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM |  | **9.01×** | +19.4 | 0e+00 | 33/34 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **7.79×** | +18.9 | 0e+00 | 40/40 (SW480, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.48×** | +13.8 | 2e-41 | 35/40 (RKO, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **4.33×** | +12.9 | 1e-36 | 8/13 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.83×** | +12.3 | 3e-33 | 32/37 (SW480, RKO, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.80×** | +12.3 | 7e-33 | 25/33 (RKO, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.70×** | +12.0 | 2e-31 | 30/39 (RKO, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.69×** | +12.0 | 2e-31 | 37/42 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.46×** | +11.0 | 2e-26 | 18/25 (SW480, HS-578T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.45×** | +10.9 | 3e-26 | 23/31 (SW480, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.21×** | +10.1 | 2e-22 | 28/34 (SK-MEL-2, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.90×** | +9.8 | 6e-21 | 22/28 (Panc 03.27, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.87×** | +9.7 | 1e-20 | 31/42 (RKO, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.94×** | +8.4 | 9e-16 | 16/40 (PANC-1, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.22×** | +7.3 | 7e-12 | 17/34 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8679.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.627×** | -4.2 | 0.011 | 9/30 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | **0.735×** | -4.0 | 0.011 | 15/41 (RKO, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.630×** | -4.0 | 0.011 | 10/41 (Hs 766T, C32, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -3.9 | 0.011 | 6/41 (J82, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.673×** | -3.7 | 0.026 | 5/41 (A-427, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.682×** | -3.6 | 0.035 | 9/33 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.688×** | -3.5 | 0.040 | 9/39 (AsPC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.691×** | -3.4 | 0.042 | 10/39 (A-172, H4, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.736×** | -3.3 | 0.053 | 9/37 (AsPC-1, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sodium Salicylate (drug)]] 0.5 µM |  | 0.719× | -3.1 | 0.12 | 7/33 (A-427, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Neratinib (drug)]] 5 µM |  | 0.725× | -3.0 | 0.14 | 6/39 (SNU-1, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.04 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8679. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.86 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +15.0) | — |
| [[RKO (line)]] | wt | 28.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +13.3) | — |
| [[hTERT-HPNE (line)]] | wt | 8.55 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +12.4) | [[Clobetasol propionate (drug)]] 0.5 µM 0.0764× (z -8.6) |
| [[A-172 (line)]] | wt | 1.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 1.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.5× (z +9.4) | — |
| [[C32 (line)]] | wt | 1.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.9× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 1.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +10.7) | — |
| [[HEC-1-A (line)]] | alt | 2.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 1.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.9× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 5.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +11.6) | — |
| [[J82 (line)]] | alt | 1.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +8.8) | — |
| [[LoVo (line)]] | wt | 1.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.6× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 2.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 1.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.2× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 1.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 1.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 2.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 0.864 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 6.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +11.0) | — |
| [[SHP-77 (line)]] | alt | 9.83 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0856× (z -10.1) |
| [[SNU-423 (line)]] | alt | 3.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +10.0) | — |
| [[SW 900 (line)]] | alt | 2.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 3.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +10.8) | — |
| [[A-427 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.924 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.899 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.937 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.796 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8679), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPAL1]] | +0.71 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ADTRP]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[LINC01204]] | +0.68 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[ROBO4]] | +0.65 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[NRIP3]] | +0.64 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[PNP]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[KCTD5]] | +0.63 | +0.61 / +0.53 | both halves | 1e-05 | same gene group; STRING 569 |
| [[CORO2B]] | +0.63 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[MAST4]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[PTHLH]] | +0.63 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[NABP1]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[HBEGF]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR3]] | -0.57 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[TNRC6A]] | -0.55 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[SUMF2]] | -0.54 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[C12orf76]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ERP29]] | -0.53 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[MIRLET7BHG]] | -0.52 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[PPP1CB]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[NUDT21]] | -0.51 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[USP33]] | -0.51 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SORT1]] | -0.50 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[RABL6]] | -0.50 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[RCN2]] | -0.50 | -0.52 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL11]] | B | IL11 activity raises KBTBD8's level | lines that do not express IL11 (27) vs lines expressing it (23) | 1.82× lower at baseline in the lines without IL11 | 0.018 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |
| [[CFAP299]] | B | CFAP299 activity raises KBTBD8's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 1.60× lower at baseline in the lines without CFAP299 | 0.026 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2 |
| [[RDUR]] | B | RDUR activity raises KBTBD8's level | lines that do not express RDUR (28) vs lines expressing it (22) | 1.94× lower at baseline in the lines without RDUR | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC |
| [[MAP2K1]] | B | MAP2K1 activity raises KBTBD8's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[RGS4]] | B | RGS4 activity raises KBTBD8's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 1.57× lower at baseline in the lines without RGS4 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| [[ZFPM2-AS1]] | B | ZFPM2-AS1 activity raises KBTBD8's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 1.71× lower at baseline in the lines without ZFPM2-AS1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[DSCAM]] | B | DSCAM activity raises KBTBD8's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 1.51× lower at baseline in the lines without DSCAM | 0.064 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent |
| [[CCL3]] | B | CCL3 activity raises KBTBD8's level | lines that do not express CCL3 (37) vs lines expressing it (13) | 1.82× lower at baseline in the lines without CCL3 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| [[LNCOG]] | B | LNCOG activity raises KBTBD8's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without LNCOG | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[MAP2K2]] | B | MAP2K2 activity raises KBTBD8's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[BCL2A1]] | B | BCL2A1 activity raises KBTBD8's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.61× lower at baseline in the lines without BCL2A1 | 0.096 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA2-AS1]] | C | KBTBD8 activity raises ITGA2-AS1's level | lines that do not express KBTBD8 (4) vs lines expressing it (46) | 1.99× lower at baseline in the lines without KBTBD8 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000289986; its own permutation p |
| [[C3orf52]] | C | KBTBD8 activity raises C3orf52's level | lines that do not express KBTBD8 (4) vs lines expressing it (46) | 1.53× lower at baseline in the lines without KBTBD8 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000289986; its own permutation p |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.3, 1.3); signed map (14.3, 45.4). **Vector** length 54.6, 8.23% of its response variance represented; |z| ≥ 3 in 1,316 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +20.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +20.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.2 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +33.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.7 | +12.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +12.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +12.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +4.8 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -4.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -1.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | kelch repeat and BTB domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:66,998,307-67,011,210 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TA-KRP, KIAA1842 |
| Gene groups (HGNC) | BTB domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFY9](https://www.uniprot.org/uniprotkb/Q8NFY9) (Kelch repeat and BTB domain-containing protein 8):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin ligase complex that acts as a regulator of neural crest specification. The BCR(KBTBD8) complex acts by mediating monoubiquitination of NOLC1 and TCOF1: monoubiquitination promotes the formation of a NOLC1-TCOF1 complex that acts as a platform to connect RNA polymerase I with enzymes responsible for ribosomal processing and modification, leading to remodel the translational program of differentiating cells in favor of neural crest …

**Summary**, from NCBI Gene [84541](https://www.ncbi.nlm.nih.gov/gene/84541):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Involved in neural crest cell development; neural crest formation; and protein monoubiquitination. Part of Cul3-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30691](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30691) · Entrez [84541](https://www.ncbi.nlm.nih.gov/gene/84541) · UniProt [Q8NFY9](https://www.uniprot.org/uniprotkb/Q8NFY9) · Ensembl [ENSG00000163376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163376)

## Data

Gene col 8679: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8679); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8679, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8679]; `tensor/DDL_lfc|DDL_z.npy` [8679]; `embed/gene_vectors.npy` [8679]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8679 or target_col == 8679). Every well: [[KBTBD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KBTBD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
