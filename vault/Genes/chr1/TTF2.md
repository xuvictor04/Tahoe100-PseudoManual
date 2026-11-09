---
symbol: "TTF2"
type: "gene"
col: 3845
ensembl_id: "ENSG00000116830"
name: "transcription termination factor 2"
location: "1p13.1"
module: 6
arm: "+"
pooled_cpm: 28.07
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TTF2

*transcription termination factor 2* — 1p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (21 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +14.4, q 3e-44, up in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.39× (z +7.8, q 4e-13, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.718× (z -8.0, q 6e-13, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.170×, SNU-1 0.104×); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.293×; ⚠ cell-cycle shift, explains ~58% of this change); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.367×; ⚠ cell-cycle shift, explains ~48% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.147×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (H4 0.100×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XRCC2]] (+0.70, fdr 7e-06), [[XRCC3]] (+0.70, fdr 7e-06), [[SUV39H2]] (+0.70, fdr 7e-06); moves opposite to [[CTR9]] (-0.63, fdr 1e-05), [[LINC00888-1]] (-0.61, fdr 1e-05), [[AFTPH]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 23 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3845.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.87×** | +14.4 | 3e-44 | 37/47 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.17×** | +13.3 | 7e-38 | 33/45 (SW480, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.90×** | +10.6 | 5e-24 | 29/36 (SW480, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.75×** | +9.7 | 7e-20 | 37/47 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.73×** | +9.4 | 5e-19 | 31/48 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.73×** | +8.7 | 3e-16 | 25/40 (CFPAC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +8.7 | 3e-16 | 32/47 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.66×** | +8.4 | 5e-15 | 29/46 (HS-578T, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.8 | 4e-13 | 30/48 (HS-578T, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +7.7 | 6e-13 | 29/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.51×** | +7.1 | 7e-11 | 27/47 (PANC-1, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.47×** | +6.6 | 2e-09 | 27/48 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +6.5 | 3e-09 | 27/47 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.46×** | +6.2 | 2e-08 | 22/44 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.44×** | +6.0 | 7e-08 | 25/48 (SW480, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +5.4 | 2e-06 | 24/47 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 6e-06 | 23/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.62×** | +4.3 | 4e-04 | 13/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.60×** | +4.2 | 6e-04 | 11/46 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.001 | 21/48 (A-172, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.003 | 9/48 (NCI-H23, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.004 | 7/47 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.026 | 14/47 (NCI-H1792, SNU-1, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.034 | 5/48 (A498, A-172, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.20×** | +3.0 | 0.044 | 9/48 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +2.9 | 0.062 | 5/48 (NCI-H1573, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +2.8 | 0.088 | 13/47 (HOP62, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3845.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.170×, SNU-1 0.104×); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.293×; ⚠ cell-cycle shift, explains ~58% of this change); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.367×; ⚠ cell-cycle shift, explains ~48% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.147×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (H4 0.100×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.718×** | -8.0 | 6e-13 | 29/48 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.694×** | -6.3 | 7e-08 | 31/47 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.795×** | -5.3 | 3e-05 | 25/48 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.808×** | -4.9 | 1e-04 | 23/48 (A-427, RKO, …) | rises with dose | low cells (technical?) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.735×** | -3.7 | 0.026 | 5/48 (SW480, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.837× | -3.1 | 0.16 | 14/48 (A-172, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.838× | -3.1 | 0.16 | 11/48 (CFPAC-1, A498, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3845. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 28.2 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +13.2) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.04× (z +10.2) | — |
| [[A498 (line)]] | wt | 40.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.10× (z +12.1) | — |
| [[A-172 (line)]] | wt | 27.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +15.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.12× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 28.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +14.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.30× (z +11.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 39.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -13.1) |
| [[SNU-423 (line)]] | alt | 17.2 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +10.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A-427 (line)]] | wt | 29.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.367× (z -10.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[AN3 CA (line)]] | alt | 57.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.147× (z -9.4) |
| [[H4 (line)]] | wt | 13.1 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.100× (z -8.5) |
| [[HOP62 (line)]] | alt | 10.1 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +8.8) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[J82 (line)]] | alt | 34.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.6) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[NCI-H1792 (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.03× (z +13.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H23 (line)]] | alt | 69.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SK-MEL-2 (line)]] | alt | 63.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.4) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SNU-1 (line)]] | wt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -13.0) |
| [[SW480 (line)]] | alt | 42.8 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +9.0) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3845), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRCC2]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[XRCC3]] | +0.70 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SUV39H2]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[VRK1]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[MCM5]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[CDC25A]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[MCM3]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[MCM4]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[KNTC1]] | +0.65 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[HNRNPAB]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PKMYT1]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[MCM6]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTR9]] | -0.63 | -0.54 / -0.58 | both halves | 1e-05 | STRING 750 |
| [[LINC00888-1]] | -0.61 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[AFTPH]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 | same gene group |
| [[A1BG]] | -0.58 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[OAZ1]] | -0.57 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[UBE2B]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | -0.56 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[KRT10]] ⚠ | -0.56 | -0.48 / -0.53 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TTF2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[E2F2]] | B | E2F2 activity raises TTF2's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.77× lower at baseline in the lines without E2F2 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[MPZL3]] | B | MPZL3 activity lowers TTF2's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.32× higher at baseline in the lines without MPZL3 | 0.068 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[CDC25A]] | B | CDC25A activity raises TTF2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.03× lower at baseline in the lines without CDC25A | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises TTF2's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.31× lower at baseline in the lines without MYBL2 | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-38.1, -43.8); signed map (-38.0, -48.4). **Vector** length 108, 28.5% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.53 to 28); *DNA Replication* (reactome, mean cos +0.52 to 40); *E2F G1/S* (control, mean cos +0.51 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.2 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.2 | +14.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.2 | +6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +4.1 | +5.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.0 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.3 | -8.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -6.1 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -6.1 | -6.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.1 | -3.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -3.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transcription termination factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.1 — chr1:117,060,326-117,107,453 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HuF2, ZGRF6 |
| Gene groups (HGNC) | Zinc fingers GRF-type; SNF2 related family; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNY4](https://www.uniprot.org/uniprotkb/Q9UNY4) (Transcription termination factor 2):

> DsDNA-dependent ATPase which acts as a transcription termination factor by coupling ATP hydrolysis with removal of RNA polymerase II from the DNA template. May contribute to mitotic transcription repression. May also be involved in pre-mRNA splicing.

**Summary**, from NCBI Gene [8458](https://www.ncbi.nlm.nih.gov/gene/8458):

> This gene encodes a member of the SWI2/SNF2 family of proteins, which play a critical role in altering protein-DNA interactions. The encoded protein has been shown to have dsDNA-dependent ATPase activity and RNA polymerase II termination activity. This protein interacts with cell division cycle 5-like, associates with human splicing complexes, and plays a role in pre-mRNA splicing. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12398](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12398) · Entrez [8458](https://www.ncbi.nlm.nih.gov/gene/8458) · UniProt [Q9UNY4](https://www.uniprot.org/uniprotkb/Q9UNY4) · Ensembl [ENSG00000116830](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116830)

## Data

Gene col 3845: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3845); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3845, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3845]; `tensor/DDL_lfc|DDL_z.npy` [3845]; `embed/gene_vectors.npy` [3845]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3845 or target_col == 3845). Every well: [[TTF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
