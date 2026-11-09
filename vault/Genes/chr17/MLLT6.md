---
symbol: "MLLT6"
type: "gene"
col: 15837
ensembl_id: "ENSG00000275023"
name: "MLLT6, PHD finger containing"
location: "17q12"
module: 138
arm: "+"
pooled_cpm: 80.48
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 27
n_dd_up_clean: 1
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# MLLT6

*MLLT6, PHD finger containing* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.67× (z +11.5, q 1e-27, up in 30 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.37× (z +5.0, q 9e-05, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 9 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 4.47×, SHP-77 3.09×, SW480 1.95×, NCI-H1792 2.48×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 1.79×, J82 1.74×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW1417 2.23×, HEC-1-A 1.76×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.290× (z -27.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC12A7]] (+0.70, fdr 7e-06), [[TAPBP]] (+0.62, fdr 1e-05), [[STAT5A]] (+0.61, fdr 1e-05); moves opposite to [[GNAI3]] (-0.59, fdr 2e-04), [[POGLUT2]] (-0.56, fdr 3e-05), [[BOLA3]] (-0.54, fdr 1e-04).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRRN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15837.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 9 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 4.47×, SHP-77 3.09×, SW480 1.95×, NCI-H1792 2.48×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 1.79×, J82 1.74×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW1417 2.23×, HEC-1-A 1.76×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +11.5 | 1e-27 | 30/48 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +7.8 | 1e-12 | 27/44 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 9e-05 | 30/48 (HEC-1-A, KATO III, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.7 | 0.030 | 18/48 (BT-474, A-172, …) | rises with dose | composition shift |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.17× | +3.5 | 0.057 | 18/47 (LS 180, Hs 766T, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.083 | 16/47 (A549, HS-578T, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.22× | +3.2 | 0.11 | 14/48 (A-427, PANC-1, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.12 | 16/45 (SW1417, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.21× | +3.1 | 0.12 | 15/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15837.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.290×** | -27.7 | 0e+00 | 47/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.296×** | -27.2 | 0e+00 | 46/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.344×** | -23.9 | 0e+00 | 46/48 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.590×** | -11.8 | 5e-30 | 44/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.728×** | -10.0 | 1e-21 | 38/48 (J82, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.500×** | -8.1 | 5e-14 | 39/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.503×** | -8.0 | 8e-14 | 39/48 (hTERT-HPNE, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.711×** | -7.6 | 2e-12 | 33/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.552×** | -6.9 | 2e-10 | 39/49 (BT-474, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.750×** | -6.4 | 8e-09 | 25/48 (LS 180, SW480, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -6.1 | 5e-08 | 26/48 (SW480, BT-474, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.599×** | -6.0 | 1e-07 | 35/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.759×** | -5.8 | 3e-07 | 31/48 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.781×** | -5.5 | 1e-06 | 28/47 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.775×** | -5.5 | 2e-06 | 25/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.661×** | -4.8 | 4e-05 | 25/47 (SW480, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.677×** | -4.6 | 1e-04 | 28/48 (BT-474, NCI-H23, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 100 | 1 (1 ⚠) | 12 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.95× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.175× (z -24.9) |
| [[BT-474 (line)]] | alt | 609 | 4 (4 ⚠) | 8 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -30.5) |
| [[COLO 205 (line)]] | alt | 123 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -29.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.144× (z -21.6) |
| [[HEC-1-A (line)]] | alt | 135 | 1 (1 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.76× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -17.4) |
| [[LS 180 (line)]] | wt | 70.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.339× (z -12.4) |
| [[HCT15 (line)]] | alt | 129 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -17.1) |
| [[SW1417 (line)]] | alt | 95.1 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.358× (z -12.7) |
| [[A549 (line)]] | wt | 68.9 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -15.5) |
| [[C32 (line)]] | wt | 51.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.224× (z -12.5) |
| [[CHP-212 (line)]] | wt | 118 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0844× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.201× (z -11.0) |
| [[J82 (line)]] | alt | 78.0 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.267× (z -16.3) |
| [[MIA PaCa-2 (line)]] | alt | 79.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -19.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.249× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 94.7 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -22.2) |
| [[NCI-H460 (line)]] | wt | 49.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -21.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.267× (z -18.7) |
| [[RKO (line)]] | wt | 72.8 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.350× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 114 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.144× (z -23.3) |
| [[SNU-423 (line)]] | alt | 64.4 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -16.9) |
| [[A-172 (line)]] | wt | 85.4 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 65.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -13.5) |
| [[HS-578T (line)]] | alt | 58.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -17.8) |
| [[HT-29 (line)]] | alt | 176 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -19.8) |
| [[LoVo (line)]] | wt | 56.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -20.0) |
| [[NCI-H1573 (line)]] | alt | 44.5 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.47× (z +13.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.287× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 50.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.250× (z -13.4) |
| [[NCI-H2347 (line)]] | alt | 76.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.347× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 93.0 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.285× (z -14.6) |
| [[SHP-77 (line)]] | alt | 51.0 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +9.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -11.4) |
| [[SNU-1 (line)]] | wt | 86.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -16.1) |
| [[A498 (line)]] | wt | 74.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.409× (z -12.5) |
| [[C-33 A (line)]] | alt | 70.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -13.7) |
| [[HOP62 (line)]] | alt | 60.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -15.7) |
| [[hTERT-HPNE (line)]] | wt | 50.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -11.4) |
| [[KATO III (line)]] | alt | 69.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -12.2) |
| [[PANC-1 (line)]] | alt | 36.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -14.9) |
| [[SW 900 (line)]] | alt | 45.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -11.8) |
| [[SW48 (line)]] | wt | 74.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.213× (z -12.3) |
| [[A-427 (line)]] | wt | 53.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.312× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 84.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.429× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 69.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.429× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 51.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.310× (z -9.7) |
| [[H4 (line)]] | wt | 47.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.242× (z -9.0) |
| [[AN3 CA (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC12A7]] | +0.70 | +0.62 / +0.63 | both halves | 7e-06 | same gene group |
| [[TAPBP]] | +0.62 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[STAT5A]] | +0.61 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[CLCN7]] | +0.61 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[AKT1S1]] | +0.60 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[STK11]] | +0.59 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[HDGF]] | +0.58 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[RCC2]] | +0.56 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[TAPBPL]] | +0.56 | +0.43 / +0.45 | both halves | 4e-05 |  |
| [[GIGYF1]] | +0.56 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[PLXNB1]] | +0.55 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[MED12]] | +0.54 | +0.45 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI3]] | -0.59 | -0.54 / -0.29 | both halves | 2e-04 | same gene group |
| [[POGLUT2]] | -0.56 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[BOLA3]] | -0.54 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[NDUFA12]] | -0.53 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[ATG5]] | -0.53 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[FOCAD]] | -0.53 | -0.48 / -0.46 | both halves | 3e-05 | same gene group |
| [[INTS4]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[EDRF1]] | -0.52 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[ATG4C]] | -0.52 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[RARS1]] | -0.52 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[POMGNT2]] | -0.52 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[YIF1B]] | -0.51 | -0.31 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRN1]] | B | LRRN1 activity raises MLLT6's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 1.37× lower at baseline in the lines without LRRN1 | 0.099 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.6, 3.5); signed map (32.5, -25.2). **Vector** length 108, 30.7% of its response variance represented; |z| ≥ 3 in 1,261 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.1 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | -4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.4 | -0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.8 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.3 | -10.0 |
|  | [[EX229 (drug)]] 5 µM |  | -4.8 | -6.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -7.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.1 | -8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -8.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | MLLT6, PHD finger containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:38,705,273-38,729,795 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AF17, FLJ23480 |
| Gene groups (HGNC) | PHD finger proteins; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P55198](https://www.uniprot.org/uniprotkb/P55198) (Protein AF-17):

> Involved in the stimulation of renal sodium reabsorption mediated by the epithelial sodium channel (ENaC) (By similarity). Up-regulates ENaC expression in renal collecting duct cells by promoting DOT1L export from the nucleus to the cytoplasm, thus limiting DOT1L-mediated H3K79 methylation and transcriptional repression at the SCNN1A promoter.

**Summary**, from NCBI Gene [4302](https://www.ncbi.nlm.nih.gov/gene/4302):

> Enables histone binding activity and nucleosome binding activity. Predicted to be involved in chromatin remodeling and regulation of transcription by RNA polymerase II. Predicted to act upstream of or within several processes, including renal potassium excretion; renal sodium excretion; and renal water absorption. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7138](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7138) · Entrez [4302](https://www.ncbi.nlm.nih.gov/gene/4302) · UniProt [P55198](https://www.uniprot.org/uniprotkb/P55198) · Ensembl [ENSG00000275023](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000275023)

## Data

Gene col 15837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15837); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15837]; `tensor/DDL_lfc|DDL_z.npy` [15837]; `embed/gene_vectors.npy` [15837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15837 or target_col == 15837). Every well: [[MLLT6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLLT6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
