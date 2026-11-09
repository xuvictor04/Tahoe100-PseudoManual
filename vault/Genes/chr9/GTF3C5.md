---
symbol: "GTF3C5"
type: "gene"
col: 7263
ensembl_id: "ENSG00000148308"
name: "general transcription factor IIIC subunit 5"
location: "9q34.13"
module: 142
arm: "+"
pooled_cpm: 34.63
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# GTF3C5

*general transcription factor IIIC subunit 5* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +13.9, q 3e-41, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.695× (z -9.0, q 1e-16, down in 27 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.757× (z -8.4, q 1e-14, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (RKO 0.161×, NCI-H460 0.332×, NCI-H23 0.259×, COLO 205 0.339×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.0662×, PANC-1 0.192×, HCT15 0.191×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-423 0.178×, HepG2/C3A 0.209×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.177×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.428×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XAB2]] (+0.67, fdr 7e-06), [[IL17RA]] (+0.65, fdr 1e-05), [[OGFOD2]] (+0.61, fdr 2e-05); moves opposite to [[TMEM14C]] (-0.58, fdr 2e-05), [[AIG1]] (-0.56, fdr 3e-05), [[ALCAM]] (-0.53, fdr 3e-05).
> It is in [[Module 142]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7263.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +13.9 | 3e-41 | 40/48 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +10.1 | 2e-21 | 39/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +9.4 | 1e-18 | 39/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +7.6 | 4e-12 | 27/48 (COLO 205, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.32×** | +6.8 | 8e-10 | 26/48 (SW480, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +6.8 | 1e-09 | 23/48 (COLO 205, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.26×** | +5.8 | 5e-07 | 23/47 (COLO 205, LoVo, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.39×** | +5.8 | 5e-07 | 22/47 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.22×** | +4.7 | 1e-04 | 16/47 (HS-578T, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.7 | 2e-04 | 19/48 (COLO 205, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.6 | 3e-04 | 14/43 (RPMI-7951, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.001 | 15/46 (SW1417, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.14× | +4.1 | 0.002 | 13/48 (NCI-H23, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.004 | 9/47 (RPMI-7951, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.007 | 13/46 (HS-578T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.007 | 13/48 (SW480, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.026 | 7/48 (RPMI-7951, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.031 | 5/48 (LS 180, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.048 | 8/47 (Hs 766T, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[DTP3 (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.074 | 1/48 (CHP-212) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.18× | +2.9 | 0.087 | 4/47 (J82, HS-578T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7263.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (RKO 0.161×, NCI-H460 0.332×, NCI-H23 0.259×, COLO 205 0.339×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.0662×, PANC-1 0.192×, HCT15 0.191×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-423 0.178×, HepG2/C3A 0.209×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.177×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.428×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.695×** | -9.0 | 1e-16 | 27/46 (RKO, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.757×** | -8.4 | 1e-14 | 30/48 (AsPC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.623×** | -6.1 | 2e-07 | 21/49 (LOX-IMVI, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.755×** | -5.0 | 8e-05 | 23/43 (SW48, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.843× | -4.1 | 0.005 | 17/47 (SNU-423, HepG2/C3A, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.762×** | -3.5 | 0.042 | 12/34 (HepG2/C3A, H4, …) | top dose only | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.853× | -3.2 | 0.10 | 3/48 (HT-29, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.854× | -3.2 | 0.10 | 1/48 (CFPAC-1) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.881× | -3.1 | 0.11 | 11/47 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.883× | -3.1 | 0.12 | 8/48 (NCI-H2347, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7263. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 49.0 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.0662× (z -32.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 44.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +12.8) | — |
| [[NCI-H460 (line)]] | wt | 35.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -13.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -8.8) |
| [[BT-474 (line)]] | alt | 36.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 70.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -9.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.209× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 30.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 23.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.177× (z -10.1) |
| [[KATO III (line)]] | alt | 47.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.9) | — |
| [[LoVo (line)]] | wt | 28.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -11.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 65.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -18.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 28.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -10.3) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SNU-423 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.178× (z -14.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 37.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.0) | — |
| [[A-172 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7263), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XAB2]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[IL17RA]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[OGFOD2]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[VRK3]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ARL16]] | +0.61 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PDCL]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[EIF1AD]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[MED31]] | +0.57 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PEX16]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[ZNF500]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[BAHD1]] | +0.57 | +0.35 / +0.65 | both halves | 1e-04 |  |
| [[WDR83]] | +0.57 | +0.41 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM14C]] | -0.58 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[AIG1]] | -0.56 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[ALCAM]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PLCB4]] | -0.52 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[HNRNPC]] | -0.52 | -0.24 / -0.65 | both halves | 5e-04 |  |
| [[ARHGEF9]] | -0.51 | -0.37 / -0.54 | both halves | 7e-05 |  |
| [[NAB1]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[LEPROT]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[RFK]] | -0.50 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[LEKR1]] | -0.50 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[SEPTIN11]] | -0.50 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[YWHAE]] | -0.50 | -0.29 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.4, -4.4); signed map (-25.6, 7.0). **Vector** length 83.3, 16.9% of its response variance represented; |z| ≥ 3 in 703 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +5.4 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | +7.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +5.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | +2.7 | +4.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +6.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +3.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | -5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.0 | -8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | -9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.8 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | +0.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -0.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIIC subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13 — chr9:133,030,675-133,058,503 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TFiiiC2-63, TFIIIC63, TFIIICepsilon |
| Gene groups (HGNC) | MicroRNA protein coding host genes; General transcription factor IIIC complex subunits |
| Hallmark sets | KRAS_SIGNALING_DN, DNA_REPAIR |
| Reactome | 5 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 2 Promoter; RNA Polymerase III Transcription Initiation From Type 1 Promoter; RNA Polymerase III Transcription Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5Q8](https://www.uniprot.org/uniprotkb/Q9Y5Q8) (General transcription factor 3C polypeptide 5):

> Involved in RNA polymerase III-mediated transcription. Integral, tightly associated component of the DNA-binding TFIIIC2 subcomplex that directly binds tRNA and virus-associated RNA promoters.

**Summary**, from NCBI Gene [9328](https://www.ncbi.nlm.nih.gov/gene/9328):

> Enables RNA polymerase III general transcription initiation factor activity. Involved in transcription initiation at RNA polymerase III promoter. Located in nucleoplasm. Part of transcription factor TFIIIC complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4668](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4668) · Entrez [9328](https://www.ncbi.nlm.nih.gov/gene/9328) · UniProt [Q9Y5Q8](https://www.uniprot.org/uniprotkb/Q9Y5Q8) · Ensembl [ENSG00000148308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148308)

## Data

Gene col 7263: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7263); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7263, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7263]; `tensor/DDL_lfc|DDL_z.npy` [7263]; `embed/gene_vectors.npy` [7263]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7263 or target_col == 7263). Every well: [[GTF3C5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF3C5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
