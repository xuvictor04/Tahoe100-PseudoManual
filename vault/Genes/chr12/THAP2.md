---
symbol: "THAP2"
type: "gene"
col: 10386
ensembl_id: "ENSG00000173451"
name: "THAP domain containing 2"
location: "12q21.1"
module: 23
arm: "+"
pooled_cpm: 7.91
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# THAP2

*THAP domain containing 2* — 12q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.31× (z +27.5, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.678× (z -6.3, q 1e-07, down in 20 of 47 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.761× (z -4.3, q 0.003, down in 12 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (HS-578T 0.0712×); [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM in 1 line (Hs 766T 0.0793×); [[Digitoxin (drug)]] 5 µM in 1 line (RPMI-7951 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEPTIN7-DT]] (+0.83, fdr 3e-05), [[PPP1R12A-AS2]] (+0.82, fdr 4e-05), [[ATE1OSP]] (+0.81, fdr 1e-05); moves opposite to [[GTF2E2]] (-0.71, fdr 3e-05), [[SLC23A2]] (-0.71, fdr 1e-05), [[GNA12]] (-0.70, fdr 8e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10386.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.31×** | +27.5 | 0e+00 | 42/43 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +23.9 | 0e+00 | 42/43 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.59×** | +20.7 | 0e+00 | 39/41 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.70×** | +15.5 | 0e+00 | 27/36 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.33×** | +13.2 | 7e-38 | 32/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.96×** | +10.9 | 7e-26 | 32/46 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +10.0 | 8e-22 | 11/22 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +9.9 | 2e-21 | 23/41 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +9.9 | 3e-21 | 25/45 (LoVo, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +9.4 | 3e-19 | 23/41 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +8.7 | 1e-16 | 21/48 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +8.4 | 2e-15 | 21/47 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.62×** | +7.8 | 2e-13 | 25/46 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.2 | 3e-08 | 12/32 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +5.5 | 1e-06 | 15/37 (A-172, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.41×** | +5.1 | 1e-05 | 9/43 (PANC-1, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.002 | 9/46 (LS 180, A-172, …) | rises with dose |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.010 | 7/43 (H4, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.047 | 8/47 (NCI-H23, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10386.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (HS-578T 0.0712×); [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM in 1 line (Hs 766T 0.0793×); [[Digitoxin (drug)]] 5 µM in 1 line (RPMI-7951 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.678×** | -6.3 | 1e-07 | 20/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.695×** | -5.9 | 9e-07 | 17/46 (H4, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.714×** | -5.5 | 8e-06 | 14/47 (LS 180, NCI-H1792, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.761×** | -4.3 | 0.003 | 12/45 (NCI-H1573, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10386. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 9.19 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 8.96 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +12.6) | — |
| [[A498 (line)]] | wt | 7.72 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +12.8) | — |
| [[HS-578T (line)]] | alt | 7.83 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0712× (z -11.3) |
| [[PANC-1 (line)]] | alt | 9.19 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +12.8) | — |
| [[SW480 (line)]] | alt | 8.16 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.8) | — |
| [[A-172 (line)]] | wt | 13.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 12.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 12.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.04× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 15.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +12.2) | — |
| [[NCI-H2030 (line)]] | alt | 6.00 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 4.78 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 4.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.16× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 5.61 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 7.16× (z +8.5) ⚠ toxic | — |
| [[HOP62 (line)]] | alt | 9.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 6.25 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0793× (z -9.7) |
| [[LoVo (line)]] | wt | 8.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 9.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +12.7) | — |
| [[RPMI-7951 (line)]] | alt | 9.57 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 5.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 4.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.35× (z +9.3) | — |
| [[A-427 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10386), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN7-DT]] | +0.83 | +0.85 / +0.46 | both halves | 3e-05 |  |
| [[PPP1R12A-AS2]] | +0.82 | +0.84 / +0.41 | both halves | 4e-05 |  |
| [[ATE1OSP]] | +0.81 | +0.82 / +0.52 | both halves | 1e-05 |  |
| [[AK9]] | +0.81 | +0.86 / +0.50 | both halves | 1e-05 |  |
| [[ERCC6L2-AS1]] | +0.81 | +0.83 / +0.46 | both halves | 3e-05 |  |
| [[METTL6]] | +0.81 | +0.82 / +0.47 | both halves | 2e-05 |  |
| [[LINC01004]] | +0.81 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | +0.80 | +0.82 / +0.43 | both halves | 3e-05 |  |
| [[MAILR]] | +0.80 | +0.81 / +0.37 | both halves | 8e-05 |  |
| [[TMEM202-AS1]] | +0.80 | +0.82 / +0.42 | both halves | 4e-05 |  |
| [[KRBOX5]] | +0.79 | +0.82 / +0.50 | both halves | 1e-05 |  |
| [[RFX3-DT]] | +0.79 | +0.80 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2E2]] | -0.71 | -0.68 / -0.46 | both halves | 3e-05 |  |
| [[SLC23A2]] | -0.71 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[GNA12]] | -0.70 | -0.71 / -0.37 | both halves | 8e-05 |  |
| [[CEP131]] | -0.70 | -0.58 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers THAP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises THAP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC00491]] | B | LINC00491 activity raises THAP2's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 1.29× lower at baseline in the lines without LINC00491 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7 |
| [[LINC01829]] | C | LINC01829 activity raises THAP2's level | lines that do not express LINC01829 (3) vs lines expressing it (47) | 1.71× lower at baseline in the lines without LINC01829 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PARP11, GNG12-AS1, LINC02763; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.883). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.1, 12.4); signed map (23.3, -10.6). **Vector** length 86.5, 16.6% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +27.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +23.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +20.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.2 | +13.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +15.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +8.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +5.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -6.1 | -5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -6.0 | -5.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.9 | -6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -2.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -4.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | THAP domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.1 — chr12:71,664,301-71,680,644 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564I0422 |
| Gene groups (HGNC) | THAP domain family |
| Matched by | ensembl_id |

UniProt [Q9H0W7](https://www.uniprot.org/uniprotkb/Q9H0W7) carries no function annotation.

**Summary**, from NCBI Gene [83591](https://www.ncbi.nlm.nih.gov/gene/83591):

> Predicted to enable DNA binding activity and zinc ion binding activity. Located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20854) · Entrez [83591](https://www.ncbi.nlm.nih.gov/gene/83591) · UniProt [Q9H0W7](https://www.uniprot.org/uniprotkb/Q9H0W7) · Ensembl [ENSG00000173451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173451)

## Data

Gene col 10386: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10386); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10386, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10386]; `tensor/DDL_lfc|DDL_z.npy` [10386]; `embed/gene_vectors.npy` [10386]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10386 or target_col == 10386). Every well: [[THAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
