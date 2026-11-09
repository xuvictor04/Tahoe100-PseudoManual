---
symbol: "ZDBF2"
type: "gene"
col: 12828
ensembl_id: "ENSG00000204186"
name: "zinc finger DBF-type containing 2"
location: "2q33.3"
module: 23
arm: "+"
pooled_cpm: 43.89
n_lines_expressing: 36
n_dd_up: 2
n_dd_down: 27
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ZDBF2

*zinc finger DBF-type containing 2* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.23× (z +6.5, q 4e-08, up in 16 of 34 measured lines) ⚠ cell-cycle shift, explains ~61% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 4.08×; ⚠ cell-cycle shift, explains ~32% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 4.40×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 2.50×).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.406× (z -19.7, q 0e+00, down in 32 of 34 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.422× (z -18.9, q 0e+00, down in 31 of 34 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF563]] (+0.55, fdr 1e-04), [[THAP2]] (+0.55, fdr 1e-04), [[YAE1]] (+0.53, fdr 1e-04); moves opposite to [[PLXND1]] (-0.57, fdr 3e-05), [[CYRIB]] (-0.56, fdr 4e-05), [[SPIDR]] (-0.55, fdr 7e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[NFU1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12828.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 4.08×; ⚠ cell-cycle shift, explains ~32% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 4.40×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 2.50×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.23×** | +6.5 | 4e-08 | 16/34 (A-427, SW480, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.20×** | +4.1 | 0.010 | 13/34 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.9 | 0.010 | 10/33 (A498, A-427, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.9 | 0.010 | 10/34 (A-427, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.19× | +3.9 | 0.010 | 9/34 (C32, A-427, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.8 | 0.013 | 13/34 (LoVo, SW480, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.031 | 8/34 (HOP62, A-172, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.3 | 0.076 | 14/34 (A498, SHP-77, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.083 | 8/34 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.17× | +3.2 | 0.085 | 8/33 (NCI-H2030, HOP62, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.098 | 11/33 (SW480, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12828.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.406×** | -19.7 | 0e+00 | 32/34 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.422×** | -18.9 | 0e+00 | 31/34 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.484×** | -15.9 | 0e+00 | 31/34 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.502×** | -15.1 | 0e+00 | 26/34 (NCI-H1573, H4, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.492×** | -14.1 | 6e-43 | 30/33 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.640×** | -13.8 | 2e-41 | 25/34 (NCI-H1792, A-172, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.560×** | -12.7 | 4e-35 | 27/33 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.632×** | -10.0 | 7e-22 | 24/34 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.419×** | -10.0 | 2e-21 | 30/35 (NCI-H1573, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.647×** | -9.5 | 1e-19 | 24/34 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.648×** | -9.5 | 1e-19 | 25/34 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.630×** | -9.2 | 2e-18 | 19/31 (NCI-H23, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.678×** | -8.5 | 7e-16 | 25/34 (NCI-H460, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **0.678×** | -8.5 | 7e-16 | 23/33 (H4, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.658×** | -8.3 | 4e-15 | 22/34 (A-172, NCI-H1792, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.614×** | -5.6 | 7e-07 | 20/34 (A-427, NCI-H1573, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.767×** | -5.5 | 1e-06 | 19/34 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.639×** | -5.1 | 8e-06 | 20/34 (NCI-H23, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.819×** | -3.9 | 0.002 | 15/34 (C32, NCI-H1792, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.836× | -3.9 | 0.002 | 13/34 (SW 1088, HOP62, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.717×** | -3.8 | 0.003 | 12/34 (HOP62, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.788×** | -3.7 | 0.004 | 9/34 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.727×** | -3.6 | 0.006 | 11/33 (A-427, SW 1271, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.860× | -3.3 | 0.020 | 10/33 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.812×** | -3.2 | 0.023 | 10/34 (NCI-H23, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.850× | -3.2 | 0.024 | 8/34 (H4, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12828. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 78.0 | 5 (4 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +25.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.50× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -15.5) |
| [[A-172 (line)]] | wt | 147 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -15.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.478× (z -10.4) |
| [[H4 (line)]] | wt | 97.1 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -15.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.209× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 115 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.360× (z -11.4) |
| [[LoVo (line)]] | wt | 51.9 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -14.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.292× (z -12.6) |
| [[A-427 (line)]] | wt | 69.9 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.469× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 35.9 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.387× (z -9.2) |
| [[HOP62 (line)]] | alt | 117 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -19.4) |
| [[NCI-H1573 (line)]] | alt | 85.4 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.266× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.446× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 73.5 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -16.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.292× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 66.1 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -14.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.281× (z -13.7) |
| [[RKO (line)]] | wt | 42.8 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.290× (z -9.3) |
| [[SW480 (line)]] | alt | 50.3 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 40.4 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.272× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 42.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.393× (z -8.7) |
| [[C32 (line)]] | wt | 41.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -12.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.303× (z -8.6) |
| [[LS 180 (line)]] | wt | 19.9 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RPMI-7951 (line)]] | alt | 79.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[SW 900 (line)]] | alt | 52.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.252× (z -11.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.323× (z -10.1) |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 59.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.336× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 81.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.446× (z -8.6) |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.254× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -11.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 1271 (line)]] | alt | 154 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.51 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.94 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12828), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF563]] | +0.55 | +0.35 / +0.39 | both halves | 1e-04 |  |
| [[THAP2]] | +0.55 | +0.33 / +0.44 | both halves | 1e-04 |  |
| [[YAE1]] | +0.53 | +0.35 / +0.41 | both halves | 1e-04 |  |
| [[PIGP]] | +0.53 | +0.38 / +0.39 | both halves | 7e-05 |  |
| [[HSDL2-AS1]] | +0.52 | +0.27 / +0.41 | both halves | 3e-04 |  |
| [[MALINC1]] | +0.52 | +0.34 / +0.31 | both halves | 2e-04 |  |
| [[ZNF425]] | +0.52 | +0.36 / +0.34 | both halves | 1e-04 |  |
| [[ZNF160]] | +0.52 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[DCP1B]] | +0.52 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[ATE1OSP]] | +0.51 | +0.29 / +0.42 | both halves | 3e-04 |  |
| [[ZBTB21]] | +0.51 | +0.38 / +0.29 | both halves | 3e-04 |  |
| [[THAP1]] | +0.51 | +0.32 / +0.48 | both halves | 1e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXND1]] | -0.57 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[CYRIB]] | -0.56 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SPIDR]] | -0.55 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[TTLL5]] | -0.53 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[ABHD2]] | -0.52 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[RTTN]] | -0.51 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[NUP93]] | -0.51 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[MSH5]] | -0.51 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[PARP1]] | -0.49 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[CENPI]] | -0.49 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[ITPK1]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[TMEM245]] | -0.49 | -0.32 / -0.34 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFU1]] | B | ZDBF2 activity raises NFU1's level | lines that do not express ZDBF2 (14) vs lines expressing it (36) | 1.27× lower at baseline in the lines without ZDBF2 | 0.098 | ⚠ within organs, on part of the lines; also absent: WIPF1, MICU3, POPDC3 |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-4.0, 34.6); signed map (22.4, -11.3). **Vector** length 82.4, 19.2% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.3 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.8 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | -1.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.1 | -0.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.6 | -15.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.4 | -19.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.1 | -14.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.1 | -10.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -18.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -8.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 5 µM |  | -1.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger DBF-type containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:206,274,663-206,314,427 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ45338, KIAA1571 |
| Gene groups (HGNC) | Zinc fingers DBF-type |
| Matched by | ensembl_id |

UniProt [Q9HCK1](https://www.uniprot.org/uniprotkb/Q9HCK1) carries no function annotation.

**Summary**, from NCBI Gene [57683](https://www.ncbi.nlm.nih.gov/gene/57683):

> This gene encodes a protein containing DBF4-type zinc finger domains. This gene is imprinted and paternally expressed in lymphocytes but is more stochastically expressed in the placenta. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:29313](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29313) · Entrez [57683](https://www.ncbi.nlm.nih.gov/gene/57683) · UniProt [Q9HCK1](https://www.uniprot.org/uniprotkb/Q9HCK1) · Ensembl [ENSG00000204186](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204186)

## Data

Gene col 12828: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12828); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12828, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12828]; `tensor/DDL_lfc|DDL_z.npy` [12828]; `embed/gene_vectors.npy` [12828]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12828 or target_col == 12828). Every well: [[ZDBF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDBF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
