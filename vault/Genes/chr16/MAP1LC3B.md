---
symbol: "MAP1LC3B"
type: "gene"
col: 6465
ensembl_id: "ENSG00000140941"
name: "microtubule associated protein 1 light chain 3 beta"
location: "16q24.2"
module: 4
arm: "-"
pooled_cpm: 150.62
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MAP1LC3B

*microtubule associated protein 1 light chain 3 beta* — 16q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.09× (z +18.5, q 0e+00, up in 48 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNPLA8]] (+0.66, fdr 7e-06), [[EIF1]] (+0.58, fdr 7e-06), [[CCNI]] (+0.58, fdr 7e-06); moves opposite to [[RBM26]] (-0.62, fdr 2e-05), [[SNRPD1]] (-0.59, fdr 1e-05), [[PFAS]] (-0.58, fdr 1e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6465.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +18.5 | 0e+00 | 48/49 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.61×** | +15.7 | 0e+00 | 43/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.56×** | +14.7 | 0e+00 | 46/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.59×** | +11.0 | 4e-26 | 47/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.45×** | +10.4 | 5e-23 | 44/49 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +9.6 | 1e-19 | 41/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.17×** | +9.0 | 2e-17 | 46/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.16×** | +8.6 | 7e-16 | 37/44 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +8.2 | 1e-14 | 47/48 (SW480, HS-578T, …) | two highest doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.92×** | +7.0 | 2e-10 | 37/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +6.8 | 5e-10 | 41/48 (SW480, HS-578T, …) | two highest doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +6.6 | 2e-09 | 41/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.76×** | +6.5 | 3e-09 | 46/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.76×** | +6.5 | 3e-09 | 42/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.43×** | +5.9 | 2e-07 | 41/49 (A-427, LoVo, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +5.8 | 2e-07 | 41/50 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +5.6 | 7e-07 | 39/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +5.3 | 4e-06 | 39/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.2 | 5e-06 | 37/48 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +4.7 | 6e-05 | 38/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.46×** | +4.4 | 3e-04 | 35/48 (Panc 03.27, A-427, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.2 | 7e-04 | 27/48 (HOP62, A-172, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.003 | 32/48 (HOP62, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6465.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.802× | -3.6 | 0.12 | 32/48 (PANC-1, SW480, …) | inconsistent across doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 0.738× | -3.5 | 0.12 | 37/48 (AN3 CA, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Arbutin (drug)]] 0.5 µM |  | 0.751× | -3.3 | 0.17 | 34/48 (HS-578T, HOP62, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6465. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 148 | 13 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +23.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +20.1) | — |
| [[NCI-H460 (line)]] | wt | 94.7 | 13 (9 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.37× (z +18.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +15.7) | — |
| [[SW480 (line)]] | alt | 87.3 | 13 (8 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.94× (z +20.0) | — |
| [[NCI-H1573 (line)]] | alt | 138 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.60× (z +27.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.35× (z +17.4) | — |
| [[HEC-1-A (line)]] | alt | 80.2 | 8 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.31× (z +17.3) | — |
| [[LoVo (line)]] | wt | 118 | 8 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.50× (z +20.9) | — |
| [[AsPC-1 (line)]] | alt | 176 | 7 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +18.2) | — |
| [[SW 900 (line)]] | alt | 136 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +15.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +14.9) | — |
| [[A498 (line)]] | wt | 126 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +20.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +18.0) | — |
| [[HepG2_C3A (line)]] | wt | 195 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +15.1) | — |
| [[HS-578T (line)]] | alt | 169 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +15.4) | — |
| [[HT-29 (line)]] | alt | 122 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.47× (z +15.8) | — |
| [[LS 180 (line)]] | wt | 94.3 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +15.8) | — |
| [[PANC-1 (line)]] | alt | 120 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +14.2) | — |
| [[SHP-77 (line)]] | alt | 95.6 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +12.5) | — |
| [[A-172 (line)]] | wt | 153 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +17.5) | — |
| [[C32 (line)]] | wt | 137 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +22.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.47× (z +16.3) | — |
| [[hTERT-HPNE (line)]] | wt | 108 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +19.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +17.3) | — |
| [[SNU-1 (line)]] | wt | 149 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.19× (z +13.2) | — |
| [[SNU-423 (line)]] | alt | 148 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +18.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +14.8) | — |
| [[SW1417 (line)]] | alt | 194 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +15.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +14.6) | — |
| [[Hs 766T (line)]] | wt | 165 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +16.5) | — |
| [[LOX-IMVI (line)]] | wt | 149 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +17.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 379 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +13.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.82× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 201 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +21.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 154 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +17.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +12.9) | — |
| [[SW48 (line)]] | wt | 110 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 104 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +16.3) | — |
| [[H4 (line)]] | wt | 168 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +11.6) | — |
| [[HCT15 (line)]] | alt | 150 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.07× (z +14.8) | — |
| [[KATO III (line)]] | alt | 208 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +12.1) | — |
| [[NCI-H2030 (line)]] | alt | 300 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +14.2) | — |
| [[NCI-H23 (line)]] | alt | 130 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.78× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 61.0 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +17.3) | — |
| [[C-33 A (line)]] | alt | 152 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 274 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 111 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +13.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[J82 (line)]] | alt | 170 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +15.3) | — |
| [[NCI-H2347 (line)]] | alt | 88.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +14.9) | — |
| [[RKO (line)]] | wt | 222 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.64× (z +10.1) | — |
| [[A-427 (line)]] | wt | 186 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.91× (z +13.4) | — |
| [[A549 (line)]] | wt | 117 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +14.8) | — |
| [[AN3 CA (line)]] | alt | 143 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.83× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 278 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.26× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 168 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6465), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPLA8]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[EIF1]] | +0.58 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[CCNI]] | +0.58 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ATG12]] | +0.56 | +0.45 / +0.61 | both halves | 3e-05 | same gene group; pathway: Autophagy; STRING 969 |
| [[SWT1]] | +0.56 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[NIT1]] | +0.56 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CTNNA1]] | +0.56 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[YPEL5]] | +0.55 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[RIOK3]] | +0.54 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ZBTB43]] | +0.54 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[TPT1-AS1]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[MXD1]] | +0.53 | +0.46 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM26]] | -0.62 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[SNRPD1]] | -0.59 | -0.54 / -0.64 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[PFAS]] | -0.58 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[TUBGCP3]] | -0.57 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[MAP3K4]] | -0.57 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[GMNN]] | -0.56 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[LCLAT1]] | -0.55 | -0.43 / -0.63 | both halves | 4e-05 |  |
| [[COA1]] | -0.55 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PDSS1]] | -0.55 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[KAT14]] | -0.55 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[UNG]] | -0.54 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[CENPM]] | -0.54 | -0.50 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MAP1LC3B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CTSL]] | B | CTSL activity raises MAP1LC3B's level | lines that do not express CTSL (9) vs lines expressing it (41) | 1.28× lower at baseline in the lines without CTSL | 0.087 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.462). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-16.9, -48.3); signed map (-12.4, 14.6). **Vector** length 99.6, 42.5% of its response variance represented; |z| ≥ 3 in 1,422 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +18.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +14.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.1 | +4.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.8 | +2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.7 | +1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.1 | +0.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | -4.7 | +3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -4.7 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.0 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -1.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.0 | -0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein 1 light chain 3 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.2 — chr16:87,383,953-87,404,779 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATG8F |
| Gene groups (HGNC) | Autophagy related; Microtubule associated protein 1 light chain 3 family |
| Reactome | 26 pathways, smallest: Pexophagy; Receptor Mediated Mitophagy; SARS-CoV-2 modulates autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZQ8](https://www.uniprot.org/uniprotkb/Q9GZQ8) (Microtubule-associated protein 1 light chain 3 beta):

> Ubiquitin-like modifier involved in formation of autophagosomal vacuoles (autophagosomes). Plays a role in mitophagy which contributes to regulate mitochondrial quantity and quality by eliminating the mitochondria to a basal level to fulfill cellular energy requirements and preventing excess ROS production. In response to cellular stress and upon mitochondria fission, binds C-18 ceramides and anchors autophagolysosomes to outer mitochondrial membranes to eliminate damaged mitochondria. While …

**Summary**, from NCBI Gene [81631](https://www.ncbi.nlm.nih.gov/gene/81631):

> The product of this gene is a subunit of neuronal microtubule-associated MAP1A and MAP1B proteins, which are involved in microtubule assembly and important for neurogenesis. Studies on the rat homolog implicate a role for this gene in autophagy, a process that involves the bulk degradation of cytoplasmic component. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13352) · Entrez [81631](https://www.ncbi.nlm.nih.gov/gene/81631) · UniProt [Q9GZQ8](https://www.uniprot.org/uniprotkb/Q9GZQ8) · Ensembl [ENSG00000140941](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140941)

## Data

Gene col 6465: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6465); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6465, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6465]; `tensor/DDL_lfc|DDL_z.npy` [6465]; `embed/gene_vectors.npy` [6465]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6465 or target_col == 6465). Every well: [[MAP1LC3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP1LC3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
