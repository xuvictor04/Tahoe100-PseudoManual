---
symbol: "RTF1"
type: "gene"
col: 6073
ensembl_id: "ENSG00000137815"
name: "RTF1 homolog, Paf1/RNA polymerase II complex component"
location: "15q15.1"
module: 118
arm: "+"
pooled_cpm: 85.24
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# RTF1

*RTF1 homolog, Paf1/RNA polymerase II complex component* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.51× (z +19.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.810× (z -4.4, q 0.008, down in 25 of 49 measured lines) ⚠ cell-cycle shift, explains ~25% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.342×, NCI-H23 0.463×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (BT-474 0.139×; ⚠ toxic); [[Carbidopa (monohydrate) (drug)]] 0.5 µM in 1 line (SW 1088 0.0868×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HECTD4]] (+0.66, fdr 1e-05), [[ZNF446]] (+0.56, fdr 1e-05), [[WDR83]] (+0.54, fdr 4e-05); moves opposite to [[PTAR1]] (-0.50, fdr 2e-04), [[DAP]] (-0.49, fdr 2e-05), [[PHOSPHO2]] (-0.47, fdr 8e-05).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MEX3D]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6073.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.51×** | +19.0 | 0e+00 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +18.3 | 0e+00 | 46/49 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.28×** | +17.1 | 0e+00 | 48/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.18×** | +16.1 | 0e+00 | 48/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.50×** | +11.9 | 2e-30 | 39/48 (A498, NCI-H1792, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.9 | 2e-13 | 38/48 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.44×** | +7.3 | 2e-11 | 36/50 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +6.8 | 8e-10 | 37/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.40×** | +6.7 | 1e-09 | 34/48 (HEC-1-A, NCI-H1792, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +6.4 | 7e-09 | 36/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.74×** | +6.0 | 9e-08 | 36/49 (KATO III, COLO 205, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.7 | 1e-04 | 26/48 (HOP62, C32, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.49×** | +4.3 | 6e-04 | 33/47 (C32, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.001 | 23/49 (NCI-H23, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~72% of this change | **1.22×** | +4.2 | 0.001 | 27/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.001 | 23/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.5 | 0.012 | 17/48 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.044 | 13/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.066 | 15/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +2.8 | 0.086 | 13/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.30×** | +2.8 | 0.086 | 13/49 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6073.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.342×, NCI-H23 0.463×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (BT-474 0.139×; ⚠ toxic); [[Carbidopa (monohydrate) (drug)]] 0.5 µM in 1 line (SW 1088 0.0868×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.810×** | -4.4 | 0.008 | 25/49 (LoVo, C32, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6073. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 85.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +17.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +13.0) | — |
| [[A549 (line)]] | wt | 52.4 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 73.9 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +13.2) | — |
| [[HEC-1-A (line)]] | alt | 103 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +12.2) | — |
| [[LoVo (line)]] | wt | 101 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +14.6) | — |
| [[LOX-IMVI (line)]] | wt | 69.4 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 80.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.48× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 65.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +15.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.03× (z +11.6) | — |
| [[NCI-H2030 (line)]] | alt | 119 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +12.0) | — |
| [[NCI-H460 (line)]] | wt | 81.0 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +15.0) | — |
| [[RPMI-7951 (line)]] | alt | 90.9 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 50.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.32× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 84.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 75.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +14.9) | — |
| [[HS-578T (line)]] | alt | 52.7 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 101 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +13.3) | — |
| [[hTERT-HPNE (line)]] | wt | 67.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.06× (z +9.3) | — |
| [[KATO III (line)]] | alt | 98.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +13.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 96.4 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 89.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +12.8) | — |
| [[SW 900 (line)]] | alt | 77.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.51× (z +10.2) | — |
| [[SW1417 (line)]] | alt | 111 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.47× (z +11.8) | — |
| [[SW480 (line)]] | alt | 92.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +16.5) | — |
| [[H4 (line)]] | wt | 72.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 77.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 93.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +10.1) | — |
| [[A-427 (line)]] | wt | 62.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.51× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 88.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +10.1) | [[Lonafarnib (drug)]] 5 µM 0.139× (z -11.0) ⚠ toxic |
| [[C32 (line)]] | wt | 89.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +13.9) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 59.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.14× (z +11.4) | — |
| [[J82 (line)]] | alt | 91.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.17× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 49.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.27× (z +10.6) | — |
| [[RKO (line)]] | wt | 114 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +11.3) | — |
| [[SHP-77 (line)]] | alt | 92.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.58× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 73.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 64.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.32× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 125 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.45× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 59.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.463× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 95.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +11.4) | — |
| [[SW 1088 (line)]] | alt | 80.4 | 0 | 1 (1 ⚠) | — | [[Carbidopa (monohydrate) (drug)]] 0.5 µM 0.0868× (z -8.7) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 157 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 94.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6073), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 18 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HECTD4]] | +0.66 | +0.51 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[ZNF446]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[WDR83]] | +0.54 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[ZNF324]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[DHX8]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 | STRING 483 |
| [[PIAS1]] | +0.53 | +0.24 / +0.55 | both halves | 5e-04 |  |
| [[HDGFL2]] | +0.52 | +0.18 / +0.67 | ⚠ one half (not replicated) | 0.001 |  |
| [[C6orf47]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TPRN]] | +0.52 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[GPATCH8]] | +0.51 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TSEN34]] | +0.50 | +0.12 / +0.54 | ⚠ one half (not replicated) | 0.002 |  |
| [[COA3]] | +0.49 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[TLK2]] | +0.49 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[DCTN3]] | +0.48 | +0.25 / +0.57 | both halves | 4e-04 | pathway: Affinity selection of immunoglobulins |

