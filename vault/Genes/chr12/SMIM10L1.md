---
symbol: "SMIM10L1"
type: "gene"
col: 14995
ensembl_id: "ENSG00000256537"
name: "small integral membrane protein 10 like 1"
location: "12p13.2"
module: 7
arm: "+"
pooled_cpm: 20.05
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SMIM10L1

*small integral membrane protein 10 like 1* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.18× (z +9.1, q 5e-17, up in 36 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.68× (z +6.1, q 2e-07, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.533× (z -7.3, q 1e-10, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7]] (+0.69, fdr 1e-05), [[TYW3]] (+0.64, fdr 2e-05), [[PSMC1]] (+0.63, fdr 1e-05); moves opposite to [[SUN1]] (-0.59, fdr 4e-05), [[NCOR2]] (-0.55, fdr 2e-05), [[ENTPD2]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14995.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.18×** | +9.1 | 5e-17 | 36/42 (Panc 03.27, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.89×** | +7.2 | 2e-10 | 22/31 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +6.1 | 2e-07 | 30/47 (NCI-H1573, HOP62, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +6.0 | 3e-07 | 26/37 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +5.7 | 1e-06 | 32/43 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +5.2 | 1e-05 | 28/47 (COLO 205, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +4.7 | 3e-04 | 23/47 (NCI-H1573, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +4.5 | 5e-04 | 25/48 (HEC-1-A, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.30×** | +4.4 | 7e-04 | 27/48 (A-427, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.34×** | +3.4 | 0.033 | 19/44 (CFPAC-1, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 1.29× | +3.0 | 0.12 | 12/48 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14995.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.533×** | -7.3 | 1e-10 | 37/48 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.546×** | -7.1 | 5e-10 | 37/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.614×** | -5.7 | 2e-06 | 30/48 (NCI-H1792, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -4.7 | 4e-04 | 24/47 (NCI-H2030, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.773×** | -4.2 | 0.002 | 21/47 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.718×** | -3.9 | 0.011 | 21/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.758× | -3.2 | 0.10 | 15/48 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.825× | -3.2 | 0.11 | 10/48 (SW1417, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14995. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 76.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -16.5) |
| [[C32 (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 28.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 21.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.86× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 32.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -10.5) |
| [[SW480 (line)]] | alt | 29.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.325× (z -8.8) |
| [[A-172 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14995), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7]] | +0.69 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[TYW3]] | +0.64 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[PSMC1]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[PSMA1]] | +0.62 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SPR]] | +0.59 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[RHBDD3]] | +0.59 | +0.59 / +0.34 | both halves | 1e-04 |  |
| [[ZNF189]] | +0.59 | +0.60 / +0.39 | both halves | 6e-05 |  |
| [[PSMC2]] | +0.58 | +0.57 / +0.33 | both halves | 1e-04 |  |
| [[CAP2]] | +0.58 | +0.66 / +0.33 | both halves | 1e-04 |  |
| [[PHTF1]] | +0.58 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[COA6]] | +0.58 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[TACO1]] | +0.58 | +0.60 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUN1]] | -0.59 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[NCOR2]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ENTPD2]] | -0.53 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[PLCB3]] | -0.53 | -0.53 / -0.40 | both halves | 4e-05 |  |
| [[TBCD]] | -0.50 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[DNAAF3]] | -0.48 | -0.39 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[ARL6IP6]] | -0.48 | -0.42 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SMIM10L1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.535). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-18.3, 10.4); signed map (-24.9, -23.3). **Vector** length 65.0, 13.3% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.6 | +4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.5 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +1.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +2.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.3 | -7.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -5.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.9 | -7.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.8 | -2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -0.9 | +0.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -0.9 | -0.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -0.9 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 10 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:11,171,194-11,176,016 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [P0DMW3](https://www.uniprot.org/uniprotkb/P0DMW3) carries no function annotation.

**Summary**, from NCBI Gene [100129361](https://www.ncbi.nlm.nih.gov/gene/100129361):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:49847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49847) · Entrez [100129361](https://www.ncbi.nlm.nih.gov/gene/100129361) · UniProt [P0DMW3](https://www.uniprot.org/uniprotkb/P0DMW3) · Ensembl [ENSG00000256537](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256537)

## Data

Gene col 14995: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14995); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14995, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14995]; `tensor/DDL_lfc|DDL_z.npy` [14995]; `embed/gene_vectors.npy` [14995]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14995 or target_col == 14995). Every well: [[SMIM10L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM10L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
