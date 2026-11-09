---
symbol: "UQCC1"
type: "gene"
col: 2061
ensembl_id: "ENSG00000101019"
name: "ubiquinol-cytochrome c reductase complex assembly factor 1"
location: "20q11.22"
module: 89
arm: "+"
pooled_cpm: 85.82
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# UQCC1

*ubiquinol-cytochrome c reductase complex assembly factor 1* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.50× (z +7.2, q 3e-10, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.42× (z +6.3, q 7e-08, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.641× (z -7.7, q 9e-12, down in 28 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.728× (z -5.7, q 2e-06, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APTX]] (+0.75, fdr 7e-06), [[SLC25A17]] (+0.70, fdr 7e-06), [[RCC1L]] (+0.69, fdr 1e-05); moves opposite to [[KLF2]] (-0.56, fdr 3e-04), [[CDKN2D]] (-0.55, fdr 6e-05), [[ACBD7]] (-0.54, fdr 4e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2061.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.50×** | +7.2 | 3e-10 | 37/48 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.48×** | +6.6 | 1e-08 | 37/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +6.3 | 7e-08 | 35/48 (SHP-77, NCI-H2347, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +5.3 | 2e-05 | 34/49 (A498, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +5.0 | 7e-05 | 32/48 (A-172, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.7 | 2e-04 | 27/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 3e-04 | 29/48 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.5 | 4e-04 | 25/48 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.002 | 27/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +4.0 | 0.004 | 22/48 (A-427, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.012 | 21/47 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.22×** | +3.5 | 0.022 | 23/48 (A549, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.20× | +3.3 | 0.049 | 21/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 1.19× | +3.1 | 0.074 | 18/49 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.19× | +3.1 | 0.080 | 15/48 (A498, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2061.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.641×** | -7.7 | 9e-12 | 28/44 (SK-MEL-2, CHP-212, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.655×** | -7.6 | 9e-12 | 35/49 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **0.717×** | -6.0 | 5e-07 | 36/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.728×** | -5.7 | 2e-06 | 35/48 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.744×** | -5.3 | 1e-05 | 31/48 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.759×** | -4.9 | 7e-05 | 30/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.762×** | -4.7 | 2e-04 | 29/48 (PANC-1, RPMI-7951, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.773×** | -4.3 | 0.001 | 24/45 (C32, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.790×** | -4.2 | 0.001 | 22/48 (SW1417, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.825×** | -4.1 | 0.002 | 25/48 (NCI-H460, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.817×** | -3.6 | 0.015 | 22/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2061. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H596 (line)]] | alt | 81.2 | 2 | 4 | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 2.25× (z +13.6) | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.126× (z -33.8) |
| [[A498 (line)]] | wt | 88.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.17× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 34.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW1417 (line)]] | alt | 121 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 2.22× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.478× (z -9.1) |
| [[BT-474 (line)]] | alt | 243 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.366× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 61.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[CHP-212 (line)]] | wt | 97.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 62.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 76.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H1573 (line)]] | alt | 71.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H1792 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.367× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0662× (z -31.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H460 (line)]] | wt | 81.2 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 93.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.410× (z -10.6) ⚠ transcription drop; cell-cycle shift, explains ~58% of this change |
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SHP-77 (line)]] | alt | 87.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.44× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW 1088 (line)]] | alt | 101 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0923× (z -8.9) |
| [[A-172 (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 68.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 75.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 142 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 104 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2061), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APTX]] | +0.75 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[SLC25A17]] | +0.70 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RCC1L]] | +0.69 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[SPRYD4]] | +0.69 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[PTCD1]] | +0.67 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ZCCHC4]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MAFIP]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[IREB2]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[PAAF1]] | +0.64 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[GPALPP1]] | +0.62 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[EXOSC3]] | +0.62 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[CSTF3]] | +0.61 | +0.41 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF2]] | -0.56 | -0.29 / -0.57 | both halves | 3e-04 |  |
| [[CDKN2D]] | -0.55 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[ACBD7]] | -0.54 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[STARD5]] | -0.53 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[AFDN]] | -0.53 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[USP2]] | -0.53 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[ING1]] | -0.52 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[NCAM1]] | -0.52 | -0.37 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UQCC1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises UQCC1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises UQCC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.1, 18.6); signed map (29.0, -19.3). **Vector** length 110, 31.9% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.3 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.5 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.8 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.9 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.8 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +4.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.1 | +1.4 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -6.0 | -5.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -4.9 | -3.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.9 | -4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | -4.1 | -4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -2.0 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.9 | -1.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquinol-cytochrome c reductase complex assembly factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:35,302,566-35,412,031 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10850, CBP3, BFZB; previously C20orf44, UQCC |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex III assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVA1](https://www.uniprot.org/uniprotkb/Q9NVA1) (Ubiquinol-cytochrome c reductase complex assembly factor 1):

> Required for the assembly of the ubiquinol-cytochrome c reductase complex (mitochondrial respiratory chain complex III or cytochrome b-c1 complex). Involved in cytochrome b translation and/or stability.

**Summary**, from NCBI Gene [55245](https://www.ncbi.nlm.nih.gov/gene/55245):

> This gene encodes a transmembrane protein that is structurally similar to the mouse basic fibroblast growth factor repressed ZIC-binding protein. In mouse this protein may be involved in fibroblast growth factor regulated growth control. In humans, polymorphisms in this gene are associated with variation in human height and osteoarthritis. Alternate splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:15891](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15891) · Entrez [55245](https://www.ncbi.nlm.nih.gov/gene/55245) · UniProt [Q9NVA1](https://www.uniprot.org/uniprotkb/Q9NVA1) · Ensembl [ENSG00000101019](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101019)

## Data

Gene col 2061: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2061); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2061, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2061]; `tensor/DDL_lfc|DDL_z.npy` [2061]; `embed/gene_vectors.npy` [2061]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2061 or target_col == 2061). Every well: [[UQCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UQCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
