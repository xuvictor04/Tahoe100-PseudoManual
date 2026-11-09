---
symbol: "LDLRAP1"
type: "gene"
col: 8119
ensembl_id: "ENSG00000157978"
name: "low density lipoprotein receptor adaptor protein 1"
location: "1p36.11"
module: 2
arm: "+"
pooled_cpm: 10.8
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# LDLRAP1

*low density lipoprotein receptor adaptor protein 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.99× (z +10.4, q 1e-22, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.603× (z -10.8, q 2e-24, down in 25 of 42 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.265× (z -10.5, q 2e-23, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNMT3B]] (+0.64, fdr 1e-05), [[PEDS1]] (+0.63, fdr 1e-05), [[TBC1D24]] (+0.63, fdr 1e-05); moves opposite to [[LEKR1]] (-0.62, fdr 3e-05), [[GTF2H1]] (-0.62, fdr 1e-05), [[USP40]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8119.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +10.4 | 1e-22 | 34/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.79×** | +8.8 | 4e-16 | 32/46 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +6.8 | 2e-09 | 26/46 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +6.7 | 2e-09 | 27/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +5.4 | 7e-06 | 20/46 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +3.7 | 0.018 | 6/46 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.26×** | +3.5 | 0.032 | 9/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.11 | 13/43 (LoVo, H4, …) | rises with dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.23× | +3.1 | 0.11 | 8/41 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 1.28× | +3.0 | 0.14 | 7/43 (CFPAC-1, H4, …) | rises with dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8119.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.603×** | -10.8 | 2e-24 | 25/42 (HS-578T, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.265×** | -10.5 | 2e-23 | 38/45 (RPMI-7951, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.318×** | -9.1 | 2e-17 | 29/42 (RPMI-7951, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.558×** | -7.2 | 1e-10 | 27/44 (HS-578T, RPMI-7951, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.626×** | -7.1 | 2e-10 | 26/42 (RPMI-7951, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.652×** | -6.5 | 1e-08 | 24/44 (AsPC-1, HOP62, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.658×** | -6.3 | 2e-08 | 21/36 (NCI-H2030, HEC-1-A, …) | two highest doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.666×** | -6.2 | 5e-08 | 24/44 (SW480, RPMI-7951, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.702×** | -5.3 | 6e-06 | 24/46 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.603×** | -4.0 | 0.004 | 7/19 (SW480, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.780×** | -3.7 | 0.009 | 19/45 (A498, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.739×** | -3.7 | 0.010 | 13/22 (HOP62, LoVo, …) | two highest doses | composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.643×** | -3.5 | 0.021 | 7/41 (RPMI-7951, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.805×** | -3.3 | 0.045 | 15/45 (NCI-H1573, NCI-H460, …) | rises with dose | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.861× | -3.2 | 0.053 | 5/46 (A549, AsPC-1, …) | top dose only | position effect removed |
| [[Clofarabine (drug)]] 0.05 µM |  | **0.803×** | -3.1 | 0.080 | 10/43 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 26.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0837× (z -13.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0231× (z -10.6) |
| [[A-172 (line)]] | wt | 9.62 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -11.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[LoVo (line)]] | wt | 17.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[NCI-H1573 (line)]] | alt | 6.01 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0449× (z -13.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H460 (line)]] | wt | 5.34 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.3) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -12.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A498 (line)]] | wt | 8.30 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.0) ⚠ cell-cycle shift, explains ~48% of this change |
| [[AsPC-1 (line)]] | alt | 8.70 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0647× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.227× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 26.3 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.113× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0926× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HepG2_C3A (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0950× (z -10.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0682× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HS-578T (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -14.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HT-29 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[NCI-H2030 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0851× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -9.2) ⚠ cell-cycle shift, explains ~48% of this change |
| [[Panc 03.27 (line)]] | alt | 8.97 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0468× (z -11.5) |
| [[SW480 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNMT3B]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PEDS1]] | +0.63 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[TBC1D24]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[TPST2]] | +0.63 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[TMEM184B]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[CCNQ]] | +0.62 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[GNA12]] | +0.62 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[TNK2]] | +0.62 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[RIMS3]] | +0.61 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.60 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[MIIP]] | +0.60 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[SPRYD3]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEKR1]] | -0.62 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[GTF2H1]] | -0.62 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[USP40]] | -0.60 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[WAKMAR2]] | -0.58 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[PRORP]] | -0.57 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[ATP5PB]] | -0.57 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[LINC00174]] | -0.56 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[KRR1]] | -0.56 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[AFG1L]] | -0.55 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[METTL6]] | -0.55 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[PDCL3P4]] | -0.55 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[RBM23]] | -0.54 | -0.53 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers LDLRAP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers LDLRAP1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RTN4R]] | C | RTN4R activity raises LDLRAP1's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without RTN4R | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |
| [[PBX4]] | C | PBX4 activity raises LDLRAP1's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 2.33× lower at baseline in the lines without PBX4 | 0.047 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.657). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (2.5, 3.7); signed map (-41.7, -6.1). **Vector** length 74.4, 12.9% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +8.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.2 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +6.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.8 | +6.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | -0.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.5 | +0.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.7 | -10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -5.2 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.4 | -7.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.1 | -7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -6.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.8 | -0.6 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | low density lipoprotein receptor adaptor protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:25,543,606-25,568,886 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARH, ARH2, FHCB1, FHCB2, MGC34705, DKFZp586D0624 |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 16 pathways, smallest: Chylomicron clearance; Transport of RCbl within the body; Vitamin D (calciferol) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SW96](https://www.uniprot.org/uniprotkb/Q5SW96) (Low density lipoprotein receptor adapter protein 1):

> Adapter protein (clathrin-associated sorting protein (CLASP)) required for efficient endocytosis of the LDL receptor (LDLR) in polarized cells such as hepatocytes and lymphocytes, but not in non-polarized cells (fibroblasts). May be required for LDL binding and internalization but not for receptor clustering in coated pits. May facilitate the endocytosis of LDLR and LDLR-LDL complexes from coated pits by stabilizing the interaction between the receptor and the structural components of the pits. …

**Summary**, from NCBI Gene [26119](https://www.ncbi.nlm.nih.gov/gene/26119):

> The protein encoded by this gene is a cytosolic protein which contains a phosphotyrosine binding (PTD) domain. The PTD domain has been found to interact with the cytoplasmic tail of the LDL receptor. Mutations in this gene lead to LDL receptor malfunction and cause the disorder autosomal recessive hypercholesterolaemia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18640](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18640) · Entrez [26119](https://www.ncbi.nlm.nih.gov/gene/26119) · UniProt [Q5SW96](https://www.uniprot.org/uniprotkb/Q5SW96) · Ensembl [ENSG00000157978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157978)

## Data

Gene col 8119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8119); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8119]; `tensor/DDL_lfc|DDL_z.npy` [8119]; `embed/gene_vectors.npy` [8119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8119 or target_col == 8119). Every well: [[LDLRAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LDLRAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
