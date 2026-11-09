---
symbol: "ARL4A"
type: "gene"
col: 4361
ensembl_id: "ENSG00000122644"
name: "ARF like GTPase 4A"
location: "7p21.3"
module: 123
arm: "+"
pooled_cpm: 19.71
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# ARL4A

*ARF like GTPase 4A* — 7p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.47× (z +18.7, q 0e+00, up in 41 of 46 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.80× (z +10.9, q 1e-25, up in 40 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.138×, SK-MEL-2 0.155×, AN3 CA 0.112×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.368×, C-33 A 0.371×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C-33 A 0.232×, AN3 CA 0.140×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.344×, C-33 A 0.304×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNIP]] (+0.73, fdr 7e-06), [[MT1E]] (+0.67, fdr 7e-06), [[IRF2BP2]] (+0.65, fdr 1e-05); moves opposite to [[CTTN]] (-0.62, fdr 1e-05), [[THOC5]] (-0.61, fdr 1e-05), [[STX16-NPEPL1]] (-0.60, fdr 1e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LMCD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4361.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.47×** | +18.7 | 0e+00 | 41/46 (SW1417, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.67×** | +13.3 | 5e-38 | 44/47 (SW1417, SW480, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.80×** | +10.9 | 1e-25 | 40/46 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.46×** | +9.6 | 1e-19 | 37/47 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.12×** | +8.0 | 1e-13 | 37/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +7.5 | 5e-12 | 35/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +6.8 | 8e-10 | 33/47 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.88×** | +6.7 | 2e-09 | 32/46 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +4.6 | 3e-04 | 21/47 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.49×** | +4.2 | 0.001 | 19/45 (SW 900, NCI-H2347, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.003 | 21/46 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~73% of this change | **1.46×** | +4.0 | 0.003 | 23/43 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +3.0 | 0.100 | 16/47 (NCI-H1573, SW1417, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4361.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.138×, SK-MEL-2 0.155×, AN3 CA 0.112×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.368×, C-33 A 0.371×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C-33 A 0.232×, AN3 CA 0.140×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.344×, C-33 A 0.304×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.732× | -3.2 | 0.71 | 16/46 (Hs 766T, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4361. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 107 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -8.9) |
| [[SW480 (line)]] | alt | 53.1 | 3 (2 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.43× (z +11.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -9.7) |
| [[A-427 (line)]] | wt | 48.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.81× (z +10.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.61× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 16.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.09× (z +10.0) | — |
| [[A-172 (line)]] | wt | 10.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +15.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.26× (z +9.2) | — |
| [[A498 (line)]] | wt | 27.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +15.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.84× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 11.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +15.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.56× (z +8.7) | — |
| [[KATO III (line)]] | alt | 28.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +17.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.15× (z +11.4) | — |
| [[LoVo (line)]] | wt | 12.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +12.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.40× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 17.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +12.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.44× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 12.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +15.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.00× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 44.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +19.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.20× (z +13.9) | — |
| [[AN3 CA (line)]] | alt | 57.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 16.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +14.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.20× (z +8.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 21.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +12.4) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 18.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +11.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +12.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[COLO 205 (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +12.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 17.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +9.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HOP62 (line)]] | alt | 8.69 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +10.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +12.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 14.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +13.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 34.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[Panc 03.27 (line)]] | alt | 7.44 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.15× (z +11.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 10.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.63× (z +12.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4361), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNIP]] | +0.73 | +0.63 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[MT1E]] | +0.67 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[IRF2BP2]] | +0.65 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[MT1F]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TMEM42]] | +0.63 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[PIM3]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[ZNF22]] | +0.61 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[RHOB]] | +0.61 | +0.54 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[ZNF608]] | +0.60 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[PNRC1]] | +0.60 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PPP4R2]] | +0.60 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[ZFP36L2]] | +0.59 | +0.59 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTTN]] | -0.62 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[THOC5]] | -0.61 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[STX16-NPEPL1]] | -0.60 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[SMG1P6]] | -0.59 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[LY6G5B]] | -0.58 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[ZNF731P]] | -0.58 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[NDOR1]] | -0.58 | -0.49 / -0.49 | both halves | 2e-05 |  |
| [[AHSA1]] | -0.57 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[PRDM10]] | -0.57 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.55 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[FUBP3]] | -0.55 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[NIPA2]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMCD1]] | B | LMCD1 activity raises ARL4A's level | lines that do not express LMCD1 (11) vs lines expressing it (39) | 1.47× lower at baseline in the lines without LMCD1 | 0.013 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MT2A]] | B | MT2A activity lowers ARL4A's level | lines that do not express MT2A (9) vs lines expressing it (41) | 2.00× higher at baseline in the lines without MT2A | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X |
| [[MT1X]] | B | MT1X activity lowers ARL4A's level | lines that do not express MT1X (5) vs lines expressing it (45) | 2.34× higher at baseline in the lines without MT1X | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RABGEF1P3, KIFC3, ENSG00000255031; its own permutation p |
| [[ANKRD20A8P]] | B | ANKRD20A8P activity raises ARL4A's level | lines that do not express ANKRD20A8P (38) vs lines expressing it (12) | 1.47× lower at baseline in the lines without ANKRD20A8P | 0.094 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.6, 12.0); signed map (12.4, 26.6). **Vector** length 99.4, 24.0% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.52 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +7.7 | +13.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +7.0 | +18.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +10.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +2.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.9 | +2.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.8 | +2.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.7 | +2.1 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.1 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.3 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.3 — chr7:12,686,856-12,690,958 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ARL4 |
| Gene groups (HGNC) | ARF GTPase family |
| Hallmark sets | SPERMATOGENESIS, IL2_STAT5_SIGNALING, INTERFERON_GAMMA_RESPONSE, ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [P40617](https://www.uniprot.org/uniprotkb/P40617) (ADP-ribosylation factor-like protein 4A):

> Small GTP-binding protein which cycles between an inactive GDP-bound and an active GTP-bound form, and the rate of cycling is regulated by guanine nucleotide exchange factors (GEF) and GTPase-activating proteins (GAP). GTP-binding protein that does not act as an allosteric activator of the cholera toxin catalytic subunit. Recruits CYTH1, CYTH2, CYTH3 and CYTH4 to the plasma membrane in GDP-bound form.

**Summary**, from NCBI Gene [10124](https://www.ncbi.nlm.nih.gov/gene/10124):

> ADP-ribosylation factor-like 4A is a member of the ADP-ribosylation factor family of GTP-binding proteins. ARL4A is similar to ARL4C and ARL4D and each has a nuclear localization signal and an unusually high guaninine nucleotide exchange rate. ARL4A is located in both the nuclear and extranuclear cell compartments. Multiple transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:695](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:695) · Entrez [10124](https://www.ncbi.nlm.nih.gov/gene/10124) · UniProt [P40617](https://www.uniprot.org/uniprotkb/P40617) · Ensembl [ENSG00000122644](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122644)

## Data

Gene col 4361: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4361); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4361, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4361]; `tensor/DDL_lfc|DDL_z.npy` [4361]; `embed/gene_vectors.npy` [4361]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4361 or target_col == 4361). Every well: [[ARL4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
