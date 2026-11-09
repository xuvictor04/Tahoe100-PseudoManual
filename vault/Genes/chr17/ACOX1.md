---
symbol: "ACOX1"
type: "gene"
col: 8436
ensembl_id: "ENSG00000161533"
name: "acyl-CoA oxidase 1"
location: "17q25.1"
module: 4
arm: "-"
pooled_cpm: 44.79
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ACOX1

*acyl-CoA oxidase 1* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +22.9, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.767× (z -6.8, q 5e-09, down in 27 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.606× (z -6.7, q 5e-09, down in 27 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2A]] (+0.57, fdr 1e-05), [[RC3H1]] (+0.54, fdr 3e-05), [[DVL3]] (+0.54, fdr 1e-04); moves opposite to [[CLYBL]] (-0.58, fdr 2e-05), [[SERBP1]] (-0.56, fdr 8e-05), [[DHODH]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8436.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +22.9 | 0e+00 | 45/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +18.9 | 0e+00 | 42/47 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +13.5 | 2e-39 | 39/47 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +11.7 | 2e-29 | 29/41 (SNU-423, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +11.5 | 1e-28 | 31/45 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +11.3 | 1e-27 | 34/48 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +11.1 | 1e-26 | 32/48 (Panc 03.27, C32, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.30×** | +9.5 | 2e-19 | 30/48 (J82, SW480, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +8.7 | 3e-16 | 30/47 (CFPAC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +8.3 | 4e-15 | 31/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +8.2 | 9e-15 | 35/48 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +8.2 | 9e-15 | 30/48 (PANC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +7.5 | 3e-12 | 27/48 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.33×** | +7.2 | 2e-11 | 29/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.29×** | +6.5 | 2e-09 | 30/48 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +5.2 | 7e-06 | 21/48 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +5.1 | 1e-05 | 21/47 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 9e-04 | 12/48 (PANC-1, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.8 | 0.005 | 20/48 (A-427, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.027 | 14/48 (HT-29, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8436.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.767×** | -6.8 | 5e-09 | 27/48 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -6.7 | 5e-09 | 0/49 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.606×** | -6.7 | 5e-09 | 27/49 (SNU-1, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.776×** | -6.5 | 1e-08 | 24/48 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.625×** | -6.3 | 4e-08 | 23/48 (LS 180, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.882× | -4.5 | 6e-04 | 16/48 (SW480, RPMI-7951, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.852× | -3.9 | 0.007 | 16/47 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.865× | -3.7 | 0.016 | 12/48 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.862× | -3.6 | 0.018 | 14/48 (NCI-H23, Hs 766T, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.875× | -3.4 | 0.037 | 10/47 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.777×** | -3.4 | 0.040 | 12/48 (AN3 CA, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.837× | -3.2 | 0.056 | 13/48 (NCI-H1573, NCI-H1792, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.885× | -3.1 | 0.082 | 12/47 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[Cinacalcet (drug)]] 0.5 µM |  | 0.887× | -3.0 | 0.093 | 7/48 (SW 1088, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8436. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 40.3 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +17.2) | — |
| [[HEC-1-A (line)]] | alt | 29.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 51.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +14.4) | — |
| [[C32 (line)]] | wt | 35.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 29.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 41.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 81.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +14.3) | — |
| [[J82 (line)]] | alt | 23.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 26.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0721× (z -19.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 32.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +15.3) | — |
| [[SK-MEL-2 (line)]] | alt | 33.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.5) | — |
| [[SW1417 (line)]] | alt | 57.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +14.0) | — |
| [[SW480 (line)]] | alt | 64.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +12.9) | — |
| [[A498 (line)]] | wt | 81.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +10.6) | — |
| [[A549 (line)]] | wt | 39.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +12.4) | — |
| [[AN3 CA (line)]] | alt | 42.6 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.140× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 34.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +12.2) | — |
| [[CHP-212 (line)]] | wt | 88.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0693× (z -16.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HOP62 (line)]] | alt | 42.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +12.8) | — |
| [[KATO III (line)]] | alt | 74.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 40.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +16.8) | — |
| [[NCI-H2030 (line)]] | alt | 36.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.7) | — |
| [[RKO (line)]] | wt | 37.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +14.9) | — |
| [[SNU-1 (line)]] | wt | 38.2 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0651× (z -9.2) |
| [[SW 1271 (line)]] | alt | 49.2 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.0794× (z -8.8) |
| [[SW 900 (line)]] | alt | 41.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.5) | — |
| [[A-172 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8436), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2A]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[RC3H1]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[DVL3]] | +0.54 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[ATOSA]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ZNF490]] | +0.52 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[FAM117A]] | +0.52 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[TSTD3]] | +0.52 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[YPEL5]] | +0.51 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[MAN2B1]] | +0.50 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[UNKL]] | +0.49 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[PHYH]] | +0.49 | +0.44 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS; STRING 538 |
| [[PMS2P4-1]] | +0.49 | +0.45 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLYBL]] | -0.58 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[SERBP1]] | -0.56 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[DHODH]] | -0.55 | -0.55 / -0.45 | both halves | 3e-05 | same gene group |
| [[NARS2]] | -0.54 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[SNRPD1]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[POLR1B]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[POLR3B]] | -0.54 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[CENPB]] | -0.52 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[ZHX3]] | -0.52 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[ZNF22]] | -0.52 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[COA1]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[TMEM177]] | -0.52 | -0.37 / -0.43 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.390). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-13.3, -43.7); signed map (-10.3, 10.3). **Vector** length 102, 24.5% of its response variance represented; |z| ≥ 3 in 1,168 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +5.2 | +9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +22.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +13.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.4 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +18.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +8.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[Entrectinib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.7 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -4.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.2 | -6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.5 | -6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.3 | -6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.5 | -0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.2 | -3.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | -3.1 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA oxidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,941,507-75,979,177 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PALMCOX |
| Gene groups (HGNC) | Flavoproteins; Acyl-CoA oxidase family |
| Hallmark sets | PEROXISOME, FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM, ADIPOGENESIS |
| Reactome | 11 pathways, smallest: TYSND1 cleaves peroxisomal proteins; Beta-oxidation of very long chain fatty acids; alpha-linolenic (omega3) and linoleic (omega6) acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15067](https://www.uniprot.org/uniprotkb/Q15067) (Peroxisomal acyl-coenzyme A oxidase 1):

> Involved in the initial and rate-limiting step of peroxisomal beta-oxidation of straight-chain saturated and unsaturated very-long-chain fatty acids (VLCFAs). Catalyzes the desaturation of fatty acyl-CoAs that have a saturated bond between C2 and C3 (2,3-saturated acyl-CoA) to 2-trans-enoyl-CoAs ((2E)-enoyl-CoAs), and donates electrons directly to molecular oxygen (O(2)), thereby producing hydrogen peroxide (H(2)O(2)). May play a role in peroxisomal beta-oxidation step in polyunsaturated fatty …

**Summary**, from NCBI Gene [51](https://www.ncbi.nlm.nih.gov/gene/51):

> The protein encoded by this gene is the first enzyme of the fatty acid beta-oxidation pathway, which catalyzes the desaturation of acyl-CoAs to 2-trans-enoyl-CoAs. It donates electrons directly to molecular oxygen, thereby producing hydrogen peroxide. Defects in this gene result in pseudoneonatal adrenoleukodystrophy, a disease that is characterized by accumulation of very long chain fatty acids. Alternatively spliced transcript variants encoding different isoforms have been identified. …

**Accessions** — [HGNC:119](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:119) · Entrez [51](https://www.ncbi.nlm.nih.gov/gene/51) · UniProt [Q15067](https://www.uniprot.org/uniprotkb/Q15067) · Ensembl [ENSG00000161533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161533)

## Data

Gene col 8436: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8436); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8436, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8436]; `tensor/DDL_lfc|DDL_z.npy` [8436]; `embed/gene_vectors.npy` [8436]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8436 or target_col == 8436). Every well: [[ACOX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACOX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
