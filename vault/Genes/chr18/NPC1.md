---
symbol: "NPC1"
type: "gene"
col: 6526
ensembl_id: "ENSG00000141458"
name: "NPC intracellular cholesterol transporter 1"
location: "18q11.2"
module: 34
arm: "+"
pooled_cpm: 202.05
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 19
n_dd_up_clean: 25
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# NPC1

*NPC intracellular cholesterol transporter 1* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.65× (z +7.5, q 3e-11, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.579× (z -8.7, q 2e-15, down in 40 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.645× (z -7.0, q 5e-10, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST3GAL1]] (+0.65, fdr 7e-06), [[LDLR]] (+0.62, fdr 7e-06), [[STRIP2]] (+0.61, fdr 1e-05); moves opposite to [[KCTD3]] (-0.57, fdr 1e-05), [[TRUB1]] (-0.56, fdr 1e-05), [[PAIP1]] (-0.56, fdr 2e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LAMA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +7.5 | 3e-11 | 38/47 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.38×** | +7.3 | 6e-11 | 41/47 (NCI-H23, LS 180, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +6.3 | 5e-08 | 34/47 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Berbamine (drug)]] 5 µM |  | **1.31×** | +6.1 | 1e-07 | 36/48 (LS 180, NCI-H23, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.44×** | +5.8 | 6e-07 | 35/46 (RKO, SW48, …) | two highest doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +5.8 | 8e-07 | 27/47 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +5.5 | 3e-06 | 31/47 (AsPC-1, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +5.5 | 3e-06 | 32/47 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +5.2 | 1e-05 | 33/47 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.39×** | +5.0 | 3e-05 | 30/46 (SW48, RKO, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.33×** | +4.4 | 7e-04 | 33/47 (HOP62, HS-578T, …) | top dose only |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.001 | 30/47 (HEC-1-A, hTERT-HPNE, …) | top dose only | plate-row cell shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.30×** | +4.2 | 0.001 | 28/47 (SHP-77, Panc 03.27, …) | rises with dose |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.002 | 30/47 (HEC-1-A, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.004 | 26/47 (AsPC-1, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.005 | 26/48 (A-172, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6526.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.579×** | -8.7 | 2e-15 | 40/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.597×** | -7.9 | 7e-13 | 32/43 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.645×** | -7.0 | 5e-10 | 37/47 (C32, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.633×** | -6.8 | 2e-09 | 33/44 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.742×** | -6.7 | 2e-09 | 35/47 (C32, AsPC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.754×** | -6.4 | 2e-08 | 32/47 (SK-MEL-2, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.693×** | -5.6 | 1e-06 | 29/47 (C32, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.522×** | -5.4 | 4e-06 | 39/47 (CFPAC-1, A-427, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.702×** | -5.4 | 4e-06 | 32/46 (CFPAC-1, C32, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.753×** | -4.5 | 3e-04 | 30/47 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.748×** | -4.5 | 4e-04 | 31/47 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.772×** | -4.1 | 0.002 | 29/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.774×** | -4.1 | 0.002 | 28/47 (C32, A-172, …) | two highest doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.844× | -3.8 | 0.005 | 19/48 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.810×** | -3.6 | 0.014 | 24/48 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.803×** | -3.5 | 0.016 | 26/47 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.851× | -3.1 | 0.067 | 17/47 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.698×** | -3.0 | 0.077 | 19/48 (NCI-H1792, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.865× | -2.9 | 0.081 | 20/47 (C32, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.878× | -2.9 | 0.081 | 16/48 (C32, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 760 | 0 | 24 (8 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.146× (z -17.5) |
| [[A-172 (line)]] | wt | 249 | 7 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.18× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 92.1 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +21.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.13× (z +15.4) | — |
| [[SW480 (line)]] | alt | 127 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.11× (z +22.9) | — |
| [[CFPAC-1 (line)]] | alt | 322 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 268 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.503× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 398 | 1 | 3 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.08× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.585× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 111 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.72× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 527 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 285 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.24× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SHP-77 (line)]] | alt | 73.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.10× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 181 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 236 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -10.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 192 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 383 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 122 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cepharanthine (drug)]] 5 µM 1.94× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 174 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.602× (z -8.5) |
| [[A-427 (line)]] | wt | 247 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 217 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -15.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 260 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 180 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[C-33 A (line)]] | alt | 74.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.82× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[H4 (line)]] | wt | 260 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HepG2_C3A (line)]] | wt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[Hs 766T (line)]] | wt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[hTERT-HPNE (line)]] | wt | 176 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 203 | 0 | 1 | — | [[Radotinib (drug)]] 5 µM 0.531× (z -8.7) |
| [[LS 180 (line)]] | wt | 113 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 1.82× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 131 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 171 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 87.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 1088 (line)]] | alt | 164 | 0 | 1 (1 ⚠) | — | [[Carbidopa (monohydrate) (drug)]] 0.5 µM 0.0428× (z -15.1) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 248 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[AN3 CA (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 179 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 258 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 182 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 147 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL1]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[LDLR]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 | pathway: LDL clearance |
| [[STRIP2]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[LRRFIP1]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PLEKHM1]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PLEKHM1P1]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[TUT7]] | +0.59 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[WNT2B]] | +0.58 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[LIPG]] | +0.56 | +0.55 / +0.49 | both halves | 1e-05 | pathway: Plasma lipoprotein assembly, remodeling, and clearance |
| [[C11orf91]] | +0.55 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[FRMD8]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SEPTIN10]] | +0.55 | +0.58 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD3]] | -0.57 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[TRUB1]] | -0.56 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[PAIP1]] | -0.56 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[CEPT1]] | -0.55 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[POMK]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[RBM26]] | -0.54 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[CAND1]] | -0.54 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[SMG7]] | -0.53 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[PUM2]] | -0.52 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[RAF1]] | -0.52 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[COX11]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[RCHY1]] | -0.51 | -0.46 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA3]] | B | LAMA3 activity raises NPC1's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.48× lower at baseline in the lines without LAMA3 | 0.003 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[C11orf91]] | B | C11orf91 activity raises NPC1's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.96× lower at baseline in the lines without C11orf91 | 0.066 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[ST3GAL1]] | B | ST3GAL1 activity raises NPC1's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without ST3GAL1 | 0.091 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[LHFPL2]] | C | LHFPL2 activity raises NPC1's level | lines that do not express LHFPL2 (4) vs lines expressing it (46) | 1.84× lower at baseline in the lines without LHFPL2 | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, SESTD1, HIPK2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.8, -48.1); signed map (-8.9, 44.4). **Vector** length 148, 53.6% of its response variance represented; |z| ≥ 3 in 1,858 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.5 | +5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.7 | +7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.6 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.5 | +5.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +6.1 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +5.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.9 | +5.8 |
|  | [[Berbamine (drug)]] 5 µM |  | +5.9 | +6.1 |
| fall | [[Radotinib (drug)]] 5 µM |  | -6.8 | -6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.7 | -7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.9 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.9 | +0.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -5.5 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.3 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | NPC intracellular cholesterol transporter 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:23,506,184-23,586,506 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLC65A1 |
| Gene groups (HGNC) | Solute carrier family 65 |
| Hallmark sets | BILE_ACID_METABOLISM, XENOBIOTIC_METABOLISM |
| Reactome | 4 pathways, smallest: LDL clearance; Plasma lipoprotein clearance; Plasma lipoprotein assembly, remodeling, and clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [O15118](https://www.uniprot.org/uniprotkb/O15118) (NPC intracellular cholesterol transporter 1):

> Intracellular cholesterol transporter which acts in concert with NPC2 and plays an important role in the egress of cholesterol from the endosomal/lysosomal compartment. Unesterified cholesterol that has been released from LDLs in the lumen of the late endosomes/lysosomes is transferred by NPC2 to the cholesterol-binding pocket in the N-terminal domain of NPC1. Cholesterol binds to NPC1 with the hydroxyl group buried in the binding pocket. Mediates cholesterol transfer from lysosomes to …

**Summary**, from NCBI Gene [4864](https://www.ncbi.nlm.nih.gov/gene/4864):

> This gene encodes a large protein that resides in the limiting membrane of endosomes and lysosomes and mediates intracellular cholesterol trafficking via binding of cholesterol to its N-terminal domain. It is predicted to have a cytoplasmic C-terminus, 13 transmembrane domains, and 3 large loops in the lumen of the endosome - the last loop being at the N-terminus. This protein transports low-density lipoproteins to late endosomal/lysosomal compartments where they are hydrolized and released as …

**Accessions** — [HGNC:7897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7897) · Entrez [4864](https://www.ncbi.nlm.nih.gov/gene/4864) · UniProt [O15118](https://www.uniprot.org/uniprotkb/O15118) · Ensembl [ENSG00000141458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141458)

## Data

Gene col 6526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6526); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6526]; `tensor/DDL_lfc|DDL_z.npy` [6526]; `embed/gene_vectors.npy` [6526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6526 or target_col == 6526). Every well: [[NPC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
