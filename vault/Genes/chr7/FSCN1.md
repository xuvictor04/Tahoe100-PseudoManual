---
symbol: "FSCN1"
type: "gene"
col: 1125
ensembl_id: "ENSG00000075618"
name: "fascin actin-bundling protein 1"
location: "7p22.1"
module: 84
arm: "+"
pooled_cpm: 82.78
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 5
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# FSCN1

*fascin actin-bundling protein 1* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.09× (z +8.4, q 3e-14, up in 38 of 44 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +8.2, q 7e-14, up in 32 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 2 lines (H4 0.254×, HOP62 0.387×; ⚠ cell-cycle shift, explains ~23% of this change); [[Trametinib (drug)]] 5 µM in 2 lines (AsPC-1 0.342×, NCI-H1573 0.220×; ⚠ cell-cycle shift, explains ~32% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (A-172 0.379×, H4 0.386×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.443×); [[Cobimetinib (drug)]] 5 µM in 1 line (AsPC-1 0.324×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A-172 0.372×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFRSF10D]] (+0.68, fdr 7e-06), [[SNAI1]] (+0.66, fdr 1e-05), [[RIN1]] (+0.65, fdr 1e-05); moves opposite to [[QRSL1]] (-0.61, fdr 1e-05), [[LARP4]] (-0.58, fdr 1e-05), [[MGST1]] (-0.57, fdr 3e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LGALS1]] → it (grade B ⚠); 5 go from it, the strongest it → [[KCNN4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.09×** | +8.4 | 3e-14 | 38/44 (SW480, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +8.2 | 7e-14 | 32/45 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.62×** | +7.7 | 3e-12 | 30/44 (PANC-1, A498, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.92×** | +7.4 | 2e-11 | 36/44 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.81×** | +6.7 | 2e-09 | 35/44 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +5.6 | 2e-06 | 33/44 (MIA PaCa-2, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.68×** | +5.1 | 3e-05 | 27/44 (PANC-1, A498, …) | top dose only | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +4.3 | 0.001 | 28/44 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.004 | 28/44 (A-427, J82, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.9 | 0.005 | 25/43 (LOX-IMVI, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.019 | 26/45 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.33×** | +3.2 | 0.069 | 24/44 (A498, PANC-1, …) | inconsistent across doses | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1125.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 2 lines (H4 0.254×, HOP62 0.387×; ⚠ cell-cycle shift, explains ~23% of this change); [[Trametinib (drug)]] 5 µM in 2 lines (AsPC-1 0.342×, NCI-H1573 0.220×; ⚠ cell-cycle shift, explains ~32% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (A-172 0.379×, H4 0.386×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.443×); [[Cobimetinib (drug)]] 5 µM in 1 line (AsPC-1 0.324×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A-172 0.372×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | 0.549× | -3.6 | 0.12 | 27/46 (AsPC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.691× | -3.5 | 0.12 | 25/46 (AsPC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.724× | -3.4 | 0.12 | 23/44 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.748× | -3.3 | 0.12 | 23/43 (A-172, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.750× | -3.3 | 0.12 | 24/44 (A-172, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.748× | -3.1 | 0.14 | 23/44 (A-172, H4, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.821× | -3.1 | 0.14 | 22/44 (AsPC-1, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 0.729× | -3.1 | 0.14 | 20/44 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.769× | -3.0 | 0.17 | 22/43 (AsPC-1, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 276 | 0 | 8 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.342× (z -11.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.443× (z -10.1) |
| [[PANC-1 (line)]] | alt | 125 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +31.5) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[A498 (line)]] | wt | 144 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +24.5) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 26.4 | 5 (4 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.87× (z +10.8) | — |
| [[J82 (line)]] | alt | 38.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +15.0) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +10.0) | — |
| [[SW480 (line)]] | alt | 64.3 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +13.5) | — |
| [[A-172 (line)]] | wt | 123 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.366× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.372× (z -9.6) |
| [[A-427 (line)]] | wt | 42.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +10.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 89.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 125 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.276× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 50.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +12.1) | — |
| [[H4 (line)]] | wt | 247 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.254× (z -13.1) ⚠ cell-cycle shift, explains ~23% of this change |
| [[HEC-1-A (line)]] | alt | 62.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.4) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 100.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.0) ⚠ cell-cycle shift, explains ~59% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.386× (z -8.5) ⚠ cell-cycle shift, explains ~23% of this change |
| [[LOX-IMVI (line)]] | wt | 80.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.80× (z +10.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 105 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +14.5) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[NCI-H2347 (line)]] | alt | 78.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +15.9) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[Panc 03.27 (line)]] | alt | 76.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +16.5) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 69.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +11.6) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[SW 900 (line)]] | alt | 82.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +13.3) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[SW1417 (line)]] | alt | 54.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +14.4) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.80× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 25.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +9.9) | — |
| [[C32 (line)]] | wt | 71.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +13.0) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[CFPAC-1 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.1) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[COLO 205 (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +8.6) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[HCT15 (line)]] | alt | 83.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HepG2_C3A (line)]] | wt | 35.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +10.3) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[HOP62 (line)]] | alt | 92.9 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.387× (z -8.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[LoVo (line)]] | wt | 28.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.06× (z +10.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.220× (z -10.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 69.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 39.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +12.7) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[SW 1271 (line)]] | alt | 155 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +9.2) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 85.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 280 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 106 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.86 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 91.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF10D]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[SNAI1]] | +0.66 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[RIN1]] | +0.65 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[KATNA1]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[EHD1]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[CNNM4]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[WDR47]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[PDGFB]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[RAC2]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[LGALS1]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRSL1]] | -0.61 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[LARP4]] | -0.58 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[MGST1]] | -0.57 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[TRAPPC8]] | -0.56 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[PEX26]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[GFM1]] | -0.55 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ACTR3C]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[MRRF]] | -0.55 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[HECTD1]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[MKRN5P]] | -0.54 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[DPY19L1P2]] | -0.54 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[RNASEH2B]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS1]] | B | LGALS1 activity raises FSCN1's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 3.78× lower at baseline in the lines without LGALS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[PORCN]] | B | PORCN activity raises FSCN1's level | lines that do not express PORCN (5) vs lines expressing it (45) | 2.59× lower at baseline in the lines without PORCN | 0.029 | ⚠ within organs, on part of the lines; also absent: IQSEC2, APOBEC3F, CELSR1; maybe low, not absent |
| [[ITGA5]] | B | ITGA5 activity raises FSCN1's level | lines that do not express ITGA5 (11) vs lines expressing it (39) | 2.39× lower at baseline in the lines without ITGA5 | 0.034 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1 |
| [[CAVIN1]] | B | CAVIN1 activity raises FSCN1's level | lines that do not express CAVIN1 (6) vs lines expressing it (44) | 3.24× lower at baseline in the lines without CAVIN1 | 0.035 | ⚠ within organs, on part of the lines; also absent: NUAK1, SLC25A43, BLVRA |
| [[HSPA2]] | B | HSPA2 activity raises FSCN1's level | lines that do not express HSPA2 (12) vs lines expressing it (38) | 3.37× lower at baseline in the lines without HSPA2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SGCE, MICU3, TUSC3; maybe low, not absent; its own permutation p |
| [[FGFR1]] | B | FGFR1 activity raises FSCN1's level | lines that do not express FGFR1 (8) vs lines expressing it (42) | 2.55× lower at baseline in the lines without FGFR1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SIX4, CPLANE1, QKI |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNN4]] | C | FSCN1 activity raises KCNN4's level | lines that do not express FSCN1 (4) vs lines expressing it (46) | 3.23× lower at baseline in the lines without FSCN1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, ELK3, WWTR1; its own permutation p |
| [[C8orf58]] | C | FSCN1 activity raises C8orf58's level | lines that do not express FSCN1 (4) vs lines expressing it (46) | 1.58× lower at baseline in the lines without FSCN1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, ELK3, WWTR1; its own permutation p |
| [[TNFRSF10D]] | C | FSCN1 activity raises TNFRSF10D's level | lines that do not express FSCN1 (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without FSCN1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, ELK3, WWTR1; its own permutation p |
| [[RUFY3]] | C | FSCN1 activity lowers RUFY3's level | lines that do not express FSCN1 (4) vs lines expressing it (46) | 1.09× higher at baseline in the lines without FSCN1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, ELK3, WWTR1; its own permutation p |
| [[ICAM3]] | C | FSCN1 activity raises ICAM3's level | lines that do not express FSCN1 (4) vs lines expressing it (46) | 1.84× lower at baseline in the lines without FSCN1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, ELK3, WWTR1; its own permutation p |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.571). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.7, -1.7); signed map (-3.0, 28.4). **Vector** length 134, 44.3% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +4.8 | +7.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.7 | +2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.7 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +2.8 | +2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.7 | +1.7 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.6 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | -5.5 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.1 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.1 | -3.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.8 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.7 | -3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.2 | -2.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -4.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | fascin actin-bundling protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:5,592,816-5,606,655 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p55, FLJ38511; previously SNL |
| Gene groups (HGNC) | Fascin family |
| Hallmark sets | APICAL_JUNCTION, MITOTIC_SPINDLE |
| Reactome | 3 pathways, smallest: Interleukin-4 and Interleukin-13 signaling; Signaling by Interleukins; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16658](https://www.uniprot.org/uniprotkb/Q16658) (Fascin):

> Actin-binding protein that contains 2 major actin binding sites. Organizes filamentous actin into parallel bundles. Plays a role in the organization of actin filament bundles and the formation of microspikes, membrane ruffles, and stress fibers. Important for the formation of a diverse set of cell protrusions, such as filopodia, and for cell motility and migration. Mediates reorganization of the actin cytoskeleton and axon growth cone collapse in response to NGF.

**Summary**, from NCBI Gene [6624](https://www.ncbi.nlm.nih.gov/gene/6624):

> This gene encodes a member of the fascin family of actin-binding proteins. Fascin proteins organize F-actin into parallel bundles, and are required for the formation of actin-based cellular protrusions. The encoded protein plays a critical role in cell migration, motility, adhesion and cellular interactions. Expression of this gene is known to be regulated by several microRNAs, and overexpression of this gene may play a role in the metastasis of multiple types of cancer by increasing cell …

**Accessions** — [HGNC:11148](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11148) · Entrez [6624](https://www.ncbi.nlm.nih.gov/gene/6624) · UniProt [Q16658](https://www.uniprot.org/uniprotkb/Q16658) · Ensembl [ENSG00000075618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075618)

## Data

Gene col 1125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1125); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1125]; `tensor/DDL_lfc|DDL_z.npy` [1125]; `embed/gene_vectors.npy` [1125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1125 or target_col == 1125). Every well: [[FSCN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FSCN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
