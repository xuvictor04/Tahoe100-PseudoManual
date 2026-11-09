---
symbol: "TRABD2A"
type: "gene"
col: 11862
ensembl_id: "ENSG00000186854"
name: "TraB domain containing 2A"
location: "2p11.2"
module: 73
arm: "+"
pooled_cpm: 20.09
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# TRABD2A

*TraB domain containing 2A* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.88× (z +28.4, q 0e+00, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.746× (z -4.2, q 0.013, down in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (KATO III 0.177×, RKO 0.187×, LS 180 0.222×; ⚠ cell-cycle shift, explains ~26% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (LoVo 0.125×, LS 180 0.101×, KATO III 0.221×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LoVo 0.127×, LS 180 0.108×; ⚠ cell-cycle shift, explains ~0% of this change); [[Hexylresorcinol (drug)]] 5 µM in 2 lines (LoVo 0.462×, LS 180 0.431×); [[Harringtonine (drug)]] 5 µM in 1 line (LoVo 0.248×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LS 180 0.243×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEPTIN9-DT]] (+0.65, fdr 1e-05), [[LINC02580]] (+0.61, fdr 1e-05), [[BAIAP2L2]] (+0.59, fdr 4e-05); moves opposite to [[COMMD2]] (-0.49, fdr 1e-04), [[NAA40]] (-0.49, fdr 1e-04), [[SSNA1]] (-0.48, fdr 3e-04).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TPTEP1-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11862.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.88×** | +28.4 | 0e+00 | 39/44 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +12.6 | 1e-33 | 32/36 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +11.4 | 6e-28 | 21/27 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +9.2 | 6e-18 | 22/32 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.52×** | +8.8 | 2e-16 | 23/46 (NCI-H1792, NCI-H460, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +7.9 | 3e-13 | 18/48 (PANC-1, SNU-423, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +7.0 | 2e-10 | 24/46 (A-172, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +7.0 | 2e-10 | 21/48 (HOP62, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +6.4 | 9e-09 | 26/44 (HS-578T, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.8 | 4e-07 | 23/45 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.46×** | +5.6 | 1e-06 | 24/47 (BT-474, HepG2/C3A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.5 | 2e-06 | 22/48 (PANC-1, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.2 | 7e-06 | 19/46 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.37×** | +4.7 | 1e-04 | 20/46 (NCI-H460, SW1417, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 4e-04 | 14/45 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 5e-04 | 12/47 (HOP62, A-172, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.8 | 0.005 | 9/42 (CFPAC-1, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.20× | +3.7 | 0.007 | 14/48 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.008 | 8/45 (HepG2/C3A, HEC-1-A, …) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.010 | 8/46 (BT-474, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.013 | 5/46 (NCI-H1792, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Dexmedetomidine (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.018 | 4/46 (C32, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.018 | 10/47 (NCI-H2030, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11862.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (KATO III 0.177×, RKO 0.187×, LS 180 0.222×; ⚠ cell-cycle shift, explains ~26% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (LoVo 0.125×, LS 180 0.101×, KATO III 0.221×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LoVo 0.127×, LS 180 0.108×; ⚠ cell-cycle shift, explains ~0% of this change); [[Hexylresorcinol (drug)]] 5 µM in 2 lines (LoVo 0.462×, LS 180 0.431×); [[Harringtonine (drug)]] 5 µM in 1 line (LoVo 0.248×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LS 180 0.243×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.746×** | -4.2 | 0.013 | 18/47 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.794× | -3.2 | 0.42 | 10/48 (LoVo, LS 180, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11862. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 132 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.243× (z -10.2) |
| [[LoVo (line)]] | wt | 102 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -16.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.248× (z -10.8) |
| [[HOP62 (line)]] | alt | 14.7 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +14.5) | — |
| [[NCI-H460 (line)]] | wt | 12.3 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.30× (z +17.2) | — |
| [[KATO III (line)]] | alt | 55.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -17.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 9.06 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +12.9) | — |
| [[RKO (line)]] | wt | 33.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -16.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 14.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +12.7) | — |
| [[H4 (line)]] | wt | 12.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +9.4) | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0861× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 15.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +13.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +9.5) | — |
| [[A498 (line)]] | wt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.54× (z +18.6) | — |
| [[A549 (line)]] | wt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 21.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 6.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.83× (z +9.0) | — |
| [[C32 (line)]] | wt | 7.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.92× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +12.2) | — |
| [[HEC-1-A (line)]] | alt | 8.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.43× (z +12.3) | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.32× (z +14.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +8.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.11× (z +12.9) | — |
| [[NCI-H1792 (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.38× (z +18.2) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 8.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 9.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.13× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 9.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +9.4) | — |
| [[SW48 (line)]] | wt | 35.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 18.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.8) | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11862), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN9-DT]] | +0.65 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[LINC02580]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[BAIAP2L2]] | +0.59 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[SLC22A3]] | +0.58 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[UBE2R2-AS1]] | +0.58 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[CASC11]] | +0.57 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[SLC6A20]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PPP1R15B-AS1]] | +0.56 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[TBXAS1]] | +0.56 | +0.39 / +0.60 | both halves | 6e-05 |  |
| [[CTSE]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[DGUOK-AS1]] | +0.56 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[PRSS48]] | +0.55 | +0.57 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD2]] | -0.49 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[NAA40]] | -0.49 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[SSNA1]] | -0.48 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[NSFL1C]] | -0.47 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[FITM2]] | -0.46 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[ISCA2]] | -0.46 | -0.24 / -0.35 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPTEP1-1]] | B | TPTEP1-1 activity raises TRABD2A's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 2.34× lower at baseline in the lines without TPTEP1-1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975 |
| [[LINC02582]] | B | LINC02582 activity raises TRABD2A's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.23× lower at baseline in the lines without LINC02582 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[MMP28]] | B | MMP28 activity raises TRABD2A's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.48× lower at baseline in the lines without MMP28 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[DSG4]] | B | DSG4 activity raises TRABD2A's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 3.30× lower at baseline in the lines without DSG4 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[LINC02582]] | B | LINC02582 activity weakens TRABD2A's drug response | lines that do not express LINC02582 (41) vs lines expressing it (7) | the lines without LINC02582 respond 3.63× as strongly (z diff -2.60); strongest at Homoharringtonine 5 µM: 1.62x vs 0.54x (z diff -7.3) | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers TRABD2A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SPON1]] | B | SPON1 activity raises TRABD2A's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 1.83× lower at baseline in the lines without SPON1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A |
| [[NR3C1]] | B | NR3C1 activity raises TRABD2A's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.7% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.7, 48.4); signed map (69.3, 6.3). **Vector** length 90.5, 18.7% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.4 | +28.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.1 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +7.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +1.9 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.3 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | TraB domain containing 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:84,821,650-84,907,008 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIKI1; previously C2orf89 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86V40](https://www.uniprot.org/uniprotkb/Q86V40) (Metalloprotease TIKI1):

> Metalloprotease that acts as a negative regulator of the Wnt signaling pathway by mediating the cleavage of the 8 N-terminal residues of a subset of Wnt proteins. Following cleavage, Wnt proteins become oxidized and form large disulfide-bond oligomers, leading to their inactivation. Able to cleave WNT3A, WNT5, but not WNT11. Required for head formation.

**Summary**, from NCBI Gene [129293](https://www.ncbi.nlm.nih.gov/gene/129293):

> Enables Wnt-protein binding activity and metalloendopeptidase activity. Involved in negative regulation of Wnt signaling pathway and proteolysis. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27013) · Entrez [129293](https://www.ncbi.nlm.nih.gov/gene/129293) · UniProt [Q86V40](https://www.uniprot.org/uniprotkb/Q86V40) · Ensembl [ENSG00000186854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186854)

## Data

Gene col 11862: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11862); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11862, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11862]; `tensor/DDL_lfc|DDL_z.npy` [11862]; `embed/gene_vectors.npy` [11862]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11862 or target_col == 11862). Every well: [[TRABD2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRABD2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
