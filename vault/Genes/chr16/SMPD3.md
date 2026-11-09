---
symbol: "SMPD3"
type: "gene"
col: 2313
ensembl_id: "ENSG00000103056"
name: "sphingomyelin phosphodiesterase 3"
location: "16q22.1"
module: 165
arm: "+"
pooled_cpm: 2.93
n_lines_expressing: 44
n_dd_up: 58
n_dd_down: 1
n_dd_up_clean: 41
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# SMPD3

*sphingomyelin phosphodiesterase 3* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 58 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 26.5× (z +33.0, q 0e+00, up in 35 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 0.761× (z -3.9, q 0.048, down in 7 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW1417 0.146×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.213×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC8A1-AS1]] (+0.63, fdr 1e-05), [[CYP2U1-AS1]] (+0.62, fdr 1e-05), [[ACHE]] (+0.59, fdr 1e-05); moves opposite to [[MRPL19]] (-0.54, fdr 3e-05), [[ERCC8]] (-0.47, fdr 1e-04), [[C5orf22]] (-0.46, fdr 1e-04).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SCG3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NUDT13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 58 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2313.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **26.5×** | +33.0 | 0e+00 | 35/36 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.81×** | +31.0 | 0e+00 | 19/22 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **18.3×** | +29.3 | 0e+00 | 30/31 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **6.57×** | +26.8 | 0e+00 | 23/24 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **8.99×** | +22.1 | 0e+00 | 29/32 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.98×** | +15.6 | 0e+00 | 15/32 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.95×** | +15.5 | 0e+00 | 13/19 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.73×** | +12.8 | 2e-35 | 16/23 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.27×** | +11.5 | 1e-28 | 21/28 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.24×** | +11.4 | 2e-28 | 0/2 | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.08×** | +11.3 | 4e-28 | 2/11 (KATO III, HT-29) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.99×** | +10.6 | 9e-25 | 17/23 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +10.1 | 3e-22 | 17/33 (SW480, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.92×** | +10.0 | 8e-22 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.69×** | +9.6 | 3e-20 | 7/11 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.52×** | +9.3 | 4e-19 | 18/35 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.22×** | +8.0 | 4e-14 | 11/39 (SHP-77, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +7.2 | 2e-11 | 9/26 (A-172, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.85×** | +5.9 | 7e-08 | 16/28 (NCI-H2030, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2313.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW1417 0.146×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.213×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.761×** | -3.9 | 0.048 | 7/27 (HT-29, NCI-H2030, …) | top dose only |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.784× | -3.5 | 0.13 | 6/32 (A-172, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2313. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 4.63 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +18.5) | — |
| [[NCI-H2030 (line)]] | alt | 4.70 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.1× (z +15.6) | — |
| [[SW1417 (line)]] | alt | 31.3 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 8.98× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 1.48 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.1× (z +12.5) | — |
| [[Panc 03.27 (line)]] | alt | 2.61 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.0× (z +10.3) | — |
| [[A498 (line)]] | wt | 1.12 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 53.0× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 14.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 0.959 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 27.1× (z +11.5) | — |
| [[A549 (line)]] | wt | 1.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 47.0× (z +10.1) | — |
| [[C32 (line)]] | wt | 1.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +8.8) | — |
| [[LoVo (line)]] | wt | 2.65 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 17.8× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 0.904 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 85.0× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 1.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.6× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 2.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +9.1) | — |
| [[A-172 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.751 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.984 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.772 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.887 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.766 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.995 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.695 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.773 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.788 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.906 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2313), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC8A1-AS1]] | +0.63 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[CYP2U1-AS1]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[ACHE]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[DISP3]] | +0.58 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[SRRM3]] | +0.57 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[DLGAP2]] | +0.57 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[AP3B2]] | +0.55 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[MUC12]] | +0.54 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[HAP1]] | +0.53 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[RBM38]] | +0.53 | +0.40 / +0.55 | both halves | 4e-05 |  |
| [[PWRN1]] | +0.53 | +0.42 / +0.69 | both halves | 4e-05 |  |
| [[SGCZ]] | +0.52 | +0.50 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL19]] | -0.54 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ERCC8]] | -0.47 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[C5orf22]] | -0.46 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[PPA2]] | -0.46 | -0.37 / -0.26 | both halves | 3e-04 |  |
| [[PEX26]] | -0.45 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[AIFM1]] | -0.44 | -0.29 / -0.36 | both halves | 3e-04 |  |
| [[HERC2P3-1]] | -0.43 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[CEP20]] | -0.43 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[APIP]] | -0.43 | -0.39 / -0.29 | both halves | 2e-04 |  |
| [[METAP1D]] | -0.43 | -0.18 / -0.47 | ⚠ not reproduced | 0.001 |  |
| [[TMEM209]] | -0.43 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[TSEN15]] | -0.43 | -0.36 / -0.25 | both halves | 4e-04 |  |
| [[NUDT13]] | -0.43 | -0.36 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCG3]] | B | SCG3 activity raises SMPD3's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 1.89× lower at baseline in the lines without SCG3 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA |
| [[XKR7]] | B | XKR7 activity raises SMPD3's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 2.05× lower at baseline in the lines without XKR7 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[NPHS1]] | C | NPHS1 activity strengthens SMPD3's drug response | lines that do not express NPHS1 (4) vs lines expressing it (34) | the lines without NPHS1 respond 0.34× as strongly (z diff +2.84); strongest at Idarubicin (hydrochloride) 5 µM: 1.41x vs 11x (z diff +6.2) | 0.010 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUDT13]] | B | SMPD3 activity raises NUDT13's level | lines that do not express SMPD3 (6) vs lines expressing it (44) | 1.40× lower at baseline in the lines without SMPD3 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with NF1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.558). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.1, 33.5); signed map (28.6, 17.8). **Vector** length 49.2, 7.86% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +31.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +26.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +33.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +2.9 | +11.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.5 | +29.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +15.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.6 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +1.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.0 | +0.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.9 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.9 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | sphingomyelin phosphodiesterase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:68,358,327-68,448,508 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NSMASE2 |
| Reactome | 7 pathways, smallest: TNFR1-mediated ceramide production; Glycosphingolipid catabolism; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY59](https://www.uniprot.org/uniprotkb/Q9NY59) (Sphingomyelin phosphodiesterase 3):

> Catalyzes the hydrolysis of sphingomyelin to form ceramide and phosphocholine. Ceramide mediates numerous cellular functions, such as apoptosis and growth arrest, and is capable of regulating these 2 cellular events independently. Also hydrolyzes sphingosylphosphocholine. Regulates the cell cycle by acting as a growth suppressor in confluent cells. Probably acts as a regulator of postnatal development and participates in bone and dentin mineralization. Binds to anionic phospholipids (APLs) such …

**Summary**, from NCBI Gene [55512](https://www.ncbi.nlm.nih.gov/gene/55512):

> Enables sphingomyelin phosphodiesterase activity. Involved in sphingomyelin catabolic process. Located in endoplasmic reticulum. Biomarker of pulmonary emphysema. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14240](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14240) · Entrez [55512](https://www.ncbi.nlm.nih.gov/gene/55512) · UniProt [Q9NY59](https://www.uniprot.org/uniprotkb/Q9NY59) · Ensembl [ENSG00000103056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103056)

## Data

Gene col 2313: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2313); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2313, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2313]; `tensor/DDL_lfc|DDL_z.npy` [2313]; `embed/gene_vectors.npy` [2313]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2313 or target_col == 2313). Every well: [[SMPD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMPD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
