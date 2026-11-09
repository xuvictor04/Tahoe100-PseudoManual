---
symbol: "RAD54L"
type: "gene"
col: 1449
ensembl_id: "ENSG00000085999"
name: "RAD54 like"
location: "1p34.1"
module: 6
arm: "+"
pooled_cpm: 18.34
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 31
n_dd_up_clean: 4
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RAD54L

*RAD54 like* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (27 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.17× (z +10.0, q 1e-20, up in 34 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Gemcitabine (drug)]] 0.05 µM: 1.24× (z +3.7, q 0.007, up in 12 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.388× (z -12.2, q 1e-31, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXO1]] (+0.91, fdr 7e-06), [[DTL]] (+0.91, fdr 7e-06), [[FANCA]] (+0.91, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 27 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 27 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.17×** | +10.0 | 1e-20 | 34/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.02×** | +9.0 | 6e-17 | 32/47 (SW480, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.99×** | +8.9 | 1e-16 | 30/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.85×** | +7.9 | 5e-13 | 30/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.87×** | +7.7 | 2e-12 | 32/45 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.48×** | +6.7 | 2e-09 | 26/46 (NCI-H2030, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.64×** | +6.4 | 2e-08 | 24/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.61×** | +6.1 | 7e-08 | 24/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.63×** | +6.1 | 9e-08 | 28/47 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~70% of this change | **1.63×** | +6.0 | 9e-08 | 25/44 (NCI-H460, PANC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +5.2 | 9e-06 | 20/47 (MIA PaCa-2, RKO, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.49×** | +5.1 | 2e-05 | 21/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.44×** | +4.6 | 2e-04 | 20/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.43×** | +4.6 | 2e-04 | 24/47 (MIA PaCa-2, J82, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.42×** | +4.5 | 2e-04 | 17/44 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.007 | 12/48 (SW480, J82, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.012 | 17/48 (SW480, SNU-423, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +3.3 | 0.017 | 16/44 (PANC-1, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.37×** | +2.9 | 0.079 | 4/48 (SW480, HOP62, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1449.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.388×** | -12.2 | 1e-31 | 37/46 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.626×** | -8.2 | 6e-14 | 26/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.520×** | -8.2 | 7e-14 | 29/47 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.571×** | -7.3 | 5e-11 | 32/48 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.586×** | -6.9 | 4e-10 | 28/47 (A-427, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.632×** | -6.0 | 2e-07 | 24/47 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.670×** | -5.2 | 2e-05 | 25/45 (NCI-H460, LS 180, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.682×** | -5.0 | 4e-05 | 20/47 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.756×** | -5.0 | 4e-05 | 22/47 (LS 180, COLO 205, …) | all doses, stronger at high dose | low cells (technical?) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.597×** | -4.8 | 1e-04 | 22/48 (SW480, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.698×** | -4.4 | 5e-04 | 18/48 (LoVo, CFPAC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.778×** | -4.4 | 5e-04 | 19/48 (COLO 205, KATO III, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.713×** | -4.4 | 5e-04 | 17/46 (NCI-H661, RKO, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.786×** | -4.2 | 0.001 | 18/48 (HCT15, Hs 766T, …) | two highest doses |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.552×** | -3.9 | 0.004 | 15/45 (NCI-H2030, C-33 A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.749×** | -3.8 | 0.006 | 19/45 (LoVo, RKO, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.019 | 16/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.021 | 11/48 (SW 1088, RKO, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.773×** | -3.4 | 0.021 | 15/45 (PANC-1, H4, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.773×** | -3.4 | 0.021 | 16/47 (RKO, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[palbociclib (drug)]] 5 µM |  | **0.610×** | -3.2 | 0.032 | 16/45 (H4, A498, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.35 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 13.9 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.185× (z -11.9) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.188× (z -11.7) |
| [[A-427 (line)]] | wt | 33.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -15.2) |
| [[A498 (line)]] | wt | 38.5 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.191× (z -13.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.441× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 10.3 | 3 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 6.91× (z +10.9) ⚠ cell-cycle shift, explains ~67% of this change | [[Selinexor (drug)]] 5 µM 0.306× (z -8.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HEC-1-A (line)]] | alt | 32.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 36.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -13.5) |
| [[AsPC-1 (line)]] | alt | 5.23 | 0 | 2 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0887× (z -9.0) |
| [[HOP62 (line)]] | alt | 20.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -13.3) |
| [[KATO III (line)]] | alt | 15.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0595× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 20.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.101× (z -11.9) |
| [[SW480 (line)]] | alt | 21.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -16.2) |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0843× (z -11.2) ⚠ cell-cycle shift, explains ~52% of this change |
| [[H4 (line)]] | wt | 18.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -11.9) |
| [[Hs 766T (line)]] | wt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -9.3) |
| [[HT-29 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -8.8) |
| [[PANC-1 (line)]] | alt | 19.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +8.9) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[RKO (line)]] | wt | 24.3 | 0 | 1 | — | [[LJI308 (drug)]] 5 µM 0.0460× (z -9.0) |
| [[SHP-77 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -9.7) |
| [[SW48 (line)]] | wt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -8.6) |
| [[A-172 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXO1]] | +0.91 | +0.90 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 832 |
| [[DTL]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | STRING 516 |
| [[FANCA]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | STRING 749 |
| [[PCLAF]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | STRING 595 |
| [[CHAF1A]] | +0.89 | +0.84 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 600 |
| [[RAD51]] | +0.89 | +0.88 / +0.88 | both halves | 7e-06 | STRING 992 |
| [[FANCI]] | +0.89 | +0.89 / +0.88 | both halves | 7e-06 | STRING 784 |
| [[CDC45]] | +0.88 | +0.88 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 856 |
| [[DSCC1]] | +0.88 | +0.84 / +0.89 | both halves | 7e-06 | STRING 502 |
| [[WDR76]] | +0.88 | +0.89 / +0.85 | both halves | 7e-06 |  |
| [[BLM]] | +0.88 | +0.89 / +0.87 | both halves | 7e-06 | STRING 738 |
| [[MELK]] | +0.88 | +0.88 / +0.86 | both halves | 7e-06 | STRING 649 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises RAD54L's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.33× lower at baseline in the lines without E2F8 | 0.016 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises RAD54L's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.19× lower at baseline in the lines without CDC25A | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises RAD54L's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.72× lower at baseline in the lines without TCF19 | 0.022 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers RAD54L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[E2F2]] | B | E2F2 activity raises RAD54L's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.95× lower at baseline in the lines without E2F2 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises RAD54L's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.56× lower at baseline in the lines without FAM111B | 0.063 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers RAD54L's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GGH]] | B | GGH activity raises RAD54L's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.35× lower at baseline in the lines without GGH | 0.097 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises RAD54L's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.36× lower at baseline in the lines without DSCC1 | 0.018 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises RAD54L's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.53× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[BRME1]] | C | BRME1 activity raises RAD54L's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 1.93× lower at baseline in the lines without BRME1 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises RAD54L's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.33× lower at baseline in the lines without E2F1, MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.914). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.2, -45.3); signed map (-37.9, -44.0). **Vector** length 139, 43.1% of its response variance represented; |z| ≥ 3 in 1,284 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.68 to 65); *DNA strand elongation* (reactome, mean cos +0.72 to 28); *DNA Replication* (reactome, mean cos +0.72 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +5.6 | +7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.0 | +4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | +6.1 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +4.2 | +4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +4.2 | +6.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.6 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.5 | -12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.0 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -6.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.0 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | RAD54 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:46,246,461-46,278,480 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hHR54, hRAD54, RAD54A |
| Gene groups (HGNC) | SNF2 related family |
| Hallmark sets | G2M_CHECKPOINT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92698](https://www.uniprot.org/uniprotkb/Q92698) (DNA repair and recombination protein RAD54-like):

> Multifunctional ATPase that plays a role in homologous recombination (HR) which is a major pathway for repairing DNA double-strand breaks (DSBs), single-stranded DNA (ssDNA) gaps, and stalled or collapsed replication forks. Acts as a molecular motor during the homology search and guides RAD51 ssDNA along a donor dsDNA thereby changing the homology search from the diffusion-based mechanism to a motor-guided mechanism. Also plays an essential role in RAD51-mediated synaptic complex formation …

**Summary**, from NCBI Gene [8438](https://www.ncbi.nlm.nih.gov/gene/8438):

> The protein encoded by this gene belongs to the DEAD-like helicase superfamily, and shares similarity with Saccharomyces cerevisiae Rad54, a protein known to be involved in the homologous recombination and repair of DNA. This protein has been shown to play a role in homologous recombination related repair of DNA double-strand breaks. The binding of this protein to double-strand DNA induces a DNA topological change, which is thought to facilitate homologous DNA paring, and stimulate DNA …

**Accessions** — [HGNC:9826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9826) · Entrez [8438](https://www.ncbi.nlm.nih.gov/gene/8438) · UniProt [Q92698](https://www.uniprot.org/uniprotkb/Q92698) · Ensembl [ENSG00000085999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085999)

## Data

Gene col 1449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1449); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1449]; `tensor/DDL_lfc|DDL_z.npy` [1449]; `embed/gene_vectors.npy` [1449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1449 or target_col == 1449). Every well: [[RAD54L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD54L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
