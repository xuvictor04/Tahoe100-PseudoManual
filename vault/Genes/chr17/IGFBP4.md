---
symbol: "IGFBP4"
type: "gene"
col: 6572
ensembl_id: "ENSG00000141753"
name: "insulin like growth factor binding protein 4"
location: "17q21.2"
module: 97
arm: "+"
pooled_cpm: 59.3
n_lines_expressing: 31
n_dd_up: 5
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# IGFBP4

*insulin like growth factor binding protein 4* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.82× (z +14.6, q 1e-45, up in 25 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Betamethasone dipropionate (drug)]] 0.5 µM: 1.37× (z +3.4, q 0.054, up in 12 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H2030 4.66×, PANC-1 6.56×, HS-578T 6.73×, CFPAC-1 3.84×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H2030 3.96×, HOP62 3.72×, PANC-1 5.42×, CFPAC-1 3.49×, …; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.59×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.405× (z -13.9, q 6e-41, down in 23 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNS4]] (+0.62, fdr 7e-06, ⚠ same locus), [[B4GALT1]] (+0.59, fdr 1e-05), [[TBC1D8]] (+0.57, fdr 1e-05), [[SLC6A14]] (+0.57, fdr 1e-05); moves opposite to [[CBR3-AS1]] (-0.49, fdr 3e-05), [[OTUD7B]] (-0.48, fdr 6e-05), [[PLEKHO1]] (-0.46, fdr 1e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TGM2]] → it (grade B ⚠); 3 go from it, the strongest it → [[SLPI]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6572.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H2030 4.66×, PANC-1 6.56×, HS-578T 6.73×, CFPAC-1 3.84×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H2030 3.96×, HOP62 3.72×, PANC-1 5.42×, CFPAC-1 3.49×, …; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.59×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.82×** | +14.6 | 1e-45 | 25/29 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.44×** | +12.9 | 7e-36 | 20/23 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +7.9 | 5e-13 | 17/25 (CFPAC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +6.2 | 9e-08 | 14/29 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.60×** | +5.1 | 4e-05 | 16/28 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.054 | 12/29 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.82× | +3.2 | 0.10 | 9/20 (HOP62, HS-578T, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.55× | +3.2 | 0.10 | 7/29 (HepG2/C3A, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.52× | +3.1 | 0.14 | 10/28 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6572.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.405×** | -13.9 | 6e-41 | 23/29 (Hs 766T, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.405×** | -9.8 | 3e-20 | 24/29 (NCI-H2030, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.455×** | -8.6 | 2e-15 | 22/29 (LS 180, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.475×** | -8.1 | 1e-13 | 26/29 (A549, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.524×** | -7.0 | 3e-10 | 23/29 (LS 180, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.529×** | -6.9 | 4e-10 | 26/29 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.513×** | -6.5 | 8e-09 | 24/29 (Hs 766T, HOP62, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.597×** | -5.4 | 6e-06 | 20/29 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.715×** | -5.1 | 2e-05 | 20/29 (HOP62, SW 1271, …) | rises with dose | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **0.652×** | -4.5 | 5e-04 | 17/29 (hTERT-HPNE, Hs 766T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.665×** | -4.4 | 5e-04 | 18/29 (LS 180, HOP62, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.673×** | -4.3 | 9e-04 | 20/29 (HOP62, NCI-H2030, …) | top dose only | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.675×** | -4.3 | 9e-04 | 16/28 (SW 900, hTERT-HPNE, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.695×** | -3.9 | 0.003 | 17/29 (A549, HOP62, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.688×** | -3.9 | 0.004 | 12/28 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.714×** | -3.6 | 0.009 | 9/28 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.719×** | -3.6 | 0.012 | 14/29 (AsPC-1, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6572. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 55.9 | 1 (1 ⚠) | 11 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.2) |
| [[LS 180 (line)]] | wt | 106 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -20.5) |
| [[HOP62 (line)]] | alt | 162 | 3 (3 ⚠) | 6 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.59× (z +11.6) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -13.7) |
| [[A549 (line)]] | wt | 735 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -16.7) |
| [[NCI-H460 (line)]] | wt | 40.9 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.3) |
| [[HT-29 (line)]] | alt | 40.8 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 4.03× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -12.4) |
| [[Hs 766T (line)]] | wt | 212 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -23.8) |
| [[KATO III (line)]] | alt | 84.2 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 207 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -17.7) |
| [[CFPAC-1 (line)]] | alt | 62.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +10.2) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 53.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -13.0) |
| [[HCT15 (line)]] | alt | 47.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0485× (z -19.4) |
| [[HS-578T (line)]] | alt | 46.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.73× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 23.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 61.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -11.2) |
| [[PANC-1 (line)]] | alt | 15.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.56× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 39.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -10.9) |
| [[BT-474 (line)]] | alt | 37.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -11.2) |
| [[CHP-212 (line)]] | wt | 148 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 146 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.219× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.79× (z +10.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 78.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -8.7) |
| [[A-172 (line)]] | wt | 6.27 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.79 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.89 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.00 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.24 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.15 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.53 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.33 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6572), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNS4]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 | ⚠ same locus (18.1 kb: neighbours can correlate without regulation) |
| [[B4GALT1]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[TBC1D8]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[SLC6A14]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ATP1A1]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[SLC39A8]] | +0.53 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[DPYD]] | +0.53 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[CAPN8]] | +0.53 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ABCC3]] | +0.52 | +0.50 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[DPY19L1]] | +0.52 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[MMD]] | +0.51 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[PKP2]] | +0.51 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[SERPINA5]] | +0.50 | +0.49 / +0.38 | both halves | 7e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBR3-AS1]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[OTUD7B]] | -0.48 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[PLEKHO1]] | -0.46 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[ZNF761]] | -0.45 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[C19orf12]] | -0.44 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[LRSAM1]] | -0.44 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[HMOX1]] | -0.43 | -0.47 / -0.36 | both halves | 9e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[NOL7]] ⚠ | -0.43 | -0.43 / -0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CRYM]] | -0.43 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[CCSER2]] | -0.42 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[PGLS]] | -0.42 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[ZNF765]] | -0.42 | -0.38 / -0.44 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGM2]] | B | TGM2 activity raises IGFBP4's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 2.81× lower at baseline in the lines without TGM2 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[SLPI]] | B | SLPI activity raises IGFBP4's level | lines that do not express SLPI (25) vs lines expressing it (25) | 2.25× lower at baseline in the lines without SLPI | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| [[MAML2]] | B | MAML2 activity raises IGFBP4's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 3.04× lower at baseline in the lines without MAML2 | 0.081 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[TNS4]] | B | TNS4 activity raises IGFBP4's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 2.68× lower at baseline in the lines without TNS4 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[LINC00511]] | B | LINC00511 activity raises IGFBP4's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 2.51× lower at baseline in the lines without LINC00511 | 0.088 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[ABCC3]] | B | ABCC3 activity raises IGFBP4's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.85× lower at baseline in the lines without ABCC3 | 0.089 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[ITPK1]] | C | ITPK1 activity strengthens IGFBP4's drug response | lines that do not express ITPK1 (3) vs lines expressing it (26) | the lines without ITPK1 respond 0.66× as strongly (z diff +2.79); strongest at Homoharringtonine 5 µM: 0.92x vs 0.31x (z diff +7.6) | 0.047 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLPI]] | B | IGFBP4 activity raises SLPI's level | lines that do not express IGFBP4 (19) vs lines expressing it (31) | 2.52× lower at baseline in the lines without IGFBP4 | 0.046 | ⚠ within organs, on part of the lines; also absent: SDR16C5, TNFRSF1B, TSPAN15 |
| cells under [[Afatinib (drug)]] 0.05 µM | B | IGFBP4 activity lowers the cells' numbers under Afatinib 0.05 µM (makes them more sensitive) | lines that do not express IGFBP4 (19) vs lines expressing it (29) | the lines without IGFBP4: 1.10× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SDR16C5, TNFRSF1B, TSPAN15 |
| cells under [[Adagrasib (drug)]] 5 µM | B | IGFBP4 activity raises the cells' numbers under Adagrasib 5 µM (protects the cells) | lines that do not express IGFBP4 (19) vs lines expressing it (29) | the lines without IGFBP4: 0.85× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: SDR16C5, TNFRSF1B, TSPAN15 |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.519). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.4, 19.0); signed map (13.1, 33.1). **Vector** length 87.2, 24.6% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | +14.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +1.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.2 | +2.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.2 | +2.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.1 | +2.3 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -3.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.0 | -3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | insulin like growth factor binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:40,443,450-40,457,725 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IBP4, BP-4, HT29-IGFBP, IGFBP-4 |
| Gene groups (HGNC) | Insulin like growth factor binding proteins |
| Hallmark sets | XENOBIOTIC_METABOLISM, ESTROGEN_RESPONSE_LATE, EPITHELIAL_MESENCHYMAL_TRANSITION, ESTROGEN_RESPONSE_EARLY |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [P22692](https://www.uniprot.org/uniprotkb/P22692) (Insulin-like growth factor-binding protein 4):

> IGF-binding proteins prolong the half-life of the IGFs and have been shown to either inhibit or stimulate the growth promoting effects of the IGFs on cell culture. They alter the interaction of IGFs with their cell surface receptors.

**Summary**, from NCBI Gene [3487](https://www.ncbi.nlm.nih.gov/gene/3487):

> This gene is a member of the insulin-like growth factor binding protein (IGFBP) family and encodes a protein with an IGFBP domain and a thyroglobulin type-I domain. The protein binds both insulin-like growth factors (IGFs) I and II and circulates in the plasma in both glycosylated and non-glycosylated forms. Binding of this protein prolongs the half-life of the IGFs and alters their interaction with cell surface receptors. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5473) · Entrez [3487](https://www.ncbi.nlm.nih.gov/gene/3487) · UniProt [P22692](https://www.uniprot.org/uniprotkb/P22692) · Ensembl [ENSG00000141753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141753)

## Data

Gene col 6572: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6572); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6572, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6572]; `tensor/DDL_lfc|DDL_z.npy` [6572]; `embed/gene_vectors.npy` [6572]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6572 or target_col == 6572). Every well: [[IGFBP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGFBP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
