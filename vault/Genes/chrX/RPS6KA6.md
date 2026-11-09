---
symbol: "RPS6KA6"
type: "gene"
col: 1006
ensembl_id: "ENSG00000072133"
name: "ribosomal protein S6 kinase A6"
location: "Xq21.1"
module: 52
arm: "-"
pooled_cpm: 17.63
n_lines_expressing: 29
n_dd_up: 15
n_dd_down: 11
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# RPS6KA6

*ribosomal protein S6 kinase A6* — Xq21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.40× (z +19.0, q 0e+00, up in 22 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.740× (z -6.6, q 2e-08, down in 15 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTN2A2]] (+0.64, fdr 1e-05), [[ZFHX2]] (+0.61, fdr 1e-05), [[CFAP300]] (+0.59, fdr 4e-05); moves opposite to [[FBH1]] (-0.63, fdr 2e-05), [[TRAPPC10]] (-0.59, fdr 1e-05), [[PDCD6]] (-0.57, fdr 3e-05).
> It sits in the **-** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[AHR]] → it (grade B ⚠); 5 go from it, the strongest it → [[AHR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1006.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.40×** | +19.0 | 0e+00 | 22/26 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +8.9 | 1e-16 | 19/26 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +8.8 | 3e-16 | 21/26 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +6.4 | 2e-08 | 17/26 (NCI-H1573, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.31×** | +5.8 | 7e-07 | 16/26 (SW480, HOP62, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 3e-06 | 12/26 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +5.2 | 2e-05 | 15/26 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.34×** | +4.5 | 6e-04 | 9/26 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +4.3 | 0.001 | 12/26 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +4.1 | 0.002 | 9/27 (NCI-H23, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.022 | 9/26 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.034 | 8/26 (CFPAC-1, SW480, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.044 | 6/27 (CFPAC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.062 | 9/26 (HOP62, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.24×** | +3.0 | 0.092 | 8/26 (CFPAC-1, SW480, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1006.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -6.6 | 2e-08 | 15/27 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.715×** | -5.0 | 2e-04 | 12/21 (SHP-77, SW 900, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.729×** | -4.9 | 2e-04 | 15/25 (CHP-212, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.741×** | -4.5 | 0.001 | 14/26 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.765×** | -4.2 | 0.004 | 12/26 (A549, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.768×** | -4.1 | 0.004 | 12/26 (SW480, HCT15, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.770×** | -4.1 | 0.004 | 9/26 (SW480, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.767×** | -4.0 | 0.005 | 13/26 (NCI-H23, HEC-1-A, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.778×** | -3.9 | 0.006 | 12/26 (CFPAC-1, HCT15, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.665×** | -3.3 | 0.054 | 6/26 (CHP-212, A549, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.808×** | -3.2 | 0.078 | 6/26 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.689× | -3.0 | 0.12 | 9/21 (SW1417, A549, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1006. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +15.1) | — |
| [[CFPAC-1 (line)]] | alt | 69.2 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.162× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -11.9) |
| [[A549 (line)]] | wt | 47.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +17.0) | — |
| [[HOP62 (line)]] | alt | 25.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +13.5) | — |
| [[NCI-H1573 (line)]] | alt | 65.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.8) | — |
| [[NCI-H23 (line)]] | alt | 51.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -11.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 50.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.0) | — |
| [[CHP-212 (line)]] | wt | 37.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.101× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HCT15 (line)]] | alt | 71.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +12.9) | — |
| [[J82 (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 27.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.95× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +13.8) | — |
| [[SHP-77 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[SNU-423 (line)]] | alt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +13.1) | — |
| [[SW 900 (line)]] | alt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +11.0) | — |
| [[SW480 (line)]] | alt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.4) | — |
| [[A-172 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.88 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1006), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN2A2]] | +0.64 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ZFHX2]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[CFAP300]] | +0.59 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[KPNA5]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SEMA3E]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[TEX9]] | +0.57 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[OCIAD1]] | +0.57 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[CXCL2]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[KCNT2]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[HDX]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[DCDC2]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[TAB2]] | +0.54 | +0.41 / +0.44 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBH1]] | -0.63 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TRAPPC10]] | -0.59 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[PDCD6]] | -0.57 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[WDR37]] | -0.55 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[SENP5]] | -0.55 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[HIRA]] | -0.54 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[SHPK]] | -0.53 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[DGCR8]] | -0.53 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[GLE1]] | -0.52 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[TMEM104]] | -0.52 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[POC1A]] | -0.51 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[RNF4]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHR]] | B | AHR activity raises RPS6KA6's level | lines that do not express AHR (7) vs lines expressing it (43) | 3.76× lower at baseline in the lines without AHR | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[TOP2A]] | B | TOP2A activity raises RPS6KA6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF711]] | C | ZNF711 activity raises RPS6KA6's level | lines that do not express ZNF711 (15) vs lines expressing it (35) | 4.71× lower at baseline in the lines without ZNF711 | 0.026 | ⚠ within organs, on part of the lines; also absent: FRMPD3, RPS6KA6, MIR9-3HG; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHR]] | B | RPS6KA6 activity raises AHR's level | lines that do not express RPS6KA6 (21) vs lines expressing it (29) | 1.78× lower at baseline in the lines without RPS6KA6 | 0.030 | ⚠ within organs, on part of the lines; also absent: VWDE, SCN9A, MIR9-3HG |
| [[ZNF385C]] | B | RPS6KA6 activity raises ZNF385C's level | lines that do not express RPS6KA6 (21) vs lines expressing it (29) | 1.62× lower at baseline in the lines without RPS6KA6 | 0.049 | ⚠ within organs, on part of the lines; also absent: VWDE, SCN9A, MIR9-3HG |
| [[CCDC148]] | B | RPS6KA6 activity raises CCDC148's level | lines that do not express RPS6KA6 (21) vs lines expressing it (29) | 1.44× lower at baseline in the lines without RPS6KA6 | 0.067 | ⚠ within organs, on part of the lines; also absent: VWDE, SCN9A, MIR9-3HG |
| [[TBC1D9]] | B | RPS6KA6 activity raises TBC1D9's level | lines that do not express RPS6KA6 (21) vs lines expressing it (29) | 1.74× lower at baseline in the lines without RPS6KA6 | 0.078 | ⚠ within organs, on part of the lines; also absent: VWDE, SCN9A, MIR9-3HG |
| [[POLG]] | B | RPS6KA6 activity raises POLG's level | lines that do not express RPS6KA6 (21) vs lines expressing it (29) | 1.08× lower at baseline in the lines without RPS6KA6 | 0.097 | ⚠ within organs, on part of the lines; also absent: VWDE, SCN9A, MIR9-3HG |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (20.1, 8.1); signed map (50.2, 19.3). **Vector** length 65.8, 15.5% of its response variance represented; |z| ≥ 3 in 628 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +19.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.7 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.2 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +1.7 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -2.5 | -4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -2.4 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -1.8 | -3.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | +0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.3 | -6.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S6 kinase A6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.1 — chrX:84,058,346-84,206,356 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RSK4 |
| Gene groups (HGNC) | MAPK activated protein kinases; Ribosomal protein S6 kinase family |
| Reactome | 11 pathways, smallest: RSK activation; CREB1 phosphorylation through NMDA receptor-mediated activation of RAS signaling; Recycling pathway of L1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK32](https://www.uniprot.org/uniprotkb/Q9UK32) (Ribosomal protein S6 kinase alpha-6):

> Constitutively active serine/threonine-protein kinase that exhibits growth-factor-independent kinase activity and that may participate in p53/TP53-dependent cell growth arrest signaling and play an inhibitory role during embryogenesis.

**Summary**, from NCBI Gene [27330](https://www.ncbi.nlm.nih.gov/gene/27330):

> This gene encodes a member of ribosomal S6 kinase family, serine-threonine protein kinases which are regulated by growth factors. The encoded protein may be distinct from other members of this family, however, as studies suggest it is not growth factor dependent and may not participate in the same signaling pathways. [provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:10435](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10435) · Entrez [27330](https://www.ncbi.nlm.nih.gov/gene/27330) · UniProt [Q9UK32](https://www.uniprot.org/uniprotkb/Q9UK32) · Ensembl [ENSG00000072133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072133)

## Data

Gene col 1006: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1006); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1006, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1006]; `tensor/DDL_lfc|DDL_z.npy` [1006]; `embed/gene_vectors.npy` [1006]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1006 or target_col == 1006). Every well: [[RPS6KA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS6KA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
