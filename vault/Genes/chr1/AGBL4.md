---
symbol: "AGBL4"
type: "gene"
col: 11776
ensembl_id: "ENSG00000186094"
name: "AGBL carboxypeptidase 4"
location: "1p33"
module: 150
arm: "+"
pooled_cpm: 12.98
n_lines_expressing: 39
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 3
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# AGBL4

*AGBL carboxypeptidase 4* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.01× (z +23.3, q 0e+00, up in 24 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 0.198×, SHP-77 0.427×); [[TAK-901 (drug)]] 5 µM in 2 lines (NCI-H23 0.0142×, SHP-77 0.0866×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.128×, SK-MEL-2 0.186×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H23 0.156×, H4 0.0597×); [[Malotilate (drug)]] 0.05 µM in 1 line (H4 0.0422×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRID2]] (+0.73, fdr 7e-06), [[LINC01122]] (+0.72, fdr 7e-06), [[SPAG17]] (+0.71, fdr 7e-06).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NELL2]] → it (grade B ⚠); 3 go from it, the strongest it → [[NREP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11776.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.01×** | +23.3 | 0e+00 | 24/31 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.62×** | +15.3 | 0e+00 | 16/22 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.56×** | +14.5 | 3e-45 | 7/12 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.86×** | +11.5 | 1e-28 | 9/16 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.61×** | +11.4 | 5e-28 | 21/33 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +9.3 | 2e-18 | 17/31 (HOP62, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +7.6 | 2e-12 | 18/34 (HT-29, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.74×** | +6.6 | 3e-09 | 21/36 (NCI-H460, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.6 | 1e-06 | 12/35 (HOP62, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.5 | 2e-06 | 9/31 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +5.4 | 3e-06 | 3/22 (SW1417, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.57×** | +5.4 | 4e-06 | 15/33 (BT-474, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +5.3 | 5e-06 | 13/33 (HT-29, C32, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.55×** | +5.0 | 2e-05 | 7/29 (HOP62, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +4.9 | 3e-05 | 18/35 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.3 | 5e-04 | 16/33 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 0.001 | 7/34 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.004 | 10/33 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.7 | 0.006 | 10/33 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.019 | 7/33 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +3.0 | 0.062 | 13/34 (LoVo, SHP-77, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.068 | 11/34 (NCI-H23, SK-MEL-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11776.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 0.198×, SHP-77 0.427×); [[TAK-901 (drug)]] 5 µM in 2 lines (NCI-H23 0.0142×, SHP-77 0.0866×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.128×, SK-MEL-2 0.186×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H23 0.156×, H4 0.0597×); [[Malotilate (drug)]] 0.05 µM in 1 line (H4 0.0422×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.730× | -3.7 | 0.12 | 11/34 (NCI-H23, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.760× | -3.2 | 0.23 | 8/35 (hTERT-HPNE, HS-578T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.826× | -3.2 | 0.23 | 13/34 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.757× | -3.2 | 0.23 | 6/33 (NCI-H23, LoVo, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.831× | -3.1 | 0.23 | 7/35 (hTERT-HPNE, SW1417, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.775× | -3.0 | 0.25 | 4/34 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11776. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 114 | 0 | 10 (8 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0220× (z -23.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -14.4) |
| [[HOP62 (line)]] | alt | 3.54 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.98× (z +12.0) | — |
| [[LoVo (line)]] | wt | 6.72 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.15× (z +13.0) | — |
| [[SHP-77 (line)]] | alt | 229 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0866× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.5) |
| [[H4 (line)]] | wt | 13.5 | 0 | 2 | — | [[Malotilate (drug)]] 0.05 µM 0.0422× (z -10.8) |
| [[HT-29 (line)]] | alt | 4.00 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 9.58× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 3.75 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.09× (z +12.7) | — |
| [[SK-MEL-2 (line)]] | alt | 69.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0745× (z -14.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 5.69 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +11.2) | — |
| [[C-33 A (line)]] | alt | 3.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +9.1) | — |
| [[C32 (line)]] | wt | 3.44 | 0 | 1 | — | [[Asciminib (drug)]] 0.5 µM 0.0412× (z -8.8) |
| [[KATO III (line)]] | alt | 3.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.55× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 8.21 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0743× (z -9.8) |
| [[RKO (line)]] | wt | 4.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.74× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 4.60 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0737× (z -8.6) |
| [[A-172 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11776), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRID2]] | +0.73 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[LINC01122]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[SPAG17]] | +0.71 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[STPG2]] | +0.68 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[LINC01414]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[LINC01524]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[GALNT17]] | +0.64 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[CTNNA3]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[FAT3]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[MIR2052HG]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[OR3A2]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[LINC02208]] | +0.62 | +0.62 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NELL2]] | B | NELL2 activity raises AGBL4's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 2.21× lower at baseline in the lines without NELL2 | 0.040 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers AGBL4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RERG]] | B | RERG activity raises AGBL4's level | lines that do not express RERG (24) vs lines expressing it (26) | 2.23× lower at baseline in the lines without RERG | 0.057 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MGAT4C, ENSG00000266450; maybe low, not absent |
| [[MGAT4C]] | B | MGAT4C activity raises AGBL4's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 2.95× lower at baseline in the lines without MGAT4C | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385 |
| [[STXBP5L]] | B | STXBP5L activity raises AGBL4's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 2.28× lower at baseline in the lines without STXBP5L | 0.060 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent |
| [[BRINP3]] | B | BRINP3 activity raises AGBL4's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 2.32× lower at baseline in the lines without BRINP3 | 0.064 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent |
| [[KLRC4-KLRK1]] | B | KLRC4-KLRK1 activity raises AGBL4's level | lines that do not express KLRC4-KLRK1 (29) vs lines expressing it (21) | 2.24× lower at baseline in the lines without KLRC4-KLRK1 | 0.069 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KLRC3, KLRC2, PIP5K1B |
| [[LINC00648]] | B | LINC00648 activity raises AGBL4's level | lines that do not express LINC00648 (35) vs lines expressing it (15) | 2.99× lower at baseline in the lines without LINC00648 | 0.091 | ⚠ within organs, on part of the lines; also absent: LINC00470, ANKRD20A8P, ZIC1 |
| [[MIR646HG]] | B | MIR646HG activity raises AGBL4's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 2.40× lower at baseline in the lines without MIR646HG | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NREP]] | B | AGBL4 activity raises NREP's level | lines that do not express AGBL4 (11) vs lines expressing it (39) | 2.87× lower at baseline in the lines without AGBL4 | 0.009 | ⚠ within organs, on part of the lines; also absent: RBFOX1, ENSG00000248347; maybe low, not absent |
| [[LINC01117]] | B | AGBL4 activity raises LINC01117's level | lines that do not express AGBL4 (11) vs lines expressing it (39) | 1.90× lower at baseline in the lines without AGBL4 | 0.044 | ⚠ within organs, on part of the lines; also absent: RBFOX1, ENSG00000248347; maybe low, not absent |
| [[AKAP6]] | B | AGBL4 activity raises AKAP6's level | lines that do not express AGBL4 (11) vs lines expressing it (39) | 2.23× lower at baseline in the lines without AGBL4 | 0.090 | ⚠ within organs, on part of the lines; also absent: RBFOX1, ENSG00000248347; maybe low, not absent |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.8, 28.2); signed map (38.0, 16.5). **Vector** length 62.2, 11.2% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.3 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +23.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +5.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +2.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | AGBL carboxypeptidase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p33 — chr1:48,532,854-50,023,954 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14442, CCP6 |
| Gene groups (HGNC) | M14 carboxypeptidases |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VU57](https://www.uniprot.org/uniprotkb/Q5VU57) (Cytosolic carboxypeptidase 6):

> Metallocarboxypeptidase that mediates protein deglutamylation of tubulin and non-tubulin target proteins. Catalyzes the removal of polyglutamate side chains present on the gamma-carboxyl group of glutamate residues within the C-terminal tail of tubulin protein. Specifically cleaves tubulin long-side-chains, while it is not able to remove the branching point glutamate. Also catalyzes the removal of polyglutamate residues from the carboxy-terminus of non-tubulin proteins such as MYLK. Mediates …

**Summary**, from NCBI Gene [84871](https://www.ncbi.nlm.nih.gov/gene/84871):

> Predicted to enable metallocarboxypeptidase activity and tubulin binding activity. Predicted to be involved in C-terminal protein deglutamylation; defense response to virus; and protein side chain deglutamylation. Predicted to act upstream of or within several processes, including axonal transport of mitochondrion; positive regulation of ubiquitin-dependent protein catabolic process; and regulation of blastocyst development. Located in Golgi apparatus; centriole; and ciliary basal body. …

**Accessions** — [HGNC:25892](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25892) · Entrez [84871](https://www.ncbi.nlm.nih.gov/gene/84871) · UniProt [Q5VU57](https://www.uniprot.org/uniprotkb/Q5VU57) · Ensembl [ENSG00000186094](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186094)

## Data

Gene col 11776: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11776); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11776, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11776]; `tensor/DDL_lfc|DDL_z.npy` [11776]; `embed/gene_vectors.npy` [11776]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11776 or target_col == 11776). Every well: [[AGBL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGBL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
