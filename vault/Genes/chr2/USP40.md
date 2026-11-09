---
symbol: "USP40"
type: "gene"
col: 1447
ensembl_id: "ENSG00000085982"
name: "ubiquitin specific peptidase 40"
location: "2q37.1"
module: 88
arm: "+"
pooled_cpm: 59.11
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 35
n_dd_up_clean: 7
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# USP40

*ubiquitin specific peptidase 40* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.35× (z +4.1, q 0.027, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (17 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.315× (z -16.0, q 0e+00, down in 44 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.352× (z -14.5, q 7e-45, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00174]] (+0.76, fdr 7e-06), [[RAD50]] (+0.74, fdr 7e-06), [[TRMT13]] (+0.73, fdr 1e-05); moves opposite to [[RGS10]] (-0.66, fdr 7e-06), [[ANKRD9]] (-0.66, fdr 9e-06), [[UBTD1]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1447.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.027 | 28/46 (J82, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.031 | 18/48 (SW480, J82, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.031 | 21/46 (RKO, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.32×** | +3.7 | 0.031 | 23/48 (J82, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.032 | 24/47 (RKO, AsPC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.038 | 20/47 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.18× | +3.4 | 0.057 | 15/47 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.057 | 18/46 (AsPC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.063 | 22/46 (J82, HOP62, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.53× | +3.1 | 0.11 | 13/48 (J82, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1447.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.315×** | -16.0 | 0e+00 | 44/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.352×** | -14.5 | 7e-45 | 44/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.363×** | -14.0 | 2e-42 | 41/47 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.485×** | -10.0 | 2e-21 | 42/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.546×** | -8.4 | 7e-15 | 41/47 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.548×** | -8.0 | 1e-13 | 36/46 (RKO, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.567×** | -7.8 | 4e-13 | 41/47 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.570×** | -7.8 | 5e-13 | 42/47 (LoVo, HOP62, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -7.4 | 6e-12 | 33/48 (RPMI-7951, LS 180, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.589×** | -7.0 | 1e-10 | 34/46 (KATO III, HCT15, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.607×** | -6.9 | 3e-10 | 39/47 (LoVo, J82, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.653×** | -5.9 | 2e-07 | 31/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.670×** | -5.5 | 2e-06 | 27/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.799×** | -4.4 | 5e-04 | 25/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.736×** | -4.2 | 9e-04 | 27/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.578×** | -4.0 | 0.002 | 22/47 (SNU-1, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.757×** | -3.6 | 0.008 | 21/47 (KATO III, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.620×** | -3.5 | 0.015 | 22/47 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.784×** | -3.3 | 0.020 | 19/47 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.641×** | -3.2 | 0.029 | 22/47 (SW1417, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.849× | -3.2 | 0.032 | 14/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.798×** | -3.1 | 0.038 | 17/47 (CFPAC-1, SW 1088, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.745×** | -2.9 | 0.070 | 16/47 (LoVo, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1447. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 85.6 | 0 | 15 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -16.7) |
| [[LoVo (line)]] | wt | 81.6 | 0 | 11 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.253× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -13.0) |
| [[SW480 (line)]] | alt | 65.9 | 0 | 10 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -18.1) |
| [[HCT15 (line)]] | alt | 95.3 | 0 | 8 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.150× (z -14.8) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.296× (z -9.8) |
| [[PANC-1 (line)]] | alt | 57.4 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 84.5 | 0 | 7 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -16.8) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 90.3 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.310× (z -10.2) |
| [[A-427 (line)]] | wt | 52.6 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 0.5 µM 0.177× (z -16.3) |
| [[HOP62 (line)]] | alt | 78.0 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -9.4) |
| [[KATO III (line)]] | alt | 66.0 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0904× (z -22.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -11.2) |
| [[LS 180 (line)]] | wt | 61.8 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -12.9) |
| [[BT-474 (line)]] | alt | 71.4 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.241× (z -12.2) |
| [[COLO 205 (line)]] | alt | 54.2 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.130× (z -15.9) |
| [[hTERT-HPNE (line)]] | wt | 67.8 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -13.4) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -9.9) |
| [[J82 (line)]] | alt | 44.4 | 2 (1 ⚠) | 2 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 4.58× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.234× (z -9.3) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H23 (line)]] | alt | 79.2 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.397× (z -8.9) |
| [[SHP-77 (line)]] | alt | 40.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.262× (z -10.2) |
| [[A549 (line)]] | wt | 78.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.5) |
| [[H4 (line)]] | wt | 55.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -8.8) |
| [[RKO (line)]] | wt | 50.8 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.153× (z -15.1) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 46.9 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 76.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.339× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 76.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.352× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 60.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -9.6) |
| [[SNU-1 (line)]] | wt | 77.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.181× (z -12.5) |
| [[AN3 CA (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.139× (z -8.9) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 45.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -13.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -11.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 55.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.307× (z -8.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 67.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -15.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[SNU-423 (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -14.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 63.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.314× (z -8.5) |
| [[A-172 (line)]] | wt | 90.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.54 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 24.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1447), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00174]] | +0.76 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[RAD50]] | +0.74 | +0.84 / +0.59 | both halves | 7e-06 |  |
| [[TRMT13]] | +0.73 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[NEK9]] | +0.73 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[DARS1]] | +0.73 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[LEKR1]] | +0.72 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[ZMYM4]] | +0.72 | +0.73 / +0.58 | both halves | 8e-06 |  |
| [[LZIC]] | +0.71 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[TASOR]] | +0.71 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[ZNF429]] | +0.71 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[TCTN1]] | +0.70 | +0.76 / +0.58 | both halves | 8e-06 |  |
| [[DZIP3]] | +0.70 | +0.80 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS10]] | -0.66 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[ANKRD9]] | -0.66 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[UBTD1]] | -0.65 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[IGSF8]] | -0.64 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[ANKRD13D]] | -0.64 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[B3GAT3]] | -0.64 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[UQCRH]] | -0.64 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[TPST2]] | -0.63 | -0.76 / -0.38 | both halves | 6e-05 |  |
| [[GNB2]] | -0.63 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[SMARCD2]] | -0.62 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[KLHL7]] | -0.62 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[SDHAP2]] | -0.62 | -0.65 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers USP40's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FHIT]] | B | FHIT activity raises USP40's level | lines that do not express FHIT (6) vs lines expressing it (44) | 1.73× lower at baseline in the lines without FHIT | 0.056 | ⚠ within organs, on part of the lines; also absent: PTGFRN, FBXO16; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity lowers USP40's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[COQ5]] | C | COQ5's natural level strengthens USP40's drug response | COQ5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.12; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.756). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-23.4, 8.0); signed map (11.0, -25.3). **Vector** length 90.9, 27.1% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.8 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.0 | +0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +0.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.9 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -7.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -4.7 | -7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.6 | -7.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -4.4 | -6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.8 | -7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:233,475,526-233,566,782 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10785 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVE5](https://www.uniprot.org/uniprotkb/Q9NVE5) (Ubiquitin carboxyl-terminal hydrolase 40):

