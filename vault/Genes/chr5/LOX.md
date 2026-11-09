---
symbol: "LOX"
type: "gene"
col: 3430
ensembl_id: "ENSG00000113083"
name: "lysyl oxidase"
location: "5q23.1"
module: 13
arm: "+"
pooled_cpm: 146.74
n_lines_expressing: 19
n_dd_up: 20
n_dd_down: 30
n_dd_up_clean: 18
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 40
direction_downstream: 55
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# LOX

*lysyl oxidase* — 5q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Budesonide (drug)]] 0.5 µM: 1.76× (z +6.2, q 3e-07, up in 15 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.412× (z -13.8, q 1e-40, down in 17 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTGFR]] (+0.76, fdr 7e-06), [[CA12]] (+0.73, fdr 7e-06), [[IRAK3]] (+0.66, fdr 7e-06); moves opposite to [[KIAA1549]] (-0.58, fdr 1e-05), [[TUSC3]] (-0.53, fdr 4e-05), [[AMIGO2]] (-0.50, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 40 arrows point to it, the strongest [[ABLIM3]] → it (grade B ⚠); 55 go from it, the strongest it → [[ATE1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3430.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 0.5 µM |  | **1.76×** | +6.2 | 3e-07 | 15/17 (HS-578T, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.70×** | +5.6 | 5e-06 | 14/18 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.64×** | +5.4 | 1e-05 | 9/17 (HS-578T, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.61×** | +5.2 | 2e-05 | 14/17 (HS-578T, H4, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +4.9 | 1e-04 | 1/18 (A498) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.58×** | +4.6 | 3e-04 | 15/16 (HS-578T, H4, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +4.6 | 3e-04 | 1/16 (HepG2/C3A) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.51×** | +4.5 | 4e-04 | 11/17 (HS-578T, NCI-H2347, …) | two highest doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.50×** | +4.5 | 5e-04 | 10/17 (HS-578T, H4, …) | all doses, flat | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.001 | 15/17 (NCI-H2347, H4, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.002 | 12/17 (HS-578T, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.005 | 13/17 (H4, HS-578T, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.010 | 15/17 (H4, HS-578T, …) | all doses, stronger at high dose |  |
| [[Econazole (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.017 | 14/17 (H4, HS-578T, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.023 | 11/17 (CFPAC-1, HOP62, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.025 | 10/19 (HS-578T, NCI-H2347, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.027 | 13/17 (HS-578T, H4, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3430.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.412×** | -13.8 | 1e-40 | 17/17 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.338×** | -11.5 | 4e-28 | 17/17 (H4, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.379×** | -10.7 | 2e-24 | 17/17 (H4, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.418×** | -9.6 | 1e-19 | 17/17 (H4, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.459×** | -8.6 | 1e-15 | 17/17 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.473×** | -8.2 | 1e-14 | 17/17 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.495×** | -7.7 | 8e-13 | 15/17 (H4, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.534×** | -6.9 | 4e-10 | 16/17 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.555×** | -6.5 | 5e-09 | 11/16 (H4, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.586×** | -5.9 | 2e-07 | 16/17 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.600×** | -5.6 | 9e-07 | 15/17 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.605×** | -5.5 | 1e-06 | 17/17 (H4, HOP62, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.605×** | -5.3 | 4e-06 | 15/16 (J82, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.618×** | -5.3 | 5e-06 | 16/17 (H4, SW 900, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.630×** | -5.1 | 1e-05 | 15/17 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.641×** | -4.9 | 3e-05 | 15/17 (J82, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.661×** | -4.6 | 2e-04 | 12/17 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.672×** | -4.4 | 4e-04 | 14/17 (CFPAC-1, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3430. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 760 | 0 | 25 (9 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0131× (z -31.9) |
| [[HOP62 (line)]] | alt | 720 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0394× (z -32.4) |
| [[CFPAC-1 (line)]] | alt | 175 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0587× (z -26.1) |
| [[NCI-H1792 (line)]] | alt | 1,051 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0885× (z -26.3) |
| [[SW 900 (line)]] | alt | 193 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0498× (z -28.8) |
| [[A-172 (line)]] | wt | 1,241 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0693× (z -26.0) |
| [[J82 (line)]] | alt | 250 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0989× (z -23.8) |
| [[SNU-423 (line)]] | alt | 272 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0600× (z -27.0) |
| [[HS-578T (line)]] | alt | 797 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -18.2) |
| [[hTERT-HPNE (line)]] | wt | 656 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 256 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -21.0) |
| [[HepG2_C3A (line)]] | wt | 94.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0745× (z -22.6) |
| [[NCI-H2347 (line)]] | alt | 41.4 | 1 | 5 | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 3.71× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -20.2) |
| [[Hs 766T (line)]] | wt | 45.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -14.1) |
| [[SW 1088 (line)]] | alt | 896 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0396× (z -18.3) |
| [[CHP-212 (line)]] | wt | 55.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 6.16 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.99 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.36 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.32 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.94 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.44 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.83 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.58 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.34 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.2 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.32 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 27.9 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.62 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.34 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.05 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.21 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3430), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGFR]] | +0.76 | +0.76 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[CA12]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 416 |
| [[IRAK3]] | +0.66 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ADAMTS2]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 | pathway: Collagen formation; STRING 750 |
| [[GPR173]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[TRAM2]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[COL6A3]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 441 |
| [[DCN]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 616 |
| [[TLR2]] | +0.59 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ITGA8]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 | pathway: Elastic fibre formation |
| [[PRR16]] | +0.58 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[PCBP3]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1549]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[TUSC3]] | -0.53 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[AMIGO2]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[CSF2]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[BEND7]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ZNF704]] | -0.46 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[PATJ]] | -0.45 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[MAP7]] | -0.45 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[ATE1]] | -0.45 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[STAU2]] | -0.45 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[CRACD]] | -0.44 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[EIF4G3]] | -0.44 | -0.54 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 6, C 34. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABLIM3]] | B | ABLIM3 activity raises LOX's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 5.28× lower at baseline in the lines without ABLIM3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[TUSC3]] | B | TUSC3 activity raises LOX's level | lines that do not express TUSC3 (17) vs lines expressing it (33) | 4.61× lower at baseline in the lines without TUSC3 | 0.060 | ⚠ within organs, on part of the lines; also absent: MAP9, BVES-AS1, RNF150; its own permutation p |
| [[PATJ]] | B | PATJ activity lowers LOX's level | lines that do not express PATJ (9) vs lines expressing it (41) | 3.82× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[LPAR1]] | B | LPAR1 activity raises LOX's level | lines that do not express LPAR1 (15) vs lines expressing it (35) | 4.83× lower at baseline in the lines without LPAR1 | 0.078 | ⚠ within organs, on part of the lines; also absent: SVEP1, PAPSS2, TOX2 |
| [[CRACD]] | B | CRACD activity lowers LOX's level | lines that do not express CRACD (12) vs lines expressing it (38) | 5.03× higher at baseline in the lines without CRACD | 0.099 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[EHD2]] | B | EHD2 activity raises LOX's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 4.03× lower at baseline in the lines without EHD2 | 0.0996 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |
| [[CA12]] | C | CA12 activity raises LOX's level | lines that do not express CA12 (29) vs lines expressing it (21) | 7.83× lower at baseline in the lines without CA12 | 0.001 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; co-absent with the target |
| [[GPR173]] | C | GPR173 activity raises LOX's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 9.67× lower at baseline in the lines without GPR173 | 0.002 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises LOX's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 11.28× lower at baseline in the lines without COL5A1 | 0.002 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[PTGFR]] | C | PTGFR activity raises LOX's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 9.30× lower at baseline in the lines without PTGFR | 0.005 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; co-absent with the target |
| [[TNS1]] | C | TNS1 activity raises LOX's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 4.82× lower at baseline in the lines without TNS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786; co-absent with the target |
| [[TLR2]] | C | TLR2 activity raises LOX's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 4.10× lower at baseline in the lines without TLR2 | 0.008 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA; co-absent with the target |

### Downstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 24, C 31. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATE1]] | B | LOX activity lowers ATE1's level | lines that do not express LOX (31) vs lines expressing it (19) | 1.82× higher at baseline in the lines without LOX | 8e-04 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[KIAA1549]] | B | LOX activity lowers KIAA1549's level | lines that do not express LOX (31) vs lines expressing it (19) | 1.99× higher at baseline in the lines without LOX | 0.007 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[LPAR1]] | B | LOX activity raises LPAR1's level | lines that do not express LOX (31) vs lines expressing it (19) | 3.96× lower at baseline in the lines without LOX | 0.010 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[ATE1]] | B | LOX activity weakens ATE1's drug response | lines that do not express LOX (31) vs lines expressing it (18) | the lines without LOX respond 1.66× as strongly (z diff -1.19); strongest at Panobinostat 5 µM: 0.58x vs 0.94x (z diff -4.5) | 0.013 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; target measured in part of the lines; artifact flags |
| [[B4GALT6]] | B | LOX activity lowers B4GALT6's level | lines that do not express LOX (31) vs lines expressing it (19) | 1.65× higher at baseline in the lines without LOX | 0.015 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[TMEM92-AS1]] | B | LOX activity raises TMEM92-AS1's level | lines that do not express LOX (31) vs lines expressing it (19) | 3.12× lower at baseline in the lines without LOX | 0.019 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[THEMIS2]] | B | LOX activity raises THEMIS2's level | lines that do not express LOX (31) vs lines expressing it (19) | 2.51× lower at baseline in the lines without LOX | 0.020 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[ITGA5]] | B | LOX activity raises ITGA5's level | lines that do not express LOX (31) vs lines expressing it (19) | 3.79× lower at baseline in the lines without LOX | 0.022 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[EHD2]] | B | LOX activity raises EHD2's level | lines that do not express LOX (31) vs lines expressing it (19) | 3.84× lower at baseline in the lines without LOX | 0.022 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[NFIL3]] | B | LOX activity raises NFIL3's level | lines that do not express LOX (31) vs lines expressing it (19) | 2.06× lower at baseline in the lines without LOX | 0.023 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[LTBP1]] | B | LOX activity raises LTBP1's level | lines that do not express LOX (31) vs lines expressing it (19) | 2.60× lower at baseline in the lines without LOX | 0.024 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[ABLIM3]] | B | LOX activity raises ABLIM3's level | lines that do not express LOX (31) vs lines expressing it (19) | 3.94× lower at baseline in the lines without LOX | 0.030 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.379). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.6, 20.5); signed map (27.3, 45.8). **Vector** length 124, 51.7% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Budesonide (drug)]] 0.5 µM |  | +4.1 | +6.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.8 | +5.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.7 | +5.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.6 | +5.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.3 | +3.9 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -4.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.6 | -6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -7.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | lysyl oxidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.1 — chr5:122,063,195-122,078,413 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Lysyl oxidase family |
| Hallmark sets | HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 5 pathways, smallest: Crosslinking of collagen fibrils; Elastic fibre formation; Assembly of collagen fibrils and other multimeric structures |
| Matched by | ensembl_id |

**Function**, from UniProt [P28300](https://www.uniprot.org/uniprotkb/P28300) (Protein-lysine 6-oxidase):

> Responsible for the post-translational oxidative deamination of peptidyl lysine residues in precursors to fibrous collagen and elastin. Regulator of Ras expression. May play a role in tumor suppression. Plays a role in the aortic wall architecture (By similarity).

**Summary**, from NCBI Gene [4015](https://www.ncbi.nlm.nih.gov/gene/4015):

> This gene encodes a member of the lysyl oxidase family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate a regulatory propeptide and the mature enzyme. The copper-dependent amine oxidase activity of this enzyme functions in the crosslinking of collagens and elastin, while the propeptide may play a role in tumor suppression. In addition, defects in this gene have been linked with …

**Accessions** — [HGNC:6664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6664) · Entrez [4015](https://www.ncbi.nlm.nih.gov/gene/4015) · UniProt [P28300](https://www.uniprot.org/uniprotkb/P28300) · Ensembl [ENSG00000113083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113083)

## Data

Gene col 3430: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3430); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3430, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3430]; `tensor/DDL_lfc|DDL_z.npy` [3430]; `embed/gene_vectors.npy` [3430]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3430 or target_col == 3430). Every well: [[LOX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LOX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
