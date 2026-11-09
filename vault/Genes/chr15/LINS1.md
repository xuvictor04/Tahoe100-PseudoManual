---
symbol: "LINS1"
type: "gene"
col: 6415
ensembl_id: "ENSG00000140471"
name: "lines homolog 1"
location: "15q26.3"
module: 11
arm: "+"
pooled_cpm: 17.51
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# LINS1

*lines homolog 1* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.03× (z +30.5, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.713× (z -6.4, q 1e-07, down in 25 of 44 measured lines) ⚠ toxic. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A549 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (J82 0.139×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.243×; ⚠ toxic; transcription drop); [[Pimozide (drug)]] 0.05 µM in 1 line (BT-474 0.189×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSPRY1]] (+0.66, fdr 7e-06), [[NFX1]] (+0.65, fdr 7e-06), [[HELQ]] (+0.64, fdr 1e-05); moves opposite to [[PACC1]] (-0.65, fdr 2e-05), [[ZNF483]] (-0.61, fdr 2e-05), [[UBE2Q2P2-1]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6415.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.03×** | +30.5 | 0e+00 | 44/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.66×** | +26.8 | 0e+00 | 44/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.52×** | +17.9 | 0e+00 | 42/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.48×** | +16.9 | 0e+00 | 42/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.14×** | +14.7 | 0e+00 | 43/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.23×** | +14.6 | 0e+00 | 40/48 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.00×** | +13.4 | 5e-39 | 44/47 (AsPC-1, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.97×** | +13.2 | 1e-37 | 43/48 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +11.6 | 2e-29 | 34/47 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +11.4 | 2e-28 | 32/42 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +10.4 | 1e-23 | 34/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +9.1 | 4e-18 | 26/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.7 | 4e-13 | 21/48 (HOP62, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +7.5 | 2e-12 | 27/48 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +7.3 | 1e-11 | 29/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +6.8 | 5e-10 | 23/44 (LS 180, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +5.8 | 2e-07 | 23/47 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +5.6 | 6e-07 | 22/47 (SW 900, SNU-423, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +5.5 | 9e-07 | 20/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6415.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A549 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (J82 0.139×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.243×; ⚠ toxic; transcription drop); [[Pimozide (drug)]] 0.05 µM in 1 line (BT-474 0.189×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.713×** | -6.4 | 1e-07 | 25/44 (NCI-H2030, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.760×** | -5.2 | 6e-05 | 17/28 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -4.9 | 2e-04 | 14/48 (RPMI-7951, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.824×** | -3.8 | 0.019 | 15/41 (COLO 205, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.835× | -3.3 | 0.12 | 15/35 (A549, SW480, …) | all doses, stronger at high dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6415. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +20.3) | — |
| [[LoVo (line)]] | wt | 21.8 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 17.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +18.7) | — |
| [[J82 (line)]] | alt | 12.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.67× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 26.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +14.5) | — |
| [[SW 900 (line)]] | alt | 15.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +11.8) | — |
| [[SW480 (line)]] | alt | 20.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +15.7) | — |
| [[A-172 (line)]] | wt | 11.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +11.5) | — |
| [[A549 (line)]] | wt | 22.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 44.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -9.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 10.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +13.3) | — |
| [[LOX-IMVI (line)]] | wt | 16.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +12.7) | — |
| [[LS 180 (line)]] | wt | 13.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.87 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +14.2) | — |
| [[NCI-H1792 (line)]] | alt | 20.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +14.0) | — |
| [[NCI-H2030 (line)]] | alt | 14.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +13.9) | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +12.7) | — |
| [[SNU-423 (line)]] | alt | 11.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.22× (z +15.4) | — |
| [[A498 (line)]] | wt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +12.7) | — |
| [[BT-474 (line)]] | alt | 17.3 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.189× (z -8.9) |
| [[C-33 A (line)]] | alt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.1) | — |
| [[C32 (line)]] | wt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +11.8) | — |
| [[HCT15 (line)]] | alt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 18.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 18.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +11.8) | — |
| [[HS-578T (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 40.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +11.2) | — |
| [[KATO III (line)]] | alt | 29.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 19.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +9.6) | — |
| [[RKO (line)]] | wt | 15.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +13.0) | — |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +12.9) | — |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6415), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSPRY1]] | +0.66 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[NFX1]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[HELQ]] | +0.64 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[CHTF8]] | +0.64 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[ZNF689]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.62 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[ARMC5]] | +0.62 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[C14orf119]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TOGARAM1]] | +0.61 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[PDCD7]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[LATS1]] | +0.60 | +0.63 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACC1]] | -0.65 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[ZNF483]] | -0.61 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[UBE2Q2P2-1]] | -0.60 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[NDRG3]] | -0.60 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[GNB5]] | -0.59 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[PRKCI]] | -0.59 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[INPP4A]] | -0.59 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[CAMK2G]] | -0.58 | -0.61 / -0.32 | both halves | 1e-04 |  |
| [[WASF3]] | -0.58 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[UBE2Q2P2]] | -0.58 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[SLC23A2]] | -0.57 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[METAP1]] | -0.57 | -0.66 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LINS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.537). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.5, 2.3); signed map (-1.3, -15.0). **Vector** length 70.6, 12.9% of its response variance represented; |z| ≥ 3 in 1,233 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +14.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +17.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +30.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +7.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +16.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +6.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.6 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.5 | -6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.9 | -3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | lines homolog 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:100,559,369-100,603,230 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WINS1; previously LINS, MRT27 |
| Matched by | ensembl_id |

UniProt [Q8NG48](https://www.uniprot.org/uniprotkb/Q8NG48) carries no function annotation.

**Summary**, from NCBI Gene [55180](https://www.ncbi.nlm.nih.gov/gene/55180):

> The Drosophila segment polarity gene lin encodes a protein, lines, which plays important roles in development of the epidermis and hindgut. This gene encodes a protein containing a lines-like domain. This gene is located on chromosome 15 and clustered with the gene encoding ankyrin repeat and SOCS box-containing protein 7. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2017]

**Accessions** — [HGNC:30922](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30922) · Entrez [55180](https://www.ncbi.nlm.nih.gov/gene/55180) · UniProt [Q8NG48](https://www.uniprot.org/uniprotkb/Q8NG48) · Ensembl [ENSG00000140471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140471)

## Data

Gene col 6415: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6415); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6415, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6415]; `tensor/DDL_lfc|DDL_z.npy` [6415]; `embed/gene_vectors.npy` [6415]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6415 or target_col == 6415). Every well: [[LINS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LINS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
