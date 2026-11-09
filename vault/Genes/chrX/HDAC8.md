---
symbol: "HDAC8"
type: "gene"
col: 7145
ensembl_id: "ENSG00000147099"
name: "histone deacetylase 8"
location: "Xq13.1"
module: 213
arm: "+"
pooled_cpm: 226.84
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 27
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 599
tags: ["gene", "module/213"]
generated_by: "tahoemap"
---

# HDAC8

*histone deacetylase 8* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 1.24× (z +4.6, q 0.002, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.310× (z -36.3, q 0e+00, down in 49 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MNAT1]] (+0.66, fdr 7e-06), [[LINC01278]] (+0.62, fdr 7e-06), [[MBD5]] (+0.62, fdr 9e-06); moves opposite to [[SELENOI]] (-0.48, fdr 5e-05), [[SHPK]] (-0.47, fdr 1e-04), [[PTPN18]] (-0.45, fdr 1e-04).
> It is in [[Module 213]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MGMT]] → it (grade B ⚠); 599 go from it, the strongest it → [[CDC23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7145.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +4.6 | 0.002 | 25/48 (HS-578T, SNU-423, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.23×** | +4.5 | 0.002 | 28/48 (LS 180, AsPC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.21×** | +4.1 | 0.006 | 23/49 (AsPC-1, LS 180, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.006 | 25/47 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.019 | 23/48 (HS-578T, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.18× | +3.7 | 0.021 | 20/49 (KATO III, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.12× | +3.6 | 0.022 | 17/48 (AsPC-1, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.10 | 16/47 (AsPC-1, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 21 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7145.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.310×** | -36.3 | 0e+00 | 49/49 (COLO 205, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.626×** | -14.5 | 6e-45 | 38/48 (SNU-423, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.532×** | -13.8 | 5e-41 | 44/49 (NCI-H23, SW480, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.537×** | -13.1 | 6e-37 | 42/48 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.549×** | -12.1 | 1e-31 | 40/45 (KATO III, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.572×** | -11.7 | 7e-30 | 39/44 (SW480, SNU-423, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.590×** | -11.1 | 1e-26 | 38/50 (SNU-423, A-427, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -10.3 | 4e-23 | 40/47 (COLO 205, SNU-423, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.698×** | -7.9 | 3e-13 | 35/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.692×** | -7.7 | 6e-13 | 35/47 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.703×** | -7.7 | 8e-13 | 32/48 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **0.707×** | -7.6 | 2e-12 | 42/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -6.9 | 3e-10 | 37/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.740×** | -6.3 | 1e-08 | 33/48 (PANC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.761×** | -6.0 | 9e-08 | 31/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.775×** | -5.6 | 9e-07 | 34/48 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.816×** | -4.4 | 3e-04 | 25/48 (HCT15, C-33 A, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.846× | -3.7 | 0.007 | 20/47 (CFPAC-1, MIA PaCa-2, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.891× | -3.6 | 0.010 | 10/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.854× | -3.5 | 0.013 | 15/48 (AN3 CA, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.854× | -3.4 | 0.013 | 16/48 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.809×** | -3.3 | 0.020 | 23/48 (MIA PaCa-2, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.860× | -3.3 | 0.020 | 19/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.751×** | -3.3 | 0.021 | 18/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.757×** | -3.2 | 0.026 | 21/48 (HOP62, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.758×** | -3.2 | 0.027 | 25/48 (Hs 766T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7145. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 330 | 0 | 15 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -31.5) |
| [[SW480 (line)]] | alt | 457 | 0 | 15 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -30.1) |
| [[C32 (line)]] | wt | 206 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -26.3) |
| [[MIA PaCa-2 (line)]] | alt | 289 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -23.6) |
| [[PANC-1 (line)]] | alt | 215 | 0 | 11 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -24.1) |
| [[LS 180 (line)]] | wt | 200 | 1 (1 ⚠) | 9 (6 ⚠) | [[Selinexor (drug)]] 5 µM 1.61× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -34.2) |
| [[SNU-423 (line)]] | alt | 369 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -35.2) |
| [[HEC-1-A (line)]] | alt | 216 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -26.2) |
| [[KATO III (line)]] | alt | 245 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -33.9) |
| [[COLO 205 (line)]] | alt | 315 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -40.4) |
| [[Panc 03.27 (line)]] | alt | 284 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -28.5) |
| [[HOP62 (line)]] | alt | 248 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -28.4) |
| [[CFPAC-1 (line)]] | alt | 170 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -22.6) |
| [[HT-29 (line)]] | alt | 207 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -28.1) |
| [[NCI-H1792 (line)]] | alt | 197 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -21.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -17.3) |
| [[SK-MEL-2 (line)]] | alt | 299 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -26.5) |
| [[LoVo (line)]] | wt | 190 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -26.4) |
| [[NCI-H23 (line)]] | alt | 392 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -28.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -28.1) |
| [[RKO (line)]] | wt | 239 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -22.6) |
| [[RPMI-7951 (line)]] | alt | 294 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -25.6) |
| [[C-33 A (line)]] | alt | 289 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -18.2) |
| [[Hs 766T (line)]] | wt | 247 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -23.1) |
| [[J82 (line)]] | alt | 183 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -21.2) |
| [[NCI-H1573 (line)]] | alt | 202 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -21.8) |
| [[A-427 (line)]] | wt | 201 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -14.6) |
| [[A498 (line)]] | wt | 176 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -16.5) |
| [[AN3 CA (line)]] | alt | 341 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -18.1) |
| [[AsPC-1 (line)]] | alt | 138 | 1 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.97× (z +11.3) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -13.8) |
| [[BT-474 (line)]] | alt | 134 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -15.1) |
| [[H4 (line)]] | wt | 220 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -19.9) |
| [[HCT15 (line)]] | alt | 270 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -25.2) |
| [[hTERT-HPNE (line)]] | wt | 153 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -19.3) |
| [[LOX-IMVI (line)]] | wt | 168 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -21.4) |
| [[CHP-212 (line)]] | wt | 268 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 103 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -11.4) |
| [[SHP-77 (line)]] | alt | 163 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -17.2) |
| [[SW 900 (line)]] | alt | 141 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -14.1) |
| [[SW1417 (line)]] | alt | 169 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -25.0) |
| [[A-172 (line)]] | wt | 133 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -15.0) |
| [[A549 (line)]] | wt | 229 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -22.7) |
| [[HS-578T (line)]] | alt | 112 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -14.0) |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 142 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -19.2) |
| [[NCI-H661 (line)]] | alt | 188 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -12.0) |
| [[SNU-1 (line)]] | wt | 214 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -24.6) |
| [[SW48 (line)]] | wt | 199 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -17.5) |
| [[NCI-H2122 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 149 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7145), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MNAT1]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[LINC01278]] | +0.62 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[MBD5]] | +0.62 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[KIAA1143]] | +0.62 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[TUT4]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[NDUFC2]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[CWC27]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CSTPP1]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ACBD6]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[RABGAP1]] | +0.56 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[CDKAL1]] | +0.56 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[SMIM30]] | +0.56 | +0.31 / +0.65 | both halves | 2e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOI]] | -0.48 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[SHPK]] | -0.47 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[PTPN18]] | -0.45 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[LINC01128]] | -0.45 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[SEPTIN8]] | -0.45 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ACLY]] | -0.45 | -0.38 / -0.48 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGMT]] | B | MGMT activity raises HDAC8's level | lines that do not express MGMT (11) vs lines expressing it (39) | 1.33× lower at baseline in the lines without MGMT | 0.042 | ⚠ within organs, on part of the lines; also absent: LINC02666, CDCP1, ZNF718 |

