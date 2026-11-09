---
symbol: "PPP1R36"
type: "gene"
col: 9191
ensembl_id: "ENSG00000165807"
name: "protein phosphatase 1 regulatory subunit 36"
location: "14q23.3"
module: 53
arm: "+"
pooled_cpm: 2.69
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# PPP1R36

*protein phosphatase 1 regulatory subunit 36* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 10.0× (z +18.8, q 0e+00, up in 30 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0603×); [[Valdecoxib (drug)]] 0.5 µM in 1 line (A498 0.0537×); [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0675×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP210L]] (+0.83, fdr 7e-06), [[LDHC]] (+0.82, fdr 7e-06), [[TRIM72]] (+0.82, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9191.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **10.0×** | +18.8 | 0e+00 | 30/36 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.06×** | +18.6 | 0e+00 | 32/35 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.83×** | +11.9 | 1e-30 | 22/35 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.10×** | +9.2 | 5e-18 | 8/14 (CFPAC-1, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.14×** | +8.7 | 3e-16 | 16/43 (SW480, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.96×** | +8.1 | 4e-14 | 1/5 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +8.0 | 7e-14 | 1/3 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +8.0 | 8e-14 | 14/29 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.57×** | +7.6 | 1e-12 | 27/44 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +7.1 | 1e-10 | 16/34 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.08×** | +6.0 | 1e-07 | 20/44 (A549, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +5.6 | 1e-06 | 18/40 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +5.5 | 2e-06 | 12/36 (SW480, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **3.36×** | +5.1 | 1e-05 | 10/23 (SW480, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +4.9 | 4e-05 | 11/33 (A498, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +4.6 | 1e-04 | 7/42 (NCI-H2030, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +4.3 | 5e-04 | 9/42 (SW480, A498, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.74×** | +4.2 | 7e-04 | 9/39 (A549, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9191.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0603×); [[Valdecoxib (drug)]] 0.5 µM in 1 line (A498 0.0537×); [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0675×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.670× | -3.3 | 0.44 | 9/38 (PANC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[LB-100 (drug)]] 0.05 µM |  | 0.679× | -3.0 | 0.44 | 3/42 (NCI-H2347, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.77 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +10.9) | [[Valdecoxib (drug)]] 0.5 µM 0.0537× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 5.99 | 3 | 0 | [[Auranofin (drug)]] 5 µM 37.5× (z +10.7) | — |
| [[SW480 (line)]] | alt | 2.06 | 3 | 0 | [[Auranofin (drug)]] 5 µM 29.9× (z +10.4) | — |
| [[A549 (line)]] | wt | 2.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.7× (z +10.9) | — |
| [[C32 (line)]] | wt | 4.38 | 1 | 0 | [[Auranofin (drug)]] 5 µM 54.8× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 2.76 | 1 | 0 | [[Auranofin (drug)]] 5 µM 20.0× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 2.28 | 1 | 0 | [[Auranofin (drug)]] 5 µM 35.6× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 3.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 6.18 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM 0.0675× (z -9.0) |
| [[PANC-1 (line)]] | alt | 1.95 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0603× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 5.12 | 0 | 1 | — | [[Methyl aminolevulinate (hydrochloride) (drug)]] 5 µM 0.0444× (z -8.5) |
| [[A-172 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.797 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.743 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.699 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.648 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP210L]] | +0.83 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[LDHC]] | +0.82 | +0.76 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[TRIM72]] | +0.82 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.82 | +0.76 / +0.80 | both halves | 7e-06 |  |
| [[USP50]] | +0.78 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.78 | +0.64 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[GRAMD2A]] | +0.78 | +0.74 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[PLA2G12B]] | +0.77 | +0.61 / +0.80 | both halves | 7e-06 |  |
| [[DPYS]] | +0.77 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.77 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.76 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.76 | +0.75 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PPP1R36's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PTPN6]] | B | PTPN6 activity raises PPP1R36's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.54× lower at baseline in the lines without PTPN6 | 0.048 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[C9]] | B | C9 activity raises PPP1R36's level | lines that do not express C9 (21) vs lines expressing it (29) | 1.47× lower at baseline in the lines without C9 | 0.059 | ⚠ within organs, on part of the lines; also absent: DAB2, ENSG00000253891, PTGFR |
| [[NPHS1]] | C | NPHS1 activity strengthens PPP1R36's drug response | lines that do not express NPHS1 (4) vs lines expressing it (41) | the lines without NPHS1 respond 0.17× as strongly (z diff +2.21); strongest at Idarubicin (hydrochloride) 5 µM: 1.41x vs 5.67x (z diff +4.7) | 0.037 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.846). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.5, -15.9); signed map (16.6, 11.0). **Vector** length 63.8, 9.86% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.0 | +18.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +18.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +11.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +8.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +8.7 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:64,549,920-64,589,381 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf50 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LQ0](https://www.uniprot.org/uniprotkb/Q96LQ0) (Protein phosphatase 1 regulatory subunit 36):

> Inhibits phosphatase activity of protein phosphatase 1 (PP1) complexes.

**Summary**, from NCBI Gene [145376](https://www.ncbi.nlm.nih.gov/gene/145376):

> Predicted to enable phosphatase binding activity and protein phosphatase inhibitor activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20097) · Entrez [145376](https://www.ncbi.nlm.nih.gov/gene/145376) · UniProt [Q96LQ0](https://www.uniprot.org/uniprotkb/Q96LQ0) · Ensembl [ENSG00000165807](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165807)

## Data

Gene col 9191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9191); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9191]; `tensor/DDL_lfc|DDL_z.npy` [9191]; `embed/gene_vectors.npy` [9191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9191 or target_col == 9191). Every well: [[PPP1R36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
