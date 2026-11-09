---
symbol: "NUB1"
type: "gene"
col: 270
ensembl_id: "ENSG00000013374"
name: "negative regulator of ubiquitin like proteins 1"
location: "7q36.1"
module: 70
arm: "+"
pooled_cpm: 118.96
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# NUB1

*negative regulator of ubiquitin like proteins 1* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.59× (z +9.5, q 9e-19, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.565× (z -11.7, q 4e-29, down in 44 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.448× (z -8.6, q 1e-15, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBP4]] (+0.69, fdr 7e-06), [[OPTN]] (+0.65, fdr 7e-06), [[CYLD]] (+0.65, fdr 7e-06); moves opposite to [[UBE2N]] (-0.54, fdr 1e-05), [[NACC1]] (-0.50, fdr 3e-05), [[RNGTT]] (-0.48, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[OAS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 270.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +9.5 | 9e-19 | 40/48 (LoVo, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +7.4 | 4e-11 | 37/48 (LoVo, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +6.7 | 5e-09 | 38/48 (MIA PaCa-2, A-172, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +6.1 | 2e-07 | 31/48 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +5.9 | 4e-07 | 29/48 (C32, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **1.24×** | +4.4 | 0.001 | 24/49 (NCI-H2030, J82, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | **1.22×** | +4.0 | 0.006 | 22/44 (SHP-77, C-33 A, …) | rises with dose | composition shift |
| [[Binimetinib (drug)]] 5 µM |  | 1.19× | +3.8 | 0.011 | 21/49 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.013 | 23/47 (AsPC-1, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.018 | 14/48 (AsPC-1, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.019 | 20/48 (SW480, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.5 | 0.019 | 16/48 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.021 | 23/47 (C32, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.021 | 18/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.034 | 20/50 (A-427, AsPC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.041 | 18/49 (AsPC-1, CFPAC-1, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.047 | 16/48 (SK-MEL-2, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.056 | 15/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 270.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.565×** | -11.7 | 4e-29 | 44/48 (AsPC-1, HEC-1-A, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.448×** | -8.6 | 1e-15 | 41/49 (A498, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.566×** | -6.1 | 2e-07 | 31/48 (C32, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.589×** | -5.7 | 2e-06 | 35/48 (AsPC-1, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.831×** | -5.4 | 7e-06 | 22/48 (A498, COLO 205, …) | top dose only | low cells (technical?) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.712×** | -5.0 | 5e-05 | 34/48 (MIA PaCa-2, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.632×** | -4.9 | 6e-05 | 30/48 (SW1417, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.809×** | -4.1 | 0.003 | 25/48 (RKO, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.689×** | -4.0 | 0.004 | 27/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.690×** | -4.0 | 0.004 | 28/48 (MIA PaCa-2, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.822×** | -3.8 | 0.007 | 20/47 (BT-474, SW48, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.705×** | -3.8 | 0.008 | 23/47 (PANC-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.847× | -3.4 | 0.026 | 17/48 (LoVo, KATO III, …) | all doses, flat |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.026 | 22/49 (H4, RKO, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.859× | -3.1 | 0.067 | 13/48 (LoVo, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 270. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 144 | 8 (1 ⚠) | 1 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.72× (z +11.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.319× (z -13.5) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 295 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -14.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.247× (z -11.4) |
| [[LoVo (line)]] | wt | 172 | 3 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.25× (z +16.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.91× (z +15.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.530× (z -8.9) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 158 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.95× (z +11.8) | [[TAK-901 (drug)]] 5 µM 0.168× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 114 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.67× (z +13.8) | — |
| [[A-172 (line)]] | wt | 111 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.19× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.465× (z -9.9) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 103 | 2 | 1 | [[Harringtonine (drug)]] 0.5 µM 2.53× (z +10.5) | [[TAK-901 (drug)]] 5 µM 0.219× (z -9.0) |
| [[C32 (line)]] | wt | 171 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.167× (z -13.2) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.302× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 121 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +11.9) | — |
| [[HS-578T (line)]] | alt | 167 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.65× (z +10.6) | — |
| [[J82 (line)]] | alt | 78.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 124 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.471× (z -9.1) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 94.8 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.46× (z +11.9) | — |
| [[SNU-423 (line)]] | alt | 133 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +11.7) | — |
| [[SW480 (line)]] | alt | 119 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.81× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.571× (z -9.0) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 88.0 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.366× (z -9.5) |
| [[C-33 A (line)]] | alt | 78.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | — |
| [[HEC-1-A (line)]] | alt | 93.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.408× (z -12.0) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 75.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0528× (z -12.7) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 61.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.439× (z -8.9) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 72.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.119× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 126 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.13× (z +9.3) | — |
| [[RKO (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.429× (z -11.3) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 108 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.28× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 80.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | — |
| [[SW 1088 (line)]] | alt | 177 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.0527× (z -12.8) |
| [[SW 900 (line)]] | alt | 112 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.61× (z +11.0) | — |
| [[SW1417 (line)]] | alt | 196 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.462× (z -11.3) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 116 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.372× (z -9.0) |
| [[A-427 (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 98.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 127 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 83.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 90.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 270), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP4]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 445 |
| [[OPTN]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CYLD]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CCDC186]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[APOL3]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[HLA-E]] | +0.61 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[PSMB9]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 576 |
| [[SP100]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[WHAMM]] | +0.60 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[APOL2]] | +0.60 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[SP140L]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[OGFR]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2N]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[NACC1]] | -0.50 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[RNGTT]] | -0.48 | -0.55 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS1]] | B | OAS1 activity raises NUB1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.26× lower at baseline in the lines without OAS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[CFB]] | B | CFB activity raises NUB1's level | lines that do not express CFB (20) vs lines expressing it (30) | 1.31× lower at baseline in the lines without CFB | 0.034 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[TMEM140]] | B | TMEM140 activity raises NUB1's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without TMEM140 | 0.042 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SLC15A3]] | B | SLC15A3 activity raises NUB1's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 1.33× lower at baseline in the lines without SLC15A3 | 0.046 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[CD5L]] | B | CD5L activity weakens NUB1's drug response | lines that do not express CD5L (23) vs lines expressing it (26) | the lines without CD5L respond 0.88× as strongly (z diff +0.41); strongest at Panobinostat 5 µM: 1.45x vs 1.15x (z diff -2.6) | 0.046 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[EPSTI1]] | B | EPSTI1 activity raises NUB1's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.31× lower at baseline in the lines without EPSTI1 | 0.051 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[CD5L]] | B | CD5L activity raises NUB1's level | lines that do not express CD5L (23) vs lines expressing it (27) | 1.34× lower at baseline in the lines without CD5L | 0.056 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[GBP4]] | B | GBP4 activity raises NUB1's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.26× lower at baseline in the lines without GBP4 | 0.061 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[SP110]] | B | SP110 activity raises NUB1's level | lines that do not express SP110 (5) vs lines expressing it (45) | 1.22× lower at baseline in the lines without SP110 | 0.082 | ⚠ within organs, on part of the lines; also absent: IFIT1; maybe low, not absent |
| [[GBP1]] | B | GBP1 activity raises NUB1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.28× lower at baseline in the lines without GBP1 | 0.086 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.3, 48.3); signed map (63.0, 26.3). **Vector** length 139, 44.0% of its response variance represented; |z| ≥ 3 in 1,274 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Non-canonical inflammasome activation* (reactome, mean cos +0.57 to 4); *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.54 to 4); *CASP4 inflammasome assembly* (reactome, mean cos +0.60 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.6 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +7.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.5 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.5 | +3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.4 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.2 | +3.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.8 | -11.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -9.1 | -8.6 |
|  | [[EX229 (drug)]] 5 µM |  | -7.2 | -5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.6 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.3 | -6.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.8 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.5 | -4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.3 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | negative regulator of ubiquitin like proteins 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:151,341,772-151,378,449 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BS4, NYREN18, NUB1L |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5A7](https://www.uniprot.org/uniprotkb/Q9Y5A7) (NEDD8 ultimate buster 1):

> Specific down-regulator of the NEDD8 conjugation system. Recruits NEDD8, UBD, and their conjugates to the proteasome for degradation. Isoform 1 promotes the degradation of NEDD8 more efficiently than isoform 2.

**Summary**, from NCBI Gene [51667](https://www.ncbi.nlm.nih.gov/gene/51667):

> This gene encodes a protein that functions as a negative regulator of NEDD8, a ubiquitin-like protein that conjugates with cullin family members in order to regulate vital biological events. The protein encoded by this gene regulates the NEDD8 conjugation system post-transcriptionally by recruiting NEDD8 and its conjugates to the proteasome for degradation. This protein interacts with the product of the AIPL1 gene, which is associated with Leber congenital amaurosis, an inherited retinopathy, …

**Accessions** — [HGNC:17623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17623) · Entrez [51667](https://www.ncbi.nlm.nih.gov/gene/51667) · UniProt [Q9Y5A7](https://www.uniprot.org/uniprotkb/Q9Y5A7) · Ensembl [ENSG00000013374](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013374)

## Data

Gene col 270: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 270); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 270, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 270]; `tensor/DDL_lfc|DDL_z.npy` [270]; `embed/gene_vectors.npy` [270]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 270 or target_col == 270). Every well: [[NUB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