### Downstream of this gene

*599 arrows, 599 of them with an alert ⚠; grade A 0, B 599, C 0. Shown: the 12 strongest; 587 more arrows (587 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC23]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], HDAC8, [[HDAC10]], [[HDAC11]] activity raises CDC23's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CMIP]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], HDAC8, [[HDAC10]], [[HDAC11]] activity lowers CMIP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CROCCP3]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], HDAC8, [[HDAC10]], [[HDAC11]] activity lowers CROCCP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CYB561]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], HDAC8, [[HDAC10]], [[HDAC11]] activity raises CYB561's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[DNAJC2]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], HDAC8, [[HDAC10]], [[HDAC11]] activity raises DNAJC2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ENSG00000288899]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], HDAC8, [[HDAC10]], [[HDAC11]] activity raises ENSG00000288899's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FAM78B]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], HDAC8, [[HDAC10]], [[HDAC11]] activity lowers FAM78B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FBXW9]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], HDAC8, [[HDAC10]], [[HDAC11]] activity raises FBXW9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FMN1]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], HDAC8, [[HDAC10]], [[HDAC11]] activity lowers FMN1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[LRRC51]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], HDAC8, [[HDAC10]], [[HDAC11]] activity raises LRRC51's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[MRPS7]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], HDAC8, [[HDAC10]], [[HDAC11]] activity raises MRPS7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[NCBP3]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], HDAC8, [[HDAC10]], [[HDAC11]] activity raises NCBP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

## Where it sits

- **Module**: [[Module 213]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-26.5, -6.0); signed map (-19.9, -22.0). **Vector** length 102, 37.0% of its response variance represented; |z| ≥ 3 in 1,387 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.4 | +3.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +6.1 | +4.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | -2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.5 | +0.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.9 | +3.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.5 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | -0.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +2.6 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.1 | -36.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -13.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -11.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.9 | -5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -3.8 | -11.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | histone deacetylase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:72,329,516-72,573,101 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPD3, KDAC8; previously HDACL1, WTS, MRXS6 |
| Gene groups (HGNC) | Histone deacetylases, class I |
| Reactome | 25 pathways, smallest: Notch-HLH transcription pathway; NOTCH signaling regulates gene expression in endothelial stalk cells; HDACs deacetylate histones |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY41](https://www.uniprot.org/uniprotkb/Q9BY41) (Histone deacetylase 8):

> Histone deacetylase that catalyzes the deacetylation of lysine residues on the N-terminal part of the core histones (H2A, H2B, H3 and H4). Histone deacetylation gives a tag for epigenetic repression and plays an important role in transcriptional regulation, cell cycle progression and developmental events. Histone deacetylases act via the formation of large multiprotein complexes. Also involved in the deacetylation of cohesin complex protein SMC3 regulating release of cohesin complexes from …

**Summary**, from NCBI Gene [55869](https://www.ncbi.nlm.nih.gov/gene/55869):

> Histones play a critical role in transcriptional regulation, cell cycle progression, and developmental events. Histone acetylation/deacetylation alters chromosome structure and affects transcription factor access to DNA. The protein encoded by this gene belongs to class I of the histone deacetylase family. It catalyzes the deacetylation of lysine residues in the histone N-terminal tails and represses transcription in large multiprotein complexes with transcriptional co-repressors. Multiple …

**Accessions** — [HGNC:13315](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13315) · Entrez [55869](https://www.ncbi.nlm.nih.gov/gene/55869) · UniProt [Q9BY41](https://www.uniprot.org/uniprotkb/Q9BY41) · Ensembl [ENSG00000147099](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147099)

## Data

Gene col 7145: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7145); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7145, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7145]; `tensor/DDL_lfc|DDL_z.npy` [7145]; `embed/gene_vectors.npy` [7145]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7145 or target_col == 7145). Every well: [[HDAC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDAC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
