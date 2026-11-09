---
symbol: "SWAP70"
type: "gene"
col: 5474
ensembl_id: "ENSG00000133789"
name: "switching B cell complex subunit SWAP70"
location: "11p15.4"
module: 59
arm: "+"
pooled_cpm: 122.09
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# SWAP70

*switching B cell complex subunit SWAP70* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.31× (z +10.2, q 1e-21, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.810× (z -5.7, q 8e-06, down in 22 of 47 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 0.516×, BT-474 0.626×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.322×, SW1417 0.531×; ⚠ toxic; cell-cycle shift, explains ~54% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (AsPC-1 0.485×, BT-474 0.504×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (CHP-212 0.0994×); [[Dorzolamide (hydrochloride) (drug)]] 5 µM in 1 line (SW 1088 0.0733×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OPTN]] (+0.68, fdr 7e-06), [[OTUD1]] (+0.59, fdr 1e-05), [[KRAS]] (+0.59, fdr 1e-05); moves opposite to [[TIMM23B-AGAP6]] (-0.56, fdr 1e-05), [[WT1]] (-0.50, fdr 3e-05), [[ALG8]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RAB32]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +10.2 | 1e-21 | 31/47 (C-33 A, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.27×** | +8.9 | 1e-16 | 26/47 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +8.0 | 1e-13 | 30/47 (H4, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +8.0 | 1e-13 | 34/48 (C-33 A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.27×** | +6.5 | 1e-08 | 27/47 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +6.2 | 7e-08 | 30/48 (RKO, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.25×** | +5.8 | 6e-07 | 22/47 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.5 | 2e-06 | 21/47 (A-427, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +5.5 | 2e-06 | 23/47 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.22×** | +5.4 | 4e-06 | 21/47 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.22×** | +5.2 | 9e-06 | 21/46 (NCI-H1573, COLO 205, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.21×** | +5.1 | 2e-05 | 25/48 (NCI-H23, J82, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.21×** | +5.1 | 2e-05 | 21/47 (SW480, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +4.9 | 4e-05 | 15/47 (SK-MEL-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.40×** | +4.7 | 9e-05 | 19/49 (A-427, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +4.6 | 1e-04 | 7/47 (A-427, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +4.0 | 0.002 | 13/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.16× | +3.7 | 0.006 | 16/46 (A549, C-33 A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.007 | 18/47 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.13× | +3.6 | 0.007 | 9/48 (RKO, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.15× | +3.6 | 0.008 | 14/46 (NCI-H1573, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5474.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 0.516×, BT-474 0.626×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.322×, SW1417 0.531×; ⚠ toxic; cell-cycle shift, explains ~54% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (AsPC-1 0.485×, BT-474 0.504×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (CHP-212 0.0994×); [[Dorzolamide (hydrochloride) (drug)]] 5 µM in 1 line (SW 1088 0.0733×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.810×** | -5.7 | 8e-06 | 22/47 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.877× | -5.0 | 2e-04 | 5/47 (CHP-212, RPMI-7951, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | 0.876× | -3.4 | 0.11 | 19/46 (RKO, SW1417, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.891× | -3.1 | 0.23 | 10/46 (KATO III, BT-474, …) | inconsistent across doses |  |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.924× | -3.0 | 0.23 | 1/47 (hTERT-HPNE) | top dose only |  |
| [[Olanzapine (drug)]] 5 µM |  | 0.924× | -3.0 | 0.23 | 1/47 (CHP-212) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 274 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +20.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[PANC-1 (line)]] | alt | 202 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +24.9) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A-172 (line)]] | wt | 159 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +19.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.52× (z +8.6) | — |
| [[A498 (line)]] | wt | 144 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +18.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A549 (line)]] | wt | 154 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +16.9) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[BT-474 (line)]] | alt | 207 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.438× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 205 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +15.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H460 (line)]] | wt | 71.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +19.2) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[AsPC-1 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 153 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.00× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.423× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 240 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.3) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A-427 (line)]] | wt | 126 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.54× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 34.0 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0994× (z -9.5) |
| [[HCT15 (line)]] | alt | 83.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 94.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HT-29 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +15.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 98.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[KATO III (line)]] | alt | 61.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +8.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.463× (z -9.8) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +11.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.322× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~54% of this change |
| [[RPMI-7951 (line)]] | alt | 95.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.6) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW 1088 (line)]] | alt | 80.7 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 5 µM 0.0733× (z -9.3) |
| [[SW1417 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.531× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~54% of this change |
| [[SW480 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.63× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 93.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 100 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 273 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 114 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 87.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 107 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPTN]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[OTUD1]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[KRAS]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[LACTB]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ABI1]] | +0.56 | +0.41 / +0.61 | both halves | 4e-05 | pathway: RAC1 GTPase cycle; STRING 509 |
| [[TBC1D9]] | +0.55 | +0.46 / +0.60 | both halves | 3e-05 | same gene group |
| [[VAT1]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[NDRG4]] | +0.53 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[CYRIA]] | +0.53 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[KMT2A]] | +0.53 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[TPPP]] | +0.52 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[DAAM1]] | +0.52 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B-AGAP6]] | -0.56 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[WT1]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ALG8]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[TRNT1]] | -0.47 | -0.40 / -0.54 | both halves | 4e-05 |  |
| [[PDCD6]] | -0.46 | -0.42 / -0.50 | both halves | 4e-05 | same gene group |
| [[HDAC4]] | -0.46 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ANAPC1]] | -0.46 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[TOMM40]] | -0.45 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[AGAP6]] | -0.45 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[NEU3]] | -0.45 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[SEC16A]] | -0.45 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[EARS2]] | -0.44 | -0.39 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB32]] | B | RAB32 activity raises SWAP70's level | lines that do not express RAB32 (7) vs lines expressing it (43) | 1.53× lower at baseline in the lines without RAB32 | 0.046 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.425). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-0.2, -38.0); signed map (-9.6, 13.8). **Vector** length 126, 35.0% of its response variance represented; |z| ≥ 3 in 1,144 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +8.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.2 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.6 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +6.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +4.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +4.1 | +4.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | -3.6 | -3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | -3.1 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | switching B cell complex subunit SWAP70 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:9,664,077-9,752,993 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0640, SWAP-70 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; EF-hand domain containing; Minor histocompatibility antigens |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 6 pathways, smallest: RAC2 GTPase cycle; RAC3 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UH65](https://www.uniprot.org/uniprotkb/Q9UH65) (Switch-associated protein 70):

> Phosphatidylinositol 3,4,5-trisphosphate-dependent guanine nucleotide exchange factor (GEF) which, independently of RAS, transduces signals from tyrosine kinase receptors to RAC. It also mediates signaling of membrane ruffling. Regulates the actin cytoskeleton as an effector or adapter protein in response to agonist stimulated phosphatidylinositol (3,4)-bisphosphate production and cell protrusion (By similarity).

**Summary**, from NCBI Gene [23075](https://www.ncbi.nlm.nih.gov/gene/23075):

> Enables cadherin binding activity. Predicted to be involved in regulation of small GTPase mediated signal transduction. Predicted to act upstream of or within isotype switching. Located in actin cytoskeleton; cytoplasm; and plasma membrane. Is active in postsynapse. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17070](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17070) · Entrez [23075](https://www.ncbi.nlm.nih.gov/gene/23075) · UniProt [Q9UH65](https://www.uniprot.org/uniprotkb/Q9UH65) · Ensembl [ENSG00000133789](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133789)

## Data

Gene col 5474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5474); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5474]; `tensor/DDL_lfc|DDL_z.npy` [5474]; `embed/gene_vectors.npy` [5474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5474 or target_col == 5474). Every well: [[SWAP70 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SWAP70.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
