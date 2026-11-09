---
symbol: "PLP2"
type: "gene"
col: 2202
ensembl_id: "ENSG00000102007"
name: "proteolipid protein 2"
location: "Xp11.23"
module: 78
arm: "+"
pooled_cpm: 57.03
n_lines_expressing: 46
n_dd_up: 3
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 6
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# PLP2

*proteolipid protein 2* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.11× (z +12.3, q 4e-32, up in 42 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H460 4.34×, NCI-H1792 5.00×, PANC-1 3.40×, LoVo 4.71×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H460 3.83×, A549 4.09×, Panc 03.27 3.98×, PANC-1 3.30×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.384× (z -14.7, q 0e+00, down in 44 of 44 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK1]] (+0.62, fdr 6e-05), [[CD151]] (+0.62, fdr 1e-05), [[ITGA3]] (+0.58, fdr 1e-05); moves opposite to [[SMAD1]] (-0.50, fdr 6e-04), [[PPCS]] (-0.50, fdr 7e-04), [[IWS1]] (-0.48, fdr 1e-04).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZCCHC24]] → it (grade B ⚠); 6 go from it, the strongest it → [[PODXL]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2202.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H460 4.34×, NCI-H1792 5.00×, PANC-1 3.40×, LoVo 4.71×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H460 3.83×, A549 4.09×, Panc 03.27 3.98×, PANC-1 3.30×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +12.3 | 4e-32 | 42/43 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +11.2 | 2e-26 | 34/36 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +7.1 | 2e-10 | 31/39 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2202.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.384×** | -14.7 | 0e+00 | 44/44 (H4, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.449×** | -8.7 | 7e-16 | 36/44 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.554×** | -6.4 | 2e-08 | 38/44 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.579×** | -6.0 | 4e-07 | 39/44 (SW 1088, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.609×** | -5.4 | 7e-06 | 36/44 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.621×** | -5.2 | 2e-05 | 39/44 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -5.1 | 3e-05 | 27/44 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.641×** | -4.9 | 9e-05 | 33/44 (HCT15, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.440×** | -4.7 | 2e-04 | 35/44 (SK-MEL-2, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.648×** | -4.5 | 4e-04 | 26/44 (KATO III, HS-578T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.677×** | -4.3 | 0.001 | 30/44 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.693×** | -3.8 | 0.006 | 28/44 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.710×** | -3.7 | 0.008 | 26/44 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.700×** | -3.7 | 0.008 | 23/43 (SK-MEL-2, A-172, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **0.792×** | -3.6 | 0.011 | 27/44 (LS 180, A-172, …) | rises with dose | low cells (technical?) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -3.6 | 0.011 | 23/44 (A498, KATO III, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.741×** | -3.3 | 0.035 | 27/44 (J82, A-172, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.726×** | -3.2 | 0.036 | 22/44 (SW480, SK-MEL-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.744×** | -3.2 | 0.036 | 23/44 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 34.9 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -14.4) |
| [[HOP62 (line)]] | alt | 75.1 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -9.4) |
| [[HS-578T (line)]] | alt | 55.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -12.9) |
| [[LoVo (line)]] | wt | 41.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 60.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -13.2) |
| [[SW480 (line)]] | alt | 111 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -13.7) |
| [[A-172 (line)]] | wt | 69.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -12.5) |
| [[A549 (line)]] | wt | 61.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 58.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.8) |
| [[J82 (line)]] | alt | 55.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -12.9) |
| [[KATO III (line)]] | alt | 73.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 96.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -15.8) |
| [[RPMI-7951 (line)]] | alt | 100 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -10.7) |
| [[A-427 (line)]] | wt | 57.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.62× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.9) |
| [[A498 (line)]] | wt | 39.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +10.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 78.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -8.5) |
| [[H4 (line)]] | wt | 79.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -19.3) |
| [[HCT15 (line)]] | alt | 72.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.87× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.2) |
| [[Hs 766T (line)]] | wt | 92.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 35.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 80.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 43.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 31.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 102 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -15.3) |
| [[PANC-1 (line)]] | alt | 75.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +11.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 42.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -17.9) |
| [[SW 1088 (line)]] | alt | 93.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0443× (z -11.8) |
| [[SW 900 (line)]] | alt | 47.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -8.9) |
| [[BT-474 (line)]] | alt | 34.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -13.8) |
| [[C32 (line)]] | wt | 43.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 30.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -13.5) |
| [[hTERT-HPNE (line)]] | wt | 45.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -9.7) |
| [[RKO (line)]] | wt | 61.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.5) |
| [[SW 1271 (line)]] | alt | 59.7 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0892× (z -8.7) |
| [[SW1417 (line)]] | alt | 30.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 7.53 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.84 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK1]] | +0.62 | +0.70 / +0.38 | both halves | 6e-05 |  |
| [[CD151]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ITGA3]] | +0.58 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[MYADM]] | +0.58 | +0.64 / +0.44 | both halves | 3e-05 | same gene group |
| [[ITPR3]] | +0.57 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[TAGLN2]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[FXYD5]] | +0.56 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[PLXNA1]] | +0.56 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[PPP1CA]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 | STRING 569 |
| [[CLIC1]] | +0.55 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[LAPTM5]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[LTBP3]] | +0.53 | +0.59 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD1]] | -0.50 | -0.58 / -0.22 | both halves | 6e-04 |  |
| [[PPCS]] | -0.50 | -0.65 / -0.21 | both halves | 7e-04 |  |
| [[IWS1]] | -0.48 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[GCNT2]] | -0.47 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[PSTPIP2]] | -0.47 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[SLC11A2]] | -0.46 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[NEMF]] | -0.46 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[SART3]] | -0.46 | -0.48 / -0.18 | ⚠ not reproduced | 0.001 |  |
| [[TFAP2A-AS1]] | -0.46 | -0.55 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[COIL]] | -0.45 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[FUNDC1]] | -0.44 | -0.52 / -0.23 | both halves | 5e-04 |  |
| [[CCDC43]] | -0.44 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[SULT1C2]] | -0.44 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[C11orf52]] | -0.44 | -0.45 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZCCHC24]] | B | ZCCHC24 activity raises PLP2's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 2.01× lower at baseline in the lines without ZCCHC24 | 0.012 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[TGFB1I1]] | B | TGFB1I1 activity raises PLP2's level | lines that do not express TGFB1I1 (13) vs lines expressing it (37) | 2.26× lower at baseline in the lines without TGFB1I1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, ENSG00000234405, TMOD1 |
| [[KCNC4]] | B | KCNC4 activity raises PLP2's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 2.81× lower at baseline in the lines without KCNC4 | 0.045 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[LAPTM5]] | B | LAPTM5 activity raises PLP2's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.71× lower at baseline in the lines without LAPTM5 | 0.062 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |
| [[LTBP3]] | C | LTBP3 activity raises PLP2's level | lines that do not express LTBP3 (4) vs lines expressing it (46) | 3.29× lower at baseline in the lines without LTBP3 | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: DBN1, NUAK1, BLVRA; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL]] | C | PLP2 activity raises PODXL's level | lines that do not express PLP2 (4) vs lines expressing it (46) | 2.70× lower at baseline in the lines without PLP2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OTULINL, C12orf75; maybe low, not absent; its own permutation p |
| [[ARHGDIA]] | C | PLP2 activity raises ARHGDIA's level | lines that do not express PLP2 (4) vs lines expressing it (46) | 1.38× lower at baseline in the lines without PLP2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OTULINL, C12orf75; maybe low, not absent; its own permutation p |
| [[FUNDC1]] | C | PLP2's natural level strengthens FUNDC1's drug response | PLP2's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.44; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[TUBB]] | C | PLP2 activity raises TUBB's level | lines that do not express PLP2 (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without PLP2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OTULINL, C12orf75; maybe low, not absent; its own permutation p |
| [[PPP1CA]] | C | PLP2 activity raises PPP1CA's level | lines that do not express PLP2 (4) vs lines expressing it (46) | 1.41× lower at baseline in the lines without PLP2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OTULINL, C12orf75; maybe low, not absent; its own permutation p |
| [[ATP13A2]] | C | PLP2 activity raises ATP13A2's level | lines that do not express PLP2 (4) vs lines expressing it (46) | 1.34× lower at baseline in the lines without PLP2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OTULINL, C12orf75; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.609). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.0, -3.5); signed map (-12.1, 34.6). **Vector** length 75.6, 22.1% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +11.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | -6.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | -6.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | -1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -14.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -2.6 | -3.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.5 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -8.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | proteolipid protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:49,171,898-49,175,235 (+) |
| Ensembl biotype | protein_coding |
| Also known as | A4, A4-LSB, MGC126187 |
| Gene groups (HGNC) | MARVEL domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04941](https://www.uniprot.org/uniprotkb/Q04941) (Proteolipid protein 2):

> May play a role in cell differentiation in the intestinal epithelium.

**Summary**, from NCBI Gene [5355](https://www.ncbi.nlm.nih.gov/gene/5355):

> This gene encodes an integral membrane protein that localizes to the endoplasmic reticulum in colonic epithelial cells. The encoded protein can multimerize and may function as an ion channel. A polymorphism in the promoter of this gene may be linked to an increased risk of X-linked cognitive disability. A pseudogene of this gene is found on chromosome 5. [provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:9087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9087) · Entrez [5355](https://www.ncbi.nlm.nih.gov/gene/5355) · UniProt [Q04941](https://www.uniprot.org/uniprotkb/Q04941) · Ensembl [ENSG00000102007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102007)

## Data

Gene col 2202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2202); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2202]; `tensor/DDL_lfc|DDL_z.npy` [2202]; `embed/gene_vectors.npy` [2202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2202 or target_col == 2202). Every well: [[PLP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
