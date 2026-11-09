---
symbol: "AGMO"
type: "gene"
col: 11921
ensembl_id: "ENSG00000187546"
name: "alkylglycerol monooxygenase"
location: "7p21.2"
module: 9
arm: "+"
pooled_cpm: 16.96
n_lines_expressing: 20
n_dd_up: 28
n_dd_down: 14
n_dd_up_clean: 24
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 24
direction_downstream: 22
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# AGMO

*alkylglycerol monooxygenase* — 7p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.13× (z +22.8, q 0e+00, up in 8 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 0.598× (z -5.1, q 2e-04, down in 13 of 18 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.462× (z -4.0, q 0.013, down in 11 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DGKB]] (+0.76, fdr 7e-06), [[DACH1]] (+0.65, fdr 9e-06), [[NELL1]] (+0.65, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[CHRM3]] → it (grade B ⚠); 22 go from it, the strongest it → [[MIR325HG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11921.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.13×** | +22.8 | 0e+00 | 8/16 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.35×** | +14.5 | 4e-45 | 2/12 (LOX-IMVI, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.97×** | +13.6 | 1e-39 | 8/17 (SK-MEL-2, LS 180, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +10.9 | 2e-25 | 7/16 (SW1417, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +10.4 | 2e-23 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.98×** | +9.5 | 1e-19 | 9/17 (KATO III, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.51×** | +8.4 | 5e-15 | 2/12 (KATO III, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +5.6 | 1e-06 | 8/17 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +5.1 | 2e-05 | 8/17 (KATO III, SW1417, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +4.6 | 2e-04 | 5/17 (SK-MEL-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.36×** | +4.1 | 0.002 | 5/18 (SHP-77, SK-MEL-2, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.004 | 9/18 (KATO III, SW1417, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.004 | 1/17 (KATO III) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.012 | 8/17 (KATO III, SK-MEL-2, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.012 | 4/17 (A498, SW1417, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.016 | 8/17 (A549, SW480, …) | top dose only |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.46×** | +3.5 | 0.018 | 3/17 (A549, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.019 | 7/17 (KATO III, SHP-77, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11921.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.598×** | -5.1 | 2e-04 | 13/18 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.663×** | -4.0 | 0.013 | 9/17 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.462×** | -4.0 | 0.013 | 11/17 (KATO III, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.757×** | -3.9 | 0.014 | 11/17 (HT-29, A498, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.667×** | -3.8 | 0.014 | 7/17 (SHP-77, Hs 766T, …) | top dose only |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.682×** | -3.8 | 0.015 | 6/17 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.688×** | -3.7 | 0.019 | 12/17 (SW480, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.689×** | -3.5 | 0.026 | 8/17 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.504×** | -3.5 | 0.026 | 10/17 (SHP-77, A549, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.778×** | -3.5 | 0.027 | 10/18 (Hs 766T, AN3 CA, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **0.782×** | -3.4 | 0.033 | 7/18 (SHP-77, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.706×** | -3.4 | 0.034 | 8/18 (SW480, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.714×** | -3.3 | 0.047 | 4/17 (SHP-77, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.734×** | -3.1 | 0.092 | 7/18 (HT-29, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11921. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 63.1 | 7 (1 ⚠) | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 19.1× (z +20.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.224× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~46% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -8.9) |
| [[SHP-77 (line)]] | alt | 91.2 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0762× (z -17.6) |
| [[SW480 (line)]] | alt | 59.0 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0803× (z -15.2) |
| [[C32 (line)]] | wt | 125 | 0 | 7 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.5 µM 0.0770× (z -12.1) |
| [[SW1417 (line)]] | alt | 5.38 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 42.3× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 91.4 | 0 | 4 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.119× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -8.8) |
| [[HT-29 (line)]] | alt | 28.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.140× (z -9.9) |
| [[A-427 (line)]] | wt | 7.06 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 21.4× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 4.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.42× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.11× (z +8.8) | — |
| [[A-172 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11921), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKB]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | STRING 732 |
| [[DACH1]] | +0.65 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[NELL1]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[LINC02466]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[PKHD1]] | +0.62 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[LOXL4]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[TSHZ2]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[LRFN2]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ASCL1]] | +0.60 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[RIT2]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[RMST]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[FKBP9P1-1]] | +0.58 | +0.49 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 2, C 22. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHRM3]] | B | CHRM3 activity raises AGMO's level | lines that do not express CHRM3 (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without CHRM3 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, NRXN1, MIR2052HG |
| [[LINC02466]] | B | LINC02466 activity raises AGMO's level | lines that do not express LINC02466 (21) vs lines expressing it (29) | 1.78× lower at baseline in the lines without LINC02466 | 0.090 | ⚠ within organs, on part of the lines; also absent: MME, ENSG00000227088, GABRA3; maybe low, not absent |
| [[DGKB]] | C | DGKB activity raises AGMO's level | lines that do not express DGKB (23) vs lines expressing it (27) | 3.08× lower at baseline in the lines without DGKB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent; co-absent with the target |
| [[CALCA]] | C | CALCA activity raises AGMO's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.32× lower at baseline in the lines without CALCA | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[LOXL4]] | C | LOXL4 activity raises AGMO's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 1.98× lower at baseline in the lines without LOXL4 | 0.014 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3; co-absent with the target |
| [[TSHZ2]] | C | TSHZ2 activity raises AGMO's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.35× lower at baseline in the lines without TSHZ2 | 0.014 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5; co-absent with the target |
| [[ST18]] | C | ST18 activity raises AGMO's level | lines that do not express ST18 (39) vs lines expressing it (11) | 2.86× lower at baseline in the lines without ST18 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[PHYHIPL]] | C | PHYHIPL activity raises AGMO's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 2.36× lower at baseline in the lines without PHYHIPL | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises AGMO's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.06× lower at baseline in the lines without RIT2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises AGMO's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.36× lower at baseline in the lines without RUNX1T1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[PROX1-AS1]] | C | PROX1-AS1 activity raises AGMO's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 2.22× lower at baseline in the lines without PROX1-AS1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1; co-absent with the target |
| [[APOD]] | C | APOD activity raises AGMO's level | lines that do not express APOD (43) vs lines expressing it (7) | 3.48× lower at baseline in the lines without APOD | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 6, C 16. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR325HG]] | B | AGMO activity raises MIR325HG's level | lines that do not express AGMO (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without AGMO | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657 |
| [[LINC02466]] | B | AGMO activity raises LINC02466's level | lines that do not express AGMO (30) vs lines expressing it (20) | 1.47× lower at baseline in the lines without AGMO | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657 |
| [[CHRM3]] | B | AGMO activity raises CHRM3's level | lines that do not express AGMO (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without AGMO | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657 |
| [[UNC80]] | B | AGMO activity raises UNC80's level | lines that do not express AGMO (30) vs lines expressing it (20) | 1.74× lower at baseline in the lines without AGMO | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657 |
| [[CSRNP3]] | B | AGMO activity raises CSRNP3's level | lines that do not express AGMO (30) vs lines expressing it (20) | 2.13× lower at baseline in the lines without AGMO | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657 |
| [[FKBP9P1]] | B | AGMO activity raises FKBP9P1's level | lines that do not express AGMO (30) vs lines expressing it (20) | 1.59× lower at baseline in the lines without AGMO | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657 |
| [[DACH1]] | C | AGMO activity raises DACH1's level | lines that do not express AGMO (30) vs lines expressing it (20) | 3.56× lower at baseline in the lines without AGMO | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657; co-absent with the target |
| [[DGKB]] | C | AGMO activity raises DGKB's level | lines that do not express AGMO (30) vs lines expressing it (20) | 2.22× lower at baseline in the lines without AGMO | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657; co-absent with the target |
| [[LOXL4]] | C | AGMO activity raises LOXL4's level | lines that do not express AGMO (30) vs lines expressing it (20) | 1.76× lower at baseline in the lines without AGMO | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657; co-absent with the target |
| [[FGF9]] | C | AGMO activity raises FGF9's level | lines that do not express AGMO (30) vs lines expressing it (20) | 2.55× lower at baseline in the lines without AGMO | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657; co-absent with the target |
| [[GRIA2]] | C | AGMO activity raises GRIA2's level | lines that do not express AGMO (30) vs lines expressing it (20) | 2.06× lower at baseline in the lines without AGMO | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657; co-absent with the target |
| [[MIR3667HG]] | C | AGMO activity raises MIR3667HG's level | lines that do not express AGMO (30) vs lines expressing it (20) | 2.26× lower at baseline in the lines without AGMO | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.497). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.6, 38.6); signed map (46.4, 33.2). **Vector** length 56.8, 14.9% of its response variance represented; |z| ≥ 3 in 570 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +14.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +22.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +13.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +3.6 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.8 | -5.1 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | alkylglycerol monooxygenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.2 — chr7:15,200,317-15,562,015 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ16237; previously TMEM195 |
| Gene groups (HGNC) | Fatty acid hydroxylase domain containing |
| Reactome | 3 pathways, smallest: Triglyceride biosynthesis; Triglyceride metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZNB7](https://www.uniprot.org/uniprotkb/Q6ZNB7) (Alkylglycerol monooxygenase):

> Glyceryl-ether monooxygenase that cleaves the O-alkyl bond of ether lipids. Ether lipids are essential components of brain membranes.

**Summary**, from NCBI Gene [392636](https://www.ncbi.nlm.nih.gov/gene/392636):

> The protein encoded by this gene is a tetrahydrobiopterin- and iron-dependent enzyme that cleaves the ether bond of alkylglycerols. Sequence comparisons distinguish this protein as forming a third, distinct class of tetrahydrobiopterin-dependent enzymes. Variations in this gene have been associated with decreased glucose-stimulated insulin response, type 2 diabetes, and susceptibility to intracranial aneurysms. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:33784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33784) · Entrez [392636](https://www.ncbi.nlm.nih.gov/gene/392636) · UniProt [Q6ZNB7](https://www.uniprot.org/uniprotkb/Q6ZNB7) · Ensembl [ENSG00000187546](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187546)

## Data

Gene col 11921: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11921); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11921, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11921]; `tensor/DDL_lfc|DDL_z.npy` [11921]; `embed/gene_vectors.npy` [11921]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11921 or target_col == 11921). Every well: [[AGMO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGMO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
