---
symbol: "TARS1"
type: "gene"
col: 3462
ensembl_id: "ENSG00000113407"
name: "threonyl-tRNA synthetase 1"
location: "5p13.3"
module: 63
arm: "+"
pooled_cpm: 161.63
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 12
n_dd_up_clean: 27
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# TARS1

*threonyl-tRNA synthetase 1* — 5p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 2.17× (z +14.3, q 1e-43, up in 47 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.71× (z +10.3, q 8e-23, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.661× (z -8.0, q 7e-13, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NARS1]] (+0.85, fdr 7e-06), [[YARS1]] (+0.84, fdr 7e-06), [[AARS1]] (+0.83, fdr 7e-06); moves opposite to [[POLR2L]] (-0.55, fdr 1e-05), [[ZSWIM4]] (-0.46, fdr 3e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ASNSP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3462.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +14.3 | 1e-43 | 47/47 (Hs 766T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.87×** | +12.1 | 3e-31 | 47/48 (SW 900, AsPC-1, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +10.3 | 8e-23 | 44/48 (BT-474, C32, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **1.41×** | +8.7 | 3e-16 | 43/48 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.58×** | +8.5 | 1e-15 | 47/48 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.47×** | +7.4 | 2e-11 | 41/48 (Panc 03.27, C-33 A, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.44×** | +6.8 | 9e-10 | 39/48 (SHP-77, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.84×** | +6.1 | 6e-08 | 39/49 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.28×** | +6.1 | 6e-08 | 32/48 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +5.9 | 2e-07 | 27/49 (NCI-H23, A549, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +5.9 | 2e-07 | 33/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +5.8 | 3e-07 | 33/49 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.78×** | +5.8 | 3e-07 | 39/48 (LOX-IMVI, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.77×** | +5.7 | 4e-07 | 38/48 (AsPC-1, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.77×** | +5.7 | 4e-07 | 43/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.67×** | +5.2 | 7e-06 | 35/48 (AsPC-1, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.31×** | +5.2 | 7e-06 | 32/47 (SHP-77, C32, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.30×** | +5.0 | 2e-05 | 31/48 (NCI-H460, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3462.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.661×** | -8.0 | 7e-13 | 40/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.686×** | -7.3 | 8e-11 | 42/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.726×** | -6.2 | 1e-07 | 37/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -5.6 | 2e-06 | 28/49 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.756×** | -5.4 | 7e-06 | 33/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.746×** | -5.2 | 2e-05 | 31/47 (LoVo, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.783×** | -4.6 | 4e-04 | 25/47 (HT-29, RKO, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.843× | -4.2 | 0.002 | 24/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.802×** | -4.1 | 0.002 | 26/49 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.814×** | -4.0 | 0.004 | 26/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.816×** | -3.8 | 0.007 | 25/48 (Hs 766T, H4, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.862× | -3.8 | 0.007 | 15/48 (KATO III, J82, …) | all doses, stronger at high dose |  |
| [[Sodium Salicylate (drug)]] 0.5 µM |  | **0.829×** | -3.5 | 0.019 | 21/48 (HS-578T, NCI-H23, …) | two highest doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.841× | -3.4 | 0.031 | 21/48 (AsPC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.842× | -3.3 | 0.031 | 20/49 (RPMI-7951, NCI-H2347, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.787×** | -3.3 | 0.033 | 22/48 (SHP-77, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3462. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 273 | 1 (1 ⚠) | 8 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.78× (z +8.9) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -16.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.467× (z -11.9) |
| [[LoVo (line)]] | wt | 198 | 1 (1 ⚠) | 5 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.70× (z +13.8) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.451× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 112 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.81× (z +15.0) | — |
| [[PANC-1 (line)]] | alt | 241 | 1 (1 ⚠) | 5 | [[Niclosamide (olamine) (drug)]] 5 µM 1.75× (z +8.8) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.372× (z -16.2) |
| [[Hs 766T (line)]] | wt | 155 | 5 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.40× (z +15.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +10.3) | — |
| [[KATO III (line)]] | alt | 150 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 142 | 5 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.44× (z +14.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 86.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.77× (z +14.9) | — |
| [[SW1417 (line)]] | alt | 214 | 1 (1 ⚠) | 3 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.92× (z +9.1) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.577× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 223 | 3 (1 ⚠) | 1 | [[PH-797804 (drug)]] 5 µM 3.60× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -10.3) |
| [[BT-474 (line)]] | alt | 162 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.65× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.426× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 60.2 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.49× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 168 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.09× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.491× (z -9.3) |
| [[RKO (line)]] | wt | 199 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.15× (z +9.6) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.500× (z -9.1) |
| [[SHP-77 (line)]] | alt | 177 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.70× (z +11.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +11.0) | — |
| [[A498 (line)]] | wt | 207 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.04× (z +9.0) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -8.8) |
| [[A549 (line)]] | wt | 102 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | — |
| [[AsPC-1 (line)]] | alt | 109 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.84× (z +13.9) ⚠ toxic | — |
| [[COLO 205 (line)]] | alt | 116 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 5.74× (z +15.0) ⚠ toxic | [[Digitoxin (drug)]] 5 µM 0.365× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 119 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.46× (z +9.9) ⚠ unreliable plate only | — |
| [[A-427 (line)]] | wt | 190 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 114 | 1 | 0 | [[5-Azacytidine (drug)]] 5 µM 2.66× (z +9.3) | — |
| [[H4 (line)]] | wt | 194 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 101 | 1 | 0 | [[Artesunate (drug)]] 5 µM 1.94× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 164 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.31× (z +11.5) ⚠ toxic | — |
| [[HS-578T (line)]] | alt | 216 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.16× (z +9.0) ⚠ toxic | — |
| [[J82 (line)]] | alt | 194 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.17× (z +10.3) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 153 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 81.5 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.96× (z +11.6) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 153 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.30× (z +11.3) ⚠ toxic | — |
| [[RPMI-7951 (line)]] | alt | 124 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.28× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 134 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.56× (z +9.1) ⚠ toxic | — |
| [[SW 900 (line)]] | alt | 190 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.64× (z +10.8) ⚠ unreliable plate only | — |
| [[SW48 (line)]] | wt | 166 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.61× (z +10.8) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 111 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 177 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 159 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3462), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NARS1]] | +0.85 | +0.83 / +0.80 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 924 |
| [[YARS1]] | +0.84 | +0.79 / +0.86 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 911 |
| [[AARS1]] | +0.83 | +0.80 / +0.85 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 929 |
| [[IARS1]] | +0.82 | +0.79 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 913 |
| [[MARS1]] | +0.82 | +0.83 / +0.80 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 881 |
| [[PSAT1]] | +0.81 | +0.80 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[XPOT]] | +0.81 | +0.78 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[TCEA1]] | +0.81 | +0.79 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[CEBPG]] | +0.79 | +0.77 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[EPRS1]] | +0.78 | +0.81 / +0.82 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 928 |
| [[HSPA9]] | +0.77 | +0.73 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 402 |
| [[PCK2]] | +0.77 | +0.77 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2L]] | -0.55 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ZSWIM4]] | -0.46 | -0.43 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASNSP1]] | B | ASNSP1 activity raises TARS1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.30× lower at baseline in the lines without ASNSP1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.838). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.1, 47.4); signed map (-13.7, 23.8). **Vector** length 149, 54.2% of its response variance represented; |z| ≥ 3 in 1,537 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.69 to 16); *mTORC1 signaling* (hallmark, mean cos +0.65 to 20); *Metabolism of amino acids and derivatives* (reactome, mean cos +0.66 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.9 | +12.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +9.9 | +14.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.7 | +10.3 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +8.2 | +8.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +7.8 | +7.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +7.3 | +6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +7.2 | +4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +6.7 | +6.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -8.7 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.3 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.1 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.4 | -4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -2.9 | -3.8 |
|  | [[4EGI-1 (drug)]] 5 µM |  | -2.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | threonyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.3 — chr5:33,440,696-33,468,091 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, UV_RESPONSE_UP |
| Reactome | 3 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P26639](https://www.uniprot.org/uniprotkb/P26639) (Threonine--tRNA ligase 1, cytoplasmic):

> Catalyzes the attachment of threonine to tRNA(Thr) in a two-step reaction: threonine is first activated by ATP to form Thr-AMP and then transferred to the acceptor end of tRNA(Thr). Also edits incorrectly charged tRNA(Thr) via its editing domain, at the post-transfer stage (By similarity).

**Summary**, from NCBI Gene [6897](https://www.ncbi.nlm.nih.gov/gene/6897):

> Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Threonyl-tRNA synthetase belongs to the class-II aminoacyl-tRNA synthetase family [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11572](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11572) · Entrez [6897](https://www.ncbi.nlm.nih.gov/gene/6897) · UniProt [P26639](https://www.uniprot.org/uniprotkb/P26639) · Ensembl [ENSG00000113407](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113407)

## Data

Gene col 3462: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3462); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3462, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3462]; `tensor/DDL_lfc|DDL_z.npy` [3462]; `embed/gene_vectors.npy` [3462]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3462 or target_col == 3462). Every well: [[TARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
