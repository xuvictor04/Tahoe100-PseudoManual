---
symbol: "DERL2"
type: "gene"
col: 1035
ensembl_id: "ENSG00000072849"
name: "derlin 2"
location: "17p13.2"
module: 49
arm: "+"
pooled_cpm: 23.27
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# DERL2

*derlin 2* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.90× (z +5.9, q 3e-06, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.632× (z -8.0, q 1e-12, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG5]] (+0.74, fdr 7e-06), [[SLC33A1]] (+0.72, fdr 7e-06), [[RUSF1]] (+0.69, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1035.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.90×** | +5.9 | 3e-06 | 25/48 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Salicylic acid (drug)]] 5 µM |  | 1.17× | +3.7 | 0.067 | 10/48 (SHP-77, LOX-IMVI, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.40× | +3.0 | 0.45 | 11/46 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1035.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.632×** | -8.0 | 1e-12 | 32/48 (SW480, A-172, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.714×** | -7.9 | 1e-12 | 33/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.725×** | -7.1 | 2e-10 | 24/47 (NCI-H1792, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.739×** | -6.7 | 3e-09 | 27/47 (LS 180, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.714×** | -5.8 | 6e-07 | 28/48 (KATO III, AsPC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.731×** | -5.4 | 6e-06 | 21/48 (AsPC-1, HT-29, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.738×** | -5.2 | 1e-05 | 23/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.579×** | -5.0 | 5e-05 | 20/48 (A549, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.782×** | -4.3 | 0.001 | 19/46 (AsPC-1, HepG2/C3A, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | **0.823×** | -4.2 | 0.001 | 18/48 (NCI-H661, HOP62, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.788×** | -4.1 | 0.002 | 19/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.788×** | -4.1 | 0.002 | 21/47 (AN3 CA, NCI-H661, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.794×** | -4.0 | 0.003 | 15/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.805×** | -3.7 | 0.007 | 14/48 (KATO III, SHP-77, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.816×** | -3.4 | 0.029 | 16/47 (KATO III, SW 1088, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1035. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 29.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -10.4) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H1792 (line)]] | alt | 24.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.7) |
| [[A-172 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -8.5) ⚠ cell-cycle shift, explains ~21% of this change |
| [[AsPC-1 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.366× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -8.5) ⚠ cell-cycle shift, explains ~21% of this change |
| [[KATO III (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.348× (z -8.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.134× (z -8.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1035), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG5]] | +0.74 | +0.75 / +0.67 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 402 |
| [[SLC33A1]] | +0.72 | +0.71 / +0.63 | both halves | 7e-06 | pathway: Disorders of transmembrane transporters |
| [[RUSF1]] | +0.69 | +0.71 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[OSTC]] | +0.67 | +0.68 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[GOLGA5]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[MMUT]] | +0.66 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[PARL]] | +0.65 | +0.71 / +0.53 | both halves | 1e-05 | same gene group |
| [[SPCS2]] | +0.65 | +0.63 / +0.78 | both halves | 7e-06 |  |
| [[ZW10]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ERCC5]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[COG3]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[CWF19L1]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, -36.9); signed map (-54.5, 12.1). **Vector** length 79.5, 15.6% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.56 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +0.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.5 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.9 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.8 | -4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -2.6 | -4.3 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | derlin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:5,471,254-5,486,811 (-) |
| Ensembl biotype | protein_coding |
| Also known as | F-LAN-1, FLANa, F-LANa, CGI-101, derlin-2 |
| Gene groups (HGNC) | Rhomboid family |
| Reactome | 20 pathways, smallest: ER Quality Control Compartment (ERQC); Calnexin/calreticulin cycle; N-glycan trimming in the ER and Calnexin/Calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZP9](https://www.uniprot.org/uniprotkb/Q9GZP9) (Derlin-2):

> Functional component of endoplasmic reticulum-associated degradation (ERAD) for misfolded lumenal glycoproteins, but not that of misfolded nonglycoproteins. May act by forming a channel that allows the retrotranslocation of misfolded glycoproteins into the cytosol where they are ubiquitinated and degraded by the proteasome. May mediate the interaction between VCP and misfolded glycoproteins. May also be involved in endoplasmic reticulum stress-induced pre-emptive quality control, a mechanism …

**Summary**, from NCBI Gene [51009](https://www.ncbi.nlm.nih.gov/gene/51009):

> Proteins that are unfolded or misfolded in the endoplasmic reticulum (ER) must be refolded or degraded to maintain the homeostasis of the ER. DERL2 is involved in the degradation of misfolded glycoproteins in the ER (Oda et al., 2006 [PubMed 16449189]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:17943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17943) · Entrez [51009](https://www.ncbi.nlm.nih.gov/gene/51009) · UniProt [Q9GZP9](https://www.uniprot.org/uniprotkb/Q9GZP9) · Ensembl [ENSG00000072849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072849)

## Data

Gene col 1035: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1035); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1035, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1035]; `tensor/DDL_lfc|DDL_z.npy` [1035]; `embed/gene_vectors.npy` [1035]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1035 or target_col == 1035). Every well: [[DERL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DERL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
