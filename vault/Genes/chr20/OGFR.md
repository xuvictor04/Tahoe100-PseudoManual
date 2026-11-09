---
symbol: "OGFR"
type: "gene"
col: 687
ensembl_id: "ENSG00000060491"
name: "opioid growth factor receptor"
location: "20q13.33"
module: 70
arm: "+"
pooled_cpm: 42.44
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 12
direction_downstream: 8
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# OGFR

*opioid growth factor receptor* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.86× (z +9.8, q 4e-20, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.399× (z -14.0, q 8e-42, down in 31 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.554× (z -13.0, q 6e-36, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHFL]] (+0.76, fdr 7e-06), [[UBE2L6]] (+0.75, fdr 7e-06), [[PSMB9]] (+0.74, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[JAK2]] → it (grade B ⚠); 8 go from it, the strongest it → [[TRIM14]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 687.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.86×** | +9.8 | 4e-20 | 42/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.68×** | +8.2 | 1e-13 | 37/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +7.9 | 8e-13 | 39/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +6.0 | 4e-07 | 31/48 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +5.8 | 9e-07 | 28/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **1.37×** | +5.0 | 5e-05 | 29/47 (Hs 766T, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.007 | 22/48 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.011 | 23/47 (RPMI-7951, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.034 | 17/47 (H4, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.2 | 0.088 | 17/46 (HT-29, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 5 µM |  | 1.15× | +3.1 | 0.10 | 15/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | 1.44× | +3.0 | 0.12 | 14/48 (CFPAC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 687.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.399×** | -14.0 | 8e-42 | 31/42 (A549, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.554×** | -13.0 | 6e-36 | 39/48 (LS 180, SW1417, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.475×** | -11.7 | 4e-29 | 39/46 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.524×** | -9.4 | 9e-19 | 35/43 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.589×** | -8.4 | 5e-15 | 36/48 (A549, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.602×** | -8.1 | 7e-14 | 39/48 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.715×** | -7.3 | 3e-11 | 31/48 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.655×** | -6.7 | 1e-09 | 29/48 (NCI-H23, A549, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.752×** | -6.2 | 4e-08 | 28/47 (NCI-H1792, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.747×** | -4.6 | 2e-04 | 23/48 (A549, SNU-423, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.750×** | -4.6 | 3e-04 | 26/48 (LoVo, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.838× | -3.8 | 0.006 | 19/48 (A549, C-33 A, …) | rises with dose | low cells (technical?) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.791×** | -3.7 | 0.008 | 22/48 (A549, NCI-H23, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.793×** | -3.7 | 0.009 | 20/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.847× | -3.7 | 0.009 | 22/48 (A-427, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.800×** | -3.5 | 0.013 | 18/48 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.802×** | -3.5 | 0.014 | 18/48 (C-33 A, RPMI-7951, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.855× | -3.5 | 0.015 | 21/48 (A549, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.830×** | -2.9 | 0.092 | 14/47 (NCI-H661, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 687. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 66.9 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -11.6) |
| [[A549 (line)]] | wt | 47.8 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0678× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.293× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 66.7 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.350× (z -9.8) |
| [[PANC-1 (line)]] | alt | 21.1 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.05× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -11.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 41.1 | 3 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.59× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -8.8) |
| [[A498 (line)]] | wt | 44.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 59.2 | 1 | 3 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.90× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -12.8) |
| [[RPMI-7951 (line)]] | alt | 76.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 46.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.340× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 36.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -12.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 59.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -11.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 24.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.383× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 59.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -18.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 85.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0757× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 50.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -12.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -14.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 38.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 60.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -13.4) |
| [[SW1417 (line)]] | alt | 98.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -14.4) |
| [[SW480 (line)]] | alt | 37.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -10.5) |
| [[C32 (line)]] | wt | 28.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -8.6) |
| [[CHP-212 (line)]] | wt | 40.4 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.104× (z -9.2) |
| [[HS-578T (line)]] | alt | 55.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -10.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 37.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0878× (z -13.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 25.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -14.6) |
| [[RKO (line)]] | wt | 48.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 48.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -12.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 49.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -12.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 21.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -8.5) |
| [[AN3 CA (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 687), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHFL]] | +0.76 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[UBE2L6]] | +0.75 | +0.65 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PSMB9]] | +0.74 | +0.63 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[GSDMD]] | +0.74 | +0.48 / +0.81 | both halves | 2e-05 | **novel candidate** |
| [[ISG15]] | +0.73 | +0.52 / +0.79 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[OAS1]] | +0.68 | +0.54 / +0.74 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[APOL3]] | +0.67 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[GBP4]] | +0.67 | +0.62 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IRF7]] | +0.67 | +0.39 / +0.75 | both halves | 6e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[APOL2]] | +0.67 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[SLC15A3]] | +0.67 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[SP140L]] | +0.67 | +0.57 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAK2]] | B | JAK2 activity raises OGFR's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[IFI6]] | B | IFI6 activity raises OGFR's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without IFI6 | 0.043 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity raises OGFR's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without OAS2 | 0.044 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[OAS1]] | B | OAS1 activity raises OGFR's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without OAS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IFI44L]] | B | IFI44L activity raises OGFR's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.30× lower at baseline in the lines without IFI44L | 0.049 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[BATF2]] | B | BATF2 activity raises OGFR's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.28× lower at baseline in the lines without BATF2 | 0.062 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises OGFR's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.36× lower at baseline in the lines without MX1 | 0.088 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[CD5L]] | B | CD5L activity raises OGFR's level | lines that do not express CD5L (23) vs lines expressing it (27) | 1.34× lower at baseline in the lines without CD5L | 0.094 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[PARP9]] | B | PARP9 activity raises OGFR's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without PARP9 | 0.096 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[SHFL]] | C | SHFL's natural level strengthens OGFR's drug response | SHFL's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.57; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[EIF2AK2]] | C | EIF2AK2's natural level strengthens OGFR's drug response | EIF2AK2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.56; direction not clear | 0.062 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[TRIM14]] | C | TRIM14's natural level strengthens OGFR's drug response | TRIM14's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.73; direction not clear | 0.083 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM14]] | C | OGFR's natural level strengthens TRIM14's drug response | OGFR's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.63; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | OGFR's natural level strengthens HELZ2's drug response | OGFR's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.60; direction not clear | 0.007 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | OGFR's natural level strengthens ADAR's drug response | OGFR's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.48; direction not clear | 0.014 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | OGFR's natural level strengthens PARP12's drug response | OGFR's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.55; direction not clear | 0.027 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PML]] | C | OGFR's natural level strengthens PML's drug response | OGFR's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.58; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT1]] | C | OGFR's natural level strengthens IFIT1's drug response | OGFR's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.59; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP14]] | C | OGFR's natural level strengthens PARP14's drug response | OGFR's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.44; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SP100]] | C | OGFR's natural level strengthens SP100's drug response | OGFR's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.47; direction not clear | 0.099 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.7, 51.1); signed map (63.7, 29.0). **Vector** length 113, 31.2% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing-Cross presentation* (reactome, mean cos +0.50 to 14); *Interferon gamma signaling* (reactome, mean cos +0.52 to 13); *ER-Phagosome pathway* (reactome, mean cos +0.51 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +8.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | +4.7 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.6 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.2 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.5 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.2 | -11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.5 | -14.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.3 | -7.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.9 | -3.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.6 | -4.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -3.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | opioid growth factor receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,804,835-62,814,000 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 7-60 |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZT2](https://www.uniprot.org/uniprotkb/Q9NZT2) (Opioid growth factor receptor):

> Receptor for opioid growth factor (OGF), also known as Met-enkephalin. Seems to be involved in growth regulation.

**Summary**, from NCBI Gene [11054](https://www.ncbi.nlm.nih.gov/gene/11054):

> The protein encoded by this gene is a receptor for opioid growth factor (OGF), also known as [Met(5)]-enkephalin. OGF is a negative regulator of cell proliferation and tissue organization in a variety of processes. The encoded unbound receptor for OGF has been localized to the outer nuclear envelope, where it binds OGF and is translocated into the nucleus. The coding sequence of this gene contains a polymorphic region of 60 nt tandem imperfect repeat units. Several transcripts containing …

**Accessions** — [HGNC:15768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15768) · Entrez [11054](https://www.ncbi.nlm.nih.gov/gene/11054) · UniProt [Q9NZT2](https://www.uniprot.org/uniprotkb/Q9NZT2) · Ensembl [ENSG00000060491](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060491)

## Data

Gene col 687: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 687); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 687, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 687]; `tensor/DDL_lfc|DDL_z.npy` [687]; `embed/gene_vectors.npy` [687]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 687 or target_col == 687). Every well: [[OGFR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OGFR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
