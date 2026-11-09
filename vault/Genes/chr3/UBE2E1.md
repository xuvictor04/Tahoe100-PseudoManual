---
symbol: "UBE2E1"
type: "gene"
col: 9906
ensembl_id: "ENSG00000170142"
name: "ubiquitin conjugating enzyme E2 E1"
location: "3p24.2"
module: 98
arm: "+"
pooled_cpm: 203.92
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# UBE2E1

*ubiquitin conjugating enzyme E2 E1* — 3p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.38× (z +7.8, q 3e-12, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.196× (z -39.4, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1M]] (+0.62, fdr 3e-05), [[FLVCR2]] (+0.60, fdr 1e-05), [[HIF1A]] (+0.60, fdr 2e-05); moves opposite to [[DPP9]] (-0.52, fdr 2e-04), [[EP400P1]] (-0.52, fdr 3e-05), [[ADAMTS16]] (-0.52, fdr 5e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TLR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9906.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +7.8 | 3e-12 | 32/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +5.2 | 6e-05 | 25/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +5.1 | 7e-05 | 26/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +4.6 | 6e-04 | 25/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.039 | 18/47 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.10 | 14/47 (Hs 766T, CHP-212, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 1.29× | +3.2 | 0.10 | 19/48 (AsPC-1, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9906.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.196×** | -39.4 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.210×** | -37.7 | 0e+00 | 47/47 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.292×** | -29.8 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.515×** | -16.1 | 0e+00 | 46/47 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -13.8 | 4e-41 | 36/48 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.643×** | -10.7 | 1e-24 | 44/47 (SW 1088, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.730×** | -7.3 | 2e-11 | 33/46 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.743×** | -6.9 | 4e-10 | 35/49 (SNU-423, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.580×** | -6.9 | 4e-10 | 40/48 (SNU-423, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **0.768×** | -6.1 | 5e-08 | 22/43 (LoVo, HEC-1-A, …) | all doses, flat | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.785×** | -5.8 | 3e-07 | 35/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **0.780×** | -5.6 | 1e-06 | 23/44 (RKO, NCI-H2347, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.796×** | -5.3 | 5e-06 | 29/47 (SNU-423, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.811×** | -5.1 | 2e-05 | 23/48 (NCI-H2347, SW1417, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.815×** | -4.9 | 3e-05 | 25/47 (SW 900, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.895× | -3.8 | 0.005 | 14/47 (SK-MEL-2, LOX-IMVI, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.756×** | -3.5 | 0.011 | 23/47 (CFPAC-1, J82, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 448 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -23.3) |
| [[A-172 (line)]] | wt | 223 | 1 (1 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.155× (z -28.2) |
| [[HS-578T (line)]] | alt | 175 | 4 (3 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.201× (z -23.2) |
| [[SW1417 (line)]] | alt | 322 | 2 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -25.6) |
| [[SW480 (line)]] | alt | 190 | 4 (1 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +14.8) | [[Panobinostat (drug)]] 5 µM 0.153× (z -39.1) |
| [[PANC-1 (line)]] | alt | 182 | 5 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.209× (z -26.6) |
| [[SK-MEL-2 (line)]] | alt | 255 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -29.7) |
| [[SNU-423 (line)]] | alt | 289 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -28.9) |
| [[A498 (line)]] | wt | 110 | 3 (3 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.234× (z -22.5) |
| [[AsPC-1 (line)]] | alt | 158 | 2 | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.155× (z -25.3) |
| [[LoVo (line)]] | wt | 223 | 2 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.192× (z -31.0) |
| [[LOX-IMVI (line)]] | wt | 223 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -25.3) |
| [[NCI-H1573 (line)]] | alt | 143 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -21.3) |
| [[SW 900 (line)]] | alt | 177 | 2 | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.221× (z -19.7) |
| [[C32 (line)]] | wt | 219 | 1 | 5 | [[Ponatinib (drug)]] 5 µM 3.10× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.196× (z -22.6) |
| [[CFPAC-1 (line)]] | alt | 156 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -25.6) |
| [[HEC-1-A (line)]] | alt | 327 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -24.3) |
| [[Hs 766T (line)]] | wt | 134 | 3 | 3 | [[Triamcinolone (drug)]] 0.5 µM 2.27× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -18.5) |
| [[LS 180 (line)]] | wt | 192 | 2 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.189× (z -25.6) |
| [[MIA PaCa-2 (line)]] | alt | 152 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -28.6) |
| [[NCI-H1792 (line)]] | alt | 289 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -20.7) |
| [[NCI-H460 (line)]] | wt | 161 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -28.6) |
| [[A549 (line)]] | wt | 295 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -22.4) |
| [[hTERT-HPNE (line)]] | wt | 212 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -20.5) |
| [[NCI-H23 (line)]] | alt | 90.8 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 263 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -30.5) |
| [[RKO (line)]] | wt | 233 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -21.7) |
| [[RPMI-7951 (line)]] | alt | 283 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -23.8) |
| [[SHP-77 (line)]] | alt | 157 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.234× (z -18.4) |
| [[SW48 (line)]] | wt | 277 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -21.8) |
| [[BT-474 (line)]] | alt | 208 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -19.1) |
| [[CHP-212 (line)]] | wt | 237 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -14.8) |
| [[H4 (line)]] | wt | 123 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.166× (z -18.2) |
| [[HCT15 (line)]] | alt | 303 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -19.3) |
| [[HepG2_C3A (line)]] | wt | 114 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.284× (z -12.5) |
| [[HOP62 (line)]] | alt | 255 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -29.7) |
| [[HT-29 (line)]] | alt | 125 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -20.1) |
| [[J82 (line)]] | alt | 200 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -21.6) |
| [[SNU-1 (line)]] | wt | 211 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -19.9) |
| [[A-427 (line)]] | wt | 157 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -17.5) |
| [[AN3 CA (line)]] | alt | 249 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.156× (z -15.7) |
| [[C-33 A (line)]] | alt | 213 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -19.3) |
| [[COLO 205 (line)]] | alt | 110 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -17.2) |
| [[NCI-H2030 (line)]] | alt | 174 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -17.0) |
| [[SW 1088 (line)]] | alt | 218 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.0984× (z -11.9) |
| [[SW 1271 (line)]] | alt | 313 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -10.6) |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -8.6) |
| [[KATO III (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 208 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1M]] | +0.62 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[FLVCR2]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[HIF1A]] | +0.60 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[TLR2]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[PDZD2]] | +0.57 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[STOM]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[KLF9]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[MAOA]] | +0.56 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ATOH8]] | +0.55 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[ADGRG2]] | +0.55 | +0.42 / +0.40 | both halves | 4e-05 |  |
| [[RIPOR2]] | +0.55 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[IRAK3]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP9]] | -0.52 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[EP400P1]] | -0.52 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ADAMTS16]] | -0.52 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[SYNJ2]] | -0.51 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[EHD1]] | -0.50 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[TM4SF1]] | -0.50 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[WNT7B]] | -0.50 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[MMP1]] | -0.49 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[ANTXR2]] | -0.49 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[MANCR]] | -0.48 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[KRT15]] | -0.48 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[EFL1]] | -0.47 | -0.36 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLR2]] | B | TLR2 activity raises UBE2E1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.42× lower at baseline in the lines without TLR2 | 0.022 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[ADAMTS16]] | B | ADAMTS16 activity raises UBE2E1's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 1.26× lower at baseline in the lines without ADAMTS16 | 0.035 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[EPS8]] | B | EPS8 activity raises UBE2E1's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 1.29× lower at baseline in the lines without EPS8 | 0.074 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises UBE2E1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.5, 16.9); signed map (18.1, 29.8). **Vector** length 101, 32.1% of its response variance represented; |z| ≥ 3 in 1,338 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.2 | -5.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.6 | +1.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +4.5 | +2.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +4.5 | +3.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.4 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.4 | +2.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -10.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.4 | -16.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.2 | -4.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 E1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.2 — chr3:23,805,955-23,891,640 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UbcH6 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 49 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [P51965](https://www.uniprot.org/uniprotkb/P51965) (Ubiquitin-conjugating enzyme E2 E1):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. Catalyzes the covalent attachment of ISG15 to other proteins. Mediates the selective degradation of short-lived and abnormal proteins. In vitro also catalyzes 'Lys-48'-linked polyubiquitination. Catalyzes monoubiquitination of other proteins in both an E3-dependent and E3-independent manner.

**Summary**, from NCBI Gene [7324](https://www.ncbi.nlm.nih.gov/gene/7324):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. Three alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. …

**Accessions** — [HGNC:12477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12477) · Entrez [7324](https://www.ncbi.nlm.nih.gov/gene/7324) · UniProt [P51965](https://www.uniprot.org/uniprotkb/P51965) · Ensembl [ENSG00000170142](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170142)

## Data

Gene col 9906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9906); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9906]; `tensor/DDL_lfc|DDL_z.npy` [9906]; `embed/gene_vectors.npy` [9906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9906 or target_col == 9906). Every well: [[UBE2E1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2E1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
