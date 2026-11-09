---
symbol: "SH2B2"
type: "gene"
col: 8406
ensembl_id: "ENSG00000160999"
name: "SH2B adaptor protein 2"
location: "7q22.1"
module: 85
arm: "+"
pooled_cpm: 10.11
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 37
n_dd_up_clean: 4
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# SH2B2

*SH2B adaptor protein 2* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 1.54× (z +6.8, q 5e-09, up in 21 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.315× (z -17.4, q 0e+00, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFYVE28]] (+0.70, fdr 1e-05), [[PLA2G15]] (+0.69, fdr 1e-05), [[SLC66A2]] (+0.67, fdr 2e-05); moves opposite to [[DECR1]] (-0.69, fdr 4e-05), [[RIPK2-DT]] (-0.66, fdr 1e-05), [[AHI1-DT]] (-0.63, fdr 4e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KIF26A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8406.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +6.8 | 5e-09 | 21/44 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +5.6 | 6e-06 | 17/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.004 | 16/48 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.012 | 13/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.19 | 4/42 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.22× | +3.1 | 0.20 | 9/44 (C-33 A, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8406.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.315×** | -17.4 | 0e+00 | 37/46 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.477×** | -16.4 | 0e+00 | 34/45 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.446×** | -12.6 | 3e-34 | 27/34 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.472×** | -11.8 | 9e-30 | 30/43 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.470×** | -10.9 | 1e-25 | 20/25 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.509×** | -10.6 | 4e-24 | 30/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.583×** | -8.4 | 3e-15 | 28/48 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.581×** | -8.2 | 2e-14 | 16/20 (MIA PaCa-2, J82, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.605×** | -7.8 | 3e-13 | 28/44 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.595×** | -7.8 | 3e-13 | 26/46 (NCI-H23, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.392×** | -7.7 | 9e-13 | 27/47 (RKO, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.718×** | -7.3 | 1e-11 | 26/48 (J82, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.623×** | -7.1 | 5e-11 | 24/46 (MIA PaCa-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.635×** | -7.1 | 6e-11 | 23/46 (C32, KATO III, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.644×** | -6.6 | 1e-09 | 21/40 (C32, NCI-H23, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.659×** | -6.5 | 3e-09 | 17/47 (C32, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.678×** | -6.1 | 4e-08 | 23/46 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.682×** | -6.0 | 8e-08 | 21/45 (C32, A-172, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.696×** | -5.7 | 5e-07 | 23/46 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[NG25 (drug)]] 5 µM |  | **0.517×** | -5.4 | 2e-06 | 15/41 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8406. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.1 | 0 | 8 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0507× (z -18.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.171× (z -16.4) |
| [[C32 (line)]] | wt | 28.2 | 0 | 8 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0292× (z -22.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0314× (z -19.8) |
| [[NCI-H460 (line)]] | wt | 9.04 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -11.3) |
| [[A498 (line)]] | wt | 10.0 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.167× (z -9.7) |
| [[HOP62 (line)]] | alt | 18.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.180× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -10.7) |
| [[J82 (line)]] | alt | 10.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 11.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -10.4) |
| [[A-427 (line)]] | wt | 10.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0952× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 7.50 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0308× (z -18.2) |
| [[RKO (line)]] | wt | 16.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -15.6) |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -10.2) |
| [[SNU-423 (line)]] | alt | 9.12 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0715× (z -12.0) |
| [[SW48 (line)]] | wt | 15.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -11.2) |
| [[A549 (line)]] | wt | 7.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -9.9) |
| [[BT-474 (line)]] | alt | 8.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -8.8) |
| [[C-33 A (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -8.8) |
| [[CHP-212 (line)]] | wt | 14.6 | 0 | 1 | — | [[Zileuton (drug)]] 0.5 µM 0.0455× (z -8.9) |
| [[KATO III (line)]] | alt | 3.48 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 5 µM 0.0674× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 8.21 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0831× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 8.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -8.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0507× (z -11.6) |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -8.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8406), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE28]] | +0.70 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[PLA2G15]] | +0.69 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[SLC66A2]] | +0.67 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[GFOD2]] | +0.66 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.65 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[GPR157]] | +0.65 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[XYLT2]] | +0.65 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[ANKRD13D]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[CORO7]] | +0.64 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[MAST3]] | +0.64 | +0.65 / +0.32 | both halves | 2e-04 |  |
| [[PBX4]] | +0.63 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[SH3GL1]] | +0.63 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | -0.69 | -0.62 / -0.40 | both halves | 4e-05 |  |
| [[RIPK2-DT]] | -0.66 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[AHI1-DT]] | -0.63 | -0.58 / -0.24 | both halves | 4e-04 |  |
| [[CASC9]] | -0.62 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[UFL1-AS1]] | -0.61 | -0.55 / -0.29 | both halves | 2e-04 |  |
| [[TSGA10]] | -0.61 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[ERCC6L2-AS1]] | -0.61 | -0.64 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[ZSCAN30]] | -0.61 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ACADM]] | -0.61 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[AMMECR1]] | -0.61 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[BCLAF1]] | -0.61 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[TIA1]] | -0.61 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[PSME3IP1]] | -0.60 | -0.56 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF26A]] | B | KIF26A activity raises SH2B2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.56× lower at baseline in the lines without KIF26A | 0.005 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[HDAC6]] | B | HDAC6 activity lowers SH2B2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CFL2]] | C | CFL2 activity raises SH2B2's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 2.01× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.694). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.5, -0.3); signed map (-29.3, 17.5). **Vector** length 84.3, 16.4% of its response variance represented; |z| ≥ 3 in 1,142 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.4 | +6.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +5.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | +3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.5 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.1 | +0.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -17.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -11.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.1 | -12.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.0 | -7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | SH2B adaptor protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:102,285,091-102,321,711 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APS |
| Gene groups (HGNC) | Pleckstrin homology domain containing; SH2 domain containing; MicroRNA protein coding host genes; SH2B adaptor protein family |
| Hallmark sets | COAGULATION |
| Reactome | 5 pathways, smallest: Regulation of KIT signaling; Signaling by SCF-KIT; Factors involved in megakaryocyte development and platelet production |
| Matched by | ensembl_id |

