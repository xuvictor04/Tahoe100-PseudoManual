---
symbol: "AKR1C3"
type: "gene"
col: 12137
ensembl_id: "ENSG00000196139"
name: "aldo-keto reductase family 1 member C3"
location: "10p15.1"
module: 117
arm: "+"
pooled_cpm: 19.21
n_lines_expressing: 31
n_dd_up: 37
n_dd_down: 9
n_dd_up_clean: 30
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 21
direction_downstream: 18
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# AKR1C3

*aldo-keto reductase family 1 member C3* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.96× (z +13.4, q 4e-38, up in 24 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.85× (z +6.0, q 4e-07, up in 18 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.542× (z -6.0, q 1e-06, down in 19 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKR1C2]] (+0.79, fdr 7e-06, ⚠ same locus), [[AKR1C1]] (+0.73, fdr 7e-06), [[GNGT1]] (+0.63, fdr 1e-05), [[ABCC2]] (+0.63, fdr 8e-06); moves opposite to [[DPY19L3]] (-0.59, fdr 1e-05), [[HMOX2]] (-0.53, fdr 3e-05), [[ODF2]] (-0.52, fdr 2e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[TRIM31]] → it (grade B ⚠); 18 go from it, the strongest it → [[ABCC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12137.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.96×** | +13.4 | 4e-38 | 24/27 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.88×** | +12.7 | 2e-34 | 13/18 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +6.0 | 4e-07 | 18/28 (LoVo, COLO 205, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +5.6 | 3e-06 | 14/23 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +5.6 | 3e-06 | 15/29 (KATO III, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.78×** | +5.4 | 8e-06 | 17/27 (HepG2/C3A, AsPC-1, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.74×** | +5.2 | 2e-05 | 18/27 (A549, HS-578T, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.9 | 7e-05 | 15/29 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.58×** | +4.5 | 4e-04 | 15/29 (SW480, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **2.29×** | +4.2 | 0.001 | 18/27 (HepG2/C3A, HT-29, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 0.002 | 16/29 (A498, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.51×** | +4.0 | 0.003 | 15/28 (HepG2/C3A, A498, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.004 | 14/28 (A549, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.005 | 15/29 (A498, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.006 | 15/29 (A549, A498, …) | all doses, flat |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.009 | 8/27 (LoVo, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[AZD-7648 (drug)]] 5 µM |  | **1.97×** | +3.4 | 0.017 | 13/27 (A498, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **1.89×** | +3.2 | 0.033 | 9/27 (J82, A498, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12137.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.542×** | -6.0 | 1e-06 | 19/28 (HepG2/C3A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.558×** | -5.7 | 2e-06 | 19/28 (HepG2/C3A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.559×** | -5.7 | 2e-06 | 19/27 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -5.2 | 3e-05 | 16/28 (COLO 205, SHP-77, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.641×** | -4.4 | 0.001 | 14/28 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.684×** | -3.7 | 0.018 | 17/28 (HepG2/C3A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.710×** | -3.4 | 0.060 | 14/28 (NCI-H2030, LS 180, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.717×** | -3.3 | 0.075 | 12/28 (HS-578T, A-172, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.793×** | -3.2 | 0.098 | 13/29 (NCI-H1573, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12137. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 88.2 | 1 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.96× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -16.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 38.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.64× (z +13.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 49.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +11.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 71.3 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0937× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 29.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -8.6) |
| [[HT-29 (line)]] | alt | 27.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 0.5 µM 4.18× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.239× (z -8.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 8.52 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.19× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 7.21 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 7.20× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 20.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0870× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 18.0 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 8.55× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 49.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -11.2) |
| [[A549 (line)]] | wt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +8.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 30.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -8.7) |
| [[KATO III (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 58.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -11.2) |
| [[A-172 (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12137), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKR1C2]] | +0.79 | +0.77 / +0.82 | both halves | 7e-06 | same gene group; pathway: HALLMARK_XENOBIOTIC_METABOLISM; STRING 997; ⚠ same locus (17.3 kb: neighbours can correlate without regulation) |
| [[AKR1C1]] | +0.73 | +0.73 / +0.73 | both halves | 7e-06 | same gene group; pathway: Bile acid and bile salt metabolism; STRING 995 |
| [[GNGT1]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 | pathway: Sensory Perception |
| [[ABCC2]] | +0.63 | +0.69 / +0.57 | both halves | 8e-06 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[CYP4F3]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 | pathway: Arachidonate metabolism |
| [[EGF]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 | pathway: Signaling by Nuclear Receptors |
| [[CAPS2]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ZSCAN31]] | +0.58 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TRIM16L]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[NMRAL2P-1]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[RBM47]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ADGRV1]] | +0.56 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[MID1]] | +0.55 | +0.58 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L3]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[HMOX2]] | -0.53 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ODF2]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[CTNNBIP1]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[MTMR14]] | -0.51 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[SPATA33]] | -0.51 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[RASA2]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[RAPGEF3]] | -0.50 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[MPP3]] | -0.50 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[USP20]] | -0.50 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[CERS5]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ZMYND19]] | -0.49 | -0.35 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 16, C 5. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM31]] | B | TRIM31 activity raises AKR1C3's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 3.20× lower at baseline in the lines without TRIM31 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[MGST1]] | B | MGST1 activity raises AKR1C3's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 3.19× lower at baseline in the lines without MGST1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[RBM47]] | B | RBM47 activity raises AKR1C3's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.92× lower at baseline in the lines without RBM47 | 0.013 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[WDR72]] | B | WDR72 activity raises AKR1C3's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.38× lower at baseline in the lines without WDR72 | 0.013 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2 |
| [[GCNT2]] | B | GCNT2 activity raises AKR1C3's level | lines that do not express GCNT2 (16) vs lines expressing it (34) | 2.57× lower at baseline in the lines without GCNT2 | 0.024 | ⚠ within organs, on part of the lines; also absent: WBP2NL, LOXL2, CSF3 |
| [[CYP4F3]] | B | CYP4F3 activity raises AKR1C3's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.52× lower at baseline in the lines without CYP4F3 | 0.027 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[HGD]] | B | HGD activity raises AKR1C3's level | lines that do not express HGD (15) vs lines expressing it (35) | 2.41× lower at baseline in the lines without HGD | 0.028 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[RASSF6]] | B | RASSF6 activity raises AKR1C3's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.77× lower at baseline in the lines without RASSF6 | 0.030 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[AKR1B10]] | B | AKR1B10 activity raises AKR1C3's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 4.33× lower at baseline in the lines without AKR1B10 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[SPP1]] | B | SPP1 activity raises AKR1C3's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 3.16× lower at baseline in the lines without SPP1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG |
| [[TSHZ2]] | B | TSHZ2 activity raises AKR1C3's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.33× lower at baseline in the lines without TSHZ2 | 0.063 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[PDK4]] | B | PDK4 activity raises AKR1C3's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 2.38× lower at baseline in the lines without PDK4 | 0.067 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 13, C 5. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCC2]] | B | AKR1C3 activity raises ABCC2's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.52× lower at baseline in the lines without AKR1C3 | 0.008 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[RASSF6]] | B | AKR1C3 activity raises RASSF6's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.87× lower at baseline in the lines without AKR1C3 | 0.012 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[HGD]] | B | AKR1C3 activity raises HGD's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without AKR1C3 | 0.018 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[AKR1B10]] | B | AKR1C3 activity raises AKR1B10's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.32× lower at baseline in the lines without AKR1C3 | 0.026 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[CYP4F3]] | B | AKR1C3 activity raises CYP4F3's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.40× lower at baseline in the lines without AKR1C3 | 0.034 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[TRIM31]] | B | AKR1C3 activity raises TRIM31's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.32× lower at baseline in the lines without AKR1C3 | 0.041 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[RHOU]] | B | AKR1C3 activity raises RHOU's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 1.94× lower at baseline in the lines without AKR1C3 | 0.043 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[ETS2]] | B | AKR1C3 activity raises ETS2's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.27× lower at baseline in the lines without AKR1C3 | 0.055 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[ALDH3A1]] | B | AKR1C3 activity raises ALDH3A1's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without AKR1C3 | 0.057 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| cells under [[Pimitespib (drug)]] 5 µM | B | AKR1C3 activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express AKR1C3 (19) vs lines expressing it (29) | the lines without AKR1C3: 1.24× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[GCLC]] | B | AKR1C3 activity raises GCLC's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 1.83× lower at baseline in the lines without AKR1C3 | 0.077 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[ALDH3B1]] | B | AKR1C3 activity raises ALDH3B1's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 1.96× lower at baseline in the lines without AKR1C3 | 0.090 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.4, 48.6); signed map (52.0, -9.0). **Vector** length 74.8, 19.7% of its response variance represented; |z| ≥ 3 in 706 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +12.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.7 | +5.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.7 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.5 | -3.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | aldo-keto reductase family 1 member C3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.1 — chr10:5,035,354-5,107,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0119, DDX, HAKRB, PGFS; previously HSD17B5 |
| Gene groups (HGNC) | Aldo-keto reductases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 18 pathways, smallest: Synthesis of bile acids and bile salts via 27-hydroxycholesterol; Synthesis of bile acids and bile salts via 24-hydroxycholesterol; Synthesis of Prostaglandins (PG) and Thromboxanes (TX) |
| Matched by | ensembl_id |

