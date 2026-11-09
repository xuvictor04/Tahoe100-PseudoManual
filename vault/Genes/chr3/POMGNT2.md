---
symbol: "POMGNT2"
type: "gene"
col: 6908
ensembl_id: "ENSG00000144647"
name: "protein O-linked mannose N-acetylglucosaminyltransferase 2 (beta 1,4-)"
location: "3p22.1"
module: 30
arm: "+"
pooled_cpm: 5.95
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# POMGNT2

*protein O-linked mannose N-acetylglucosaminyltransferase 2 (beta 1,4-)* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.60× (z +6.7, q 8e-09, up in 19 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.455× (z -16.0, q 0e+00, down in 34 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAF5L]] (+0.74, fdr 7e-06), [[POGLUT2]] (+0.71, fdr 7e-06), [[WASF3]] (+0.70, fdr 1e-05); moves opposite to [[LINC01004]] (-0.67, fdr 1e-05), [[AKT1S1]] (-0.66, fdr 1e-05), [[GGPS1]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6908.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +6.7 | 8e-09 | 19/46 (NCI-H2347, HOP62, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +6.7 | 8e-09 | 21/46 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +5.9 | 8e-07 | 18/45 (NCI-H2347, LS 180, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +5.6 | 3e-06 | 16/40 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +5.3 | 2e-05 | 16/46 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +5.2 | 2e-05 | 13/43 (NCI-H23, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.6 | 4e-04 | 12/46 (NCI-H2347, PANC-1, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.23×** | +4.1 | 0.003 | 9/46 (RKO, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.066 | 7/42 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.05 µM |  | 1.24× | +3.1 | 0.11 | 4/46 (HOP62, A-427, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6908.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.455×** | -16.0 | 0e+00 | 34/41 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.346×** | -14.6 | 0e+00 | 37/44 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.409×** | -12.8 | 3e-35 | 29/39 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.465×** | -11.0 | 7e-26 | 25/39 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.481×** | -10.5 | 1e-23 | 28/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.514×** | -9.5 | 2e-19 | 25/46 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.551×** | -8.5 | 1e-15 | 26/45 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.613×** | -7.0 | 2e-10 | 14/24 (HEC-1-A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.596×** | -6.9 | 4e-10 | 9/15 (SW1417, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.631×** | -6.3 | 1e-08 | 17/33 (HEC-1-A, SHP-77, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.649×** | -6.2 | 3e-08 | 19/45 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.673×** | -5.7 | 7e-07 | 19/45 (A-172, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.673×** | -5.4 | 2e-06 | 7/12 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.778×** | -5.1 | 1e-05 | 15/47 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -3.8 | 0.006 | 12/38 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.771×** | -3.6 | 0.012 | 8/42 (SNU-423, LoVo, …) | top dose only |  |
| [[Pyridoxine (drug)]] 0.05 µM |  | **0.807×** | -3.1 | 0.070 | 4/45 (Hs 766T, CHP-212, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.801×** | -3.1 | 0.071 | 5/46 (LoVo, NCI-H2347, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6908. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.27 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0877× (z -15.5) |
| [[SW480 (line)]] | alt | 7.42 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.215× (z -11.0) |
| [[C32 (line)]] | wt | 5.15 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0931× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 16.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.9) |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0748× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.0928× (z -8.8) |
| [[HOP62 (line)]] | alt | 3.30 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -12.5) |
| [[KATO III (line)]] | alt | 9.54 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 2.93 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0746× (z -11.1) |
| [[PANC-1 (line)]] | alt | 3.66 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -15.9) |
| [[LS 180 (line)]] | wt | 6.57 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0838× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 12.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -14.7) |
| [[A498 (line)]] | wt | 3.10 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0561× (z -12.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 3.82 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0879× (z -11.4) |
| [[J82 (line)]] | alt | 5.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 3.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 3.62 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -8.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 10.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.246× (z -9.2) |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0883× (z -12.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6908), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF5L]] | +0.74 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[POGLUT2]] | +0.71 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[WASF3]] | +0.70 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[SEMA4F]] | +0.70 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[FAM104A]] | +0.70 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[ABHD10]] | +0.69 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[SKP2]] | +0.69 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[LRFN3]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[GRB2]] | +0.68 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.68 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[MFSD9]] | +0.67 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01004]] | -0.67 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[AKT1S1]] | -0.66 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[GGPS1]] | -0.66 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.66 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[C11orf58]] | -0.66 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[XIAP]] | -0.65 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[ST7L]] | -0.64 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[CHMP4A]] | -0.64 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[GTF2H1]] | -0.64 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[BAZ2B]] | -0.64 | -0.64 / -0.40 | both halves | 4e-05 |  |
| [[ANGPT2]] | -0.63 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[TIA1]] | -0.63 | -0.59 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers POMGNT2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers POMGNT2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HACE1]] | C | HACE1 activity raises POMGNT2's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.34× lower at baseline in the lines without HACE1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[IL17RD]] | C | IL17RD activity raises POMGNT2's level | lines that do not express IL17RD (4) vs lines expressing it (46) | 1.53× lower at baseline in the lines without IL17RD | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PRKAG2, ZNF391, FAM89A; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.670). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-0.9, -3.9); signed map (-38.2, -7.9). **Vector** length 75.1, 12.4% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +2.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +5.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +2.8 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.7 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | -0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.1 | -16.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -14.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -11.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.1 | -10.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.0 | -8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -5.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.5 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | protein O-linked mannose N-acetylglucosaminyltransferase 2 (beta 1,4-) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:43,079,229-43,106,085 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14566, AGO61; previously C3orf39, GTDC2 |
| Gene groups (HGNC) | O-linked N-acetylglucosaminyltransferases |
| Reactome | 3 pathways, smallest: DAG1 core M3 glycosylations; DAG1 glycosylations; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NAT1](https://www.uniprot.org/uniprotkb/Q8NAT1) (Protein O-linked-mannose beta-1,4-N-acetylglucosaminyltransferase 2):

> O-linked mannose beta-1,4-N-acetylglucosaminyltransferase that transfers UDP-N-acetyl-D-glucosamine to the 4-position of the mannose to generate N-acetyl-D-glucosamine-beta-1,4-O-D-mannosylprotein. Involved in the biosynthesis of the phosphorylated O-mannosyl trisaccharide (N-acetylgalactosamine-beta-3-N-acetylglucosamine-beta-4-(phosphate-6-)mannose), a carbohydrate structure present in alpha-dystroglycan (DAG1), which is required for binding laminin G-like domain-containing extracellular …

**Summary**, from NCBI Gene [84892](https://www.ncbi.nlm.nih.gov/gene/84892):

> This gene encodes a protein with glycosyltransferase activity although its function is not currently known. [provided by RefSeq, Sep 2012]

**Accessions** — [HGNC:25902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25902) · Entrez [84892](https://www.ncbi.nlm.nih.gov/gene/84892) · UniProt [Q8NAT1](https://www.uniprot.org/uniprotkb/Q8NAT1) · Ensembl [ENSG00000144647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144647)

## Data

Gene col 6908: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6908); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6908, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6908]; `tensor/DDL_lfc|DDL_z.npy` [6908]; `embed/gene_vectors.npy` [6908]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6908 or target_col == 6908). Every well: [[POMGNT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POMGNT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
