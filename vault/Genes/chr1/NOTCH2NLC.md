---
symbol: "NOTCH2NLC"
type: "gene"
col: 16212
ensembl_id: "ENSG00000286219"
name: "notch 2 N-terminal like C"
location: "1q21.2"
module: 226
arm: "+"
pooled_cpm: 2.16
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/226"]
generated_by: "tahoemap"
---

# NOTCH2NLC

*notch 2 N-terminal like C* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.49× (z +18.6, q 0e+00, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.811× (z -5.8, q 3e-06, down in 25 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Darinaparsin (drug)]] 5 µM: 0.695× (z -4.0, q 0.013, down in 5 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOTCH2NLB]] (+0.77, fdr 7e-06), [[NBPF26]] (+0.65, fdr 7e-06), [[SYNGAP1]] (+0.65, fdr 1e-05); moves opposite to [[NFATC3]] (-0.67, fdr 1e-05), [[TYW1]] (-0.66, fdr 1e-05), [[ORC2]] (-0.60, fdr 1e-05).
> It is in [[Module 226]], a single-armed module (NOTCH2 Activation and Transmission of Signal to the Nucleus).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16212.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.49×** | +18.6 | 0e+00 | 29/32 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.78×** | +7.9 | 8e-13 | 19/30 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.66×** | +7.3 | 7e-11 | 28/40 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.26×** | +6.3 | 5e-08 | 22/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.80×** | +4.5 | 7e-04 | 15/34 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.75×** | +4.2 | 0.003 | 2/23 (HOP62, MIA PaCa-2) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +4.1 | 0.004 | 6/22 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.40×** | +3.5 | 0.029 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.54×** | +3.3 | 0.053 | 3/15 (J82, NCI-H1792, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.056 | 8/43 (SW1417, HepG2/C3A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16212.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.811×** | -5.8 | 3e-06 | 25/47 (SW1417, A498, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.566×** | -4.4 | 0.003 | 17/43 (CFPAC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.695×** | -4.0 | 0.013 | 5/43 (COLO 205, HS-578T, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.09 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +14.8) | — |
| [[A-172 (line)]] | wt | 3.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 3.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 3.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +10.1) | — |
| [[A-427 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.746 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.675 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.990 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.840 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLB]] | +0.77 | +0.70 / +0.74 | both halves | 7e-06 | pathway: Expression of NOTCH2NL genes |
| [[NBPF26]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[SYNGAP1]] | +0.65 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[NOTCH2NLA]] | +0.63 | +0.52 / +0.67 | both halves | 1e-05 | pathway: Expression of NOTCH2NL genes |
| [[TEF]] | +0.59 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[ATP2C2-AS1]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[NBPF19]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 | STRING 791; ⚠ same locus (3.2 kb, same strand: neighbours can correlate without regulation) |
| [[CGGBP1]] | +0.57 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[MMRN2]] | +0.56 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[PIEZO1]] | +0.56 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[DZIP3]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[LINC00882]] | +0.55 | +0.44 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFATC3]] | -0.67 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[TYW1]] | -0.66 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[ORC2]] | -0.60 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[SDHAF1]] | -0.60 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.58 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[CDC123]] | -0.58 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[GRB2]] | -0.58 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[FBXW11]] | -0.58 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[HIRA]] | -0.58 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ANKRD13D]] | -0.58 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[RAB5IF]] | -0.57 | -0.40 / -0.58 | both halves | 4e-05 |  |
| [[TRAPPC10]] | -0.57 | -0.59 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 226]] — NOTCH2 Activation and Transmission of Signal to the Nucleus; 9 genes; every member is in the + arm (projection on the module's main direction 0.735). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.8, -17.7); signed map (44.2, -15.5). **Vector** length 39.9, 4.03% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +18.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +0.8 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.7 | +0.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +0.7 | +1.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.6 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -0.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | notch 2 N-terminal like C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:149,390,621-149,471,833 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 6 pathways, smallest: Expression of NOTCH2NL genes; NOTCH2 Activation and Transmission of Signal to the Nucleus; Signaling by NOTCH2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DPK4](https://www.uniprot.org/uniprotkb/P0DPK4) (Notch homolog 2 N-terminal-like protein C):

> Human-specific protein that promotes neural progenitor proliferation and evolutionary expansion of the brain neocortex by regulating the Notch signaling pathway. Able to promote neural progenitor self-renewal, possibly by down-regulating neuronal differentiation genes, thereby delaying the differentiation of neuronal progenitors and leading to an overall final increase in neuronal production. Acts by enhancing the Notch signaling pathway via two different mechanisms that probably work in …

**Summary**, from NCBI Gene [100996717](https://www.ncbi.nlm.nih.gov/gene/100996717):

> Enables Notch binding activity. Involved in cerebral cortex development and positive regulation of Notch signaling pathway. Located in extracellular region; nucleoplasm; and plasma membrane. Implicated in essential tremor 6; neuronal intranuclear inclusion disease; and oculopharyngodistal myopathy 3. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:53924](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53924) · Entrez [100996717](https://www.ncbi.nlm.nih.gov/gene/100996717) · UniProt [P0DPK4](https://www.uniprot.org/uniprotkb/P0DPK4) · Ensembl [ENSG00000286219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000286219)

## Data

Gene col 16212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16212); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16212]; `tensor/DDL_lfc|DDL_z.npy` [16212]; `embed/gene_vectors.npy` [16212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16212 or target_col == 16212). Every well: [[NOTCH2NLC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOTCH2NLC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
