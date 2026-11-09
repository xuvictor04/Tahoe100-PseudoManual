---
symbol: "CAND1"
type: "gene"
col: 3238
ensembl_id: "ENSG00000111530"
name: "cullin associated and neddylation dissociated 1"
location: "12q14.3-q15"
module: 25
arm: "+"
pooled_cpm: 136.39
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# CAND1

*cullin associated and neddylation dissociated 1* — 12q14.3-q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.16× (z +18.5, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.648× (z -13.3, q 8e-38, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDH1]] (+0.65, fdr 7e-06), [[KCTD3]] (+0.60, fdr 1e-05), [[ZNF639]] (+0.60, fdr 2e-05); moves opposite to [[WNT9A]] (-0.57, fdr 1e-05), [[TM4SF19-DYNLT2B]] (-0.56, fdr 4e-05), [[CATSPERG]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3238.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.16×** | +18.5 | 0e+00 | 48/49 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +14.0 | 7e-42 | 45/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +6.0 | 3e-07 | 0/50 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.21×** | +5.6 | 3e-06 | 25/48 (A549, PANC-1, …) | rises with dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.38×** | +5.2 | 3e-05 | 26/47 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.13× | +3.8 | 0.012 | 15/48 (A549, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +3.8 | 0.013 | 16/47 (SW1417, LOX-IMVI, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.13× | +3.7 | 0.016 | 2/48 (hTERT-HPNE, CHP-212) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.13× | +3.5 | 0.030 | 14/47 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.030 | 16/49 (NCI-H2030, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.08× | +3.0 | 0.12 | 0/48 | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3238.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.648×** | -13.3 | 8e-38 | 47/48 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.669×** | -12.4 | 1e-32 | 46/48 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.661×** | -11.7 | 1e-29 | 33/45 (SW48, H4, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.700×** | -10.9 | 1e-25 | 40/48 (SW480, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.791×** | -9.6 | 6e-20 | 28/49 (A549, SNU-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.761×** | -8.4 | 4e-15 | 37/48 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.765×** | -7.9 | 2e-13 | 28/47 (NCI-H2347, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | 0.839× | -5.4 | 5e-06 | 23/49 (SW48, HEC-1-A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | 0.837× | -5.3 | 9e-06 | 22/44 (HCT15, KATO III, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.893× | -3.5 | 0.027 | 11/48 (CHP-212, A498, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.894× | -3.5 | 0.028 | 3/48 (SW480, SW1417, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | 0.895× | -3.4 | 0.028 | 13/48 (BT-474, Hs 766T, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.845× | -3.3 | 0.037 | 14/49 (LS 180, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.819×** | -3.2 | 0.053 | 14/47 (A498, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.902× | -3.2 | 0.055 | 3/48 (SW 900, H4, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.853× | -3.1 | 0.061 | 14/48 (A-427, NCI-H2347, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.927× | -3.0 | 0.099 | 7/48 (NCI-H2347, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 145 | 2 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.75× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.421× (z -15.1) |
| [[KATO III (line)]] | alt | 111 | 2 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.72× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.449× (z -13.0) |
| [[SW480 (line)]] | alt | 125 | 2 | 4 | [[TAK-901 (drug)]] 5 µM 4.25× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.557× (z -11.4) |
| [[A-427 (line)]] | wt | 202 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 4.33× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -13.3) |
| [[A549 (line)]] | wt | 137 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +15.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.36× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -12.1) ⚠ cell-cycle shift, explains ~12% of this change |
| [[PANC-1 (line)]] | alt | 147 | 4 (2 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 4.60× (z +15.0) | [[Panobinostat (drug)]] 0.5 µM 0.633× (z -8.6) |
| [[BT-474 (line)]] | alt | 118 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.22× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 130 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.559× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 146 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 3.33× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.595× (z -10.1) |
| [[SW1417 (line)]] | alt | 139 | 3 | 1 | [[TAK-901 (drug)]] 5 µM 3.69× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.543× (z -9.8) |
| [[LoVo (line)]] | wt | 166 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.06× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.632× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[LOX-IMVI (line)]] | wt | 148 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 4.36× (z +11.5) | — |
| [[LS 180 (line)]] | wt | 137 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.43× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.464× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 136 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.52× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.547× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[NCI-H2347 (line)]] | alt | 147 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.485× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~18% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.564× (z -10.1) |
| [[SW 900 (line)]] | alt | 196 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.462× (z -9.9) |
| [[SW48 (line)]] | wt | 138 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.65× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -13.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 155 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.592× (z -9.1) |
| [[C32 (line)]] | wt | 137 | 1 | 1 | [[PH-797804 (drug)]] 5 µM 6.72× (z +12.2) | [[Auranofin (drug)]] 5 µM 0.444× (z -10.0) |
| [[COLO 205 (line)]] | alt | 116 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.09× (z +12.4) | — |
| [[H4 (line)]] | wt | 139 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 168 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.508× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 118 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.40× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 189 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.60× (z +12.1) | [[Auranofin (drug)]] 5 µM 0.556× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 80.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.71× (z +11.1) | — |
| [[RKO (line)]] | wt | 197 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.36× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 128 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0680× (z -14.5) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -9.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 169 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.64× (z +9.0) | — |
| [[CHP-212 (line)]] | wt | 144 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -9.1) ⚠ cell-cycle shift, explains ~12% of this change |
| [[HT-29 (line)]] | alt | 105 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.43× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 100 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.47× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.513× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 147 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 128 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 127 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 158 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDH1]] | +0.65 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[KCTD3]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ZNF639]] | +0.60 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[C2CD5]] | +0.60 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[ZMYM3]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ERLIN1]] | +0.57 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TUBGCP3]] | +0.56 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[WBP11]] | +0.56 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[HNRNPR]] | +0.56 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ERH]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SNX17]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ZBTB14]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WNT9A]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[TM4SF19-DYNLT2B]] | -0.56 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[CATSPERG]] | -0.56 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[ADGRL1-AS1]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[CLN8]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[NPC1]] | -0.54 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[IER5]] | -0.53 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[EXD3]] | -0.52 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[ZNF83]] | -0.52 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[TPT1-AS1]] | -0.51 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[LINC01128]] | -0.51 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[RAB7A]] | -0.51 | -0.40 / -0.54 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CAND1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.405). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.1, 0.6); signed map (-3.9, -36.3). **Vector** length 106, 29.1% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.4 | +18.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.8 | +14.0 |
|  | [[NG25 (drug)]] 5 µM |  | +4.8 | +5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +4.7 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +3.8 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.3 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.4 | -0.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.2 | +0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.8 | -10.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | -6.1 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.7 | -11.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | cullin associated and neddylation dissociated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.3-q15 — chr12:67,269,358-67,319,953 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIP120A, DKFZp434M1414, KIAA0829, TIP120 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Reactome | 5 pathways, smallest: Iron uptake and transport; Neddylation; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VP6](https://www.uniprot.org/uniprotkb/Q86VP6) (Cullin-associated NEDD8-dissociated protein 1):

> Key assembly factor of SCF (SKP1-CUL1-F-box protein) E3 ubiquitin ligase complexes that promotes the exchange of the substrate-recognition F-box subunit in SCF complexes, thereby playing a key role in the cellular repertoire of SCF complexes. Acts as a F-box protein exchange factor. The exchange activity of CAND1 is coupled with cycles of neddylation conjugation: in the deneddylated state, cullin-binding CAND1 binds CUL1-RBX1, increasing dissociation of the SCF complex and promoting exchange of …

**Summary**, from NCBI Gene [55832](https://www.ncbi.nlm.nih.gov/gene/55832):

> This gene encodes an essential regulator of Cullin-RING ubiquitin ligases, which are in involved in ubiquitinylation of proteins degraded by the Ub proteasome system. The encoded protein binds to unneddylated cullin-RING box protein complexes and acts as an inhibitor of cullin neddylation and of Skp1, cullin, and F box ubiquitin ligase complex assembly and activity. In mammalian cell culture, this protein predominantly localizes to the cytoplasm. Knockdown of this gene in preadipocytes results …

**Accessions** — [HGNC:30688](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30688) · Entrez [55832](https://www.ncbi.nlm.nih.gov/gene/55832) · UniProt [Q86VP6](https://www.uniprot.org/uniprotkb/Q86VP6) · Ensembl [ENSG00000111530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111530)

## Data

Gene col 3238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3238); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3238]; `tensor/DDL_lfc|DDL_z.npy` [3238]; `embed/gene_vectors.npy` [3238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3238 or target_col == 3238). Every well: [[CAND1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAND1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
