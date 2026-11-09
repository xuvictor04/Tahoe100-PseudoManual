---
symbol: "GDPD4"
type: "gene"
col: 10961
ensembl_id: "ENSG00000178795"
name: "glycerophosphodiester phosphodiesterase domain containing 4"
location: "11q13.5"
module: 21
arm: "+"
pooled_cpm: 2.93
n_lines_expressing: 18
n_dd_up: 37
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# GDPD4

*glycerophosphodiester phosphodiesterase domain containing 4* — 11q13.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 12.1× (z +17.1, q 0e+00, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.01× (z +16.3, q 0e+00, up in 6 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.260×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.148×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.190×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFL1P1-1]] (+0.59, fdr 2e-05), [[KLKP1-1]] (+0.59, fdr 1e-05), [[MYO18B]] (+0.57, fdr 2e-05); moves opposite to [[VWA1]] (-0.42, fdr 2e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[NIT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10961.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **12.1×** | +17.1 | 0e+00 | 2/4 (CFPAC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.01×** | +16.3 | 0e+00 | 6/11 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **9.40×** | +16.0 | 0e+00 | 3/6 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.02×** | +11.4 | 5e-28 | 3/5 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.52×** | +9.3 | 1e-18 | 3/11 (SW 900, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.46×** | +8.9 | 8e-17 | 4/13 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.87×** | +7.5 | 5e-12 | 8/14 (LoVo, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.28×** | +5.9 | 3e-07 | 5/13 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +5.9 | 3e-07 | 2/8 (SHP-77, NCI-H2347) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.34×** | +5.8 | 3e-07 | 2/7 (SW 900, NCI-H2347) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.20×** | +5.6 | 9e-07 | 8/15 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.70×** | +4.9 | 5e-05 | 2/3 (CFPAC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.54×** | +4.7 | 1e-04 | 1/3 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +4.7 | 1e-04 | 1/7 (SW 900) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +4.6 | 2e-04 | 4/6 (SW 900, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.75×** | +4.0 | 0.002 | 1/9 (CFPAC-1) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.003 | 0/14 | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +3.8 | 0.005 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.006 | 4/13 (CFPAC-1, C32, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.66×** | +3.6 | 0.008 | 1/14 (LoVo) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.98×** | +3.5 | 0.013 | 4/14 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.023 | 1/13 (LOX-IMVI) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.023 | 3/10 (SW 900, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.67×** | +3.3 | 0.024 | 1/7 (SW 900) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10961.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.260×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.148×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.190×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.630× | -3.2 | 0.80 | 3/14 (SW 900, NCI-H2347, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10961. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 92.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -14.1) |
| [[SW 900 (line)]] | alt | 6.98 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 65.2× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.496 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.901 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.716 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.824 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.602 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.648 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.808 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.808 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.745 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.518 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.485 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.542 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10961), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL1P1-1]] | +0.59 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[KLKP1-1]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[MYO18B]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[TRD-AS1]] | +0.55 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[ABCC11]] | +0.54 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[KIAA2012]] | +0.54 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[SLC16A13]] | +0.54 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[PKD2L2]] | +0.53 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[CACNG2]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[SUMO2P17]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[PDE8B]] | +0.52 | +0.37 / +0.48 | both halves | 7e-05 |  |
| [[ZNF236-DT]] | +0.52 | +0.43 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VWA1]] | -0.42 | -0.47 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIT2]] | B | GDPD4 activity lowers NIT2's level | lines that do not express GDPD4 (32) vs lines expressing it (18) | 1.30× higher at baseline in the lines without GDPD4 | 0.085 | ⚠ within organs, on part of the lines; also absent: STEAP4, ENSG00000275016, DDX43; maybe low, not absent |
| [[SLC7A11-AS1]] | B | GDPD4 activity raises SLC7A11-AS1's level | lines that do not express GDPD4 (32) vs lines expressing it (18) | 1.70× lower at baseline in the lines without GDPD4 | 0.092 | ⚠ within organs, on part of the lines; also absent: STEAP4, ENSG00000275016, DDX43; maybe low, not absent |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.400). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.8, 32.0); signed map (37.8, 7.1). **Vector** length 22.8, 4.15% of its response variance represented; |z| ≥ 3 in 292 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +17.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +16.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +16.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.8 | +5.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.7 | +1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.6 | +3.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | +1.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.7 | +0.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.5 | -1.8 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -0.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | glycerophosphodiester phosphodiesterase domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.5 — chr11:77,216,558-77,301,687 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GDE6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6W3E5](https://www.uniprot.org/uniprotkb/Q6W3E5) (Glycerophosphodiester phosphodiesterase 6):

> Ecto-phospholipase that cleaves the phosphodiester bond in the glycosylphosphatidylinositol (GPI) anchor of TRABD2A and TRABD2B, releasing them from the plasma membrane. The release in the extracellular space inactivates these metalloproteases involved in the negative regulation of Wnt signaling.

**Summary**, from NCBI Gene [220032](https://www.ncbi.nlm.nih.gov/gene/220032):

> Predicted to enable glycerophosphodiester phosphodiesterase activity. Predicted to be involved in lipid metabolic process. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24849](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24849) · Entrez [220032](https://www.ncbi.nlm.nih.gov/gene/220032) · UniProt [Q6W3E5](https://www.uniprot.org/uniprotkb/Q6W3E5) · Ensembl [ENSG00000178795](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178795)

## Data

Gene col 10961: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10961); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10961, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10961]; `tensor/DDL_lfc|DDL_z.npy` [10961]; `embed/gene_vectors.npy` [10961]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10961 or target_col == 10961). Every well: [[GDPD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDPD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
