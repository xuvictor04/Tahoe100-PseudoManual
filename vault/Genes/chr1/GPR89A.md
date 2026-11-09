---
symbol: "GPR89A"
type: "gene"
col: 3889
ensembl_id: "ENSG00000117262"
name: "golgi pH regulator A"
location: "1q21.1"
module: 142
arm: "+"
pooled_cpm: 22.07
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# GPR89A

*golgi pH regulator A* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.07× (z +12.1, q 4e-31, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.448× (z -12.4, q 2e-32, down in 29 of 38 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (NCI-H460 0.177×, A549 0.0993×, HT-29 0.0584×, SNU-423 0.0911×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 0.222×, A-427 0.171×, SHP-77 0.213×, NCI-H2030 0.266×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (AsPC-1 0.155×, A498 0.225×, SW480 0.341×, NCI-H460 0.341×; ⚠ toxic; transcription drop); [[Decitabine (drug)]] 0.05 µM in 1 line (SW48 0.118×); [[Ranolazine (drug)]] 0.05 µM in 1 line (SW48 0.151×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR89B]] (+0.88, fdr 7e-06), [[SLC30A6]] (+0.77, fdr 7e-06), [[RABEPK]] (+0.75, fdr 7e-06); moves opposite to [[VEZF1]] (-0.66, fdr 7e-06), [[BCL3]] (-0.65, fdr 1e-05), [[RAP2C-AS1]] (-0.65, fdr 7e-06).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AHR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3889.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.07×** | +12.1 | 4e-31 | 43/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +11.1 | 3e-26 | 41/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +10.4 | 6e-23 | 42/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +9.3 | 3e-18 | 34/47 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +7.6 | 4e-12 | 34/48 (CFPAC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.45×** | +6.0 | 2e-07 | 28/45 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.99×** | +6.0 | 2e-07 | 28/40 (RKO, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +6.0 | 2e-07 | 24/46 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.38×** | +5.4 | 5e-06 | 23/47 (RKO, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.56×** | +5.2 | 1e-05 | 19/48 (RKO, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.6 | 2e-04 | 20/47 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.31×** | +4.4 | 5e-04 | 19/46 (NCI-H23, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 1.17× | +3.6 | 0.016 | 12/48 (J82, SNU-423, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.17× | +3.5 | 0.017 | 17/48 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.23×** | +3.4 | 0.029 | 19/48 (NCI-H23, SNU-1, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.042 | 6/48 (NCI-H460, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3889.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (NCI-H460 0.177×, A549 0.0993×, HT-29 0.0584×, SNU-423 0.0911×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 0.222×, A-427 0.171×, SHP-77 0.213×, NCI-H2030 0.266×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (AsPC-1 0.155×, A498 0.225×, SW480 0.341×, NCI-H460 0.341×; ⚠ toxic; transcription drop); [[Decitabine (drug)]] 0.05 µM in 1 line (SW48 0.118×); [[Ranolazine (drug)]] 0.05 µM in 1 line (SW48 0.151×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.448×** | -12.4 | 2e-32 | 29/38 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.517×** | -11.0 | 8e-26 | 32/42 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -9.8 | 3e-20 | 26/34 (AsPC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.612×** | -7.9 | 4e-13 | 28/47 (A498, A549, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.774×** | -5.6 | 2e-06 | 24/47 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.746×** | -4.9 | 9e-05 | 18/48 (A498, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.822×** | -3.3 | 0.088 | 18/47 (A-172, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.760× | -3.2 | 0.10 | 12/44 (A498, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.872× | -3.2 | 0.10 | 12/48 (SW480, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~81% of this change | 0.833× | -3.0 | 0.13 | 16/46 (KATO III, A-172, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3889. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 23.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 30.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -15.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 22.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -9.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 17.7 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.233× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~81% of this change |
| [[SW48 (line)]] | wt | 19.2 | 0 | 2 | — | [[Decitabine (drug)]] 0.05 µM 0.118× (z -9.5) |
| [[SW480 (line)]] | alt | 29.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -15.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -13.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0993× (z -15.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -12.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0912× (z -8.6) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 20.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.39× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 20.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.61× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0584× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -8.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -8.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -12.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0911× (z -12.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -11.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3889), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR89B]] | +0.88 | +0.82 / +0.88 | both halves | 7e-06 | STRING 780 |
| [[SLC30A6]] | +0.77 | +0.67 / +0.79 | both halves | 7e-06 |  |
| [[RABEPK]] | +0.75 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[EEF1AKMT4]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[C8orf76]] | +0.68 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[IQCB1]] | +0.67 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ZCCHC17]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[RARS2]] | +0.66 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CCDC32]] | +0.66 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[SS18L1]] | +0.66 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[QPCTL]] | +0.65 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[STARD3]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEZF1]] | -0.66 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[BCL3]] | -0.65 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[RAP2C-AS1]] | -0.65 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[CGGBP1]] | -0.64 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.63 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[TBL1XR1]] | -0.63 | -0.36 / -0.68 | both halves | 9e-05 |  |
| [[YWHAE]] | -0.62 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[DZIP3]] | -0.62 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[SYNPO]] | -0.62 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[CCDC148]] | -0.62 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[BMI1]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[HNRNPH3]] | -0.61 | -0.47 / -0.60 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHR]] | B | AHR activity lowers GPR89A's level | lines that do not express AHR (7) vs lines expressing it (43) | 1.25× higher at baseline in the lines without AHR | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[SERTAD4]] | B | SERTAD4 activity lowers GPR89A's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.12× higher at baseline in the lines without SERTAD4 | 0.060 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.821). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.4, -4.9); signed map (-44.7, 3.6). **Vector** length 92.7, 20.3% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.3 | +9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | +4.9 | +6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.8 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.3 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +4.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +5.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.1 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.7 | -5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.8 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -5.4 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.3 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.1 | -12.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | golgi pH regulator A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:145,607,988-145,670,650 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GPHR, UNQ192; previously GPR89A |
| Gene groups (HGNC) | Golgi pH regulators |
| Matched by | ensembl_id |

**Function**, from UniProt [B7ZAQ6](https://www.uniprot.org/uniprotkb/B7ZAQ6) (Golgi pH regulator A):

> Voltage-gated channel that enables the transfer of monoatomic anions such as iodide, chloride, bromide and fluoride which may function in counter-ion conductance and participates in Golgi acidification. Plays a role in lymphocyte development, probably by acting as a RABL3 effector in hematopoietic cells (By similarity). Essential for maintaining the acidic luminal pH of the Golgi apparatus in neurons, which is important for preserving Golgi structural integrity (By similarity). This integrity …

**Summary**, from NCBI Gene [653519](https://www.ncbi.nlm.nih.gov/gene/653519):

> Enables voltage-gated monoatomic anion channel activity. Involved in intracellular pH reduction. Located in Golgi cisterna membrane and Golgi-associated vesicle membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31984) · Entrez [653519](https://www.ncbi.nlm.nih.gov/gene/653519) · UniProt [B7ZAQ6](https://www.uniprot.org/uniprotkb/B7ZAQ6) · Ensembl [ENSG00000117262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117262)

## Data

Gene col 3889: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3889); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3889, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3889]; `tensor/DDL_lfc|DDL_z.npy` [3889]; `embed/gene_vectors.npy` [3889]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3889 or target_col == 3889). Every well: [[GPR89A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPR89A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
