---
symbol: "NEK10"
type: "gene"
col: 8701
ensembl_id: "ENSG00000163491"
name: "NIMA related kinase 10"
location: "3p24.1"
module: 39
arm: "+"
pooled_cpm: 19.8
n_lines_expressing: 44
n_dd_up: 24
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 24
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# NEK10

*NIMA related kinase 10* — 3p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.43× (z +19.3, q 0e+00, up in 39 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Radotinib (drug)]] 5 µM: 0.665× (z -5.3, q 6e-05, down in 24 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPP4]] (+0.76, fdr 7e-06), [[LINC01934]] (+0.72, fdr 7e-06), [[MYH15]] (+0.71, fdr 7e-06); moves opposite to [[USP30]] (-0.67, fdr 7e-06), [[ARNT]] (-0.64, fdr 1e-05), [[IFT172]] (-0.64, fdr 1e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ZEB1]] → it (grade B ⚠); 24 go from it, the strongest it → [[HCG17]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8701.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.43×** | +19.3 | 0e+00 | 39/41 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.19×** | +15.0 | 0e+00 | 31/38 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.23×** | +13.2 | 2e-37 | 38/39 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.89×** | +11.9 | 1e-30 | 37/41 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.40×** | +11.2 | 5e-27 | 30/42 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.12×** | +9.7 | 3e-20 | 37/41 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +9.0 | 1e-17 | 33/41 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.35×** | +7.8 | 5e-13 | 25/41 (SW480, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.28×** | +7.5 | 3e-12 | 25/42 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.29×** | +7.3 | 2e-11 | 24/41 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.79×** | +4.6 | 3e-04 | 21/41 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.69×** | +4.4 | 4e-04 | 12/26 (RPMI-7951, SW480, …) | inconsistent across doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +4.4 | 5e-04 | 23/41 (HOP62, NCI-H460, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.58×** | +4.2 | 0.001 | 19/40 (SW 900, NCI-H1792, …) | all doses, flat |  |
| [[BAY1125976 (drug)]] 5 µM |  | **2.27×** | +3.9 | 0.003 | 17/42 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.005 | 17/42 (PANC-1, SW480, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.055 | 10/41 (LOX-IMVI, RPMI-7951, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.055 | 13/41 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.87×** | +3.0 | 0.069 | 14/40 (NCI-H460, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8701.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.665×** | -5.3 | 6e-05 | 24/41 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.404×** | -4.4 | 0.004 | 19/42 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.762×** | -3.6 | 0.065 | 7/42 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **0.672×** | -3.5 | 0.065 | 16/41 (A498, HS-578T, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.496×** | -3.4 | 0.080 | 11/37 (C32, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.699×** | -3.3 | 0.080 | 11/42 (hTERT-HPNE, H4, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.699×** | -3.3 | 0.080 | 16/41 (HS-578T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Fumaric acid (drug)]] 5 µM |  | 0.708× | -3.1 | 0.15 | 5/42 (SW 1088, LoVo, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8701. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.69 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +17.8) | — |
| [[HOP62 (line)]] | alt | 19.7 | 7 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 16.4× (z +13.1) | — |
| [[C32 (line)]] | wt | 22.5 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +15.7) | [[Roxadustat (drug)]] 0.05 µM 0.0883× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 13.4 | 5 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +13.8) | — |
| [[SK-MEL-2 (line)]] | alt | 23.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 8.99 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.25× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 10.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.00× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 5.87 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.06× (z +11.1) | — |
| [[LoVo (line)]] | wt | 6.42 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +15.2) | — |
| [[LOX-IMVI (line)]] | wt | 27.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 8.20 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.105× (z -8.9) |
| [[RKO (line)]] | wt | 16.4 | 3 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 24.7× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 29.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.21× (z +10.9) | [[Orlistat (drug)]] 0.05 µM 0.0846× (z -9.7) |
| [[SW 900 (line)]] | alt | 16.7 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +9.7) | [[Silodosin (drug)]] 5 µM 0.0600× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 6.03 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +10.3) | — |
| [[HepG2_C3A (line)]] | wt | 31.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.02× (z +12.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0656× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[NCI-H1792 (line)]] | alt | 11.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 10.9× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 30.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.94× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.167× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 13.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.15× (z +11.0) | — |
| [[A-427 (line)]] | wt | 9.50 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +8.6) | — |
| [[A549 (line)]] | wt | 14.1 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0822× (z -10.0) |
| [[COLO 205 (line)]] | alt | 4.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.4× (z +11.8) | — |
| [[HCT15 (line)]] | alt | 9.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +9.1) | — |
| [[KATO III (line)]] | alt | 6.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.07× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 70.4 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.359× (z -13.6) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 35.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +13.0) | — |
| [[A498 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 20.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8701), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP4]] | +0.76 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[LINC01934]] | +0.72 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[MYH15]] | +0.71 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[LINC02798]] | +0.70 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[LINC01204]] | +0.70 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ITPR2-AS1]] | +0.69 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[DPYS]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.68 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[IMPG2]] | +0.68 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SSUH2]] | +0.68 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[LINC01191]] | +0.68 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[TBILA]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP30]] | -0.67 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[ARNT]] | -0.64 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[IFT172]] | -0.64 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[PRUNE1]] | -0.62 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[CRYZL1]] | -0.61 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[NCK1]] | -0.61 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[SNAPC3]] | -0.59 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[PEX3]] | -0.58 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[PLA2G12A]] | -0.58 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[RCOR3]] | -0.58 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[DIXDC1]] | -0.57 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[C12orf76]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZEB1]] | B | ZEB1 activity raises NEK10's level | lines that do not express ZEB1 (9) vs lines expressing it (41) | 2.75× lower at baseline in the lines without ZEB1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1 |
| [[TOP2A]] | B | TOP2A activity lowers NEK10's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[COL27A1]] | B | COL27A1 activity raises NEK10's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 2.35× lower at baseline in the lines without COL27A1 | 0.035 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[ASGR1]] | B | ASGR1 activity raises NEK10's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.58× lower at baseline in the lines without ASGR1 | 0.070 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[EID2B]] | B | EID2B activity raises NEK10's level | lines that do not express EID2B (13) vs lines expressing it (37) | 2.37× lower at baseline in the lines without EID2B | 0.077 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity raises NEK10's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 3.90× lower at baseline in the lines without ITPR2-AS1 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17; co-absent with the target |
| [[ITPR2]] | C | ITPR2 activity raises NEK10's level | lines that do not express ITPR2 (5) vs lines expressing it (45) | 2.91× lower at baseline in the lines without ITPR2 | 0.0999 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ENSG00000286162, SPATA17; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 22, C 2. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HCG17]] | B | NEK10 activity raises HCG17's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.20× lower at baseline in the lines without NEK10 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[CAVIN4]] | B | NEK10 activity raises CAVIN4's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.73× lower at baseline in the lines without NEK10 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[SCUBE2]] | B | NEK10 activity raises SCUBE2's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 3.51× lower at baseline in the lines without NEK10 | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[MSS51]] | B | NEK10 activity raises MSS51's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 1.69× lower at baseline in the lines without NEK10 | 0.021 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[CHPT1]] | B | NEK10 activity raises CHPT1's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without NEK10 | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[GSTA4]] | B | NEK10 activity raises GSTA4's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without NEK10 | 0.036 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[FLACC1]] | B | NEK10 activity raises FLACC1's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 1.80× lower at baseline in the lines without NEK10 | 0.036 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | NEK10 activity raises the cells' numbers under Minodronic acid 0.5 µM (protects the cells) | lines that do not express NEK10 (6) vs lines expressing it (42) | the lines without NEK10: 0.78× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[ALDH8A1]] | B | NEK10 activity raises ALDH8A1's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.17× lower at baseline in the lines without NEK10 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[IFT172]] | B | NEK10 activity raises IFT172's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without NEK10 | 0.053 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[ASGR1]] | B | NEK10 activity raises ASGR1's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.42× lower at baseline in the lines without NEK10 | 0.054 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[ZEB1]] | B | NEK10 activity raises ZEB1's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.66× lower at baseline in the lines without NEK10 | 0.057 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.6, -11.1); signed map (19.7, 8.7). **Vector** length 106, 26.6% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.2 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +19.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +15.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +11.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +4.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.1 | +3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.9 | +4.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +2.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.5 | -5.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.2 | +7.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.1 | -3.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | +0.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | NIMA related kinase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.1 — chr3:27,106,484-27,369,460 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32685 |
| Gene groups (HGNC) | Armadillo like helical domain containing; NIMA related kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZWH5](https://www.uniprot.org/uniprotkb/Q6ZWH5) (Serine/threonine-protein kinase Nek10):

> Plays a role in the cellular response to UV irradiation. Mediates G2/M cell cycle arrest, MEK autoactivation and ERK1/2-signaling pathway activation in response to UV irradiation. In ciliated cells of airways, it is involved in the regulation of mucociliary transport.

**Summary**, from NCBI Gene [152110](https://www.ncbi.nlm.nih.gov/gene/152110):

> Enables protein kinase activity. Involved in several processes, including mucociliary clearance; positive regulation of protein phosphorylation; and regulation of ERK1 and ERK2 cascade. Part of protein kinase complex. Implicated in primary ciliary dyskinesia 44. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18592) · Entrez [152110](https://www.ncbi.nlm.nih.gov/gene/152110) · UniProt [Q6ZWH5](https://www.uniprot.org/uniprotkb/Q6ZWH5) · Ensembl [ENSG00000163491](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163491)

## Data

Gene col 8701: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8701); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8701, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8701]; `tensor/DDL_lfc|DDL_z.npy` [8701]; `embed/gene_vectors.npy` [8701]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8701 or target_col == 8701). Every well: [[NEK10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEK10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
