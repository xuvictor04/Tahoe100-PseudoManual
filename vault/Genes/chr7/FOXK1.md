---
symbol: "FOXK1"
type: "gene"
col: 9028
ensembl_id: "ENSG00000164916"
name: "forkhead box K1"
location: "7p22.1"
module: 85
arm: "+"
pooled_cpm: 133.5
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 29
n_dd_up_clean: 1
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# FOXK1

*forkhead box K1* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 1.64× (z +6.6, q 2e-08, up in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (A498 3.26×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (HEC-1-A 3.25×).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.348× (z -38.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB40B]] (+0.63, fdr 9e-06), [[BRAT1]] (+0.60, fdr 6e-05), [[ST3GAL4]] (+0.59, fdr 9e-05); moves opposite to [[PLAGL1]] (-0.56, fdr 1e-04), [[KRBOX5]] (-0.55, fdr 9e-05), [[ZBTB21]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9028.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (A498 3.26×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (HEC-1-A 3.25×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +6.6 | 2e-08 | 32/48 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.4 | 0.19 | 17/48 (HOP62, J82, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.09× | +3.1 | 0.25 | 3/48 (H4, BT-474, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.13× | +3.1 | 0.25 | 14/48 (A498, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9028.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.348×** | -38.1 | 0e+00 | 48/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.502×** | -24.9 | 0e+00 | 45/49 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.404×** | -23.2 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.469×** | -19.3 | 0e+00 | 46/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.521×** | -16.0 | 0e+00 | 42/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -12.9 | 8e-36 | 40/50 (MIA PaCa-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.596×** | -12.7 | 4e-35 | 41/44 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.386×** | -12.7 | 4e-35 | 44/48 (LoVo, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.625×** | -12.0 | 2e-31 | 43/49 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.411×** | -11.9 | 1e-30 | 45/48 (KATO III, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.637×** | -11.5 | 6e-29 | 42/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.433×** | -11.2 | 3e-27 | 42/48 (LoVo, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -11.0 | 2e-26 | 43/48 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[EX229 (drug)]] 5 µM |  | **0.488×** | -9.6 | 4e-20 | 43/48 (LoVo, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.651×** | -9.4 | 2e-19 | 33/45 (NCI-H23, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.494×** | -9.4 | 2e-19 | 40/48 (KATO III, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.720×** | -8.4 | 2e-15 | 34/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.725×** | -7.8 | 2e-13 | 38/48 (LoVo, SW48, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.818×** | -7.3 | 1e-11 | 26/48 (SNU-1, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9028. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 239 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -33.3) |
| [[LoVo (line)]] | wt | 161 | 0 | 16 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -33.6) |
| [[MIA PaCa-2 (line)]] | alt | 215 | 0 | 15 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -26.5) |
| [[Hs 766T (line)]] | wt | 188 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -24.7) |
| [[HT-29 (line)]] | alt | 178 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -22.3) |
| [[A549 (line)]] | wt | 172 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -19.6) |
| [[HEC-1-A (line)]] | alt | 162 | 1 | 10 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.25× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -20.4) |
| [[KATO III (line)]] | alt | 206 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -17.1) |
| [[SNU-1 (line)]] | wt | 189 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -25.4) |
| [[A498 (line)]] | wt | 198 | 1 (1 ⚠) | 9 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.26× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -25.6) |
| [[SW480 (line)]] | alt | 146 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -39.4) |
| [[AsPC-1 (line)]] | alt | 133 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -39.7) |
| [[A-172 (line)]] | wt | 99.4 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -21.0) |
| [[HOP62 (line)]] | alt | 71.4 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -16.6) |
| [[NCI-H2347 (line)]] | alt | 125 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -16.8) |
| [[PANC-1 (line)]] | alt | 138 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -26.7) |
| [[C32 (line)]] | wt | 82.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -25.5) |
| [[NCI-H23 (line)]] | alt | 112 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -31.1) |
| [[SHP-77 (line)]] | alt | 209 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -16.2) |
| [[SK-MEL-2 (line)]] | alt | 104 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -25.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.241× (z -24.1) |
| [[SW1417 (line)]] | alt | 143 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 73.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -23.9) |
| [[NCI-H2030 (line)]] | alt | 118 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -26.8) |
| [[SW48 (line)]] | wt | 187 | 0 | 5 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.250× (z -14.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.437× (z -12.5) |
| [[COLO 205 (line)]] | alt | 108 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0912× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.232× (z -18.2) |
| [[LS 180 (line)]] | wt | 130 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -19.5) |
| [[NCI-H1573 (line)]] | alt | 41.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 116 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -15.5) |
| [[RKO (line)]] | wt | 102 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.347× (z -12.3) |
| [[C-33 A (line)]] | alt | 106 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -14.6) |
| [[HS-578T (line)]] | alt | 90.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -15.0) |
| [[hTERT-HPNE (line)]] | wt | 89.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -14.4) |
| [[J82 (line)]] | alt | 82.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 82.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -15.9) |
| [[SNU-423 (line)]] | alt | 72.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -15.7) |
| [[SW 900 (line)]] | alt | 116 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -18.7) |
| [[A-427 (line)]] | wt | 74.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 59.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -15.6) |
| [[H4 (line)]] | wt | 174 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.322× (z -11.2) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 118 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -23.4) |
| [[SW 1088 (line)]] | alt | 128 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -9.3) |
| [[AN3 CA (line)]] | alt | 130 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -9.5) |
| [[HCT15 (line)]] | alt | 123 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.7) |
| [[SW 1271 (line)]] | alt | 140 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -12.0) |
| [[BT-474 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 159 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9028), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB40B]] | +0.63 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[BRAT1]] | +0.60 | +0.63 / +0.38 | both halves | 6e-05 |  |
| [[ST3GAL4]] | +0.59 | +0.67 / +0.36 | both halves | 9e-05 |  |
| [[SPSB3]] | +0.59 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[EXOSC5]] | +0.59 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[PPT2]] | +0.57 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[GLRX5]] | +0.57 | +0.54 / +0.36 | both halves | 9e-05 |  |
| [[BCR]] | +0.56 | +0.70 / +0.33 | both halves | 1e-04 |  |
| [[EPHB4]] | +0.56 | +0.70 / +0.36 | both halves | 1e-04 |  |
| [[PIM1]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PAK4]] | +0.56 | +0.66 / +0.39 | both halves | 5e-05 |  |
| [[COQ8A]] | +0.55 | +0.32 / +0.58 | both halves | 2e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAGL1]] | -0.56 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[KRBOX5]] | -0.55 | -0.65 / -0.36 | both halves | 9e-05 |  |
| [[ZBTB21]] | -0.54 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[AIMP1]] | -0.53 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[ERCC6L2]] | -0.53 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[DZIP3]] | -0.53 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[RCAN1]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ZNG1A]] | -0.52 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[TAF9]] | -0.52 | -0.60 / -0.30 | both halves | 2e-04 |  |
| [[LACC1]] | -0.52 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[ACAD11]] | -0.51 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[GOLGA1]] | -0.51 | -0.53 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FOXK1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FZD4]] | B | FZD4 activity raises FOXK1's level | lines that do not express FZD4 (9) vs lines expressing it (41) | 1.31× lower at baseline in the lines without FZD4 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FBXL16]] | B | FBXL16 activity raises FOXK1's level | lines that do not express FBXL16 (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without FBXL16 | 0.073 | ⚠ within organs, on part of the lines; also absent: SHC2, PLEKHG3 |
| [[PLXND1]] | B | PLXND1 activity raises FOXK1's level | lines that do not express PLXND1 (7) vs lines expressing it (43) | 1.48× lower at baseline in the lines without PLXND1 | 0.080 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-0.7, -1.4); signed map (-19.3, 13.8). **Vector** length 125, 41.2% of its response variance represented; |z| ≥ 3 in 1,606 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.9 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.1 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.6 | +2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.0 | +0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +5.9 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +6.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.5 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | -1.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.5 | -19.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.6 | -12.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.4 | -11.9 |
|  | [[EX229 (drug)]] 5 µM |  | -7.3 | -9.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.2 | -11.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.0 | -9.4 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box K1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:4,682,295-4,771,442 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IMAGE:5164497 |
| Gene groups (HGNC) | Forkhead boxes |
| Reactome | 2 pathways, smallest: UCH proteinases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [P85037](https://www.uniprot.org/uniprotkb/P85037) (Forkhead box protein K1):

> Transcriptional regulator involved in different processes such as glucose metabolism, aerobic glycolysis, muscle cell differentiation and autophagy (By similarity). Recognizes and binds the forkhead DNA sequence motif (5'-GTAAACA-3') and can both act as a transcription activator or repressor, depending on the context. Together with FOXK2, acts as a key regulator of metabolic reprogramming towards aerobic glycolysis, a process in which glucose is converted to lactate in the presence of oxygen …

**Summary**, from NCBI Gene [221937](https://www.ncbi.nlm.nih.gov/gene/221937):

> Enables 14-3-3 protein binding activity; DNA-binding transcription repressor activity, RNA polymerase II-specific; and transcription cis-regulatory region binding activity. Involved in several processes, including intracellular glucose homeostasis; regulation of DNA-templated transcription; and regulation of glucose metabolic process. Located in cytoplasm and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23480) · Entrez [221937](https://www.ncbi.nlm.nih.gov/gene/221937) · UniProt [P85037](https://www.uniprot.org/uniprotkb/P85037) · Ensembl [ENSG00000164916](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164916)

## Data

Gene col 9028: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9028); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9028, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9028]; `tensor/DDL_lfc|DDL_z.npy` [9028]; `embed/gene_vectors.npy` [9028]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9028 or target_col == 9028). Every well: [[FOXK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
