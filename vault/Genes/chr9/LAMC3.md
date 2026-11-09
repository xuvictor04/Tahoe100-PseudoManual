---
symbol: "LAMC3"
type: "gene"
col: 568
ensembl_id: "ENSG00000050555"
name: "laminin subunit gamma 3"
location: "9q34.12"
module: 128
arm: "+"
pooled_cpm: 5.08
n_lines_expressing: 25
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 34
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# LAMC3

*laminin subunit gamma 3* — 9q34.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.02× (z +14.4, q 3e-44, up in 4 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.99× (z +10.4, q 3e-23, up in 3 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (PANC-1 0.128×, A-427 0.167×, SW480 0.146×, NCI-H460 0.400×); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (A-427 0.111×, PANC-1 0.212×, NCI-H460 0.224×, SW480 0.149×; ⚠ cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.0964×; ⚠ toxic; cell-cycle shift, explains ~19% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 0.186×); [[Erlotinib (drug)]] 5 µM in 1 line (NCI-H2030 0.0764×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRZ1]] (+0.61, fdr 3e-05), [[EMID1]] (+0.61, fdr 1e-05), [[SLC4A3]] (+0.60, fdr 1e-05); moves opposite to [[MORN2]] (-0.47, fdr 1e-04), [[ANKRD54]] (-0.45, fdr 7e-05), [[CDKL5]] (-0.44, fdr 1e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[WNK2]] → it (grade B ⚠); 34 go from it, the strongest it → [[DDX54]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 568.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.02×** | +14.4 | 3e-44 | 4/8 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.95×** | +11.6 | 7e-29 | 7/11 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +10.4 | 3e-23 | 3/17 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.63×** | +10.4 | 3e-23 | 9/23 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +10.3 | 5e-23 | 11/22 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +9.4 | 4e-19 | 8/11 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.97×** | +7.3 | 3e-11 | 7/22 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.84×** | +6.6 | 4e-09 | 7/20 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.61×** | +4.9 | 6e-05 | 6/15 (A-427, A549, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.57×** | +4.8 | 7e-05 | 9/21 (NCI-H460, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.8 | 8e-05 | 4/19 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +4.4 | 6e-04 | 2/18 (NCI-H1792, SW48) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.42×** | +3.7 | 0.008 | 8/22 (A549, SW48, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +3.6 | 0.014 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.34×** | +3.2 | 0.059 | 5/23 (H4, A498, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.061 | 5/22 (SHP-77, NCI-H23, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.061 | 2/22 (A549, A498) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.061 | 3/16 (NCI-H460, NCI-H23, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.061 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +2.9 | 0.079 | 7/19 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 568.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (PANC-1 0.128×, A-427 0.167×, SW480 0.146×, NCI-H460 0.400×); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (A-427 0.111×, PANC-1 0.212×, NCI-H460 0.224×, SW480 0.149×; ⚠ cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.0964×; ⚠ toxic; cell-cycle shift, explains ~19% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 0.186×); [[Erlotinib (drug)]] 5 µM in 1 line (NCI-H2030 0.0764×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | 0.699× | -3.7 | 0.11 | 14/19 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 568. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.60 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -13.3) |
| [[A-427 (line)]] | wt | 35.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -19.2) |
| [[NCI-H460 (line)]] | wt | 14.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.61× (z +9.1) ⚠ cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -10.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.2) |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -21.6) |
| [[NCI-H2030 (line)]] | alt | 6.78 | 0 | 2 | — | [[Erlotinib (drug)]] 5 µM 0.0764× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 24.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0964× (z -15.1) ⚠ toxic; cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -8.8) |
| [[A-172 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.916 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.748 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 568), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRZ1]] | +0.61 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[EMID1]] | +0.61 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SLC4A3]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[DGCR5]] | +0.59 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[ADGRB1]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[RNF212]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[COLGALT2]] | +0.55 | +0.53 / +0.39 | both halves | 5e-05 | pathway: Extracellular matrix organization |
| [[ZP3]] | +0.54 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[JPH3]] | +0.53 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[WT1-AS]] | +0.53 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[VASH1]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[C16orf95]] | +0.53 | +0.53 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MORN2]] | -0.47 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[ANKRD54]] | -0.45 | -0.40 / -0.37 | both halves | 7e-05 |  |
| [[CDKL5]] | -0.44 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[H2AJ]] | -0.43 | -0.33 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 6, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNK2]] | B | WNK2 activity raises LAMC3's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.98× lower at baseline in the lines without WNK2 | 0.027 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[NUP210]] | B | NUP210 activity raises LAMC3's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 2.09× lower at baseline in the lines without NUP210 | 0.053 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |
| [[PARD6G]] | B | PARD6G activity raises LAMC3's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.34× lower at baseline in the lines without PARD6G | 0.059 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[GNAZ]] | B | GNAZ activity raises LAMC3's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.05× lower at baseline in the lines without GNAZ | 0.069 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[TERT]] | B | TERT activity raises LAMC3's level | lines that do not express TERT (13) vs lines expressing it (37) | 2.00× lower at baseline in the lines without TERT | 0.093 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[MVB12B]] | B | MVB12B activity raises LAMC3's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.28× lower at baseline in the lines without MVB12B | 0.095 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[KIF26A]] | C | KIF26A activity raises LAMC3's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.62× lower at baseline in the lines without KIF26A | 0.011 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN; co-absent with the target |
| [[BRSK2]] | C | BRSK2 activity raises LAMC3's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 2.49× lower at baseline in the lines without BRSK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent; co-absent with the target |
| [[MYT1]] | C | MYT1 activity raises LAMC3's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.38× lower at baseline in the lines without MYT1 | 0.035 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2; co-absent with the target |
| [[JAKMIP1]] | C | JAKMIP1 activity raises LAMC3's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 2.70× lower at baseline in the lines without JAKMIP1 | 0.048 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |
| [[KLHL14]] | C | KLHL14 activity raises LAMC3's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 2.13× lower at baseline in the lines without KLHL14 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55; co-absent with the target |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 29, C 5. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX54]] | B | LAMC3 activity raises DDX54's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.29× lower at baseline in the lines without LAMC3 | 0.003 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[KAT2A]] | B | LAMC3 activity raises KAT2A's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.52× lower at baseline in the lines without LAMC3 | 0.007 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[GNAZ]] | B | LAMC3 activity raises GNAZ's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.85× lower at baseline in the lines without LAMC3 | 0.010 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[LHX6]] | B | LAMC3 activity raises LHX6's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without LAMC3 | 0.010 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[WNK2]] | B | LAMC3 activity raises WNK2's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.73× lower at baseline in the lines without LAMC3 | 0.011 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[SEPTIN5]] | B | LAMC3 activity raises SEPTIN5's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 2.69× lower at baseline in the lines without LAMC3 | 0.015 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[ZP3]] | B | LAMC3 activity raises ZP3's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.79× lower at baseline in the lines without LAMC3 | 0.019 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[TCOF1]] | B | LAMC3 activity raises TCOF1's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.44× lower at baseline in the lines without LAMC3 | 0.022 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[PARD6G]] | B | LAMC3 activity raises PARD6G's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 2.14× lower at baseline in the lines without LAMC3 | 0.030 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[CHST10]] | B | LAMC3 activity raises CHST10's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.99× lower at baseline in the lines without LAMC3 | 0.036 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[TANGO6]] | B | LAMC3 activity raises TANGO6's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.61× lower at baseline in the lines without LAMC3 | 0.036 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[TMCC1-DT]] | B | LAMC3 activity raises TMCC1-DT's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.73× lower at baseline in the lines without LAMC3 | 0.042 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.2, 39.7); signed map (24.3, 26.5). **Vector** length 47.5, 10.4% of its response variance represented; |z| ≥ 3 in 498 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +3.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | laminin subunit gamma 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.12 — chr9:131,009,174-131,094,473 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434E202 |
| Gene groups (HGNC) | Laminin subunits |
| Reactome | 17 pathways, smallest: Attachment of bacteria to epithelial cells; Biofilm formation; Developmental Lineage of Pancreatic Ductal Cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6N6](https://www.uniprot.org/uniprotkb/Q9Y6N6) (Laminin subunit gamma-3):

> Binding to cells via a high affinity receptor, laminin is thought to mediate the attachment, migration and organization of cells into tissues during embryonic development by interacting with other extracellular matrix components.

**Summary**, from NCBI Gene [10319](https://www.ncbi.nlm.nih.gov/gene/10319):

> Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectively) and they form a cruciform structure consisting of 3 short arms, each formed by a different …

**Accessions** — [HGNC:6494](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6494) · Entrez [10319](https://www.ncbi.nlm.nih.gov/gene/10319) · UniProt [Q9Y6N6](https://www.uniprot.org/uniprotkb/Q9Y6N6) · Ensembl [ENSG00000050555](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000050555)

## Data

Gene col 568: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 568); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 568, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 568]; `tensor/DDL_lfc|DDL_z.npy` [568]; `embed/gene_vectors.npy` [568]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 568 or target_col == 568). Every well: [[LAMC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
