---
symbol: "SLC35E3"
type: "gene"
col: 10648
ensembl_id: "ENSG00000175782"
name: "solute carrier family 35 member E3"
location: "12q15"
module: 144
arm: "+"
pooled_cpm: 54.16
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# SLC35E3

*solute carrier family 35 member E3* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.32× (z +7.0, q 1e-09, up in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~64% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.30× (z +6.6, q 6e-09, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.469× (z -14.2, q 8e-43, down in 37 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.638× (z -8.7, q 3e-16, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C4orf47]] (+0.67, fdr 7e-06), [[DDB2]] (+0.63, fdr 1e-05), [[POM121C]] (+0.63, fdr 1e-05); moves opposite to [[HUWE1]] (-0.54, fdr 1e-05), [[XRN2]] (-0.54, fdr 3e-05), [[FAT1]] (-0.53, fdr 2e-05).
> It is in [[Module 144]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10648.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.32×** | +7.0 | 1e-09 | 30/48 (LoVo, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +6.9 | 2e-09 | 33/47 (SNU-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.6 | 6e-09 | 29/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.1 | 2e-07 | 28/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +5.8 | 7e-07 | 30/48 (LoVo, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.34×** | +5.7 | 8e-07 | 30/48 (LoVo, A-427, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +5.1 | 2e-05 | 24/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +5.0 | 5e-05 | 22/48 (HT-29, SW480, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +4.7 | 1e-04 | 24/48 (RKO, LS 180, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +4.5 | 3e-04 | 25/48 (SNU-1, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.23×** | +4.0 | 0.003 | 22/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.007 | 16/48 (C-33 A, HepG2/C3A, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.16× | +3.7 | 0.010 | 16/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.038 | 16/49 (SW480, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.038 | 21/49 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.051 | 13/48 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.065 | 11/50 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.12× | +3.1 | 0.066 | 11/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.076 | 11/48 (NCI-H23, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10648.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.469×** | -14.2 | 8e-43 | 37/47 (HCT15, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.487×** | -13.4 | 1e-38 | 35/43 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.524×** | -12.1 | 3e-31 | 39/48 (C32, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.569×** | -10.9 | 1e-25 | 36/48 (NCI-H23, C32, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.687×** | -9.3 | 1e-18 | 32/48 (HEC-1-A, A549, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.638×** | -8.7 | 3e-16 | 33/48 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.619×** | -8.6 | 6e-16 | 30/45 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.679×** | -7.5 | 4e-12 | 33/48 (CFPAC-1, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.727×** | -6.2 | 4e-08 | 31/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.779×** | -4.8 | 7e-05 | 23/48 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.799×** | -4.1 | 0.002 | 23/48 (CFPAC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.669×** | -4.1 | 0.002 | 19/45 (RPMI-7951, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **0.819×** | -3.9 | 0.005 | 21/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.683×** | -3.9 | 0.005 | 19/49 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.833× | -3.5 | 0.017 | 21/48 (NCI-H1792, HCT15, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.720×** | -3.3 | 0.029 | 14/48 (LOX-IMVI, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10648. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 105 | 0 | 11 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -18.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 56.4 | 0 | 7 (7 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0731× (z -15.7) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 69.2 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -14.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 74.5 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H460 (line)]] | wt | 62.8 | 3 (1 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +11.9) | [[Harringtonine (drug)]] 5 µM 0.380× (z -10.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 93.7 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 69.9 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.247× (z -13.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 54.6 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.249× (z -12.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[CFPAC-1 (line)]] | alt | 51.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -12.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 52.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.406× (z -8.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 59.1 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.293× (z -11.8) ⚠ toxic |
| [[A-427 (line)]] | wt | 102 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0892× (z -26.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 47.1 | 1 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +11.5) | [[Harringtonine (drug)]] 5 µM 0.328× (z -10.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[C-33 A (line)]] | alt | 104 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HepG2_C3A (line)]] | wt | 95.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -9.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[NCI-H1573 (line)]] | alt | 60.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[RPMI-7951 (line)]] | alt | 64.9 | 0 | 3 (3 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0916× (z -10.7) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 54.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -8.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 61.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -12.2) ⚠ cell-cycle shift, explains ~72% of this change |
| [[HS-578T (line)]] | alt | 53.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -12.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 48.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 85.7 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.386× (z -9.7) ⚠ cell-cycle shift, explains ~64% of this change |
| [[NCI-H2030 (line)]] | alt | 41.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.274× (z -11.5) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 76.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[RKO (line)]] | wt | 49.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -11.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 49.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -14.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 41.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -10.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.145× (z -10.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 81.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.231× (z -12.0) ⚠ toxic |
| [[HOP62 (line)]] | alt | 58.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 36.5 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 48.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -12.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 47.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[AsPC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10648), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C4orf47]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[DDB2]] | +0.63 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[POM121C]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[C9orf153]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[VPS13B-DT]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[FUT11]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[AKAP10]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[BCL2L2-PABPN1]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[TRNAU1AP]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[ZNF8-DT]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SMIM4]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[VDAC1P8]] | +0.58 | +0.58 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HUWE1]] | -0.54 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[XRN2]] | -0.54 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[FAT1]] | -0.53 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[BCL7B]] | -0.52 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ARAF]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[RUVBL1]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[PRELID3B]] | -0.51 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[TJP1]] | -0.50 | -0.49 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.7, 28.4); signed map (-2.1, 5.0). **Vector** length 121, 36.1% of its response variance represented; |z| ≥ 3 in 1,214 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +9.2 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +6.3 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +6.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +4.8 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +5.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +4.1 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +0.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.5 | +2.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -5.8 | -10.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.8 | -14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -13.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.8 | -12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.0 | -8.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.5 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.2 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member E3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:68,746,125-68,793,964 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BLOV1 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z769](https://www.uniprot.org/uniprotkb/Q7Z769) (Solute carrier family 35 member E3):

> Putative transporter.

**Summary**, from NCBI Gene [55508](https://www.ncbi.nlm.nih.gov/gene/55508):

> Predicted to enable antiporter activity and nucleotide-sugar transmembrane transporter activity. Predicted to be involved in transmembrane transport. Predicted to be located in membrane. Predicted to be active in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20864](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20864) · Entrez [55508](https://www.ncbi.nlm.nih.gov/gene/55508) · UniProt [Q7Z769](https://www.uniprot.org/uniprotkb/Q7Z769) · Ensembl [ENSG00000175782](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175782)

## Data

Gene col 10648: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10648); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10648, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10648]; `tensor/DDL_lfc|DDL_z.npy` [10648]; `embed/gene_vectors.npy` [10648]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10648 or target_col == 10648). Every well: [[SLC35E3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35E3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
