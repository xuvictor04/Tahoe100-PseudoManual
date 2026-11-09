---
symbol: "ANKRD10"
type: "gene"
col: 1534
ensembl_id: "ENSG00000088448"
name: "ankyrin repeat domain 10"
location: "13q34"
module: 15
arm: "+"
pooled_cpm: 193.51
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ANKRD10

*ankyrin repeat domain 10* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 1.95× (z +10.0, q 4e-21, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.612× (z -7.4, q 6e-11, down in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 4 lines (HEC-1-A 0.262×, LoVo 0.461×, KATO III 0.416×, HepG2/C3A 0.363×; ⚠ cell-cycle shift, explains ~33% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HEC-1-A 0.295×, LOX-IMVI 0.529×, SW480 0.627×); [[Panobinostat (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.245×, KATO III 0.421×, LoVo 0.526×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HEC-1-A 0.402×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARGLU1]] (+0.66, fdr 1e-05), [[RAD51-AS1]] (+0.61, fdr 1e-05), [[SLC16A4-AS1]] (+0.59, fdr 3e-05); moves opposite to [[GPATCH11]] (-0.57, fdr 3e-05), [[POLR3A]] (-0.56, fdr 2e-05), [[MEA1]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1534.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **1.95×** | +10.0 | 4e-21 | 43/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.95×** | +10.0 | 4e-21 | 40/48 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +9.9 | 6e-21 | 47/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +8.7 | 3e-16 | 42/47 (LoVo, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.72×** | +8.2 | 3e-14 | 43/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +7.9 | 2e-13 | 34/45 (SK-MEL-2, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +5.0 | 6e-05 | 33/48 (SHP-77, AN3 CA, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.36×** | +4.6 | 3e-04 | 31/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.5 | 4e-04 | 2/50 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +4.2 | 0.002 | 28/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.002 | 24/48 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.005 | 27/48 (LoVo, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.005 | 29/49 (A-172, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.18× | +3.5 | 0.020 | 23/48 (SNU-423, HS-578T, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1534.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 4 lines (HEC-1-A 0.262×, LoVo 0.461×, KATO III 0.416×, HepG2/C3A 0.363×; ⚠ cell-cycle shift, explains ~33% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HEC-1-A 0.295×, LOX-IMVI 0.529×, SW480 0.627×); [[Panobinostat (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.245×, KATO III 0.421×, LoVo 0.526×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HEC-1-A 0.402×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.612×** | -7.4 | 6e-11 | 46/48 (HEC-1-A, KATO III, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.674×** | -6.0 | 6e-07 | 42/48 (HEC-1-A, LoVo, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.724×** | -4.9 | 2e-04 | 34/48 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.834× | -3.9 | 0.014 | 24/48 (MIA PaCa-2, C-33 A, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.817× | -3.1 | 0.24 | 20/47 (hTERT-HPNE, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1534. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 536 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -18.7) |
| [[NCI-H460 (line)]] | wt | 117 | 8 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 4.10× (z +19.2) | — |
| [[KATO III (line)]] | alt | 295 | 5 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.20× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.416× (z -9.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.421× (z -9.5) |
| [[LoVo (line)]] | wt | 156 | 4 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.461× (z -10.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.526× (z -8.5) |
| [[HOP62 (line)]] | alt | 92.8 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 188 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +12.7) | — |
| [[AsPC-1 (line)]] | alt | 135 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +18.3) | — |
| [[C32 (line)]] | wt | 159 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.74× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +13.8) | — |
| [[NCI-H1792 (line)]] | alt | 64.7 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.10× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 116 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.99× (z +14.0) | — |
| [[SW 900 (line)]] | alt | 114 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.46× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.45× (z +9.0) | — |
| [[SW48 (line)]] | wt | 248 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.69× (z +14.2) | — |
| [[SW480 (line)]] | alt | 371 | 2 | 2 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.08× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.498× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.627× (z -8.9) |
| [[A-172 (line)]] | wt | 243 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +11.3) | — |
| [[COLO 205 (line)]] | alt | 546 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.05× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 113 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.89× (z +9.4) | — |
| [[J82 (line)]] | alt | 298 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.35× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 334 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.88× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 216 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.12× (z +12.9) | — |
| [[H4 (line)]] | wt | 88.7 | 2 | 0 | [[Digitoxin (drug)]] 0.05 µM 2.98× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 251 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.363× (z -9.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 264 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 167 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 91.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.57× (z +11.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 161 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.37× (z +11.6) | — |
| [[C-33 A (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.58× (z +8.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +9.1) ⚠ cell-cycle shift, explains ~8% of this change | — |
| [[LOX-IMVI (line)]] | wt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -10.1) |
| [[LS 180 (line)]] | wt | 256 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.13× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 58.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.45× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 289 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.84× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 176 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +9.3) | — |
| [[A-427 (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 255 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 306 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 105 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 202 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 145 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1534), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARGLU1]] | +0.66 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[RAD51-AS1]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SLC16A4-AS1]] | +0.59 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[SMG1P1]] | +0.57 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[CTTN-DT]] | +0.55 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[DYNLT2]] | +0.55 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[C8orf44-SGK3]] | +0.54 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[LAMTOR5-AS1]] | +0.54 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[BCL2L2]] | +0.54 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[EME2]] | +0.54 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[SPTY2D1OS]] | +0.53 | +0.27 / +0.33 | both halves | 3e-04 |  |
| [[PPP1R3E]] | +0.53 | +0.37 / +0.45 | both halves | 8e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH11]] | -0.57 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[POLR3A]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[MEA1]] | -0.56 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[ZNF699]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[LTN1]] | -0.54 | -0.58 / -0.29 | both halves | 2e-04 |  |
| [[MRPL10]] | -0.54 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[MRPL17]] | -0.53 | -0.37 / -0.44 | both halves | 9e-05 |  |
| [[CINP]] | -0.52 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[NDUFA8]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ISCA2]] | -0.52 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[DDX50]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[C17orf58]] | -0.51 | -0.38 / -0.48 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ANKRD10's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.440). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-5.3, 23.5); signed map (32.0, -17.0). **Vector** length 122, 40.7% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.9 | +1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.6 | +8.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +4.4 | +2.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.2 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.1 | +1.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.7 | -7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.5 | -6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -0.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -2.4 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:110,878,540-110,915,069 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20093 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q9NXR5](https://www.uniprot.org/uniprotkb/Q9NXR5) carries no function annotation.

**Summary**, from NCBI Gene [55608](https://www.ncbi.nlm.nih.gov/gene/55608):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20265) · Entrez [55608](https://www.ncbi.nlm.nih.gov/gene/55608) · UniProt [Q9NXR5](https://www.uniprot.org/uniprotkb/Q9NXR5) · Ensembl [ENSG00000088448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088448)

## Data

Gene col 1534: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1534); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1534, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1534]; `tensor/DDL_lfc|DDL_z.npy` [1534]; `embed/gene_vectors.npy` [1534]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1534 or target_col == 1534). Every well: [[ANKRD10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
