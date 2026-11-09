---
symbol: "TSTD3"
type: "gene"
col: 15930
ensembl_id: "ENSG00000279170"
name: "thiosulfate sulfurtransferase like domain containing 3, pseudogene"
location: "6q16.2"
module: 46
arm: "+"
pooled_cpm: 29.87
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 20
n_dd_up_clean: 14
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# TSTD3

*thiosulfate sulfurtransferase like domain containing 3, pseudogene* — 6q16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +20.5, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.420× (z -15.5, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFF-DT]] (+0.79, fdr 1e-05), [[LINC00938]] (+0.78, fdr 7e-06), [[PNISR-AS1]] (+0.77, fdr 3e-05); moves opposite to [[STUB1]] (-0.67, fdr 0.001, ⚠ one half only (not replicated)), [[EDA]] (-0.65, fdr 4e-05), [[SIPA1]] (-0.63, fdr 1e-04), [[GPRIN1]] (-0.62, fdr 9e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +20.5 | 0e+00 | 43/47 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +10.1 | 2e-21 | 34/47 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +8.8 | 4e-16 | 34/48 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.39×** | +8.4 | 5e-15 | 33/48 (NCI-H2347, J82, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +6.3 | 4e-08 | 32/48 (C-33 A, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.6 | 2e-06 | 25/46 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.6 | 2e-06 | 23/48 (A-172, HOP62, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.21×** | +5.0 | 5e-05 | 21/48 (A498, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +4.9 | 5e-05 | 22/47 (SW48, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 8e-04 | 19/48 (SW480, HT-29, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.002 | 15/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.003 | 20/47 (SW480, SW48, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.005 | 10/47 (J82, KATO III, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.019 | 10/47 (SW 900, C-33 A, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.022 | 13/48 (SW480, A-427, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.022 | 11/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.059 | 8/47 (LOX-IMVI, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15930.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.420×** | -15.5 | 0e+00 | 47/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.425×** | -15.3 | 0e+00 | 47/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.446×** | -14.5 | 4e-45 | 45/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.600×** | -9.1 | 1e-17 | 40/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.605×** | -9.0 | 3e-17 | 43/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.654×** | -7.3 | 3e-11 | 29/47 (SNU-1, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.501×** | -6.5 | 8e-09 | 27/48 (MIA PaCa-2, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -6.2 | 4e-08 | 6/48 (LoVo, C-33 A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.785×** | -6.1 | 8e-08 | 27/48 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.743×** | -5.3 | 7e-06 | 23/48 (SW480, SNU-1, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.585×** | -5.0 | 3e-05 | 21/48 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.596×** | -4.8 | 6e-05 | 21/48 (AN3 CA, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.753×** | -4.8 | 8e-05 | 21/48 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.765×** | -4.8 | 8e-05 | 22/48 (SNU-1, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.782×** | -4.4 | 5e-04 | 21/47 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.646×** | -4.1 | 0.002 | 15/47 (SHP-77, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.806×** | -3.8 | 0.004 | 19/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.710×** | -3.2 | 0.038 | 11/48 (NCI-H460, H4, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 62.3 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.164× (z -12.1) ⚠ toxic; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.195× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 44.5 | 3 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +13.1) | [[Belinostat (drug)]] 5 µM 0.309× (z -13.1) |
| [[HS-578T (line)]] | alt | 32.4 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.256× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 52.1 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.185× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 33.6 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 30.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.250× (z -13.7) |
| [[PANC-1 (line)]] | alt | 46.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.395× (z -10.6) |
| [[A-172 (line)]] | wt | 31.0 | 2 | 1 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.66× (z +11.0) | [[Belinostat (drug)]] 5 µM 0.243× (z -11.3) |
| [[HOP62 (line)]] | alt | 29.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 32.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 30.5 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.384× (z -9.7) |
| [[A-427 (line)]] | wt | 29.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.54× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -8.6) |
| [[C32 (line)]] | wt | 29.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 29.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.267× (z -10.4) |
| [[SNU-423 (line)]] | alt | 34.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.1) | [[AZD2858 (drug)]] 0.5 µM 0.188× (z -9.8) ⚠ toxic |
| [[A549 (line)]] | wt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -10.1) |
| [[AN3 CA (line)]] | alt | 38.3 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0640× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 30.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 42.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.247× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +12.7) | — |
| [[CHP-212 (line)]] | wt | 23.8 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0803× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 24.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.207× (z -9.0) |
| [[Hs 766T (line)]] | wt | 29.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 29.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +9.5) | — |
| [[J82 (line)]] | alt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.3) | — |
| [[KATO III (line)]] | alt | 25.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.8) | — |
| [[LoVo (line)]] | wt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 27.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 28.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.304× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 41.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 26.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +10.8) | — |
| [[SW48 (line)]] | wt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +8.8) | — |
| [[A498 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFF-DT]] | +0.79 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[LINC00938]] | +0.78 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[PNISR-AS1]] | +0.77 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[ATE1OSP]] | +0.76 | +0.66 / +0.43 | both halves | 4e-05 | same gene group |
| [[SEC24B-AS1]] | +0.75 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[VPS13B-DT]] | +0.74 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[MAILR]] | +0.74 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[C2orf76]] | +0.74 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[DDX59]] | +0.73 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[OXA1L-DT]] | +0.72 | +0.64 / +0.37 | both halves | 8e-05 |  |
| [[PBLD]] | +0.72 | +0.58 / +0.31 | both halves | 2e-04 |  |
| [[FBXW4]] | +0.72 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | -0.67 | -0.51 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[EDA]] | -0.65 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[SIPA1]] | -0.63 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[GPRIN1]] | -0.62 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[GNB1L]] | -0.62 | -0.56 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TSTD3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HOXC8]] | B | HOXC8 activity raises TSTD3's level | lines that do not express HOXC8 (11) vs lines expressing it (39) | 1.36× lower at baseline in the lines without HOXC8 | 0.035 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC6, IRX5 |
| [[TMEM92]] | B | TMEM92 activity lowers TSTD3's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.30× higher at baseline in the lines without TMEM92 | 0.037 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[SHOX2]] | B | SHOX2 activity raises TSTD3's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 1.26× lower at baseline in the lines without SHOX2 | 0.092 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B |
| [[PSMD14-DT]] | C | PSMD14-DT's natural level strengthens TSTD3's drug response | PSMD14-DT's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.08; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.821). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.9, 17.8); signed map (25.3, -14.1). **Vector** length 120, 32.7% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.5 | +20.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +10.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +7.3 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.3 | +5.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +8.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.9 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +5.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.7 | +4.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +1.4 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -8.6 | -15.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -8.4 | -14.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -8.4 | -15.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.9 | -9.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.6 | -9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -6.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -6.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | thiosulfate sulfurtransferase like domain containing 3, pseudogene |
| Locus type | pseudogene |
| Location | 6q16.2 — chr6:99,520,976-99,589,899 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TSTD3 |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

UniProt [H0UI37](https://www.uniprot.org/uniprotkb/H0UI37) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40910) · Entrez [100130890](https://www.ncbi.nlm.nih.gov/gene/100130890) · UniProt [H0UI37](https://www.uniprot.org/uniprotkb/H0UI37) · Ensembl [ENSG00000279170](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000279170)

## Data

Gene col 15930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15930); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15930]; `tensor/DDL_lfc|DDL_z.npy` [15930]; `embed/gene_vectors.npy` [15930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15930 or target_col == 15930). Every well: [[TSTD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSTD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
