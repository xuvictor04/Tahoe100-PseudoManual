---
symbol: "PARP14"
type: "gene"
col: 10351
ensembl_id: "ENSG00000173193"
name: "poly(ADP-ribose) polymerase family member 14"
location: "3q21.1"
module: 32
arm: "+"
pooled_cpm: 297.74
n_lines_expressing: 47
n_dd_up: 28
n_dd_down: 59
n_dd_up_clean: 26
n_dd_down_clean: 45
in_vector_space: true
direction_upstream: 69
direction_downstream: 25
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# PARP14

*poly(ADP-ribose) polymerase family member 14* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.00× (z +8.8, q 8e-16, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 59 drug-doses (14 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.174× (z -22.1, q 0e+00, down in 45 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIT3]] (+0.93, fdr 7e-06), [[DDX60]] (+0.92, fdr 7e-06), [[PARP9]] (+0.92, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 69 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 25 go from it, the strongest it → [[SAMHD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 2 with an alert ⚠; shown: the 15 strongest. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10351.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.00×** | +8.8 | 8e-16 | 38/45 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +8.2 | 6e-14 | 33/45 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.88×** | +7.7 | 2e-12 | 42/44 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.44×** | +5.9 | 6e-07 | 38/45 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.55×** | +5.8 | 8e-07 | 38/46 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.55×** | +5.6 | 2e-06 | 37/44 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.46×** | +5.4 | 5e-06 | 35/47 (AsPC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.41×** | +5.4 | 5e-06 | 37/45 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +5.1 | 2e-05 | 35/45 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.0 | 3e-05 | 26/45 (HEC-1-A, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.30×** | +4.7 | 1e-04 | 32/45 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.42×** | +4.5 | 3e-04 | 33/46 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +4.5 | 3e-04 | 30/46 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.45×** | +4.5 | 3e-04 | 32/45 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.40×** | +4.0 | 0.002 | 33/46 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 59 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 59 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10351.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.174×** | -22.1 | 0e+00 | 45/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.178×** | -21.8 | 0e+00 | 45/45 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.206×** | -20.0 | 0e+00 | 45/45 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.419×** | -15.5 | 0e+00 | 33/46 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.507×** | -12.1 | 9e-32 | 35/46 (COLO 205, BT-474, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.410×** | -11.3 | 2e-27 | 44/46 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.412×** | -11.2 | 4e-27 | 35/45 (BT-474, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.420×** | -11.0 | 4e-26 | 44/45 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.548×** | -10.7 | 5e-25 | 35/45 (COLO 205, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.449×** | -10.1 | 3e-22 | 35/46 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.467×** | -9.6 | 4e-20 | 44/45 (BT-474, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.529×** | -7.7 | 6e-13 | 37/44 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.569×** | -7.1 | 5e-11 | 35/45 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.697×** | -6.4 | 5e-09 | 35/46 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.703×** | -6.3 | 1e-08 | 38/45 (NCI-H460, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.623×** | -6.0 | 9e-08 | 32/45 (HepG2/C3A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.419×** | -5.7 | 3e-07 | 41/46 (A-172, SHP-77, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10351. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 429 | 0 | 23 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0743× (z -21.7) |
| [[A-172 (line)]] | wt | 450 | 3 | 17 (5 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 3.26× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.110× (z -22.2) |
| [[A549 (line)]] | wt | 441 | 0 | 20 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0878× (z -17.8) |
| [[LoVo (line)]] | wt | 477 | 1 | 18 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.0687× (z -25.8) |
| [[MIA PaCa-2 (line)]] | alt | 370 | 2 (1 ⚠) | 16 (4 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.51× (z +10.1) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.51× (z +8.7) | [[Belinostat (drug)]] 5 µM 0.0690× (z -18.6) |
| [[CFPAC-1 (line)]] | alt | 604 | 6 (1 ⚠) | 11 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.36× (z +11.2) | [[Tofacitinib (drug)]] 5 µM 0.250× (z -18.9) |
| [[NCI-H1573 (line)]] | alt | 324 | 1 | 16 (5 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.78× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.0785× (z -21.0) |
| [[SNU-423 (line)]] | alt | 441 | 1 | 15 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +9.3) | [[Belinostat (drug)]] 5 µM 0.0924× (z -19.5) |
| [[HepG2_C3A (line)]] | wt | 237 | 0 | 15 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -15.8) |
| [[HS-578T (line)]] | alt | 485 | 3 | 12 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.52× (z +12.9) | [[Belinostat (drug)]] 5 µM 0.168× (z -15.3) |
| [[NCI-H1792 (line)]] | alt | 423 | 0 | 15 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -18.5) |
| [[NCI-H23 (line)]] | alt | 261 | 0 | 14 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0589× (z -17.8) |
| [[RKO (line)]] | wt | 310 | 0 | 14 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0752× (z -23.3) |
| [[NCI-H2347 (line)]] | alt | 582 | 4 (1 ⚠) | 9 | [[Homoharringtonine (drug)]] 0.5 µM 4.14× (z +14.0) | [[Tofacitinib (drug)]] 5 µM 0.341× (z -15.0) |
| [[RPMI-7951 (line)]] | alt | 563 | 1 | 12 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.57× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.147× (z -17.6) |
| [[C-33 A (line)]] | alt | 173 | 0 | 11 | — | [[Belinostat (drug)]] 5 µM 0.0934× (z -17.0) |
| [[COLO 205 (line)]] | alt | 944 | 0 | 11 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -20.5) |
| [[HEC-1-A (line)]] | alt | 134 | 6 (2 ⚠) | 5 | [[Harringtonine (drug)]] 0.5 µM 4.43× (z +18.5) | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -17.7) |
| [[NCI-H460 (line)]] | wt | 135 | 5 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.7) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.26× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.196× (z -19.4) |
| [[SHP-77 (line)]] | alt | 177 | 0 | 11 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0835× (z -19.5) |
| [[A498 (line)]] | wt | 378 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 275 | 2 | 6 | [[Cobimetinib (drug)]] 5 µM 3.01× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -13.9) |
| [[KATO III (line)]] | alt | 347 | 1 | 7 | [[Harringtonine (drug)]] 0.5 µM 3.19× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.0926× (z -19.0) |
| [[PANC-1 (line)]] | alt | 227 | 2 | 6 | [[Harringtonine (drug)]] 0.5 µM 3.56× (z +14.8) | [[Panobinostat (drug)]] 5 µM 0.291× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 393 | 2 | 6 | [[Homoharringtonine (drug)]] 0.5 µM 3.32× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -15.0) |
| [[SW1417 (line)]] | alt | 339 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -12.6) |
| [[C32 (line)]] | wt | 140 | 3 | 4 | [[Harringtonine (drug)]] 0.5 µM 3.03× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.164× (z -15.4) |
| [[HCT15 (line)]] | alt | 257 | 3 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +14.3) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.87× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.154× (z -20.0) |
| [[J82 (line)]] | alt | 298 | 6 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +9.6) | [[Tofacitinib (drug)]] 5 µM 0.478× (z -10.0) |
| [[SW480 (line)]] | alt | 86.2 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.153× (z -22.3) |
| [[CHP-212 (line)]] | wt | 281 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.107× (z -13.5) |
| [[Hs 766T (line)]] | wt | 279 | 1 | 4 | [[Cobimetinib (drug)]] 5 µM 3.08× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 807 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 3.04× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.275× (z -11.0) |
| [[SNU-1 (line)]] | wt | 180 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -16.0) |
| [[SW 900 (line)]] | alt | 280 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.226× (z -14.0) |
| [[A-427 (line)]] | wt | 84.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.231× (z -13.6) |
| [[AN3 CA (line)]] | alt | 145 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -10.8) |
| [[H4 (line)]] | wt | 216 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -13.8) |
| [[HT-29 (line)]] | alt | 261 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -18.5) |
| [[LOX-IMVI (line)]] | wt | 99.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -12.2) |
| [[LS 180 (line)]] | wt | 144 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -14.4) |
| [[SW48 (line)]] | wt | 115 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 127 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.34× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 61.7 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 68.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10351), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIT3]] | +0.93 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 705 |
| [[DDX60]] | +0.92 | +0.88 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 667 |
| [[PARP9]] | +0.92 | +0.89 / +0.94 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 942 |
| [[DDX60L]] | +0.92 | +0.88 / +0.92 | both halves | 7e-06 | STRING 582 |
| [[DTX3L]] | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | STRING 975 |
| [[HERC6]] | +0.91 | +0.88 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 569 |
| [[RSAD2]] | +0.91 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 751 |
| [[IFIH1]] | +0.91 | +0.90 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 879 |
| [[NMI]] | +0.91 | +0.87 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[SAMD9L]] | +0.91 | +0.82 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 841 |
| [[XAF1]] | +0.91 | +0.81 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 824 |
| [[OAS2]] | +0.90 | +0.82 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 751 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 54, C 15. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises PARP14's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.56× lower at baseline in the lines without OAS2 | 4e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[IFI6]] | B | IFI6 activity raises PARP14's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without IFI6 | 5e-04 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises PARP14's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.55× lower at baseline in the lines without OAS1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises PARP14's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.34× lower at baseline in the lines without MX1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[SAMD9L]] | B | SAMD9L activity raises PARP14's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.11× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[GBP4]] | B | GBP4 activity raises PARP14's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.33× lower at baseline in the lines without GBP4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[RSAD2]] | B | RSAD2 activity raises PARP14's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.38× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[CD5L]] | B | CD5L activity raises PARP14's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.18× lower at baseline in the lines without CD5L | 0.002 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[PARP9]] | B | PARP9 activity raises PARP14's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 3.18× lower at baseline in the lines without PARP9 | 0.002 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[ETV7]] | B | ETV7 activity raises PARP14's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 1.96× lower at baseline in the lines without ETV7 | 0.002 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises PARP14's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.47× lower at baseline in the lines without TRIM22 | 0.002 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[PLSCR1]] | B | PLSCR1 activity raises PARP14's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.83× lower at baseline in the lines without PLSCR1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 0, C 25. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMHD1]] | C | PARP14's natural level strengthens SAMHD1's drug response | PARP14's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.83, reverse +0.61; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[NMI]] | C | PARP14's natural level strengthens NMI's drug response | PARP14's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.79, reverse +0.39; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF9]] | C | PARP14's natural level strengthens IRF9's drug response | PARP14's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.75; direction not clear | 0.005 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PSMB9]] | C | PARP14's natural level strengthens PSMB9's drug response | PARP14's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.17; direction clear | 0.014 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |
| [[IFIT5]] | C | PARP14's natural level strengthens IFIT5's drug response | PARP14's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.68; direction not clear | 0.027 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM25]] | C | PARP14's natural level strengthens TRIM25's drug response | PARP14's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.57; direction not clear | 0.029 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | PARP14's natural level strengthens ADAR's drug response | PARP14's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.76; direction not clear | 0.042 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PLSCR1]] | C | [[DTX3L]], PARP14 activity raises PLSCR1's level | lines that do not express DTX3L, PARP14 (3) vs lines expressing them (47) | 4.95× lower at baseline in the lines without DTX3L, PARP14 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CRYBG3, TTC39C; maybe low, not absent; its own permutation p; co-absent genes |
| [[CMPK2]] | C | [[DTX3L]], PARP14 activity raises CMPK2's level | lines that do not express DTX3L, PARP14 (3) vs lines expressing them (47) | 4.48× lower at baseline in the lines without DTX3L, PARP14 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CRYBG3, TTC39C; maybe low, not absent; its own permutation p; co-absent genes |
| [[PARP9]] | C | [[DTX3L]], PARP14 activity raises PARP9's level | lines that do not express DTX3L, PARP14 (3) vs lines expressing them (47) | 4.44× lower at baseline in the lines without DTX3L, PARP14 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CRYBG3, TTC39C; maybe low, not absent; its own permutation p; co-absent genes |
| [[HERC6]] | C | [[DTX3L]], PARP14 activity raises HERC6's level | lines that do not express DTX3L, PARP14 (3) vs lines expressing them (47) | 3.81× lower at baseline in the lines without DTX3L, PARP14 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CRYBG3, TTC39C; maybe low, not absent; its own permutation p; co-absent genes |
| [[SP110]] | C | [[DTX3L]], PARP14 activity raises SP110's level | lines that do not express DTX3L, PARP14 (3) vs lines expressing them (47) | 3.53× lower at baseline in the lines without DTX3L, PARP14 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CRYBG3, TTC39C; maybe low, not absent; its own permutation p; co-absent genes |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.948). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.3, 53.7); signed map (63.5, 31.8). **Vector** length 171, 73.9% of its response variance represented; |z| ≥ 3 in 2,414 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.86 to 23); *Interferon Signaling* (reactome, mean cos +0.80 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.82 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +15.9 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +14.2 | +8.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.5 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +9.1 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.6 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.4 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +6.7 | +5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.4 | +5.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -12.4 | -15.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -11.2 | -12.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -10.9 | -11.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -9.9 | -10.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.7 | -10.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -9.4 | -11.3 |

