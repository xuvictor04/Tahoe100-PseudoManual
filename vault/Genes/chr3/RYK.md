---
symbol: "RYK"
type: "gene"
col: 8776
ensembl_id: "ENSG00000163785"
name: "receptor like tyrosine kinase"
location: "3q22.2"
module: 182
arm: "+"
pooled_cpm: 160.5
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# RYK

*receptor like tyrosine kinase* — 3q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.20× (z +7.8, q 2e-12, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.595× (z -9.8, q 5e-20, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMAD5]] (+0.67, fdr 7e-06), [[USP3]] (+0.67, fdr 7e-06), [[FOXJ3]] (+0.63, fdr 7e-06); moves opposite to [[SETX]] (-0.61, fdr 1e-05), [[TUT7]] (-0.58, fdr 7e-06), [[SUPT6H]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 182]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8776.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.20×** | +7.8 | 2e-12 | 41/49 (SW480, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +7.7 | 3e-12 | 39/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.01×** | +7.0 | 7e-10 | 39/48 (A-427, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +6.8 | 1e-09 | 34/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +5.2 | 2e-05 | 34/47 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +5.0 | 7e-05 | 32/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 1e-04 | 30/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.13× | +3.4 | 0.045 | 17/48 (A-427, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.3 | 0.059 | 18/38 (NCI-H1573, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.17× | +3.1 | 0.12 | 19/48 (NCI-H23, H4, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8776.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.595×** | -9.8 | 5e-20 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.616×** | -9.2 | 1e-17 | 40/48 (C32, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.639×** | -8.5 | 5e-15 | 40/49 (NCI-H2347, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.633×** | -8.3 | 1e-14 | 39/44 (SNU-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.719×** | -6.2 | 5e-08 | 34/48 (SW480, SW48, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.780×** | -4.7 | 2e-04 | 27/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.786×** | -4.2 | 0.002 | 25/45 (C-33 A, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.796×** | -4.1 | 0.003 | 23/47 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~10% of this change | **0.821×** | -3.7 | 0.012 | 25/48 (hTERT-HPNE, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.824×** | -3.6 | 0.015 | 25/48 (MIA PaCa-2, J82, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.833×** | -3.5 | 0.028 | 23/48 (AsPC-1, A549, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.834× | -3.4 | 0.031 | 22/48 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.843× | -3.2 | 0.059 | 16/48 (Panc 03.27, SW1417, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.846× | -3.2 | 0.064 | 18/48 (AsPC-1, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8776. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 194 | 9 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +18.6) | [[Panobinostat (drug)]] 0.5 µM 0.549× (z -10.3) |
| [[SW48 (line)]] | wt | 187 | 3 | 4 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.48× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.414× (z -9.2) |
| [[SW480 (line)]] | alt | 145 | 3 (1 ⚠) | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.78× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.423× (z -14.6) |
| [[A-427 (line)]] | wt | 233 | 3 (2 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.73× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 221 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +10.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 232 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 129 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -10.0) |
| [[LoVo (line)]] | wt | 120 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.11× (z +9.8) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.416× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.533× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 188 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.409× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.516× (z -8.7) |
| [[C-33 A (line)]] | alt | 195 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[C32 (line)]] | wt | 205 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.331× (z -12.3) |
| [[HCT15 (line)]] | alt | 149 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.128× (z -11.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 156 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.485× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 257 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.42× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.457× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 168 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.428× (z -9.9) |
| [[SNU-1 (line)]] | wt | 215 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0636× (z -27.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -9.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 252 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 116 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 148 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.322× (z -11.9) ⚠ transcription drop; cell-cycle shift, explains ~10% of this change |
| [[LS 180 (line)]] | wt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.404× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.35× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.499× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW 900 (line)]] | alt | 125 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.396× (z -10.0) |
| [[SW1417 (line)]] | alt | 218 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 194 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 81.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 244 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 154 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 176 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8776), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD5]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[USP3]] | +0.67 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[FOXJ3]] | +0.63 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[SEC24B]] | +0.63 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[RNF145]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[SNRPA1]] | +0.62 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[MTX2]] | +0.61 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[FIP1L1]] | +0.61 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[FHIP2A]] | +0.60 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[SNX4]] | +0.59 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[MLLT10]] | +0.59 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[C16orf87]] | +0.58 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETX]] | -0.61 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[TUT7]] | -0.58 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[SUPT6H]] | -0.56 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[RP2]] | -0.54 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[EXOC8]] | -0.52 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[ATP6V1D]] | -0.48 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[RABL3]] | -0.48 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[KATNIP]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[TAF2]] | -0.47 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[NPC1]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-7.1, -8.9); signed map (-34.5, -10.6). **Vector** length 105, 36.0% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +7.9 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.0 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.3 | -0.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.2 | -0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +0.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.0 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +2.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.6 | -9.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.3 | +5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | +7.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -0.2 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.3 | -1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | receptor like tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.2 — chr3:134,065,303-134,250,859 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D3S3195, RYK1, JTK5; previously JTK5A |
| Gene groups (HGNC) | Pseudokinases; WNT binding RTK type pseudokinases |
| Reactome | 4 pathways, smallest: PCP/CE pathway; Beta-catenin independent WNT signaling; TCF dependent signaling in response to WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [P34925](https://www.uniprot.org/uniprotkb/P34925) (Inactive tyrosine-protein kinase RYK):

> May be a coreceptor along with FZD8 of Wnt proteins, such as WNT1, WNT3, WNT3A and WNT5A. Involved in neuron differentiation, axon guidance, corpus callosum establishment and neurite outgrowth. In response to WNT3 stimulation, receptor C-terminal cleavage occurs in its transmembrane region and allows the C-terminal intracellular product to translocate from the cytoplasm to the nucleus where it plays a crucial role in neuronal development.

**Summary**, from NCBI Gene [6259](https://www.ncbi.nlm.nih.gov/gene/6259):

> The protein encoded by this gene is an atypical member of the family of growth factor receptor protein tyrosine kinases, differing from other members at a number of conserved residues in the activation and nucleotide binding domains. This gene product belongs to a subfamily whose members do not appear to be regulated by phosphorylation in the activation segment. It has been suggested that mediation of biological activity by recruitment of a signaling-competent auxiliary protein may occur …

**Accessions** — [HGNC:10481](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10481) · Entrez [6259](https://www.ncbi.nlm.nih.gov/gene/6259) · UniProt [P34925](https://www.uniprot.org/uniprotkb/P34925) · Ensembl [ENSG00000163785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163785)

## Data

Gene col 8776: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8776); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8776, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8776]; `tensor/DDL_lfc|DDL_z.npy` [8776]; `embed/gene_vectors.npy` [8776]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8776 or target_col == 8776). Every well: [[RYK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RYK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
