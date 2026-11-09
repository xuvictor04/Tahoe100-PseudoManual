---
symbol: "CDCA7L"
type: "gene"
col: 8980
ensembl_id: "ENSG00000164649"
name: "cell division cycle associated 7 like"
location: "7p15.3"
module: 6
arm: "+"
pooled_cpm: 32.88
n_lines_expressing: 42
n_dd_up: 23
n_dd_down: 23
n_dd_up_clean: 17
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 6
direction_downstream: 11
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CDCA7L

*cell division cycle associated 7 like* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.60× (z +15.1, q 0e+00, up in 35 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.612× (z -11.0, q 2e-25, down in 30 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THEM6]] (+0.70, fdr 7e-06), [[PRIM1]] (+0.68, fdr 7e-06), [[PARP1]] (+0.68, fdr 1e-05); moves opposite to [[DENND6A-AS1]] (-0.61, fdr 1e-04), [[GTF2IRD2]] (-0.61, fdr 1e-05), [[CLDN18]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PODXL2]] → it (grade B ⚠); 11 go from it, the strongest it → [[C20orf27]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.60×** | +15.1 | 0e+00 | 35/40 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.55×** | +14.9 | 0e+00 | 38/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.64×** | +14.8 | 0e+00 | 27/32 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.32×** | +13.4 | 1e-38 | 37/40 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +13.1 | 3e-37 | 38/40 (PANC-1, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.94×** | +10.5 | 6e-24 | 36/40 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.75×** | +8.9 | 4e-17 | 27/38 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +7.5 | 4e-12 | 32/40 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.63×** | +7.1 | 6e-11 | 20/36 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.34×** | +7.1 | 9e-11 | 31/40 (PANC-1, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +5.2 | 1e-05 | 22/40 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 4e-04 | 13/40 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.32×** | +4.4 | 4e-04 | 20/38 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.002 | 16/40 (SK-MEL-2, PANC-1, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.19× | +4.0 | 0.002 | 14/40 (PANC-1, Panc 03.27, …) | top dose only |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.008 | 12/40 (SHP-77, SW1417, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.013 | 12/40 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.027 | 11/40 (SW 900, NCI-H460, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.052 | 8/40 (A-172, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.052 | 11/39 (LOX-IMVI, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8980.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.612×** | -11.0 | 2e-25 | 30/40 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -9.5 | 6e-19 | 31/40 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.576×** | -8.8 | 3e-16 | 27/39 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.622×** | -7.6 | 6e-12 | 26/40 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.620×** | -7.2 | 8e-11 | 26/40 (HT-29, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.639×** | -6.9 | 6e-10 | 24/39 (A-427, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.461×** | -6.4 | 9e-09 | 25/40 (SW480, HCT15, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.468×** | -6.3 | 2e-08 | 24/40 (A-427, NCI-H23, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.666×** | -6.1 | 5e-08 | 21/40 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.687×** | -5.8 | 5e-07 | 23/40 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.700×** | -5.7 | 8e-07 | 26/40 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.722×** | -5.2 | 1e-05 | 21/40 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.547×** | -5.0 | 2e-05 | 20/40 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.759×** | -4.2 | 1e-03 | 16/39 (A549, J82, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -3.8 | 0.005 | 17/39 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.795×** | -3.7 | 0.009 | 13/40 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.794×** | -3.5 | 0.017 | 15/39 (SW48, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.809×** | -3.4 | 0.023 | 15/40 (SW48, HT-29, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.7 | 5 (2 ⚠) | 3 | [[Panobinostat (drug)]] 5 µM 3.82× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -14.2) |
| [[PANC-1 (line)]] | alt | 33.7 | 5 (1 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.57× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -11.2) |
| [[SW480 (line)]] | alt | 86.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -15.8) |
| [[RKO (line)]] | wt | 57.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.4) |
| [[A-172 (line)]] | wt | 47.3 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 3.15× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -9.5) |
| [[LoVo (line)]] | wt | 20.1 | 4 (1 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 2.73× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -8.5) |
| [[HOP62 (line)]] | alt | 17.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.91× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 35.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.270× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 28.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0884× (z -16.5) |
| [[SW48 (line)]] | wt | 78.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -15.0) |
| [[A-427 (line)]] | wt | 73.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -15.8) |
| [[A549 (line)]] | wt | 10.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.48× (z +9.5) | — |
| [[H4 (line)]] | wt | 46.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.83× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 37.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -13.3) |
| [[Hs 766T (line)]] | wt | 38.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -8.7) |
| [[J82 (line)]] | alt | 71.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.65× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 46.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -13.2) |
| [[A498 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.283× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 63.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 16.8 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0600× (z -12.7) |
| [[KATO III (line)]] | alt | 37.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 46.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -15.7) |
| [[NCI-H2347 (line)]] | alt | 15.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[SW1417 (line)]] | alt | 52.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.7) |
| [[AN3 CA (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.76 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.13 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.12 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM6]] | +0.70 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PRIM1]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[PARP1]] | +0.68 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SSX2IP]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[GGCT]] | +0.66 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SSRP1]] | +0.66 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[HLTF]] | +0.66 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[AIF1L]] | +0.66 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PHF6]] | +0.66 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PODXL2]] | +0.64 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[PSIP1]] | +0.64 | +0.54 / +0.63 | both halves | 1e-05 | STRING 900 |
| [[TMEM106C]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND6A-AS1]] | -0.61 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[GTF2IRD2]] | -0.61 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[CLDN18]] | -0.60 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ZNF425]] | -0.60 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[SPATA1]] | -0.60 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[USP34-DT]] | -0.60 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[ZNF547]] | -0.59 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[NOXRED1]] | -0.59 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[LINC01004]] | -0.59 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[GSK3B-DT]] | -0.59 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[NMNAT1]] | -0.59 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ZNF213-AS1]] | -0.59 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | PODXL2 activity raises CDCA7L's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.78× lower at baseline in the lines without PODXL2 | 0.024 | ⚠ within organs, on part of the lines |
| [[LRRC20]] | B | LRRC20 activity raises CDCA7L's level | lines that do not express LRRC20 (5) vs lines expressing it (45) | 2.86× lower at baseline in the lines without LRRC20 | 0.049 | ⚠ within organs, on part of the lines; also absent: MCM2, MCM10, SEMA4D; maybe low, not absent |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity lowers CDCA7L's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.47× higher at baseline in the lines without ZNF341-AS1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[HOOK1]] | B | HOOK1 activity weakens CDCA7L's drug response | lines that do not express HOOK1 (16) vs lines expressing it (24) | the lines without HOOK1 respond 1.17× as strongly (z diff -0.89); strongest at Panobinostat 5 µM: 3.50x vs 1.97x (z diff -3.0) | 0.084 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1; target measured in part of the lines; artifact flags |
| [[S100A13]] | C | S100A13 activity lowers CDCA7L's level | lines that do not express S100A13 (4) vs lines expressing it (46) | 1.41× higher at baseline in the lines without S100A13 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CASP4, SP100, KIFC3; maybe low, not absent; its own permutation p |
| [[LRRCC1]] | C | LRRCC1 activity raises CDCA7L's level | lines that do not express LRRCC1 (4) vs lines expressing it (46) | 3.72× lower at baseline in the lines without LRRCC1 | 0.062 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C20orf27]] | B | CDCA7L activity raises C20orf27's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without CDCA7L | 0.020 | ⚠ within organs, on part of the lines |
| [[TMEM245]] | B | CDCA7L activity raises TMEM245's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without CDCA7L | 0.024 | ⚠ within organs, on part of the lines |
| [[AIG1]] | B | CDCA7L activity raises AIG1's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without CDCA7L | 0.042 | ⚠ within organs, on part of the lines |
| [[GGCT]] | B | CDCA7L activity raises GGCT's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.35× lower at baseline in the lines without CDCA7L | 0.045 | ⚠ within organs, on part of the lines |
| [[MTHFD1]] | B | CDCA7L activity raises MTHFD1's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.30× lower at baseline in the lines without CDCA7L | 0.050 | ⚠ within organs, on part of the lines |
| [[MSH5]] | B | CDCA7L activity raises MSH5's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.29× lower at baseline in the lines without CDCA7L | 0.051 | ⚠ within organs, on part of the lines |
| [[PRIM1]] | B | CDCA7L activity raises PRIM1's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.49× lower at baseline in the lines without CDCA7L | 0.058 | ⚠ within organs, on part of the lines |
| [[TMEM106C]] | B | CDCA7L activity raises TMEM106C's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.30× lower at baseline in the lines without CDCA7L | 0.066 | ⚠ within organs, on part of the lines |
| [[DEK]] | B | CDCA7L activity raises DEK's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.13× lower at baseline in the lines without CDCA7L | 0.071 | ⚠ within organs, on part of the lines |
| [[FYCO1]] | B | CDCA7L activity raises FYCO1's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.19× lower at baseline in the lines without CDCA7L | 0.071 | ⚠ within organs, on part of the lines |
| [[ANKRD28]] | B | CDCA7L activity raises ANKRD28's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without CDCA7L | 0.093 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-28.0, -36.7); signed map (-33.2, -35.6). **Vector** length 115, 32.4% of its response variance represented; |z| ≥ 3 in 1,090 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +13.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.9 | +14.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.8 | +10.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.8 | +13.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.7 | +15.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.2 | +7.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +5.2 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.2 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -11.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.8 | -6.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -3.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle associated 7 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:21,900,899-21,945,903 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAM2, R1, JPO2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GN5](https://www.uniprot.org/uniprotkb/Q96GN5) (Cell division cycle-associated 7-like protein):

> Plays a role in transcriptional regulation as a repressor that inhibits monoamine oxidase A (MAOA) activity and gene expression by binding to the promoter. Plays an important oncogenic role in mediating the full transforming effect of MYC in medulloblastoma cells. Involved in apoptotic signaling pathways; May act downstream of P38-kinase and BCL-2, but upstream of CASP3/caspase-3 as well as CCND1/cyclin D1 and E2F1.

**Summary**, from NCBI Gene [55536](https://www.ncbi.nlm.nih.gov/gene/55536):

> Acts upstream of or within positive regulation of cell population proliferation. Located in cytosol; fibrillar center; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30777](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30777) · Entrez [55536](https://www.ncbi.nlm.nih.gov/gene/55536) · UniProt [Q96GN5](https://www.uniprot.org/uniprotkb/Q96GN5) · Ensembl [ENSG00000164649](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164649)

## Data

Gene col 8980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8980); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8980]; `tensor/DDL_lfc|DDL_z.npy` [8980]; `embed/gene_vectors.npy` [8980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8980 or target_col == 8980). Every well: [[CDCA7L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDCA7L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