**Function**, from UniProt [O14492](https://www.uniprot.org/uniprotkb/O14492) (SH2B adapter protein 2):

> Adapter protein for several members of the tyrosine kinase receptor family. Involved in multiple signaling pathways. May be involved in coupling from immunoreceptor to Ras signaling. Acts as a negative regulator of cytokine signaling in collaboration with CBL. Binds to EPOR and suppresses EPO-induced STAT5 activation, possibly through a masking effect on STAT5 docking sites in EPOR. Suppresses PDGF-induced mitogenesis. May induce cytoskeletal reorganization via interaction with VAV3.

**Summary**, from NCBI Gene [10603](https://www.ncbi.nlm.nih.gov/gene/10603):

> The protein encoded by this gene is expressed in B lymphocytes and contains pleckstrin homology and src homology 2 (SH2) domains. In Burkitt's lymphoma cell lines, it is tyrosine-phosphorylated in response to B cell receptor stimulation. Because it binds Shc independent of stimulation and Grb2 after stimulation, it appears to play a role in signal transduction from the receptor to the Shc/Grb2 pathway. [provided by RefSeq, Jun 2009]

**Accessions** — [HGNC:17381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17381) · Entrez [10603](https://www.ncbi.nlm.nih.gov/gene/10603) · UniProt [O14492](https://www.uniprot.org/uniprotkb/O14492) · Ensembl [ENSG00000160999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160999)

## Data

Gene col 8406: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8406); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8406, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8406]; `tensor/DDL_lfc|DDL_z.npy` [8406]; `embed/gene_vectors.npy` [8406]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8406 or target_col == 8406). Every well: [[SH2B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH2B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
