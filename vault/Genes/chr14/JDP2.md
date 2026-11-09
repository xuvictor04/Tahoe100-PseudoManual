---
symbol: "JDP2"
type: "gene"
col: 6371
ensembl_id: "ENSG00000140044"
name: "Jun dimerization protein 2"
location: "14q24.3"
module: 63
arm: "+"
pooled_cpm: 15.54
n_lines_expressing: 38
n_dd_up: 57
n_dd_down: 27
n_dd_up_clean: 49
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# JDP2

*Jun dimerization protein 2* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 57 drug-doses (8 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 2.54× (z +13.3, q 1e-37, up in 25 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.267× (z -18.9, q 0e+00, down in 28 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSAT1]] (+0.76, fdr 7e-06), [[YARS1]] (+0.75, fdr 7e-06), [[MARS1]] (+0.73, fdr 7e-06); moves opposite to [[VEGFC]] (-0.49, fdr 3e-05), [[CD59]] (-0.48, fdr 3e-05), [[RAI14]] (-0.48, fdr 5e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ESRP1]] → it (grade B ⚠); 4 go from it, the strongest it → [[COBLL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 57 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6371.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **2.54×** | +13.3 | 1e-37 | 25/35 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.01×** | +9.9 | 8e-21 | 24/34 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.55×** | +8.9 | 1e-16 | 25/36 (Panc 03.27, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.70×** | +7.6 | 6e-12 | 17/35 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.69×** | +7.2 | 8e-11 | 19/34 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.57×** | +6.7 | 3e-09 | 16/35 (NCI-H2347, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.39×** | +6.5 | 8e-09 | 16/35 (LoVo, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.44×** | +6.3 | 1e-08 | 17/35 (NCI-H2347, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | **1.56×** | +6.3 | 1e-08 | 13/35 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.37×** | +6.3 | 1e-08 | 17/35 (HEC-1-A, LS 180, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.40×** | +5.8 | 3e-07 | 16/35 (NCI-H2347, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.51×** | +5.6 | 1e-06 | 15/33 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.32×** | +5.5 | 2e-06 | 14/35 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.46×** | +5.3 | 4e-06 | 12/35 (A549, HS-578T, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.1 | 1e-05 | 13/31 (hTERT-HPNE, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.27×** | +4.9 | 4e-05 | 12/36 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Neratinib (drug)]] 0.5 µM |  | **1.40×** | +4.8 | 7e-05 | 7/35 (Panc 03.27, BT-474, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +4.7 | 7e-05 | 15/34 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.39×** | +4.6 | 1e-04 | 15/35 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6371.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.267×** | -18.9 | 0e+00 | 28/35 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.418×** | -17.7 | 0e+00 | 28/34 (LoVo, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.292×** | -17.0 | 0e+00 | 31/34 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.343×** | -15.4 | 0e+00 | 28/35 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.351×** | -15.1 | 0e+00 | 28/34 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.368×** | -14.4 | 1e-44 | 29/35 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.485×** | -10.4 | 2e-23 | 24/35 (LoVo, KATO III, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.613×** | -10.0 | 1e-21 | 24/35 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.500×** | -10.0 | 1e-21 | 22/34 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.518×** | -9.1 | 5e-18 | 26/35 (HT-29, SW1417, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.532×** | -9.1 | 5e-18 | 21/33 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.545×** | -8.7 | 1e-16 | 21/35 (SW48, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.609×** | -7.1 | 4e-11 | 19/35 (SW1417, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.617×** | -7.0 | 1e-10 | 21/35 (LoVo, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.638×** | -6.5 | 3e-09 | 20/34 (SW48, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.659×** | -6.0 | 6e-08 | 21/32 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.671×** | -5.8 | 3e-07 | 22/34 (SW1417, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.759×** | -5.6 | 5e-07 | 19/34 (HT-29, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.684×** | -5.1 | 1e-05 | 16/32 (NCI-H2347, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.752×** | -4.1 | 1e-03 | 12/35 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.835× | -3.7 | 0.005 | 14/36 (SW1417, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.778×** | -3.6 | 0.006 | 15/34 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.793×** | -3.4 | 0.017 | 7/35 (HS-578T, KATO III, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6371. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 63.0 | 0 | 22 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0727× (z -30.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0254× (z -28.9) |
| [[SW1417 (line)]] | alt | 36.7 | 0 | 19 (11 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0406× (z -23.8) ⚠ toxic; cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0874× (z -18.8) |
| [[HT-29 (line)]] | alt | 38.1 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0688× (z -25.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0215× (z -25.0) |
| [[SW48 (line)]] | wt | 54.0 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0679× (z -20.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0636× (z -14.9) |
| [[KATO III (line)]] | alt | 50.6 | 0 | 16 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0749× (z -20.6) |
| [[LS 180 (line)]] | wt | 42.0 | 0 | 11 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0723× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0856× (z -16.3) |
| [[PANC-1 (line)]] | alt | 16.3 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0710× (z -24.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0771× (z -16.1) |
| [[SW480 (line)]] | alt | 16.1 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0990× (z -16.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.125× (z -14.4) |
| [[RKO (line)]] | wt | 16.2 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0523× (z -13.4) |
| [[A-427 (line)]] | wt | 21.4 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -9.4) |
| [[A-172 (line)]] | wt | 6.15 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0309× (z -13.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.0806× (z -10.0) |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0333× (z -12.9) |
| [[H4 (line)]] | wt | 17.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0966× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 34.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 21.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -13.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.232× (z -9.3) |
| [[A498 (line)]] | wt | 8.05 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0728× (z -19.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 7.61 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 17.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0781× (z -10.4) |
| [[HS-578T (line)]] | alt | 7.97 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -9.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 15.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -10.4) |
| [[A549 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6371), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSAT1]] | +0.76 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[YARS1]] | +0.75 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[MARS1]] | +0.73 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[PHGDH]] | +0.73 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[TARS1]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[SLC7A1]] | +0.71 | +0.66 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A9]] | +0.70 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[ASNS]] | +0.70 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[AARS1]] | +0.69 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[IARS1]] | +0.69 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[LINC01133]] | +0.69 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[CHAC1]] | +0.67 | +0.68 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEGFC]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[CD59]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[RAI14]] | -0.48 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[SMAD3]] | -0.47 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[LOXL2]] | -0.47 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[LUCAT1]] | -0.47 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[PDLIM7]] | -0.45 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[WWTR1]] | -0.45 | -0.39 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESRP1]] | B | ESRP1 activity raises JDP2's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 2.92× lower at baseline in the lines without ESRP1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[LINC02331]] | B | LINC02331 activity raises JDP2's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 2.64× lower at baseline in the lines without LINC02331 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[C6orf132]] | B | C6orf132 activity raises JDP2's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 2.85× lower at baseline in the lines without C6orf132 | 0.072 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[GPRIN2]] | B | GPRIN2 activity raises JDP2's level | lines that do not express GPRIN2 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without GPRIN2 | 0.075 | ⚠ within organs, on part of the lines; also absent: MUC16, KRT6A, ACP7 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COBLL1]] | B | JDP2 activity raises COBLL1's level | lines that do not express JDP2 (12) vs lines expressing it (38) | 2.23× lower at baseline in the lines without JDP2 | 0.024 | ⚠ within organs, on part of the lines; also absent: JUP, LINC01836, SEL1L3; maybe low, not absent |
| [[C6orf132]] | B | JDP2 activity raises C6orf132's level | lines that do not express JDP2 (12) vs lines expressing it (38) | 5.40× lower at baseline in the lines without JDP2 | 0.063 | ⚠ within organs, on part of the lines; also absent: JUP, LINC01836, SEL1L3; maybe low, not absent |
| [[PLEKHA7]] | B | JDP2 activity raises PLEKHA7's level | lines that do not express JDP2 (12) vs lines expressing it (38) | 2.51× lower at baseline in the lines without JDP2 | 0.087 | ⚠ within organs, on part of the lines; also absent: JUP, LINC01836, SEL1L3; maybe low, not absent |
| [[SLC7A11]] | B | JDP2 activity raises SLC7A11's level | lines that do not express JDP2 (12) vs lines expressing it (38) | 2.13× lower at baseline in the lines without JDP2 | 0.097 | ⚠ within organs, on part of the lines; also absent: JUP, LINC01836, SEL1L3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.8, 47.3); signed map (-13.5, 23.6). **Vector** length 115, 32.7% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.55 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.65 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.65 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.0 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.6 | +13.3 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +4.1 | +9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +7.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.5 | +8.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.2 | +3.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -15.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -17.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -5.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[4EGI-1 (drug)]] 5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | Jun dimerization protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:75,427,716-75,474,111 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously JUNDM2 |
| Gene groups (HGNC) | Activating transcription factor 3 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYK2](https://www.uniprot.org/uniprotkb/Q8WYK2) (Jun dimerization protein 2):

> Component of the AP-1 transcription factor that represses transactivation mediated by the Jun family of proteins. Involved in a variety of transcriptional responses associated with AP-1 such as UV-induced apoptosis, cell differentiation, tumorigenesis and antitumogeneris. Can also function as a repressor by recruiting histone deacetylase 3/HDAC3 to the promoter region of JUN. May control transcription via direct regulation of the modification of histones and the assembly of chromatin.

**Summary**, from NCBI Gene [122953](https://www.ncbi.nlm.nih.gov/gene/122953):

> Enables DNA-binding transcription repressor activity, RNA polymerase II-specific and sequence-specific double-stranded DNA binding activity. Involved in negative regulation of transcription by RNA polymerase II. Located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17546](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17546) · Entrez [122953](https://www.ncbi.nlm.nih.gov/gene/122953) · UniProt [Q8WYK2](https://www.uniprot.org/uniprotkb/Q8WYK2) · Ensembl [ENSG00000140044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140044)

## Data

Gene col 6371: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6371); `tables/drug_effects.parquet` (91 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6371, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6371]; `tensor/DDL_lfc|DDL_z.npy` [6371]; `embed/gene_vectors.npy` [6371]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6371 or target_col == 6371). Every well: [[JDP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JDP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
