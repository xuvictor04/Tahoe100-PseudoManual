---
symbol: "RTN3"
type: "gene"
col: 5441
ensembl_id: "ENSG00000133318"
name: "reticulon 3"
location: "11q13"
module: 11
arm: "-"
pooled_cpm: 184.7
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# RTN3

*reticulon 3* — 11q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.44× (z +22.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.710× (z -8.5, q 2e-14, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDH1]] (+0.69, fdr 7e-06), [[PRKCI]] (+0.66, fdr 7e-06), [[SARAF]] (+0.63, fdr 1e-05); moves opposite to [[UTP3]] (-0.67, fdr 1e-05), [[ZNF689]] (-0.65, fdr 1e-05), [[ZNF597]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CDS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.44×** | +22.0 | 0e+00 | 48/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +18.4 | 0e+00 | 47/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +17.6 | 0e+00 | 48/48 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +11.7 | 1e-29 | 44/48 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +11.2 | 3e-27 | 39/49 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +11.0 | 6e-26 | 33/44 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +10.5 | 6e-24 | 43/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +10.5 | 8e-24 | 43/48 (C32, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +10.1 | 3e-22 | 46/48 (C32, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +9.5 | 2e-19 | 35/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +8.5 | 1e-15 | 42/48 (C32, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +7.7 | 5e-13 | 29/48 (NCI-H460, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +7.0 | 1e-10 | 37/49 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +6.2 | 2e-08 | 41/49 (LOX-IMVI, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +6.1 | 5e-08 | 32/48 (C32, NCI-H2030, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.57×** | +5.8 | 2e-07 | 38/48 (SW480, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +5.6 | 7e-07 | 28/48 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +5.2 | 6e-06 | 30/49 (LOX-IMVI, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5441.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -8.5 | 2e-14 | 33/48 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.737×** | -7.5 | 1e-11 | 32/48 (A-427, PANC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.762×** | -6.5 | 2e-08 | 26/48 (LoVo, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.777×** | -6.2 | 7e-08 | 32/48 (AN3 CA, A-427, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.800×** | -5.1 | 4e-05 | 31/47 (LoVo, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.741×** | -3.9 | 0.011 | 23/49 (LoVo, Hs 766T, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.958× | -3.8 | 0.011 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.881× | -3.1 | 0.12 | 6/48 (LS 180, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 84.3 | 11 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.34× (z +14.8) | — |
| [[PANC-1 (line)]] | alt | 187 | 9 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.11× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.02× (z +14.2) | [[Homoharringtonine (drug)]] 0.05 µM 0.627× (z -9.5) |
| [[A549 (line)]] | wt | 148 | 7 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.15× (z +18.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.524× (z -10.2) ⚠ cell-cycle shift, explains ~19% of this change |
| [[LOX-IMVI (line)]] | wt | 120 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.80× (z +20.2) | — |
| [[NCI-H460 (line)]] | wt | 136 | 8 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.14× (z +18.4) | — |
| [[AsPC-1 (line)]] | alt | 191 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +16.7) | — |
| [[HOP62 (line)]] | alt | 94.8 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.91× (z +15.1) | — |
| [[LoVo (line)]] | wt | 192 | 4 (1 ⚠) | 3 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.10× (z +11.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 1.96× (z +11.3) | [[Harringtonine (drug)]] 5 µM 0.388× (z -15.3) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.487× (z -12.1) |
| [[SW480 (line)]] | alt | 216 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.61× (z +19.1) | — |
| [[A-172 (line)]] | wt | 154 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.89× (z +14.5) | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.471× (z -10.2) |
| [[A-427 (line)]] | wt | 280 | 3 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 1.79× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -21.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.557× (z -10.6) |
| [[J82 (line)]] | alt | 263 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +16.3) | — |
| [[SW1417 (line)]] | alt | 263 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +14.0) | — |
| [[A498 (line)]] | wt | 91.2 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 171 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +12.8) | — |
| [[KATO III (line)]] | alt | 301 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.22× (z +11.4) | [[Harringtonine (drug)]] 5 µM 0.425× (z -11.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[NCI-H1573 (line)]] | alt | 112 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.33× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 229 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.67× (z +16.0) | — |
| [[RKO (line)]] | wt | 137 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.41× (z +15.5) | — |
| [[COLO 205 (line)]] | alt | 192 | 4 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.27× (z +13.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 2.13× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.91× (z +13.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 200 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.10× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 121 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 199 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.29× (z +14.5) | [[Harringtonine (drug)]] 0.5 µM 0.608× (z -8.8) |
| [[SW 900 (line)]] | alt | 175 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +12.1) | — |
| [[H4 (line)]] | wt | 147 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.31× (z +11.5) | — |
| [[HepG2_C3A (line)]] | wt | 117 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 169 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +14.1) | — |
| [[NCI-H1792 (line)]] | alt | 120 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.14× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 171 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.29× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 125 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.46× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 66.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.05× (z +10.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -8.7) ⚠ cell-cycle shift, explains ~19% of this change |
| [[SNU-423 (line)]] | alt | 188 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +11.6) | — |
| [[BT-474 (line)]] | alt | 286 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.39× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 194 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 1.75× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 273 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.76× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.563× (z -9.3) ⚠ cell-cycle shift, explains ~19% of this change |
| [[HCT15 (line)]] | alt | 239 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.338× (z -13.6) ⚠ cell-cycle shift, explains ~23% of this change |
| [[HT-29 (line)]] | alt | 412 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.508× (z -9.4) ⚠ cell-cycle shift, explains ~19% of this change |
| [[AN3 CA (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0731× (z -22.9) ⚠ cell-cycle shift, explains ~19% of this change |
| [[HEC-1-A (line)]] | alt | 250 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.71× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H596 (line)]] | alt | 179 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.126× (z -11.2) |
| [[SHP-77 (line)]] | alt | 135 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.98× (z +9.0) | — |
| [[CHP-212 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 244 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 209 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 218 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDH1]] | +0.69 | +0.70 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS |
| [[PRKCI]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[SARAF]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PLA2G12A]] | +0.62 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[SNX3]] | +0.61 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[GFPT1]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[CALCOCO2]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ASAP3]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[STRN]] | +0.59 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[HSPA5]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 | pathway: Dengue Virus Genome Translation and Replication |
| [[ERP29]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[PHGDH]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP3]] | -0.67 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[ZNF689]] | -0.65 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[ZNF597]] | -0.63 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[MRM2]] | -0.63 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[CHAMP1]] | -0.62 | -0.71 / -0.41 | both halves | 4e-05 |  |
| [[SURF6]] | -0.61 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[CCDC137]] | -0.61 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[CYREN]] | -0.60 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ADO]] | -0.60 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[DDX28]] | -0.60 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[THUMPD3]] | -0.59 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[ZBTB6]] | -0.58 | -0.54 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDS1]] | B | CDS1 activity raises RTN3's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without CDS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[F11R]] | B | F11R activity raises RTN3's level | lines that do not express F11R (10) vs lines expressing it (40) | 1.20× lower at baseline in the lines without F11R | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-8.5, 7.0); signed map (-17.9, 27.9). **Vector** length 145, 52.5% of its response variance represented; |z| ≥ 3 in 1,509 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +11.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +7.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +6.3 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.8 | +10.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.6 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +10.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.9 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -12.9 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -12.2 | -8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -10.8 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -10.5 | -7.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -9.4 | -6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -8.1 | -5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | reticulon 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13 — chr11:63,681,446-63,759,891 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NSPL2, NSPLII, ASYIP, HAP, RTN3-A1 |
| Gene groups (HGNC) | Reticulons |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 6 pathways, smallest: Synaptic adhesion-like molecules; Protein-protein interactions at synapses; Dengue Virus Genome Translation and Replication |
| Matched by | ensembl_id |

