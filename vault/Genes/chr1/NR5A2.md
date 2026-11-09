---
symbol: "NR5A2"
type: "gene"
col: 3846
ensembl_id: "ENSG00000116833"
name: "nuclear receptor subfamily 5 group A member 2"
location: "1q32.1"
module: 128
arm: "+"
pooled_cpm: 30.84
n_lines_expressing: 17
n_dd_up: 15
n_dd_down: 17
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# NR5A2

*nuclear receptor subfamily 5 group A member 2* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.44× (z +10.5, q 4e-23, up in 1 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +9.8, q 3e-20, up in 3 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.624× (z -5.6, q 2e-05, down in 10 of 14 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02643]] (+0.62, fdr 1e-05), [[GCG]] (+0.62, fdr 2e-05), [[CACNA1B]] (+0.61, fdr 2e-05); moves opposite to [[KRBOX4]] (-0.39, fdr 1e-04), [[TGFA]] (-0.38, fdr 2e-04), [[SVIL-AS1-1]] (-0.37, fdr 1e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 6 go from it, the strongest it → [[NEBL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3846.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +10.5 | 4e-23 | 1/14 (NCI-H23) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +9.8 | 3e-20 | 3/15 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.73×** | +9.1 | 1e-17 | 6/15 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +8.0 | 3e-13 | 1/11 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +6.4 | 2e-08 | 5/14 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +5.4 | 6e-06 | 1/12 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +4.2 | 0.002 | 5/14 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.005 | 6/14 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.006 | 5/14 (LoVo, A549, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.020 | 3/14 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.028 | 6/15 (LoVo, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.028 | 7/14 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.028 | 4/14 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.030 | 9/15 (LoVo, A549, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.051 | 5/15 (CFPAC-1, A549, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.087 | 2/15 (AsPC-1, PANC-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3846.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.624×** | -5.6 | 2e-05 | 10/14 (A-427, A549, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.638×** | -5.3 | 3e-05 | 13/14 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.642×** | -5.2 | 3e-05 | 11/14 (A-427, A549, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.648×** | -5.1 | 5e-05 | 11/14 (A-427, A549, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.667×** | -4.8 | 2e-04 | 12/14 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.687×** | -4.4 | 9e-04 | 9/14 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.706×** | -4.1 | 0.003 | 10/14 (A-427, C-33 A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.906× | -3.9 | 0.006 | 1/15 (MIA PaCa-2) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.809×** | -3.5 | 0.027 | 12/15 (AsPC-1, NCI-H1792, …) | two highest doses | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.753×** | -3.3 | 0.048 | 11/14 (C-33 A, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.755×** | -3.3 | 0.048 | 10/14 (C-33 A, A-427, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.824×** | -3.2 | 0.058 | 9/15 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Tucatinib (drug)]] 0.5 µM |  | **0.682×** | -3.2 | 0.058 | 0/15 | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.764×** | -3.2 | 0.064 | 12/14 (C-33 A, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.761×** | -3.1 | 0.076 | 10/14 (AsPC-1, A-427, …) | all doses, flat | composition shift; position effect removed |
| [[Tomivosertib (drug)]] 5 µM |  | **0.607×** | -3.1 | 0.076 | 3/14 (HepG2/C3A, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.776×** | -3.0 | 0.097 | 1/14 (HT-29) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3846. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 860 | 0 | 15 (13 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0390× (z -24.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -21.7) |
| [[A-427 (line)]] | wt | 472 | 0 | 14 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0662× (z -22.0) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 85.1 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -16.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -11.8) |
| [[A549 (line)]] | wt | 122 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -15.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.147× (z -9.1) |
| [[LoVo (line)]] | wt | 15.6 | 4 (1 ⚠) | 0 | [[Cobimetinib (drug)]] 5 µM 4.88× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 30.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -12.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.125× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0997× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0837× (z -16.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.65 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.60 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.31 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.79 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.87 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3846), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02643]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[GCG]] | +0.62 | +0.65 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[CACNA1B]] | +0.61 | +0.64 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[LRRC36]] | +0.58 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[LINC01010]] | +0.55 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[MMRN1]] | +0.53 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[LINC00466]] | +0.52 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[FGA]] | +0.52 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[RFPL1S]] | +0.51 | +0.56 / +0.26 | both halves | 4e-04 |  |
| [[JPH3]] | +0.50 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[OLR1]] | +0.50 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[CYP24A1]] | +0.49 | +0.42 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRBOX4]] | -0.39 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[TGFA]] | -0.38 | -0.31 / -0.42 | both halves | 2e-04 | pathway: ESR-mediated signaling |
| [[SVIL-AS1-1]] | -0.37 | -0.32 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers NR5A2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[CNTNAP3]] | C | CNTNAP3 activity raises NR5A2's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 3.17× lower at baseline in the lines without CNTNAP3 | 0.040 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |
| [[PON3]] | C | PON3 activity raises NR5A2's level | lines that do not express PON3 (22) vs lines expressing it (28) | 2.74× lower at baseline in the lines without PON3 | 0.066 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5; co-absent with the target |
| [[BTNL9]] | C | BTNL9 activity raises NR5A2's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without BTNL9 | 0.088 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEBL]] | B | NR5A2 activity strengthens NEBL's drug response | lines that do not express NR5A2 (19) vs lines expressing it (12) | the lines without NR5A2 respond 0.59× as strongly (z diff +2.31); strongest at Ouabain (Octahydrate) 5 µM: 0.58x vs 0.30x (z diff +5.0) | 0.059 | ⚠ within organs, on part of the lines; also absent: FGA, ENSG00000237031, CYP24A1; target measured in part of the lines; artifact flags |
| [[SDHAP3]] | B | NR5A2 activity raises SDHAP3's level | lines that do not express NR5A2 (33) vs lines expressing it (17) | 1.90× lower at baseline in the lines without NR5A2 | 0.078 | ⚠ within organs, on part of the lines; also absent: FGA, ENSG00000237031, CYP24A1 |
| [[RASGEF1A]] | C | NR5A2 activity raises RASGEF1A's level | lines that do not express NR5A2 (33) vs lines expressing it (17) | 1.96× lower at baseline in the lines without NR5A2 | 0.013 | ⚠ within organs, on part of the lines; also absent: FGA, ENSG00000237031, CYP24A1; co-absent with the target |
| [[BTNL9]] | C | NR5A2 activity raises BTNL9's level | lines that do not express NR5A2 (33) vs lines expressing it (17) | 2.18× lower at baseline in the lines without NR5A2 | 0.014 | ⚠ within organs, on part of the lines; also absent: FGA, ENSG00000237031, CYP24A1; co-absent with the target |
| [[PON3]] | C | NR5A2 activity raises PON3's level | lines that do not express NR5A2 (33) vs lines expressing it (17) | 2.54× lower at baseline in the lines without NR5A2 | 0.048 | ⚠ within organs, on part of the lines; also absent: FGA, ENSG00000237031, CYP24A1; co-absent with the target |
| [[PLAC8]] | C | NR5A2 activity raises PLAC8's level | lines that do not express NR5A2 (33) vs lines expressing it (17) | 3.16× lower at baseline in the lines without NR5A2 | 0.093 | ⚠ within organs, on part of the lines; also absent: FGA, ENSG00000237031, CYP24A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.9, 37.0); signed map (25.3, 25.6). **Vector** length 62.3, 21.7% of its response variance represented; |z| ≥ 3 in 465 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +2.2 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +9.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +3.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.1 | +3.4 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -4.1 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 5 group A member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:200,027,614-200,177,420 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FTZ-F1beta, hB1F, LRH-1, FTZ-F1, hB1F-2, B1F2, LRH1; previously FTF |
| Gene groups (HGNC) | Nuclear receptor subfamily 5 group A |
| Reactome | 14 pathways, smallest: Regulation of gene expression in early pancreatic precursor cells; Regulation of beta-cell development; SUMOylation of intracellular receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [O00482](https://www.uniprot.org/uniprotkb/O00482) (Nuclear receptor subfamily 5 group A member 2):

> Orphan nuclear receptor that binds DNA as a monomer to the 5'-TCAAGGCCA-3' sequence and controls expression of target genes: regulates key biological processes, such as early embryonic development, cholesterol and bile acid synthesis pathways, as well as liver and pancreas morphogenesis. Ligand-binding causes conformational change which causes recruitment of coactivators, promoting target gene activation. The specific ligand is unknown, but specific phospholipids, such as …

**Summary**, from NCBI Gene [2494](https://www.ncbi.nlm.nih.gov/gene/2494):

> The protein encoded by this gene is a DNA-binding zinc finger transcription factor and is a member of the fushi tarazu factor-1 subfamily of orphan nuclear receptors. The encoded protein is involved in the expression of genes for hepatitis B virus and cholesterol biosynthesis, and may be an important regulator of embryonic development. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:7984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7984) · Entrez [2494](https://www.ncbi.nlm.nih.gov/gene/2494) · UniProt [O00482](https://www.uniprot.org/uniprotkb/O00482) · Ensembl [ENSG00000116833](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116833)

## Data

Gene col 3846: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3846); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3846, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3846]; `tensor/DDL_lfc|DDL_z.npy` [3846]; `embed/gene_vectors.npy` [3846]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3846 or target_col == 3846). Every well: [[NR5A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR5A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
