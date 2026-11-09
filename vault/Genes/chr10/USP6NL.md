---
symbol: "USP6NL"
type: "gene"
col: 7283
ensembl_id: "ENSG00000148429"
name: "USP6 N-terminal like"
location: "10p14"
module: 8
arm: "+"
pooled_cpm: 100.75
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 44
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# USP6NL

*USP6 N-terminal like* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.86× (z +12.4, q 1e-32, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.391× (z -18.0, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.694× (z -7.3, q 4e-11, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST14]] (+0.62, fdr 1e-05), [[SPINT1]] (+0.61, fdr 2e-05), [[TJP2]] (+0.61, fdr 9e-06); moves opposite to [[PCYT1A]] (-0.50, fdr 5e-05), [[JMJD6]] (-0.50, fdr 3e-05), [[ZNF621]] (-0.50, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 44 arrows point to it, the strongest [[CLIC5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7283.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.86×** | +12.4 | 1e-32 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +10.6 | 8e-24 | 36/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.66×** | +10.2 | 4e-22 | 41/49 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +7.9 | 6e-13 | 31/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +7.4 | 1e-11 | 28/48 (A549, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.03×** | +7.4 | 2e-11 | 33/48 (SW48, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +6.9 | 4e-10 | 31/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +5.7 | 8e-07 | 28/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.0 | 0.004 | 21/48 (RKO, A549, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.013 | 21/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Folic acid (drug)]] 5 µM |  | 1.12× | +3.1 | 0.086 | 4/48 (SW48, KATO III, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.094 | 15/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.11× | +3.0 | 0.099 | 2/48 (RPMI-7951, SW48) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.17× | +3.0 | 0.099 | 15/49 (PANC-1, A-172, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7283.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.391×** | -18.0 | 0e+00 | 40/44 (LS 180, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.487×** | -14.4 | 3e-44 | 39/47 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.672×** | -7.4 | 4e-11 | 28/45 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.694×** | -7.3 | 4e-11 | 38/48 (Panc 03.27, SW48, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.803×** | -4.4 | 0.001 | 26/48 (LS 180, SW1417, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -4.2 | 0.002 | 1/50 (SNU-1) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.828×** | -3.8 | 0.012 | 22/48 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.875× | -3.8 | 0.012 | 21/49 (NCI-H2347, SW48, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.846× | -3.3 | 0.052 | 16/48 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~3% of this change | 0.853× | -3.2 | 0.082 | 21/46 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.798× | -3.1 | 0.10 | 15/48 (LoVo, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.799× | -3.0 | 0.10 | 13/48 (LS 180, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 0.748× | -3.0 | 0.10 | 15/48 (NCI-H2347, CHP-212, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7283. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 307 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -11.2) |
| [[SW48 (line)]] | wt | 272 | 2 | 7 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 11.6× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.270× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 187 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -18.2) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.409× (z -10.1) |
| [[PANC-1 (line)]] | alt | 62.6 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.67× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.493× (z -8.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 132 | 3 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.11× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.531× (z -8.5) |
| [[KATO III (line)]] | alt | 200 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -11.4) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.302× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 54.5 | 6 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.42× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +14.4) | — |
| [[HT-29 (line)]] | alt | 145 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.71× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.398× (z -9.8) |
| [[SW1417 (line)]] | alt | 189 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.446× (z -10.2) |
| [[BT-474 (line)]] | alt | 111 | 4 | 0 | [[PH-797804 (drug)]] 5 µM 6.20× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 157 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -15.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 150 | 1 (1 ⚠) | 3 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.80× (z +11.8) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.390× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 174 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.231× (z -16.2) |
| [[A-427 (line)]] | wt | 81.1 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.33× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -12.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 80.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.55× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -11.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 144 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 79.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -9.8) |
| [[HOP62 (line)]] | alt | 40.6 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.45× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 68.3 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 18.4× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 86.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.95× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 71.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.68× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -18.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 71.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -12.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -10.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 41.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 148 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.352× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 253 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 90.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -12.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 96.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -14.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 93.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -13.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 63.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.398× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -10.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 92.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +9.7) | — |
| [[C32 (line)]] | wt | 35.7 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.14× (z +8.6) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[LOX-IMVI (line)]] | wt | 84.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 68.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7283), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST14]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[SPINT1]] | +0.61 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[TJP2]] | +0.61 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[MAGI1]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[RNF43]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TMPRSS2]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[EPS8L3]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[GRB7]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SMAD6]] | +0.58 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[TCF7L2]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[RANBP9]] | +0.57 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[OCLN]] | +0.57 | +0.66 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCYT1A]] | -0.50 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[JMJD6]] | -0.50 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ZNF621]] | -0.50 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[POLR3D]] | -0.50 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[PRKAG1]] | -0.49 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[SZT2]] | -0.49 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[MYSM1]] | -0.48 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[SCFD1]] | -0.48 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[GOLGA3]] | -0.48 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[IL6R]] | -0.48 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[BRSK1]] | -0.47 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[TMEM132D]] | -0.47 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 44, C 0. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLIC5]] | B | CLIC5 activity raises USP6NL's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 2.27× lower at baseline in the lines without CLIC5 | 6e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[ST14]] | B | ST14 activity raises USP6NL's level | lines that do not express ST14 (32) vs lines expressing it (18) | 2.19× lower at baseline in the lines without ST14 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[ITGB6]] | B | ITGB6 activity raises USP6NL's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 2.04× lower at baseline in the lines without ITGB6 | 0.002 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[TMEM45B]] | B | TMEM45B activity raises USP6NL's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 2.29× lower at baseline in the lines without TMEM45B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[MTUS1]] | B | MTUS1 activity raises USP6NL's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 1.96× lower at baseline in the lines without MTUS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[INAVA]] | B | INAVA activity raises USP6NL's level | lines that do not express INAVA (29) vs lines expressing it (21) | 2.12× lower at baseline in the lines without INAVA | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[SLC6A14]] | B | SLC6A14 activity raises USP6NL's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 2.09× lower at baseline in the lines without SLC6A14 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[LINC02331]] | B | LINC02331 activity raises USP6NL's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 2.24× lower at baseline in the lines without LINC02331 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises USP6NL's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.05× lower at baseline in the lines without TMPRSS2 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[GRB7]] | B | GRB7 activity raises USP6NL's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 2.04× lower at baseline in the lines without GRB7 | 0.007 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[TOX3]] | B | TOX3 activity raises USP6NL's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 1.92× lower at baseline in the lines without TOX3 | 0.010 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[ELF3]] | B | ELF3 activity raises USP6NL's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 1.94× lower at baseline in the lines without ELF3 | 0.010 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.518). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.4, 57.6); signed map (55.7, 9.8). **Vector** length 110, 34.3% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.1 | +5.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | +0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +10.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Ixazomib (drug)]] 5 µM |  | +1.6 | +0.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.6 | -1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.2 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.7 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.5 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -3.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | USP6 N-terminal like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:11,460,510-11,611,666 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNTRE, KIAA0019, TRE2NL, RN-tre; previously USP6NL-IT1 |
| Gene groups (HGNC) | TBC1 domain family members |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92738](https://www.uniprot.org/uniprotkb/Q92738) (USP6 N-terminal-like protein):

> Acts as a GTPase-activating protein for RAB43, RAB5A and RAB30. Involved in receptor trafficking. In complex with EPS8 inhibits internalization of EGFR. Involved in retrograde transport from the endocytic pathway to the Golgi apparatus. Involved in the transport of Shiga toxin from early and recycling endosomes to the trans-Golgi network. Required for structural integrity of the Golgi complex.

**Summary**, from NCBI Gene [9712](https://www.ncbi.nlm.nih.gov/gene/9712):

> Enables GTPase activator activity and small GTPase binding activity. Involved in several processes, including plasma membrane to endosome transport; positive regulation of GTPase activity; and retrograde transport, plasma membrane to Golgi. Located in cytoplasmic vesicle and plasma membrane. Is active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16858) · Entrez [9712](https://www.ncbi.nlm.nih.gov/gene/9712) · UniProt [Q92738](https://www.uniprot.org/uniprotkb/Q92738) · Ensembl [ENSG00000148429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148429)

## Data

Gene col 7283: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7283); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7283, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7283]; `tensor/DDL_lfc|DDL_z.npy` [7283]; `embed/gene_vectors.npy` [7283]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7283 or target_col == 7283). Every well: [[USP6NL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP6NL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
