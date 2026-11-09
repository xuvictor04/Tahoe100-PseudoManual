---
symbol: "ABI1"
type: "gene"
col: 5899
ensembl_id: "ENSG00000136754"
name: "abl interactor 1"
location: "10p12.1"
module: 5
arm: "-"
pooled_cpm: 197.64
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ABI1

*abl interactor 1* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.47× (z +10.5, q 4e-23, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.624× (z -9.2, q 2e-17, down in 37 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.727× (z -6.2, q 5e-08, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSBPL9]] (+0.62, fdr 7e-06), [[OPTN]] (+0.59, fdr 1e-05), [[UBE2D1]] (+0.59, fdr 1e-05); moves opposite to [[DNAAF5]] (-0.61, fdr 2e-05), [[CPSF7]] (-0.60, fdr 1e-05), [[TIMM23B-AGAP6]] (-0.58, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TIMM23B-AGAP6]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5899.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +10.5 | 4e-23 | 37/48 (BT-474, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +8.5 | 5e-15 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +8.1 | 1e-13 | 32/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +7.0 | 3e-10 | 30/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +6.9 | 5e-10 | 38/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +6.1 | 1e-07 | 30/48 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +5.8 | 5e-07 | 29/49 (HepG2/C3A, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +5.3 | 7e-06 | 29/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +5.3 | 7e-06 | 33/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 1e-05 | 27/48 (LS 180, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +4.6 | 2e-04 | 30/49 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +4.6 | 2e-04 | 28/47 (H4, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +4.5 | 2e-04 | 24/48 (A-172, NCI-H23, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.001 | 30/48 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.003 | 21/47 (COLO 205, HT-29, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.5 | 0.016 | 20/47 (SNU-1, H4, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.20× | +3.5 | 0.017 | 24/48 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.048 | 28/48 (NCI-H2030, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.048 | 16/48 (BT-474, NCI-H2030, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.051 | 13/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5899.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.624×** | -9.2 | 2e-17 | 37/49 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.632×** | -8.6 | 2e-15 | 41/47 (NCI-H2347, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.632×** | -8.6 | 2e-15 | 37/44 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.735×** | -8.5 | 3e-15 | 37/49 (A549, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.700×** | -6.4 | 1e-08 | 32/45 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.727×** | -6.2 | 5e-08 | 35/48 (Panc 03.27, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.764×** | -5.3 | 1e-05 | 29/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.828×** | -5.2 | 1e-05 | 24/48 (H4, CFPAC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.656×** | -4.3 | 0.001 | 29/48 (NCI-H2347, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.821×** | -3.9 | 0.006 | 23/48 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.828×** | -3.7 | 0.011 | 24/48 (CFPAC-1, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.697×** | -3.7 | 0.011 | 29/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.709×** | -3.5 | 0.020 | 26/48 (NCI-H2347, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.882× | -3.5 | 0.021 | 14/48 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.839× | -3.4 | 0.024 | 21/48 (CFPAC-1, A-172, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.847× | -3.2 | 0.042 | 19/48 (BT-474, A549, …) | two highest doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.851× | -3.1 | 0.054 | 14/48 (C32, A498, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.852× | -3.1 | 0.055 | 21/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5899. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 119 | 11 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.04× (z +19.4) | — |
| [[PANC-1 (line)]] | alt | 108 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +17.3) | — |
| [[BT-474 (line)]] | alt | 191 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +20.8) | [[Dinaciclib (drug)]] 5 µM 0.440× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[CFPAC-1 (line)]] | alt | 397 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.602× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 293 | 0 | 7 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.395× (z -12.8) ⚠ unreliable plate only · without an alert: [[Belumosudil (drug)]] 5 µM 0.482× (z -9.7) |
| [[A-172 (line)]] | wt | 257 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 146 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 344 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[LS 180 (line)]] | wt | 240 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.24× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 279 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 139 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +18.7) | — |
| [[A549 (line)]] | wt | 228 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -19.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 266 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 179 | 2 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.54× (z +13.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 198 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H1573 (line)]] | alt | 195 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 226 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +11.9) | — |
| [[A498 (line)]] | wt | 178 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +14.9) | — |
| [[J82 (line)]] | alt | 155 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +18.0) | — |
| [[KATO III (line)]] | alt | 156 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 178 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.448× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.496× (z -9.3) |
| [[SW 900 (line)]] | alt | 178 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +8.7) | — |
| [[SW48 (line)]] | wt | 227 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.39× (z +9.7) | — |
| [[CHP-212 (line)]] | wt | 114 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.238× (z -9.3) |
| [[H4 (line)]] | wt | 163 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 154 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 161 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 188 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 1.79× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 203 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 225 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.24× (z +8.6) ⚠ toxic | — |
| [[SNU-1 (line)]] | wt | 170 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.56× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 212 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.440× (z -8.5) |
| [[SW480 (line)]] | alt | 193 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 175 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 117 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 137 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 182 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 293 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 301 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 249 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 138 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5899), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSBPL9]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[OPTN]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[UBE2D1]] | +0.59 | +0.51 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[CCNDBP1]] | +0.59 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[YPEL2]] | +0.58 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ATP11B]] | +0.57 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[DMXL1]] | +0.57 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[ZC2HC1A]] | +0.57 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[JUP]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 | pathway: Signaling by VEGF |
| [[DDAH2]] | +0.56 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[RALBP1]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[CHMP2B]] | +0.56 | +0.41 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF5]] | -0.61 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[CPSF7]] | -0.60 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | -0.58 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[TMX2]] | -0.57 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[PRDM15]] | -0.57 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[TSR1]] | -0.57 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[UPF1]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ZNF8]] | -0.54 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[EARS2]] | -0.54 | -0.37 / -0.62 | both halves | 7e-05 |  |
| [[TRNT1]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ALG8]] | -0.54 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[ABCE1]] | -0.54 | -0.61 / -0.42 | both halves | 4e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TIMM23B-AGAP6]] | C | TIMM23B-AGAP6's natural level strengthens ABI1's drug response | TIMM23B-AGAP6's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.09; direction not clear | 0.052 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.593). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (0.1, -37.2); signed map (-10.2, 14.7). **Vector** length 105, 40.1% of its response variance represented; |z| ≥ 3 in 1,336 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +7.6 | -9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +6.6 | -8.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.5 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +5.3 | -6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.8 | +5.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.0 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.5 | +3.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +4.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.3 | -5.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.0 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.2 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.3 | -3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | abl interactor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:26,746,593-26,861,087 (-) |
| Ensembl biotype | protein_coding |
| Also known as | E3B1, ABI-1; previously SSH3BP1 |
| Gene groups (HGNC) | ABI family; SH3 domain containing |
| Hallmark sets | ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, MITOTIC_SPINDLE |
| Reactome | 19 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZP0](https://www.uniprot.org/uniprotkb/Q8IZP0) (Abl interactor 1):

> May act in negative regulation of cell growth and transformation by interacting with nonreceptor tyrosine kinases ABL1 and/or ABL2. May play a role in regulation of EGF-induced Erk pathway activation. Involved in cytoskeletal reorganization and EGFR signaling. Together with EPS8 participates in transduction of signals from Ras to Rac. In vitro, a trimeric complex of ABI1, EPS8 and SOS1 exhibits Rac specific guanine nucleotide exchange factor (GEF) activity and ABI1 seems to act as an adapter in …

**Summary**, from NCBI Gene [10006](https://www.ncbi.nlm.nih.gov/gene/10006):

> This gene encodes a member of the Abelson-interactor family of adaptor proteins. These proteins facilitate signal transduction as components of several multiprotein complexes, and regulate actin polymerization and cytoskeletal remodeling through interactions with Abelson tyrosine kinases. The encoded protein plays a role in macropinocytosis as a component of the WAVE2 complex, and also forms a complex with EPS8 and SOS1 that mediates signal transduction from Ras to Rac. This gene may play a …

**Accessions** — [HGNC:11320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11320) · Entrez [10006](https://www.ncbi.nlm.nih.gov/gene/10006) · UniProt [Q8IZP0](https://www.uniprot.org/uniprotkb/Q8IZP0) · Ensembl [ENSG00000136754](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136754)

## Data

Gene col 5899: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5899); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5899, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5899]; `tensor/DDL_lfc|DDL_z.npy` [5899]; `embed/gene_vectors.npy` [5899]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5899 or target_col == 5899). Every well: [[ABI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
