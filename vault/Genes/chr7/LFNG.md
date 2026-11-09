---
symbol: "LFNG"
type: "gene"
col: 2702
ensembl_id: "ENSG00000106003"
name: "LFNG O-fucosylpeptide 3-beta-N-acetylglucosaminyltransferase"
location: "7p22.3"
module: 154
arm: "+"
pooled_cpm: 2.09
n_lines_expressing: 36
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# LFNG

*LFNG O-fucosylpeptide 3-beta-N-acetylglucosaminyltransferase* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.18× (z +17.4, q 0e+00, up in 18 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (SHP-77 0.0335×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (SHP-77 0.0447×); [[Tadalafil (drug)]] 5 µM in 1 line (SW1417 0.0927×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMIZ1]] (+0.59, fdr 3e-05), [[LRIG1]] (+0.58, fdr 1e-04), [[FOXO6]] (+0.56, fdr 3e-05); moves opposite to [[SLC38A6]] (-0.49, fdr 3e-05), [[CMKLR2]] (-0.49, fdr 6e-05), [[BOD1]] (-0.49, fdr 6e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CMKLR2]] → it (grade B ⚠); 4 go from it, the strongest it → [[SMTN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2702.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.18×** | +17.4 | 0e+00 | 18/20 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **6.93×** | +14.5 | 4e-45 | 28/30 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.31×** | +12.5 | 2e-33 | 25/27 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.08×** | +11.9 | 2e-30 | 16/23 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.64×** | +9.7 | 5e-20 | 24/29 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.45×** | +8.9 | 5e-17 | 1/2 (NCI-H1792) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.25×** | +8.1 | 3e-14 | 3/6 (SW1417, HOP62, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.02×** | +7.9 | 2e-13 | 9/17 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.11×** | +7.9 | 2e-13 | 19/29 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.55×** | +7.0 | 1e-10 | 3/12 (NCI-H1792, A498, …) | all doses, flat | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +6.0 | 8e-08 | 7/13 (KATO III, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.11×** | +5.6 | 1e-06 | 5/11 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +5.5 | 2e-06 | 9/21 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +5.1 | 1e-05 | 11/29 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.71×** | +4.0 | 0.003 | 4/16 (Hs 766T, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +3.8 | 0.004 | 11/25 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +3.5 | 0.016 | 7/26 (A498, SW1417, …) | top dose only | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.64×** | +3.4 | 0.023 | 2/15 (PANC-1, A498) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.80×** | +3.1 | 0.054 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.73×** | +2.9 | 0.097 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2702.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (SHP-77 0.0335×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (SHP-77 0.0447×); [[Tadalafil (drug)]] 5 µM in 1 line (SW1417 0.0927×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.745× | -3.2 | 0.57 | 4/28 (LoVo, H4, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2702. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 7.44 | 0 | 2 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0335× (z -10.6) |
| [[A498 (line)]] | wt | 1.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +13.0) | — |
| [[AsPC-1 (line)]] | alt | 0.941 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.1× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 4.54 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0664× (z -8.6) |
| [[SW1417 (line)]] | alt | 5.85 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0927× (z -8.8) |
| [[A-172 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.733 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.369 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.902 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.814 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.951 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.958 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.627 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.457 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.868 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2702), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMIZ1]] | +0.59 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[LRIG1]] | +0.58 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[FOXO6]] | +0.56 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[DOT1L]] | +0.56 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[ACBD7]] | +0.55 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[IFFO2]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ICAM5]] | +0.54 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[COL5A3]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[SEMA3F]] | +0.53 | +0.36 / +0.55 | both halves | 9e-05 | same gene group |
| [[PTHLH]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[PHETA1]] | +0.52 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[FGFR3]] | +0.52 | +0.49 / +0.46 | both halves | 2e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC38A6]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[CMKLR2]] | -0.49 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[BOD1]] | -0.49 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[STXBP5]] | -0.48 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[APOOL]] | -0.48 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[SLC22A15]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[TRMT11]] | -0.47 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[IDE]] | -0.46 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[NARS1]] | -0.46 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[COX10]] | -0.45 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[MRPS35]] | -0.44 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[IARS1]] | -0.44 | -0.49 / -0.39 | both halves | 6e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMKLR2]] | B | CMKLR2 activity raises LFNG's level | lines that do not express CMKLR2 (16) vs lines expressing it (34) | 1.57× lower at baseline in the lines without CMKLR2 | 0.092 | ⚠ within organs, on part of the lines; also absent: SATB1-AS1, ENSG00000231772, NYAP2; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMTN]] | B | LFNG activity strengthens SMTN's drug response | lines that do not express LFNG (14) vs lines expressing it (35) | the lines without LFNG respond 0.59× as strongly (z diff +1.25); strongest at Homoharringtonine 5 µM: 0.99x vs 1.80x (z diff +4.6) | 0.058 | ⚠ within organs, on part of the lines; also absent: TNFSF10, EPHA4, CXXC5; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[FGF9]] | B | LFNG activity raises FGF9's level | lines that do not express LFNG (14) vs lines expressing it (36) | 1.87× lower at baseline in the lines without LFNG | 0.067 | ⚠ within organs, on part of the lines; also absent: TNFSF10, EPHA4, CXXC5; maybe low, not absent |
| [[TTYH3]] | B | LFNG activity raises TTYH3's level | lines that do not express LFNG (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without LFNG | 0.078 | ⚠ within organs, on part of the lines; also absent: TNFSF10, EPHA4, CXXC5; maybe low, not absent |
| cells under [[Neratinib (drug)]] 5 µM | B | LFNG activity raises the cells' numbers under Neratinib 5 µM (protects the cells) | lines that do not express LFNG (14) vs lines expressing it (34) | the lines without LFNG: 0.86× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: TNFSF10, EPHA4, CXXC5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.8, -3.7); signed map (-4.3, 29.0). **Vector** length 45.9, 7.84% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +17.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.2 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +11.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +0.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | LFNG O-fucosylpeptide 3-beta-N-acetylglucosaminyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:2,512,529-2,529,177 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SCDO3 |
| Gene groups (HGNC) | Beta 3-glycosyltransferases; MicroRNA protein coding host genes |
| Hallmark sets | NOTCH_SIGNALING, KRAS_SIGNALING_DN |
| Reactome | 12 pathways, smallest: Defective LFNG causes SCDO3; Nephron development; Pre-NOTCH Processing in Golgi |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NES3](https://www.uniprot.org/uniprotkb/Q8NES3) (Beta-1,3-N-acetylglucosaminyltransferase lunatic fringe):

> Glycosyltransferase that initiates the elongation of O-linked fucose residues attached to EGF-like repeats in the extracellular domain of Notch molecules. Modulates NOTCH1 activity by modifying O-fucose residues at specific EGF-like domains resulting in inhibition of NOTCH1 activation by JAG1 and enhancement of NOTCH1 activation by DLL1 via an increase in its binding to DLL1 (By similarity). Decreases the binding of JAG1 to NOTCH2 but not that of DLL1. Essential mediator of somite segmentation …

**Summary**, from NCBI Gene [3955](https://www.ncbi.nlm.nih.gov/gene/3955):

> This gene is a member of the glycosyltransferase 31 gene family. Members of this gene family, which also includes the MFNG (GeneID: 4242) and RFNG (GeneID: 5986) genes, encode evolutionarily conserved glycosyltransferases that act in the Notch signaling pathway to define boundaries during embryonic development. While their genomic structure is distinct from other glycosyltransferases, these proteins have a fucose-specific beta-1,3-N-acetylglucosaminyltransferase activity that leads to …

**Accessions** — [HGNC:6560](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6560) · Entrez [3955](https://www.ncbi.nlm.nih.gov/gene/3955) · UniProt [Q8NES3](https://www.uniprot.org/uniprotkb/Q8NES3) · Ensembl [ENSG00000106003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106003)

## Data

Gene col 2702: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2702); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2702, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2702]; `tensor/DDL_lfc|DDL_z.npy` [2702]; `embed/gene_vectors.npy` [2702]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2702 or target_col == 2702). Every well: [[LFNG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LFNG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