**Function**, from UniProt [O95197](https://www.uniprot.org/uniprotkb/O95197) (Reticulon-3):

> May be involved in membrane trafficking in the early secretory pathway. Inhibits BACE1 activity and amyloid precursor protein processing. May induce caspase-8 cascade and apoptosis. May favor BCL2 translocation to the mitochondria upon endoplasmic reticulum stress. Induces the formation of endoplasmic reticulum tubules. Also acts as an inflammation-resolving regulator by interacting with both TRIM25 and RIGI, subsequently impairing RIGI 'Lys-63'-linked polyubiquitination leading to IRF3 and …

**Summary**, from NCBI Gene [10313](https://www.ncbi.nlm.nih.gov/gene/10313):

> This gene belongs to the reticulon family of highly conserved genes that are preferentially expressed in neuroendocrine tissues. This family of proteins interact with, and modulate the activity of beta-amyloid converting enzyme 1 (BACE1), and the production of amyloid-beta. An increase in the expression of any reticulon protein substantially reduces the production of amyloid-beta, suggesting that reticulon proteins are negative modulators of BACE1 in cells. Alternatively spliced transcript …

**Accessions** — [HGNC:10469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10469) · Entrez [10313](https://www.ncbi.nlm.nih.gov/gene/10313) · UniProt [O95197](https://www.uniprot.org/uniprotkb/O95197) · Ensembl [ENSG00000133318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133318)

## Data

Gene col 5441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5441); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5441]; `tensor/DDL_lfc|DDL_z.npy` [5441]; `embed/gene_vectors.npy` [5441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5441 or target_col == 5441). Every well: [[RTN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
