---
symbol: "HOXA13"
type: "gene"
col: 2711
ensembl_id: "ENSG00000106031"
name: "homeobox A13"
location: "7p15.2"
module: 103
arm: "+"
pooled_cpm: 13.73
n_lines_expressing: 36
n_dd_up: 2
n_dd_down: 40
n_dd_up_clean: 2
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# HOXA13

*homeobox A13* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.65× (z +4.7, q 0.001, up in 18 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (LS 180 2.71×; ⚠ cell-cycle shift, explains ~39% of this change); [[Selinexor (drug)]] 0.5 µM in 1 line (LS 180 3.23×; ⚠ cell-cycle shift, explains ~50% of this change).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.228× (z -20.4, q 0e+00, down in 30 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRN1]] (+0.67, fdr 7e-06), [[EFNA3]] (+0.65, fdr 1e-05), [[RASSF4]] (+0.62, fdr 1e-05); moves opposite to [[PCBD2]] (-0.58, fdr 3e-05), [[DPH5-DT]] (-0.57, fdr 4e-05), [[AVEN]] (-0.57, fdr 3e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[LINC-PINT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2711.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (LS 180 2.71×; ⚠ cell-cycle shift, explains ~39% of this change); [[Selinexor (drug)]] 0.5 µM in 1 line (LS 180 3.23×; ⚠ cell-cycle shift, explains ~50% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.65×** | +4.7 | 0.001 | 18/32 (A-172, LoVo, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.047 | 16/33 (Hs 766T, AsPC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.40× | +3.4 | 0.14 | 7/34 (LoVo, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.39× | +3.2 | 0.17 | 9/33 (AsPC-1, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2711.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.228×** | -20.4 | 0e+00 | 30/32 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.220×** | -14.8 | 0e+00 | 27/31 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.283×** | -12.3 | 1e-32 | 27/33 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.310×** | -11.0 | 6e-26 | 25/30 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.361×** | -9.9 | 3e-21 | 27/33 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.349×** | -9.9 | 5e-21 | 25/32 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.378×** | -9.5 | 2e-19 | 29/32 (A-427, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.440×** | -8.0 | 8e-14 | 23/31 (SW 900, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.421×** | -8.0 | 1e-13 | 24/33 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.445×** | -7.9 | 2e-13 | 25/33 (LS 180, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.482×** | -7.1 | 7e-11 | 25/32 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.479×** | -6.9 | 2e-10 | 19/30 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.626×** | -6.4 | 6e-09 | 19/32 (NCI-H1792, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.634×** | -6.3 | 2e-08 | 22/34 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.545×** | -5.9 | 1e-07 | 21/32 (H4, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.658×** | -5.7 | 3e-07 | 22/34 (LoVo, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.588×** | -5.2 | 7e-06 | 16/32 (HT-29, AN3 CA, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2711. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 41.0 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0315× (z -27.4) |
| [[HT-29 (line)]] | alt | 63.1 | 0 | 12 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.129× (z -16.2) |
| [[A-172 (line)]] | wt | 29.5 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0344× (z -34.3) |
| [[LoVo (line)]] | wt | 79.5 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -18.5) |
| [[NCI-H1792 (line)]] | alt | 26.8 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0690× (z -20.6) |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 7 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0359× (z -13.7) |
| [[LS 180 (line)]] | wt | 39.8 | 2 (2 ⚠) | 3 | [[Selinexor (drug)]] 5 µM 2.71× (z +10.5) ⚠ cell-cycle shift, explains ~39% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.162× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -15.4) |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0613× (z -11.5) |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 4 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.177× (z -9.8) |
| [[HOP62 (line)]] | alt | 14.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0780× (z -21.8) |
| [[Hs 766T (line)]] | wt | 39.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -13.9) |
| [[J82 (line)]] | alt | 14.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0887× (z -18.3) |
| [[PANC-1 (line)]] | alt | 5.41 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0390× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0393× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -13.8) |
| [[AN3 CA (line)]] | alt | 25.1 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0688× (z -9.1) |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -10.8) |
| [[HCT15 (line)]] | alt | 45.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0973× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 4.96 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0623× (z -10.0) |
| [[A-427 (line)]] | wt | 5.58 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0344× (z -14.2) |
| [[CFPAC-1 (line)]] | alt | 7.25 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -9.9) |
| [[H4 (line)]] | wt | 24.2 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0516× (z -12.6) |
| [[HS-578T (line)]] | alt | 5.00 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0646× (z -9.3) |
| [[SW480 (line)]] | alt | 6.61 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -8.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.925 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.865 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2711), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRN1]] | +0.67 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[EFNA3]] | +0.65 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[RASSF4]] | +0.62 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[WDR54]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[RNASE4]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ZNF404]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ARL6]] | +0.60 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[RAB20]] | +0.60 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[AKR7A2]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[ABCB9]] | +0.59 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.59 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[MLLT3]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCBD2]] | -0.58 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[DPH5-DT]] | -0.57 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[AVEN]] | -0.57 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[EPM2A]] | -0.56 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[SMCO2]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ENOX2]] | -0.51 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[POU6F1]] | -0.51 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[RNF32-AS1]] | -0.49 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[SPTY2D1OS]] | -0.49 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[MSTO1]] | -0.48 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[RGS20]] | -0.48 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[DESI1]] | -0.48 | -0.42 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises HOXA13's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NRN1]] | B | NRN1 activity raises HOXA13's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 2.78× lower at baseline in the lines without NRN1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC-PINT]] | B | HOXA13 activity raises LINC-PINT's level | lines that do not express HOXA13 (14) vs lines expressing it (36) | 1.60× lower at baseline in the lines without HOXA13 | 0.020 | ⚠ within organs, on part of the lines; also absent: PRR5L |
| [[DPYSL4]] | B | HOXA13 activity raises DPYSL4's level | lines that do not express HOXA13 (14) vs lines expressing it (36) | 1.91× lower at baseline in the lines without HOXA13 | 0.069 | ⚠ within organs, on part of the lines; also absent: PRR5L |
| [[IFT172]] | B | HOXA13 activity raises IFT172's level | lines that do not express HOXA13 (14) vs lines expressing it (36) | 1.27× lower at baseline in the lines without HOXA13 | 0.085 | ⚠ within organs, on part of the lines; also absent: PRR5L |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.0, -14.0); signed map (-31.9, 28.6). **Vector** length 96.2, 25.9% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +0.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.7 | -4.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.0 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.8 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +1.7 | +2.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.0 | -5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.9 | -5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -6.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.4 | -4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -1.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.5 | -5.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | homeobox A13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:27,193,503-27,200,091 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX1J, HOX1 |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P31271](https://www.uniprot.org/uniprotkb/P31271) (Homeobox protein Hox-A13):

> Sequence-specific, AT-rich binding transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.; Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3209](https://www.ncbi.nlm.nih.gov/gene/3209):

> In vertebrates, the genes encoding the class of transcription factors called homeobox genes are found in clusters named A, B, C, and D on four separate chromosomes. Expression of these proteins is spatially and temporally regulated during embryonic development. This gene is part of the A cluster on chromosome 7 and encodes a DNA-binding transcription factor which may regulate gene expression, morphogenesis, and differentiation. Expansion of a polyalanine tract in the encoded protein can cause …

**Accessions** — [HGNC:5102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5102) · Entrez [3209](https://www.ncbi.nlm.nih.gov/gene/3209) · UniProt [P31271](https://www.uniprot.org/uniprotkb/P31271) · Ensembl [ENSG00000106031](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106031)

## Data

Gene col 2711: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2711); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2711, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2711]; `tensor/DDL_lfc|DDL_z.npy` [2711]; `embed/gene_vectors.npy` [2711]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2711 or target_col == 2711). Every well: [[HOXA13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXA13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
