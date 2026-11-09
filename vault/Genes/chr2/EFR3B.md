---
symbol: "EFR3B"
type: "gene"
col: 1408
ensembl_id: "ENSG00000084710"
name: "EFR3 homolog B"
location: "2p23.3"
module: 87
arm: "+"
pooled_cpm: 17.21
n_lines_expressing: 40
n_dd_up: 31
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# EFR3B

*EFR3 homolog B* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 11.7× (z +40.5, q 0e+00, up in 36 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.911× (z -5.6, q 1e-05, down in 7 of 38 measured lines) ⚠ position not correctable. The strongest without an alert is [[Pentagastrin (drug)]] 5 µM: 0.846× (z -4.0, q 0.021, down in 1 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 0.182×, SK-MEL-2 0.170×, AN3 CA 0.177×); [[Harringtonine (drug)]] 5 µM in 2 lines (C32 0.109×, AN3 CA 0.112×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (C32 0.127×, SK-MEL-2 0.106×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STAG3]] (+0.66, fdr 7e-06), [[MIR3681HG]] (+0.65, fdr 7e-06), [[STK32B]] (+0.63, fdr 1e-05).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LOXL3]] → it (grade B ⚠); 4 go from it, the strongest it → [[JAM3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1408.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **11.7×** | +40.5 | 0e+00 | 36/37 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **9.00×** | +36.2 | 0e+00 | 35/37 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **7.31×** | +32.7 | 0e+00 | 35/37 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +22.4 | 0e+00 | 27/36 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.21×** | +18.4 | 0e+00 | 29/38 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.79×** | +16.9 | 0e+00 | 32/37 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +15.0 | 0e+00 | 16/36 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **2.39×** | +14.3 | 2e-44 | 30/37 (SW480, NCI-H2347, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **3.94×** | +11.8 | 3e-30 | 24/33 (SW480, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **3.44×** | +10.6 | 1e-24 | 26/37 (SW480, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.83×** | +9.5 | 1e-19 | 18/33 (A498, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.77×** | +9.4 | 3e-19 | 18/29 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.76×** | +9.0 | 1e-17 | 11/22 (SW480, J82, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +8.0 | 6e-14 | 16/36 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.58×** | +7.2 | 3e-11 | 13/31 (A498, SW 900, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +4.4 | 3e-04 | 6/36 (SW1417, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 6e-04 | 9/35 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.002 | 11/36 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.26×** | +3.8 | 0.004 | 7/37 (A549, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1408.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 0.182×, SK-MEL-2 0.170×, AN3 CA 0.177×); [[Harringtonine (drug)]] 5 µM in 2 lines (C32 0.109×, AN3 CA 0.112×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (C32 0.127×, SK-MEL-2 0.106×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.911× | -5.6 | 1e-05 | 7/38 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.846× | -4.0 | 0.021 | 1/38 (A549) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.801×** | -3.7 | 0.035 | 12/35 (A-172, Hs 766T, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.857× | -3.7 | 0.035 | 6/38 (PANC-1, LoVo, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.817×** | -3.4 | 0.071 | 5/37 (C32, A-172, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.810×** | -3.4 | 0.071 | 6/38 (C32, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | 0.695× | -3.2 | 0.13 | 6/35 (NCI-H460, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 279 | 0 | 27 (13 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0540× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.182× (z -20.5) |
| [[SW480 (line)]] | alt | 15.6 | 11 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 12.3× (z +21.2) | — |
| [[LS 180 (line)]] | wt | 5.04 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 20.4× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 16.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 11.7× (z +15.1) | — |
| [[A-427 (line)]] | wt | 18.0 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 10.3× (z +14.6) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.348× (z -9.5) |
| [[A498 (line)]] | wt | 4.92 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 26.8× (z +15.4) | — |
| [[A549 (line)]] | wt | 11.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 14.4× (z +13.9) | — |
| [[LoVo (line)]] | wt | 5.47 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 21.4× (z +14.1) | — |
| [[LOX-IMVI (line)]] | wt | 9.05 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 14.8× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 20.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.95× (z +13.5) | [[Harringtonine (drug)]] 0.5 µM 0.284× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 24.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.70× (z +11.4) | [[Selinexor (drug)]] 5 µM 0.382× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 64.2 | 0 | 3 | — | [[Verteporfin (drug)]] 5 µM 0.0556× (z -13.9) |
| [[HOP62 (line)]] | alt | 5.21 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 17.5× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 9.83 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.89× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 8.88 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.4× (z +12.8) | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.8× (z +12.3) | — |
| [[SHP-77 (line)]] | alt | 34.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 42.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -15.6) |
| [[Hs 766T (line)]] | wt | 14.6 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 9.22× (z +9.9) | [[GSK1059615 (drug)]] 0.5 µM 0.0650× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 5.72 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 24.8× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 4.95 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 11.3× (z +11.1) | — |
| [[SW 900 (line)]] | alt | 11.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 10.5× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 51.2 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.224× (z -10.8) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 7.04 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 25.3× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 5.05 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 12.6× (z +9.3) | — |
| [[J82 (line)]] | alt | 5.47 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.03× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAG3]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 | same gene group |
| [[MIR3681HG]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[STK32B]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[COL19A1]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[A2M]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[C10orf90]] | +0.61 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MAN1C1]] | +0.61 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[GAS7]] | +0.61 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[ZCCHC24]] | +0.60 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[GLDC]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SOX10]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CPNE5]] | +0.57 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOXL3]] | B | LOXL3 activity raises EFR3B's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.38× lower at baseline in the lines without LOXL3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent |
| [[ELOVL2]] | B | ELOVL2 activity raises EFR3B's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 2.08× lower at baseline in the lines without ELOVL2 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046 |
| [[MMP14]] | B | MMP14 activity lowers EFR3B's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 1.80× higher at baseline in the lines without MMP14 | 0.052 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[PTPRZ1]] | B | PTPRZ1 activity raises EFR3B's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.57× lower at baseline in the lines without PTPRZ1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[NLGN4X]] | B | NLGN4X activity raises EFR3B's level | lines that do not express NLGN4X (37) vs lines expressing it (13) | 2.36× lower at baseline in the lines without NLGN4X | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| [[EIF1AY]] | B | EIF1AY activity raises EFR3B's level | lines that do not express EIF1AY (31) vs lines expressing it (19) | 1.72× lower at baseline in the lines without EIF1AY | 0.084 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAM3]] | B | EFR3B activity raises JAM3's level | lines that do not express EFR3B (10) vs lines expressing it (40) | 4.86× lower at baseline in the lines without EFR3B | 0.050 | ⚠ within organs, on part of the lines; also absent: RTN4RL1, SEPTIN5, NT5M; maybe low, not absent |
| [[NPTXR]] | B | EFR3B activity raises NPTXR's level | lines that do not express EFR3B (10) vs lines expressing it (40) | 2.43× lower at baseline in the lines without EFR3B | 0.062 | ⚠ within organs, on part of the lines; also absent: RTN4RL1, SEPTIN5, NT5M; maybe low, not absent |
| [[MAN1C1]] | B | EFR3B activity raises MAN1C1's level | lines that do not express EFR3B (10) vs lines expressing it (40) | 2.22× lower at baseline in the lines without EFR3B | 0.074 | ⚠ within organs, on part of the lines; also absent: RTN4RL1, SEPTIN5, NT5M; maybe low, not absent |
| [[KDM2B-DT]] | B | EFR3B activity raises KDM2B-DT's level | lines that do not express EFR3B (10) vs lines expressing it (40) | 2.14× lower at baseline in the lines without EFR3B | 0.089 | ⚠ within organs, on part of the lines; also absent: RTN4RL1, SEPTIN5, NT5M; maybe low, not absent |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.2, 28.1); signed map (28.8, 39.4). **Vector** length 85.4, 17.5% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +18.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | +6.7 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | +6.3 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | +5.4 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +8.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.9 | +11.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +14.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -2.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -5.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.3 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | EFR3 homolog B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:25,042,076-25,159,135 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37871; previously KIAA0953 |
| Gene groups (HGNC) | Armadillo like helical domain containing; EFR3 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2G0](https://www.uniprot.org/uniprotkb/Q9Y2G0) (Protein EFR3 homolog B):

> Component of a complex required to localize phosphatidylinositol 4-kinase (PI4K) to the plasma membrane. The complex acts as a regulator of phosphatidylinositol 4-phosphate (PtdIns(4)P) synthesis (Probable). In the complex, EFR3B probably acts as the membrane-anchoring component. Also involved in responsiveness to G protein-coupled receptors; it is however unclear whether this role is direct or indirect.

**Summary**, from NCBI Gene [22979](https://www.ncbi.nlm.nih.gov/gene/22979):

> Involved in phosphatidylinositol phosphate biosynthetic process and protein localization to plasma membrane. Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29155](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29155) · Entrez [22979](https://www.ncbi.nlm.nih.gov/gene/22979) · UniProt [Q9Y2G0](https://www.uniprot.org/uniprotkb/Q9Y2G0) · Ensembl [ENSG00000084710](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084710)

## Data

Gene col 1408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1408); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1408]; `tensor/DDL_lfc|DDL_z.npy` [1408]; `embed/gene_vectors.npy` [1408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1408 or target_col == 1408). Every well: [[EFR3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFR3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
