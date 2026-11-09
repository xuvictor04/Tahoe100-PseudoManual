---
symbol: "SEMA3B"
type: "gene"
col: 253
ensembl_id: "ENSG00000012171"
name: "semaphorin 3B"
location: "3p21.31"
module: 31
arm: "+"
pooled_cpm: 53.03
n_lines_expressing: 31
n_dd_up: 11
n_dd_down: 39
n_dd_up_clean: 7
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 50
direction_downstream: 76
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# SEMA3B

*semaphorin 3B* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.61× (z +6.9, q 2e-09, up in 10 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.54× (z +6.0, q 3e-07, up in 21 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (12 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.691× (z -7.6, q 2e-11, down in 24 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYBG2]] (+0.77, fdr 7e-06), [[JUP]] (+0.73, fdr 7e-06), [[LSMEM2]] (+0.72, fdr 7e-06, ⚠ read-through risk), [[RDH13]] (+0.71, fdr 7e-06); moves opposite to [[ECHDC1]] (-0.50, fdr 6e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 50 arrows point to it, the strongest [[RNF39]] → it (grade B ⚠); 76 go from it, the strongest it → [[LSMEM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 253.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +6.9 | 2e-09 | 10/29 (C32, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +6.8 | 3e-09 | 9/25 (HepG2/C3A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.54×** | +6.0 | 3e-07 | 21/28 (H4, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +5.0 | 9e-05 | 12/29 (HOP62, HCT15, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 9e-04 | 16/28 (H4, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +4.3 | 0.002 | 9/28 (CHP-212, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.1 | 0.004 | 6/23 (HepG2/C3A, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.0 | 0.004 | 5/24 (C32, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.007 | 7/30 (LS 180, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.44×** | +3.8 | 0.010 | 9/28 (C32, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.048 | 9/29 (LS 180, HT-29, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.23× | +3.1 | 0.11 | 10/29 (LoVo, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 253.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.691×** | -7.6 | 2e-11 | 24/29 (SW48, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.608×** | -7.2 | 2e-10 | 18/28 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.633×** | -6.6 | 7e-09 | 19/29 (LoVo, H4, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.643×** | -6.4 | 2e-08 | 22/29 (AsPC-1, SW48, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.754×** | -5.8 | 9e-07 | 18/29 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.688×** | -5.4 | 6e-06 | 21/29 (SW48, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.693×** | -5.3 | 9e-06 | 18/29 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.695×** | -5.3 | 1e-05 | 19/29 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.699×** | -5.2 | 1e-05 | 19/28 (MIA PaCa-2, HT-29, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.722×** | -4.7 | 1e-04 | 18/29 (SW48, AsPC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.732×** | -4.5 | 3e-04 | 18/28 (CFPAC-1, SW48, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.733×** | -4.5 | 3e-04 | 13/29 (SW48, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.741×** | -4.4 | 6e-04 | 16/28 (AsPC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.745×** | -4.3 | 8e-04 | 18/29 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.752×** | -4.1 | 0.001 | 17/30 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.754×** | -4.1 | 0.002 | 17/29 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.768×** | -3.8 | 0.004 | 9/29 (HS-578T, CFPAC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.783×** | -3.4 | 0.017 | 15/29 (NCI-H2347, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 253. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 344 | 0 | 12 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0549× (z -18.5) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.245× (z -12.7) |
| [[HT-29 (line)]] | alt | 71.8 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -20.2) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.229× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 55.2 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -13.7) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -13.4) |
| [[LoVo (line)]] | wt | 63.4 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -13.6) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 44.9 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -18.1) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.318× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 227 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -19.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.392× (z -9.0) |
| [[SW1417 (line)]] | alt | 493 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -16.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.409× (z -9.5) |
| [[SW480 (line)]] | alt | 54.7 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -15.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.324× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 267 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0750× (z -27.4) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0743× (z -19.5) |
| [[LS 180 (line)]] | wt | 91.2 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -10.5) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -8.6) |
| [[HCT15 (line)]] | alt | 102 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -14.1) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -11.5) |
| [[A-172 (line)]] | wt | 29.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.273× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[BT-474 (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.7) ⚠ cell-cycle shift, explains ~88% of this change |
| [[H4 (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0922× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[Panc 03.27 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.2) ⚠ cell-cycle shift, explains ~88% of this change |
| [[SK-MEL-2 (line)]] | alt | 29.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.343× (z -9.1) |
| [[A-427 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 13.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.00 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.24 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.94 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.63 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.03 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.70 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.17 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 13.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 253), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYBG2]] | +0.77 | +0.75 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[JUP]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[LSMEM2]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 | ⚠ **readthrough risk**: LSMEM2 lies 1.5 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[RDH13]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[EPS8L1]] | +0.70 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[DENND2C]] | +0.69 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[GJB3]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[TTC9]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[TMC6]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[FA2H]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[RHOF]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[HS3ST1]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECHDC1]] | -0.50 | -0.44 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 44, C 6. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF39]] | B | RNF39 activity raises SEMA3B's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 4.08× lower at baseline in the lines without RNF39 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[MYO5B]] | B | MYO5B activity raises SEMA3B's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 3.33× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[ANO1]] | B | ANO1 activity raises SEMA3B's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 3.49× lower at baseline in the lines without ANO1 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[PRSS8]] | B | PRSS8 activity raises SEMA3B's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 4.03× lower at baseline in the lines without PRSS8 | 0.003 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises SEMA3B's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.05× lower at baseline in the lines without TMPRSS4 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[GJB3]] | B | GJB3 activity raises SEMA3B's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.87× lower at baseline in the lines without GJB3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[INAVA]] | B | INAVA activity raises SEMA3B's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.43× lower at baseline in the lines without INAVA | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[FAM83B]] | B | FAM83B activity raises SEMA3B's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.25× lower at baseline in the lines without FAM83B | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[ITGB4]] | B | ITGB4 activity raises SEMA3B's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.00× lower at baseline in the lines without ITGB4 | 0.006 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[SULT2B1]] | B | SULT2B1 activity raises SEMA3B's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 3.15× lower at baseline in the lines without SULT2B1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[C1orf116]], [[IRF6]] | B | C1orf116, IRF6 activity raises SEMA3B's level | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (19) | 3.82× lower at baseline in the lines without C1orf116, IRF6 | 0.006 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[GRB7]] | B | GRB7 activity raises SEMA3B's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 3.00× lower at baseline in the lines without GRB7 | 0.006 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |

### Downstream of this gene

*76 arrows, 76 of them with an alert ⚠; grade A 0, B 71, C 5. Shown: the 12 strongest; 64 more arrows (64 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSMEM2]] | B | SEMA3B activity raises LSMEM2's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.74× lower at baseline in the lines without SEMA3B | 2e-04 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[PPARD]] | B | SEMA3B activity raises PPARD's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.24× lower at baseline in the lines without SEMA3B | 0.001 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[EPS8L2]] | B | SEMA3B activity raises EPS8L2's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without SEMA3B | 0.002 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[ATG9B]] | B | SEMA3B activity raises ATG9B's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.22× lower at baseline in the lines without SEMA3B | 0.004 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[DEF6]] | B | SEMA3B activity raises DEF6's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.66× lower at baseline in the lines without SEMA3B | 0.004 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[UNC13D]] | B | SEMA3B activity raises UNC13D's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.56× lower at baseline in the lines without SEMA3B | 0.008 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[GJB3]] | B | SEMA3B activity raises GJB3's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.26× lower at baseline in the lines without SEMA3B | 0.009 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[CLDN4]] | B | SEMA3B activity raises CLDN4's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.86× lower at baseline in the lines without SEMA3B | 0.010 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[SERINC2]] | B | SEMA3B activity raises SERINC2's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.18× lower at baseline in the lines without SEMA3B | 0.011 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[EZR]] | B | SEMA3B activity raises EZR's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without SEMA3B | 0.012 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[MYO18A]] | B | SEMA3B activity raises MYO18A's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.69× lower at baseline in the lines without SEMA3B | 0.012 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[GRB7]] | B | SEMA3B activity raises GRB7's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.22× lower at baseline in the lines without SEMA3B | 0.013 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.4, 56.1); signed map (-1.1, 37.4). **Vector** length 101, 29.5% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of the cornified envelope* (reactome, mean cos +0.51 to 9); *Keratinization* (reactome, mean cos +0.51 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.3 | +3.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.3 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | -5.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.3 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -5.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.9 | -7.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,267,558-50,277,546 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SemA, semaV, LUCA-1, sema5; previously SEMAA |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Semaphorins; MicroRNA protein coding host genes |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, KRAS_SIGNALING_UP, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13214](https://www.uniprot.org/uniprotkb/Q13214) (Semaphorin-3B):

> Inhibits axonal extension by providing local signals to specify territories inaccessible for growing axons.

**Summary**, from NCBI Gene [7869](https://www.ncbi.nlm.nih.gov/gene/7869):

> The protein encoded by this gene belongs to the class-3 semaphorin/collapsin family, whose members function in growth cone guidance during neuronal development. This family member inhibits axonal extension and has been shown to act as a tumor suppressor by inducing apoptosis. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:10724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10724) · Entrez [7869](https://www.ncbi.nlm.nih.gov/gene/7869) · UniProt [Q13214](https://www.uniprot.org/uniprotkb/Q13214) · Ensembl [ENSG00000012171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012171)

## Data

Gene col 253: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 253); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 253, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 253]; `tensor/DDL_lfc|DDL_z.npy` [253]; `embed/gene_vectors.npy` [253]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 253 or target_col == 253). Every well: [[SEMA3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
