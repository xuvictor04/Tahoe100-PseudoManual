---
symbol: "NR0B1"
type: "gene"
col: 9792
ensembl_id: "ENSG00000169297"
name: "nuclear receptor subfamily 0 group B member 1"
location: "Xp21.2"
module: 61
arm: "+"
pooled_cpm: 2.97
n_lines_expressing: 12
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# NR0B1

*nuclear receptor subfamily 0 group B member 1* — Xp21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.65× (z +10.5, q 4e-23, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.96× (z +8.5, q 3e-15, up in 10 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR158]] (+0.66, fdr 1e-05), [[TRIML2]] (+0.59, fdr 1e-05), [[PCSK2]] (+0.59, fdr 1e-05); moves opposite to [[NR2E3]] (-0.61, fdr 1e-05), [[THBD]] (-0.56, fdr 1e-05), [[GBA2]] (-0.50, fdr 4e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MSC]] → it (grade C ⚠); 4 go from it, the strongest it → [[MLKL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9792.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.65×** | +10.5 | 4e-23 | 1/6 (A549) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.93×** | +8.5 | 3e-15 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.96×** | +8.5 | 3e-15 | 10/10 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.80×** | +8.1 | 1e-13 | 2/5 (A549, NCI-H460) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.21×** | +6.2 | 5e-08 | 1/7 (NCI-H2030) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.05×** | +5.9 | 4e-07 | 8/9 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.69×** | +5.5 | 3e-06 | 2/7 (NCI-H2030, HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.67×** | +5.1 | 2e-05 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +4.7 | 2e-04 | 3/7 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +4.4 | 7e-04 | 3/9 (A549, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.48×** | +4.4 | 7e-04 | 2/5 (A549, A498) | top dose only | noisy plate (z scaled); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +4.2 | 0.001 | 3/9 (NCI-H2030, RPMI-7951, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.10×** | +4.1 | 0.002 | 8/10 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.16×** | +4.1 | 0.002 | 8/10 (A498, A549, …) | rises with dose | composition shift |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.99×** | +3.8 | 0.005 | 0/7 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.021 | 3/10 (NCI-H460, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +3.0 | 0.083 | 6/10 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +2.9 | 0.097 | 2/7 (A549, NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Silodosin (drug)]] 5 µM |  | **1.73×** | +2.9 | 0.097 | 1/8 (A498) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9792.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[9-ING-41 (drug)]] 5 µM |  | 0.324× | -3.3 | 0.36 | 0/10 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.536× | -3.2 | 0.36 | 0/10 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9792. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 15.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 19.3 | 3 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 7.62× (z +11.5) | — |
| [[A549 (line)]] | wt | 10.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.53× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.92× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 4.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +8.6) | — |
| [[A-172 (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.183 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.970 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.355 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.256 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.345 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.240 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.214 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.217 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.226 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.274 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.234 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9792), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR158]] | +0.66 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TRIML2]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[PCSK2]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[LINC02968]] | +0.58 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[CPEB2]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CPLX2]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[SLCO2B1]] | +0.53 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[ENTHD1]] | +0.52 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[ADAMTSL1]] | +0.52 | +0.48 / +0.39 | both halves | 6e-05 |  |
| [[SEMA3E]] | +0.52 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[KMO]] | +0.52 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[NR3C1]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 | pathway: Nuclear Receptor transcription pathway; STRING 414 |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2E3]] | -0.61 | -0.59 / -0.50 | both halves | 1e-05 | pathway: Nuclear Receptor transcription pathway |
| [[THBD]] | -0.56 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[GBA2]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[BCR]] | -0.49 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[MLKL]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[EPGN]] | -0.48 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[CAP1]] | -0.48 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[METTL9]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[MTMR12]] | -0.47 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[NAPG]] | -0.47 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[ZNF595]] | -0.46 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[TEX2]] | -0.46 | -0.48 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSC]] | C | MSC activity raises NR0B1's level | lines that do not express MSC (34) vs lines expressing it (16) | 2.21× lower at baseline in the lines without MSC | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLKL]] | B | NR0B1 activity raises MLKL's level | lines that do not express NR0B1 (38) vs lines expressing it (12) | 1.92× lower at baseline in the lines without NR0B1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, CDH19, TBXT |
| [[TBC1D8]] | B | NR0B1 activity raises TBC1D8's level | lines that do not express NR0B1 (38) vs lines expressing it (12) | 1.63× lower at baseline in the lines without NR0B1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, CDH19, TBXT |
| [[COL4A3]] | C | NR0B1 activity raises COL4A3's level | lines that do not express NR0B1 (38) vs lines expressing it (12) | 4.33× lower at baseline in the lines without NR0B1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, CDH19, TBXT; co-absent with the target |
| [[NRCAM]] | C | NR0B1 activity raises NRCAM's level | lines that do not express NR0B1 (38) vs lines expressing it (12) | 4.30× lower at baseline in the lines without NR0B1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, CDH19, TBXT; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.459). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.1, 19.9); signed map (40.6, 21.1). **Vector** length 33.8, 11.2% of its response variance represented; |z| ≥ 3 in 233 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.9 | +5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +1.7 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.6 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +1.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.7 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.6 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.6 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -0.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 0 group B member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp21.2 — chrX:30,304,206-30,309,390 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DAX1, AHCH; previously AHC, DSS |
| Gene groups (HGNC) | Nuclear receptor subfamily 0 group B |
| Reactome | 1 pathways, smallest: Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P51843](https://www.uniprot.org/uniprotkb/P51843) (Nuclear receptor subfamily 0 group B member 1):

> Nuclear receptor that lacks a DNA-binding domain and acts as a corepressor that inhibits the transcriptional activity of other nuclear receptors through heterodimeric interactions. Component of a cascade required for the development of the hypothalamic-pituitary-adrenal-gonadal axis. May also have a role in the development of the embryo and in the maintenance of embryonic stem cell pluripotency (By similarity).

**Summary**, from NCBI Gene [190](https://www.ncbi.nlm.nih.gov/gene/190):

> This gene encodes a protein that contains a DNA-binding domain. The encoded protein acts as a dominant-negative regulator of transcription which is mediated by the retinoic acid receptor. This protein also functions as an anti-testis gene by acting antagonistically to Sry. Mutations in this gene result in both X-linked congenital adrenal hypoplasia and hypogonadotropic hypogonadism. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7960) · Entrez [190](https://www.ncbi.nlm.nih.gov/gene/190) · UniProt [P51843](https://www.uniprot.org/uniprotkb/P51843) · Ensembl [ENSG00000169297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169297)

## Data

Gene col 9792: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9792); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9792, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9792]; `tensor/DDL_lfc|DDL_z.npy` [9792]; `embed/gene_vectors.npy` [9792]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9792 or target_col == 9792). Every well: [[NR0B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR0B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
