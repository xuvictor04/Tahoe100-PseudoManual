---
symbol: "SNX21"
type: "gene"
col: 4479
ensembl_id: "ENSG00000124104"
name: "sorting nexin family member 21"
location: "20q13.12"
module: 7
arm: "+"
pooled_cpm: 8.18
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 26
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SNX21

*sorting nexin family member 21* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Belumosudil (drug)]] 5 µM: 1.48× (z +4.4, q 0.006, up in 15 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.251× (z -22.8, q 0e+00, down in 39 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TANGO2]] (+0.57, fdr 1e-05), [[TMEM234]] (+0.54, fdr 3e-05), [[USP35]] (+0.54, fdr 3e-05); moves opposite to [[ANK3]] (-0.55, fdr 3e-05), [[CCSER1]] (-0.53, fdr 3e-05), [[ARHGEF38]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC02331]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4479.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **1.48×** | +4.4 | 0.006 | 15/44 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |
| [[Alpelisib (drug)]] 5 µM |  | 1.68× | +3.2 | 0.28 | 2/36 (SK-MEL-2, C-33 A) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.32× | +3.1 | 0.28 | 13/43 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.32× | +3.1 | 0.28 | 3/16 (A498, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4479.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.251×** | -22.8 | 0e+00 | 39/43 (SNU-423, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.252×** | -15.5 | 0e+00 | 39/45 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.431×** | -13.9 | 9e-42 | 32/42 (MIA PaCa-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.306×** | -13.8 | 2e-41 | 34/41 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.336×** | -12.8 | 3e-35 | 39/47 (SW 900, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.411×** | -10.4 | 3e-23 | 31/41 (SW 900, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.446×** | -9.4 | 3e-19 | 33/47 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.447×** | -9.4 | 4e-19 | 30/47 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.459×** | -9.1 | 5e-18 | 30/46 (NCI-H460, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.507×** | -7.9 | 1e-13 | 27/46 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.541×** | -7.2 | 4e-11 | 23/45 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.562×** | -6.7 | 8e-10 | 27/45 (SNU-423, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.594×** | -5.8 | 2e-07 | 16/34 (J82, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.592×** | -5.8 | 3e-07 | 21/47 (HS-578T, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.623×** | -5.3 | 4e-06 | 18/41 (MIA PaCa-2, SW480, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.490×** | -4.4 | 4e-04 | 14/40 (MIA PaCa-2, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.694×** | -4.3 | 6e-04 | 17/46 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.546×** | -3.7 | 0.006 | 11/45 (NCI-H460, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.723×** | -3.6 | 0.007 | 9/47 (MIA PaCa-2, HS-578T, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.744×** | -3.5 | 0.014 | 13/45 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.833×** | -3.0 | 0.059 | 14/46 (RPMI-7951, NCI-H2347, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.624×** | -2.9 | 0.088 | 8/40 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4479. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 39.2 | 0 | 14 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0825× (z -25.3) |
| [[NCI-H460 (line)]] | wt | 8.51 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -16.7) |
| [[RPMI-7951 (line)]] | alt | 26.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -15.7) |
| [[A-172 (line)]] | wt | 15.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0978× (z -16.7) |
| [[HS-578T (line)]] | alt | 14.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0618× (z -19.5) |
| [[J82 (line)]] | alt | 8.96 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0974× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.132× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -15.9) |
| [[PANC-1 (line)]] | alt | 8.02 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -14.2) |
| [[SNU-423 (line)]] | alt | 13.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0438× (z -20.8) |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 6.43 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0552× (z -10.6) |
| [[C32 (line)]] | wt | 9.32 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -9.4) |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 5.22 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.122× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0868× (z -11.2) |
| [[A549 (line)]] | wt | 3.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0797× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 7.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 4.85 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -9.2) |
| [[HOP62 (line)]] | alt | 4.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -11.7) |
| [[HT-29 (line)]] | alt | 3.27 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0544× (z -9.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 6.53 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0506× (z -11.0) |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -8.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW480 (line)]] | alt | 4.11 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -9.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-427 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4479), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TANGO2]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TMEM234]] | +0.54 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[USP35]] | +0.54 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[UBE2Q2P1-1]] | +0.54 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[BRMS1]] | +0.54 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[ASB6]] | +0.52 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[TBC1D13]] | +0.52 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[TRIP4]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[CPTP]] | +0.51 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[FCHSD1]] | +0.50 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[HARS2]] | +0.50 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[SNTA1]] | +0.49 | +0.56 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANK3]] | -0.55 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[CCSER1]] | -0.53 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ARHGEF38]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TMTC2]] | -0.48 | -0.38 / -0.41 | both halves | 6e-05 | same gene group |
| [[SLC12A2]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[LINC02331]] | -0.47 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[RAPGEF5]] | -0.47 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[PRSS12]] | -0.46 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[SIDT1]] | -0.46 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[NPSR1-AS1]] | -0.46 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[NFIA]] | -0.46 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[PLCH1]] | -0.46 | -0.53 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02331]] | B | LINC02331 activity lowers SNX21's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 1.68× higher at baseline in the lines without LINC02331 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[ARHGEF38]] | B | ARHGEF38 activity lowers SNX21's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 1.76× higher at baseline in the lines without ARHGEF38 | 0.081 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.358). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-51.7, -2.7); signed map (-10.6, -24.6). **Vector** length 57.5, 8.75% of its response variance represented; |z| ≥ 3 in 1,187 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | -1.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | -1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +1.8 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +4.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | -22.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.6 | -3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -2.6 | -4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -13.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.4 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin family member 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,833,799-45,843,276 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ337O18.4, SNX-L; previously C20orf161 |
| Gene groups (HGNC) | Sorting nexins; Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969T3](https://www.uniprot.org/uniprotkb/Q969T3) (Sorting nexin-21):

> Binds to membranes enriched in phosphatidylinositol 3-phosphate (PtdIns(P3)) and phosphatidylinositol 4,5-bisphosphate. May be involved in several stages of intracellular trafficking.

**Summary**, from NCBI Gene [90203](https://www.ncbi.nlm.nih.gov/gene/90203):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This protein does not contain a coiled coil region, like some family members. The specific function of this protein has not been determined. Multiple transcript variants encoding distinct isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16154) · Entrez [90203](https://www.ncbi.nlm.nih.gov/gene/90203) · UniProt [Q969T3](https://www.uniprot.org/uniprotkb/Q969T3) · Ensembl [ENSG00000124104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124104)

## Data

Gene col 4479: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4479); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4479, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4479]; `tensor/DDL_lfc|DDL_z.npy` [4479]; `embed/gene_vectors.npy` [4479]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4479 or target_col == 4479). Every well: [[SNX21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
