---
symbol: "BSN"
type: "gene"
col: 8850
ensembl_id: "ENSG00000164061"
name: "bassoon presynaptic cytomatrix protein"
location: "3p21.31"
module: 209
arm: "+"
pooled_cpm: 7.0
n_lines_expressing: 33
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 13
tags: ["gene", "module/209"]
generated_by: "tahoemap"
---

# BSN

*bassoon presynaptic cytomatrix protein* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 11.6× (z +31.7, q 0e+00, up in 29 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Peretinoin (drug)]] 5 µM: 0.717× (z -4.2, q 0.018, down in 1 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 0.127×, SHP-77 0.199×, A-427 0.260×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.137×, LOX-IMVI 0.156×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.126×; ⚠ cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.295×); [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0634×); [[Auranofin (drug)]] 5 µM in 1 line (C-33 A 0.184×).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM167A]] (+0.52, fdr 5e-05), [[FAAP100]] (+0.49, fdr 9e-05), [[TMEM175]] (+0.48, fdr 7e-05); moves opposite to [[DISC1]] (-0.46, fdr 4e-04), [[C2]] (-0.43, fdr 9e-04, ⚠ not reproduced), [[RAPGEF4]] (-0.43, fdr 1e-04), [[DOCK7-DT]] (-0.42, fdr 2e-04).
> It is in [[Module 209]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[POTEF]] → it (grade B ⚠); 13 go from it, the strongest it → [[DNAJC14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **11.6×** | +31.7 | 0e+00 | 29/30 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **9.35×** | +28.9 | 0e+00 | 27/29 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.21×** | +26.3 | 0e+00 | 18/23 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **6.28×** | +23.8 | 0e+00 | 24/29 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.94×** | +13.4 | 5e-39 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +12.9 | 4e-36 | 9/25 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.69×** | +12.3 | 6e-33 | 7/15 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +9.9 | 3e-21 | 3/9 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +8.9 | 2e-17 | 14/29 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +8.5 | 1e-15 | 16/27 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +7.6 | 1e-12 | 12/24 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +6.2 | 2e-08 | 8/28 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.3 | 5e-06 | 1/13 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.11×** | +5.1 | 2e-05 | 6/25 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.46×** | +4.9 | 3e-05 | 7/28 (NCI-H460, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.002 | 6/28 (SK-MEL-2, Panc 03.27, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.009 | 7/25 (NCI-H23, SW480, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.009 | 3/28 (A549, NCI-H460, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.68×** | +3.5 | 0.012 | 2/21 (NCI-H2347, MIA PaCa-2) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.013 | 3/29 (SW480, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8850.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 0.127×, SHP-77 0.199×, A-427 0.260×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.137×, LOX-IMVI 0.156×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.126×; ⚠ cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.295×); [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0634×); [[Auranofin (drug)]] 5 µM in 1 line (C-33 A 0.184×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Peretinoin (drug)]] 5 µM |  | **0.717×** | -4.2 | 0.018 | 1/27 (NCI-H2030) | top dose only | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 0.759× | -3.4 | 0.15 | 2/28 (SW 900, PANC-1) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.773× | -3.3 | 0.15 | 7/28 (NCI-H2347, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Hesperidin (drug)]] 5 µM |  | 0.771× | -3.2 | 0.16 | 4/25 (A-172, SNU-1, …) | top dose only |  |
| [[Captopril (drug)]] 0.5 µM |  | 0.785× | -3.1 | 0.19 | 2/27 (HEC-1-A, BT-474) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.63 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 8.04× (z +13.1) | — |
| [[A-427 (line)]] | wt | 36.1 | 0 | 4 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.295× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 2.33 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 15.7× (z +9.3) | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0634× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 2.13 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 17.6× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 7.04 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.87× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.127× (z -11.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 26.5 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.184× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 1.84 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.04× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 3.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 45.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.924 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.824 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.836 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.757 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM167A]] | +0.52 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[FAAP100]] | +0.49 | +0.46 / +0.36 | both halves | 9e-05 |  |
| [[TMEM175]] | +0.48 | +0.45 / +0.38 | both halves | 7e-05 |  |
| [[DAGLA]] | +0.48 | +0.41 / +0.38 | both halves | 6e-05 |  |
| [[KAT5]] | +0.47 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[BCL7B]] | +0.47 | +0.49 / +0.33 | both halves | 1e-04 |  |
| [[NLRP2]] | +0.47 | +0.42 / +0.39 | both halves | 6e-05 |  |
| [[ZNF18]] | +0.45 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[MT1G]] | +0.45 | +0.49 / +0.28 | both halves | 3e-04 |  |
| [[DNAJB5]] | +0.45 | +0.43 / +0.36 | both halves | 1e-04 |  |
| [[ZSCAN9]] | +0.44 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[C19orf47]] | +0.44 | +0.42 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DISC1]] | -0.46 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[C2]] | -0.43 | -0.18 / -0.32 | ⚠ not reproduced | 9e-04 |  |
| [[RAPGEF4]] | -0.43 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[DOCK7-DT]] | -0.42 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[HOXB6]] | -0.42 | -0.39 / -0.25 | both halves | 4e-04 |  |
| [[REXO2]] | -0.42 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[LINC02680]] | -0.41 | -0.19 / -0.45 | ⚠ not reproduced | 8e-04 |  |
| [[LINC02641]] | -0.41 | -0.07 / -0.41 | ⚠ not reproduced | 0.004 |  |
| [[LEPR]] | -0.40 | -0.19 / -0.44 | ⚠ not reproduced | 8e-04 |  |
| [[PPHLN1]] | -0.40 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[MESD]] | -0.40 | -0.29 / -0.32 | both halves | 2e-04 |  |
| [[GABRE]] | -0.40 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[CCNH]] | -0.39 | -0.26 / -0.31 | both halves | 3e-04 |  |
| [[SOS1]] | -0.39 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[C9orf153]] | -0.39 | -0.24 / -0.36 | both halves | 4e-04 |  |
| [[HSPH1]] | -0.38 | -0.21 / -0.31 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POTEF]] | B | POTEF activity raises BSN's level | lines that do not express POTEF (29) vs lines expressing it (21) | 2.60× lower at baseline in the lines without POTEF | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |
| [[ELFN1]] | B | ELFN1 activity raises BSN's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.81× lower at baseline in the lines without ELFN1 | 0.071 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAJC14]] | B | BSN activity raises DNAJC14's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.31× lower at baseline in the lines without BSN | 0.004 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[OTUD7A]] | B | BSN activity raises OTUD7A's level | lines that do not express BSN (17) vs lines expressing it (33) | 2.63× lower at baseline in the lines without BSN | 0.007 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[CCDC113]] | B | BSN activity raises CCDC113's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.66× lower at baseline in the lines without BSN | 0.023 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[SURF2]] | B | BSN activity raises SURF2's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.27× lower at baseline in the lines without BSN | 0.048 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[ABCC10]] | B | BSN activity raises ABCC10's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.37× lower at baseline in the lines without BSN | 0.068 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[PPHLN1]] | B | BSN activity raises PPHLN1's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.25× lower at baseline in the lines without BSN | 0.071 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[ZNF678]] | B | BSN activity raises ZNF678's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.50× lower at baseline in the lines without BSN | 0.071 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[UQCC2]] | B | BSN activity raises UQCC2's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.37× lower at baseline in the lines without BSN | 0.074 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[LEPR]] | B | BSN activity lowers LEPR's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.37× higher at baseline in the lines without BSN | 0.074 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[GABRE]] | B | BSN activity lowers GABRE's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.82× higher at baseline in the lines without BSN | 0.083 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[NOC4L]] | B | BSN activity raises NOC4L's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.08× lower at baseline in the lines without BSN | 0.093 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[TNKS1BP1]] | B | BSN activity lowers TNKS1BP1's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.46× higher at baseline in the lines without BSN | 0.095 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 209]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.321). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.5, 20.7); signed map (-14.5, -24.3). **Vector** length 45.6, 7.20% of its response variance represented; |z| ≥ 3 in 729 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +26.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +13.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +28.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +31.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.1 | +2.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.8 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.4 | +0.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -3.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | bassoon presynaptic cytomatrix protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,554,477-49,671,549 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZNF231 |
| Gene groups (HGNC) | Zinc fingers PCLO-type |
| Reactome | 3 pathways, smallest: Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound; Sensory Perception |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPA5](https://www.uniprot.org/uniprotkb/Q9UPA5) (Protein bassoon):

> Scaffold protein of the presynaptic cytomatrix at the active zone (CAZ) which is the place in the synapse where neurotransmitter is released. After synthesis, participates in the formation of Golgi-derived membranous organelles termed Piccolo-Bassoon transport vesicles (PTVs) that are transported along axons to sites of nascent synaptic contacts. At the presynaptic active zone, regulates the spatial organization of synaptic vesicle cluster, the protein complexes that execute membrane fusion and …

**Summary**, from NCBI Gene [8927](https://www.ncbi.nlm.nih.gov/gene/8927):

> Neurotransmitters are released from a specific site in the axon terminal called the active zone, which is composed of synaptic vesicles and a meshwork of cytoskeleton underlying the plasma membrane. The protein encoded by this gene is thought to be a scaffolding protein involved in organizing the presynaptic cytoskeleton. The gene is expressed primarily in neurons in the brain. A similar gene product in rodents is concentrated in the active zone of axon terminals and tightly associated with …

**Accessions** — [HGNC:1117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1117) · Entrez [8927](https://www.ncbi.nlm.nih.gov/gene/8927) · UniProt [Q9UPA5](https://www.uniprot.org/uniprotkb/Q9UPA5) · Ensembl [ENSG00000164061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164061)

## Data

Gene col 8850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8850); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8850]; `tensor/DDL_lfc|DDL_z.npy` [8850]; `embed/gene_vectors.npy` [8850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8850 or target_col == 8850). Every well: [[BSN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BSN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
