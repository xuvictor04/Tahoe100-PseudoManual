---
symbol: "LIX1L"
type: "gene"
col: 15689
ensembl_id: "ENSG00000271601"
name: "limb and CNS expressed 1 like"
location: "1q21.1"
module: 79
arm: "+"
pooled_cpm: 37.71
n_lines_expressing: 38
n_dd_up: 1
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 13
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# LIX1L

*limb and CNS expressed 1 like* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.23× (z +4.0, q 0.037, up in 10 of 29 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 2.12×, NCI-H1792 2.15×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.470× (z -14.9, q 0e+00, down in 30 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSBP2]] (+0.60, fdr 1e-05), [[BBS2]] (+0.58, fdr 2e-05), [[AKR7A2]] (+0.58, fdr 3e-05); moves opposite to [[DNTTIP2]] (-0.63, fdr 1e-05), [[HMGA1P4]] (-0.62, fdr 3e-05), [[ALOX12P2-1]] (-0.59, fdr 1e-04).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ACTR3C]] → it (grade B ⚠); 13 go from it, the strongest it → [[KLHL2P1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15689.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 2.12×, NCI-H1792 2.15×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.0 | 0.037 | 10/29 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 5 µM |  | 1.20× | +3.6 | 0.098 | 10/36 (AsPC-1, SW 900, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | 1.19× | +3.5 | 0.099 | 16/36 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.15 | 9/36 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.17× | +3.1 | 0.15 | 8/36 (PANC-1, A-172, …) | inconsistent across doses | position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.15 | 6/36 (SHP-77, NCI-H23, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 1.17× | +3.1 | 0.15 | 9/36 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.15 | 8/36 (AsPC-1, A498, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15689.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.470×** | -14.9 | 0e+00 | 30/35 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.493×** | -13.9 | 9e-42 | 33/36 (HOP62, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.681×** | -10.7 | 1e-24 | 25/36 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.593×** | -10.3 | 1e-22 | 30/36 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.706×** | -9.7 | 3e-20 | 27/36 (hTERT-HPNE, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.712×** | -9.5 | 3e-19 | 20/35 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.626×** | -8.7 | 2e-16 | 28/36 (hTERT-HPNE, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.499×** | -7.2 | 6e-11 | 20/31 (J82, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.710×** | -6.8 | 8e-10 | 22/36 (HOP62, A-172, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.711×** | -6.5 | 6e-09 | 18/36 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -6.2 | 3e-08 | 23/36 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.778×** | -5.0 | 3e-05 | 17/36 (SNU-1, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.636×** | -4.7 | 1e-04 | 15/36 (HOP62, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.724×** | -4.5 | 2e-04 | 16/36 (AsPC-1, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.788×** | -4.5 | 2e-04 | 16/36 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.824×** | -3.8 | 0.004 | 12/36 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.820×** | -3.7 | 0.006 | 13/35 (RKO, LOX-IMVI, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.835× | -3.4 | 0.021 | 11/36 (SW 1271, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15689. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 59.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -18.1) |
| [[hTERT-HPNE (line)]] | wt | 54.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -12.2) |
| [[SW 900 (line)]] | alt | 69.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -16.8) |
| [[AsPC-1 (line)]] | alt | 52.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -20.7) |
| [[MIA PaCa-2 (line)]] | alt | 90.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -18.9) |
| [[PANC-1 (line)]] | alt | 42.1 | 1 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.12× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | [[Auranofin (drug)]] 5 µM 0.384× (z -11.3) |
| [[CHP-212 (line)]] | wt | 58.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -10.6) |
| [[H4 (line)]] | wt | 47.1 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.220× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.235× (z -9.4) |
| [[HS-578T (line)]] | alt | 37.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.323× (z -10.7) |
| [[J82 (line)]] | alt | 19.3 | 0 | 3 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0909× (z -9.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 68.9 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.341× (z -12.7) |
| [[C32 (line)]] | wt | 47.2 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.286× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 24.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 72.3 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.15× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -14.3) |
| [[NCI-H2030 (line)]] | alt | 61.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 56.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -14.0) |
| [[SNU-1 (line)]] | wt | 85.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -10.9) |
| [[SNU-423 (line)]] | alt | 41.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -12.6) |
| [[SW 1088 (line)]] | alt | 49.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0612× (z -8.6) |
| [[A-427 (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.320× (z -10.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 82.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 68.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.379× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 45.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 32.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.194× (z -11.6) |
| [[A-172 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.19 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.53 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.95 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 32.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15689), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSBP2]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[BBS2]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[AKR7A2]] | +0.58 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[IFT122]] | +0.58 | +0.65 / +0.36 | both halves | 9e-05 |  |
| [[CABIN1]] | +0.57 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[WDR54]] | +0.56 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[PIAS3]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TRAM2]] | +0.55 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[ARSK]] | +0.55 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[ALAD]] | +0.55 | +0.34 / +0.42 | both halves | 1e-04 |  |
| [[DDHD2]] | +0.55 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[PER1]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNTTIP2]] | -0.63 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[HMGA1P4]] | -0.62 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[ALOX12P2-1]] | -0.59 | -0.67 / -0.33 | both halves | 1e-04 |  |
| [[TMEM217]] | -0.58 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[ACTR3C]] | -0.56 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[CLCF1]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[SMCO2]] | -0.55 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[EIF5]] | -0.54 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[LINC00536]] | -0.54 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[ZNF189]] | -0.54 | -0.60 / -0.27 | both halves | 3e-04 |  |
| [[MRPL45P2]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[CLIP1]] | -0.53 | -0.59 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTR3C]] | B | ACTR3C activity lowers LIX1L's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 2.67× higher at baseline in the lines without ACTR3C | 0.039 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[MAP7]] | B | MAP7 activity lowers LIX1L's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 2.65× higher at baseline in the lines without MAP7 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[PIP4P2]] | C | PIP4P2 activity raises LIX1L's level | lines that do not express PIP4P2 (4) vs lines expressing it (46) | 4.85× lower at baseline in the lines without PIP4P2 | 0.066 | ⚠ few lines (4 vs 46); across organs; also absent: THEM4, MRPS30-DT; maybe low, not absent |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL2P1]] | B | LIX1L activity lowers KLHL2P1's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 2.16× higher at baseline in the lines without LIX1L | 0.002 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[VKORC1]] | B | LIX1L activity raises VKORC1's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 2.61× lower at baseline in the lines without LIX1L | 0.031 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[CNTROB]] | B | LIX1L activity raises CNTROB's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 1.59× lower at baseline in the lines without LIX1L | 0.035 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[WDR54]] | B | LIX1L activity raises WDR54's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 2.19× lower at baseline in the lines without LIX1L | 0.054 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[COPS8]] | B | LIX1L activity raises COPS8's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 1.50× lower at baseline in the lines without LIX1L | 0.060 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[PEX3]] | B | LIX1L activity raises PEX3's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 1.61× lower at baseline in the lines without LIX1L | 0.066 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[NOMO1]] | B | LIX1L activity raises NOMO1's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 1.34× lower at baseline in the lines without LIX1L | 0.068 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | LIX1L activity raises the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express LIX1L (10) vs lines expressing it (36) | the lines without LIX1L: 0.85× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[IFT172]] | B | LIX1L activity raises IFT172's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 1.59× lower at baseline in the lines without LIX1L | 0.082 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| cells under [[Filgotinib (drug)]] 0.05 µM | B | LIX1L activity raises the cells' numbers under Filgotinib 0.05 µM (protects the cells) | lines that do not express LIX1L (10) vs lines expressing it (36) | the lines without LIX1L: 0.81× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[HACE1]] | B | LIX1L activity raises HACE1's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 2.12× lower at baseline in the lines without LIX1L | 0.089 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | B | LIX1L activity lowers the cells' numbers under Vinblastine (sulfate) 5 µM (makes them more sensitive) | lines that do not express LIX1L (10) vs lines expressing it (36) | the lines without LIX1L: 1.15× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.476). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.0, 9.1); signed map (-35.8, 18.9). **Vector** length 91.6, 22.0% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.3 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +3.2 | -5.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.8 | +3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.0 | +3.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.9 | -13.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.8 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -10.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.3 | -7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -10.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -9.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | limb and CNS expressed 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:145,933,423-145,958,017 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC46719 |
| Matched by | ensembl_id |

UniProt [Q8IVB5](https://www.uniprot.org/uniprotkb/Q8IVB5) carries no function annotation.

**Summary**, from NCBI Gene [128077](https://www.ncbi.nlm.nih.gov/gene/128077):

> Predicted to be involved in autophagosome maturation. Predicted to act upstream of or within actin cytoskeleton organization; gene expression; and mitral valve development. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28715) · Entrez [128077](https://www.ncbi.nlm.nih.gov/gene/128077) · UniProt [Q8IVB5](https://www.uniprot.org/uniprotkb/Q8IVB5) · Ensembl [ENSG00000271601](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000271601)

## Data

Gene col 15689: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15689); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15689, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15689]; `tensor/DDL_lfc|DDL_z.npy` [15689]; `embed/gene_vectors.npy` [15689]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15689 or target_col == 15689). Every well: [[LIX1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIX1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
