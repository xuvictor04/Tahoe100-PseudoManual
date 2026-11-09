---
symbol: "SNTB2"
type: "gene"
col: 9704
ensembl_id: "ENSG00000168807"
name: "syntrophin beta 2"
location: "16q22.1"
module: 17
arm: "-"
pooled_cpm: 61.8
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# SNTB2

*syntrophin beta 2* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +16.2, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.685× (z -10.4, q 2e-22, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXW7]] (+0.60, fdr 1e-05), [[MFSD14CP-1]] (+0.59, fdr 1e-05), [[COP1]] (+0.57, fdr 3e-05); moves opposite to [[PRPF39]] (-0.64, fdr 1e-05), [[NEPRO]] (-0.60, fdr 1e-05), [[ZDHHC17]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9704.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +16.2 | 0e+00 | 44/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.63×** | +9.2 | 2e-17 | 36/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.50×** | +7.9 | 5e-13 | 34/47 (HS-578T, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.50×** | +7.5 | 8e-12 | 31/48 (LS 180, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.4 | 1e-08 | 30/47 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.39×** | +6.3 | 2e-08 | 28/47 (RPMI-7951, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.33×** | +5.5 | 3e-06 | 26/47 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.27×** | +4.6 | 4e-04 | 24/48 (NCI-H1573, A-427, …) | two highest doses | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.25×** | +4.2 | 0.002 | 22/47 (A498, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.23×** | +4.1 | 0.003 | 19/47 (A498, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 1.19× | +3.3 | 0.045 | 17/47 (SW480, A549, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.045 | 14/47 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.051 | 6/47 (SW1417, A498, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.054 | 11/47 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.18× | +3.2 | 0.055 | 8/47 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.057 | 13/47 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.1 | 0.062 | 14/47 (HS-578T, SNU-423, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.066 | 10/47 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.066 | 11/47 (SW1417, C32, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.068 | 12/47 (SW1417, HT-29, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.068 | 7/48 (A498, HT-29, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.16× | +2.9 | 0.090 | 6/47 (AsPC-1, SW 1088, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9704.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.685×** | -10.4 | 2e-22 | 33/47 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.649×** | -8.1 | 2e-13 | 34/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.698×** | -7.0 | 6e-10 | 29/47 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.756×** | -5.4 | 8e-06 | 24/47 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.599×** | -5.2 | 2e-05 | 26/48 (HepG2/C3A, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.788×** | -4.6 | 4e-04 | 23/47 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.751×** | -4.0 | 0.006 | 14/47 (SW480, HT-29, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.834× | -3.5 | 0.031 | 17/47 (HT-29, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.882× | -3.4 | 0.036 | 15/47 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.842× | -3.3 | 0.048 | 12/47 (NCI-H2030, BT-474, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.846× | -3.3 | 0.059 | 17/47 (A-427, KATO III, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.847× | -3.2 | 0.060 | 16/46 (SNU-1, COLO 205, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.890× | -3.2 | 0.061 | 3/47 (NCI-H23, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9704. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.8 | 3 (2 ⚠) | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +19.4) | [[Digitoxin (drug)]] 5 µM 0.337× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.374× (z -12.5) |
| [[LoVo (line)]] | wt | 66.5 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.395× (z -11.8) |
| [[RKO (line)]] | wt | 52.8 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -10.8) |
| [[SW480 (line)]] | alt | 140 | 2 (2 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.8) ⚠ cell-cycle shift, explains ~29% of this change | [[Lonafarnib (drug)]] 5 µM 0.274× (z -9.9) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 49.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +12.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 57.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +15.2) | — |
| [[SW1417 (line)]] | alt | 81.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.347× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.515× (z -8.9) |
| [[A-172 (line)]] | wt | 63.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -13.1) |
| [[H4 (line)]] | wt | 45.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 59.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +11.6) | [[Digitoxin (drug)]] 5 µM 0.265× (z -9.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 96.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 113 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +10.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.506× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 29.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 46.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -9.1) |
| [[A-427 (line)]] | wt | 63.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -11.2) |
| [[A498 (line)]] | wt | 89.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +13.6) | — |
| [[AN3 CA (line)]] | alt | 57.8 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.173× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 49.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.344× (z -8.6) |
| [[C32 (line)]] | wt | 68.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.7) | — |
| [[CHP-212 (line)]] | wt | 43.0 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0974× (z -9.7) |
| [[Hs 766T (line)]] | wt | 67.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -9.2) |
| [[HS-578T (line)]] | alt | 44.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -10.5) |
| [[HT-29 (line)]] | alt | 55.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 65.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.354× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 86.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.394× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 41.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -8.5) |
| [[PANC-1 (line)]] | alt | 45.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.614× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 65.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.320× (z -9.1) |
| [[SNU-1 (line)]] | wt | 51.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +8.7) | — |
| [[SW48 (line)]] | wt | 53.6 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.244× (z -9.4) |
| [[A549 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9704), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW7]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[MFSD14CP-1]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[COP1]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[GATAD2A]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[NR2C2]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SRGAP2C]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SRGAP2]] | +0.56 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[SRGAP2B]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[PGP]] | +0.55 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SNRPB]] | +0.54 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[TEAD4]] | +0.54 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[PKP4]] | +0.54 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF39]] | -0.64 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[NEPRO]] | -0.60 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[ZDHHC17]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[KPNA5]] | -0.59 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[TP53BP1]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[TTC8]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[DYNC2LI1]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[RING1]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.55 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[STK32A]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ZNF14]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[SPEF2]] | -0.54 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SNTB2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RFLNB]] | B | RFLNB activity raises SNTB2's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 1.20× lower at baseline in the lines without RFLNB | 0.035 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.580). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-22.3, 2.2); signed map (-51.0, -25.4). **Vector** length 103, 26.3% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.1 | +9.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.3 | +7.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | -1.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +6.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | -1.9 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +1.9 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -10.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.7 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.6 | -2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | syntrophin beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:69,187,147-69,309,052 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EST25263, SNT3; previously SNT2B2, SNTL, D16S2531E |
| Gene groups (HGNC) | PDZ domain containing; Syntrophin family |
| Reactome | 3 pathways, smallest: Formation of the dystrophin-glycoprotein complex (DGC); Non-integrin membrane-ECM interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13425](https://www.uniprot.org/uniprotkb/Q13425) (Beta-2-syntrophin):

> Adapter protein that binds to and probably organizes the subcellular localization of a variety of membrane proteins. May link various receptors to the actin cytoskeleton and the dystrophin glycoprotein complex. May play a role in the regulation of secretory granules via its interaction with PTPRN.

**Summary**, from NCBI Gene [6645](https://www.ncbi.nlm.nih.gov/gene/6645):

> Dystrophin is a large, rod-like cytoskeletal protein found at the inner surface of muscle fibers. Dystrophin is missing in Duchenne Muscular Dystrophy patients and is present in reduced amounts in Becker Muscular Dystrophy patients. The protein encoded by this gene is a peripheral membrane protein found associated with dystrophin and dystrophin-related proteins. This gene is a member of the syntrophin gene family, which contains at least two other structurally-related genes. [provided by …

**Accessions** — [HGNC:11169](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11169) · Entrez [6645](https://www.ncbi.nlm.nih.gov/gene/6645) · UniProt [Q13425](https://www.uniprot.org/uniprotkb/Q13425) · Ensembl [ENSG00000168807](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168807)

## Data

Gene col 9704: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9704); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9704, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9704]; `tensor/DDL_lfc|DDL_z.npy` [9704]; `embed/gene_vectors.npy` [9704]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9704 or target_col == 9704). Every well: [[SNTB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNTB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
