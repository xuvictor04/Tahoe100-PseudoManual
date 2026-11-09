---
symbol: "IL4R"
type: "gene"
col: 1180
ensembl_id: "ENSG00000077238"
name: "interleukin 4 receptor"
location: "16p12.1"
module: 219
arm: "+"
pooled_cpm: 42.47
n_lines_expressing: 46
n_dd_up: 1
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/219"]
generated_by: "tahoemap"
---

# IL4R

*interleukin 4 receptor* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 1.46× (z +4.8, q 0.001, up in 24 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 3.39×, HepG2/C3A 2.17×, A-172 2.12×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 4.08×).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.182× (z -22.4, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC71L]] (+0.67, fdr 7e-06), [[TANK]] (+0.62, fdr 7e-06), [[HS3ST3B1]] (+0.60, fdr 1e-05); moves opposite to [[HMBOX1]] (-0.53, fdr 1e-04), [[SARAF]] (-0.52, fdr 2e-05), [[KIZ]] (-0.51, fdr 2e-05).
> It is in [[Module 219]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[C11orf91]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1180.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 3.39×, HepG2/C3A 2.17×, A-172 2.12×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 4.08×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +4.8 | 0.001 | 24/43 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | 1.30× | +3.5 | 0.14 | 18/44 (HS-578T, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.29× | +3.4 | 0.14 | 18/44 (AsPC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1180.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.182×** | -22.4 | 0e+00 | 42/44 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.219×** | -19.9 | 0e+00 | 42/44 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.284×** | -16.5 | 0e+00 | 42/44 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.315×** | -15.2 | 0e+00 | 35/41 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.570×** | -10.4 | 3e-23 | 32/45 (Panc 03.27, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.472×** | -9.5 | 3e-19 | 25/35 (HepG2/C3A, A549, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.479×** | -8.9 | 3e-17 | 29/36 (A549, LS 180, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.641×** | -8.2 | 1e-14 | 33/44 (J82, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.534×** | -8.2 | 1e-14 | 32/44 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.302×** | -8.2 | 1e-14 | 36/43 (CFPAC-1, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -6.4 | 6e-09 | 31/45 (Panc 03.27, RKO, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.626×** | -6.1 | 4e-08 | 29/44 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.656×** | -5.5 | 1e-06 | 28/44 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.681×** | -5.0 | 2e-05 | 30/44 (HOP62, BT-474, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.696×** | -4.7 | 9e-05 | 27/45 (BT-474, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.691×** | -4.6 | 2e-04 | 24/43 (NCI-H1573, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.533×** | -4.3 | 5e-04 | 22/45 (HOP62, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.735×** | -4.0 | 0.002 | 24/43 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 99.6 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.145× (z -15.9) |
| [[HepG2_C3A (line)]] | wt | 169 | 1 (1 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.0608× (z -23.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.134× (z -17.7) |
| [[HOP62 (line)]] | alt | 53.9 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0860× (z -21.6) |
| [[Panc 03.27 (line)]] | alt | 57.4 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -18.2) |
| [[J82 (line)]] | alt | 53.8 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -14.1) |
| [[A549 (line)]] | wt | 79.6 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0517× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.0684× (z -20.8) |
| [[BT-474 (line)]] | alt | 48.0 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.166× (z -10.1) |
| [[HS-578T (line)]] | alt | 42.5 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.159× (z -13.2) |
| [[A-172 (line)]] | wt | 61.4 | 1 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.220× (z -13.4) |
| [[HT-29 (line)]] | alt | 49.6 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -13.5) |
| [[LS 180 (line)]] | wt | 42.2 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -13.3) |
| [[A498 (line)]] | wt | 49.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -15.1) |
| [[NCI-H1573 (line)]] | alt | 71.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 31.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -14.2) |
| [[SW1417 (line)]] | alt | 69.8 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -19.0) |
| [[COLO 205 (line)]] | alt | 79.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0742× (z -17.2) |
| [[Hs 766T (line)]] | wt | 58.6 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 61.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 48.6 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.133× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 39.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -13.8) |
| [[PANC-1 (line)]] | alt | 28.6 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +15.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.08× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.340× (z -9.6) |
| [[SW48 (line)]] | wt | 58.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -11.1) |
| [[SW480 (line)]] | alt | 18.4 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.246× (z -11.8) |
| [[CHP-212 (line)]] | wt | 61.9 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0698× (z -10.7) |
| [[HCT15 (line)]] | alt | 42.9 | 0 | 3 (1 ⚠) | — | [[NG25 (drug)]] 5 µM 0.0597× (z -8.7) |
| [[LoVo (line)]] | wt | 36.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -15.2) |
| [[RKO (line)]] | wt | 34.3 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.171× (z -11.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.212× (z -10.3) |
| [[SW 900 (line)]] | alt | 36.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.236× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 72.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.248× (z -10.8) |
| [[H4 (line)]] | wt | 28.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -9.0) |
| [[KATO III (line)]] | alt | 28.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 20.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 23.0 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 32.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 32.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -12.0) |
| [[A-427 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.98 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 52.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC71L]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[TANK]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[HS3ST3B1]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ZC3H12C]] | +0.57 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[SERPINA1]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SBNO2]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[IRAK2]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[TLNRD1]] | +0.56 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[SOCS3]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 | pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING; STRING 543 |
| [[MMD]] | +0.55 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[BCAR1]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[OSMR]] | +0.54 | +0.48 / +0.59 | both halves | 2e-05 | pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMBOX1]] | -0.53 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[SARAF]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[KIZ]] | -0.51 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[GET1]] | -0.50 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[TMEM9]] | -0.50 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[TPD52]] | -0.50 | -0.34 / -0.51 | both halves | 1e-04 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[CDON]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[SCAI]] | -0.49 | -0.32 / -0.54 | both halves | 1e-04 |  |
| [[VDAC3]] | -0.49 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[MARCHF8]] | -0.48 | -0.50 / -0.37 | both halves | 9e-05 |  |
| [[UBE4B]] | -0.48 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[SH3BGR]] | -0.48 | -0.46 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf91]] | B | C11orf91 activity raises IL4R's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.81× lower at baseline in the lines without C11orf91 | 0.005 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[PHLDA2]] | B | PHLDA2 activity raises IL4R's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.61× lower at baseline in the lines without PHLDA2 | 0.007 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[C1RL-AS1]] | B | C1RL-AS1 activity raises IL4R's level | lines that do not express C1RL-AS1 (7) vs lines expressing it (43) | 2.84× lower at baseline in the lines without C1RL-AS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: EGFR, HFE, SH2D4A |
| [[PI3]] | B | PI3 activity raises IL4R's level | lines that do not express PI3 (27) vs lines expressing it (23) | 1.74× lower at baseline in the lines without PI3 | 0.033 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[ADAMTS9]] | B | ADAMTS9 activity strengthens IL4R's drug response | lines that do not express ADAMTS9 (18) vs lines expressing it (27) | the lines without ADAMTS9 respond 0.75× as strongly (z diff +1.26); strongest at Dinaciclib 0.5 µM: 0.44x vs 0.28x (z diff +2.3) | 0.052 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2; target measured in part of the lines; artifact flags |
| [[CSF3]] | B | CSF3 activity raises IL4R's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 1.70× lower at baseline in the lines without CSF3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |
| [[OSMR]] | B | OSMR activity raises IL4R's level | lines that do not express OSMR (13) vs lines expressing it (37) | 1.23× lower at baseline in the lines without OSMR | 0.060 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, APC, SETD1B; also absent: OSMR-DT, LIFR, IL1R1; its own permutation p |
| [[ABCC3]] | B | ABCC3 activity raises IL4R's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.17× lower at baseline in the lines without ABCC3 | 0.085 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[FAM83A]] | B | FAM83A activity raises IL4R's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 1.82× lower at baseline in the lines without FAM83A | 0.096 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 219]]; 11 genes; every member is in the + arm (projection on the module's main direction 0.742). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.44; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.5, 8.1); signed map (9.5, 25.4). **Vector** length 110, 33.7% of its response variance represented; |z| ≥ 3 in 1,329 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.0 | +2.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.7 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | -1.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.4 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +1.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.0 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.1 | -8.2 |
|  | [[NG25 (drug)]] 5 µM |  | -4.7 | -8.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.0 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -5.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.1 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 4 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.1 — chr16:27,313,668-27,364,778 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD124 |
| Gene groups (HGNC) | CD molecules; Interleukin receptors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INTERFERON_ALPHA_RESPONSE, ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, IL2_STAT5_SIGNALING, INTERFERON_GAMMA_RESPONSE |
| Reactome | 5 pathways, smallest: Differentiation of naive CD4+ T cells to T helper 2 cells (Th2 cells); Interleukin-4 and Interleukin-13 signaling; Differentiation of T cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P24394](https://www.uniprot.org/uniprotkb/P24394) (Interleukin-4 receptor subunit alpha):

> Receptor for both interleukin 4 and interleukin 13. Couples to the JAK1/2/3-STAT6 pathway. The IL4 response is involved in promoting Th2 differentiation. The IL4/IL13 responses are involved in regulating IgE production and, chemokine and mucus production at sites of allergic inflammation. In certain cell types, can signal through activation of insulin receptor substrates, IRS1/IRS2.; Soluble IL4R (sIL4R) inhibits IL4-mediated cell proliferation and IL5 up-regulation by T-cells.

**Summary**, from NCBI Gene [3566](https://www.ncbi.nlm.nih.gov/gene/3566):

> This gene encodes the alpha chain of the interleukin-4 receptor, a type I transmembrane protein that can bind interleukin 4 and interleukin 13 to regulate IgE production. The encoded protein also can bind interleukin 4 to promote differentiation of Th2 cells. A soluble form of the encoded protein can be produced by proteolysis of the membrane-bound protein, and this soluble form can inhibit IL4-mediated cell proliferation and IL5 upregulation by T-cells. Allelic variations in this gene have …

**Accessions** — [HGNC:6015](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6015) · Entrez [3566](https://www.ncbi.nlm.nih.gov/gene/3566) · UniProt [P24394](https://www.uniprot.org/uniprotkb/P24394) · Ensembl [ENSG00000077238](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077238)

## Data

Gene col 1180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1180); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1180]; `tensor/DDL_lfc|DDL_z.npy` [1180]; `embed/gene_vectors.npy` [1180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1180 or target_col == 1180). Every well: [[IL4R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL4R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
