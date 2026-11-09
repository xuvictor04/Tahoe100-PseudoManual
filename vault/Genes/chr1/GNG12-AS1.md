---
symbol: "GNG12-AS1"
type: "gene"
col: 13842
ensembl_id: "ENSG00000232284"
name: "GNG12, DIRAS3 and WLS antisense RNA 1"
location: "1p31.3"
module: 85
arm: "-"
pooled_cpm: 26.78
n_lines_expressing: 47
n_dd_up: 13
n_dd_down: 36
n_dd_up_clean: 8
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# GNG12-AS1

*GNG12, DIRAS3 and WLS antisense RNA 1* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.70× (z +19.8, q 0e+00, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.340× (z -15.2, q 0e+00, down in 45 of 45 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDSR]] (+0.69, fdr 9e-06), [[CDK6-AS1]] (+0.67, fdr 2e-05), [[PHC2-AS1]] (+0.65, fdr 1e-05); moves opposite to [[PEDS1]] (-0.67, fdr 4e-05), [[TMEM9]] (-0.64, fdr 2e-05), [[YIF1B]] (-0.63, fdr 3e-04).
> It sits in the **-** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[WDR27]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13842.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +19.8 | 0e+00 | 41/43 (HS-578T, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +9.8 | 2e-20 | 31/43 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +8.4 | 1e-14 | 33/44 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +8.3 | 1e-14 | 32/45 (HS-578T, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.24×** | +4.2 | 0.003 | 19/45 (C32, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.35×** | +4.0 | 0.007 | 14/45 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.025 | 14/45 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.59×** | +3.4 | 0.042 | 15/45 (PANC-1, C32, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.40×** | +3.4 | 0.042 | 8/45 (C32, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.26×** | +3.3 | 0.060 | 10/44 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.26×** | +3.2 | 0.067 | 13/45 (PANC-1, C32, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.085 | 13/44 (HS-578T, A498, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.085 | 12/44 (A498, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.17× | +3.1 | 0.086 | 14/45 (H4, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13842.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.340×** | -15.2 | 0e+00 | 45/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.345×** | -15.0 | 0e+00 | 44/45 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.405×** | -12.7 | 7e-35 | 39/45 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.503×** | -9.7 | 5e-20 | 32/45 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.523×** | -9.1 | 8e-18 | 34/45 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.541×** | -8.6 | 5e-16 | 26/43 (H4, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.590×** | -7.1 | 8e-11 | 25/44 (A-427, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.631×** | -6.5 | 6e-09 | 24/45 (PANC-1, SW480, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.445×** | -6.0 | 2e-07 | 25/41 (C32, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.657×** | -5.9 | 2e-07 | 28/44 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.458×** | -5.7 | 5e-07 | 25/42 (RKO, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.467×** | -5.6 | 1e-06 | 28/45 (A-427, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.488×** | -5.3 | 5e-06 | 25/45 (A498, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -5.2 | 1e-05 | 27/45 (SW48, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.700×** | -5.0 | 2e-05 | 22/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.625×** | -4.7 | 8e-05 | 20/45 (RKO, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.786×** | -4.5 | 2e-04 | 19/45 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.728×** | -4.5 | 2e-04 | 23/45 (AN3 CA, A-172, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.774×** | -4.5 | 2e-04 | 22/45 (SK-MEL-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.739×** | -4.1 | 0.001 | 21/44 (C32, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13842. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 32.3 | 1 | 13 (9 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +12.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -16.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.229× (z -12.4) |
| [[H4 (line)]] | wt | 70.3 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0579× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.159× (z -10.9) |
| [[SW480 (line)]] | alt | 35.7 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.210× (z -13.6) |
| [[HS-578T (line)]] | alt | 26.2 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +14.3) | — |
| [[J82 (line)]] | alt | 30.5 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -10.9) |
| [[RKO (line)]] | wt | 36.5 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.150× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 24.9 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +11.5) | [[Belinostat (drug)]] 5 µM 0.230× (z -11.1) |
| [[HOP62 (line)]] | alt | 27.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +11.6) | — |
| [[NCI-H2030 (line)]] | alt | 28.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.175× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 19.9 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.156× (z -11.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 41.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 33.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -9.7) |
| [[COLO 205 (line)]] | alt | 34.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -11.4) |
| [[HT-29 (line)]] | alt | 37.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.121× (z -13.4) |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.109× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 20.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +24.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 25.4 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.606× (z -9.9) ⚠ position not correctable |
| [[SNU-1 (line)]] | wt | 9.04 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM 0.0768× (z -8.8) |
| [[SNU-423 (line)]] | alt | 34.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -9.8) |
| [[SW48 (line)]] | wt | 30.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.158× (z -9.0) |
| [[A-172 (line)]] | wt | 49.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -8.9) |
| [[A549 (line)]] | wt | 32.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 83.7 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.72× (z +9.4) ⚠ cell-cycle shift, explains ~80% of this change | — |
| [[HEC-1-A (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 18.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +12.7) | — |
| [[KATO III (line)]] | alt | 16.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -8.6) |
| [[LoVo (line)]] | wt | 24.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 26.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 23.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 42.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AN3 CA (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.61 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.20 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13842), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDSR]] | +0.69 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[CDK6-AS1]] | +0.67 | +0.60 / +0.48 | both halves | 2e-05 | same gene group |
| [[PHC2-AS1]] | +0.65 | +0.49 / +0.54 | both halves | 1e-05 | same gene group |
| [[MSANTD2]] | +0.63 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[DGKH]] | +0.63 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[MOSMO]] | +0.63 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[GABPB1-AS1]] | +0.62 | +0.55 / +0.43 | both halves | 3e-05 | same gene group |
| [[PCBP1-AS1]] | +0.62 | +0.52 / +0.35 | both halves | 1e-04 | same gene group |
| [[PTPRG]] | +0.62 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[E2F3]] | +0.61 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ZNF341-AS1]] | +0.60 | +0.50 / +0.35 | both halves | 1e-04 | same gene group |
| [[LENG8-AS1]] | +0.60 | +0.40 / +0.53 | both halves | 5e-05 | same gene group |

## Genes that move opposite

*40 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEDS1]] | -0.67 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[TMEM9]] | -0.64 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[YIF1B]] | -0.63 | -0.55 / -0.27 | both halves | 3e-04 |  |
| [[NAA40]] | -0.61 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[PKIG]] | -0.61 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SNTA1]] | -0.61 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[CDON]] | -0.61 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ARL6]] | -0.60 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[ROGDI]] | -0.60 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[RAB3A]] | -0.60 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[ALAD]] | -0.60 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[PAFAH1B3]] | -0.60 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GNG12-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[COL27A1]] | B | COL27A1 activity raises GNG12-AS1's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without COL27A1 | 0.023 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[LINC01829]] | C | LINC01829 activity raises GNG12-AS1's level | lines that do not express LINC01829 (3) vs lines expressing it (47) | 2.64× lower at baseline in the lines without LINC01829 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PARP11, GNG12-AS1, LINC02763; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR27]] | C | GNG12-AS1 activity raises WDR27's level | lines that do not express GNG12-AS1 (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without GNG12-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GALNT7, PARP11, DPP7; maybe low, not absent; its own permutation p |
| [[ZEB1-AS1]] | C | GNG12-AS1 activity raises ZEB1-AS1's level | lines that do not express GNG12-AS1 (3) vs lines expressing it (47) | 1.78× lower at baseline in the lines without GNG12-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GALNT7, PARP11, DPP7; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **-** arm (projection on the module's main direction -0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (6.3, -2.0); signed map (18.4, -5.4). **Vector** length 113, 30.7% of its response variance represented; |z| ≥ 3 in 1,352 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +14.4 | +19.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +9.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.8 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | +3.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.4 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -0.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -8.1 | -15.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.7 | -15.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.4 | -12.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.4 | -4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.3 | -6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.3 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.2 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.1 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | GNG12, DIRAS3 and WLS antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p31.3 — chr1:67,832,293-68,202,987 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43938](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43938) · Entrez [100289178](https://www.ncbi.nlm.nih.gov/gene/100289178) · Ensembl [ENSG00000232284](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232284)

## Data

Gene col 13842: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13842); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13842, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13842]; `tensor/DDL_lfc|DDL_z.npy` [13842]; `embed/gene_vectors.npy` [13842]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13842 or target_col == 13842). Every well: [[GNG12-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNG12-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
