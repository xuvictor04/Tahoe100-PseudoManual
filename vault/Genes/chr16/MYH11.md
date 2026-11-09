---
symbol: "MYH11"
type: "gene"
col: 5443
ensembl_id: "ENSG00000133392"
name: "myosin heavy chain 11"
location: "16p13.11"
module: 21
arm: "+"
pooled_cpm: 3.49
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# MYH11

*myosin heavy chain 11* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.68× (z +16.8, q 0e+00, up in 31 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.101×); [[Tetracycline (hydrochloride) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0562×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0713×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HRG-AS1]] (+0.77, fdr 7e-06), [[PKD2L2]] (+0.76, fdr 7e-06), [[SPATA21]] (+0.76, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.68×** | +16.8 | 0e+00 | 31/35 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.56×** | +14.7 | 0e+00 | 5/5 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.13×** | +13.8 | 8e-41 | 20/21 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +11.0 | 7e-26 | 3/8 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +6.7 | 3e-09 | 13/35 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.4 | 1e-08 | 13/46 (PANC-1, LOX-IMVI, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +6.0 | 2e-07 | 19/44 (HEC-1-A, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.9 | 2e-07 | 10/35 (LOX-IMVI, HS-578T, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.9 | 2e-07 | 9/32 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +5.0 | 3e-05 | 6/22 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.3 | 7e-04 | 3/20 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.8 | 0.007 | 1/8 (A498) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.012 | 8/44 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.034 | 6/46 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.44×** | +3.1 | 0.064 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5443.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.101×); [[Tetracycline (hydrochloride) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0562×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0713×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Afatinib (drug)]] 5 µM |  | 0.780× | -3.1 | 0.41 | 6/44 (AsPC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.59× (z +10.8) | — |
| [[A549 (line)]] | wt | 3.56 | 0 | 1 | — | [[Thymopentin (drug)]] 5 µM 0.0728× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 3.44 | 0 | 1 | — | [[Tetracycline (hydrochloride) (drug)]] 0.05 µM 0.0562× (z -10.3) |
| [[HOP62 (line)]] | alt | 2.99 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0936× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 3.07 | 0 | 1 | — | [[Pyridoxine (drug)]] 5 µM 0.101× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 4.08 | 0 | 1 | — | [[Mebendazole (drug)]] 0.05 µM 0.0808× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 2.47 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0713× (z -9.1) |
| [[PANC-1 (line)]] | alt | 3.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +10.5) | — |
| [[A-172 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HRG-AS1]] | +0.77 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.76 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.76 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[TOMM20L-DT]] | +0.76 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[ABHD15-AS1]] | +0.74 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.74 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[C12orf40]] | +0.74 | +0.58 / +0.75 | both halves | 8e-06 |  |
| [[PP2D1]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[SPAG5-AS1]] | +0.73 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.71 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[SEC1P]] | +0.71 | +0.60 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYH11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, 26.2); signed map (32.0, 4.9). **Vector** length 45.7, 4.78% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +16.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +11.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -0.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.1 | +0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | myosin heavy chain 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.11 — chr16:15,703,135-15,858,438 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMMHC, SMHC, SMMS-1 |
| Gene groups (HGNC) | Myosin heavy chains, class II |
| Hallmark sets | MYOGENESIS |
| Reactome | 16 pathways, smallest: RHO GTPases Activate ROCKs; RHO GTPases activate CIT; Sema4D induced cell migration and growth-cone collapse |
| Matched by | ensembl_id |

**Function**, from UniProt [P35749](https://www.uniprot.org/uniprotkb/P35749) (Myosin-11):

> Muscle contraction.

**Summary**, from NCBI Gene [4629](https://www.ncbi.nlm.nih.gov/gene/4629):

> The protein encoded by this gene is a smooth muscle myosin belonging to the myosin heavy chain family. The gene product is a subunit of a hexameric protein that consists of two heavy chain subunits and two pairs of non-identical light chain subunits. It functions as a major contractile protein, converting chemical energy into mechanical energy through the hydrolysis of ATP. A chromosomal rearrangement involving this gene is associated with acute myeloid leukemia of the M4Eo subtype. Mutations …

**Accessions** — [HGNC:7569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7569) · Entrez [4629](https://www.ncbi.nlm.nih.gov/gene/4629) · UniProt [P35749](https://www.uniprot.org/uniprotkb/P35749) · Ensembl [ENSG00000133392](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133392)

## Data

Gene col 5443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5443); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5443]; `tensor/DDL_lfc|DDL_z.npy` [5443]; `embed/gene_vectors.npy` [5443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5443 or target_col == 5443). Every well: [[MYH11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYH11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
