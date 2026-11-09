---
symbol: "MCFD2"
type: "gene"
col: 11105
ensembl_id: "ENSG00000180398"
name: "multiple coagulation factor deficiency 2, ER cargo receptor complex subunit"
location: "2p21"
module: 42
arm: "+"
pooled_cpm: 126.45
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# MCFD2

*multiple coagulation factor deficiency 2, ER cargo receptor complex subunit* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.74× (z +15.2, q 0e+00, up in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.11× (z +11.3, q 3e-27, up in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 13 lines (C32 3.34×, A-172 2.26×, SK-MEL-2 2.77×, SW480 2.15×, …); [[Dinaciclib (drug)]] 0.5 µM in 10 lines (A549 4.60×, NCI-H1792 5.16×, NCI-H2030 3.79×, LOX-IMVI 4.10×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (LOX-IMVI 4.51×, NCI-H1792 5.22×, SNU-423 4.42×, HEC-1-A 3.38×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.536× (z -12.9, q 2e-35, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SURF4]] (+0.53, fdr 1e-05), [[TMED2]] (+0.53, fdr 3e-05), [[SEC61A1]] (+0.52, fdr 1e-05); moves opposite to [[WTAP]] (-0.52, fdr 2e-05), [[PTBP2]] (-0.51, fdr 7e-05), [[IKZF3]] (-0.49, fdr 3e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RARRES1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11105.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 13 lines (C32 3.34×, A-172 2.26×, SK-MEL-2 2.77×, SW480 2.15×, …); [[Dinaciclib (drug)]] 0.5 µM in 10 lines (A549 4.60×, NCI-H1792 5.16×, NCI-H2030 3.79×, LOX-IMVI 4.10×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (LOX-IMVI 4.51×, NCI-H1792 5.22×, SNU-423 4.42×, HEC-1-A 3.38×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +15.2 | 0e+00 | 46/49 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +14.2 | 3e-43 | 42/44 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +11.3 | 3e-27 | 46/48 (C32, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +10.0 | 1e-21 | 41/45 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.5 | 8e-04 | 0/50 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.33×** | +4.3 | 0.002 | 32/48 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.7 | 0.016 | 21/48 (A-427, C32, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.3 | 0.080 | 23/47 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11105.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.536×** | -12.9 | 2e-35 | 43/48 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.667×** | -6.1 | 3e-07 | 33/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.520×** | -5.2 | 5e-05 | 37/48 (SW48, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.716×** | -5.0 | 6e-05 | 35/48 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.558×** | -4.6 | 5e-04 | 34/49 (A-427, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.627×** | -3.7 | 0.022 | 32/49 (Panc 03.27, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.803× | -3.2 | 0.12 | 27/49 (NCI-H23, hTERT-HPNE, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.789× | -3.1 | 0.13 | 22/50 (A-172, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11105. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 227 | 4 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.26× (z +10.0) | [[Trametinib (drug)]] 5 µM 0.464× (z -9.4) ⚠ cell-cycle shift, explains ~18% of this change |
| [[CFPAC-1 (line)]] | alt | 171 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -25.7) |
| [[NCI-H2030 (line)]] | alt | 209 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 118 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 114 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.12× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -11.0) |
| [[HOP62 (line)]] | alt | 188 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -14.0) |
| [[HS-578T (line)]] | alt | 136 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 113 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.42× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 88.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 158 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.49× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -10.2) |
| [[SNU-423 (line)]] | alt | 123 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.42× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.52× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 189 | 2 (1 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 2.14× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -12.5) |
| [[SW480 (line)]] | alt | 112 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.15× (z +9.4) | — |
| [[A-427 (line)]] | wt | 117 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 127 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -22.3) |
| [[C32 (line)]] | wt | 66.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.34× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 88.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 169 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 193 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -8.7) |
| [[J82 (line)]] | alt | 95.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -10.2) |
| [[KATO III (line)]] | alt | 146 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.11× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -15.7) |
| [[Panc 03.27 (line)]] | alt | 131 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -14.0) |
| [[PANC-1 (line)]] | alt | 89.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 86.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.77× (z +9.5) | — |
| [[A498 (line)]] | wt | 210 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 119 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +17.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +11.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 112 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.42× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 109 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.57× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 89.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +14.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 115 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -12.5) |
| [[SW1417 (line)]] | alt | 119 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.17× (z +8.8) | — |
| [[SW48 (line)]] | wt | 86.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +9.9) ⚠ toxic; transcription drop | [[PH-797804 (drug)]] 5 µM 0.0650× (z -11.2) |
| [[AN3 CA (line)]] | alt | 88.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +8.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 61.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.39× (z +8.8) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -10.8) |
| [[LS 180 (line)]] | wt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 92.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 56.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 154 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -11.7) |
| [[BT-474 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 177 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 98.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 188 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11105), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SURF4]] | +0.53 | +0.59 / +0.49 | both halves | 1e-05 | STRING 618 |
| [[TMED2]] | +0.53 | +0.56 / +0.46 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation; STRING 517 |
| [[SEC61A1]] | +0.52 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[SEL1L]] | +0.52 | +0.50 / +0.53 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[CDRT4]] | +0.51 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[UBE4A]] | +0.50 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[FKBP14]] | +0.50 | +0.51 / +0.40 | both halves | 5e-05 | same gene group |
| [[LMAN1]] | +0.49 | +0.55 / +0.48 | both halves | 2e-05 | pathway: Asparagine N-linked glycosylation; STRING 999 |
| [[SRPRA]] | +0.49 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[SLC39A7]] | +0.48 | +0.58 / +0.38 | both halves | 7e-05 |  |
| [[SEC22B]] | +0.47 | +0.43 / +0.52 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation; STRING 588 |
| [[SSR1]] | +0.47 | +0.58 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WTAP]] | -0.52 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[PTBP2]] | -0.51 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[IKZF3]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[RARRES1]] | -0.46 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[RNF138]] | -0.45 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[ASXL1]] | -0.44 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[RELB]] | -0.44 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[HIRIP3]] | -0.43 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[BCL3]] | -0.43 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[NDUFAF3]] | -0.43 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[EXOSC9]] | -0.42 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[USP43]] | -0.42 | -0.32 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RARRES1]] | B | RARRES1 activity raises MCFD2's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 1.24× lower at baseline in the lines without RARRES1 | 0.056 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.497). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.6, -30.0); signed map (-55.3, 8.1). **Vector** length 89.7, 28.0% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.9 | +11.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | -0.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -0.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.8 | +1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.7 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -12.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.0 | +15.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | +14.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.5 | -0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | multiple coagulation factor deficiency 2, ER cargo receptor complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:46,901,870-46,941,855 (-) |
| Ensembl biotype | protein_coding |
| Also known as | F5F8D, LMAN1IP, SDNSF |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 7 pathways, smallest: Cargo concentration in the ER; COPII-mediated vesicle transport; ER to Golgi Anterograde Transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NI22](https://www.uniprot.org/uniprotkb/Q8NI22) (Multiple coagulation factor deficiency protein 2):

> The MCFD2-LMAN1 complex forms a specific cargo receptor for the ER-to-Golgi transport of selected proteins. Plays a role in the secretion of coagulation factors.

**Summary**, from NCBI Gene [90411](https://www.ncbi.nlm.nih.gov/gene/90411):

> This gene encodes a soluble luminal protein with two calmodulin-like EF-hand motifs at its C-terminus. This protein forms a complex with LMAN1 (lectin mannose binding protein 1; also known as ERGIC-53) that facilitates the transport of coagulation factors V (FV) and VIII (FVIII) from the endoplasmic reticulum to the Golgi apparatus via an endoplasmic reticulum Golgi intermediate compartment (ERGIC). Mutations in this gene cause combined deficiency of FV and FVIII (F5F8D); a rare autosomal …

**Accessions** — [HGNC:18451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18451) · Entrez [90411](https://www.ncbi.nlm.nih.gov/gene/90411) · UniProt [Q8NI22](https://www.uniprot.org/uniprotkb/Q8NI22) · Ensembl [ENSG00000180398](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180398)

## Data

Gene col 11105: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11105); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11105, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11105]; `tensor/DDL_lfc|DDL_z.npy` [11105]; `embed/gene_vectors.npy` [11105]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11105 or target_col == 11105). Every well: [[MCFD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCFD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
