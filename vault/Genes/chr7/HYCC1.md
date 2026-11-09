---
symbol: "HYCC1"
type: "gene"
col: 4356
ensembl_id: "ENSG00000122591"
name: "hyccin PI4KA lipid kinase complex subunit 1"
location: "7p15.3"
module: 89
arm: "+"
pooled_cpm: 125.59
n_lines_expressing: 42
n_dd_up: 32
n_dd_down: 2
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# HYCC1

*hyccin PI4KA lipid kinase complex subunit 1* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.37× (z +30.6, q 0e+00, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.772× (z -4.7, q 0.001, down in 20 of 40 measured lines) ⚠ transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.801× (z -4.1, q 0.014, down in 20 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HS-578T 0.445×, NCI-H2347 0.568×, SW 900 0.571×; ⚠ cell-cycle shift, explains ~46% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.353×, SW 900 0.423×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Budesonide (drug)]] 0.5 µM in 2 lines (HS-578T 0.408×, H4 0.411×); [[Auranofin (drug)]] 5 µM in 2 lines (NCI-H2347 0.478×, SW 900 0.466×); [[Clobetasol propionate (drug)]] 0.05 µM in 2 lines (HS-578T 0.440×, H4 0.407×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSC22D2]] (+0.52, fdr 1e-05), [[RGS9]] (+0.50, fdr 4e-04), [[PICALM]] (+0.50, fdr 2e-04); moves opposite to [[ZSCAN25]] (-0.56, fdr 4e-05), [[THAP4]] (-0.55, fdr 6e-05), [[TRMT44]] (-0.55, fdr 5e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[RGS9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4356.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.37×** | +30.6 | 0e+00 | 40/40 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.09×** | +25.6 | 0e+00 | 39/40 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.84×** | +24.5 | 0e+00 | 40/40 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.51×** | +23.7 | 0e+00 | 38/40 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +16.0 | 0e+00 | 37/40 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.33×** | +15.4 | 0e+00 | 38/40 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.42×** | +14.9 | 0e+00 | 38/40 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +13.2 | 9e-38 | 37/40 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.93×** | +12.0 | 4e-31 | 38/40 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +11.3 | 9e-28 | 33/40 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +10.8 | 1e-25 | 37/41 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +9.1 | 3e-18 | 34/40 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +8.7 | 9e-17 | 29/40 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.50×** | +8.7 | 1e-16 | 38/41 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +7.3 | 1e-11 | 30/40 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +7.1 | 4e-11 | 31/40 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4356.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HS-578T 0.445×, NCI-H2347 0.568×, SW 900 0.571×; ⚠ cell-cycle shift, explains ~46% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.353×, SW 900 0.423×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Budesonide (drug)]] 0.5 µM in 2 lines (HS-578T 0.408×, H4 0.411×); [[Auranofin (drug)]] 5 µM in 2 lines (NCI-H2347 0.478×, SW 900 0.466×); [[Clobetasol propionate (drug)]] 0.05 µM in 2 lines (HS-578T 0.440×, H4 0.407×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.772×** | -4.7 | 0.001 | 20/40 (SW 900, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.801×** | -4.1 | 0.014 | 20/40 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.842× | -3.2 | 0.26 | 14/39 (HOP62, C32, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.26 | 17/39 (SW 1271, A549, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4356. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 36.1 | 13 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 14.7× (z +23.7) | — |
| [[SW480 (line)]] | alt | 52.5 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +24.0) | — |
| [[KATO III (line)]] | alt | 90.7 | 11 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 10.9× (z +24.0) | — |
| [[SNU-423 (line)]] | alt | 158 | 11 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.02× (z +16.4) | — |
| [[SW1417 (line)]] | alt | 124 | 10 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +21.2) | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 512 | 2 (1 ⚠) | 8 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.97× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.29× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -12.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.395× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 56.7 | 10 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 10.2× (z +20.0) | — |
| [[NCI-H460 (line)]] | wt | 196 | 8 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.96× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 52.6 | 9 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 10.2× (z +19.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 53.2 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +20.9) | — |
| [[NCI-H2347 (line)]] | alt | 278 | 7 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.56× (z +17.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -10.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.478× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 340 | 9 | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +17.1) | — |
| [[J82 (line)]] | alt | 190 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.51× (z +13.6) | — |
| [[Panc 03.27 (line)]] | alt | 101 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +19.4) | — |
| [[PANC-1 (line)]] | alt | 111 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 5.70× (z +26.7) | — |
| [[A-172 (line)]] | wt | 155 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.70× (z +18.5) | — |
| [[A498 (line)]] | wt | 220 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +23.2) | — |
| [[LOX-IMVI (line)]] | wt | 115 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.32× (z +17.6) | — |
| [[CFPAC-1 (line)]] | alt | 52.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +19.6) | — |
| [[HEC-1-A (line)]] | alt | 81.2 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 7.04× (z +17.3) | — |
| [[HOP62 (line)]] | alt | 95.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +16.7) | — |
| [[Hs 766T (line)]] | wt | 65.5 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 8.23× (z +18.3) | — |
| [[NCI-H1792 (line)]] | alt | 144 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.62× (z +17.5) | — |
| [[SHP-77 (line)]] | alt | 135 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.43× (z +19.2) | — |
| [[SNU-1 (line)]] | wt | 68.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +15.7) | — |
| [[SW 900 (line)]] | alt | 316 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.423× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.466× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 56.2 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.93× (z +15.8) | — |
| [[hTERT-HPNE (line)]] | wt | 232 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.2) | — |
| [[A-427 (line)]] | wt | 41.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.71× (z +19.4) | — |
| [[C-33 A (line)]] | alt | 38.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.37× (z +12.2) | — |
| [[C32 (line)]] | wt | 220 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +21.6) | — |
| [[NCI-H2030 (line)]] | alt | 167 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.50× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 109 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.24× (z +17.8) | — |
| [[A549 (line)]] | wt | 56.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.91× (z +18.6) | — |
| [[H4 (line)]] | wt | 559 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.9) | [[Clobetasol propionate (drug)]] 0.05 µM 0.407× (z -8.8) |
| [[AN3 CA (line)]] | alt | 71.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.24× (z +9.7) | — |
| [[CHP-212 (line)]] | wt | 111 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +8.7) | — |
| [[SW 1088 (line)]] | alt | 1,066 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 29.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 30.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 19.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 334 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4356), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*25 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D2]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[RGS9]] | +0.50 | +0.24 / +0.58 | both halves | 4e-04 |  |
| [[PICALM]] | +0.50 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[PAG1]] | +0.50 | +0.22 / +0.55 | both halves | 6e-04 |  |
| [[PTBP3]] | +0.49 | +0.41 / +0.35 | both halves | 1e-04 |  |
| [[CYRIA]] | +0.48 | +0.26 / +0.57 | both halves | 4e-04 |  |
| [[CCNYL1]] | +0.47 | +0.37 / +0.48 | both halves | 7e-05 |  |
| [[PPFIBP1]] | +0.47 | +0.23 / +0.48 | both halves | 5e-04 | STRING 412 |
| [[UGCG]] | +0.46 | +0.29 / +0.40 | both halves | 2e-04 |  |
| [[VWA5A]] | +0.46 | +0.25 / +0.47 | both halves | 4e-04 |  |
| [[SUSD4]] | +0.45 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[SPTSSA]] | +0.45 | +0.26 / +0.49 | both halves | 4e-04 |  |

