---
symbol: "INCENP"
type: "gene"
col: 7380
ensembl_id: "ENSG00000149503"
name: "inner centromere protein"
location: "11q12.3"
module: 22
arm: "+"
pooled_cpm: 44.17
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 32
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# INCENP

*inner centromere protein* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (17 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.72× (z +7.9, q 2e-12, up in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~69% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.16× (z +5.8, q 6e-07, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (NCI-H2030 3.99×, PANC-1 2.92×, RKO 3.37×, Panc 03.27 2.70×, …; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 3.47×, KATO III 3.47×; ⚠ cell-cycle shift, explains ~69% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 3.52×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (16 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.662× (z -8.4, q 2e-14, down in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~81% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.724× (z -6.6, q 8e-09, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BUB1B]] (+0.94, fdr 7e-06), [[ARHGAP11A]] (+0.92, fdr 7e-06), [[RACGAP1]] (+0.90, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 18 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7380.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (NCI-H2030 3.99×, PANC-1 2.92×, RKO 3.37×, Panc 03.27 2.70×, …; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 3.47×, KATO III 3.47×; ⚠ cell-cycle shift, explains ~69% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 3.52×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.72×** | +7.9 | 2e-12 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.55×** | +7.1 | 4e-10 | 35/48 (RKO, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | **1.57×** | +6.6 | 1e-08 | 33/46 (NCI-H460, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.56×** | +6.4 | 2e-08 | 32/47 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.52×** | +6.1 | 2e-07 | 29/48 (A549, SW480, …) | two highest doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.16×** | +5.8 | 6e-07 | 30/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **2.15×** | +5.8 | 6e-07 | 30/47 (J82, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.48×** | +5.7 | 8e-07 | 29/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.44×** | +5.3 | 9e-06 | 30/48 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.41×** | +5.0 | 3e-05 | 27/48 (SW480, AsPC-1, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.41×** | +4.9 | 4e-05 | 24/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.38×** | +4.7 | 1e-04 | 24/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +4.6 | 2e-04 | 23/48 (NCI-H2030, PANC-1, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.31×** | +3.9 | 0.004 | 23/48 (A549, SW480, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +3.7 | 0.009 | 21/48 (PANC-1, C32, …) | top dose only | composition shift; position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.046 | 17/48 (NCI-H23, SW 900, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7380.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.662×** | -8.4 | 2e-14 | 38/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.586×** | -7.7 | 3e-12 | 37/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -6.6 | 8e-09 | 29/48 (LS 180, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.642×** | -6.4 | 2e-08 | 30/48 (SK-MEL-2, HEC-1-A, …) | top dose only | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.790×** | -4.8 | 2e-04 | 24/48 (RKO, HCT15, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.795×** | -4.7 | 3e-04 | 24/48 (A-427, LS 180, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.798×** | -4.6 | 3e-04 | 22/48 (SK-MEL-2, PANC-1, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.742×** | -4.3 | 0.001 | 22/48 (SHP-77, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.741×** | -4.2 | 0.002 | 26/48 (NCI-H661, A549, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.680×** | -4.0 | 0.004 | 17/47 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.754×** | -3.9 | 0.004 | 20/47 (A549, NCI-H2347, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.829×** | -3.8 | 0.006 | 21/48 (Hs 766T, A-427, …) | rises with dose | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **0.831×** | -3.8 | 0.007 | 22/48 (A-172, LOX-IMVI, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **0.609×** | -3.7 | 0.007 | 19/42 (A-172, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.777×** | -3.6 | 0.010 | 19/47 (SNU-1, A549, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.838× | -3.6 | 0.011 | 13/48 (SK-MEL-2, AN3 CA, …) | top dose only | position effect removed |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | **0.790×** | -3.4 | 0.020 | 16/48 (HCT15, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.646×** | -3.3 | 0.025 | 15/48 (H4, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.785×** | -3.2 | 0.029 | 17/48 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.857× | -3.1 | 0.036 | 16/48 (SW480, HCT15, …) | all doses, flat |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **0.815×** | -2.9 | 0.067 | 14/45 (HepG2/C3A, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.817×** | -2.9 | 0.070 | 20/48 (A-427, A498, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.754×** | -2.9 | 0.070 | 16/48 (HCT15, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7380. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 38.8 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.269× (z -13.5) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.293× (z -8.9) |
| [[A-427 (line)]] | wt | 89.9 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.243× (z -15.8) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.471× (z -8.5) |
| [[H4 (line)]] | wt | 47.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0906× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -8.8) |
| [[A-172 (line)]] | wt | 33.6 | 0 | 2 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.235× (z -11.4) ⚠ cell-cycle shift, explains ~70% of this change |
| [[A549 (line)]] | wt | 38.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.285× (z -8.8) ⚠ cell-cycle shift, explains ~70% of this change |
| [[KATO III (line)]] | alt | 46.4 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.52× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | — |
| [[LS 180 (line)]] | wt | 37.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -9.6) |
| [[PANC-1 (line)]] | alt | 41.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 36.2 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.219× (z -11.4) |
| [[A498 (line)]] | wt | 30.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.383× (z -10.5) ⚠ cell-cycle shift, explains ~81% of this change |
| [[COLO 205 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0916× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 56.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.365× (z -11.1) ⚠ cell-cycle shift, explains ~81% of this change |
| [[HS-578T (line)]] | alt | 37.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 48.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +15.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 46.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 50.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 45.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +12.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 38.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 68.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7380), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BUB1B]] | +0.94 | +0.92 / +0.94 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 912 |
| [[ARHGAP11A]] | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | **novel candidate** |
| [[RACGAP1]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 920 |
| [[CIT]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 691 |
| [[CCNA2]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 628 |
| [[KIF23]] | +0.90 | +0.87 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 977 |
| [[KIF4A]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 748 |
| [[DLGAP5]] | +0.90 | +0.87 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 806 |
| [[BUB1]] | +0.89 | +0.87 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 864 |
| [[TPX2]] | +0.88 | +0.87 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 679 |
| [[NCAPH]] | +0.88 | +0.87 / +0.86 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 584 |
| [[MKI67]] | +0.88 | +0.86 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 525 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises INCENP's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.04× lower at baseline in the lines without PIMREG | 0.017 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises INCENP's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.81× lower at baseline in the lines without NEURL1B | 0.037 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[NDC80]] | C | NDC80 activity raises INCENP's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.24× lower at baseline in the lines without NDC80 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises INCENP's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.35× lower at baseline in the lines without AURKB | 0.042 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises INCENP's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[SKA3]] | C | SKA3 activity raises INCENP's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 2.57× lower at baseline in the lines without SKA3 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises INCENP's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[PBK]] | C | PBK activity raises INCENP's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without PBK | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[SAPCD2]] | C | SAPCD2 activity raises INCENP's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.09× lower at baseline in the lines without SAPCD2 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises INCENP's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.905). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.5, -54.9); signed map (-48.4, -42.5). **Vector** length 147, 48.8% of its response variance represented; |z| ≥ 3 in 1,245 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.81 to 28); *E2F targets* (hallmark, mean cos +0.70 to 46); *G2/M Transition* (reactome, mean cos +0.69 to 28).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | +6.4 | +6.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +5.1 | +5.8 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +4.5 | +3.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.3 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +5.8 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.0 | +2.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.6 | +2.4 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +2.4 | +3.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -7.7 | -8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.4 | -6.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -7.0 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -5.0 | -3.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.8 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | inner centromere protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,123,998-62,153,169 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31633 |
| Gene groups (HGNC) | Chromosomal passenger complex |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 20 pathways, smallest: SUMOylation of DNA replication proteins; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQS7](https://www.uniprot.org/uniprotkb/Q9NQS7) (Inner centromere protein):

> Component of the chromosomal passenger complex (CPC), a complex that acts as a key regulator of mitosis. The CPC complex has essential functions at the centromere in ensuring correct chromosome alignment and segregation and is required for chromatin-induced microtubule stabilization and spindle assembly. Acts as a scaffold regulating CPC localization and activity. The C-terminus associates with AURKB or AURKC, the N-terminus associated with BIRC5/survivin and CDCA8/borealin tethers the CPC to …

**Summary**, from NCBI Gene [3619](https://www.ncbi.nlm.nih.gov/gene/3619):

> In mammalian cells, 2 broad groups of centromere-interacting proteins have been described: constitutively binding centromere proteins and 'passenger,' or transiently interacting, proteins (reviewed by Choo, 1997). The constitutive proteins include CENPA (centromere protein A; MIM 117139), CENPB (MIM 117140), CENPC1 (MIM 117141), and CENPD (MIM 117142). The term 'passenger proteins' encompasses a broad collection of proteins that localize to the centromere during specific stages of the cell …

**Accessions** — [HGNC:6058](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6058) · Entrez [3619](https://www.ncbi.nlm.nih.gov/gene/3619) · UniProt [Q9NQS7](https://www.uniprot.org/uniprotkb/Q9NQS7) · Ensembl [ENSG00000149503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149503)

## Data

Gene col 7380: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7380); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7380, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7380]; `tensor/DDL_lfc|DDL_z.npy` [7380]; `embed/gene_vectors.npy` [7380]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7380 or target_col == 7380). Every well: [[INCENP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INCENP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
