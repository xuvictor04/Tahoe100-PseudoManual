---
symbol: "PPP1R14A"
type: "gene"
col: 9507
ensembl_id: "ENSG00000167641"
name: "protein phosphatase 1 regulatory inhibitor subunit 14A"
location: "19q13.1"
module: 45
arm: "+"
pooled_cpm: 3.74
n_lines_expressing: 11
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# PPP1R14A

*protein phosphatase 1 regulatory inhibitor subunit 14A* — 19q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 14.1× (z +12.2, q 1e-31, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.43× (z +5.8, q 9e-07, up in 2 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V0E2]] (+0.62, fdr 4e-05), [[GAMT]] (+0.61, fdr 4e-05), [[FLVCR1-DT]] (+0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[PTP4A2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9507.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **14.1×** | +12.2 | 1e-31 | 4/5 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **13.7×** | +11.6 | 9e-29 | 3/4 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.64×** | +7.4 | 3e-11 | 4/5 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +5.8 | 9e-07 | 2/7 (NCI-H2347, NCI-H23) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.63×** | +5.7 | 1e-06 | 2/6 (NCI-H2347, NCI-H661) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **2.28×** | +5.4 | 7e-06 | 1/9 (A549) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.98×** | +5.0 | 3e-05 | 3/5 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.16×** | +5.0 | 3e-05 | 0/7 | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.00×** | +4.9 | 6e-05 | 2/6 (PANC-1, NCI-H1792) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.76×** | +4.7 | 2e-04 | 3/8 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.55×** | +4.2 | 0.002 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.51×** | +3.6 | 0.013 | 1/4 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +3.5 | 0.021 | 2/8 (PANC-1, A549) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.07×** | +3.4 | 0.031 | 1/8 (NCI-H2347) | top dose only | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **2.06×** | +3.3 | 0.032 | 0/4 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Omeprazole (sodium) (drug)]] 5 µM |  | **1.93×** | +3.1 | 0.080 | 1/9 (NCI-H23) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9507.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.283× | -3.0 | 0.57 | 3/9 (NCI-H2347, NCI-H661, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9507. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 47.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.41× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 0.206 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.212 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.224 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.190 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.192 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.214 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.227 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.213 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.206 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.194 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[NCI-H23 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.201 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.221 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.205 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.199 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9507), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 17 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V0E2]] | +0.62 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[GAMT]] | +0.61 | +0.40 / +0.59 | both halves | 4e-05 |  |
| [[FLVCR1-DT]] | +0.56 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[DUSP9]] | +0.56 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[DLL3]] | +0.52 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[ATP8A1]] | +0.51 | +0.33 / +0.36 | both halves | 1e-04 |  |
| [[NTHL1]] | +0.51 | +0.32 / +0.47 | both halves | 1e-04 |  |
| [[SIGIRR]] | +0.51 | +0.37 / +0.41 | both halves | 8e-05 |  |
| [[SLC38A4]] | +0.51 | +0.37 / +0.31 | both halves | 2e-04 |  |
| [[MIF4GD]] | +0.50 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[CDK5]] | +0.50 | +0.25 / +0.46 | both halves | 4e-04 |  |
| [[AQP11]] | +0.50 | +0.34 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTP4A2]] | B | PPP1R14A activity raises PTP4A2's level | lines that do not express PPP1R14A (39) vs lines expressing it (11) | 1.40× lower at baseline in the lines without PPP1R14A | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, SFTPA2 |
| [[CACNG7]] | B | PPP1R14A activity raises CACNG7's level | lines that do not express PPP1R14A (39) vs lines expressing it (11) | 2.36× lower at baseline in the lines without PPP1R14A | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, SFTPA2 |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.468). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (9.9, -7.2); signed map (-27.0, -3.1). **Vector** length 16.2, 3.41% of its response variance represented; |z| ≥ 3 in 162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.2 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.8 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.7 | +1.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.6 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.6 | -0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -0.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.7 | -0.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.5 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.5 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.5 | -0.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.5 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.5 | -1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory inhibitor subunit 14A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.1 — chr19:38,251,237-38,256,532 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CPI-17; previously PPP1INL |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Reactome | 4 pathways, smallest: RHO GTPases activate PKNs; RHO GTPase Effectors; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A00](https://www.uniprot.org/uniprotkb/Q96A00) (Protein phosphatase 1 regulatory subunit 14A):

> Inhibitor of PPP1CA. Has over 1000-fold higher inhibitory activity when phosphorylated, creating a molecular switch for regulating the phosphorylation status of PPP1CA substrates and smooth muscle contraction.

**Summary**, from NCBI Gene [94274](https://www.ncbi.nlm.nih.gov/gene/94274):

> The protein encoded by this gene belongs to the protein phosphatase 1 (PP1) inhibitor family. This protein is an inhibitor of smooth muscle myosin phosphatase, and has higher inhibitory activity when phosphorylated. Inhibition of myosin phosphatase leads to increased myosin phosphorylation and enhanced smooth muscle contraction. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:14871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14871) · Entrez [94274](https://www.ncbi.nlm.nih.gov/gene/94274) · UniProt [Q96A00](https://www.uniprot.org/uniprotkb/Q96A00) · Ensembl [ENSG00000167641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167641)

## Data

Gene col 9507: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9507); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9507, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9507]; `tensor/DDL_lfc|DDL_z.npy` [9507]; `embed/gene_vectors.npy` [9507]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9507 or target_col == 9507). Every well: [[PPP1R14A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R14A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
