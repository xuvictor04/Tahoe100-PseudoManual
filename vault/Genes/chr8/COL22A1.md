---
symbol: "COL22A1"
type: "gene"
col: 9808
ensembl_id: "ENSG00000169436"
name: "collagen type XXII alpha 1 chain"
location: "8q24.23-q24.3"
module: 228
arm: "+"
pooled_cpm: 12.48
n_lines_expressing: 19
n_dd_up: 14
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 19
direction_downstream: 14
tags: ["gene", "module/228"]
generated_by: "tahoemap"
---

# COL22A1

*collagen type XXII alpha 1 chain* — 8q24.23-q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.53× (z +13.2, q 3e-37, up in 11 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Dexamethasone (drug)]] 5 µM: 0.659× (z -4.2, q 0.007, down in 8 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCKAP5]] (+0.65, fdr 7e-06), [[PAEP]] (+0.63, fdr 1e-05), [[INHBA]] (+0.63, fdr 1e-05); moves opposite to [[PHKA1]] (-0.48, fdr 3e-05).
> It is in [[Module 228]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[COL16A1]] → it (grade B ⚠); 14 go from it, the strongest it → [[DNAH17]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9808.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.53×** | +13.2 | 3e-37 | 11/16 (SW 900, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.66×** | +9.1 | 2e-17 | 0/12 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +8.9 | 9e-17 | 3/14 (HOP62, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +8.8 | 3e-16 | 1/15 (A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +8.2 | 3e-14 | 0/10 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +7.4 | 9e-12 | 13/17 (NCI-H1573, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.90×** | +6.2 | 4e-08 | 14/16 (SW 900, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.82×** | +4.3 | 0.001 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.44×** | +3.7 | 0.015 | 5/16 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.5 | 0.022 | 1/15 (SW1417) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.022 | 6/17 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.030 | 6/16 (SW 900, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.57×** | +3.3 | 0.050 | 0/17 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.078 | 1/17 (Hs 766T) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9808.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 5 µM |  | **0.659×** | -4.2 | 0.007 | 8/17 (SHP-77, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.661×** | -4.2 | 0.007 | 11/16 (SHP-77, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.643×** | -4.1 | 0.007 | 10/16 (SHP-77, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.669×** | -4.1 | 0.007 | 7/17 (SHP-77, HS-578T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.672×** | -4.0 | 0.007 | 5/17 (SHP-77, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **0.758×** | -4.0 | 0.007 | 9/17 (HS-578T, SHP-77, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.669×** | -3.9 | 0.008 | 8/17 (SHP-77, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.689×** | -3.8 | 0.012 | 11/17 (SHP-77, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.694×** | -3.7 | 0.014 | 9/17 (Panc 03.27, SHP-77, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.702×** | -3.6 | 0.020 | 9/17 (SHP-77, CFPAC-1, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.714×** | -3.4 | 0.034 | 5/17 (SHP-77, HS-578T, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.789×** | -3.4 | 0.034 | 11/17 (A498, Hs 766T, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.718×** | -3.3 | 0.036 | 12/16 (CFPAC-1, SHP-77, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.709×** | -3.2 | 0.054 | 5/17 (SHP-77, HS-578T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.739×** | -3.0 | 0.087 | 7/16 (Panc 03.27, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 49.4 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -17.8) |
| [[Panc 03.27 (line)]] | alt | 29.6 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -12.2) |
| [[SHP-77 (line)]] | alt | 271 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -16.1) |
| [[NCI-H1573 (line)]] | alt | 17.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -9.6) |
| [[HOP62 (line)]] | alt | 5.88 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.488× (z -8.9) ⚠ position not correctable |
| [[HS-578T (line)]] | alt | 34.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 23.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0575× (z -11.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 8.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +11.1) | — |
| [[A-172 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.52 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCKAP5]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PAEP]] | +0.63 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[INHBA]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[OFCC1]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[DNAH17]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[FRMPD4]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[IL1B]] | +0.57 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[ABCA13]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[NHSL2]] | +0.56 | +0.36 / +0.65 | both halves | 1e-04 |  |
| [[SNTG1]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[MAST4]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[GRIK1]] | +0.55 | +0.61 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHKA1]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 3, C 16. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL16A1]] | B | COL16A1 activity raises COL22A1's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 2.51× lower at baseline in the lines without COL16A1 | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers COL22A1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[ADGRG1]] | B | ADGRG1 activity raises COL22A1's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 2.46× lower at baseline in the lines without ADGRG1 | 0.065 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[PCSK1]] | C | PCSK1 activity raises COL22A1's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 3.42× lower at baseline in the lines without PCSK1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[SLC24A3]] | C | SLC24A3 activity raises COL22A1's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 2.86× lower at baseline in the lines without SLC24A3 | 0.008 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent; co-absent with the target |
| [[SLC14A1]] | C | SLC14A1 activity raises COL22A1's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 3.44× lower at baseline in the lines without SLC14A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |
| [[CCDC152]] | C | CCDC152 activity raises COL22A1's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 2.86× lower at baseline in the lines without CCDC152 | 0.018 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent; co-absent with the target |
| [[PAK3]] | C | PAK3 activity raises COL22A1's level | lines that do not express PAK3 (32) vs lines expressing it (18) | 3.90× lower at baseline in the lines without PAK3 | 0.020 | ⚠ within organs, on part of the lines; also absent: CRLF2, SLC14A1, ENTHD1; co-absent with the target |
| [[ADAM28]] | C | ADAM28 activity raises COL22A1's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 3.35× lower at baseline in the lines without ADAM28 | 0.021 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5; co-absent with the target |
| [[PAEP]] | C | PAEP activity raises COL22A1's level | lines that do not express PAEP (33) vs lines expressing it (17) | 2.76× lower at baseline in the lines without PAEP | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D; co-absent with the target |
| [[LYPD1]] | C | LYPD1 activity raises COL22A1's level | lines that do not express LYPD1 (21) vs lines expressing it (29) | 3.08× lower at baseline in the lines without LYPD1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SETBP1, FRMPD4, NCKAP5; co-absent with the target |
| [[SHISAL1]] | C | SHISAL1 activity raises COL22A1's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 2.99× lower at baseline in the lines without SHISAL1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 4, C 10. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAH17]] | B | COL22A1 activity raises DNAH17's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 1.62× lower at baseline in the lines without COL22A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2 |
| [[ADGRG1]] | B | COL22A1 activity raises ADGRG1's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 1.83× lower at baseline in the lines without COL22A1 | 0.081 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2 |
| [[SLCO3A1]] | B | COL22A1 activity raises SLCO3A1's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 2.78× lower at baseline in the lines without COL22A1 | 0.083 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2 |
| [[ABCA13]] | B | COL22A1 activity raises ABCA13's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without COL22A1 | 0.085 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2 |
| [[PAK3]] | C | COL22A1 activity raises PAK3's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 3.48× lower at baseline in the lines without COL22A1 | 0.029 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |
| [[PLAU]] | C | COL22A1 activity raises PLAU's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 2.97× lower at baseline in the lines without COL22A1 | 0.031 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |
| [[PAEP]] | C | COL22A1 activity raises PAEP's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 2.60× lower at baseline in the lines without COL22A1 | 0.041 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |
| [[PCSK1]] | C | COL22A1 activity raises PCSK1's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 2.39× lower at baseline in the lines without COL22A1 | 0.056 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |
| [[SMOC1]] | C | COL22A1 activity raises SMOC1's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 3.08× lower at baseline in the lines without COL22A1 | 0.059 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |
| [[NCKAP5]] | C | COL22A1 activity raises NCKAP5's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 2.87× lower at baseline in the lines without COL22A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |
| [[EYA2]] | C | COL22A1 activity raises EYA2's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 2.90× lower at baseline in the lines without COL22A1 | 0.063 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |
| [[SLC14A1]] | C | COL22A1 activity raises SLC14A1's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 2.35× lower at baseline in the lines without COL22A1 | 0.070 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |

## Where it sits

- **Module**: [[Module 228]]; 8 genes; every member is in the + arm (projection on the module's main direction 0.750). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.7, 13.9); signed map (35.9, 28.2). **Vector** length 53.5, 14.5% of its response variance represented; |z| ≥ 3 in 493 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +13.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +4.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | +1.7 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -4.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.3 | -3.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XXII alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.23-q24.3 — chr8:138,588,235-138,914,041 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fibril associated collagens with interrupted triple helices |
| Reactome | 4 pathways, smallest: Collagen chain trimerization; Collagen biosynthesis and modifying enzymes; Collagen formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFW1](https://www.uniprot.org/uniprotkb/Q8NFW1) (Collagen alpha-1(XXII) chain):

> Acts as a cell adhesion ligand for skin epithelial cells and fibroblasts.

**Summary**, from NCBI Gene [169044](https://www.ncbi.nlm.nih.gov/gene/169044):

> This gene encodes member of the collagen family which is thought to contribute to the stabilization of myotendinous junctions and strengthen skeletal muscle attachments during contractile activity. It belongs to the fibril-associated collagens with interrupted triple helix (FACIT) subset of the collagen superfamily, which associate with collagen fibers through their C-terminal collagenous domains and mediate protein-protein interactions through their N-terminal noncollagenous domains. The …

**Accessions** — [HGNC:22989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22989) · Entrez [169044](https://www.ncbi.nlm.nih.gov/gene/169044) · UniProt [Q8NFW1](https://www.uniprot.org/uniprotkb/Q8NFW1) · Ensembl [ENSG00000169436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169436)

## Data

Gene col 9808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9808); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9808]; `tensor/DDL_lfc|DDL_z.npy` [9808]; `embed/gene_vectors.npy` [9808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9808 or target_col == 9808). Every well: [[COL22A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL22A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
