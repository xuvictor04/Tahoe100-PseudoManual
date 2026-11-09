---
symbol: "PPCDC"
type: "gene"
col: 6196
ensembl_id: "ENSG00000138621"
name: "phosphopantothenoylcysteine decarboxylase"
location: "15q24.2"
module: 5
arm: "+"
pooled_cpm: 33.68
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 23
n_dd_up_clean: 14
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PPCDC

*phosphopantothenoylcysteine decarboxylase* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.75× (z +8.5, q 1e-14, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.432× (z -17.8, q 0e+00, down in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.427× (z -12.8, q 5e-35, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRP7BP-1]] (+0.48, fdr 2e-04), [[ZNF551]] (+0.47, fdr 3e-05), [[RRP7A]] (+0.47, fdr 3e-04); moves opposite to [[TAB3]] (-0.52, fdr 4e-05), [[PHYH]] (-0.51, fdr 6e-05), [[NADK2]] (-0.50, fdr 7e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ARHGAP8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6196.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +8.5 | 1e-14 | 36/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +8.3 | 2e-14 | 36/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +7.7 | 2e-12 | 36/48 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 2e-04 | 23/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.38×** | +4.7 | 3e-04 | 23/45 (NCI-H1573, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.35×** | +4.6 | 4e-04 | 20/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +4.4 | 8e-04 | 19/48 (NCI-H2347, NCI-H460, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.002 | 16/48 (NCI-H1792, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +3.8 | 0.009 | 20/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.61×** | +3.8 | 0.010 | 11/47 (A-427, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.012 | 19/48 (A498, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.012 | 14/47 (HepG2/C3A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.018 | 16/48 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.034 | 12/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.043 | 17/48 (hTERT-HPNE, SW 900, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.074 | 14/47 (CFPAC-1, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.46×** | +3.0 | 0.085 | 7/47 (NCI-H2347, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6196.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.432×** | -17.8 | 0e+00 | 42/47 (RKO, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.421×** | -13.0 | 6e-36 | 35/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.427×** | -12.8 | 5e-35 | 37/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.488×** | -10.3 | 7e-23 | 39/48 (COLO 205, PANC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.327×** | -8.7 | 3e-16 | 40/49 (PANC-1, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.581×** | -8.1 | 5e-14 | 30/47 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.617×** | -7.2 | 5e-11 | 31/48 (SW480, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -7.2 | 5e-11 | 32/47 (COLO 205, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.650×** | -6.4 | 8e-09 | 31/48 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.470×** | -5.9 | 2e-07 | 30/46 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.678×** | -5.8 | 3e-07 | 25/46 (HCT15, NCI-H23, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.670×** | -5.7 | 4e-07 | 28/47 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.706×** | -5.2 | 9e-06 | 28/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.707×** | -5.2 | 1e-05 | 28/48 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.717×** | -5.0 | 3e-05 | 25/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.768×** | -3.7 | 0.007 | 18/48 (COLO 205, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.850× | -3.4 | 0.019 | 13/48 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.801×** | -3.2 | 0.041 | 21/48 (HEC-1-A, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.803×** | -3.1 | 0.043 | 11/48 (NCI-H2347, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.865× | -3.0 | 0.057 | 6/48 (HOP62, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6196. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.1 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -19.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -13.5) |
| [[SW480 (line)]] | alt | 34.9 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -11.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.361× (z -10.5) |
| [[COLO 205 (line)]] | alt | 75.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -18.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.295× (z -10.1) |
| [[LoVo (line)]] | wt | 40.5 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.286× (z -12.1) |
| [[LS 180 (line)]] | wt | 41.8 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.109× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 59.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -12.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -9.5) |
| [[KATO III (line)]] | alt | 51.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -14.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 22.0 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.250× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 40.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -14.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HOP62 (line)]] | alt | 21.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -8.8) |
| [[A-427 (line)]] | wt | 26.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[C-33 A (line)]] | alt | 79.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[C32 (line)]] | wt | 19.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -9.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[CFPAC-1 (line)]] | alt | 95.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -14.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[H4 (line)]] | wt | 25.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0840× (z -11.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HCT15 (line)]] | alt | 57.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0886× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HT-29 (line)]] | alt | 53.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -14.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H23 (line)]] | alt | 40.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 18.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.274× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 35.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -12.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[BT-474 (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -10.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HS-578T (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H1792 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -13.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H2347 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -8.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RKO (line)]] | wt | 27.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -20.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SHP-77 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 5 µM 0.0691× (z -9.1) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SNU-1 (line)]] | wt | 40.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0578× (z -8.6) |
| [[A-172 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6196), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7BP-1]] | +0.48 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[ZNF551]] | +0.47 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[RRP7A]] | +0.47 | +0.29 / +0.55 | both halves | 3e-04 |  |
| [[CBX6]] | +0.46 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[HEXD]] | +0.46 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[NAA40]] | +0.45 | +0.37 / +0.36 | both halves | 1e-04 |  |
| [[LSM12]] | +0.45 | +0.32 / +0.36 | both halves | 2e-04 |  |
| [[TMEM241]] | +0.44 | +0.28 / +0.46 | both halves | 3e-04 |  |
| [[SLC39A3]] | +0.44 | +0.20 / +0.46 | both halves | 7e-04 |  |
| [[ARHGAP8]] | +0.44 | +0.22 / +0.43 | both halves | 6e-04 |  |
| [[CLYBL]] | +0.44 | +0.39 / +0.37 | both halves | 8e-05 |  |
| [[SCART1]] | +0.43 | +0.38 / +0.40 | both halves | 6e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAB3]] | -0.52 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[PHYH]] | -0.51 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[NADK2]] | -0.50 | -0.38 / -0.46 | both halves | 7e-05 | pathway: Metabolism of vitamins and cofactors |
| [[MRPL30]] | -0.50 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[FBXO8]] | -0.48 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[ACADSB]] | -0.48 | -0.44 / -0.43 | both halves | 4e-05 | same gene group |
| [[MTR]] | -0.48 | -0.33 / -0.50 | both halves | 1e-04 | pathway: Metabolism of vitamins and cofactors |
| [[ZNF563]] | -0.46 | -0.35 / -0.26 | both halves | 4e-04 |  |
| [[TNKS2]] | -0.45 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[PRDX6]] | -0.45 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[PRCP]] | -0.45 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[TOP2B]] | -0.45 | -0.38 / -0.46 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP8]] | B | ARHGAP8 activity raises PPCDC's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 1.71× lower at baseline in the lines without ARHGAP8 | 0.017 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.146). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-21.8, 21.6); signed map (-16.2, -20.9). **Vector** length 77.6, 17.6% of its response variance represented; |z| ≥ 3 in 1,193 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.8 | +1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +3.5 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +8.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +8.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.0 | -7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -6.7 | -17.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -5.9 | -5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -5.6 | -3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -3.2 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.2 | -0.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.2 | -0.8 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphopantothenoylcysteine decarboxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:75,023,586-75,117,462 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDS018, FLJ14585 |
| Gene groups (HGNC) | Flavoproteins; Decarboxylases |
| Reactome | 4 pathways, smallest: Coenzyme A biosynthesis; Vitamin B5 (pantothenate) metabolism; Metabolism of water-soluble vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CD2](https://www.uniprot.org/uniprotkb/Q96CD2) (Phosphopantothenoylcysteine decarboxylase):

> Catalyzes the decarboxylation of the cysteine moiety of 4-phosphopantothenoylcysteine to form 4'-phosphopantotheine and this reaction forms part of the biosynthesis of coenzyme A.

**Summary**, from NCBI Gene [60490](https://www.ncbi.nlm.nih.gov/gene/60490):

> Biosynthesis of coenzyme A (CoA) from pantothenic acid (vitamin B5) is an essential universal pathway in prokaryotes and eukaryotes. PPCDC (EC 4.1.1.36), one of the last enzymes in this pathway, converts phosphopantothenoylcysteine to 4-prime-phosphopantetheine (Daugherty et al., 2002 [PubMed 11923312]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28107](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28107) · Entrez [60490](https://www.ncbi.nlm.nih.gov/gene/60490) · UniProt [Q96CD2](https://www.uniprot.org/uniprotkb/Q96CD2) · Ensembl [ENSG00000138621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138621)

## Data

Gene col 6196: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6196); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6196, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6196]; `tensor/DDL_lfc|DDL_z.npy` [6196]; `embed/gene_vectors.npy` [6196]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6196 or target_col == 6196). Every well: [[PPCDC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPCDC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
