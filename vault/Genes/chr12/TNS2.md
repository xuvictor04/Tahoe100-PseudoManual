---
symbol: "TNS2"
type: "gene"
col: 3192
ensembl_id: "ENSG00000111077"
name: "tensin 2"
location: "12q13.13"
module: 98
arm: "+"
pooled_cpm: 7.5
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 38
n_dd_up_clean: 12
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# TNS2

*tensin 2* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 1.84× (z +6.2, q 3e-07, up in 23 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.332× (z -11.2, q 4e-26, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLF9]] (+0.69, fdr 7e-06), [[JPH2]] (+0.66, fdr 1e-05), [[CCND3]] (+0.64, fdr 7e-06); moves opposite to [[PKIA]] (-0.53, fdr 3e-05), [[DOP1B]] (-0.53, fdr 1e-05), [[FRMD5]] (-0.52, fdr 1e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3192.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.84×** | +6.2 | 3e-07 | 23/44 (A498, SW 900, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.80×** | +5.6 | 6e-06 | 23/45 (PANC-1, A498, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.1 | 5e-05 | 6/15 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 5 µM |  | **1.63×** | +4.9 | 1e-04 | 17/47 (PANC-1, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.60×** | +4.8 | 2e-04 | 20/45 (PANC-1, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.64×** | +4.6 | 3e-04 | 17/42 (A549, PANC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.55×** | +4.4 | 7e-04 | 19/46 (SW 900, PANC-1, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.48×** | +4.0 | 0.005 | 17/45 (PANC-1, SW 900, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.009 | 19/46 (PANC-1, A498, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +3.6 | 0.015 | 5/20 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.016 | 15/42 (A498, CFPAC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +3.5 | 0.019 | 11/28 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.059 | 13/45 (PANC-1, SW 900, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.059 | 19/46 (SW 900, PANC-1, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.077 | 18/45 (A498, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3192.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.332×** | -11.2 | 4e-26 | 38/47 (HT-29, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.335×** | -11.1 | 6e-26 | 33/46 (HT-29, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.366×** | -10.2 | 6e-22 | 34/46 (HS-578T, HT-29, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.383×** | -9.7 | 5e-20 | 34/45 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.386×** | -9.6 | 9e-20 | 35/48 (HT-29, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.511×** | -9.6 | 1e-19 | 31/40 (HT-29, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.398×** | -9.3 | 1e-18 | 29/41 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.428×** | -8.6 | 7e-16 | 28/45 (C32, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.434×** | -8.4 | 2e-15 | 33/45 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.452×** | -8.0 | 6e-14 | 29/36 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.473×** | -7.6 | 2e-12 | 29/45 (HepG2/C3A, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.475×** | -7.1 | 6e-11 | 26/44 (NCI-H460, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.564×** | -5.8 | 3e-07 | 25/46 (SW 900, HT-29, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.672×** | -5.7 | 6e-07 | 22/47 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.574×** | -5.6 | 9e-07 | 22/45 (C32, LS 180, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.576×** | -5.2 | 6e-06 | 22/47 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.611×** | -4.8 | 6e-05 | 19/45 (C32, SNU-423, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3192. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 20.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -15.4) |
| [[SW480 (line)]] | alt | 10.1 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0738× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.207× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 12.7 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -11.6) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.244× (z -9.6) |
| [[Hs 766T (line)]] | wt | 18.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -14.6) |
| [[C32 (line)]] | wt | 31.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 17.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0327× (z -16.0) |
| [[NCI-H2030 (line)]] | alt | 6.08 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0826× (z -9.6) |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0819× (z -9.8) |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0803× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0861× (z -8.9) |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0531× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.109× (z -9.6) |
| [[H4 (line)]] | wt | 9.55 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0409× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 8.56 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0497× (z -10.2) |
| [[HS-578T (line)]] | alt | 3.96 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0341× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0846× (z -8.6) |
| [[J82 (line)]] | alt | 7.03 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0984× (z -10.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 3.01 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0653× (z -9.9) |
| [[LS 180 (line)]] | wt | 3.95 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0584× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 4.89 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0787× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 6.31 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 5.25 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.129× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 6.20 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0555× (z -8.5) |
| [[SW1417 (line)]] | alt | 3.81 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0723× (z -8.9) |
| [[A-172 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3192), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF9]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[JPH2]] | +0.66 | +0.55 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[CCND3]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[MAOA]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[NNMT]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[BCL9L]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[IRAK3]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 | same gene group |
| [[COPS8]] | +0.60 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ITGA10]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PDZD2]] | +0.60 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[FKBP5]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 | same gene group |
| [[TLR2]] | +0.59 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKIA]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[DOP1B]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[FRMD5]] | -0.52 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[MMP1]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[SLAMF7]] | -0.49 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[GALNT12]] | -0.48 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[BTBD9]] | -0.48 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[LINC02220]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[TMEM158]] | -0.48 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[NRIP3]] | -0.47 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ADAMTS16]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[CALB2]] | -0.47 | -0.41 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises TNS2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.0% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[NNMT]] | B | NNMT activity raises TNS2's level | lines that do not express NNMT (24) vs lines expressing it (26) | 1.71× lower at baseline in the lines without NNMT | 0.025 | ⚠ within organs, on part of the lines; also absent: KC6, DPYSL3, ENSG00000230615 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.0, 16.5); signed map (17.9, 30.6). **Vector** length 75.3, 14.8% of its response variance represented; |z| ≥ 3 in 1,306 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | +5.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.3 | +4.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.3 | +2.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.2 | +4.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.2 | +6.2 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.5 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -8.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.5 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | tensin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,046,969-53,064,379 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1075, C1-TEN; previously TENC1 |
| Gene groups (HGNC) | SH2 domain containing; C2 tensin-type domain containing; PTEN protein phosphatases; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q63HR2](https://www.uniprot.org/uniprotkb/Q63HR2) (Tensin-2):

> Tyrosine-protein phosphatase which regulates cell motility, proliferation and muscle-response to insulin. Phosphatase activity is mediated by binding to phosphatidylinositol-3,4,5-triphosphate (PtdIns(3,4,5)P3) via the SH2 domain. In muscles and under catabolic conditions, dephosphorylates IRS1 leading to its degradation and muscle atrophy. Negatively regulates PI3K-AKT pathway activation. Dephosphorylates nephrin NPHS1 in podocytes which regulates activity of the mTORC1 complex. Under normal …

**Summary**, from NCBI Gene [23371](https://www.ncbi.nlm.nih.gov/gene/23371):

> The protein encoded by this gene belongs to the tensin family. Tensin is a focal adhesion molecule that binds to actin filaments and participates in signaling pathways. This protein plays a role in regulating cell migration. Alternative splicing occurs at this locus and three transcript variants encoding three distinct isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19737](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19737) · Entrez [23371](https://www.ncbi.nlm.nih.gov/gene/23371) · UniProt [Q63HR2](https://www.uniprot.org/uniprotkb/Q63HR2) · Ensembl [ENSG00000111077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111077)

## Data

Gene col 3192: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3192); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3192, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3192]; `tensor/DDL_lfc|DDL_z.npy` [3192]; `embed/gene_vectors.npy` [3192]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3192 or target_col == 3192). Every well: [[TNS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