## Genes that move opposite

*17 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTAR1]] | -0.50 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[DAP]] | -0.49 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PHOSPHO2]] | -0.47 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[HDDC2]] | -0.47 | -0.24 / -0.47 | both halves | 4e-04 |  |
| [[PEA15]] | -0.46 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[LINC03009]] | -0.46 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[SIKE1]] | -0.45 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[USP45]] | -0.44 | -0.16 / -0.39 | ⚠ not reproduced | 0.001 |  |
| [[CCND2]] | -0.44 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[CCDC169]] | -0.44 | -0.11 / -0.48 | ⚠ not reproduced | 0.002 |  |
| [[MIR30DHG]] | -0.44 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[ELK4]] | -0.43 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[HLA-K]] | -0.43 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[LENG8]] | -0.42 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEX3D]] | C | MEX3D's natural level weakens RTF1's drug response | MEX3D's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.03; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.515). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-45.4, -2.4); signed map (-8.0, -4.3). **Vector** length 84.6, 23.1% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.7 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +4.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.8 | +4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +2.5 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +18.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.0 | +0.5 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +1.9 | +2.1 |
|  | [[Thymol (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +1.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.6 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.9 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | -4.4 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | +1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | RTF1 homolog, Paf1/RNA polymerase II complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:41,408,408-41,483,563 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0252 |
| Gene groups (HGNC) | Paf1/RNA polymerase II complex |
| Reactome | 17 pathways, smallest: Dengue virus activates/modulates innate and adaptive immune responses; E3 ubiquitin ligases ubiquitinate target proteins; CHD1 and CHD2 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92541](https://www.uniprot.org/uniprotkb/Q92541) (RNA polymerase-associated protein RTF1 homolog):

> Component of the PAF1 complex (PAF1C) which has multiple functions during transcription by RNA polymerase II and is implicated in regulation of development and maintenance of embryonic stem cell pluripotency. PAF1C associates with RNA polymerase II through interaction with POLR2A CTD non-phosphorylated and 'Ser-2'- and 'Ser-5'-phosphorylated forms and is involved in transcriptional elongation, acting both independently and synergistically with TCEA1 and in cooperation with the DSIF complex and …

**Summary**, from NCBI Gene [23168](https://www.ncbi.nlm.nih.gov/gene/23168):

> This locus may represent a gene involved in regulation of transcription elongation and chromatin remodeling, based on studies of similar proteins in other organisms. The encoded protein may bind single-stranded DNA. [provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:28996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28996) · Entrez [23168](https://www.ncbi.nlm.nih.gov/gene/23168) · UniProt [Q92541](https://www.uniprot.org/uniprotkb/Q92541) · Ensembl [ENSG00000137815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137815)

## Data

Gene col 6073: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6073); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6073, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6073]; `tensor/DDL_lfc|DDL_z.npy` [6073]; `embed/gene_vectors.npy` [6073]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6073 or target_col == 6073). Every well: [[RTF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