> Deubiquitinating enzyme that plays a key role in maintaining endothelial cell (EC) barrier integrity and regulating apoptosis and inflammation. Stabilizes Claudin-1/CLDN1 by cleaving its polyubiquitin chains, thereby protecting tight junction structure. Prevents EC barrier disruption by inhibiting RhoA activation and reducing phosphorylation of myosin light chain and cofilin. Suppresses EC inflammation by inhibiting NF-kappa-B activation, decreasing ICAM1 expression, and reducing leukocyte …

**Summary**, from NCBI Gene [55230](https://www.ncbi.nlm.nih.gov/gene/55230):

> Modification of cellular proteins by ubiquitin is an essential regulatory mechanism controlled by the coordinated action of multiple ubiquitin-conjugating and deubiquitinating enzymes. USP40 belongs to a large family of cysteine proteases that function as deubiquitinating enzymes (Quesada et al., 2004 [PubMed 14715245]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20069](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20069) · Entrez [55230](https://www.ncbi.nlm.nih.gov/gene/55230) · UniProt [Q9NVE5](https://www.uniprot.org/uniprotkb/Q9NVE5) · Ensembl [ENSG00000085982](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085982)

## Data

Gene col 1447: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1447); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1447, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1447]; `tensor/DDL_lfc|DDL_z.npy` [1447]; `embed/gene_vectors.npy` [1447]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1447 or target_col == 1447). Every well: [[USP40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
