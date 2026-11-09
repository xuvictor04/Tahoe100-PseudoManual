---
symbol: "RSL1D1"
type: "gene"
col: 10120
ensembl_id: "ENSG00000171490"
name: "ribosomal L1 domain containing 1"
location: "16p13.13"
module: 1
arm: "+"
pooled_cpm: 196.45
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RSL1D1

*ribosomal L1 domain containing 1* — 16p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +9.7, q 3e-19, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~54% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.19× (z +9.1, q 3e-17, up in 42 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.497×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.528×; ⚠ cell-cycle shift, explains ~54% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOL8]] (+0.70, fdr 7e-06), [[EIF3A]] (+0.68, fdr 7e-06), [[NOP14]] (+0.66, fdr 7e-06); moves opposite to [[CALM3]] (-0.61, fdr 1e-05), [[PRKACA]] (-0.59, fdr 1e-05), [[ECM1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10120.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.80×** | +9.7 | 3e-19 | 37/48 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.19×** | +9.1 | 3e-17 | 42/48 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.98×** | +7.6 | 5e-12 | 38/44 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.07×** | +7.4 | 2e-11 | 47/48 (NCI-H1792, SW480, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.85×** | +6.9 | 5e-10 | 43/48 (COLO 205, A-172, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.97×** | +6.9 | 5e-10 | 47/49 (NCI-H1792, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +5.3 | 1e-05 | 40/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.66×** | +5.2 | 1e-05 | 37/45 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +5.1 | 2e-05 | 44/48 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +5.0 | 4e-05 | 40/47 (NCI-H1573, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.55×** | +4.9 | 4e-05 | 40/47 (NCI-H1573, HepG2/C3A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +4.7 | 1e-04 | 39/48 (HT-29, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.03×** | +4.3 | 7e-04 | 44/48 (AsPC-1, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.45×** | +4.3 | 7e-04 | 30/48 (NCI-H460, COLO 205, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.98×** | +4.1 | 0.001 | 41/49 (NCI-H2030, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +3.8 | 0.005 | 33/48 (NCI-H2030, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.86×** | +3.8 | 0.005 | 40/48 (AsPC-1, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.006 | 36/48 (BT-474, AN3 CA, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.79×** | +3.5 | 0.012 | 39/48 (CFPAC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.013 | 32/48 (HT-29, Hs 766T, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.015 | 31/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.045 | 29/48 (HT-29, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.62×** | +2.9 | 0.076 | 31/48 (CFPAC-1, KATO III, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10120.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.497×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.528×; ⚠ cell-cycle shift, explains ~54% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.820× | -3.3 | 0.43 | 33/48 (J82, A498, …) | top dose only | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 0.826× | -3.2 | 0.43 | 26/48 (hTERT-HPNE, SW 1088, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.832× | -3.0 | 0.43 | 24/48 (SW48, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10120. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 130 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +13.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.22× (z +12.8) | — |
| [[COLO 205 (line)]] | alt | 103 | 4 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.91× (z +12.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.72× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 174 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.8) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +9.4) | — |
| [[A-172 (line)]] | wt | 141 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +19.7) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.60× (z +13.1) | — |
| [[Hs 766T (line)]] | wt | 199 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.68× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 178 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 188 | 3 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.60× (z +9.0) | — |
| [[SW480 (line)]] | alt | 234 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.57× (z +8.9) | — |
| [[A498 (line)]] | wt | 256 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.8) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[A549 (line)]] | wt | 253 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.3) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[CFPAC-1 (line)]] | alt | 125 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +15.8) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +10.4) | — |
| [[H4 (line)]] | wt | 169 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +11.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.48× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 108 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +19.7) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 156 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.0) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +8.7) | — |
| [[J82 (line)]] | alt | 189 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.5) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[LoVo (line)]] | wt | 211 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2030 (line)]] | alt | 189 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.0) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +9.4) | — |
| [[RKO (line)]] | wt | 348 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 185 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.0) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.83× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 169 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +17.1) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[SW 900 (line)]] | alt | 102 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.5) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[AN3 CA (line)]] | alt | 242 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.34× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 236 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 164 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.69× (z +9.5) | — |
| [[C32 (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.6) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[HEC-1-A (line)]] | alt | 236 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.9) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[HepG2_C3A (line)]] | wt | 236 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.44× (z +8.5) ⚠ toxic; cell-cycle shift, explains ~36% of this change | — |
| [[HS-578T (line)]] | alt | 127 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +10.2) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 226 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 210 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.1) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[PANC-1 (line)]] | alt | 248 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.6) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[SHP-77 (line)]] | alt | 161 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +8.6) | — |
| [[A-427 (line)]] | wt | 215 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 250 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 342 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 225 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 254 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 323 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10120), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOL8]] | +0.70 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[EIF3A]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[NOP14]] | +0.66 | +0.72 / +0.62 | both halves | 7e-06 | same gene group; STRING 992 |
| [[UTP14A]] | +0.66 | +0.72 / +0.62 | both halves | 7e-06 | same gene group; STRING 983 |
| [[ESF1]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 | same gene group; STRING 860 |
| [[EIF3D]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[NOB1]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 | STRING 721 |
| [[MTIF2]] | +0.65 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[RAD50]] | +0.64 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[NIFK]] | +0.64 | +0.74 / +0.60 | both halves | 7e-06 | STRING 999 |
| [[RPF2]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 | STRING 996 |
| [[METAP2]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 | STRING 515 |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALM3]] | -0.61 | -0.71 / -0.55 | both halves | 1e-05 |  |
| [[PRKACA]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ECM1]] | -0.56 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[MPC2]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[NAGA]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[APLP1]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[CDK2]] | -0.51 | -0.57 / -0.43 | both halves | 3e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[PIGS]] | -0.51 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[SDC1]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[MYCBP]] | -0.51 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[TK1]] | -0.50 | -0.47 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.1, -40.8); signed map (3.8, -43.6). **Vector** length 99.6, 44.8% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +7.4 |
|  | [[EX229 (drug)]] 5 µM |  | +4.2 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.4 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +3.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | -4.4 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -3.5 | +4.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +2.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | +0.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.1 | +0.7 |
|  | [[Pimitespib (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -1.8 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal L1 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.13 — chr16:11,833,850-11,851,580 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cic1, PBK1, L12, DKFZP564M182, CSIG, UTP30 |
| Gene groups (HGNC) | SSU processome |
| Hallmark sets | MYC_TARGETS_V1 |
| Matched by | ensembl_id |

**Function**, from UniProt [O76021](https://www.uniprot.org/uniprotkb/O76021) (Ribosomal L1 domain-containing protein 1):

> Regulates cellular senescence through inhibition of PTEN translation. Acts as a pro-apoptotic regulator in response to DNA damage.

**Summary**, from NCBI Gene [26156](https://www.ncbi.nlm.nih.gov/gene/26156):

> Enables mRNA 3'-UTR binding activity and mRNA 5'-UTR binding activity. Involved in regulation of apoptotic process and regulation of cellular senescence. Acts upstream of or within regulation of protein localization. Located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24534](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24534) · Entrez [26156](https://www.ncbi.nlm.nih.gov/gene/26156) · UniProt [O76021](https://www.uniprot.org/uniprotkb/O76021) · Ensembl [ENSG00000171490](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171490)

## Data

Gene col 10120: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10120); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10120, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10120]; `tensor/DDL_lfc|DDL_z.npy` [10120]; `embed/gene_vectors.npy` [10120]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10120 or target_col == 10120). Every well: [[RSL1D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSL1D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
