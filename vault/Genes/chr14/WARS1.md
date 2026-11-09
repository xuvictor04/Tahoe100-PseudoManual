---
symbol: "WARS1"
type: "gene"
col: 6374
ensembl_id: "ENSG00000140105"
name: "tryptophanyl-tRNA synthetase 1"
location: "14q32.2"
module: 133
arm: "+"
pooled_cpm: 119.01
n_lines_expressing: 49
n_dd_up: 36
n_dd_down: 22
n_dd_up_clean: 30
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# WARS1

*tryptophanyl-tRNA synthetase 1* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (6 with an alert ⚠); the strongest is [[5-Azacytidine (drug)]] 5 µM: 2.02× (z +11.3, q 4e-27, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.564× (z -10.5, q 7e-23, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC6A9]] (+0.68, fdr 7e-06), [[APOL6]] (+0.64, fdr 7e-06), [[SLC7A11]] (+0.62, fdr 1e-05); moves opposite to [[DCBLD1]] (-0.45, fdr 4e-05), [[HMGA2]] (-0.44, fdr 1e-04), [[GRAMD1C]] (-0.43, fdr 2e-04).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SAMD9L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6374.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **2.02×** | +11.3 | 4e-27 | 41/47 (SW480, AsPC-1, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **1.72×** | +10.4 | 1e-22 | 42/47 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.67×** | +8.2 | 3e-14 | 40/47 (SW480, SW48, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.64×** | +8.0 | 2e-13 | 37/46 (SW480, SW 900, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.63×** | +7.9 | 3e-13 | 36/47 (NCI-H2030, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +7.0 | 2e-10 | 32/47 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +6.9 | 4e-10 | 24/48 (HEC-1-A, A549, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **2.03×** | +6.0 | 2e-07 | 34/47 (NCI-H2030, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.38×** | +5.7 | 8e-07 | 26/47 (NCI-H2030, SW480, …) | two highest doses |  |
| [[Encorafenib (drug)]] 5 µM |  | **1.95×** | +5.7 | 8e-07 | 32/47 (NCI-H460, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +5.6 | 1e-06 | 23/46 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.32×** | +5.4 | 4e-06 | 26/48 (SNU-1, Hs 766T, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.38×** | +5.2 | 1e-05 | 26/47 (RKO, SHP-77, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.38×** | +5.2 | 1e-05 | 26/47 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +5.0 | 2e-05 | 24/48 (CFPAC-1, NCI-H460, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.80×** | +5.0 | 2e-05 | 24/47 (PANC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +4.9 | 3e-05 | 24/47 (SHP-77, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6374.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.564×** | -10.5 | 7e-23 | 41/47 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.590×** | -10.3 | 2e-22 | 31/47 (LoVo, MIA PaCa-2, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.569×** | -9.2 | 9e-18 | 38/48 (SW48, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.673×** | -8.0 | 2e-13 | 36/47 (SK-MEL-2, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.699×** | -5.6 | 2e-06 | 26/47 (LoVo, A-172, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.712×** | -5.3 | 1e-05 | 25/46 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.742×** | -4.9 | 9e-05 | 23/47 (KATO III, LoVo, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.727×** | -4.8 | 1e-04 | 25/46 (LoVo, H4, …) | all doses, flat | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.751×** | -4.7 | 2e-04 | 23/47 (LoVo, A498, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.752×** | -4.7 | 2e-04 | 22/47 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.607×** | -4.2 | 0.001 | 19/48 (LoVo, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.773×** | -4.2 | 0.001 | 21/47 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.781×** | -4.0 | 0.002 | 18/47 (SK-MEL-2, LoVo, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.822×** | -3.9 | 0.003 | 23/48 (SK-MEL-2, C32, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.788×** | -3.9 | 0.004 | 24/47 (LoVo, H4, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.791×** | -3.8 | 0.004 | 23/47 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.804×** | -3.6 | 0.012 | 17/47 (A498, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.807×** | -3.5 | 0.013 | 19/47 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.818×** | -3.3 | 0.030 | 19/47 (LoVo, SK-MEL-2, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.822×** | -3.2 | 0.037 | 20/47 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 269 | 0 | 19 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -23.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.178× (z -14.0) |
| [[A-172 (line)]] | wt | 192 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -18.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.198× (z -11.6) |
| [[KATO III (line)]] | alt | 179 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -12.1) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Tucidinostat (drug)]] 0.5 µM 0.208× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 529 | 1 (1 ⚠) | 7 (5 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.52× (z +10.3) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -18.6) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.239× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 371 | 3 (1 ⚠) | 5 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.97× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -12.2) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.288× (z -11.5) |
| [[SW480 (line)]] | alt | 70.9 | 6 (1 ⚠) | 2 | [[Artesunate (drug)]] 5 µM 2.52× (z +14.5) | [[Tucidinostat (drug)]] 0.5 µM 0.457× (z -10.2) |
| [[SW48 (line)]] | wt | 155 | 2 | 3 (1 ⚠) | [[Artesunate (drug)]] 5 µM 3.38× (z +10.7) | [[Tucidinostat (drug)]] 0.5 µM 0.147× (z -14.0) |
| [[HT-29 (line)]] | alt | 118 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -9.1) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.362× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 215 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.374× (z -12.3) |
| [[H4 (line)]] | wt | 196 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -10.4) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.208× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 39.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 134 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.415× (z -9.7) |
| [[A498 (line)]] | wt | 90.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A549 (line)]] | wt | 30.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 125 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -12.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.431× (z -8.7) |
| [[PANC-1 (line)]] | alt | 44.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +9.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 106 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.342× (z -11.4) |
| [[A-427 (line)]] | wt | 41.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[C32 (line)]] | wt | 147 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.368× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 157 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.309× (z -9.1) |
| [[LS 180 (line)]] | wt | 87.6 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.324× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 61.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.69× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -9.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H2030 (line)]] | alt | 54.1 | 1 | 0 | [[Neratinib (maleate) (drug)]] 0.5 µM 3.20× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -11.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SW 1271 (line)]] | alt | 83.4 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.5 µM 0.0463× (z -9.0) |
| [[AN3 CA (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 180 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 70.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A9]] | +0.68 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[APOL6]] | +0.64 | +0.60 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[SLC7A11]] | +0.62 | +0.57 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[NBR2]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[AARS1]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 906 |
| [[MARS1]] | +0.60 | +0.57 / +0.62 | both halves | 9e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 923 |
| [[WDR25]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SLC7A5]] | +0.58 | +0.58 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[YARS1]] | +0.58 | +0.49 / +0.63 | both halves | 1e-05 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 997 |
| [[MOCOS]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[TRIM25]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 572 |
| [[LAMP3]] | +0.57 | +0.47 / +0.61 | both halves | 2e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[CEBPG]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCBLD1]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[HMGA2]] | -0.44 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[GRAMD1C]] | -0.43 | -0.32 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD9L]] | B | SAMD9L activity raises WARS1's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.01× lower at baseline in the lines without SAMD9L | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[NMRAL2P]] | B | NMRAL2P activity raises WARS1's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.90× lower at baseline in the lines without NMRAL2P | 0.034 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[APOL6]] | B | APOL6 activity raises WARS1's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 2.72× lower at baseline in the lines without APOL6 | 0.053 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[KRT14]] | B | KRT14 activity raises WARS1's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 1.94× lower at baseline in the lines without KRT14 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13 |
| [[NLRC5]] | B | NLRC5 activity raises WARS1's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 2.25× lower at baseline in the lines without NLRC5 | 0.086 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[CCDC194]] | B | CCDC194 activity raises WARS1's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 1.65× lower at baseline in the lines without CCDC194 | 0.089 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[RSAD2]] | B | RSAD2 activity raises WARS1's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.77× lower at baseline in the lines without RSAD2 | 0.092 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.0, 46.0); signed map (-14.1, 22.1). **Vector** length 153, 51.5% of its response variance represented; |z| ≥ 3 in 1,817 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[5-Azacytidine (drug)]] 5 µM |  | +8.0 | +11.3 |
|  | [[Artesunate (drug)]] 5 µM |  | +7.9 | +10.4 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +6.3 | +7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.1 | +7.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +5.9 | +5.7 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +5.7 | +5.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +5.6 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +4.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.8 | -10.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.1 | -8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.5 | -9.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -6.1 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.8 | -4.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.8 | -4.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | tryptophanyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:100,333,790-100,376,805 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IFP53; previously IFI53, WARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, ALLOGRAFT_REJECTION, INTERFERON_GAMMA_RESPONSE, MTORC1_SIGNALING |
| Reactome | 3 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P23381](https://www.uniprot.org/uniprotkb/P23381) (Tryptophan--tRNA ligase, cytoplasmic):

> Catalyzes the attachment of tryptophan to tRNA(Trp) in a two-step reaction: tryptophan is first activated by ATP to form Trp-AMP and then transferred to the acceptor end of the tRNA(Trp).; [Isoform 1]: Has no angiostatic activity.; [T2-TrpRS]: Possesses an angiostatic activity but has no aminoacylation activity. Inhibits fluid shear stress-activated responses of endothelial cells. Regulates ERK, Akt, and eNOS activation pathways that are associated with angiogenesis, cytoskeletal reorganization …

**Summary**, from NCBI Gene [7453](https://www.ncbi.nlm.nih.gov/gene/7453):

> Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of tryptophanyl-tRNA synthetase exist, a cytoplasmic form, named WARS, and a mitochondrial form, named WARS2. Tryptophanyl-tRNA synthetase (WARS) catalyzes the aminoacylation of tRNA(trp) with …

**Accessions** — [HGNC:12729](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12729) · Entrez [7453](https://www.ncbi.nlm.nih.gov/gene/7453) · UniProt [P23381](https://www.uniprot.org/uniprotkb/P23381) · Ensembl [ENSG00000140105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140105)

## Data

Gene col 6374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6374); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6374]; `tensor/DDL_lfc|DDL_z.npy` [6374]; `embed/gene_vectors.npy` [6374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6374 or target_col == 6374). Every well: [[WARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
