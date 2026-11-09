---
symbol: "ZDHHC7"
type: "gene"
col: 7737
ensembl_id: "ENSG00000153786"
name: "zDHHC palmitoyltransferase 7"
location: "16q24.1"
module: 169
arm: "+"
pooled_cpm: 40.4
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# ZDHHC7

*zDHHC palmitoyltransferase 7* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 2.34× (z +9.6, q 6e-19, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.717× (z -10.1, q 2e-21, down in 31 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.763× (z -5.8, q 6e-07, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1792 0.0513×, NCI-H2030 0.168×, HEC-1-A 0.328×, LS 180 0.279×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2030 0.478×, NCI-H460 0.451×, SNU-1 0.378×, NCI-H1792 0.406×; ⚠ cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HEC-1-A 0.222×, NCI-H1573 0.222×, LOX-IMVI 0.274×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change); [[Hydroxyfasudil (drug)]] 5 µM in 1 line (SHP-77 0.0565×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.421×); [[Silodosin (drug)]] 5 µM in 1 line (AN3 CA 0.0959×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF7]] (+0.66, fdr 1e-05), [[RNF4]] (+0.64, fdr 7e-06), [[WDR5]] (+0.62, fdr 7e-06); moves opposite to [[JUN]] (-0.57, fdr 1e-05), [[TRAF1]] (-0.56, fdr 1e-05), [[SKIL]] (-0.56, fdr 1e-05).
> It is in [[Module 169]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7737.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.34×** | +9.6 | 6e-19 | 40/47 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.09×** | +8.3 | 2e-14 | 35/49 (SW480, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.22×** | +6.0 | 3e-07 | 26/48 (A-172, SW480, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +5.3 | 2e-05 | 19/48 (NCI-H1792, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.1 | 0.004 | 11/33 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.005 | 16/48 (C32, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +3.9 | 0.008 | 17/47 (BT-474, SW48, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.009 | 15/48 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.13× | +3.7 | 0.015 | 17/47 (MIA PaCa-2, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.037 | 17/48 (RKO, AN3 CA, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.17× | +3.3 | 0.045 | 12/47 (NCI-H23, HOP62, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.090 | 9/47 (HepG2/C3A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.15× | +3.1 | 0.090 | 13/48 (A-427, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7737.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1792 0.0513×, NCI-H2030 0.168×, HEC-1-A 0.328×, LS 180 0.279×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2030 0.478×, NCI-H460 0.451×, SNU-1 0.378×, NCI-H1792 0.406×; ⚠ cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HEC-1-A 0.222×, NCI-H1573 0.222×, LOX-IMVI 0.274×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change); [[Hydroxyfasudil (drug)]] 5 µM in 1 line (SHP-77 0.0565×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.421×); [[Silodosin (drug)]] 5 µM in 1 line (AN3 CA 0.0959×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.717×** | -10.1 | 2e-21 | 31/47 (NCI-H2030, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.660×** | -9.0 | 1e-16 | 32/45 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.675×** | -8.1 | 7e-14 | 24/39 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.746×** | -6.1 | 2e-07 | 26/48 (SNU-1, J82, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -5.8 | 6e-07 | 29/48 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.771×** | -5.6 | 2e-06 | 21/47 (LOX-IMVI, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7737. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 97.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.421× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 79.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -19.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 44.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[LOX-IMVI (line)]] | wt | 39.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[MIA PaCa-2 (line)]] | alt | 42.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 42.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0513× (z -25.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 33.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[A-172 (line)]] | wt | 34.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 70.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.497× (z -9.3) ⚠ cell-cycle shift, explains ~20% of this change |
| [[A549 (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -8.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 29.4 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0959× (z -8.7) |
| [[C32 (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HOP62 (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -10.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 44.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[NCI-H460 (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -11.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -10.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SHP-77 (line)]] | alt | 33.7 | 0 | 1 | — | [[Hydroxyfasudil (drug)]] 5 µM 0.0565× (z -11.5) |
| [[A-427 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7737), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF7]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[RNF4]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[WDR5]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PHB2]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[LRIG2]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[COPS7B]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[TBC1D14]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[JKAMP]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ASB7]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | +0.58 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CLASP1]] | +0.58 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[GIT2]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUN]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 | pathway: ESR-mediated signaling |
| [[TRAF1]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SKIL]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[OLFM2]] | -0.55 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[DPH1-AS1]] | -0.55 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[KIAA1217]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[NANOS3]] | -0.54 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[NOTCH2NLB]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[CXCL8]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[HDX]] | -0.54 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[RPS6KA3]] | -0.53 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[ERCC6L2]] | -0.53 | -0.60 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.4, -15.5); signed map (-41.6, -12.6). **Vector** length 93.9, 19.8% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +9.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +8.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.9 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.9 | +1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.7 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -8.7 | -10.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -7.6 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.4 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.0 | -5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | -8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -0.9 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:84,974,175-85,011,535 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10792, ZNF370, FLJ20279, SERZ-B, SERZ1, DHHC7 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Reactome | 3 pathways, smallest: Extra-nuclear estrogen signaling; ESR-mediated signaling; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXF8](https://www.uniprot.org/uniprotkb/Q9NXF8) (Palmitoyltransferase ZDHHC7):

> Golgi-localized palmitoyltransferase that catalyzes the addition of palmitate onto various protein substrates and therefore functions in several unrelated biological processes. Has no stringent fatty acid selectivity and in addition to palmitate can also transfer onto target proteins myristate from tetradecanoyl-CoA and stearate from octadecanoyl-CoA (By similarity). Palmitoylates sex steroid hormone receptors, including ESR1, PGR and AR, thereby regulating their targeting to the plasma …

**Summary**, from NCBI Gene [55625](https://www.ncbi.nlm.nih.gov/gene/55625):

> Enables protein-cysteine S-palmitoyltransferase activity. Involved in several processes, including nuclear receptor-mediated steroid hormone signaling pathway; peptidyl-L-cysteine S-palmitoylation; and regulation of signal transduction. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18459](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18459) · Entrez [55625](https://www.ncbi.nlm.nih.gov/gene/55625) · UniProt [Q9NXF8](https://www.uniprot.org/uniprotkb/Q9NXF8) · Ensembl [ENSG00000153786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153786)

## Data

Gene col 7737: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7737); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7737, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7737]; `tensor/DDL_lfc|DDL_z.npy` [7737]; `embed/gene_vectors.npy` [7737]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7737 or target_col == 7737). Every well: [[ZDHHC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
