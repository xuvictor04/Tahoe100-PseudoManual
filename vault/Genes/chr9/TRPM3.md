---
symbol: "TRPM3"
type: "gene"
col: 1359
ensembl_id: "ENSG00000083067"
name: "transient receptor potential cation channel subfamily M member 3"
location: "9q21.12-q21.13"
module: 75
arm: "+"
pooled_cpm: 8.33
n_lines_expressing: 48
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# TRPM3

*transient receptor potential cation channel subfamily M member 3* — 9q21.12-q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.78× (z +27.2, q 0e+00, up in 34 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0871×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.163×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02755]] (+0.73, fdr 7e-06), [[LINC00607]] (+0.68, fdr 7e-06), [[GRM8]] (+0.67, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FGF13]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1359.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.78×** | +27.2 | 0e+00 | 34/35 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.43×** | +23.1 | 0e+00 | 32/38 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.27×** | +13.0 | 2e-36 | 36/42 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.02×** | +12.1 | 9e-32 | 18/24 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.94×** | +11.8 | 3e-30 | 30/40 (HOP62, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.05×** | +11.8 | 6e-30 | 4/10 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.06×** | +11.2 | 4e-27 | 28/45 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.85×** | +10.6 | 2e-24 | 4/13 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +8.5 | 2e-15 | 20/36 (LOX-IMVI, KATO III, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.71×** | +8.3 | 5e-15 | 20/44 (SHP-77, NCI-H2030, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +7.7 | 8e-13 | 17/36 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +6.3 | 2e-08 | 14/36 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.55×** | +4.8 | 8e-05 | 16/42 (A498, SK-MEL-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +4.3 | 7e-04 | 11/42 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.002 | 10/41 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.005 | 11/41 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.005 | 7/43 (SK-MEL-2, A-172, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.007 | 10/44 (A498, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1359.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0871×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.163×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -3.2 | 0.45 | 4/46 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.823× | -3.1 | 0.45 | 10/44 (H4, SW480, …) | top dose only | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.759× | -3.0 | 0.45 | 8/44 (SW1417, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1359. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 3.60 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +11.0) | — |
| [[LoVo (line)]] | wt | 3.61 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.9× (z +19.8) | — |
| [[HS-578T (line)]] | alt | 3.59 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.8× (z +13.2) | — |
| [[J82 (line)]] | alt | 3.29 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +11.9) | — |
| [[LOX-IMVI (line)]] | wt | 3.61 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 4.48 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 34.0× (z +17.2) | — |
| [[SHP-77 (line)]] | alt | 47.8 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.24× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 2.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.5× (z +12.6) | — |
| [[A549 (line)]] | wt | 2.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 2.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.0× (z +9.3) | — |
| [[C32 (line)]] | wt | 111 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 5.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 4.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.32× (z +12.4) | — |
| [[HepG2_C3A (line)]] | wt | 3.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.2× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 4.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +11.0) | — |
| [[KATO III (line)]] | alt | 3.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 2.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.0× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 32.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0871× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 2.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 2.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 5.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +9.0) | — |
| [[A-172 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1359), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02755]] | +0.73 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[LINC00607]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[GRM8]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 | same gene group |
| [[PCDH15]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 | same gene group |
| [[EYS]] | +0.67 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[HPSE2]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 | same gene group |
| [[LINC00534]] | +0.65 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[LINC02398]] | +0.65 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[LINC00861]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[AQP4-AS1]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[DRAIC]] | +0.63 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[PDE8B]] | +0.63 | +0.57 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF13]] | B | FGF13 activity raises TRPM3's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 2.17× lower at baseline in the lines without FGF13 | 0.032 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11 |
| [[TOP2A]] | B | TOP2A activity lowers TRPM3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SOX6]] | B | SOX6 activity raises TRPM3's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without SOX6 | 0.058 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[NRCAM]] | B | NRCAM activity raises TRPM3's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 1.68× lower at baseline in the lines without NRCAM | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG |
| [[SLCO5A1]] | C | SLCO5A1's natural level weakens TRPM3's drug response | SLCO5A1's natural level across 40 lines (lineage-adjusted; a glimpse) | r -0.69, reverse -0.62; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.2, 25.2); signed map (35.6, 11.6). **Vector** length 77.5, 13.6% of its response variance represented; |z| ≥ 3 in 1,100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.6 | +27.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +23.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +8.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -0.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -2.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.6 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.0 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | transient receptor potential cation channel subfamily M member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.12-q21.13 — chr9:70,529,060-71,446,977 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1616, LTRPC3, GON-2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Transient receptor potential cation channel subfamily M |
| Reactome | 4 pathways, smallest: TRP channels; Stimuli-sensing channels; Ion channel transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCF6](https://www.uniprot.org/uniprotkb/Q9HCF6) (Transient receptor potential cation channel subfamily M member 3):

> Constitutively active, non-selective divalent cation-conducting channel that is permeable to Ca(2+), Mn(2+), and Mg(2+), with a high permeability for Ca(2+). However, can be enhanced by increasing temperature and by ligands, including the endogenous neurosteroid pregnenolone sulfate and sphingosine-1 and suppressed by intracellular Mg(2+). Implicated in a variety of cellular processes, including insulin/peptide secretion, vascular constriction and dilation, noxious heat sensing, inflammatory …

**Summary**, from NCBI Gene [80036](https://www.ncbi.nlm.nih.gov/gene/80036):

> The product of this gene belongs to the family of transient receptor potential (TRP) channels. TRP channels are cation-selective channels important for cellular calcium signaling and homeostasis. The protein encoded by this gene mediates calcium entry, and this entry is potentiated by calcium store depletion. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17992) · Entrez [80036](https://www.ncbi.nlm.nih.gov/gene/80036) · UniProt [Q9HCF6](https://www.uniprot.org/uniprotkb/Q9HCF6) · Ensembl [ENSG00000083067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083067)

## Data

Gene col 1359: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1359); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1359, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1359]; `tensor/DDL_lfc|DDL_z.npy` [1359]; `embed/gene_vectors.npy` [1359]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1359 or target_col == 1359). Every well: [[TRPM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
