---
symbol: "ETV1"
type: "gene"
col: 113
ensembl_id: "ENSG00000006468"
name: "ETS variant transcription factor 1"
location: "7p21.2"
module: 92
arm: "+"
pooled_cpm: 46.65
n_lines_expressing: 39
n_dd_up: 6
n_dd_down: 64
n_dd_up_clean: 1
n_dd_down_clean: 57
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# ETV1

*ETS variant transcription factor 1* — 7p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.83× (z +7.6, q 2e-11, up in 28 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.38× (z +5.7, q 2e-06, up in 18 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 3.07×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 1.54×; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 3.30×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).
> Pooled over the cell lines (median), lowered significantly by 64 drug-doses (7 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.142× (z -22.3, q 0e+00, down in 37 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETV4]] (+0.74, fdr 7e-06), [[SPRED1]] (+0.72, fdr 7e-06), [[EXTL2]] (+0.68, fdr 1e-05); moves opposite to [[RAB32]] (-0.50, fdr 3e-05), [[CLIP1]] (-0.49, fdr 3e-05), [[MAP4]] (-0.48, fdr 3e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SLC16A6]] → it (grade B ⚠); 8 go from it, the strongest it → [[ARSG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 113.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 3.07×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 1.54×; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 3.30×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.83×** | +7.6 | 2e-11 | 28/35 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.75×** | +6.8 | 3e-09 | 19/29 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +5.7 | 2e-06 | 18/37 (SW1417, J82, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.29×** | +4.5 | 8e-04 | 18/37 (SW1417, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.47×** | +4.5 | 8e-04 | 12/31 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.40×** | +4.2 | 0.002 | 17/37 (A498, RKO, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.3 | 0.088 | 11/37 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.28× | +3.2 | 0.11 | 13/37 (RPMI-7951, J82, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.27× | +3.0 | 0.15 | 12/37 (A498, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 65 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 64 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 113.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.142×** | -22.3 | 0e+00 | 37/38 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.198×** | -19.4 | 0e+00 | 35/36 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.218×** | -18.3 | 0e+00 | 35/37 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.238×** | -17.6 | 0e+00 | 36/37 (SW480, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.344×** | -16.5 | 0e+00 | 36/37 (SW480, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.267×** | -16.5 | 0e+00 | 35/38 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.299×** | -15.1 | 0e+00 | 35/37 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.353×** | -13.0 | 1e-36 | 33/37 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.335×** | -12.0 | 2e-31 | 36/37 (H4, SW 900, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.509×** | -11.7 | 1e-29 | 33/37 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.515×** | -11.7 | 1e-29 | 32/37 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.386×** | -10.9 | 3e-26 | 31/37 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.137×** | -9.9 | 2e-21 | 33/37 (SW480, C32, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.452×** | -9.9 | 2e-21 | 33/36 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.465×** | -9.5 | 7e-20 | 31/37 (SK-MEL-2, H4, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.478×** | -9.2 | 2e-18 | 31/37 (NCI-H23, H4, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.483×** | -9.1 | 5e-18 | 29/37 (SW480, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 113. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 105 | 0 | 34 (8 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.0224× (z -37.1) |
| [[PANC-1 (line)]] | alt | 25.9 | 0 | 24 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -18.6) |
| [[C32 (line)]] | wt | 162 | 0 | 23 (2 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.0510× (z -27.5) |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 0 | 21 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.262× (z -29.6) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.0432× (z -18.8) |
| [[SHP-77 (line)]] | alt | 128 | 0 | 21 (3 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.150× (z -18.8) |
| [[SW 900 (line)]] | alt | 315 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0969× (z -22.5) |
| [[NCI-H2030 (line)]] | alt | 75.6 | 0 | 18 (2 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.143× (z -16.4) |
| [[SK-MEL-2 (line)]] | alt | 92.8 | 1 (1 ⚠) | 17 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.07× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Trametinib (drug)]] 5 µM 0.117× (z -17.7) |
| [[H4 (line)]] | wt | 97.0 | 0 | 17 (4 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0367× (z -19.9) |
| [[NCI-H460 (line)]] | wt | 133 | 0 | 17 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0689× (z -17.7) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0956× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 97.1 | 0 | 15 (3 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0547× (z -20.4) |
| [[NCI-H23 (line)]] | alt | 50.7 | 1 (1 ⚠) | 12 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.54× (z +9.5) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.0998× (z -21.1) |
| [[CFPAC-1 (line)]] | alt | 32.0 | 0 | 12 | — | [[Binimetinib (drug)]] 0.5 µM 0.131× (z -15.2) |
| [[HEC-1-A (line)]] | alt | 24.6 | 1 (1 ⚠) | 11 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Binimetinib (drug)]] 0.5 µM 0.191× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 25.2 | 0 | 12 (1 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.112× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 92.7 | 0 | 10 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0959× (z -17.7) |
| [[HOP62 (line)]] | alt | 35.2 | 0 | 9 | — | [[Cobimetinib (drug)]] 5 µM 0.0586× (z -18.2) |
| [[SW 1271 (line)]] | alt | 124 | 0 | 9 (1 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.0272× (z -18.5) |
| [[A498 (line)]] | wt | 16.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -12.2) |
| [[SNU-423 (line)]] | alt | 32.1 | 0 | 6 | — | [[Trametinib (drug)]] 5 µM 0.104× (z -12.3) |
| [[AN3 CA (line)]] | alt | 84.1 | 0 | 5 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0998× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 44.5 | 0 | 4 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0892× (z -14.3) |
| [[HS-578T (line)]] | alt | 26.8 | 0 | 3 | — | [[Cobimetinib (drug)]] 5 µM 0.122× (z -11.2) |
| [[RKO (line)]] | wt | 16.4 | 0 | 3 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.114× (z -10.1) |
| [[J82 (line)]] | alt | 11.9 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.189× (z -9.0) |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 2 | — | [[Binimetinib (drug)]] 0.5 µM 0.245× (z -9.0) |
| [[A-427 (line)]] | wt | 26.8 | 0 | 1 | — | [[Binimetinib (drug)]] 5 µM 0.171× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.9) |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0388× (z -18.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 134 | 0 | 1 | — | [[Binimetinib (drug)]] 5 µM 0.281× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.101× (z -9.7) |
| [[A-172 (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.94 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.58 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.31 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.39 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.82 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 113), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETV4]] | +0.74 | +0.70 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[SPRED1]] | +0.72 | +0.70 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[EXTL2]] | +0.68 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[ITGB5]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[STAMBPL1]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SPRED2]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[MAML3]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[SPRY4]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 | STRING 472 |
| [[DUSP6]] | +0.64 | +0.65 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 409 |
| [[WWTR1]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[NPAS2]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SPRY2]] | +0.62 | +0.65 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB32]] | -0.50 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[CLIP1]] | -0.49 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[MAP4]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[PHYKPL]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[CRYAB]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[NUTM2A-AS1]] | -0.46 | -0.33 / -0.56 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A6]] | B | SLC16A6 activity raises ETV1's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 2.52× lower at baseline in the lines without SLC16A6 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7 |
| [[MAP2K1]] | B | MAP2K1 activity raises ETV1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 9.2% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ETV1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ROR1]] | B | ROR1 activity raises ETV1's level | lines that do not express ROR1 (14) vs lines expressing it (36) | 2.06× lower at baseline in the lines without ROR1 | 0.081 | ⚠ within organs, on part of the lines |
| [[GNG11]] | B | GNG11 activity raises ETV1's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 2.95× lower at baseline in the lines without GNG11 | 0.094 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN |
| [[NUTM2A-AS1]] | C | NUTM2A-AS1 activity lowers ETV1's level | lines that do not express NUTM2A-AS1 (4) vs lines expressing it (46) | 4.50× higher at baseline in the lines without NUTM2A-AS1 | 0.043 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ISG15, ENSG00000285257, BIRC3; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARSG]] | B | ETV1 activity raises ARSG's level | lines that do not express ETV1 (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without ETV1 | 0.051 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136 |
| [[PTPN14]] | B | ETV1 activity strengthens PTPN14's drug response | lines that do not express ETV1 (11) vs lines expressing it (37) | the lines without ETV1 respond 0.76× as strongly (z diff +1.82); strongest at Ixazomib citrate 5 µM: 0.88x vs 0.65x (z diff +4.0) | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136; target measured in part of the lines; artifact flags |
| [[SLC16A6]] | B | ETV1 activity raises SLC16A6's level | lines that do not express ETV1 (11) vs lines expressing it (39) | 2.36× lower at baseline in the lines without ETV1 | 0.059 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136 |
| [[ZFPM2-AS1]] | B | ETV1 activity raises ZFPM2-AS1's level | lines that do not express ETV1 (11) vs lines expressing it (39) | 3.40× lower at baseline in the lines without ETV1 | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136 |
| [[MILR1]] | B | ETV1 activity raises MILR1's level | lines that do not express ETV1 (11) vs lines expressing it (39) | 2.02× lower at baseline in the lines without ETV1 | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136 |
| [[HMGA2]] | B | ETV1 activity raises HMGA2's level | lines that do not express ETV1 (11) vs lines expressing it (39) | 3.26× lower at baseline in the lines without ETV1 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136 |
| [[EGR3]] | B | ETV1 activity strengthens EGR3's drug response | lines that do not express ETV1 (10) vs lines expressing it (29) | the lines without ETV1 respond 0.72× as strongly (z diff +1.66); strongest at Trametinib 0.05 µM: 0.52x vs 0.33x (z diff +2.6) | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136; target measured in part of the lines; artifact flags |
| [[LINC02454]] | C | ETV1 activity raises LINC02454's level | lines that do not express ETV1 (11) vs lines expressing it (39) | 2.37× lower at baseline in the lines without ETV1 | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136; co-absent with the target |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.3, 6.9); signed map (9.1, 48.1). **Vector** length 138, 44.1% of its response variance represented; |z| ≥ 3 in 1,652 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MAPK family signaling cascades* (reactome, mean cos +0.55 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.4 | +4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +3.5 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.3 | +4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | +2.1 | +1.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -11.7 | -22.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -10.9 | -16.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -10.0 | -18.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -9.8 | -16.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -9.8 | -17.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -8.6 | -19.4 |

## What is on record

|  |  |
|---|---|
| Name | ETS variant transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.2 — chr7:13,891,229-13,991,425 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ER81 |
| Gene groups (HGNC) | ETS transcription factor family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [P50549](https://www.uniprot.org/uniprotkb/P50549) (ETS translocation variant 1):

> Transcriptional activator that binds to DNA sequences containing the consensus pentanucleotide 5'-CGGA[AT]-3'. Required for olfactory dopaminergic neuron differentiation; may directly activate expression of tyrosine hydroxylase (TH) (By similarity).

**Summary**, from NCBI Gene [2115](https://www.ncbi.nlm.nih.gov/gene/2115):

> This gene encodes a member of the ETS (E twenty-six) family of transcription factors. The ETS proteins regulate many target genes that modulate biological processes like cell growth, angiogenesis, migration, proliferation and differentiation. All ETS proteins contain an ETS DNA-binding domain that binds to DNA sequences containing the consensus 5'-CGGA[AT]-3'. The protein encoded by this gene contains a conserved short acidic transactivation domain (TAD) in the N-terminal region, in addition to …

**Accessions** — [HGNC:3490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3490) · Entrez [2115](https://www.ncbi.nlm.nih.gov/gene/2115) · UniProt [P50549](https://www.uniprot.org/uniprotkb/P50549) · Ensembl [ENSG00000006468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006468)

## Data

Gene col 113: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 113); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 113, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 113]; `tensor/DDL_lfc|DDL_z.npy` [113]; `embed/gene_vectors.npy` [113]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 113 or target_col == 113). Every well: [[ETV1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETV1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
