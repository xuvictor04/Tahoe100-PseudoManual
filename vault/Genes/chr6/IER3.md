---
symbol: "IER3"
type: "gene"
col: 6002
ensembl_id: "ENSG00000137331"
name: "immediate early response 3"
location: "6p21.33"
module: 112
arm: "+"
pooled_cpm: 196.33
n_lines_expressing: 45
n_dd_up: 16
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 29
direction_downstream: 27
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# IER3

*immediate early response 3* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.49× (z +9.0, q 1e-16, up in 41 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.01× (z +7.1, q 1e-10, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.378× (z -7.0, q 2e-09, down in 40 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IER2]] (+0.72, fdr 7e-06), [[CXCL8]] (+0.72, fdr 7e-06), [[GEM]] (+0.71, fdr 7e-06); moves opposite to [[NUP133]] (-0.60, fdr 1e-05), [[DGCR2]] (-0.54, fdr 1e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 29 arrows point to it, the strongest [[SERPINE2]] → it (grade B ⚠); 27 go from it, the strongest it → [[SOX9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6002.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.49×** | +9.0 | 1e-16 | 41/44 (NCI-H460, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.73×** | +8.8 | 6e-16 | 39/40 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **3.30×** | +8.3 | 3e-14 | 38/43 (HOP62, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **2.22×** | +8.1 | 6e-14 | 31/43 (AsPC-1, CFPAC-1, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +7.1 | 1e-10 | 42/43 (A-172, HOP62, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.54×** | +6.4 | 1e-08 | 40/42 (AsPC-1, C32, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.10×** | +5.3 | 8e-06 | 41/44 (NCI-H2347, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.42×** | +5.1 | 3e-05 | 41/44 (C32, AsPC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.87×** | +4.5 | 4e-04 | 27/43 (C32, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.79×** | +4.2 | 0.002 | 26/43 (AsPC-1, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.82×** | +4.1 | 0.002 | 27/40 (NCI-H460, HCT15, …) | all doses, flat | composition shift |
| [[Vilanterol (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.002 | 41/44 (SW1417, AsPC-1, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.69×** | +3.8 | 0.006 | 32/43 (SW48, SW480, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~71% of this change | **1.67×** | +3.7 | 0.008 | 31/43 (Panc 03.27, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.05×** | +3.4 | 0.028 | 40/43 (SW1417, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.89×** | +3.0 | 0.093 | 31/43 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6002.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.378×** | -7.0 | 2e-09 | 40/43 (LS 180, NCI-H2030, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.575×** | -5.6 | 6e-06 | 32/44 (SW48, SNU-423, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.474×** | -5.3 | 2e-05 | 40/43 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.442×** | -5.0 | 8e-05 | 37/45 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.507×** | -4.7 | 3e-04 | 34/43 (SNU-423, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.526×** | -4.6 | 4e-04 | 37/43 (SW 1271, HS-578T, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.551×** | -4.3 | 0.002 | 41/43 (AsPC-1, SNU-423, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.541×** | -4.1 | 0.003 | 36/43 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.681×** | -3.9 | 0.006 | 29/43 (H4, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.324×** | -3.8 | 0.007 | 32/42 (NCI-H2030, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.685×** | -3.7 | 0.010 | 38/43 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.599×** | -3.7 | 0.011 | 28/43 (HS-578T, hTERT-HPNE, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.600×** | -3.7 | 0.011 | 26/43 (NCI-H1573, H4, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.365×** | -3.4 | 0.024 | 34/44 (C32, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -3.3 | 0.038 | 26/45 (SW48, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.403×** | -3.1 | 0.069 | 30/45 (COLO 205, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.81 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 617 | 7 (7 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +12.5) ⚠ cell-cycle shift, explains ~70% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -13.1) |
| [[SW48 (line)]] | wt | 1,025 | 10 (8 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 8.23× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 5.96× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -15.9) |
| [[C32 (line)]] | wt | 309 | 8 (7 ⚠) | 3 | [[Harringtonine (drug)]] 0.5 µM 8.98× (z +15.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 21.0× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 172 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +23.3) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 16.4× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 335 | 3 (3 ⚠) | 4 | [[Harringtonine (drug)]] 5 µM 4.65× (z +9.4) ⚠ cell-cycle shift, explains ~38% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -11.2) |
| [[HOP62 (line)]] | alt | 317 | 6 (5 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 16.7× (z +13.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.36× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 218 | 6 (6 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 8.28× (z +13.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 160 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.5× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 115 | 5 (5 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.69× (z +13.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SNU-423 (line)]] | alt | 628 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +10.3) ⚠ cell-cycle shift, explains ~70% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -14.0) |
| [[A498 (line)]] | wt | 103 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +13.0) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[COLO 205 (line)]] | alt | 113 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.8× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HepG2_C3A (line)]] | wt | 174 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +11.1) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 62.5 | 4 (3 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 6.04× (z +9.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.13× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 164 | 0 | 4 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.624× (z -9.6) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.187× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 114 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +14.4) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[SW 900 (line)]] | alt | 256 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.6) ⚠ cell-cycle shift, explains ~70% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -9.1) |
| [[AN3 CA (line)]] | alt | 428 | 1 | 2 | [[Auranofin (drug)]] 5 µM 7.86× (z +10.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -9.9) |
| [[HCT15 (line)]] | alt | 84.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.25× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HEC-1-A (line)]] | alt | 131 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +11.6) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[RPMI-7951 (line)]] | alt | 285 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.20× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 147 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.0× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW 1271 (line)]] | alt | 265 | 0 | 3 | — | [[Clobetasol propionate (drug)]] 5 µM 0.0897× (z -10.1) |
| [[A-172 (line)]] | wt | 80.6 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.19× (z +9.3) | — |
| [[J82 (line)]] | alt | 137 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +12.5) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[LS 180 (line)]] | wt | 219 | 0 | 2 | — | [[Ponatinib (drug)]] 5 µM 0.177× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 605 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 256 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +15.2) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[CHP-212 (line)]] | wt | 244 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -9.3) |
| [[H4 (line)]] | wt | 155 | 0 | 1 | — | [[Triamcinolone (drug)]] 5 µM 0.300× (z -8.5) |
| [[KATO III (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.01× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 198 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2347 (line)]] | alt | 94.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.75× (z +9.9) ⚠ toxic | — |
| [[SHP-77 (line)]] | alt | 57.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 151 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.97× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[A-427 (line)]] | wt | 23.6 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.1 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 143 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 129 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 326 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 48.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 20.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 224 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER2]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 579 |
| [[CXCL8]] | +0.72 | +0.66 / +0.74 | both halves | 7e-06 | STRING 554 |
| [[GEM]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CSRNP1]] | +0.71 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[FAM43A]] | +0.70 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[LIF]] | +0.70 | +0.68 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[IL1A]] | +0.69 | +0.68 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS |
| [[ARL4C]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[SHB]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[NFKBIE]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TRAF1]] | +0.65 | +0.66 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PTGS2]] | +0.64 | +0.58 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 429 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP133]] | -0.60 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[DGCR2]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 25, C 4. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINE2]] | B | SERPINE2 activity raises IER3's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 2.10× lower at baseline in the lines without SERPINE2 | 0.009 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[CD82]] | B | CD82 activity raises IER3's level | lines that do not express CD82 (11) vs lines expressing it (39) | 2.85× lower at baseline in the lines without CD82 | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGA3, GBP3, CXCL3; maybe low, not absent |
| [[GEM]] | B | GEM activity raises IER3's level | lines that do not express GEM (9) vs lines expressing it (41) | 2.73× lower at baseline in the lines without GEM | 0.012 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[CD274]] | B | CD274 activity raises IER3's level | lines that do not express CD274 (18) vs lines expressing it (32) | 2.02× lower at baseline in the lines without CD274 | 0.014 | ⚠ within organs, on part of the lines; also absent: GBP5, IL1B, PDCD1LG2 |
| [[VDR]] | B | VDR activity raises IER3's level | lines that do not express VDR (8) vs lines expressing it (42) | 3.64× lower at baseline in the lines without VDR | 0.016 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[ARC]] | B | ARC activity raises IER3's level | lines that do not express ARC (19) vs lines expressing it (31) | 2.35× lower at baseline in the lines without ARC | 0.018 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |
| [[SOX9]] | B | SOX9 activity raises IER3's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.68× lower at baseline in the lines without SOX9 | 0.019 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[TNFRSF1B]] | B | TNFRSF1B activity raises IER3's level | lines that do not express TNFRSF1B (17) vs lines expressing it (33) | 1.85× lower at baseline in the lines without TNFRSF1B | 0.019 | ⚠ within organs, on part of the lines; also absent: GUCY1B2, DGKE, LYPD5 |
| [[PTGER4]] | B | PTGER4 activity raises IER3's level | lines that do not express PTGER4 (12) vs lines expressing it (38) | 2.20× lower at baseline in the lines without PTGER4 | 0.025 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |
| [[IL6]] | B | IL6 activity raises IER3's level | lines that do not express IL6 (32) vs lines expressing it (18) | 1.82× lower at baseline in the lines without IL6 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[RRAD]] | B | RRAD activity raises IER3's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.99× lower at baseline in the lines without RRAD | 0.040 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[PTGS2]] | B | PTGS2 activity raises IER3's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 1.95× lower at baseline in the lines without PTGS2 | 0.041 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 25, C 2. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOX9]] | B | IER3 activity raises SOX9's level | lines that do not express IER3 (5) vs lines expressing it (45) | 4.95× lower at baseline in the lines without IER3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[SEMA3A]] | B | IER3 activity lowers SEMA3A's level | lines that do not express IER3 (5) vs lines expressing it (45) | 5.89× higher at baseline in the lines without IER3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[PMEPA1]] | B | IER3 activity raises PMEPA1's level | lines that do not express IER3 (5) vs lines expressing it (45) | 4.48× lower at baseline in the lines without IER3 | 0.022 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[CXCL8]] | B | IER3 activity raises CXCL8's level | lines that do not express IER3 (5) vs lines expressing it (45) | 6.79× lower at baseline in the lines without IER3 | 0.027 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[ZMIZ2]] | B | IER3 activity raises ZMIZ2's level | lines that do not express IER3 (5) vs lines expressing it (45) | 2.10× lower at baseline in the lines without IER3 | 0.028 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[HMSD]] | B | IER3 activity lowers HMSD's level | lines that do not express IER3 (5) vs lines expressing it (45) | 1.93× higher at baseline in the lines without IER3 | 0.033 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[MAFK]] | B | IER3 activity raises MAFK's level | lines that do not express IER3 (5) vs lines expressing it (45) | 2.80× lower at baseline in the lines without IER3 | 0.037 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[MRPL37]] | B | IER3 activity lowers MRPL37's level | lines that do not express IER3 (5) vs lines expressing it (45) | 1.41× higher at baseline in the lines without IER3 | 0.041 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[MIR23AHG]] | B | IER3 activity raises MIR23AHG's level | lines that do not express IER3 (5) vs lines expressing it (45) | 1.94× lower at baseline in the lines without IER3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[ARHGAP26]] | B | IER3 activity raises ARHGAP26's level | lines that do not express IER3 (5) vs lines expressing it (45) | 2.60× lower at baseline in the lines without IER3 | 0.050 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[PTGER4]] | B | IER3 activity raises PTGER4's level | lines that do not express IER3 (5) vs lines expressing it (45) | 2.94× lower at baseline in the lines without IER3 | 0.054 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[KIAA1217]] | B | IER3 activity raises KIAA1217's level | lines that do not express IER3 (5) vs lines expressing it (45) | 6.29× lower at baseline in the lines without IER3 | 0.055 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.825). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.8, 1.7); signed map (8.6, 28.5). **Vector** length 128, 51.7% of its response variance represented; |z| ≥ 3 in 1,556 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-10 signaling* (reactome, mean cos +0.66 to 5); *KRAS signaling up* (hallmark, mean cos +0.59 to 8); *inflammatory response* (hallmark, mean cos +0.66 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +13.1 | +7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +11.3 | +5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +8.9 | +8.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.7 | +8.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.3 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.6 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +0.8 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.9 | +4.1 |
| fall | [[NG25 (drug)]] 5 µM |  | -5.6 | -3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -5.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -5.3 | -5.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -5.3 | -3.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -5.3 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.1 | -7.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.8 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | immediate early response 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:30,743,199-30,744,548 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IEX-1, DIF-2, PRG1, IEX-1L |
| Hallmark sets | APOPTOSIS, GLYCOLYSIS, HYPOXIA, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 4 pathways, smallest: PI5P, PP2A and IER3 Regulate PI3K/AKT Signaling; Negative regulation of the PI3K/AKT network; PIP3 activates AKT signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P46695](https://www.uniprot.org/uniprotkb/P46695) (Radiation-inducible immediate-early gene IEX-1):

> May play a role in the ERK signaling pathway by inhibiting the dephosphorylation of ERK by phosphatase PP2A-PPP2R5C holoenzyme. Also acts as an ERK downstream effector mediating survival. As a member of the NUPR1/RELB/IER3 survival pathway, may provide pancreatic ductal adenocarcinoma with remarkable resistance to cell stress, such as starvation or gemcitabine treatment.

**Summary**, from NCBI Gene [8870](https://www.ncbi.nlm.nih.gov/gene/8870):

> This gene functions in the protection of cells from Fas- or tumor necrosis factor type alpha-induced apoptosis. Partially degraded and unspliced transcripts are found after virus infection in vitro, but these transcripts are not found in vivo and do not generate a valid protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5392](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5392) · Entrez [8870](https://www.ncbi.nlm.nih.gov/gene/8870) · UniProt [P46695](https://www.uniprot.org/uniprotkb/P46695) · Ensembl [ENSG00000137331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137331)

## Data

Gene col 6002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6002); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6002]; `tensor/DDL_lfc|DDL_z.npy` [6002]; `embed/gene_vectors.npy` [6002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6002 or target_col == 6002). Every well: [[IER3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IER3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
