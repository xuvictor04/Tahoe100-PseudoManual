---
symbol: "RPL21"
type: "gene"
col: 4315
ensembl_id: "ENSG00000122026"
name: "ribosomal protein L21"
location: "13q12.2"
module: 43
arm: "+"
pooled_cpm: 103.12
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPL21

*ribosomal protein L21* — 13q12.2

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.74× (z +7.8, q 3e-12, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (LoVo 4.94×, SHP-77 4.88×, NCI-H460 5.58×, A-172 5.07×, …; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS6]] (+0.91, fdr 7e-06, ⚠ RPS6 in the vector space only through flagged drug-doses), [[RPL5]] (+0.90, fdr 7e-06), [[RPL37]] (+0.90, fdr 7e-06, ⚠ RPL37 in the vector space only through flagged drug-doses), [[RPL34]] (+0.89, fdr 7e-06), [[RPS8]] (+0.89, fdr 7e-06); moves opposite to [[PSME3]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4315.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (LoVo 4.94×, SHP-77 4.88×, NCI-H460 5.58×, A-172 5.07×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.74×** | +7.8 | 3e-12 | 48/49 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.10×** | +6.4 | 3e-08 | 42/43 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.87×** | +3.7 | 0.041 | 41/48 (KATO III, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 2.29× | +3.3 | 0.12 | 38/45 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | 1.75× | +3.2 | 0.17 | 40/47 (COLO 205, LoVo, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.71× | +3.0 | 0.22 | 39/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4315. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 48.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 180 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 143 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 74.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 83.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 91.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 109 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 64.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 72.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 161 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 105 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 101 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 178 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 133 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4315), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS6]] ⚠ | +0.91 | +0.86 / +0.90 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL5]] | +0.90 | +0.85 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL37]] ⚠ | +0.90 | +0.84 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL34]] | +0.89 | +0.87 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.89 | +0.84 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | +0.89 | +0.85 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL37A]] ⚠ | +0.88 | +0.80 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS3]] ⚠ | +0.88 | +0.83 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL30]] ⚠ | +0.87 | +0.81 / +0.85 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL26]] | +0.87 | +0.83 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL32]] | +0.87 | +0.83 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.87 | +0.85 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS12]] | +0.87 | +0.79 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36A]] | +0.87 | +0.82 / +0.87 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPL13A]] | +0.87 | +0.85 / +0.84 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.86 | +0.83 / +0.87 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.86 | +0.84 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS15A]] | +0.86 | +0.82 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.64 | -0.53 / -0.69 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.903). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-44.9, -28.5); signed map (-59.8, -5.3). **Vector** length 68.5, 29.6% of its response variance represented; |z| ≥ 3 in 351 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.75 to 19); *Translation initiation complex formation* (reactome, mean cos +0.73 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.73 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | -0.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.2 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.0 | +0.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.2 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -0.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.0 | -0.8 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.0 | -0.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.2 — chr13:27,251,362-27,256,691 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L21, FLJ27458, MGC71252, MGC104274, MGC104275, DKFZp686C06101, eL21 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P46778](https://www.uniprot.org/uniprotkb/P46778) (Large ribosomal subunit protein eL21):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6144](https://www.ncbi.nlm.nih.gov/gene/6144):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L21E family of ribosomal proteins. It is located in the cytoplasm. As is typical for genes encoding ribosomal proteins, there are multiple processed pseudogenes of this …

**Accessions** — [HGNC:10313](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10313) · Entrez [6144](https://www.ncbi.nlm.nih.gov/gene/6144) · UniProt [P46778](https://www.uniprot.org/uniprotkb/P46778) · Ensembl [ENSG00000122026](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122026)

## Data

Gene col 4315: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4315); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4315, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4315]; `tensor/DDL_lfc|DDL_z.npy` [4315]; `embed/gene_vectors.npy` [4315]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4315 or target_col == 4315). Every well: [[RPL21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
