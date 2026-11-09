---
symbol: "DKC1"
type: "gene"
col: 5137
ensembl_id: "ENSG00000130826"
name: "dyskerin pseudouridine synthase 1"
location: "Xq28"
module: 18
arm: "+"
pooled_cpm: 79.3
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# DKC1

*dyskerin pseudouridine synthase 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.51× (z +11.9, q 8e-30, up in 46 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.67× (z +6.6, q 3e-09, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.655× (z -7.8, q 4e-12, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDN1]] (+0.83, fdr 7e-06), [[TCOF1]] (+0.82, fdr 7e-06), [[WDR3]] (+0.77, fdr 7e-06); moves opposite to [[ZNF821]] (-0.66, fdr 1e-05), [[ATOSA]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MCOLN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 18 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5137.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.51×** | +11.9 | 8e-30 | 46/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.31×** | +10.4 | 8e-23 | 43/44 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **2.26×** | +10.1 | 1e-21 | 44/47 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.12×** | +9.0 | 4e-17 | 42/45 (KATO III, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.76×** | +7.3 | 3e-11 | 40/48 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +6.6 | 3e-09 | 36/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.66×** | +6.5 | 6e-09 | 32/47 (H4, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.52×** | +5.4 | 4e-06 | 32/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +5.2 | 1e-05 | 36/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **1.48×** | +5.0 | 3e-05 | 38/48 (HT-29, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.44×** | +4.7 | 1e-04 | 26/48 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.98×** | +4.6 | 2e-04 | 34/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.42×** | +4.5 | 3e-04 | 27/48 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 3e-04 | 31/47 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.41×** | +4.4 | 4e-04 | 29/48 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +4.2 | 0.001 | 27/48 (LOX-IMVI, A549, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.82×** | +4.0 | 0.002 | 29/48 (SW 900, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.76×** | +3.8 | 0.004 | 28/48 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.006 | 34/48 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.008 | 26/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.017 | 23/48 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.039 | 13/49 (HT-29, SW 900, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.042 | 23/48 (SK-MEL-2, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.048 | 19/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.062 | 22/48 (MIA PaCa-2, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +2.9 | 0.074 | 22/48 (PANC-1, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5137.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.655×** | -7.8 | 4e-12 | 32/48 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.719×** | -4.1 | 0.010 | 28/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.750×** | -3.8 | 0.033 | 26/47 (SK-MEL-2, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.823×** | -3.6 | 0.042 | 23/48 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.760×** | -3.5 | 0.047 | 22/50 (LoVo, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.758×** | -3.5 | 0.047 | 22/47 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.778× | -3.2 | 0.13 | 22/48 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.636× | -3.1 | 0.15 | 17/49 (A-427, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5137. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 124 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Adagrasib (drug)]] 0.05 µM 0.662× (z -11.8) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.2) |
| [[SW480 (line)]] | alt | 102 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -12.0) |
| [[Hs 766T (line)]] | wt | 57.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HT-29 (line)]] | alt | 65.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.85× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1792 (line)]] | alt | 35.6 | 4 (4 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.17× (z +10.4) ⚠ unreliable plate only | — |
| [[RKO (line)]] | wt | 113 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -16.3) |
| [[SNU-423 (line)]] | alt | 54.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[KATO III (line)]] | alt | 87.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H23 (line)]] | alt | 170 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 53.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A-427 (line)]] | wt | 107 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.502× (z -8.9) |
| [[LoVo (line)]] | wt | 52.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LS 180 (line)]] | wt | 52.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1573 (line)]] | alt | 38.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.57× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 85.9 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.35× (z +10.0) ⚠ toxic; cell-cycle shift, explains ~25% of this change | — |
| [[SW48 (line)]] | wt | 107 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -12.8) |
| [[A-172 (line)]] | wt | 53.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A498 (line)]] | wt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A549 (line)]] | wt | 74.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[AN3 CA (line)]] | alt | 85.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.9) |
| [[BT-474 (line)]] | alt | 54.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.4) |
| [[C-33 A (line)]] | alt | 96.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 32.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.06× (z +12.4) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[HCT15 (line)]] | alt | 64.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HOP62 (line)]] | alt | 68.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -11.3) |
| [[HS-578T (line)]] | alt | 41.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.230× (z -8.8) |
| [[J82 (line)]] | alt | 80.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LOX-IMVI (line)]] | wt | 68.5 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.10× (z +8.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2030 (line)]] | alt | 114 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -9.8) |
| [[PANC-1 (line)]] | alt | 185 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 40.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SW 1271 (line)]] | alt | 63.7 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0677× (z -9.8) ⚠ transcription drop |
| [[SW 900 (line)]] | alt | 49.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.64× (z +9.5) ⚠ unreliable plate only | — |
| [[SW1417 (line)]] | alt | 96.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[AsPC-1 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5137), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDN1]] | +0.83 | +0.84 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[TCOF1]] | +0.82 | +0.81 / +0.81 | both halves | 7e-06 | STRING 612 |
| [[WDR3]] | +0.77 | +0.79 / +0.76 | both halves | 7e-06 | pathway: rRNA modification in the nucleus and cytosol; STRING 670 |
| [[TSEN2]] | +0.77 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[URB1]] | +0.76 | +0.81 / +0.70 | both halves | 7e-06 | same gene group; STRING 659 |
| [[URB2]] | +0.76 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[PUM3]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 | STRING 928 |
| [[PDCD11]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 | pathway: rRNA modification in the nucleus and cytosol; STRING 936 |
| [[MYBBP1A]] | +0.74 | +0.79 / +0.69 | both halves | 7e-06 | STRING 723 |
| [[LYAR]] | +0.74 | +0.74 / +0.72 | both halves | 7e-06 | STRING 626 |
| [[LETM1]] | +0.74 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[CAD]] | +0.73 | +0.78 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF821]] | -0.66 | -0.71 / -0.57 | both halves | 1e-05 |  |
| [[ATOSA]] | -0.63 | -0.62 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN2]] | B | MCOLN2 activity raises DKC1's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.26× lower at baseline in the lines without MCOLN2 | 0.087 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.803). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.5, -37.9); signed map (-5.3, -51.4). **Vector** length 107, 40.2% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.66 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.9 | +7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +3.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | +3.8 | +10.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +4.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.6 | -7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.9 | -2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -3.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.7 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | dyskerin pseudouridine synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,762,742-154,777,689 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XAP101, dyskerin, NAP57, NOLA4, Cbf5; previously DKC |
| Gene groups (HGNC) | H/ACA ribonucleoprotein complex; Pseudouridine synthases; MicroRNA protein coding host genes; Small nucleolar RNA protein coding host genes; Telomerase holoenzyme subunits |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, G2M_CHECKPOINT |
| Reactome | 9 pathways, smallest: Telomere Extension By Telomerase; Extension of Telomeres; rRNA modification in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [O60832](https://www.uniprot.org/uniprotkb/O60832) (H/ACA ribonucleoprotein complex subunit DKC1):

> [Isoform 1]: Catalytic subunit of H/ACA small nucleolar ribonucleoprotein (H/ACA snoRNP) complex, which catalyzes pseudouridylation of rRNA. This involves the isomerization of uridine such that the ribose is subsequently attached to C5, instead of the normal N1. Each rRNA can contain up to 100 pseudouridine ('psi') residues, which may serve to stabilize the conformation of rRNAs. Required for ribosome biogenesis and telomere maintenance. Also required for correct processing or intranuclear …

**Summary**, from NCBI Gene [1736](https://www.ncbi.nlm.nih.gov/gene/1736):

> This gene functions in two distinct complexes. It plays an active role in telomerase stabilization and maintenance, as well as recognition of snoRNAs containing H/ACA sequences which provides stability during biogenesis and assembly into H/ACA small nucleolar RNA ribonucleoproteins (snoRNPs). This gene is highly conserved and widely expressed, and may play additional roles in nucleo-cytoplasmic shuttling, DNA damage response, and cell adhesion. Mutations have been associated with X-linked …

**Accessions** — [HGNC:2890](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2890) · Entrez [1736](https://www.ncbi.nlm.nih.gov/gene/1736) · UniProt [O60832](https://www.uniprot.org/uniprotkb/O60832) · Ensembl [ENSG00000130826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130826)

## Data

Gene col 5137: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5137); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5137, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5137]; `tensor/DDL_lfc|DDL_z.npy` [5137]; `embed/gene_vectors.npy` [5137]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5137 or target_col == 5137). Every well: [[DKC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DKC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
