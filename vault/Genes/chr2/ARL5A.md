---
symbol: "ARL5A"
type: "gene"
col: 8610
ensembl_id: "ENSG00000162980"
name: "ARF like GTPase 5A"
location: "2q23.3"
module: 25
arm: "+"
pooled_cpm: 69.05
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ARL5A

*ARF like GTPase 5A* — 2q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.88× (z +20.4, q 0e+00, up in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.40× (z +10.8, q 3e-25, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.732× (z -10.1, q 3e-21, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPY19L4]] (+0.63, fdr 6e-05), [[ZNF587B]] (+0.61, fdr 4e-05), [[TXNDC5]] (+0.60, fdr 1e-05); moves opposite to [[POLD4]] (-0.63, fdr 4e-05), [[H3-3B]] (-0.58, fdr 1e-04), [[PLEKHN1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8610.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +20.4 | 0e+00 | 43/49 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +19.5 | 0e+00 | 39/44 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +14.4 | 1e-44 | 32/45 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +10.8 | 3e-25 | 33/48 (SNU-423, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.20× | +8.2 | 3e-14 | 21/48 (SK-MEL-2, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +7.6 | 2e-12 | 28/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.16× | +4.9 | 9e-05 | 17/48 (HT-29, Hs 766T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +4.8 | 1e-04 | 16/47 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.15× | +4.4 | 6e-04 | 10/48 (C-33 A, HEC-1-A, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.002 | 11/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.009 | 11/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.12× | +3.6 | 0.016 | 4/48 (SNU-423, LS 180, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.030 | 9/48 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8610.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.732×** | -10.1 | 3e-21 | 32/48 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.735×** | -9.6 | 2e-19 | 32/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.826×** | -8.8 | 3e-16 | 28/48 (RKO, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.783×** | -7.9 | 3e-13 | 31/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.800×** | -7.2 | 5e-11 | 28/48 (HepG2/C3A, LoVo, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.812×** | -6.8 | 1e-09 | 24/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.821×** | -6.4 | 1e-08 | 25/48 (A498, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.838× | -5.7 | 7e-07 | 20/48 (RKO, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.892× | -5.2 | 1e-05 | 13/48 (A498, Hs 766T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.893× | -5.2 | 1e-05 | 18/48 (HepG2/C3A, AsPC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -4.6 | 2e-04 | 14/48 (SW480, HepG2/C3A, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.878× | -4.2 | 0.001 | 15/47 (SNU-423, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.842× | -4.0 | 0.003 | 13/48 (SNU-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | 0.885× | -3.9 | 0.003 | 20/48 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.885× | -3.9 | 0.003 | 12/48 (LoVo, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.906× | -3.0 | 0.067 | 12/47 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 0.880× | -3.0 | 0.067 | 9/48 (SNU-423, NCI-H2347, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Lumateperone (tosylate) (drug)]] 0.05 µM |  | 0.913× | -3.0 | 0.067 | 3/49 (J82, Hs 766T, …) | inconsistent across doses |  |
| [[Sodium Salicylate (drug)]] 0.5 µM |  | 0.914× | -2.9 | 0.072 | 2/48 (KATO III, MIA PaCa-2) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 103 | 3 (3 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.24× (z +13.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.516× (z -11.5) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A-427 (line)]] | wt | 69.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.36× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -12.5) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A549 (line)]] | wt | 44.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.04× (z +14.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 191 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[HOP62 (line)]] | alt | 55.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +14.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 91.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.88× (z +9.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.558× (z -9.1) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H1573 (line)]] | alt | 29.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +15.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 78.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +10.2) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.495× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.488× (z -8.8) |
| [[PANC-1 (line)]] | alt | 68.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +14.4) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.603× (z -8.7) |
| [[SNU-423 (line)]] | alt | 45.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.29× (z +8.6) | — |
| [[A498 (line)]] | wt | 96.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +10.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 53.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 81.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.86× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 89.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.622× (z -8.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[LS 180 (line)]] | wt | 73.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 72.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +13.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 47.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.25× (z +9.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 55.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.81× (z +9.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -14.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SW 1088 (line)]] | alt | 73.5 | 0 | 2 | — | [[Belinostat (drug)]] 0.05 µM 0.0581× (z -10.1) |
| [[A-172 (line)]] | wt | 44.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +10.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 76.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -10.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 51.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.426× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 53.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -11.5) ⚠ cell-cycle shift, explains ~21% of this change |
| [[HT-29 (line)]] | alt | 67.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +12.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 60.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.06× (z +9.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 63.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 44.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.45× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 84.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.78× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 64.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -10.0) ⚠ cell-cycle shift, explains ~6% of this change |
| [[SW1417 (line)]] | alt | 77.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +9.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 110 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 77.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 91.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 71.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L4]] | +0.63 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[ZNF587B]] | +0.61 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[TXNDC5]] | +0.60 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[MANEA]] | +0.57 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[CPSF6]] | +0.57 | +0.36 / +0.68 | both halves | 1e-04 |  |
| [[DANCR]] | +0.56 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[TSN]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[CARNMT1]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[RPN1]] | +0.54 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[SPIN3]] | +0.54 | +0.28 / +0.59 | both halves | 3e-04 |  |
| [[TMEM64]] | +0.53 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[FUT10]] | +0.53 | +0.29 / +0.56 | both halves | 3e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLD4]] | -0.63 | -0.43 / -0.69 | both halves | 4e-05 |  |
| [[H3-3B]] | -0.58 | -0.36 / -0.67 | both halves | 1e-04 |  |
| [[PLEKHN1]] | -0.56 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[IRF7]] | -0.54 | -0.40 / -0.58 | both halves | 4e-05 |  |
| [[LENG1]] | -0.52 | -0.34 / -0.61 | both halves | 1e-04 |  |
| [[ISG20]] | -0.50 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[CATSPER2]] | -0.50 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[ING2]] | -0.50 | -0.26 / -0.55 | both halves | 4e-04 |  |
| [[ZNF324]] | -0.50 | -0.29 / -0.52 | both halves | 3e-04 |  |
| [[TBCC]] | -0.50 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[ARRDC2]] | -0.50 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[PPP1R35]] ⚠ | -0.49 | -0.33 / -0.56 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[EGLN2]] | -0.49 | -0.31 / -0.57 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.513). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.8, -19.9); signed map (-22.9, -43.7). **Vector** length 105, 24.5% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +7.8 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.5 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +19.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.4 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +20.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.1 | +2.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +3.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -4.0 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -7.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.3 — chr2:151,788,984-151,828,492 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ARL5 |
| Gene groups (HGNC) | ARF GTPase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y689](https://www.uniprot.org/uniprotkb/Q9Y689) (ADP-ribosylation factor-like protein 5A):

> Lacks ADP-ribosylation enhancing activity.

**Summary**, from NCBI Gene [26225](https://www.ncbi.nlm.nih.gov/gene/26225):

> The protein encoded by this gene belongs to the ARF family of GTP-binding proteins. With its distinctive nuclear/nucleolar localization and interaction with HP1alpha, the protein is developmentally regulated and may play a role(s) in nuclear dynamics and/or signaling cascades during embryonic development. Alternative splicing results in multiple transcript variants encoding different isoforms. This gene has multiple pseudogenes. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:696) · Entrez [26225](https://www.ncbi.nlm.nih.gov/gene/26225) · UniProt [Q9Y689](https://www.uniprot.org/uniprotkb/Q9Y689) · Ensembl [ENSG00000162980](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162980)

## Data

Gene col 8610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8610); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8610]; `tensor/DDL_lfc|DDL_z.npy` [8610]; `embed/gene_vectors.npy` [8610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8610 or target_col == 8610). Every well: [[ARL5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
