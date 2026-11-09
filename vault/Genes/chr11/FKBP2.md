---
symbol: "FKBP2"
type: "gene"
col: 10394
ensembl_id: "ENSG00000173486"
name: "FKBP prolyl isomerase 2"
location: "11q13.1"
module: 131
arm: "+"
pooled_cpm: 33.02
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# FKBP2

*FKBP prolyl isomerase 2* — 11q13.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.94× (z +6.9, q 4e-09, up in 40 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 5.42×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCTN6-DT]] (+0.74, fdr 7e-06), [[ACAP1]] (+0.73, fdr 7e-06), [[DDT]] (+0.70, fdr 1e-05); moves opposite to [[CCT5]] (-0.68, fdr 7e-06), [[TMEM33]] (-0.65, fdr 1e-05), [[PRPS1]] (-0.64, fdr 7e-06).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10394.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 5.42×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.94×** | +6.9 | 4e-09 | 40/42 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +5.6 | 5e-06 | 35/38 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +4.1 | 0.008 | 30/38 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +3.8 | 0.025 | 10/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.67×** | +3.4 | 0.070 | 31/45 (CFPAC-1, A-172, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10394.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.598× | -3.2 | 0.39 | 35/48 (SW 1088, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.629× | -3.1 | 0.39 | 26/48 (CHP-212, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.720× | -3.1 | 0.39 | 25/47 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN6-DT]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[ACAP1]] | +0.73 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[DDT]] | +0.70 | +0.52 / +0.78 | both halves | 1e-05 |  |
| [[TRMT112]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[RPS15]] ⚠ | +0.69 | +0.56 / +0.71 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS29]] | +0.68 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[TMEM134]] | +0.68 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[SNHG9]] | +0.68 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[FAU]] | +0.68 | +0.48 / +0.74 | both halves | 2e-05 |  |
| [[TMEM258]] | +0.68 | +0.58 / +0.74 | both halves | 8e-06 |  |
| [[SNHG25]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SERF2]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[INAFM1]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | -0.68 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.65 | -0.57 / -0.67 | both halves | 1e-05 |  |
| [[PRPS1]] | -0.64 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[CAPRIN1]] | -0.63 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[RPE]] | -0.63 | -0.57 / -0.69 | both halves | 9e-06 |  |
| [[MANEA]] | -0.63 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[NUP155]] | -0.63 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[IPO5]] | -0.63 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[CCT2]] | -0.62 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.62 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[GPN1]] | -0.62 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[IPO8]] | -0.62 | -0.51 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: all its genes lie on one side of its main direction.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-32.8, -30.3); signed map (-28.5, 10.1). **Vector** length 64.3, 20.5% of its response variance represented; |z| ≥ 3 in 405 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Termination* (reactome, mean cos +0.58 to 20); *Peptide chain elongation* (reactome, mean cos +0.57 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.57 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.0 | +1.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.6 | +1.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.1 | +0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -1.9 | +4.1 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | FKBP prolyl isomerase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,241,003-64,244,132 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FKBP-13, FKBP13, PPIase |
| Gene groups (HGNC) | FKBP prolyl isomerase family |
| Hallmark sets | MTORC1_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [P26885](https://www.uniprot.org/uniprotkb/P26885) (Peptidyl-prolyl cis-trans isomerase FKBP2):

> PPIases accelerate the folding of proteins. It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides.

**Summary**, from NCBI Gene [2286](https://www.ncbi.nlm.nih.gov/gene/2286):

> The protein encoded by this gene is a member of the immunophilin protein family, which play a role in immunoregulation and basic cellular processes involving protein folding and trafficking. This encoded protein is a cis-trans prolyl isomerase that binds the immunosuppressants FK506 and rapamycin. It is thought to function as an ER chaperone and may also act as a component of membrane cytoskeletal scaffolds. Multiple alternatively spliced variants, encoding the same protein, have been …

**Accessions** — [HGNC:3718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3718) · Entrez [2286](https://www.ncbi.nlm.nih.gov/gene/2286) · UniProt [P26885](https://www.uniprot.org/uniprotkb/P26885) · Ensembl [ENSG00000173486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173486)

## Data

Gene col 10394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10394); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10394]; `tensor/DDL_lfc|DDL_z.npy` [10394]; `embed/gene_vectors.npy` [10394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10394 or target_col == 10394). Every well: [[FKBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
