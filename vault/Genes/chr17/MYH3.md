---
symbol: "MYH3"
type: "gene"
col: 3020
ensembl_id: "ENSG00000109063"
name: "myosin heavy chain 3"
location: "17p13.1"
module: 47
arm: "+"
pooled_cpm: 3.13
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# MYH3

*myosin heavy chain 3* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.05× (z +13.4, q 4e-38, up in 32 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.636× (z -3.9, q 0.039, down in 18 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0887×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H23 0.0790×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LoVo 0.0889×; ⚠ toxic; cell-cycle shift, explains ~4% of this change); [[Cytarabine (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0733×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAAT]] (+0.77, fdr 7e-06), [[IDI2-AS1]] (+0.74, fdr 7e-06), [[QRICH2]] (+0.74, fdr 7e-06); moves opposite to [[ALAD]] (-0.67, fdr 2e-05), [[CAT]] (-0.65, fdr 1e-05), [[TMEM14A]] (-0.64, fdr 5e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3020.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +13.4 | 4e-38 | 32/34 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +7.3 | 1e-10 | 1/1 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +6.6 | 1e-08 | 7/14 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.5 | 1e-08 | 19/44 (PANC-1, BT-474, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +5.8 | 6e-07 | 12/29 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +5.6 | 2e-06 | 2/5 (PANC-1, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +5.2 | 1e-05 | 15/38 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.0 | 3e-05 | 6/14 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.73×** | +4.6 | 2e-04 | 17/46 (KATO III, A549, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.1 | 0.002 | 10/34 (RPMI-7951, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.0 | 0.003 | 5/47 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.005 | 11/46 (SW480, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.010 | 7/45 (A549, COLO 205, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.029 | 7/41 (SHP-77, NCI-H23, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.044 | 5/46 (H4, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.054 | 13/35 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.45×** | +3.0 | 0.089 | 2/41 (A549, A-427) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.089 | 2/27 (SHP-77, KATO III) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3020.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0887×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H23 0.0790×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LoVo 0.0889×; ⚠ toxic; cell-cycle shift, explains ~4% of this change); [[Cytarabine (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0733×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.636×** | -3.9 | 0.039 | 18/46 (RPMI-7951, BT-474, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.640×** | -3.8 | 0.039 | 14/27 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Artesunate (drug)]] 5 µM |  | 0.760× | -3.3 | 0.17 | 5/45 (Panc 03.27, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.685× | -3.2 | 0.17 | 9/45 (Hs 766T, AN3 CA, …) | rises with dose | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | 0.696× | -3.1 | 0.22 | 7/45 (HepG2/C3A, SNU-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3020. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 4.95 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0889× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~4% of this change |
| [[A-427 (line)]] | wt | 4.07 | 0 | 1 | — | [[Cytarabine (hydrochloride) (drug)]] 5 µM 0.0733× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 5.82 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0887× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 8.75 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0790× (z -10.4) |
| [[A-172 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3020), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAAT]] | +0.77 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.74 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[QRICH2]] | +0.74 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[ZDHHC11]] | +0.74 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.74 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | +0.74 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[PPIEL-1]] | +0.73 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[MASP2]] | +0.73 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[PLAC8L1]] | +0.72 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[EFCAB8]] | +0.72 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[CHADL]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.71 | +0.74 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAD]] | -0.67 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CAT]] | -0.65 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[TMEM14A]] | -0.64 | -0.54 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYH3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00334]] | B | LINC00334 activity raises MYH3's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.63× lower at baseline in the lines without LINC00334 | 0.037 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[SCUBE2]] | B | SCUBE2 activity raises MYH3's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without SCUBE2 | 0.051 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[ASGR1]] | B | ASGR1 activity raises MYH3's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without ASGR1 | 0.058 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[C11orf91]] | B | C11orf91 activity lowers MYH3's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.62× higher at baseline in the lines without C11orf91 | 0.062 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[LINC01250]] | B | LINC01250 activity raises MYH3's level | lines that do not express LINC01250 (10) vs lines expressing it (40) | 1.60× lower at baseline in the lines without LINC01250 | 0.085 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SH2D4B]] | C | SH2D4B activity lowers MYH3's level | lines that do not express SH2D4B (3) vs lines expressing it (47) | 1.41× higher at baseline in the lines without SH2D4B | 0.074 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000249951, ARHGAP15, B4GALT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.9, -13.6); signed map (15.9, 3.5). **Vector** length 53.0, 6.73% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +2.2 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | +1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | myosin heavy chain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:10,628,526-10,657,309 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MYHC-EMB, MYHSE1, HEMHC, SMHCE |
| Gene groups (HGNC) | Myosin heavy chains, class II |
| Hallmark sets | MYOGENESIS |
| Reactome | 2 pathways, smallest: Striated Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P11055](https://www.uniprot.org/uniprotkb/P11055) (Myosin-3):

> Muscle contraction.

**Summary**, from NCBI Gene [4621](https://www.ncbi.nlm.nih.gov/gene/4621):

> Myosin is a major contractile protein which converts chemical energy into mechanical energy through the hydrolysis of ATP. Myosin is a hexameric protein composed of a pair of myosin heavy chains (MYH) and two pairs of nonidentical light chains. This gene is a member of the MYH family and encodes a protein with an IQ domain and a myosin head-like domain. Mutations in this gene have been associated with two congenital contracture (arthrogryposis) syndromes, Freeman-Sheldon syndrome and …

**Accessions** — [HGNC:7573](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7573) · Entrez [4621](https://www.ncbi.nlm.nih.gov/gene/4621) · UniProt [P11055](https://www.uniprot.org/uniprotkb/P11055) · Ensembl [ENSG00000109063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109063)

## Data

Gene col 3020: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3020); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3020, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3020]; `tensor/DDL_lfc|DDL_z.npy` [3020]; `embed/gene_vectors.npy` [3020]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3020 or target_col == 3020). Every well: [[MYH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
