---
symbol: "NDUFS8"
type: "gene"
col: 3160
ensembl_id: "ENSG00000110717"
name: "NADH:ubiquinone oxidoreductase core subunit S8"
location: "11q13.2"
module: 58
arm: "+"
pooled_cpm: 22.48
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# NDUFS8

*NADH:ubiquinone oxidoreductase core subunit S8* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.82× (z +5.8, q 3e-06, up in 35 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.544× (z -5.8, q 4e-06, down in 35 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AsPC-1 0.226×, C-33 A 0.226×, LoVo 0.294×, NCI-H2030 0.331×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.181×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.110×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA3]] (+0.79, fdr 7e-06), [[TMEM160]] (+0.78, fdr 7e-06), [[C19orf53]] (+0.76, fdr 7e-06); moves opposite to [[DDX39B]] (-0.58, fdr 2e-05), [[SRRM2]] (-0.58, fdr 3e-05), [[EIF4G2]] (-0.53, fdr 5e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.82×** | +5.8 | 3e-06 | 35/41 (A549, PANC-1, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.18×** | +4.9 | 3e-04 | 26/37 (KATO III, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.14×** | +4.5 | 0.001 | 26/34 (PANC-1, CFPAC-1, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.86×** | +4.2 | 0.004 | 28/43 (LS 180, HCT15, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.5 | 0.059 | 26/43 (CFPAC-1, SW480, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.38× | +3.1 | 0.19 | 23/48 (MIA PaCa-2, NCI-H23, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3160.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AsPC-1 0.226×, C-33 A 0.226×, LoVo 0.294×, NCI-H2030 0.331×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.181×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.110×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.544×** | -5.8 | 4e-06 | 35/47 (AsPC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 41.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 11.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -9.3) |
| [[C-33 A (line)]] | alt | 25.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -9.2) |
| [[LoVo (line)]] | wt | 19.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 24.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -8.5) |
| [[RKO (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 7 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA3]] | +0.79 | +0.73 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[TMEM160]] | +0.78 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[C19orf53]] | +0.76 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[CENPX]] | +0.75 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[NDUFAB1]] | +0.73 | +0.71 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[AURKAIP1]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[COPS9]] | +0.70 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[NDUFS7]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[MRPL41]] ⚠ | +0.67 | +0.54 / +0.66 | both halves | 1e-05 | STRING 524; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFS5]] | +0.67 | +0.70 / +0.53 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[ELOB]] | +0.66 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[PSMB3]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ATP5MG]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 635 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX39B]] | -0.58 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[SRRM2]] | -0.58 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.53 | -0.40 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.4, -19.2); signed map (-37.4, 6.8). **Vector** length 61.4, 17.2% of its response variance represented; |z| ≥ 3 in 361 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +0.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | -0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -2.0 | +4.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | -1.8 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | +0.7 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase core subunit S8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:68,030,617-68,036,644 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TYKY, CI-23k |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase core subunits; MicroRNA protein coding host genes |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O00217](https://www.uniprot.org/uniprotkb/O00217) (NADH dehydrogenase):

> Core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which catalyzes electron transfer from NADH through the respiratory chain, using ubiquinone as an electron acceptor. Essential for the catalytic activity and assembly of complex I.

**Summary**, from NCBI Gene [4728](https://www.ncbi.nlm.nih.gov/gene/4728):

> This gene encodes a subunit of mitochondrial NADH:ubiquinone oxidoreductase, or Complex I, a multimeric enzyme of the respiratory chain responsible for NADH oxidation, ubiquinone reduction, and the ejection of protons from mitochondria. The encoded protein is involved in the binding of two of the six to eight iron-sulfur clusters of Complex I and, as such, is required in the electron transfer process. Mutations in this gene have been associated with Leigh syndrome. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:7715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7715) · Entrez [4728](https://www.ncbi.nlm.nih.gov/gene/4728) · UniProt [O00217](https://www.uniprot.org/uniprotkb/O00217) · Ensembl [ENSG00000110717](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110717)

## Data

Gene col 3160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3160); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3160]; `tensor/DDL_lfc|DDL_z.npy` [3160]; `embed/gene_vectors.npy` [3160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3160 or target_col == 3160). Every well: [[NDUFS8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFS8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
