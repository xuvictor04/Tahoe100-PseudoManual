---
symbol: "STRBP"
type: "gene"
col: 9087
ensembl_id: "ENSG00000165209"
name: "spermatid perinuclear RNA binding protein"
location: "9q33.3"
module: 115
arm: "+"
pooled_cpm: 112.56
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# STRBP

*spermatid perinuclear RNA binding protein* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.42× (z +28.9, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.796× (z -7.5, q 3e-11, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRACD]] (+0.64, fdr 1e-05), [[ARHGAP44]] (+0.60, fdr 4e-05), [[ATP8A1]] (+0.59, fdr 9e-05); moves opposite to [[ZNF543]] (-0.60, fdr 2e-04), [[C1S]] (-0.55, fdr 6e-05), [[VCPIP1]] (-0.55, fdr 4e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ARHGAP44]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.42×** | +28.9 | 0e+00 | 47/47 (J82, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.37×** | +28.2 | 0e+00 | 45/47 (A-172, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.28×** | +26.9 | 0e+00 | 47/47 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +18.8 | 0e+00 | 42/47 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +17.4 | 0e+00 | 39/47 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +15.2 | 0e+00 | 41/47 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +14.2 | 7e-44 | 29/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.11×** | +12.8 | 2e-35 | 43/48 (HEC-1-A, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.44×** | +12.0 | 2e-31 | 30/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +10.4 | 1e-23 | 34/48 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.36×** | +9.6 | 5e-20 | 36/46 (NCI-H460, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.24×** | +7.0 | 1e-10 | 19/47 (KATO III, HepG2/C3A, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +7.0 | 1e-10 | 27/47 (J82, RKO, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.16× | +6.8 | 4e-10 | 24/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.24×** | +6.7 | 6e-10 | 24/43 (NCI-H23, C32, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +5.3 | 4e-06 | 16/47 (C32, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.25×** | +5.2 | 7e-06 | 18/49 (RKO, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +5.1 | 1e-05 | 19/47 (A-427, A-172, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.31×** | +4.6 | 1e-04 | 11/47 (J82, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 1.14× | +4.3 | 4e-04 | 13/47 (RKO, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.14× | +4.2 | 7e-04 | 16/48 (C32, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9087.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.796×** | -7.5 | 3e-11 | 28/47 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.746×** | -5.0 | 1e-04 | 16/48 (MIA PaCa-2, AN3 CA, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.747×** | -5.0 | 1e-04 | 21/48 (NCI-H23, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.750×** | -4.9 | 1e-04 | 18/47 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.865× | -4.6 | 5e-04 | 12/46 (J82, RPMI-7951, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.880× | -4.2 | 0.002 | 13/46 (RKO, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.883× | -3.8 | 0.012 | 11/46 (LoVo, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.897× | -3.6 | 0.023 | 11/47 (PANC-1, SW48, …) | inconsistent across doses |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.931× | -3.4 | 0.049 | 0/47 | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.905× | -3.2 | 0.081 | 5/47 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.936× | -3.1 | 0.096 | 6/47 (NCI-H2347, SW 1271, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.912× | -3.0 | 0.11 | 10/46 (SW480, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 93.2 | 7 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.52× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[NCI-H460 (line)]] | wt | 69.8 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +16.8) | — |
| [[A498 (line)]] | wt | 34.5 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.20× (z +15.3) | — |
| [[HOP62 (line)]] | alt | 44.8 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.18× (z +13.8) | — |
| [[LS 180 (line)]] | wt | 187 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +14.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 195 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +14.0) | [[Dinaciclib (drug)]] 0.05 µM 0.476× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[A-172 (line)]] | wt | 41.5 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.20× (z +14.6) | — |
| [[J82 (line)]] | alt | 119 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +15.9) | — |
| [[KATO III (line)]] | alt | 161 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +13.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.23× (z +12.6) | — |
| [[LoVo (line)]] | wt | 174 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +15.2) | [[Harringtonine (drug)]] 0.5 µM 0.631× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 34.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +13.8) | — |
| [[NCI-H2347 (line)]] | alt | 109 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -9.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[PANC-1 (line)]] | alt | 138 | 4 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.66× (z +11.1) | [[Harringtonine (drug)]] 0.5 µM 0.624× (z -10.3) |
| [[SNU-423 (line)]] | alt | 41.1 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +11.6) | — |
| [[A549 (line)]] | wt | 93.8 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.26× (z +9.6) | — |
| [[H4 (line)]] | wt | 37.2 | 5 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 6.28× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 233 | 5 | 0 | [[Belinostat (drug)]] 5 µM 1.98× (z +13.7) | — |
| [[Hs 766T (line)]] | wt | 55.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.95× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 179 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +15.5) | — |
| [[LOX-IMVI (line)]] | wt | 77.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +14.6) | — |
| [[Panc 03.27 (line)]] | alt | 108 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +13.9) | — |
| [[SW 900 (line)]] | alt | 38.9 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +11.7) | — |
| [[C32 (line)]] | wt | 36.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.65× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 34.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 126 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +14.0) | — |
| [[RKO (line)]] | wt | 224 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +10.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.486× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~62% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.587× (z -8.6) |
| [[SW480 (line)]] | alt | 163 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.77× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 280 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 1.90× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 255 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[HCT15 (line)]] | alt | 164 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.51× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 30.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.64× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 130 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 47.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.53× (z +9.9) | — |
| [[SW48 (line)]] | wt | 153 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.443× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 117 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.80× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.447× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -29.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[HS-578T (line)]] | alt | 46.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.08× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 146 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | — |
| [[RPMI-7951 (line)]] | alt | 51.9 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.03× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 236 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.71× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.446× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[SW 1271 (line)]] | alt | 211 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0586× (z -19.2) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 224 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRACD]] | +0.64 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ARHGAP44]] | +0.60 | +0.43 / +0.68 | both halves | 4e-05 |  |
| [[ATP8A1]] | +0.59 | +0.36 / +0.65 | both halves | 9e-05 |  |
| [[LINC00937]] | +0.59 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[RALGPS1]] | +0.58 | +0.32 / +0.65 | both halves | 2e-04 |  |
| [[ZDHHC20]] | +0.58 | +0.43 / +0.49 | both halves | 4e-05 |  |
| [[DNMT3B]] | +0.58 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[SCML2]] | +0.57 | +0.37 / +0.58 | both halves | 9e-05 |  |
| [[OTUD7A]] | +0.56 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[ARHGEF26]] | +0.55 | +0.40 / +0.67 | both halves | 5e-05 |  |
| [[SBK1]] | +0.55 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[NOS1AP]] | +0.55 | +0.36 / +0.60 | both halves | 1e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF543]] | -0.60 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[C1S]] | -0.55 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[VCPIP1]] | -0.55 | -0.26 / -0.55 | both halves | 4e-04 |  |
| [[SMG8]] | -0.54 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[MTERF1]] | -0.53 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[ATXN1L]] | -0.53 | -0.19 / -0.55 | ⚠ one half (not replicated) | 9e-04 |  |
| [[ZNF304]] | -0.53 | -0.19 / -0.50 | ⚠ not reproduced | 8e-04 |  |
| [[CBLL1]] | -0.52 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[SNIP1]] | -0.51 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[UBE3B]] | -0.51 | -0.14 / -0.47 | ⚠ not reproduced | 0.002 |  |
| [[ZBTB6]] | -0.51 | -0.24 / -0.44 | both halves | 5e-04 |  |
| [[ZNF646]] | -0.50 | -0.18 / -0.43 | ⚠ not reproduced | 9e-04 |  |
| [[WDR13]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[VPS39]] | -0.48 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[CFLAR]] | -0.48 | -0.20 / -0.51 | both halves | 7e-04 |  |
| [[ZNF621]] | -0.48 | -0.26 / -0.41 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP44]] | B | ARHGAP44 activity raises STRBP's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.72× lower at baseline in the lines without ARHGAP44 | 0.047 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[LMX1B]] | B | LMX1B activity raises STRBP's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.29× lower at baseline in the lines without LMX1B | 0.049 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[TSPAN33]] | B | TSPAN33 activity raises STRBP's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.95× lower at baseline in the lines without TSPAN33 | 0.068 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[LRRC20]] | B | LRRC20 activity raises STRBP's level | lines that do not express LRRC20 (5) vs lines expressing it (45) | 2.69× lower at baseline in the lines without LRRC20 | 0.069 | ⚠ within organs, on part of the lines; also absent: MCM2, MCM10, SEMA4D; maybe low, not absent |
| [[SBK1]] | B | SBK1 activity raises STRBP's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without SBK1 | 0.077 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[BMP7]] | B | BMP7 activity weakens STRBP's drug response | lines that do not express BMP7 (23) vs lines expressing it (25) | the lines without BMP7 respond 1.35× as strongly (z diff -1.28); strongest at Homoharringtonine 5 µM: 1.52x vs 1.35x (z diff -2.3) | 0.081 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.4, 37.8); signed map (-22.2, 37.9). **Vector** length 99.7, 27.5% of its response variance represented; |z| ≥ 3 in 1,269 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +17.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.1 | +18.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +10.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.4 | +12.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.9 | +15.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +3.2 | +5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +4.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.6 | -7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.1 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | spermatid perinuclear RNA binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:123,109,500-123,268,586 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11307, SPNR; previously ILF3L |
| Hallmark sets | SPERMATOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SI9](https://www.uniprot.org/uniprotkb/Q96SI9) (Spermatid perinuclear RNA-binding protein):

> Involved in spermatogenesis and sperm function. Plays a role in regulation of cell growth. Binds to double-stranded DNA and RNA. Binds most efficiently to poly(I:C) RNA than to poly(dI:dC) DNA. Binds also to single-stranded poly(G) RNA. Binds non-specifically to the mRNA PRM1 3'-UTR and adenovirus VA RNA (By similarity).

**Summary**, from NCBI Gene [55342](https://www.ncbi.nlm.nih.gov/gene/55342):

> Enables RNA binding activity. Predicted to be involved in cell differentiation and spermatogenesis. Predicted to act upstream of or within cell motility; mechanosensory behavior; and spermatid development. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16462](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16462) · Entrez [55342](https://www.ncbi.nlm.nih.gov/gene/55342) · UniProt [Q96SI9](https://www.uniprot.org/uniprotkb/Q96SI9) · Ensembl [ENSG00000165209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165209)

## Data

Gene col 9087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9087); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9087]; `tensor/DDL_lfc|DDL_z.npy` [9087]; `embed/gene_vectors.npy` [9087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9087 or target_col == 9087). Every well: [[STRBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STRBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
