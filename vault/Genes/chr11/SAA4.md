---
symbol: "SAA4"
type: "gene"
col: 7332
ensembl_id: "ENSG00000148965"
name: "serum amyloid A4, constitutive"
location: "11p15.1"
module: 139
arm: "+"
pooled_cpm: 3.38
n_lines_expressing: 28
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 32
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 19
direction_downstream: 30
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# SAA4

*serum amyloid A4, constitutive* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.59× (z +12.7, q 5e-34, up in 14 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.112×, SNU-423 0.0772×); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 0.0455×, COLO 205 0.0298×; ⚠ cell-cycle shift, explains ~56% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 0.0743×, CFPAC-1 0.0498×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Tofacitinib (drug)]] 0.5 µM in 2 lines (COLO 205 0.0845×, SNU-423 0.0735×); [[Tofacitinib (drug)]] 5 µM in 1 line (COLO 205 0.113×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAA2-SAA4]] (+0.97, fdr 7e-06, ⚠ same locus), [[SAA2]] (+0.97, fdr 7e-06, ⚠ same locus), [[SAA1]] (+0.92, fdr 7e-06, ⚠ same locus), [[SLPI]] (+0.72, fdr 7e-06), [[C3]] (+0.71, fdr 7e-06), [[NNMT]] (+0.69, fdr 7e-06); moves opposite to [[DCBLD2]] (-0.52, fdr 2e-05), [[CAPN2]] (-0.49, fdr 3e-05), [[HHIP]] (-0.47, fdr 3e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[HLA-DRB1]] → it (grade B ⚠); 30 go from it, the strongest it → [[ZC3H12A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7332.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.59×** | +12.7 | 5e-34 | 14/18 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **4.20×** | +10.6 | 1e-23 | 23/24 (A498, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.22×** | +8.3 | 3e-14 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.95×** | +7.1 | 1e-10 | 20/21 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **3.14×** | +5.9 | 3e-07 | 15/22 (A498, A-172, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.92×** | +5.6 | 2e-06 | 13/23 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.98×** | +5.0 | 4e-05 | 9/24 (A-172, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.54×** | +4.8 | 1e-04 | 12/23 (A498, J82, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.93×** | +4.8 | 1e-04 | 13/22 (A498, A549, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.46×** | +4.7 | 2e-04 | 15/23 (A498, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **2.44×** | +4.6 | 2e-04 | 13/23 (A498, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.42×** | +4.6 | 2e-04 | 14/23 (A498, A549, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +4.4 | 6e-04 | 4/20 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 0.05 µM |  | **2.29×** | +4.3 | 6e-04 | 12/21 (A498, A549, …) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.29×** | +4.3 | 6e-04 | 10/20 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.28×** | +4.3 | 6e-04 | 13/21 (A498, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.31×** | +4.2 | 1e-03 | 14/23 (A498, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7332.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.112×, SNU-423 0.0772×); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 0.0455×, COLO 205 0.0298×; ⚠ cell-cycle shift, explains ~56% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 0.0743×, CFPAC-1 0.0498×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Tofacitinib (drug)]] 0.5 µM in 2 lines (COLO 205 0.0845×, SNU-423 0.0735×); [[Tofacitinib (drug)]] 5 µM in 1 line (COLO 205 0.113×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | 0.516× | -3.3 | 0.22 | 7/24 (CFPAC-1, A498, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.643× | -3.3 | 0.22 | 14/23 (COLO 205, SNU-423, …) | rises with dose | position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.546× | -3.2 | 0.22 | 12/22 (COLO 205, SNU-423, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.549× | -3.2 | 0.22 | 11/24 (A498, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7332. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 27.6 | 4 (1 ⚠) | 6 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 8.20× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.0274× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.112× (z -13.7) |
| [[COLO 205 (line)]] | alt | 20.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0298× (z -11.7) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.113× (z -10.7) |
| [[A-172 (line)]] | wt | 3.98 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0772× (z -11.8) |
| [[A549 (line)]] | wt | 5.77 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0238× (z -9.8) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0498× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HT-29 (line)]] | alt | 0.874 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 42.4× (z +9.4) | — |
| [[J82 (line)]] | alt | 3.24 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.9× (z +9.2) | — |
| [[A-427 (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.942 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.705 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.355 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.978 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.382 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7332), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAA2-SAA4]] | +0.97 | +0.97 / +0.97 | both halves | 7e-06 | STRING 703; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SAA2]] | +0.97 | +0.97 / +0.97 | both halves | 7e-06 | STRING 935; ⚠ same locus (2.4 kb, same strand: neighbours can correlate without regulation) |
| [[SAA1]] | +0.92 | +0.92 / +0.93 | both halves | 7e-06 | STRING 762; ⚠ same locus (29.5 kb: neighbours can correlate without regulation) |
| [[SLPI]] | +0.72 | +0.66 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[C3]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[NNMT]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[IRAK3]] | +0.67 | +0.55 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[BCL6]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[FGA]] | +0.65 | +0.63 / +0.67 | both halves | 7e-06 | STRING 522 |
| [[CEBPD]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[C1RL]] | +0.63 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[NAMPT]] | +0.63 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[TLR2]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 | STRING 527 |
| [[STOM]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[MT1M]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCBLD2]] | -0.52 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[CAPN2]] | -0.49 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[HHIP]] | -0.47 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 4, C 15. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-DRB1]] | B | HLA-DRB1 activity raises SAA4's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.67× lower at baseline in the lines without HLA-DRB1 | 0.016 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[TOP2A]] | B | TOP2A activity lowers SAA4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DAPK2]] | B | DAPK2 activity raises SAA4's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 1.90× lower at baseline in the lines without DAPK2 | 0.091 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity raises SAA4's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.3% of all compounds | 0.099 | ⚠ off-target possible; 3 compounds |
| [[SAA1]] | C | SAA1 activity raises SAA4's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 2.75× lower at baseline in the lines without SAA1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11; co-absent with the target |
| [[TNFSF14]] | C | TNFSF14 activity raises SAA4's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 2.93× lower at baseline in the lines without TNFSF14 | 7e-04 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent; co-absent with the target |
| [[SAA2]] | C | SAA2 activity raises SAA4's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 2.78× lower at baseline in the lines without SAA2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3; co-absent with the target |
| [[C3]] | C | C3 activity raises SAA4's level | lines that do not express C3 (32) vs lines expressing it (18) | 2.80× lower at baseline in the lines without C3 | 0.004 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11; co-absent with the target |
| [[FGB]] | C | FGB activity raises SAA4's level | lines that do not express FGB (42) vs lines expressing it (8) | 2.46× lower at baseline in the lines without FGB | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2; co-absent with the target |
| [[FGA]] | C | FGA activity raises SAA4's level | lines that do not express FGA (43) vs lines expressing it (7) | 2.77× lower at baseline in the lines without FGA | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[MMP7]] | C | MMP7 activity raises SAA4's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.54× lower at baseline in the lines without MMP7 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP; co-absent with the target |
| [[CFB]] | C | CFB activity raises SAA4's level | lines that do not express CFB (20) vs lines expressing it (30) | 2.27× lower at baseline in the lines without CFB | 0.020 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG; co-absent with the target |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 16, C 14. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC3H12A]] | B | [[SAA2-SAA4]], SAA4 activity raises ZC3H12A's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.38× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.012 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[CEBPD]] | B | [[SAA2-SAA4]], SAA4 activity raises CEBPD's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.86× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.020 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[BATF]] | B | [[SAA2-SAA4]], SAA4 activity raises BATF's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.00× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.037 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[ZMYND8]] | B | [[SAA2-SAA4]], SAA4 activity raises ZMYND8's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.72× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.038 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[TRIM29]] | B | [[SAA2-SAA4]], SAA4 activity raises TRIM29's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.98× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.042 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[MUC1]] | B | SAA4 activity raises MUC1's level | lines that do not express SAA4 (22) vs lines expressing it (28) | 1.74× lower at baseline in the lines without SAA4 | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SAA2, SAA1, LMO2 |
| [[SERPINA3]] | B | [[SAA2-SAA4]], SAA4 activity raises SERPINA3's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.33× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.046 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[CCND3]] | B | [[SAA2-SAA4]], SAA4 activity raises CCND3's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.58× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.046 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[MAOA]] | B | [[SAA2-SAA4]], SAA4 activity raises MAOA's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.82× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.053 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[LCN2]] | B | [[SAA2-SAA4]], SAA4 activity raises LCN2's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.02× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.054 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[CARD14]] | B | [[SAA2-SAA4]], SAA4 activity raises CARD14's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.53× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.059 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[APOL1]] | B | [[SAA2-SAA4]], SAA4 activity raises APOL1's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.74× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.060 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.887). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.4, 16.0); signed map (16.8, 28.8). **Vector** length 80.0, 24.8% of its response variance represented; |z| ≥ 3 in 743 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.60 to 6); *interferon gamma response* (hallmark, mean cos +0.55 to 6); *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.58 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +10.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +7.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.4 | +5.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.0 | +4.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.9 | +4.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.9 | +4.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -3.8 | -3.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.3 | -3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | serum amyloid A4, constitutive |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:18,231,355-18,236,802 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C-SAA, CSAA |
| Matched by | ensembl_id |

**Function**, from UniProt [P35542](https://www.uniprot.org/uniprotkb/P35542) (Serum amyloid A-4 protein):

> Major acute phase reactant.

**Summary**, from NCBI Gene [6291](https://www.ncbi.nlm.nih.gov/gene/6291):

> Predicted to be involved in acute-phase response. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10516](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10516) · Entrez [6291](https://www.ncbi.nlm.nih.gov/gene/6291) · UniProt [P35542](https://www.uniprot.org/uniprotkb/P35542) · Ensembl [ENSG00000148965](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148965)

## Data

Gene col 7332: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7332); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7332, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7332]; `tensor/DDL_lfc|DDL_z.npy` [7332]; `embed/gene_vectors.npy` [7332]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7332 or target_col == 7332). Every well: [[SAA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