**Function**, from UniProt [P42330](https://www.uniprot.org/uniprotkb/P42330) (Aldo-keto reductase family 1 member C3):

> Cytosolic aldo-keto reductase that catalyzes NADPH-dependent reduction of ketosteroids to hydroxysteroids. Displays broad substrate specificity with distinct positional and stereochemistry, primarily generating 17beta-hydroxysteroids, but also 3alpha- and 20alpha-hydroxysteroids. Produces potent androgens via classical and 'backdoor'/alternative pathways. In the classical androgen metabolic pathway (biosynthesis of 5alpha-dihydrotestosterone (5alpha-DHT) via testosterone), catalyzes the …

**Summary**, from NCBI Gene [8644](https://www.ncbi.nlm.nih.gov/gene/8644):

> This gene encodes a member of the aldo/keto reductase superfamily, which consists of more than 40 known enzymes and proteins. These enzymes catalyze the conversion of aldehydes and ketones to their corresponding alcohols by utilizing NADH and/or NADPH as cofactors. The enzymes display overlapping but distinct substrate specificity. This enzyme catalyzes the reduction of prostaglandin (PG) D2, PGH2 and phenanthrenequinone (PQ), and the oxidation of 9alpha,11beta-PGF2 to PGD2. It may play an …

**Accessions** — [HGNC:386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:386) · Entrez [8644](https://www.ncbi.nlm.nih.gov/gene/8644) · UniProt [P42330](https://www.uniprot.org/uniprotkb/P42330) · Ensembl [ENSG00000196139](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196139)

## Data

Gene col 12137: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12137); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12137, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12137]; `tensor/DDL_lfc|DDL_z.npy` [12137]; `embed/gene_vectors.npy` [12137]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12137 or target_col == 12137). Every well: [[AKR1C3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKR1C3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
