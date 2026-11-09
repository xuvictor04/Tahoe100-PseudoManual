---
symbol: "CELF4"
type: "gene"
col: 2148
ensembl_id: "ENSG00000101489"
name: "CUGBP Elav-like family member 4"
location: "18q12.2"
module: 61
arm: "+"
pooled_cpm: 4.71
n_lines_expressing: 26
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# CELF4

*CUGBP Elav-like family member 4* — 18q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.21× (z +13.9, q 3e-41, up in 9 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.219×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0465×; ⚠ cell-cycle shift, explains ~32% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGCZ]] (+0.66, fdr 7e-06), [[DACH2]] (+0.65, fdr 7e-06), [[RUNDC3B]] (+0.63, fdr 7e-06).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ELAVL2]] → it (grade C ⚠); 3 go from it, the strongest it → [[GPR63]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2148.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.21×** | +13.9 | 3e-41 | 9/15 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.57×** | +10.7 | 2e-24 | 4/7 (SW480, SW 900, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +8.5 | 4e-15 | 0/2 | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +8.1 | 1e-13 | 7/14 (BT-474, SHP-77, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.74×** | +7.8 | 5e-13 | 0/2 | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +7.6 | 2e-12 | 14/19 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +6.7 | 1e-09 | 14/20 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +6.5 | 5e-09 | 14/21 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +5.8 | 5e-07 | 5/9 (SW480, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +5.4 | 4e-06 | 10/18 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +4.5 | 4e-04 | 8/15 (NCI-H2347, A-427, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.3 | 7e-04 | 4/15 (LOX-IMVI, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +4.1 | 0.002 | 12/19 (NCI-H2347, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.94×** | +4.0 | 0.003 | 1/8 (A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +3.9 | 0.004 | 3/12 (NCI-H2347, SHP-77, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.013 | 2/20 (SNU-1, NCI-H2347) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.51×** | +3.4 | 0.018 | 2/19 (A-427, NCI-H2347) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.023 | 3/13 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.033 | 1/14 (SHP-77) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.70×** | +3.2 | 0.036 | 1/13 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2148.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.219×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0465×; ⚠ cell-cycle shift, explains ~32% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 0.684× | -3.1 | 0.83 | 3/17 (LOX-IMVI, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -11.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0465× (z -11.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 0.966 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.695 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.978 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.934 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.887 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.952 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.803 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGCZ]] | +0.66 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[DACH2]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[RUNDC3B]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[UNC80]] | +0.62 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[PKNOX2]] | +0.62 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[SNAP91]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[SORCS1]] | +0.61 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[XKR4]] | +0.60 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[KCNH7]] | +0.60 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[APBA1]] | +0.60 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[NEURL1]] | +0.59 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[CHST8]] | +0.59 | +0.51 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELAVL2]] | C | ELAVL2 activity raises CELF4's level | lines that do not express ELAVL2 (34) vs lines expressing it (16) | 2.00× lower at baseline in the lines without ELAVL2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283982, MIR99AHG, DPP10; co-absent with the target |
| [[NAA11]] | C | NAA11 activity raises CELF4's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 1.82× lower at baseline in the lines without NAA11 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR63]] | B | CELF4 activity raises GPR63's level | lines that do not express CELF4 (24) vs lines expressing it (26) | 2.04× lower at baseline in the lines without CELF4 | 0.076 | ⚠ within organs, on part of the lines; also absent: CHST8, ASXL3, SULT4A1; maybe low, not absent |
| [[ROR2]] | C | CELF4 activity raises ROR2's level | lines that do not express CELF4 (24) vs lines expressing it (26) | 1.97× lower at baseline in the lines without CELF4 | 0.071 | ⚠ within organs, on part of the lines; also absent: CHST8, ASXL3, SULT4A1; maybe low, not absent; co-absent with the target |
| [[NOL4]] | C | CELF4 activity raises NOL4's level | lines that do not express CELF4 (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without CELF4 | 0.073 | ⚠ within organs, on part of the lines; also absent: CHST8, ASXL3, SULT4A1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.724). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.2, 31.9); signed map (31.6, 20.3). **Vector** length 24.8, 3.59% of its response variance represented; |z| ≥ 3 in 391 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +13.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +4.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -1.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | CUGBP Elav-like family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.2 — chr18:37,243,040-37,565,827 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously BRUNOL4 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZC1](https://www.uniprot.org/uniprotkb/Q9BZC1) (CUGBP Elav-like family member 4):

> RNA-binding protein implicated in the regulation of pre-mRNA alternative splicing. Mediates exon inclusion and/or exclusion in pre-mRNA that are subject to tissue-specific and developmentally regulated alternative splicing. Specifically activates exon 5 inclusion of cardiac isoforms of TNNT2 during heart remodeling at the juvenile to adult transition. Promotes exclusion of both the smooth muscle (SM) and non-muscle (NM) exons in actinin pre-mRNAs. Activates the splicing of MAPT/Tau exon 10. …

**Summary**, from NCBI Gene [56853](https://www.ncbi.nlm.nih.gov/gene/56853):

> Members of the CELF/BRUNOL protein family contain two N-terminal RNA recognition motif (RRM) domains, one C-terminal RRM domain, and a divergent segment of 160-230 aa between the second and third RRM domains. Members of this protein family regulate pre-mRNA alternative splicing and may also be involved in mRNA editing, and translation. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14015](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14015) · Entrez [56853](https://www.ncbi.nlm.nih.gov/gene/56853) · UniProt [Q9BZC1](https://www.uniprot.org/uniprotkb/Q9BZC1) · Ensembl [ENSG00000101489](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101489)

## Data

Gene col 2148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2148); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2148]; `tensor/DDL_lfc|DDL_z.npy` [2148]; `embed/gene_vectors.npy` [2148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2148 or target_col == 2148). Every well: [[CELF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CELF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
