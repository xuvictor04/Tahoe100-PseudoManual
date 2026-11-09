---
symbol: "TRAPPC5"
type: "gene"
col: 11160
ensembl_id: "ENSG00000181029"
name: "trafficking protein particle complex subunit 5"
location: "19p13.2"
module: 24
arm: "+"
pooled_cpm: 7.4
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# TRAPPC5

*trafficking protein particle complex subunit 5* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.46× (z +6.4, q 8e-08, up in 25 of 30 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.668× (z -4.2, q 0.015, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PITPNA-AS1]] (+0.77, fdr 1e-05), [[POLR2I]] (+0.76, fdr 3e-05), [[LAGE3]] (+0.75, fdr 1e-05); moves opposite to [[RCC2]] (-0.66, fdr 7e-06), [[HCFC1]] (-0.64, fdr 3e-05), [[SRSF1]] (-0.63, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00888-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +6.4 | 8e-08 | 25/30 (A498, SNU-423, …) | two highest doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +5.3 | 3e-05 | 9/11 (SW1417, A498, …) | two highest doses | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +5.1 | 8e-05 | 27/38 (NCI-H1573, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.90×** | +4.7 | 3e-04 | 26/40 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11160.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -4.2 | 0.015 | 24/44 (Hs 766T, NCI-H23, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.585×** | -3.9 | 0.022 | 23/47 (J82, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.736× | -3.2 | 0.20 | 23/44 (AsPC-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.633× | -3.1 | 0.20 | 12/47 (SK-MEL-2, C32, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.656× | -3.1 | 0.20 | 18/47 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sildenafil (drug)]] 0.5 µM |  | 0.650× | -3.1 | 0.20 | 13/47 (HS-578T, J82, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 13 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNA-AS1]] | +0.77 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[POLR2I]] | +0.76 | +0.46 / +0.78 | both halves | 3e-05 |  |
| [[LAGE3]] | +0.75 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[ATP5PO]] ⚠ | +0.73 | +0.48 / +0.70 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[IFI27L2]] | +0.73 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[RPP21]] | +0.72 | +0.36 / +0.77 | both halves | 9e-05 |  |
| [[POLR2J]] ⚠ | +0.72 | +0.53 / +0.70 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL43]] | +0.72 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[NDUFA8]] | +0.71 | +0.46 / +0.71 | both halves | 3e-05 |  |
| [[ISCA2]] | +0.71 | +0.46 / +0.71 | both halves | 2e-05 |  |
| [[C18orf21]] | +0.71 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | +0.71 | +0.48 / +0.76 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL57]] | +0.70 | +0.38 / +0.74 | both halves | 6e-05 |  |
| [[SCAND1]] | +0.70 | +0.60 / +0.80 | both halves | 7e-06 |  |
| [[C19orf53]] | +0.70 | +0.54 / +0.74 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCC2]] | -0.66 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[HCFC1]] | -0.64 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[SRSF1]] | -0.63 | -0.43 / -0.59 | both halves | 4e-05 |  |
| [[ILF3]] | -0.61 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[MACROH2A1]] | -0.61 | -0.50 / -0.72 | both halves | 1e-05 |  |
| [[HNRNPA2B1]] | -0.61 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[CERS2]] | -0.61 | -0.43 / -0.55 | both halves | 4e-05 |  |
| [[SMG1P6]] | -0.60 | -0.32 / -0.67 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00888-1]] | B | LINC00888-1 activity raises TRAPPC5's level | lines that do not express LINC00888-1 (7) vs lines expressing it (43) | 1.22× lower at baseline in the lines without LINC00888-1 | 0.046 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KIF3C, TBKBP1, GDAP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.742). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-45.1, -14.1); signed map (-17.8, -7.1). **Vector** length 52.6, 9.10% of its response variance represented; |z| ≥ 3 in 533 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.54 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.3 | +1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.0 | -2.6 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,680,833-7,687,703 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC52424, TRS31 |
| Gene groups (HGNC) | Trafficking protein particle complex subunits |
| Reactome | 8 pathways, smallest: COPII-mediated vesicle transport; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUR0](https://www.uniprot.org/uniprotkb/Q8IUR0) (Trafficking protein particle complex subunit 5):

> May play a role in vesicular transport from endoplasmic reticulum to Golgi.

**Summary**, from NCBI Gene [126003](https://www.ncbi.nlm.nih.gov/gene/126003):

> Predicted to be involved in endoplasmic reticulum to Golgi vesicle-mediated transport. Part of TRAPP complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23067) · Entrez [126003](https://www.ncbi.nlm.nih.gov/gene/126003) · UniProt [Q8IUR0](https://www.uniprot.org/uniprotkb/Q8IUR0) · Ensembl [ENSG00000181029](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181029)

## Data

Gene col 11160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11160); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11160]; `tensor/DDL_lfc|DDL_z.npy` [11160]; `embed/gene_vectors.npy` [11160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11160 or target_col == 11160). Every well: [[TRAPPC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
