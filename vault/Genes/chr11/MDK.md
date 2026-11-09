---
symbol: "MDK"
type: "gene"
col: 3144
ensembl_id: "ENSG00000110492"
name: "midkine"
location: "11p11.2"
module: 70
arm: "+"
pooled_cpm: 47.3
n_lines_expressing: 36
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# MDK

*midkine* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.61× (z +11.7, q 6e-29, up in 31 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 2.39× (z +9.4, q 8e-19, up in 32 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.546× (z -6.6, q 2e-08, down in 30 of 34 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITM2B]] (+0.63, fdr 1e-05), [[B2M]] (+0.60, fdr 1e-05), [[HLA-C]] (+0.58, fdr 2e-05); moves opposite to [[MPHOSPH6]] (-0.53, fdr 6e-05), [[DNAJA3]] (-0.53, fdr 3e-05), [[PRMT5]] (-0.50, fdr 7e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[SPPL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3144.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.61×** | +11.7 | 6e-29 | 31/32 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.79×** | +9.8 | 3e-20 | 27/27 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.39×** | +9.4 | 8e-19 | 32/34 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +8.3 | 2e-14 | 31/34 (AsPC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.28×** | +7.2 | 1e-10 | 28/29 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.31×** | +6.6 | 3e-09 | 32/34 (NCI-H23, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **2.09×** | +5.6 | 1e-06 | 31/34 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.05×** | +5.5 | 3e-06 | 29/33 (PANC-1, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here); position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.86×** | +4.7 | 1e-04 | 28/34 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.1 | 0.003 | 23/33 (CFPAC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +4.0 | 0.003 | 27/34 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.29×** | +3.6 | 0.015 | 27/33 (RKO, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.25×** | +3.5 | 0.018 | 27/34 (NCI-H2347, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.024 | 25/34 (LOX-IMVI, HepG2/C3A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +3.4 | 0.027 | 21/34 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.12×** | +3.3 | 0.037 | 23/34 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.072 | 15/34 (HT-29, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.072 | 17/34 (HOP62, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3144.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -6.6 | 2e-08 | 30/34 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.601×** | -3.9 | 0.016 | 24/34 (Hs 766T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.602×** | -3.9 | 0.016 | 21/34 (LoVo, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.644×** | -3.4 | 0.094 | 24/34 (Hs 766T, BT-474, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3144. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 31.2 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.72× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 3.35× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.218× (z -8.7) |
| [[HOP62 (line)]] | alt | 21.2 | 3 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.12× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 25.3 | 3 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.97× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 18.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 3.12× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 143 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 174 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 16.2 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 7.74× (z +12.1) | — |
| [[SHP-77 (line)]] | alt | 82.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -8.6) |
| [[SW48 (line)]] | wt | 16.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 10.8× (z +8.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.0672× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 32.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.26× (z +11.2) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 139 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -11.7) |
| [[C32 (line)]] | wt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.10× (z +8.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 94.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.1) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 86.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -11.3) |
| [[H4 (line)]] | wt | 60.1 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.54× (z +8.6) | — |
| [[J82 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 129 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.50× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 220 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -11.6) |
| [[PANC-1 (line)]] | alt | 69.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +11.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 74.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -8.6) |
| [[SW 900 (line)]] | alt | 43.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 8.42 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.37 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.07 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.35 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 381 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.61 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3144), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITM2B]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[B2M]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[HLA-C]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[PSME1]] | +0.58 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[RNASEK]] | +0.56 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[TAPBP]] | +0.56 | +0.61 / +0.39 | both halves | 6e-05 |  |
| [[HLA-B]] | +0.56 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[CRIP1]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ZNF821]] | +0.55 | +0.37 / +0.51 | both halves | 7e-05 |  |
| [[APOE]] | +0.55 | +0.52 / +0.48 | both halves | 2e-05 | STRING 509 |
| [[DNASE2]] | +0.55 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[GRN]] | +0.54 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH6]] | -0.53 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[DNAJA3]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PRMT5]] | -0.50 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[NPM3]] | -0.49 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[MIS18A]] | -0.48 | -0.49 / -0.24 | both halves | 5e-04 |  |
| [[SKIC8]] | -0.48 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[UTP11]] | -0.48 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[DGKD]] | -0.47 | -0.18 / -0.47 | ⚠ not reproduced | 9e-04 |  |
| [[EEFSEC]] | -0.47 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[CCT6A]] | -0.47 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[PGAM5]] | -0.47 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[MAP7D3]] | -0.47 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[BMS1]] | -0.46 | -0.53 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MDK's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CTSO]] | B | CTSO activity lowers MDK's level | lines that do not express CTSO (8) vs lines expressing it (42) | 2.22× higher at baseline in the lines without CTSO | 0.056 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPPL3]] | B | MDK activity strengthens SPPL3's drug response | lines that do not express MDK (14) vs lines expressing it (35) | the lines without MDK respond 0.82× as strongly (z diff +1.12); strongest at Digitoxin 0.5 µM: 1.29x vs 1.88x (z diff +2.8) | 0.006 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[C5orf15]] | B | MDK activity lowers C5orf15's level | lines that do not express MDK (14) vs lines expressing it (36) | 1.36× higher at baseline in the lines without MDK | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LIPA]] | B | MDK activity lowers LIPA's level | lines that do not express MDK (14) vs lines expressing it (36) | 1.55× higher at baseline in the lines without MDK | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.2, 49.4); signed map (64.8, 26.8). **Vector** length 81.9, 26.7% of its response variance represented; |z| ≥ 3 in 581 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Endosomal/Vacuolar pathway* (reactome, mean cos +0.51 to 8); *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.50 to 9); *Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.9 | +9.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.2 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +8.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.3 | +4.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +4.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +0.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.4 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.9 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | midkine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:46,380,756-46,383,837 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MK, FLJ27379; previously NEGF2 |
| Hallmark sets | APICAL_JUNCTION, ESTROGEN_RESPONSE_LATE |
| Reactome | 6 pathways, smallest: MDK and PTN in ALK signaling; NOTCH2 Activation and Transmission of Signal to the Nucleus; Signaling by ALK |
| Matched by | ensembl_id |

**Function**, from UniProt [P21741](https://www.uniprot.org/uniprotkb/P21741) (Midkine):

> Secreted protein that functions as a cytokine and growth factor and mediates its signal through cell-surface proteoglycan and non-proteoglycan receptors. Binds cell-surface proteoglycan receptors via their chondroitin sulfate (CS) groups. Thereby regulates many processes like inflammatory response, cell proliferation, cell adhesion, cell growth, cell survival, tissue regeneration, cell differentiation and cell migration. Participates in inflammatory processes by exerting two different …

**Summary**, from NCBI Gene [4192](https://www.ncbi.nlm.nih.gov/gene/4192):

> This gene encodes a member of a small family of secreted growth factors that binds heparin and responds to retinoic acid. The encoded protein promotes cell growth, migration, and angiogenesis, in particular during tumorigenesis. This gene has been targeted as a therapeutic for a variety of different disorders. Alternatively spliced transcript variants encoding multiple isoforms have been observed. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:6972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6972) · Entrez [4192](https://www.ncbi.nlm.nih.gov/gene/4192) · UniProt [P21741](https://www.uniprot.org/uniprotkb/P21741) · Ensembl [ENSG00000110492](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110492)

## Data

Gene col 3144: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3144); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3144, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3144]; `tensor/DDL_lfc|DDL_z.npy` [3144]; `embed/gene_vectors.npy` [3144]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3144 or target_col == 3144). Every well: [[MDK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MDK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
