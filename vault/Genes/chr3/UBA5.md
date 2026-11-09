---
symbol: "UBA5"
type: "gene"
col: 1315
ensembl_id: "ENSG00000081307"
name: "ubiquitin like modifier activating enzyme 5"
location: "3q22.1"
module: 65
arm: "+"
pooled_cpm: 52.66
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# UBA5

*ubiquitin like modifier activating enzyme 5* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.37× (z +5.0, q 3e-04, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.658× (z -6.6, q 2e-08, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBE1]] (+0.67, fdr 7e-06), [[TGDS]] (+0.66, fdr 7e-06), [[MRS2]] (+0.65, fdr 7e-06); moves opposite to [[SMURF1]] (-0.66, fdr 1e-05), [[PSEN1]] (-0.57, fdr 1e-05), [[CLCF1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1315.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 3e-04 | 26/48 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.013 | 24/48 (SW480, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.015 | 23/48 (LoVo, SW480, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.6 | 0.046 | 24/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.046 | 22/49 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; position effect removed |
| [[Tomivosertib (drug)]] 5 µM |  | 1.46× | +3.1 | 0.17 | 16/48 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 1.45× | +3.1 | 0.17 | 17/48 (NCI-H23, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1315.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.658×** | -6.6 | 2e-08 | 38/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.672×** | -6.3 | 1e-07 | 36/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -5.7 | 2e-06 | 2/49 (NCI-H23, NCI-H661) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -5.1 | 5e-05 | 28/48 (HS-578T, BT-474, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -4.3 | 0.002 | 27/48 (NCI-H2347, SW480, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.768×** | -4.2 | 0.003 | 31/48 (SW480, J82, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.813×** | -4.1 | 0.004 | 23/48 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.775×** | -4.0 | 0.004 | 28/48 (BT-474, NCI-H2030, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.779×** | -3.9 | 0.005 | 26/48 (HOP62, HCT15, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.788×** | -3.6 | 0.017 | 20/43 (NCI-H1573, BT-474, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.833×** | -3.5 | 0.021 | 18/48 (NCI-H661, NCI-H2347, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.826× | -3.0 | 0.12 | 16/48 (SNU-1, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1315. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 73.2 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0643× (z -14.5) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 56.6 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.147× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 32.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.59× (z +8.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 96.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 62.8 | 0 | 1 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0860× (z -9.1) ⚠ toxic |
| [[A-172 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 84.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 79.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 50.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1315), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBE1]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[TGDS]] | +0.66 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[MRS2]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[TRAPPC11]] | +0.65 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[TSNAX]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[ANAPC4]] | +0.63 | +0.67 / +0.61 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[TRUB1]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[FIP1L1]] | +0.62 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[LINC00888]] | +0.62 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.62 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[NFXL1]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMURF1]] | -0.66 | -0.50 / -0.58 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[PSEN1]] | -0.57 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CLCF1]] | -0.57 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[CYTH2]] | -0.56 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[WNT2B]] | -0.54 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[SLC38A2]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[CHMP1A]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ZSWIM6]] | -0.52 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[PKNOX1]] | -0.52 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[CRK]] | -0.51 | -0.49 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.4, -10.5); signed map (-30.4, -14.4). **Vector** length 105, 28.2% of its response variance represented; |z| ≥ 3 in 739 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +3.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.5 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +0.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.2 | -0.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.4 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -4.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin like modifier activating enzyme 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:132,654,446-132,679,794 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23251; previously UBE1DC1 |
| Gene groups (HGNC) | Ubiquitin like modifier activating enzymes |
| Reactome | 6 pathways, smallest: Dengue Virus Attachment and Entry; Antigen processing: Ubiquitination & Proteasome degradation; Dengue Virus Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZZ9](https://www.uniprot.org/uniprotkb/Q9GZZ9) (Ubiquitin-like modifier-activating enzyme 5):

> E1-like enzyme which specifically catalyzes the first step in ufmylation. Activates UFM1 by first adenylating its C-terminal glycine residue with ATP, and thereafter linking this residue to the side chain of a cysteine residue in E1, yielding a UFM1-E1 thioester and free AMP. Activates UFM1 via a trans-binding mechanism, in which UFM1 interacts with distinct sites in both subunits of the UBA5 homodimer. Trans-binding also promotes stabilization of the UBA5 homodimer, and enhances ATP-binding. …

**Summary**, from NCBI Gene [79876](https://www.ncbi.nlm.nih.gov/gene/79876):

> This gene encodes a member of the E1-like ubiquitin-activating enzyme family. This protein activates ubiquitin-fold modifier 1, a ubiquitin-like post-translational modifier protein, via the formation of a high-energy thioester bond. Alternative splicing results in multiple transcript variants. A pseudogene of this gene has been identified on chromosome 1. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:23230](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23230) · Entrez [79876](https://www.ncbi.nlm.nih.gov/gene/79876) · UniProt [Q9GZZ9](https://www.uniprot.org/uniprotkb/Q9GZZ9) · Ensembl [ENSG00000081307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081307)

## Data

Gene col 1315: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1315); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1315, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1315]; `tensor/DDL_lfc|DDL_z.npy` [1315]; `embed/gene_vectors.npy` [1315]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1315 or target_col == 1315). Every well: [[UBA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
