---
symbol: "FMC1"
type: "gene"
col: 9024
ensembl_id: "ENSG00000164898"
name: "formation of mitochondrial complex V assembly factor 1"
location: "7q34"
module: 24
arm: "+"
pooled_cpm: 2.43
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# FMC1

*formation of mitochondrial complex V assembly factor 1* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.21× (z +10.7, q 7e-24, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +4.7, q 3e-04, up in 9 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.557× (z -4.5, q 0.003, down in 16 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cyclosporin A (drug)]] 0.5 µM in 1 line (SW1417 0.0716×); [[Hydroxyurea (drug)]] 0.5 µM in 1 line (C32 0.0618×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf56]] (+0.70, fdr 1e-05), [[SMIM27]] (+0.68, fdr 1e-05), [[PIGP]] (+0.63, fdr 2e-05); moves opposite to [[PSMD2]] (-0.62, fdr 1e-05), [[TTL]] (-0.61, fdr 1e-05), [[STK25]] (-0.59, fdr 6e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KCNC4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.21×** | +10.7 | 7e-24 | 1/1 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +8.0 | 3e-13 | 13/16 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.18×** | +6.0 | 3e-07 | 8/14 (NCI-H2030, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +5.2 | 3e-05 | 3/4 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.7 | 3e-04 | 9/30 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.028 | 4/43 (LS 180, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.3 | 0.091 | 2/13 (HOP62, Hs 766T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.2 | 0.093 | 8/34 (A-172, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9024.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cyclosporin A (drug)]] 0.5 µM in 1 line (SW1417 0.0716×); [[Hydroxyurea (drug)]] 0.5 µM in 1 line (C32 0.0618×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.557×** | -4.5 | 0.003 | 16/42 (Hs 766T, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.679× | -3.0 | 0.51 | 9/44 (LS 180, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | 0.478× | -3.0 | 0.51 | 4/44 (SK-MEL-2, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 3.97 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.5 µM 0.0618× (z -8.6) |
| [[SW1417 (line)]] | alt | 3.28 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0716× (z -8.6) |
| [[A-172 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.934 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf56]] | +0.70 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[SMIM27]] | +0.68 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[PIGP]] | +0.63 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[ZNF428]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[PNISR]] | +0.63 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[KMT2E]] | +0.63 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[EMSY-DT]] | +0.62 | +0.46 / +0.71 | both halves | 3e-05 |  |
| [[MRPL54]] | +0.62 | +0.40 / +0.70 | both halves | 4e-05 |  |
| [[AKAP1-DT]] | +0.62 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ZNF232-AS1]] | +0.62 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[C11orf1]] | +0.62 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[SCAF11]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD2]] | -0.62 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[TTL]] | -0.61 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[STK25]] | -0.59 | -0.61 / -0.39 | both halves | 6e-05 |  |
| [[HERC2]] | -0.58 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ACOT7]] | -0.58 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[MACROH2A1]] | -0.57 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[ATP13A2]] | -0.56 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ZNF731P]] | -0.55 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[GPRIN1]] | -0.55 | -0.54 / -0.29 | both halves | 2e-04 |  |
| [[MSN]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[PLXNA1]] | -0.54 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[STIP1]] | -0.53 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNC4]] | B | KCNC4 activity raises FMC1's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 1.19× lower at baseline in the lines without KCNC4 | 0.085 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.552). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.0, -21.8); signed map (-6.7, 2.9). **Vector** length 35.8, 3.60% of its response variance represented; |z| ≥ 3 in 818 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.6 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.0 | +1.0 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.2 | -1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | formation of mitochondrial complex V assembly factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:139,339,457-139,346,328 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC268; previously C7orf55 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HJ9](https://www.uniprot.org/uniprotkb/Q96HJ9) (Protein FMC1 homolog):

> Plays a role in the assembly/stability of the mitochondrial membrane ATP synthase (F(1)F(0) ATP synthase or Complex V).

**Summary**, from NCBI Gene [154791](https://www.ncbi.nlm.nih.gov/gene/154791):

> Involved in mitochondrial proton-transporting ATP synthase complex assembly. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26946](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26946) · Entrez [154791](https://www.ncbi.nlm.nih.gov/gene/154791) · UniProt [Q96HJ9](https://www.uniprot.org/uniprotkb/Q96HJ9) · Ensembl [ENSG00000164898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164898)

## Data

Gene col 9024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9024); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9024]; `tensor/DDL_lfc|DDL_z.npy` [9024]; `embed/gene_vectors.npy` [9024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9024 or target_col == 9024). Every well: [[FMC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FMC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
