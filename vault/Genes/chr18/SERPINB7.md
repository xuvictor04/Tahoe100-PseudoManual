---
symbol: "SERPINB7"
type: "gene"
col: 9296
ensembl_id: "ENSG00000166396"
name: "serpin family B member 7"
location: "18q21.33"
module: 14
arm: "+"
pooled_cpm: 6.25
n_lines_expressing: 26
n_dd_up: 31
n_dd_down: 13
n_dd_up_clean: 24
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 10
direction_downstream: 19
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SERPINB7

*serpin family B member 7* — 18q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.12× (z +23.3, q 0e+00, up in 17 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Budesonide (drug)]] 5 µM: 0.480× (z -5.5, q 3e-05, down in 12 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGN2P46]] (+0.71, fdr 7e-06), [[TRAF1]] (+0.69, fdr 7e-06), [[NKX3-1]] (+0.66, fdr 7e-06).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CXCL3]] → it (grade B ⚠); 19 go from it, the strongest it → [[ISG20]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9296.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.12×** | +23.3 | 0e+00 | 17/20 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **10.0×** | +16.5 | 0e+00 | 19/19 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **8.17×** | +15.7 | 0e+00 | 17/20 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.63×** | +11.4 | 4e-28 | 19/22 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.35×** | +9.0 | 2e-17 | 16/22 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +9.0 | 3e-17 | 1/8 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.93×** | +8.0 | 9e-14 | 6/14 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.49×** | +6.7 | 2e-09 | 13/21 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.21×** | +5.9 | 2e-07 | 14/20 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.15×** | +5.7 | 7e-07 | 15/22 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +5.2 | 1e-05 | 4/12 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.60×** | +5.0 | 3e-05 | 9/22 (A549, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +4.8 | 6e-05 | 9/18 (NCI-H1573, SNU-423, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.37×** | +4.7 | 9e-05 | 8/19 (NCI-H460, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +4.6 | 1e-04 | 2/9 (LOX-IMVI, hTERT-HPNE) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.49×** | +4.2 | 9e-04 | 8/22 (BT-474, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.70×** | +4.0 | 0.002 | 12/21 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +3.6 | 0.011 | 9/21 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.62×** | +3.3 | 0.024 | 8/18 (A498, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.031 | 5/21 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9296.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | **0.480×** | -5.5 | 3e-05 | 12/23 (A549, NCI-H1792, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.555×** | -4.4 | 0.003 | 11/21 (A549, A-172, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.564×** | -4.3 | 0.004 | 12/22 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.570×** | -4.2 | 0.004 | 8/21 (A549, LOX-IMVI, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.581×** | -4.0 | 0.006 | 12/21 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.620×** | -3.6 | 0.029 | 9/20 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.621×** | -3.5 | 0.029 | 6/21 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 5 µM |  | **0.404×** | -3.5 | 0.029 | 5/22 (A549, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.628×** | -3.5 | 0.034 | 14/20 (BT-474, NCI-H1792, …) | top dose only | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.644×** | -3.3 | 0.060 | 9/21 (NCI-H1792, BT-474, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.650×** | -3.2 | 0.069 | 9/21 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.661×** | -3.1 | 0.098 | 6/23 (A549, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **0.748×** | -3.1 | 0.099 | 8/21 (A549, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 37.8 | 2 | 8 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.41× (z +9.4) | [[Budesonide (drug)]] 0.5 µM 0.0610× (z -14.8) |
| [[BT-474 (line)]] | alt | 20.3 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0225× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.0242× (z -10.2) |
| [[A498 (line)]] | wt | 4.13 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 32.1× (z +11.9) | — |
| [[NCI-H1792 (line)]] | alt | 22.0 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0495× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Dexamethasone (drug)]] 5 µM 0.0904× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 30.7 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 9.45× (z +9.6) | — |
| [[J82 (line)]] | alt | 3.35 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.5× (z +14.6) | — |
| [[LOX-IMVI (line)]] | wt | 79.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 2.47 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 54.4× (z +15.6) | — |
| [[A-172 (line)]] | wt | 2.86 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 44.5× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.8× (z +16.6) | — |
| [[SW 900 (line)]] | alt | 5.48 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 2.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0612× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 3.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 2.64 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 15.8× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 3.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +9.6) | — |
| [[A-427 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.976 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.415 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN2P46]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[TRAF1]] | +0.69 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[NKX3-1]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[LINC01828]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[TNFRSF9]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[GPR158]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[CPAMD8]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[HLA-F]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[INHBA]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[NEURL3]] | +0.61 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LINC02605]] | +0.61 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[RASGRP3]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL3]] | B | CXCL3 activity raises SERPINB7's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 2.66× lower at baseline in the lines without CXCL3 | 0.016 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[VNN1]] | B | VNN1 activity raises SERPINB7's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.40× lower at baseline in the lines without VNN1 | 0.029 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[GBP3]] | B | GBP3 activity raises SERPINB7's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 2.10× lower at baseline in the lines without GBP3 | 0.066 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[LINC02605]] | B | LINC02605 activity raises SERPINB7's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 2.28× lower at baseline in the lines without LINC02605 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |
| [[SERPINB3]] | C | SERPINB3 activity raises SERPINB7's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 3.07× lower at baseline in the lines without SERPINB3 | 0.032 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[PTGS2]] | C | PTGS2 activity raises SERPINB7's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.83× lower at baseline in the lines without PTGS2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4; co-absent with the target |
| [[CXCL8]] | C | CXCL8 activity raises SERPINB7's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 3.02× lower at baseline in the lines without CXCL8 | 0.036 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48; co-absent with the target |
| [[TNIP3]] | C | TNIP3 activity raises SERPINB7's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 3.57× lower at baseline in the lines without TNIP3 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA; co-absent with the target |
| [[SERPINB4]] | C | SERPINB4 activity raises SERPINB7's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 2.62× lower at baseline in the lines without SERPINB4 | 0.060 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |
| [[BMP2]] | C | BMP2 activity raises SERPINB7's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.36× lower at baseline in the lines without BMP2 | 0.076 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 11, C 8. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ISG20]] | B | SERPINB7 activity raises ISG20's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 1.98× lower at baseline in the lines without SERPINB7 | 0.005 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[CXCL3]] | B | SERPINB7 activity raises CXCL3's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 2.61× lower at baseline in the lines without SERPINB7 | 0.026 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[SLC28A3]] | B | SERPINB7 activity raises SLC28A3's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 1.67× lower at baseline in the lines without SERPINB7 | 0.034 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[KIAA1217]] | B | SERPINB7 activity raises KIAA1217's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 1.95× lower at baseline in the lines without SERPINB7 | 0.039 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[GBP3]] | B | SERPINB7 activity raises GBP3's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without SERPINB7 | 0.056 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[TNFAIP2]] | B | SERPINB7 activity raises TNFAIP2's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 2.62× lower at baseline in the lines without SERPINB7 | 0.061 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[CD47]] | B | SERPINB7 activity raises CD47's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 1.33× lower at baseline in the lines without SERPINB7 | 0.063 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[DUSP8]] | B | SERPINB7 activity raises DUSP8's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 1.31× lower at baseline in the lines without SERPINB7 | 0.073 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[VNN1]] | B | SERPINB7 activity raises VNN1's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 1.66× lower at baseline in the lines without SERPINB7 | 0.089 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| cells under [[Vortioxetine (drug)]] 0.5 µM | B | SERPINB7 activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express SERPINB7 (24) vs lines expressing it (24) | the lines without SERPINB7: 1.22× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[DUSP16]] | B | SERPINB7 activity raises DUSP16's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 1.35× lower at baseline in the lines without SERPINB7 | 0.098 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[HMGN2P46]] | C | SERPINB7 activity raises HMGN2P46's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 3.65× lower at baseline in the lines without SERPINB7 | 0.008 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.3, 1.1); signed map (40.9, 11.7). **Vector** length 75.6, 21.2% of its response variance represented; |z| ≥ 3 in 712 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +9.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +16.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +23.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +15.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.1 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +6.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +3.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.4 | -4.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.0 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | serpin family B member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.33 — chr18:63,752,935-63,805,376 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Matched by | ensembl_id |

**Function**, from UniProt [O75635](https://www.uniprot.org/uniprotkb/O75635) (Serpin B7):

> Might function as an inhibitor of Lys-specific proteases. Might influence the maturation of megakaryocytes via its action as a serpin.

**Summary**, from NCBI Gene [8710](https://www.ncbi.nlm.nih.gov/gene/8710):

> This gene encodes a member of a family of proteins which function as protease inhibitors. Expression of this gene is upregulated in IgA nephropathy and mutations have been found to cause palmoplantar keratoderma, Nagashima type. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:13902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13902) · Entrez [8710](https://www.ncbi.nlm.nih.gov/gene/8710) · UniProt [O75635](https://www.uniprot.org/uniprotkb/O75635) · Ensembl [ENSG00000166396](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166396)

## Data

Gene col 9296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9296); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9296]; `tensor/DDL_lfc|DDL_z.npy` [9296]; `embed/gene_vectors.npy` [9296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9296 or target_col == 9296). Every well: [[SERPINB7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINB7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
