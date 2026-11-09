---
symbol: "DNAJB5"
type: "gene"
col: 5966
ensembl_id: "ENSG00000137094"
name: "DnaJ heat shock protein family (Hsp40) member B5"
location: "9p13.3"
module: 189
arm: "+"
pooled_cpm: 3.42
n_lines_expressing: 47
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# DNAJB5

*DnaJ heat shock protein family (Hsp40) member B5* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.77× (z +18.3, q 0e+00, up in 27 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.741× (z -4.2, q 0.017, down in 20 of 41 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Selinexor (drug)]] 0.05 µM: 0.675× (z -3.9, q 0.017, down in 11 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Sinomenine (drug)]] 0.05 µM in 1 line (SHP-77 0.0682×); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.197×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Entrectinib (drug)]] 0.05 µM in 1 line (AsPC-1 0.0599×); [[Berberine (chloride hydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0808×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RELA]] (+0.56, fdr 7e-05), [[CIC]] (+0.53, fdr 1e-05), [[BMAL1]] (+0.52, fdr 4e-05); moves opposite to [[PPHLN1]] (-0.55, fdr 1e-05), [[POLR2B]] (-0.52, fdr 2e-05), [[TCTN3]] (-0.50, fdr 4e-05).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RNF223]] → it (grade B ⚠); 6 go from it, the strongest it → cells under [[MK-3903 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5966.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.77×** | +18.3 | 0e+00 | 27/32 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.32×** | +14.2 | 1e-43 | 36/41 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.95×** | +12.8 | 2e-35 | 30/36 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.43×** | +12.0 | 5e-31 | 35/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.40×** | +11.9 | 1e-30 | 32/41 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.93×** | +10.4 | 2e-23 | 19/32 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.27×** | +7.9 | 2e-13 | 23/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.99×** | +6.7 | 2e-09 | 17/32 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +5.4 | 5e-06 | 19/40 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +5.3 | 7e-06 | 17/40 (BT-474, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +5.3 | 7e-06 | 14/42 (HS-578T, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.70×** | +5.1 | 2e-05 | 11/35 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +5.0 | 2e-05 | 8/45 (MIA PaCa-2, HS-578T, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.38×** | +4.4 | 4e-04 | 2/10 (HOP62, BT-474) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.004 | 7/36 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.015 | 6/43 (SW 900, A549, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.021 | 7/38 (CFPAC-1, BT-474, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5966.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Sinomenine (drug)]] 0.05 µM in 1 line (SHP-77 0.0682×); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.197×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Entrectinib (drug)]] 0.05 µM in 1 line (AsPC-1 0.0599×); [[Berberine (chloride hydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0808×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.741×** | -4.2 | 0.017 | 20/41 (HOP62, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.668×** | -4.0 | 0.017 | 12/35 (KATO III, C-33 A, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM |  | **0.675×** | -3.9 | 0.017 | 11/43 (Hs 766T, HCT15, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.760×** | -3.8 | 0.017 | 12/39 (Hs 766T, SK-MEL-2, …) | top dose only | position effect removed |
| [[Cepharanthine (drug)]] 0.5 µM |  | 0.736× | -3.0 | 0.28 | 1/32 (Panc 03.27) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5966. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.63 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.50× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 5.51 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +15.4) | — |
| [[NCI-H460 (line)]] | wt | 1.93 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.86× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 3.97 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 6.23 | 0 | 2 | — | [[Sinomenine (drug)]] 0.05 µM 0.0682× (z -9.0) |
| [[A549 (line)]] | wt | 2.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 5.49 | 0 | 1 | — | [[Entrectinib (drug)]] 0.05 µM 0.0599× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 1.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.1× (z +8.9) | — |
| [[J82 (line)]] | alt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 7.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 4.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +12.2) | — |
| [[A-427 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.816 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.989 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5966), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELA]] | +0.56 | +0.38 / +0.46 | both halves | 7e-05 |  |
| [[CIC]] | +0.53 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[BMAL1]] | +0.52 | +0.40 / +0.57 | both halves | 4e-05 |  |
| [[PDLIM3]] | +0.51 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[TNKS1BP1]] | +0.51 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[CFAP46]] | +0.51 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ARVCF]] | +0.50 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[TUBB2A]] | +0.50 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[TUBB2B]] | +0.50 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[SYT7]] | +0.50 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[DLGAP4]] | +0.50 | +0.37 / +0.47 | both halves | 8e-05 |  |
| [[CREB3]] | +0.50 | +0.43 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPHLN1]] | -0.55 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[POLR2B]] | -0.52 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[TCTN3]] | -0.50 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[HOXB6]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[TYW1]] | -0.49 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[MBTD1]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[CTTN-DT]] | -0.49 | -0.11 / -0.53 | ⚠ one half (not replicated) | 0.002 |  |
| [[NDUFAF7]] | -0.49 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[IPO11]] | -0.48 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[WDR12]] | -0.48 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[MRPS35]] | -0.48 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[FAM120C]] | -0.48 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[LINC03006-1]] | -0.48 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF223]] | B | RNF223 activity lowers DNAJB5's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 1.73× higher at baseline in the lines without RNF223 | 0.023 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[MK-3903 (drug)]] 5 µM | C | DNAJB5 activity raises the cells' numbers under MK-3903 5 µM (protects the cells) | lines that do not express DNAJB5 (3) vs lines expressing it (45) | the lines without DNAJB5: 0.62× the cells of the other lines | 0.021 | ⚠ few lines (3 vs 47); across organs; also absent: CEP170, SRGAP2C, TLCD5; maybe low, not absent |
| [[ANKRD50]] | C | DNAJB5 activity raises ANKRD50's level | lines that do not express DNAJB5 (3) vs lines expressing it (47) | 2.70× lower at baseline in the lines without DNAJB5 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: CEP170, SRGAP2C, TLCD5; maybe low, not absent |
| cells under [[GSK1059615 (drug)]] 0.5 µM | C | DNAJB5 activity raises the cells' numbers under GSK1059615 0.5 µM (protects the cells) | lines that do not express DNAJB5 (3) vs lines expressing it (45) | the lines without DNAJB5: 0.62× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: CEP170, SRGAP2C, TLCD5; maybe low, not absent |
| [[KRTAP5-AS1]] | C | DNAJB5 activity lowers KRTAP5-AS1's level | lines that do not express DNAJB5 (3) vs lines expressing it (47) | 4.11× higher at baseline in the lines without DNAJB5 | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: CEP170, SRGAP2C, TLCD5; maybe low, not absent |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | C | DNAJB5 activity lowers the cells' numbers under Cysteamine (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express DNAJB5 (3) vs lines expressing it (45) | the lines without DNAJB5: 1.21× the cells of the other lines | 0.083 | ⚠ few lines (3 vs 47); across organs; also absent: CEP170, SRGAP2C, TLCD5; maybe low, not absent |
| [[SLC12A4]] | C | DNAJB5 activity raises SLC12A4's level | lines that do not express DNAJB5 (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without DNAJB5 | 0.094 | ⚠ few lines (3 vs 47); across organs; also absent: CEP170, SRGAP2C, TLCD5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.6, -12.1); signed map (-3.0, 22.1). **Vector** length 59.8, 8.92% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +18.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.6 | +5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | +2.5 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +5.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +5.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.1 | -4.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.8 | -4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -2.8 |
|  | [[Selinexor (drug)]] 0.05 µM |  | -1.9 | -3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -0.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member B5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:34,989,641-34,998,900 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hsc40 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

UniProt [O75953](https://www.uniprot.org/uniprotkb/O75953) carries no function annotation.

**Summary**, from NCBI Gene [25822](https://www.ncbi.nlm.nih.gov/gene/25822):

> This gene encodes a member of the DNAJ heat shock protein 40 family of co-chaperone proteins. The encoded protein contains an N-terminal DNAJ domain and a C-terminal substrate binding domain but lacks the cysteine-rich domain found in other DNAJ family members. In mice, a multi-protein complex containing this protein, thioredoxin 1, and histone deacetylase 4, serves as a master negative regulator of cardiac hypertrophy. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:14887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14887) · Entrez [25822](https://www.ncbi.nlm.nih.gov/gene/25822) · UniProt [O75953](https://www.uniprot.org/uniprotkb/O75953) · Ensembl [ENSG00000137094](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137094)

## Data

Gene col 5966: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5966); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5966, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5966]; `tensor/DDL_lfc|DDL_z.npy` [5966]; `embed/gene_vectors.npy` [5966]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5966 or target_col == 5966). Every well: [[DNAJB5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJB5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
