---
symbol: "RPL27"
type: "gene"
col: 5213
ensembl_id: "ENSG00000131469"
name: "ribosomal protein L27"
location: "17q21.31"
module: 43
arm: "+"
pooled_cpm: 172.6
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL27

*ribosomal protein L27* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.18× (z +6.9, q 3e-09, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 6.46×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.626× (z -4.4, q 0.007, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (NCI-H596 0.0668×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.328×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL13]] (+0.95, fdr 7e-06), [[RPL35]] (+0.94, fdr 7e-06, ⚠ RPL35 in the vector space only through flagged drug-doses), [[RPS17]] (+0.94, fdr 7e-06, ⚠ RPS17 in the vector space only through flagged drug-doses), [[RPL31]] (+0.93, fdr 7e-06), [[RPS14]] (+0.93, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5213.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 6.46×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.18×** | +6.9 | 3e-09 | 48/49 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.69×** | +6.3 | 1e-07 | 43/44 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **2.06×** | +4.8 | 4e-04 | 42/48 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.90×** | +4.2 | 0.003 | 45/48 (NCI-H460, COLO 205, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.07×** | +4.1 | 0.005 | 40/45 (SNU-423, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.20× | +4.0 | 0.005 | 22/50 (HCT15, HepG2/C3A, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.9 | 0.008 | 41/47 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.63×** | +3.2 | 0.096 | 42/48 (COLO 205, KATO III, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5213.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (NCI-H596 0.0668×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.328×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.626×** | -4.4 | 0.007 | 38/48 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5213. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 97.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.46× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.0668× (z -12.5) |
| [[RKO (line)]] | wt | 236 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.7) |
| [[A-172 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 213 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 210 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 166 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 164 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 84.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 269 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 203 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 216 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 156 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 208 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 228 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 248 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 246 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 206 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 206 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 161 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 235 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 180 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5213), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL13]] | +0.95 | +0.90 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35]] ⚠ | +0.94 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS17]] ⚠ | +0.94 | +0.88 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.93 | +0.87 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.93 | +0.91 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.93 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.93 | +0.88 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS10]] | +0.93 | +0.87 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.92 | +0.88 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL11]] | +0.92 | +0.85 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.92 | +0.88 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS16]] ⚠ | +0.92 | +0.87 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL17]] | +0.91 | +0.84 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.91 | +0.84 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.91 | +0.84 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP2]] | +0.90 | +0.88 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.66 | -0.55 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.919). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.8, -27.4); signed map (-60.4, -3.9). **Vector** length 79.5, 47.9% of its response variance represented; |z| ≥ 3 in 458 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.77 to 19); *Translation initiation complex formation* (reactome, mean cos +0.74 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.74 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +2.5 | +3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | -0.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.6 | +0.2 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.6 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -5.6 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -5.5 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -5.2 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | +2.1 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.7 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | +0.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:42,998,273-43,002,959 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L27, eL27 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P61353](https://www.uniprot.org/uniprotkb/P61353) (Large ribosomal subunit protein eL27):

> Component of the large ribosomal subunit. Required for proper rRNA processing and maturation of 28S and 5.8S rRNAs.

**Summary**, from NCBI Gene [6155](https://www.ncbi.nlm.nih.gov/gene/6155):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of four RNA species and approximately 80 structurally distinct proteins. This gene encodes a member of the L27e family of ribosomal proteins and a component of the 60S subunit. A splice site mutation in this gene has been identified in a Diamond-Blackfan anemia (DBA) patient. As is typical for genes encoding ribosomal proteins, there are …

**Accessions** — [HGNC:10328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10328) · Entrez [6155](https://www.ncbi.nlm.nih.gov/gene/6155) · UniProt [P61353](https://www.uniprot.org/uniprotkb/P61353) · Ensembl [ENSG00000131469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131469)

## Data

Gene col 5213: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5213); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5213, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5213]; `tensor/DDL_lfc|DDL_z.npy` [5213]; `embed/gene_vectors.npy` [5213]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5213 or target_col == 5213). Every well: [[RPL27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
