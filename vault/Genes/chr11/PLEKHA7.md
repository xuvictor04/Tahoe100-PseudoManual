---
symbol: "PLEKHA7"
type: "gene"
col: 9344
ensembl_id: "ENSG00000166689"
name: "pleckstrin homology domain containing A7"
location: "11p15"
module: 106
arm: "+"
pooled_cpm: 76.59
n_lines_expressing: 42
n_dd_up: 6
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 38
direction_downstream: 4
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# PLEKHA7

*pleckstrin homology domain containing A7* — 11p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.37× (z +7.5, q 2e-11, up in 15 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 1.20× (z +4.4, q 0.001, up in 10 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.746× (z -6.7, q 1e-08, down in 18 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGPP2]] (+0.61, fdr 1e-05), [[EPS8]] (+0.58, fdr 1e-05), [[SHROOM3]] (+0.58, fdr 3e-05); moves opposite to [[VEGFC]] (-0.50, fdr 3e-05), [[BMPER]] (-0.49, fdr 6e-05), [[ZNF275]] (-0.44, fdr 5e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[SGPP2]] → it (grade B ⚠); 4 go from it, the strongest it → [[EPB41L4B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +7.5 | 2e-11 | 15/38 (NCI-H2030, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.20×** | +4.4 | 0.001 | 10/41 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +4.4 | 0.001 | 14/40 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +4.4 | 0.001 | 11/41 (J82, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.20×** | +4.4 | 0.001 | 17/39 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +4.3 | 0.001 | 9/40 (NCI-H2030, Hs 766T, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.19× | +4.1 | 0.004 | 13/38 (Hs 766T, A549, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.17× | +3.7 | 0.016 | 8/39 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.17× | +3.6 | 0.016 | 10/40 (HepG2/C3A, Hs 766T, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.6 | 0.016 | 14/40 (AsPC-1, SK-MEL-2, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.037 | 4/38 (J82, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.16× | +3.4 | 0.038 | 17/42 (AsPC-1, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.073 | 10/41 (J82, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.073 | 3/42 (NCI-H23, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.073 | 14/40 (J82, NCI-H2347, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.09× | +3.1 | 0.079 | 4/41 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.14× | +3.0 | 0.088 | 9/41 (AsPC-1, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.09× | +2.9 | 0.099 | 6/40 (A549, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9344.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.746×** | -6.7 | 1e-08 | 18/40 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.793×** | -5.5 | 1e-05 | 23/40 (HepG2/C3A, HT-29, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.813×** | -4.9 | 2e-04 | 17/40 (HepG2/C3A, LoVo, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.819×** | -4.7 | 3e-04 | 20/39 (LoVo, SW48, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.820×** | -4.7 | 3e-04 | 10/41 (A549, SW 1088, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.889× | -3.9 | 0.009 | 12/40 (NCI-H2347, A549, …) | top dose only | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.733×** | -3.9 | 0.009 | 16/37 (PANC-1, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Furosemide (drug)]] 5 µM |  | 0.893× | -3.8 | 0.012 | 7/40 (NCI-H661, COLO 205, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.894× | -3.7 | 0.013 | 18/40 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.850× | -3.7 | 0.013 | 12/40 (A549, NCI-H1792, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.857× | -3.6 | 0.014 | 11/39 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | 0.903× | -3.4 | 0.035 | 10/40 (LS 180, AN3 CA, …) | top dose only | position effect removed |
| [[Bestatin (drug)]] 5 µM |  | 0.868× | -3.2 | 0.055 | 3/39 (NCI-H2347, A-427, …) | top dose only |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 0.869× | -3.2 | 0.055 | 9/39 (C-33 A, CHP-212, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.876× | -3.1 | 0.070 | 15/40 (LoVo, A-427, …) | rises with dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.780×** | -3.1 | 0.074 | 8/40 (LoVo, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[AZD1390 (drug)]] 0.05 µM |  | 0.855× | -3.1 | 0.074 | 5/40 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 241 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.450× (z -8.9) |
| [[A549 (line)]] | wt | 139 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -27.4) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.286× (z -13.5) |
| [[HepG2_C3A (line)]] | wt | 216 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -13.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 163 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.396× (z -11.5) |
| [[PANC-1 (line)]] | alt | 63.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -14.4) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.483× (z -9.2) |
| [[SW48 (line)]] | wt | 223 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.362× (z -9.3) |
| [[A-427 (line)]] | wt | 53.4 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -11.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.488× (z -9.8) |
| [[AN3 CA (line)]] | alt | 138 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0666× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.281× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 86.3 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.278× (z -11.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.361× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 178 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -10.5) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -8.9) |
| [[COLO 205 (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -12.3) ⚠ cell-cycle shift, explains ~71% of this change |
| [[NCI-H2347 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.528× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 178 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.465× (z -9.1) |
| [[C-33 A (line)]] | alt | 90.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -12.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 79.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -13.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 57.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.3) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[SW 900 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -8.7) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SW480 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -11.8) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A-172 (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.8 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9344), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGPP2]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[EPS8]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SHROOM3]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[GAREM1]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[NEBL]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SCNN1A]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[C6orf132]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MTUS1]] | +0.56 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[SORL1]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PLEKHG6]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 | same gene group |
| [[TRIM29]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[AXIN2]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEGFC]] | -0.50 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[BMPER]] | -0.49 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[ZNF275]] | -0.44 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[DIRC3-AS1]] | -0.43 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[FRMD6]] | -0.43 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ANTXR2]] | -0.43 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[ADGRL1-AS1]] | -0.43 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[GPATCH2L]] | -0.42 | -0.40 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 38, C 0. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGPP2]] | B | SGPP2 activity raises PLEKHA7's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 3.30× lower at baseline in the lines without SGPP2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[MTUS1]] | B | MTUS1 activity raises PLEKHA7's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.74× lower at baseline in the lines without MTUS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[CLIC5]] | B | CLIC5 activity raises PLEKHA7's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.27× lower at baseline in the lines without CLIC5 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[TRIM29]] | B | TRIM29 activity raises PLEKHA7's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.79× lower at baseline in the lines without TRIM29 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[ST14]] | B | ST14 activity raises PLEKHA7's level | lines that do not express ST14 (32) vs lines expressing it (18) | 3.37× lower at baseline in the lines without ST14 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[HNF4A]] | B | HNF4A activity raises PLEKHA7's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 3.17× lower at baseline in the lines without HNF4A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[FOXQ1]] | B | FOXQ1 activity raises PLEKHA7's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 2.77× lower at baseline in the lines without FOXQ1 | 0.004 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[PROM1]] | B | PROM1 activity raises PLEKHA7's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 3.32× lower at baseline in the lines without PROM1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[TC2N]] | B | TC2N activity raises PLEKHA7's level | lines that do not express TC2N (28) vs lines expressing it (22) | 3.12× lower at baseline in the lines without TC2N | 0.005 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[TOX3]] | B | TOX3 activity raises PLEKHA7's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.80× lower at baseline in the lines without TOX3 | 0.005 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[TTC22]] | B | TTC22 activity raises PLEKHA7's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 3.20× lower at baseline in the lines without TTC22 | 0.005 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[LINC02331]] | B | LINC02331 activity raises PLEKHA7's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 3.30× lower at baseline in the lines without LINC02331 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L4B]] | B | PLEKHA7 activity raises EPB41L4B's level | lines that do not express PLEKHA7 (8) vs lines expressing it (42) | 2.53× lower at baseline in the lines without PLEKHA7 | 0.023 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GAREM1]] | B | PLEKHA7 activity raises GAREM1's level | lines that do not express PLEKHA7 (8) vs lines expressing it (42) | 3.14× lower at baseline in the lines without PLEKHA7 | 0.037 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PPA1]] | B | PLEKHA7 activity raises PPA1's level | lines that do not express PLEKHA7 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without PLEKHA7 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MTUS1]] | B | PLEKHA7 activity raises MTUS1's level | lines that do not express PLEKHA7 (8) vs lines expressing it (42) | 3.63× lower at baseline in the lines without PLEKHA7 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.3, 43.9); signed map (52.9, 11.0). **Vector** length 103, 24.2% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.1 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.6 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -3.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -4.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.1 | -4.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.3 | -0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing A7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15 — chr11:16,777,297-17,014,415 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686M22243 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IQ23](https://www.uniprot.org/uniprotkb/Q6IQ23) (Pleckstrin homology domain-containing family A member 7):

> Required for zonula adherens biogenesis and maintenance. Acts via its interaction with CAMSAP3, which anchors microtubules at their minus-ends to zonula adherens, leading to the recruitment of KIFC3 kinesin to the junctional site. Mediates docking of ADAM10 to zonula adherens through a PDZD11-dependent interaction with the ADAM10-binding protein TSPAN33.

**Summary**, from NCBI Gene [144100](https://www.ncbi.nlm.nih.gov/gene/144100):

> Enables delta-catenin binding activity. Involved in epithelial cell-cell adhesion; pore complex assembly; and zonula adherens maintenance. Located in several cellular components, including centrosome; nucleoplasm; and zonula adherens. Part of pore complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27049](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27049) · Entrez [144100](https://www.ncbi.nlm.nih.gov/gene/144100) · UniProt [Q6IQ23](https://www.uniprot.org/uniprotkb/Q6IQ23) · Ensembl [ENSG00000166689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166689)

## Data

Gene col 9344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9344); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9344, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9344]; `tensor/DDL_lfc|DDL_z.npy` [9344]; `embed/gene_vectors.npy` [9344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9344 or target_col == 9344). Every well: [[PLEKHA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
