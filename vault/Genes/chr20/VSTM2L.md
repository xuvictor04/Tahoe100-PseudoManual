---
symbol: "VSTM2L"
type: "gene"
col: 5376
ensembl_id: "ENSG00000132821"
name: "V-set and transmembrane domain containing 2 like"
location: "20q11.23"
module: 98
arm: "+"
pooled_cpm: 2.64
n_lines_expressing: 30
n_dd_up: 36
n_dd_down: 1
n_dd_up_clean: 28
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# VSTM2L

*V-set and transmembrane domain containing 2 like* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.32× (z +17.0, q 0e+00, up in 15 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Glycyrrhizic acid (drug)]] 5 µM: 0.628× (z -3.8, q 0.096, down in 3 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (SW 900 0.148×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.232×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 0.158×; ⚠ toxic; transcription drop); [[Pioglitazone (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0961×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAOA]] (+0.73, fdr 7e-06), [[TLR2]] (+0.70, fdr 7e-06), [[ITGA10]] (+0.69, fdr 7e-06); moves opposite to [[IFT57]] (-0.50, fdr 4e-05), [[CD47]] (-0.50, fdr 3e-05), [[DUSP10]] (-0.49, fdr 3e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 3 go from it, the strongest it → [[DNER]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.32×** | +17.0 | 0e+00 | 15/18 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.78×** | +12.4 | 1e-32 | 2/5 (NCI-H2347, MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.43×** | +10.3 | 2e-22 | 19/24 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.17×** | +9.5 | 5e-19 | 2/11 (NCI-H1792, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Budesonide (drug)]] 0.5 µM |  | **2.53×** | +7.6 | 4e-12 | 14/22 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.63×** | +7.3 | 2e-11 | 1/7 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.46×** | +7.1 | 1e-10 | 5/11 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.32×** | +6.9 | 4e-10 | 10/25 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.05×** | +5.9 | 3e-07 | 10/20 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +5.8 | 4e-07 | 5/18 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.03×** | +5.8 | 4e-07 | 10/21 (NCI-H1792, HOP62, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.97×** | +5.5 | 2e-06 | 12/23 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.60×** | +5.4 | 3e-06 | 10/23 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.93×** | +5.3 | 3e-06 | 10/18 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +5.3 | 3e-06 | 7/13 (MIA PaCa-2, BT-474, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.92×** | +5.3 | 3e-06 | 10/21 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +5.2 | 8e-06 | 4/16 (MIA PaCa-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.84×** | +5.0 | 2e-05 | 9/20 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.73×** | +4.5 | 2e-04 | 5/16 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5376.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (SW 900 0.148×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.232×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 0.158×; ⚠ toxic; transcription drop); [[Pioglitazone (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0961×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.628×** | -3.8 | 0.096 | 3/19 (RPMI-7951, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Gefitinib (drug)]] 0.5 µM |  | 0.676× | -3.3 | 0.26 | 0/25 | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.676× | -3.1 | 0.36 | 3/25 (RPMI-7951, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 4.73 | 18 | 0 | [[Triamcinolone (drug)]] 5 µM 13.8× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 7 | 1 | [[Budesonide (drug)]] 0.5 µM 9.60× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -9.2) |
| [[SW 900 (line)]] | alt | 31.4 | 0 | 2 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.148× (z -9.3) |
| [[A549 (line)]] | wt | 2.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.91× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 1.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.2× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 4.00 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0961× (z -8.5) |
| [[PANC-1 (line)]] | alt | 2.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.28× (z +9.0) | — |
| [[A-172 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.941 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.727 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.337 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.511 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.727 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.964 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.591 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAOA]] | +0.73 | +0.68 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TLR2]] | +0.70 | +0.60 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ITGA10]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[IRAK3]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ADGRG2]] | +0.67 | +0.61 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[MT1M]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[FKBP5]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[ADPRHL1]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[MAFB]] | +0.64 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[PHACTR3]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[KLF9]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[KCNB1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT57]] | -0.50 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[CD47]] | -0.50 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[DUSP10]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[PLAU]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises VSTM2L's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[JPH2]] | B | JPH2 activity lowers VSTM2L's level | lines that do not express JPH2 (19) vs lines expressing it (31) | 1.00× higher at baseline in the lines without JPH2 | 0.093 | ⚠ within organs, on part of the lines; also absent: COL7A1, HDX, SRGN; maybe low, not absent |
| [[BATF]] | B | BATF activity strengthens VSTM2L's drug response | lines that do not express BATF (16) vs lines expressing it (10) | the lines without BATF respond 1.02× as strongly (z diff -0.38); strongest at Clobetasol propionate 0.05 µM: 1.78x vs 6.42x (z diff +3.8) | 0.095 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNER]] | B | VSTM2L activity lowers DNER's level | lines that do not express VSTM2L (20) vs lines expressing it (30) | 1.16× higher at baseline in the lines without VSTM2L | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF829, PKD2L2-DT, ZNF625; maybe low, not absent |
| [[STXBP5-AS1]] | B | VSTM2L activity lowers STXBP5-AS1's level | lines that do not express VSTM2L (20) vs lines expressing it (30) | 1.27× higher at baseline in the lines without VSTM2L | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF829, PKD2L2-DT, ZNF625; maybe low, not absent |
| [[PON3]] | B | VSTM2L activity raises PON3's level | lines that do not express VSTM2L (20) vs lines expressing it (30) | 1.21× lower at baseline in the lines without VSTM2L | 0.091 | ⚠ within organs, on part of the lines; also absent: ZNF829, PKD2L2-DT, ZNF625; maybe low, not absent |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.850). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.9, 15.5); signed map (17.4, 31.5). **Vector** length 61.0, 13.4% of its response variance represented; |z| ≥ 3 in 753 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +17.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +9.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.4 | +5.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.4 | +7.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +5.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.2 | +3.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.7 |
|  | [[Rifaximin (drug)]] 0.05 µM |  | -1.0 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.0 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | V-set and transmembrane domain containing 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:37,903,111-37,945,350 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1118M15.2; previously C20orf102 |
| Gene groups (HGNC) | V-set domain containing |
| Matched by | ensembl_id |

UniProt [Q96N03](https://www.uniprot.org/uniprotkb/Q96N03) carries no function annotation.

**Summary**, from NCBI Gene [128434](https://www.ncbi.nlm.nih.gov/gene/128434):

> Involved in negative regulation of neuron apoptotic process. Located in cytoplasm and extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16096) · Entrez [128434](https://www.ncbi.nlm.nih.gov/gene/128434) · UniProt [Q96N03](https://www.uniprot.org/uniprotkb/Q96N03) · Ensembl [ENSG00000132821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132821)

## Data

Gene col 5376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5376); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5376]; `tensor/DDL_lfc|DDL_z.npy` [5376]; `embed/gene_vectors.npy` [5376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5376 or target_col == 5376). Every well: [[VSTM2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VSTM2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
