---
symbol: "ZFYVE26"
type: "gene"
col: 1005
ensembl_id: "ENSG00000072121"
name: "zinc finger FYVE-type containing 26"
location: "14q24.1"
module: 122
arm: "+"
pooled_cpm: 39.25
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# ZFYVE26

*zinc finger FYVE-type containing 26* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.69× (z +12.0, q 2e-30, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.473× (z -11.3, q 8e-27, down in 37 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.632× (z -10.6, q 1e-23, down in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H23 0.101×, NCI-H460 0.178×, HCT15 0.115×, C-33 A 0.113×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SNU-423 0.174×, HepG2/C3A 0.115×, SW480 0.280×, MIA PaCa-2 0.228×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (Hs 766T 0.0890×, NCI-H23 0.170×, HCT15 0.191×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Tucidinostat (drug)]] 5 µM in 2 lines (LoVo 0.493×, SW480 0.575×); [[Tucidinostat (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.282×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.343×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC38A7]] (+0.76, fdr 7e-06), [[GPATCH3]] (+0.72, fdr 7e-06), [[VAC14]] (+0.67, fdr 7e-06); moves opposite to [[POGLUT2]] (-0.54, fdr 4e-05), [[PAPSS1]] (-0.54, fdr 5e-05), [[GOLIM4]] (-0.52, fdr 7e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1005.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +12.0 | 2e-30 | 30/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.75×** | +9.1 | 2e-17 | 36/48 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.46×** | +6.1 | 2e-07 | 26/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +5.5 | 6e-06 | 27/47 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.24×** | +4.9 | 1e-04 | 22/48 (CFPAC-1, SHP-77, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +4.7 | 2e-04 | 26/47 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +4.7 | 2e-04 | 27/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.22×** | +4.6 | 3e-04 | 22/48 (HOP62, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.32×** | +4.5 | 3e-04 | 25/48 (Panc 03.27, NCI-H460, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 5e-04 | 25/48 (J82, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.006 | 21/47 (BT-474, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.26×** | +3.8 | 0.007 | 17/48 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.28×** | +3.8 | 0.007 | 19/48 (LOX-IMVI, A-427, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.007 | 20/48 (A498, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.7 | 0.008 | 13/48 (AsPC-1, NCI-H2347, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.014 | 14/49 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.025 | 17/49 (HEC-1-A, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.48×** | +3.3 | 0.025 | 14/48 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.025 | 18/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.025 | 15/48 (LS 180, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.025 | 20/48 (SW1417, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1005.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H23 0.101×, NCI-H460 0.178×, HCT15 0.115×, C-33 A 0.113×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SNU-423 0.174×, HepG2/C3A 0.115×, SW480 0.280×, MIA PaCa-2 0.228×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (Hs 766T 0.0890×, NCI-H23 0.170×, HCT15 0.191×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Tucidinostat (drug)]] 5 µM in 2 lines (LoVo 0.493×, SW480 0.575×); [[Tucidinostat (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.282×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.343×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.473×** | -11.3 | 8e-27 | 37/47 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.632×** | -10.6 | 1e-23 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.602×** | -8.3 | 3e-14 | 44/48 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.599×** | -8.0 | 1e-13 | 28/47 (NCI-H23, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.682×** | -6.0 | 2e-07 | 26/41 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.740×** | -4.5 | 5e-04 | 24/44 (SNU-423, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.826× | -3.1 | 0.14 | 17/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1005. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 72.2 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 85.2 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -21.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 47.6 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +23.5) | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -17.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 59.6 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 31.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 37.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.0890× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 43.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW480 (line)]] | alt | 39.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.575× (z -8.6) |
| [[A-172 (line)]] | wt | 23.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.0) | [[Lonafarnib (drug)]] 5 µM 0.0775× (z -9.5) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 51.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.94× (z +13.0) | — |
| [[HCT15 (line)]] | alt | 45.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -14.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 34.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 68.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 54.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 47.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.335× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 39.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +16.5) | — |
| [[SK-MEL-2 (line)]] | alt | 50.9 | 0 | 2 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.282× (z -10.7) |
| [[A-427 (line)]] | wt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C-33 A (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -14.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 56.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +12.8) ⚠ cell-cycle shift, explains ~9% of this change | — |
| [[HepG2_C3A (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 33.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +10.9) | — |
| [[KATO III (line)]] | alt | 32.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +9.0) | — |
| [[LoVo (line)]] | wt | 28.8 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.493× (z -9.4) |
| [[PANC-1 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.399× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 55.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -10.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 46.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.1) ⚠ cell-cycle shift, explains ~9% of this change | — |
| [[SNU-1 (line)]] | wt | 44.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.187× (z -10.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1005), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC38A7]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[GPATCH3]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[VAC14]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[VPS11]] | +0.67 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SMCR8]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[GET3]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TMEM199]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[HEXA]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SPNS1]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NSMCE2]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[TSC1]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[WASHC2C]] | +0.58 | +0.52 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT2]] | -0.54 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[PAPSS1]] | -0.54 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[GOLIM4]] | -0.52 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[OSTF1]] | -0.52 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[ABHD10]] | -0.52 | -0.61 / -0.32 | both halves | 2e-04 |  |
| [[SSX2IP]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[WDFY2]] | -0.50 | -0.57 / -0.36 | both halves | 9e-05 | same gene group |
| [[HLTF]] | -0.50 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SDHAF3]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[WASF3]] | -0.49 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[HYCC1]] | -0.49 | -0.19 / -0.61 | ⚠ one half (not replicated) | 8e-04 |  |
| [[CYB5A]] | -0.48 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[GRB14]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-44.7, 11.6); signed map (-8.7, -20.1). **Vector** length 106, 27.5% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.6 | +9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.4 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.8 | +6.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.6 | +4.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.7 | +2.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.7 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -13.0 | -10.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -10.3 | -8.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -8.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.9 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.6 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.4 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger FYVE-type containing 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:67,727,374-67,816,590 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0321; previously SPG15 |
| Gene groups (HGNC) | Zinc fingers FYVE-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68DK2](https://www.uniprot.org/uniprotkb/Q68DK2) (Zinc finger FYVE domain-containing protein 26):

> Phosphatidylinositol 3-phosphate-binding protein required for the abscission step in cytokinesis: recruited to the midbody during cytokinesis and acts as a regulator of abscission. May also be required for efficient homologous recombination DNA double-strand break repair.

**Summary**, from NCBI Gene [23503](https://www.ncbi.nlm.nih.gov/gene/23503):

> This gene encodes a protein which contains a FYVE zinc finger binding domain. The presence of this domain is thought to target these proteins to membrane lipids through interaction with phospholipids in the membrane. Mutations in this gene are associated with autosomal recessive spastic paraplegia-15. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:20761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20761) · Entrez [23503](https://www.ncbi.nlm.nih.gov/gene/23503) · UniProt [Q68DK2](https://www.uniprot.org/uniprotkb/Q68DK2) · Ensembl [ENSG00000072121](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072121)

## Data

Gene col 1005: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1005); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1005, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1005]; `tensor/DDL_lfc|DDL_z.npy` [1005]; `embed/gene_vectors.npy` [1005]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1005 or target_col == 1005). Every well: [[ZFYVE26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFYVE26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
