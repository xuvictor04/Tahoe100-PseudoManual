---
symbol: "RNMT"
type: "gene"
col: 2162
ensembl_id: "ENSG00000101654"
name: "RNA guanine-7 methyltransferase"
location: "18p11.21"
module: 105
arm: "+"
pooled_cpm: 192.31
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 24
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# RNMT

*RNA guanine-7 methyltransferase* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.93× (z +9.2, q 2e-17, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.534× (z -8.4, q 2e-14, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.757× (z -5.5, q 8e-06, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKRIP1]] (+0.74, fdr 7e-06), [[BNIP3L]] (+0.74, fdr 7e-06), [[FAM210A]] (+0.73, fdr 7e-06, ⚠ same locus), [[ANKRD37]] (+0.73, fdr 7e-06); moves opposite to [[UBE2E3]] (-0.62, fdr 1e-05), [[SMARCB1]] (-0.60, fdr 3e-05), [[ZNF236]] (-0.60, fdr 4e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2162.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.93×** | +9.2 | 2e-17 | 42/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.04×** | +8.1 | 1e-13 | 44/49 (NCI-H23, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +7.9 | 4e-13 | 38/48 (A-427, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +6.8 | 1e-09 | 38/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.33×** | +6.2 | 7e-08 | 45/48 (SHP-77, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +6.1 | 1e-07 | 38/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.27×** | +6.0 | 2e-07 | 35/48 (HS-578T, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +5.3 | 7e-06 | 32/38 (SK-MEL-2, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +5.0 | 3e-05 | 34/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Terfenadine (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.005 | 24/48 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.26×** | +3.3 | 0.054 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2162.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.534×** | -8.4 | 2e-14 | 42/44 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.613×** | -6.8 | 2e-09 | 41/49 (RPMI-7951, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.757×** | -5.5 | 8e-06 | 38/48 (SNU-423, HepG2/C3A, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.704×** | -4.7 | 3e-04 | 39/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.733×** | -4.2 | 0.003 | 29/48 (HEC-1-A, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.744×** | -4.1 | 0.003 | 39/48 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.746×** | -3.9 | 0.005 | 29/47 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.755×** | -3.9 | 0.005 | 38/48 (H4, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.755×** | -3.9 | 0.005 | 36/48 (NCI-H1573, SW 1271, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.757×** | -3.7 | 0.010 | 27/47 (BT-474, HCT15, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.773×** | -3.6 | 0.016 | 33/48 (LOX-IMVI, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.774×** | -3.6 | 0.016 | 33/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.779×** | -3.5 | 0.021 | 33/49 (HOP62, A-172, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.780×** | -3.5 | 0.021 | 28/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.783×** | -3.4 | 0.024 | 28/49 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.849× | -3.2 | 0.039 | 18/48 (NCI-H661, A498, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.798×** | -3.2 | 0.046 | 28/49 (H4, A-172, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.799×** | -3.1 | 0.046 | 29/49 (H4, LS 180, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.801×** | -3.1 | 0.048 | 25/48 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.659×** | -3.1 | 0.056 | 23/48 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2162. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 145 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +21.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +15.5) | — |
| [[HT-29 (line)]] | alt | 199 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 210 | 2 (1 ⚠) | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.12× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -13.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 241 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.14× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -10.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 166 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +11.1) | — |
| [[LoVo (line)]] | wt | 168 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +13.5) | — |
| [[NCI-H1792 (line)]] | alt | 144 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 167 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.35× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -11.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 156 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +11.9) | — |
| [[SNU-1 (line)]] | wt | 222 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.81× (z +11.0) | — |
| [[SW480 (line)]] | alt | 171 | 3 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.58× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -11.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 190 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +13.4) | — |
| [[C32 (line)]] | wt | 320 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.415× (z -9.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 192 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.10× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.400× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 308 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.52× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -9.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 268 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.03× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -12.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 127 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.76× (z +13.6) | — |
| [[HOP62 (line)]] | alt | 426 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -8.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 187 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 292 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.64× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 231 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.01× (z +12.9) | — |
| [[A-427 (line)]] | wt | 205 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.68× (z +13.0) | — |
| [[AN3 CA (line)]] | alt | 192 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.66× (z +11.6) | — |
| [[CHP-212 (line)]] | wt | 253 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -10.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 166 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 193 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.30× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 211 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -8.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 181 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 87.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.26× (z +12.6) | — |
| [[RKO (line)]] | wt | 260 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -8.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 143 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.76× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 215 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -10.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 208 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 270 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 321 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 153 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 218 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 173 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2162), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKRIP1]] | +0.74 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[BNIP3L]] | +0.74 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[FAM210A]] | +0.73 | +0.82 / +0.67 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ANKRD37]] | +0.73 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.73 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.71 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[P4HA1]] | +0.68 | +0.74 / +0.58 | both halves | 8e-06 |  |
| [[SLC35E1]] | +0.68 | +0.75 / +0.57 | both halves | 9e-06 |  |
| [[MXI1]] | +0.67 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[SRP54]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[POM121C]] | +0.67 | +0.80 / +0.55 | both halves | 1e-05 | pathway: HIV Infection |
| [[KDM3A]] | +0.67 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[SAP30-DT]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2E3]] | -0.62 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[SMARCB1]] | -0.60 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[ZNF236]] | -0.60 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[DLG5]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[SGPL1]] | -0.57 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[DHX9]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[CPLANE1]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.775). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.0, -18.6); signed map (-35.0, 25.6). **Vector** length 127, 50.8% of its response variance represented; |z| ≥ 3 in 1,276 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.3 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.7 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.3 | -1.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.7 | +6.2 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.8 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.6 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.3 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.3 | -4.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.9 | -3.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.8 | -2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -3.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.6 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | RNA guanine-7 methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:13,726,660-13,764,556 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RG7MT1, N7-MTase |
| Gene groups (HGNC) | 7BS N7-guanosine RNA methyltransferases; DNA/RNA methyltransferases |
| Hallmark sets | DNA_REPAIR |
| Reactome | 9 pathways, smallest: RNA Pol II CTD phosphorylation and interaction with CE during HIV infection; RNA Pol II CTD phosphorylation and interaction with CE; mRNA Capping |
| Matched by | ensembl_id |

**Function**, from UniProt [O43148](https://www.uniprot.org/uniprotkb/O43148) (mRNA cap guanine-N(7) methyltransferase):

> Catalytic subunit of the mRNA-capping methyltransferase RNMT:RAMAC complex that methylates the N7 position of the added guanosine to the 5'-cap structure of mRNAs. Binds RNA containing 5'-terminal GpppC.

**Summary**, from NCBI Gene [8731](https://www.ncbi.nlm.nih.gov/gene/8731):

> Enables RNA binding activity and mRNA 5'-cap (guanine-N7-)-methyltransferase activity. Involved in 7-methylguanosine mRNA capping. Located in fibrillar center and nucleoplasm. Part of mRNA cap methyltransferase RNMT:RAMAC complex; mRNA capping enzyme complex; and signaling receptor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10075) · Entrez [8731](https://www.ncbi.nlm.nih.gov/gene/8731) · UniProt [O43148](https://www.uniprot.org/uniprotkb/O43148) · Ensembl [ENSG00000101654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101654)

## Data

Gene col 2162: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2162); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2162, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2162]; `tensor/DDL_lfc|DDL_z.npy` [2162]; `embed/gene_vectors.npy` [2162]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2162 or target_col == 2162). Every well: [[RNMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
