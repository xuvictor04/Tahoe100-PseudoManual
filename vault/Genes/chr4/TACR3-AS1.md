---
symbol: "TACR3-AS1"
type: "gene"
col: 14775
ensembl_id: "ENSG00000251577"
name: "TACR3 antisense RNA 1"
location: "4q24"
module: 75
arm: "+"
pooled_cpm: 3.37
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# TACR3-AS1

*TACR3 antisense RNA 1* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.46× (z +11.2, q 2e-26, up in 5 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +10.5, q 3e-23, up in 11 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.05 µM: 0.656× (z -3.8, q 0.079, down in 12 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (AsPC-1 0.136×, KATO III 0.0607×; ⚠ cell-cycle shift, explains ~63% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (LS 180 0.0734×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRSS48]] (+0.72, fdr 7e-06), [[MYO16]] (+0.68, fdr 1e-05), [[GRIA1]] (+0.67, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C4BPB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14775.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +11.2 | 2e-26 | 5/11 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.42×** | +10.7 | 3e-24 | 2/3 (LS 180, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +10.5 | 3e-23 | 11/26 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +6.9 | 1e-09 | 1/4 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +5.9 | 4e-07 | 8/25 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +4.8 | 1e-04 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +4.2 | 0.002 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +3.8 | 0.009 | 2/29 (NCI-H2030, RKO) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.009 | 2/19 (LS 180, NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.77×** | +3.7 | 0.014 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.6 | 0.017 | 4/21 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.026 | 0/27 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.3 | 0.046 | 0/2 | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.45×** | +3.2 | 0.063 | 0/20 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.071 | 6/40 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.076 | 3/24 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.094 | 3/27 (HepG2/C3A, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14775.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (AsPC-1 0.136×, KATO III 0.0607×; ⚠ cell-cycle shift, explains ~63% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (LS 180 0.0734×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.656×** | -3.8 | 0.079 | 12/38 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.05 µM |  | 0.670× | -3.4 | 0.18 | 0/39 | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.906× | -3.2 | 0.28 | 13/44 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.710× | -3.1 | 0.28 | 9/39 (HS-578T, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -10.2) ⚠ cell-cycle shift, explains ~63% of this change |
| [[KATO III (line)]] | alt | 3.98 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0607× (z -9.5) ⚠ cell-cycle shift, explains ~63% of this change |
| [[LS 180 (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0734× (z -12.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.904 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.920 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.986 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.948 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.898 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRSS48]] | +0.72 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MYO16]] | +0.68 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[GRIA1]] | +0.67 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[SLC44A5]] | +0.66 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[LINC02006]] | +0.66 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[SLC9C1]] | +0.66 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[FER1L6]] | +0.64 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[UBE2R2-AS1]] | +0.62 | +0.56 / +0.51 | both halves | 1e-05 | same gene group |
| [[DSG2-AS1]] | +0.62 | +0.48 / +0.56 | both halves | 2e-05 | same gene group |
| [[MEIOC]] | +0.62 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[EAF1-AS1]] | +0.61 | +0.49 / +0.59 | both halves | 1e-05 | same gene group |
| [[GUCY2C-AS1]] | +0.61 | +0.48 / +0.46 | both halves | 3e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C4BPB]] | B | C4BPB activity raises TACR3-AS1's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.34× lower at baseline in the lines without C4BPB | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.1, 29.9); signed map (31.4, 12.5). **Vector** length 37.2, 4.16% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +10.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.4 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.9 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.7 | -2.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.6 | -0.4 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -0.6 | -0.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | TACR3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q24 — chr4:103,548,745-103,624,534 (+) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-297P16.3 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55593) · Entrez [121233924](https://www.ncbi.nlm.nih.gov/gene/121233924) · Ensembl [ENSG00000251577](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251577)

## Data

Gene col 14775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14775); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14775]; `tensor/DDL_lfc|DDL_z.npy` [14775]; `embed/gene_vectors.npy` [14775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14775 or target_col == 14775). Every well: [[TACR3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TACR3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