## Genes that move opposite

*75 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN25]] | -0.56 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[THAP4]] | -0.55 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[TRMT44]] | -0.55 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[TRMT61B]] | -0.54 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[ACAD9]] | -0.54 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[WDR81]] | -0.53 | -0.26 / -0.55 | both halves | 3e-04 |  |
| [[TRMT1]] | -0.51 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[AKAP8]] | -0.50 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[L3MBTL2]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[GTF3C2]] | -0.50 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[VPS33A]] | -0.50 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[TBP]] | -0.49 | -0.29 / -0.51 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HYCC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RGS9]] | B | RGS9 activity raises HYCC1's level | lines that do not express RGS9 (6) vs lines expressing it (44) | 2.20× lower at baseline in the lines without RGS9 | 0.094 | ⚠ within organs, on part of the lines; also absent: TMEM132A, KCNC4, ECE1; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS9]] | B | HYCC1 activity raises RGS9's level | lines that do not express HYCC1 (8) vs lines expressing it (42) | 2.05× lower at baseline in the lines without HYCC1 | 0.055 | ⚠ within organs, on part of the lines; also absent: FERMT2, CCDC88A, HEG1 |
| [[FARS2]] | B | HYCC1 activity raises FARS2's level | lines that do not express HYCC1 (8) vs lines expressing it (42) | 1.26× lower at baseline in the lines without HYCC1 | 0.099 | ⚠ within organs, on part of the lines; also absent: FERMT2, CCDC88A, HEG1 |

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction -0.519). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-46.0, 10.3); signed map (-13.8, 30.6). **Vector** length 95.6, 28.2% of its response variance represented; |z| ≥ 3 in 1,385 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.3 | +16.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.3 | +10.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.7 | +12.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.2 | +7.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +8.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.1 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.0 | -4.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | +2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -4.5 | +5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | +1.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.6 | -2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | hyccin PI4KA lipid kinase complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:22,889,371-23,014,130 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DRCTNNB1A, HCC, hyccin; previously FAM126A |
| Gene groups (HGNC) | PI4KA lipid kinase complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYI3](https://www.uniprot.org/uniprotkb/Q9BYI3) (Hyccin):

> Component of a complex required to localize phosphatidylinositol 4-kinase (PI4K) to the plasma membrane. The complex acts as a regulator of phosphatidylinositol 4-phosphate (PtdIns(4)P) synthesis. HYCC1 plays a key role in oligodendrocytes formation, a cell type with expanded plasma membrane that requires generation of PtdIns(4)P. Its role in oligodendrocytes formation probably explains its importance in myelination of the central and peripheral nervous system. May also have a role in the …

**Summary**, from NCBI Gene [84668](https://www.ncbi.nlm.nih.gov/gene/84668):

> The protein encoded by this gene may play a part in the beta-catenin/Lef signaling pathway. Expression of this gene is down-regulated by beta-catenin. Defects in this gene are a cause of hypomyelination with congenital cataract (HCC). [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:24587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24587) · Entrez [84668](https://www.ncbi.nlm.nih.gov/gene/84668) · UniProt [Q9BYI3](https://www.uniprot.org/uniprotkb/Q9BYI3) · Ensembl [ENSG00000122591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122591)

## Data

Gene col 4356: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4356); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4356, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4356]; `tensor/DDL_lfc|DDL_z.npy` [4356]; `embed/gene_vectors.npy` [4356]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4356 or target_col == 4356). Every well: [[HYCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HYCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
