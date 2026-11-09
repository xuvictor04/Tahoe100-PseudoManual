---
symbol: "PLA2G12B"
type: "gene"
col: 6150
ensembl_id: "ENSG00000138308"
name: "phospholipase A2 group XIIB"
location: "10q22.1"
module: 53
arm: "+"
pooled_cpm: 2.27
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# PLA2G12B

*phospholipase A2 group XIIB* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.31× (z +16.2, q 0e+00, up in 31 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Irinotecan (hydrochloride) (drug)]] 0.5 µM: 0.509× (z -4.2, q 0.013, down in 17 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Dimethyl fumarate (drug)]] 0.05 µM in 1 line (NCI-H460 0.0481×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAH10]] (+0.78, fdr 7e-06), [[PPP1R36]] (+0.77, fdr 7e-06), [[LINC02646]] (+0.77, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6150.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.31×** | +16.2 | 0e+00 | 31/31 (CFPAC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **7.13×** | +12.2 | 6e-32 | 35/40 (SW480, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.43×** | +10.8 | 4e-25 | 24/34 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.06×** | +6.7 | 3e-09 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.00×** | +6.1 | 1e-07 | 17/44 (HEC-1-A, hTERT-HPNE, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +5.1 | 3e-05 | 16/31 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +5.0 | 4e-05 | 10/18 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.71×** | +4.7 | 2e-04 | 6/43 (HEC-1-A, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +4.7 | 2e-04 | 2/12 (HepG2/C3A, HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.20×** | +4.6 | 2e-04 | 13/40 (HepG2/C3A, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +4.1 | 0.002 | 6/34 (MIA PaCa-2, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.86×** | +3.6 | 0.018 | 5/18 (KATO III, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.76×** | +3.5 | 0.019 | 14/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.75×** | +3.5 | 0.021 | 14/47 (HepG2/C3A, SW48, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +3.4 | 0.026 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.78×** | +3.3 | 0.033 | 3/17 (NCI-H2347, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +3.1 | 0.058 | 2/25 (NCI-H460, LOX-IMVI) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6150.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Dimethyl fumarate (drug)]] 0.05 µM in 1 line (NCI-H460 0.0481×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.509×** | -4.2 | 0.013 | 17/45 (CFPAC-1, SNU-1, …) | two highest doses | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 0.678× | -3.5 | 0.15 | 18/41 (hTERT-HPNE, C32, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.605× | -3.2 | 0.27 | 12/45 (A-427, NCI-H460, …) | top dose only | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 0.713× | -3.0 | 0.27 | 11/45 (PANC-1, CFPAC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6150. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.72 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.80× (z +8.8) | [[Dimethyl fumarate (drug)]] 0.05 µM 0.0481× (z -8.5) |
| [[A-172 (line)]] | wt | 1.63 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.2× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 2.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.65× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 1.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +9.0) | — |
| [[LoVo (line)]] | wt | 1.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.9× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 3.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.67× (z +8.5) | — |
| [[SW480 (line)]] | alt | 1.24 | 1 | 0 | [[Auranofin (drug)]] 5 µM 28.9× (z +8.9) | — |
| [[A-427 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.757 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.993 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6150), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH10]] | +0.78 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[PPP1R36]] | +0.77 | +0.61 / +0.80 | both halves | 7e-06 |  |
| [[LINC02646]] | +0.77 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[MFSD2B]] | +0.77 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.76 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.75 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[USP50]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.75 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[PEBP4]] | +0.74 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[DRC1]] | +0.73 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[C2CD6]] | +0.73 | +0.68 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PLA2G12B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.802). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.3, -10.3); signed map (21.1, 9.9). **Vector** length 63.4, 9.79% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +16.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +4.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +2.4 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -1.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -0.7 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase A2 group XIIB |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:72,934,762-72,954,806 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PLA2G13 |
| Gene groups (HGNC) | Phospholipases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BX93](https://www.uniprot.org/uniprotkb/Q9BX93) (Group XIIB secretory phospholipase A2-like protein):

> Not known; does not seem to have catalytic activity.

**Summary**, from NCBI Gene [84647](https://www.ncbi.nlm.nih.gov/gene/84647):

> The protein encoded by this gene belongs to the phospholipase A2 (PLA2) group of enzymes, which function in glycolipid hydrolysis with the release of free fatty acids and lysophospholipids. This family member has altered phospholipid-binding properties and is catalytically inactive. The protein is secreted, and together with microsomal triglyceride transfer protein, it functions to regulate HNF4alpha-induced hepatitis C virus infectivity. The expression of this gene is down-regulated in various …

**Accessions** — [HGNC:18555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18555) · Entrez [84647](https://www.ncbi.nlm.nih.gov/gene/84647) · UniProt [Q9BX93](https://www.uniprot.org/uniprotkb/Q9BX93) · Ensembl [ENSG00000138308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138308)

## Data

Gene col 6150: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6150); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6150, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6150]; `tensor/DDL_lfc|DDL_z.npy` [6150]; `embed/gene_vectors.npy` [6150]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6150 or target_col == 6150). Every well: [[PLA2G12B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLA2G12B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