## What is on record

|  |  |
|---|---|
| Name | poly(ADP-ribose) polymerase family member 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1 — chr3:122,680,839-122,730,840 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1268, pART8, ARTD8, BAL2 |
| Gene groups (HGNC) | Poly(ADP-ribose) polymerases; Macro domain containing |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 12 pathways, smallest: Maturation of nucleoprotein_9683610; Maturation of nucleoprotein_9694631; Nicotinate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q460N5](https://www.uniprot.org/uniprotkb/Q460N5) (Protein mono-ADP-ribosyltransferase PARP14):

> ADP-ribosyltransferase that mediates mono-ADP-ribosylation of glutamate residues on target proteins. In contrast to PARP1 and PARP2, it is not able to mediate poly-ADP-ribosylation. Has been shown to catalyze the mono-ADP-ribosylation of STAT1 at 'Glu-657' and 'Glu-705', thus decreasing STAT1 phosphorylation which negatively regulates pro-inflammatory cytokine production in macrophages in response to IFNG stimulation. However, the role of ADP-ribosylation in the prevention of STAT1 …

**Summary**, from NCBI Gene [54625](https://www.ncbi.nlm.nih.gov/gene/54625):

> This gene encodes a member of the poly(ADP-ribose) polymerase (PARP) protein family. The encoded anti-apoptotic protein may regulate aerobic glycolysis and promote survival of cancer cells. Increased expression of this gene has been reported in a variety of tumor types. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:29232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29232) · Entrez [54625](https://www.ncbi.nlm.nih.gov/gene/54625) · UniProt [Q460N5](https://www.uniprot.org/uniprotkb/Q460N5) · Ensembl [ENSG00000173193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173193)

## Data

Gene col 10351: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10351); `tables/drug_effects.parquet` (87 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10351, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10351]; `tensor/DDL_lfc|DDL_z.npy` [10351]; `embed/gene_vectors.npy` [10351]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10351 or target_col == 10351). Every well: [[PARP14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARP14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
