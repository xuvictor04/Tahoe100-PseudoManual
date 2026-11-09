---
symbol: "DDR2"
type: "gene"
col: 8571
ensembl_id: "ENSG00000162733"
name: "discoidin domain receptor tyrosine kinase 2"
location: "1q23.3"
module: 53
arm: "+"
pooled_cpm: 39.2
n_lines_expressing: 41
n_dd_up: 33
n_dd_down: 8
n_dd_up_clean: 26
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 19
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# DDR2

*discoidin domain receptor tyrosine kinase 2* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.27× (z +36.2, q 0e+00, up in 34 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.682× (z -6.8, q 4e-09, down in 22 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCF2]] (+0.66, fdr 1e-05), [[C1S]] (+0.66, fdr 1e-05), [[ST8SIA5]] (+0.65, fdr 3e-05); moves opposite to [[COPG2]] (-0.56, fdr 1e-04), [[BTBD3]] (-0.56, fdr 5e-05), [[BRAT1]] (-0.56, fdr 5e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZNF382]] → it (grade B ⚠); 19 go from it, the strongest it → [[PLAC8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8571.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.27×** | +36.2 | 0e+00 | 34/39 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **6.05×** | +31.8 | 0e+00 | 37/39 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.38×** | +30.4 | 0e+00 | 26/39 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.86×** | +18.5 | 0e+00 | 32/39 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.59×** | +16.7 | 0e+00 | 29/39 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +13.7 | 2e-40 | 25/38 (HOP62, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.15×** | +13.5 | 1e-39 | 28/39 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.85×** | +10.8 | 2e-25 | 24/39 (HOP62, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +8.7 | 1e-16 | 12/28 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.46×** | +8.3 | 6e-15 | 23/40 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +8.2 | 1e-14 | 21/36 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +7.3 | 1e-11 | 19/39 (MIA PaCa-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.20×** | +7.3 | 2e-11 | 24/39 (A498, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.49×** | +6.6 | 2e-09 | 20/38 (C32, A-427, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +6.4 | 6e-09 | 21/39 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +6.3 | 1e-08 | 19/39 (NCI-H1792, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +5.6 | 5e-07 | 14/38 (HOP62, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.1 | 1e-05 | 17/40 (HEC-1-A, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8571.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.682×** | -6.8 | 4e-09 | 22/39 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.673×** | -6.8 | 4e-09 | 22/35 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.797×** | -5.7 | 2e-06 | 18/39 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.758×** | -4.9 | 1e-04 | 17/39 (hTERT-HPNE, HS-578T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.781×** | -4.4 | 0.001 | 18/39 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.653×** | -4.0 | 0.007 | 12/37 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Pimitespib (drug)]] 0.05 µM |  | **0.806×** | -3.6 | 0.023 | 7/39 (C-33 A, PANC-1, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.707×** | -3.2 | 0.088 | 9/39 (RKO, hTERT-HPNE, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.834× | -3.1 | 0.11 | 6/39 (A498, HT-29, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.834× | -3.1 | 0.13 | 6/38 (NCI-H23, BT-474, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8571. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 199 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.275× (z -10.5) |
| [[HOP62 (line)]] | alt | 18.7 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +24.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.258× (z -8.6) ⚠ toxic |
| [[LoVo (line)]] | wt | 22.4 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +28.3) | — |
| [[C32 (line)]] | wt | 129 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +24.2) | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -11.8) ⚠ cell-cycle shift, explains ~20% of this change |
| [[MIA PaCa-2 (line)]] | alt | 103 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.94× (z +25.0) | — |
| [[NCI-H460 (line)]] | wt | 14.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +23.7) | — |
| [[PANC-1 (line)]] | alt | 14.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +19.5) | — |
| [[RPMI-7951 (line)]] | alt | 237 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +17.3) | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -14.7) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SNU-1 (line)]] | wt | 16.5 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 17.4× (z +11.4) | — |
| [[A-172 (line)]] | wt | 265 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.67× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -16.3) ⚠ cell-cycle shift, explains ~20% of this change |
| [[A498 (line)]] | wt | 12.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +23.1) | — |
| [[HEC-1-A (line)]] | alt | 15.9 | 4 | 0 | [[Auranofin (drug)]] 5 µM 21.2× (z +18.9) | — |
| [[Hs 766T (line)]] | wt | 12.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.30× (z +14.0) | — |
| [[HS-578T (line)]] | alt | 183 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +17.0) | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -16.5) ⚠ cell-cycle shift, explains ~20% of this change |
| [[hTERT-HPNE (line)]] | wt | 302 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +15.7) | [[Panobinostat (drug)]] 5 µM 0.153× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 20.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +19.7) | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +22.7) | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.47× (z +11.9) | [[Resveratrol (drug)]] 0.05 µM 0.117× (z -9.0) |
| [[LS 180 (line)]] | wt | 12.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 7.91× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 98.4× (z +30.2) | — |
| [[RKO (line)]] | wt | 45.4 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.60× (z +9.4) | [[Selinexor (drug)]] 5 µM 0.249× (z -10.7) ⚠ cell-cycle shift, explains ~12% of this change |
| [[SNU-423 (line)]] | alt | 12.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +20.9) | — |
| [[SW 900 (line)]] | alt | 20.0 | 3 | 0 | [[Auranofin (drug)]] 5 µM 13.5× (z +12.4) | — |
| [[SW48 (line)]] | wt | 18.3 | 2 | 1 | [[Auranofin (drug)]] 5 µM 15.3× (z +11.7) | [[Bicalutamide (drug)]] 0.5 µM 0.137× (z -8.6) |
| [[AN3 CA (line)]] | alt | 129 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -9.0) ⚠ cell-cycle shift, explains ~20% of this change |
| [[HCT15 (line)]] | alt | 24.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 13.6× (z +11.7) | — |
| [[HT-29 (line)]] | alt | 11.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 23.8× (z +16.2) | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.81× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 56.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +13.2) | — |
| [[SW 1088 (line)]] | alt | 130 | 0 | 2 (1 ⚠) | — | [[Clotrimazole (drug)]] 0.5 µM 0.0517× (z -11.2) |
| [[A-427 (line)]] | wt | 23.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.0× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.38× (z +13.4) | — |
| [[BT-474 (line)]] | alt | 27.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +11.2) | — |
| [[CHP-212 (line)]] | wt | 178 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -8.8) ⚠ cell-cycle shift, explains ~20% of this change |
| [[J82 (line)]] | alt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 37.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.15× (z +14.5) | — |
| [[SW 1271 (line)]] | alt | 28.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +9.0) | — |
| [[A549 (line)]] | wt | 8.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.37 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.05 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.35 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.66 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.30 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.26 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8571), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCF2]] | +0.66 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[C1S]] | +0.66 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ST8SIA5]] | +0.65 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[ITGA9]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[SLC26A7]] | +0.64 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[ESRRB]] | +0.64 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[LINC00907]] | +0.64 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[LINC02955]] | +0.64 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[NUP210L]] | +0.64 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[NEB]] | +0.64 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[LINC01031]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[BAALC-AS1]] | +0.62 | +0.53 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPG2]] | -0.56 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[BTBD3]] | -0.56 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[BRAT1]] | -0.56 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[REPS1]] | -0.55 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[L2HGDH]] | -0.54 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[TERF1]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[KIF3A]] | -0.53 | -0.45 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF382]] | B | ZNF382 activity raises DDR2's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 2.95× lower at baseline in the lines without ZNF382 | 0.017 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[TEK]] | B | TEK activity raises DDR2's level | lines that do not express TEK (27) vs lines expressing it (23) | 2.93× lower at baseline in the lines without TEK | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent |
| [[PAPPA2]] | B | PAPPA2 activity raises DDR2's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without PAPPA2 | 0.047 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent |
| [[LINC02641]] | B | LINC02641 activity raises DDR2's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 2.08× lower at baseline in the lines without LINC02641 | 0.091 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises DDR2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAC8L1]] | B | DDR2 activity raises PLAC8L1's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without DDR2 | 0.009 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[PSMD6-AS1]] | B | DDR2 activity raises PSMD6-AS1's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without DDR2 | 0.015 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[GRK4]] | B | DDR2 activity raises GRK4's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without DDR2 | 0.017 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[FRZB]] | B | DDR2 activity raises FRZB's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 2.39× lower at baseline in the lines without DDR2 | 0.020 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[H2AZ1-DT]] | B | DDR2 activity raises H2AZ1-DT's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.49× lower at baseline in the lines without DDR2 | 0.047 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[ANKDD1B]] | B | DDR2 activity raises ANKDD1B's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.90× lower at baseline in the lines without DDR2 | 0.053 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[ITGA9]] | B | DDR2 activity raises ITGA9's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.76× lower at baseline in the lines without DDR2 | 0.058 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[MINAR1]] | B | DDR2 activity raises MINAR1's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.72× lower at baseline in the lines without DDR2 | 0.067 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[LINC00486]] | B | DDR2 activity raises LINC00486's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.30× lower at baseline in the lines without DDR2 | 0.068 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[PSMD7-DT]] | B | DDR2 activity raises PSMD7-DT's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.37× lower at baseline in the lines without DDR2 | 0.075 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[TG]] | B | DDR2 activity strengthens TG's drug response | lines that do not express DDR2 (8) vs lines expressing it (34) | the lines without DDR2 respond 0.66× as strongly (z diff +1.06); strongest at Homoharringtonine 5 µM: 3.01x vs 7.82x (z diff +3.2) | 0.076 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Balsalazide (sodium hydrate) (drug)]] 5 µM | B | DDR2 activity raises the cells' numbers under Balsalazide (sodium hydrate) 5 µM (protects the cells) | lines that do not express DDR2 (9) vs lines expressing it (39) | the lines without DDR2: 0.89× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.569). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.6, -9.2); signed map (21.8, 2.0). **Vector** length 100, 23.1% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +12.6 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.9 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +11.8 | +31.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.0 | +30.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.6 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.3 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +0.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | +2.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.1 | -6.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.9 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.0 | -4.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | discoidin domain receptor tyrosine kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:162,631,373-162,787,405 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TKT; previously TYRO10, NTRKR3 |
| Gene groups (HGNC) | Discoidin domain receptor tyrosine kinase family |
| Reactome | 2 pathways, smallest: Non-integrin membrane-ECM interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16832](https://www.uniprot.org/uniprotkb/Q16832) (Discoidin domain-containing receptor 2):

> Tyrosine kinase involved in the regulation of tissues remodeling. It functions as a cell surface receptor for fibrillar collagen and regulates cell differentiation, remodeling of the extracellular matrix, cell migration and cell proliferation. Required for normal bone development. Regulates osteoblast differentiation and chondrocyte maturation via a signaling pathway that involves MAP kinases and leads to the activation of the transcription factor RUNX2. Regulates remodeling of the …

**Summary**, from NCBI Gene [4921](https://www.ncbi.nlm.nih.gov/gene/4921):

> This gene encodes a member of the discoidin domain receptor subclass of the receptor tyrosine kinase (RTKs) protein family. RTKs play a key role in the communication of cells with their microenvironment. The encoded protein is a collagen-induced receptor that activates signal transduction pathways involved in cell adhesion, proliferation, and extracellular matrix remodeling. This protein is expressed in numerous cell types and may alos be involved in wound repair and regulate tumor growth and …

**Accessions** — [HGNC:2731](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2731) · Entrez [4921](https://www.ncbi.nlm.nih.gov/gene/4921) · UniProt [Q16832](https://www.uniprot.org/uniprotkb/Q16832) · Ensembl [ENSG00000162733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162733)

## Data

Gene col 8571: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8571); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8571, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8571]; `tensor/DDL_lfc|DDL_z.npy` [8571]; `embed/gene_vectors.npy` [8571]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8571 or target_col == 8571). Every well: [[DDR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
