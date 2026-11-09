---
symbol: "VPS13C"
type: "gene"
col: 4940
ensembl_id: "ENSG00000129003"
name: "vacuolar protein sorting 13 homolog C"
location: "15q22.2"
module: 142
arm: "+"
pooled_cpm: 200.4
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# VPS13C

*vacuolar protein sorting 13 homolog C* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.32× (z +5.0, q 3e-04, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.569× (z -10.5, q 7e-23, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNPDA1]] (+0.65, fdr 7e-06), [[TMEM126B]] (+0.65, fdr 9e-06), [[STX17]] (+0.64, fdr 7e-06); moves opposite to [[ZNF668]] (-0.62, fdr 7e-06), [[LRRC8A]] (-0.61, fdr 1e-05), [[RNF121]] (-0.60, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4940.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +5.0 | 3e-04 | 39/47 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.33×** | +4.5 | 0.002 | 35/50 (NCI-H1573, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.67×** | +4.0 | 0.013 | 36/50 (NCI-H1573, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.8 | 0.018 | 13/48 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.23×** | +3.7 | 0.021 | 23/47 (NCI-H460, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.021 | 28/47 (AsPC-1, SW480, …) | rises with dose |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.6 | 0.021 | 25/48 (KATO III, NCI-H1573, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.021 | 15/48 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.20× | +3.3 | 0.059 | 23/48 (HOP62, RPMI-7951, …) | two highest doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.21×** | +3.3 | 0.059 | 21/48 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +3.3 | 0.059 | 21/48 (A-427, HS-578T, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.060 | 21/48 (KATO III, J82, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.062 | 23/48 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.073 | 10/49 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.073 | 23/48 (NCI-H1573, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.073 | 18/49 (AsPC-1, SW48, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4940.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.569×** | -10.5 | 7e-23 | 44/48 (LoVo, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.645×** | -8.2 | 1e-13 | 39/48 (SHP-77, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.403×** | -7.1 | 3e-10 | 45/49 (LoVo, RPMI-7951, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.681×** | -6.9 | 8e-10 | 41/47 (NCI-H1573, HT-29, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.794×** | -6.1 | 1e-07 | 29/49 (A549, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.730×** | -5.9 | 4e-07 | 35/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.741×** | -5.6 | 2e-06 | 29/48 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.510×** | -5.2 | 1e-05 | 33/48 (Panc 03.27, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.766×** | -5.0 | 4e-05 | 33/48 (SW480, PANC-1, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -4.4 | 8e-04 | 1/50 (AsPC-1) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.778×** | -4.3 | 8e-04 | 26/45 (A-172, KATO III, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.797×** | -4.2 | 0.001 | 29/48 (SHP-77, LoVo, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~67% of this change | **0.814×** | -3.7 | 0.010 | 24/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.627×** | -3.6 | 0.011 | 26/45 (NCI-H1573, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~86% of this change | **0.831×** | -3.5 | 0.021 | 24/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.832×** | -3.4 | 0.021 | 21/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.835× | -3.4 | 0.025 | 21/48 (NCI-H1573, LS 180, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.844× | -3.2 | 0.047 | 18/47 (NCI-H1573, HT-29, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.854× | -2.9 | 0.086 | 22/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4940. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 186 | 0 | 9 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.381× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 243 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.347× (z -13.4) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.407× (z -11.9) |
| [[PANC-1 (line)]] | alt | 208 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.428× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.572× (z -8.7) |
| [[A-172 (line)]] | wt | 291 | 3 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[BT-474 (line)]] | alt | 191 | 2 (2 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 0.5 µM 2.38× (z +10.7) ⚠ cell-cycle shift, explains ~50% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -10.2) ⚠ cell-cycle shift, explains ~15% of this change |
| [[HT-29 (line)]] | alt | 247 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -12.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.374× (z -12.0) |
| [[LoVo (line)]] | wt | 442 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.378× (z -14.6) |
| [[SHP-77 (line)]] | alt | 232 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.273× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SK-MEL-2 (line)]] | alt | 190 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.473× (z -9.4) |
| [[A-427 (line)]] | wt | 148 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.453× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[A549 (line)]] | wt | 403 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -17.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 217 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.390× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[LS 180 (line)]] | wt | 261 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.385× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.494× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 127 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.376× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 291 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.416× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SNU-1 (line)]] | wt | 202 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.341× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 206 | 1 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 1.65× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.449× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 75.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 243 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 197 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.391× (z -10.6) ⚠ toxic |
| [[C-33 A (line)]] | alt | 210 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.498× (z -8.6) |
| [[COLO 205 (line)]] | alt | 249 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.449× (z -10.5) |
| [[HCT15 (line)]] | alt | 236 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.426× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[HEC-1-A (line)]] | alt | 185 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.552× (z -9.1) |
| [[Hs 766T (line)]] | wt | 139 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.487× (z -9.5) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 142 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.380× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 211 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 208 | 1 | 0 | [[Atazanavir (sulfate) (drug)]] 0.05 µM 2.86× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 174 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.483× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 297 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.481× (z -8.8) |
| [[SNU-423 (line)]] | alt | 174 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.524× (z -8.6) |
| [[SW 1088 (line)]] | alt | 171 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0928× (z -11.8) |
| [[A498 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 223 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 187 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 142 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 157 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 231 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 364 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 137 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4940), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNPDA1]] | +0.65 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[TMEM126B]] | +0.65 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[STX17]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[RAD50]] | +0.61 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[TAF9]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CCDC25]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[RFK]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[EEA1]] | +0.56 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[GYG1]] | +0.55 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[THOC7]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[SETDB2]] | +0.55 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ATRX]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF668]] | -0.62 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[LRRC8A]] | -0.61 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[RNF121]] | -0.60 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[RAB43]] | -0.59 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[IL9RP3]] | -0.58 | -0.26 / -0.59 | both halves | 4e-04 |  |
| [[CHST12]] | -0.58 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[SDHAP4-1]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[ATG101]] | -0.57 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[STARD3]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ASB16-AS1]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ANKRD13D]] | -0.55 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ARPC5L]] | -0.55 | -0.41 / -0.57 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers VPS13C's level | compounds that target MTOR: 3 of 8 raise it (AZD-8055, Bimiralisib, Sapanisertib) | 38% of the class's compounds vs 2.0% of all compounds | 0.088 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction -0.622). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.7, 13.2); signed map (11.8, -26.1). **Vector** length 109, 37.4% of its response variance represented; |z| ≥ 3 in 1,285 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.9 | +1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +7.1 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.1 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.1 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.9 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +0.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.5 | -10.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.0 | -6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -5.1 | -6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -5.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | vacuolar protein sorting 13 homolog C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:61,852,389-62,060,473 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20136, FLJ10381, KIAA1421, BLTP5C, PARK23 |
| Gene groups (HGNC) | Bridge-like lipid transfer protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q709C8](https://www.uniprot.org/uniprotkb/Q709C8) (Intermembrane lipid transfer protein VPS13C):

> Mediates the transfer of lipids between membranes at organelle contact sites (By similarity). Necessary for proper mitochondrial function and maintenance of mitochondrial transmembrane potential. Involved in the regulation of PINK1/PRKN-mediated mitophagy in response to mitochondrial depolarization.

**Summary**, from NCBI Gene [54832](https://www.ncbi.nlm.nih.gov/gene/54832):

> Involved in mitochondrion organization and negative regulation of type 2 mitophagy. Located in several cellular components, including late endosome; lipid droplet; and mitochondrial outer membrane. Implicated in Parkinson's disease 23. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23594) · Entrez [54832](https://www.ncbi.nlm.nih.gov/gene/54832) · UniProt [Q709C8](https://www.uniprot.org/uniprotkb/Q709C8) · Ensembl [ENSG00000129003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129003)

## Data

Gene col 4940: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4940); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4940, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4940]; `tensor/DDL_lfc|DDL_z.npy` [4940]; `embed/gene_vectors.npy` [4940]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4940 or target_col == 4940). Every well: [[VPS13C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS13C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
