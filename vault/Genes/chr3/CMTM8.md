---
symbol: "CMTM8"
type: "gene"
col: 9930
ensembl_id: "ENSG00000170293"
name: "CKLF like MARVEL transmembrane domain containing 8"
location: "3p22.3"
module: 18
arm: "+"
pooled_cpm: 48.01
n_lines_expressing: 41
n_dd_up: 15
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 12
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CMTM8

*CKLF like MARVEL transmembrane domain containing 8* — 3p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 1.69× (z +11.4, q 3e-27, up in 36 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.410× (z -27.3, q 0e+00, down in 38 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PACC1]] (+0.70, fdr 7e-06), [[SIMC1]] (+0.65, fdr 7e-06), [[GARNL3]] (+0.64, fdr 1e-05); moves opposite to [[CGGBP1]] (-0.71, fdr 8e-06), [[PAN2]] (-0.68, fdr 1e-05), [[THAP9]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CRACD]] → it (grade B ⚠); 12 go from it, the strongest it → [[ZNF277]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **1.69×** | +11.4 | 3e-27 | 36/39 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +11.0 | 7e-26 | 34/39 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +11.0 | 7e-26 | 33/39 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +10.3 | 6e-23 | 24/39 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +9.2 | 4e-18 | 27/39 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.48×** | +8.0 | 9e-14 | 28/39 (NCI-H460, SK-MEL-2, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.39×** | +7.2 | 6e-11 | 24/39 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.85×** | +7.0 | 2e-10 | 33/39 (HEC-1-A, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +6.8 | 7e-10 | 21/39 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.71×** | +6.1 | 6e-08 | 21/36 (HEC-1-A, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.9 | 2e-07 | 22/39 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +5.3 | 7e-06 | 17/39 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +5.2 | 1e-05 | 18/39 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +4.3 | 6e-04 | 17/39 (SHP-77, CFPAC-1, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.20× | +3.9 | 0.003 | 12/39 (NCI-H2347, A-172, …) | top dose only |  |
| [[Penfluridol (drug)]] 5 µM |  | 1.19× | +3.6 | 0.012 | 9/39 (C-33 A, A-172, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.045 | 9/39 (HEC-1-A, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.10× | +3.0 | 0.089 | 3/39 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.14× | +2.9 | 0.098 | 4/39 (NCI-H460, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9930.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.410×** | -27.3 | 0e+00 | 38/39 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.466×** | -16.6 | 0e+00 | 35/39 (KATO III, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.473×** | -15.6 | 0e+00 | 30/39 (SNU-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.523×** | -14.1 | 1e-42 | 34/39 (SNU-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.351×** | -11.9 | 2e-30 | 31/40 (NCI-H23, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.666×** | -8.8 | 1e-16 | 24/39 (SNU-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.679×** | -8.4 | 4e-15 | 24/39 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.728×** | -6.6 | 3e-09 | 20/34 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.727×** | -6.4 | 1e-08 | 20/35 (C-33 A, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **0.788×** | -5.2 | 1e-05 | 21/39 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.775×** | -5.1 | 2e-05 | 22/39 (LS 180, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.809×** | -4.6 | 2e-04 | 16/39 (SNU-1, RKO, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.802×** | -4.6 | 2e-04 | 17/38 (SW1417, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.824×** | -4.2 | 0.001 | 16/39 (SW48, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | 0.843× | -3.7 | 0.009 | 18/39 (RKO, SW48, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.858× | -3.2 | 0.046 | 9/39 (NCI-H1573, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 82.4 | 1 (1 ⚠) | 7 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.85× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.538× (z -12.2) |
| [[KATO III (line)]] | alt | 86.0 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -15.9) |
| [[SW1417 (line)]] | alt | 165 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.363× (z -13.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.427× (z -11.8) |
| [[SW48 (line)]] | wt | 107 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -17.5) |
| [[SW480 (line)]] | alt | 120 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -17.1) |
| [[PANC-1 (line)]] | alt | 35.2 | 3 | 3 | [[Belinostat (drug)]] 5 µM 2.31× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -21.8) |
| [[SNU-1 (line)]] | wt | 68.8 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0982× (z -16.9) |
| [[LoVo (line)]] | wt | 57.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.8) |
| [[MIA PaCa-2 (line)]] | alt | 41.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -29.0) |
| [[NCI-H460 (line)]] | wt | 32.4 | 1 (1 ⚠) | 4 | [[Ixazomib citrate (drug)]] 5 µM 2.69× (z +9.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -15.6) |
| [[Panc 03.27 (line)]] | alt | 63.4 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.184× (z -15.4) |
| [[SK-MEL-2 (line)]] | alt | 52.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.3) |
| [[A-172 (line)]] | wt | 17.6 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.10× (z +10.4) | — |
| [[A549 (line)]] | wt | 31.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -15.7) |
| [[NCI-H2030 (line)]] | alt | 51.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.408× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 40.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -18.8) |
| [[RKO (line)]] | wt | 44.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -16.6) |
| [[A-427 (line)]] | wt | 74.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -16.8) |
| [[BT-474 (line)]] | alt | 72.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -14.8) |
| [[A498 (line)]] | wt | 24.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -11.2) |
| [[C-33 A (line)]] | alt | 94.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0860× (z -24.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 71.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.5) |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -8.6) |
| [[HCT15 (line)]] | alt | 58.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.9) |
| [[LS 180 (line)]] | wt | 69.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 24.7 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.86× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 56.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -10.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.78 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.13 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.61 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.88 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.78 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 75.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACC1]] | +0.70 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[SIMC1]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[GARNL3]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[RNF216]] | +0.64 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[EBPL]] | +0.64 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SLC29A2]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ARHGAP8]] | +0.63 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ARHGAP44]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[SRPK2]] | +0.62 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PALS2]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TSEN54]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[GTF2E2]] | +0.61 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGGBP1]] | -0.71 | -0.65 / -0.58 | both halves | 8e-06 |  |
| [[PAN2]] | -0.68 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[THAP9]] | -0.61 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[COG4]] | -0.61 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[DZIP3]] | -0.60 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[APLF]] | -0.60 | -0.54 / -0.37 | both halves | 7e-05 |  |
| [[METTL6]] | -0.60 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[SGO1-AS1]] | -0.60 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[PDCL3P4]] | -0.60 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[SEPSECS]] | -0.59 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[LINC00174]] | -0.59 | -0.56 / -0.32 | both halves | 1e-04 |  |
| [[ZNF429]] | -0.58 | -0.46 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRACD]] | B | CRACD activity raises CMTM8's level | lines that do not express CRACD (12) vs lines expressing it (38) | 2.53× lower at baseline in the lines without CRACD | 0.062 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[ST6GAL1]] | B | ST6GAL1 activity raises CMTM8's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 1.88× lower at baseline in the lines without ST6GAL1 | 0.068 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| [[SLC29A2]] | B | SLC29A2 activity raises CMTM8's level | lines that do not express SLC29A2 (14) vs lines expressing it (36) | 2.71× lower at baseline in the lines without SLC29A2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC27A2, EPHA10, OCLN; its own permutation p |
| [[ATP11A]] | C | ATP11A activity raises CMTM8's level | lines that do not express ATP11A (4) vs lines expressing it (46) | 6.62× lower at baseline in the lines without ATP11A | 0.004 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent |
| [[PCBD1]] | C | PCBD1 activity raises CMTM8's level | lines that do not express PCBD1 (3) vs lines expressing it (47) | 4.89× lower at baseline in the lines without PCBD1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FZD5, EZR, ZBED3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF277]] | B | CMTM8 activity raises ZNF277's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 1.65× lower at baseline in the lines without CMTM8 | 0.017 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[PCBD1]] | B | CMTM8 activity raises PCBD1's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 2.43× lower at baseline in the lines without CMTM8 | 0.023 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[ST6GAL1]] | B | CMTM8 activity raises ST6GAL1's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 2.94× lower at baseline in the lines without CMTM8 | 0.026 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[ADGRL1]] | B | CMTM8 activity raises ADGRL1's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 2.04× lower at baseline in the lines without CMTM8 | 0.027 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[ATP11A]] | B | CMTM8 activity raises ATP11A's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 3.12× lower at baseline in the lines without CMTM8 | 0.033 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[SMG5]] | B | CMTM8 activity raises SMG5's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 1.31× lower at baseline in the lines without CMTM8 | 0.060 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[DTNB]] | B | CMTM8 activity raises DTNB's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 2.19× lower at baseline in the lines without CMTM8 | 0.064 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[METTL25B]] | B | CMTM8 activity raises METTL25B's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 1.35× lower at baseline in the lines without CMTM8 | 0.072 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[HDHD3]] | B | CMTM8 activity raises HDHD3's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 1.83× lower at baseline in the lines without CMTM8 | 0.077 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[PACC1]] | B | CMTM8 activity raises PACC1's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 1.53× lower at baseline in the lines without CMTM8 | 0.077 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[RNF130]] | B | CMTM8 activity raises RNF130's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without CMTM8 | 0.079 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[LINC00174]] | B | CMTM8 activity raises LINC00174's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without CMTM8 | 0.096 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.559). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.0, -38.2); signed map (-14.3, -53.5). **Vector** length 110, 28.5% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +7.2 | +7.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.6 | +11.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.5 | +8.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +11.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +7.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.1 | -27.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.2 | -16.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -15.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.7 | -14.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -4.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | CKLF like MARVEL transmembrane domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.3 — chr3:32,238,679-32,370,321 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CKLFSF8 |
| Gene groups (HGNC) | CKLF like MARVEL transmembrane domain containing |
| Matched by | ensembl_id |

UniProt [Q8IZV2](https://www.uniprot.org/uniprotkb/Q8IZV2) carries no function annotation.

**Summary**, from NCBI Gene [152189](https://www.ncbi.nlm.nih.gov/gene/152189):

> This gene belongs to the chemokine-like factor gene superfamily, a novel family that is similar to the chemokine and the transmembrane 4 superfamilies. This gene is one of several chemokine-like factor genes located in a cluster on chromosome 3. This gene acts as a tumor suppressor, and plays a role in regulating the migration of tumor cells. The encoded protein is thought to function as a a negative regulator of epidermal growth factor-induced signaling. Alternative splicing results in …

**Accessions** — [HGNC:19179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19179) · Entrez [152189](https://www.ncbi.nlm.nih.gov/gene/152189) · UniProt [Q8IZV2](https://www.uniprot.org/uniprotkb/Q8IZV2) · Ensembl [ENSG00000170293](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170293)

## Data

Gene col 9930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9930); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9930]; `tensor/DDL_lfc|DDL_z.npy` [9930]; `embed/gene_vectors.npy` [9930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9930 or target_col == 9930). Every well: [[CMTM8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMTM8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
