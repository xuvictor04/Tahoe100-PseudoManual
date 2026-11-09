---
symbol: "INTS9"
type: "gene"
col: 2435
ensembl_id: "ENSG00000104299"
name: "integrator complex subunit 9"
location: "8p21.1"
module: 169
arm: "+"
pooled_cpm: 29.83
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# INTS9

*integrator complex subunit 9* — 8p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.80× (z +14.6, q 1e-45, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.444× (z -19.5, q 0e+00, down in 28 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.842× (z -4.3, q 0.001, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LoVo 0.0635×, NCI-H1573 0.101×, SHP-77 0.172×, C-33 A 0.101×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1792 0.0727×, SW480 0.258×, KATO III 0.201×, LoVo 0.162×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (HEC-1-A 0.0534×, RPMI-7951 0.0578×, KATO III 0.166×, A-427 0.168×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.515×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDT2]] (+0.63, fdr 2e-05), [[FASTKD1]] (+0.62, fdr 1e-05), [[TM2D1]] (+0.60, fdr 1e-05); moves opposite to [[CSRP1]] (-0.57, fdr 1e-05), [[CREB3]] (-0.54, fdr 1e-04), [[SLC9A3R1]] (-0.50, fdr 4e-05).
> It is in [[Module 169]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2435.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +14.6 | 1e-45 | 37/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +13.6 | 6e-40 | 36/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +12.1 | 3e-31 | 33/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.56×** | +11.0 | 3e-26 | 31/48 (AsPC-1, A498, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +9.6 | 1e-19 | 31/47 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +8.9 | 5e-17 | 31/46 (SHP-77, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.43×** | +8.8 | 9e-17 | 32/48 (AsPC-1, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.26×** | +8.2 | 1e-14 | 27/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +7.5 | 4e-12 | 30/48 (NCI-H2030, AsPC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +7.5 | 5e-12 | 26/48 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.36×** | +7.4 | 8e-12 | 26/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +6.2 | 3e-08 | 21/48 (A-172, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +5.8 | 4e-07 | 21/48 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +5.6 | 9e-07 | 14/48 (H4, NCI-H1792, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.27×** | +5.5 | 1e-06 | 22/48 (HS-578T, SW 1271, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +5.1 | 1e-05 | 17/47 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +4.2 | 6e-04 | 16/48 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +4.2 | 6e-04 | 14/48 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.15× | +3.4 | 0.013 | 4/48 (LS 180, NCI-H2347, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.017 | 4/48 (LOX-IMVI, A-427, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.017 | 6/48 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | 1.14× | +3.3 | 0.017 | 3/48 (CFPAC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2435.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LoVo 0.0635×, NCI-H1573 0.101×, SHP-77 0.172×, C-33 A 0.101×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1792 0.0727×, SW480 0.258×, KATO III 0.201×, LoVo 0.162×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (HEC-1-A 0.0534×, RPMI-7951 0.0578×, KATO III 0.166×, A-427 0.168×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.515×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.444×** | -19.5 | 0e+00 | 28/37 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.550×** | -13.8 | 5e-41 | 25/44 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.595×** | -13.0 | 2e-36 | 35/46 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 0.847× | -5.9 | 5e-07 | 20/48 (A-427, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **0.832×** | -4.6 | 5e-04 | 21/46 (A498, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 0.842× | -4.3 | 0.001 | 20/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.839× | -4.2 | 0.002 | 14/48 (AN3 CA, RKO, …) | rises with dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.818×** | -3.6 | 0.022 | 17/45 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.880× | -3.2 | 0.071 | 11/48 (NCI-H460, RKO, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.876× | -3.2 | 0.071 | 11/47 (SW 1271, AsPC-1, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.837× | -3.2 | 0.071 | 8/47 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2435. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 44.5 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.515× (z -9.1) |
| [[A498 (line)]] | wt | 12.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.32× (z +9.5) | [[Docetaxel (drug)]] 0.05 µM 0.262× (z -10.6) ⚠ transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HEC-1-A (line)]] | alt | 37.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0534× (z -29.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 35.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -13.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 58.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -18.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 27.2 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.52× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0635× (z -27.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 38.0 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -10.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 47.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0578× (z -22.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 85.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -20.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 52.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -17.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 16.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.70× (z +9.5) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.181× (z -10.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 46.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -17.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 37.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 23.4 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.36× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -20.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 26.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 28.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -17.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -14.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -9.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.142× (z -9.4) ⚠ cell-cycle shift, explains ~57% of this change |
| [[Hs 766T (line)]] | wt | 29.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0994× (z -16.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.124× (z -8.9) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0727× (z -20.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -16.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 21.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +8.5) | — |
| [[RKO (line)]] | wt | 48.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -13.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.102× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[BT-474 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2435), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT2]] | +0.63 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[FASTKD1]] | +0.62 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[TM2D1]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[PPHLN1]] | +0.60 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[HIGD2A]] | +0.58 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[ORC2]] | +0.58 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[COA6]] | +0.57 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[LARS2]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[FNTB]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[TYW1]] | +0.57 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[PDSS2]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[TCTN3]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSRP1]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[CREB3]] | -0.54 | -0.63 / -0.34 | both halves | 1e-04 |  |
| [[SLC9A3R1]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[MYO1C]] | -0.50 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[EMD]] | -0.49 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[ALAS1]] | -0.49 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[GFUS]] | -0.49 | -0.68 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |
| [[PITPNM1]] | -0.49 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[BCL7B]] | -0.48 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[JUNB]] | -0.48 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[ZYX]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[FLII]] | -0.48 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[SRSF3]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | INTS9's natural level raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | INTS9's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.490 over the table, 0.078 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.0, -8.2); signed map (-42.3, -21.2). **Vector** length 88.0, 18.2% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +8.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.0 | +9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.9 | +14.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.2 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +6.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -7.5 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -5.5 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.0 | -13.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.4 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -2.5 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.1 — chr8:28,767,661-28,890,242 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10871, CPSF2L, RC-74 |
| Gene groups (HGNC) | Integrator complex; MBL fold containing DNA/RNA interacting subfamily |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NV88](https://www.uniprot.org/uniprotkb/Q9NV88) (Integrator complex subunit 9):

> Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol II subunit …

**Summary**, from NCBI Gene [55756](https://www.ncbi.nlm.nih.gov/gene/55756):

> This gene encodes a subunit of the Integrator complex. This protein complex binds the C-terminal domain of RNA polymerase II and likely plays a role in small nuclear RNA processing. The encoded protein has similarities to the subunits of the cleavage and polyadenylation specificity factor complex. Alternatively spliced transcript variants have been described.[provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:25592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25592) · Entrez [55756](https://www.ncbi.nlm.nih.gov/gene/55756) · UniProt [Q9NV88](https://www.uniprot.org/uniprotkb/Q9NV88) · Ensembl [ENSG00000104299](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104299)

## Data

Gene col 2435: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2435); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2435, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2435]; `tensor/DDL_lfc|DDL_z.npy` [2435]; `embed/gene_vectors.npy` [2435]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2435 or target_col == 2435). Every well: [[INTS9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
