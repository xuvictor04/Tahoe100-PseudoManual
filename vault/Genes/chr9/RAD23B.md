---
symbol: "RAD23B"
type: "gene"
col: 4051
ensembl_id: "ENSG00000119318"
name: "RAD23 nucleotide excision repair protein B"
location: "9q31.2"
module: 25
arm: "+"
pooled_cpm: 195.25
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# RAD23B

*RAD23 nucleotide excision repair protein B* — 9q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.04× (z +14.0, q 6e-42, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.637× (z -12.3, q 3e-32, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBQLN1]] (+0.82, fdr 7e-06), [[DLD]] (+0.74, fdr 7e-06), [[NCKAP1]] (+0.72, fdr 7e-06); moves opposite to [[TPRN]] (-0.67, fdr 7e-06), [[PDCD7]] (-0.65, fdr 7e-06), [[TNRC6C]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4051.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.04×** | +14.0 | 6e-42 | 48/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +13.3 | 6e-38 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.99×** | +13.2 | 1e-37 | 48/48 (LS 180, LoVo, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.55×** | +12.7 | 5e-35 | 47/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.94×** | +12.7 | 6e-35 | 48/48 (LS 180, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +12.2 | 3e-32 | 44/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +11.0 | 4e-26 | 43/49 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.83×** | +10.9 | 5e-26 | 47/48 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +9.9 | 3e-21 | 41/45 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +8.3 | 6e-15 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +8.2 | 2e-14 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +7.6 | 2e-12 | 35/44 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.9 | 2e-07 | 38/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 2e-05 | 37/49 (LOX-IMVI, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.0 | 2e-05 | 26/38 (NCI-H1573, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.021 | 24/49 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.20× | +3.3 | 0.028 | 21/48 (NCI-H460, HS-578T, …) | rises with dose | plate-row cell shift |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.035 | 19/49 (SNU-423, HS-578T, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.042 | 12/49 (CFPAC-1, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4051.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -12.3 | 3e-32 | 45/49 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.566×** | -11.0 | 9e-26 | 48/48 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.587×** | -10.3 | 1e-22 | 44/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.735×** | -6.0 | 3e-07 | 39/48 (HepG2/C3A, SW 900, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -5.4 | 9e-06 | 34/48 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.807×** | -4.2 | 0.003 | 27/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.819×** | -3.9 | 0.008 | 26/48 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.830×** | -3.5 | 0.033 | 24/50 (C32, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.854× | -3.1 | 0.13 | 16/48 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4051. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 199 | 13 (6 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 4.42× (z +21.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.00× (z +20.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.649× (z -9.1) |
| [[SW480 (line)]] | alt | 234 | 12 (5 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -16.3) |
| [[PANC-1 (line)]] | alt | 124 | 12 (4 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +18.4) | [[Panobinostat (drug)]] 5 µM 0.556× (z -9.0) |
| [[LoVo (line)]] | wt | 131 | 11 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.96× (z +15.7) | — |
| [[LS 180 (line)]] | wt | 173 | 10 (3 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.53× (z +16.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.630× (z -8.6) |
| [[HOP62 (line)]] | alt | 151 | 8 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.25× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -9.3) |
| [[COLO 205 (line)]] | alt | 190 | 8 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.40× (z +13.9) | — |
| [[J82 (line)]] | alt | 303 | 5 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.38× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.494× (z -9.9) |
| [[KATO III (line)]] | alt | 189 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +14.9) | — |
| [[NCI-H1792 (line)]] | alt | 123 | 8 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.52× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 170 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.92× (z +13.7) | — |
| [[Panc 03.27 (line)]] | alt | 161 | 6 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 6.49× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -8.9) |
| [[SNU-423 (line)]] | alt | 185 | 7 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.43× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.20× (z +9.9) | — |
| [[SW48 (line)]] | wt | 231 | 7 (1 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 4.43× (z +14.0) | — |
| [[C32 (line)]] | wt | 207 | 4 | 2 | [[PH-797804 (drug)]] 5 µM 7.94× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 192 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.71× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 156 | 5 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 4.70× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.18× (z +15.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 174 | 5 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.90× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.521× (z -9.6) |
| [[SW 900 (line)]] | alt | 199 | 3 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.35× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -10.8) |
| [[A-172 (line)]] | wt | 214 | 3 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.94× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 3.45× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.485× (z -10.6) |
| [[A549 (line)]] | wt | 171 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.04× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -9.6) |
| [[BT-474 (line)]] | alt | 271 | 4 | 1 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.08× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 213 | 4 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.14× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.510× (z -8.5) |
| [[H4 (line)]] | wt | 187 | 3 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.462× (z -8.5) |
| [[Hs 766T (line)]] | wt | 191 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.76× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 243 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.50× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 185 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.19× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.496× (z -9.7) |
| [[A-427 (line)]] | wt | 149 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.79× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 243 | 2 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.21× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 260 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 6.20× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 224 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 4.39× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 153 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.40× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +9.3) | — |
| [[RKO (line)]] | wt | 287 | 2 | 1 | [[PH-797804 (drug)]] 5 µM 4.37× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -13.5) |
| [[A498 (line)]] | wt | 254 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +10.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 149 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.14× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 236 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.83× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.419× (z -9.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 265 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.467× (z -9.1) |
| [[HS-578T (line)]] | alt | 162 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.71× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 130 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 238 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 203 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 235 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 257 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4051), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBQLN1]] | +0.82 | +0.80 / +0.85 | both halves | 7e-06 | STRING 881 |
| [[DLD]] | +0.74 | +0.62 / +0.81 | both halves | 7e-06 |  |
| [[NCKAP1]] | +0.72 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[GSR]] | +0.72 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[FECH]] | +0.71 | +0.35 / +0.69 | both halves | 1e-04 |  |
| [[PFKM]] | +0.71 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[HSD17B4]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[NXPE3]] | +0.69 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[SMG7]] | +0.68 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[MRPL19]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[PGAM1]] | +0.66 | +0.69 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPRN]] | -0.67 | -0.59 / -0.73 | both halves | 7e-06 |  |
| [[PDCD7]] | -0.65 | -0.67 / -0.69 | both halves | 7e-06 |  |
| [[TNRC6C]] | -0.65 | -0.69 / -0.63 | both halves | 7e-06 |  |
| [[ZNF324]] | -0.64 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.63 | -0.56 / -0.68 | both halves | 1e-05 |  |
| [[ZBTB7A]] | -0.60 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[TOB2]] | -0.60 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[ISG20L2]] | -0.60 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[RBX1]] | -0.60 | -0.58 / -0.63 | both halves | 7e-06 | pathway: DNA Damage Recognition in GG-NER; STRING 721 |
| [[IRX5]] | -0.59 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[MIDN]] | -0.58 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[SLC10A3]] | -0.58 | -0.39 / -0.67 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RAD23B's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises RAD23B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.4, -15.7); signed map (-16.2, -41.9). **Vector** length 107, 42.8% of its response variance represented; |z| ≥ 3 in 1,392 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.8 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.4 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.3 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.6 | +13.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.5 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.6 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | -2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -12.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | +8.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -3.4 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -0.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.4 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -0.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | RAD23 nucleotide excision repair protein B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.2 — chr9:107,283,137-107,332,192 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HHR23B, P58, HR23B |
| Gene groups (HGNC) | Nucleotide excision repair; RAD23 nucleotide excision repair protein family |
| Hallmark sets | G2M_CHECKPOINT, MYC_TARGETS_V1 |
| Reactome | 9 pathways, smallest: Josephin domain DUBs; N-glycan trimming in the ER and Calnexin/Calreticulin cycle; DNA Damage Recognition in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [P54727](https://www.uniprot.org/uniprotkb/P54727) (Lysine-specific demethylase RAD23B):

> Multifunctional protein that participates in histone H4K20 demethylation, DNA repair, ubiquitin-dependent protein degradation and transcriptional regulation. Specifically demethylates mono-, di- and trimethylated 'Lys-20' of histone H4 (H4K20me1, H4K20me2, H4K20me3, respectively) into unmethylated forms. Activates the transcription of coding genes by demethylating H4K20me1 and the transcription of repetitive elements by demethylating H4K20me3. Multiubiquitin chain receptor involved in …

**Summary**, from NCBI Gene [5887](https://www.ncbi.nlm.nih.gov/gene/5887):

> The protein encoded by this gene is one of two human homologs of Saccharomyces cerevisiae Rad23, a protein involved in the nucleotide excision repair (NER). This protein was found to be a component of the protein complex that specifically complements the NER defect of xeroderma pigmentosum group C (XP-c) cell extracts in vitro. This protein was also shown to interact with, and elevate the nucleotide excision activity of 3-methyladenine-DNA glycosylase (MPG), which suggested a role in DNA damage …

**Accessions** — [HGNC:9813](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9813) · Entrez [5887](https://www.ncbi.nlm.nih.gov/gene/5887) · UniProt [P54727](https://www.uniprot.org/uniprotkb/P54727) · Ensembl [ENSG00000119318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119318)

## Data

Gene col 4051: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4051); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4051, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4051]; `tensor/DDL_lfc|DDL_z.npy` [4051]; `embed/gene_vectors.npy` [4051]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4051 or target_col == 4051). Every well: [[RAD23B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD23B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
