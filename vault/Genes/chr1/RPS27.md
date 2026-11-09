---
symbol: "RPS27"
type: "gene"
col: 10881
ensembl_id: "ENSG00000177954"
name: "ribosomal protein S27"
location: "1q21.3"
module: 43
arm: "+"
pooled_cpm: 224.14
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPS27

*ribosomal protein S27* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.95× (z +5.2, q 1e-04, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.577× (z -4.1, q 0.025, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL31]] (+0.96, fdr 7e-06), [[RPL35A]] (+0.96, fdr 7e-06), [[RPL23]] (+0.95, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10881.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.95×** | +5.2 | 1e-04 | 48/49 (C-33 A, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **2.07×** | +3.9 | 0.018 | 42/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.11×** | +3.9 | 0.018 | 40/44 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +3.6 | 0.040 | 45/47 (MIA PaCa-2, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10881.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.577×** | -4.1 | 0.025 | 39/48 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10881. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 258 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 225 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 180 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 173 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 255 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 177 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 203 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 181 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 216 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 132 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 189 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 209 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 420 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 224 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 287 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 398 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 318 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 254 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 234 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 230 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 164 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10881), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 24 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL31]] | +0.96 | +0.95 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.96 | +0.93 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.95 | +0.92 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS19]] | +0.95 | +0.92 / +0.97 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS12]] | +0.95 | +0.91 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL34]] | +0.95 | +0.93 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL36]] | +0.95 | +0.91 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.94 | +0.92 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPL18]] ⚠ | +0.94 | +0.89 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL9]] ⚠ | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS17]] ⚠ | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPLP1]] | +0.93 | +0.90 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.93 | +0.87 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL19]] | +0.93 | +0.88 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.951). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.0, -27.0); signed map (-59.7, -3.9). **Vector** length 92.7, 62.0% of its response variance represented; |z| ≥ 3 in 319 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.85 to 34); *MYC targets v1* (hallmark, mean cos +0.61 to 17); *oxidative phosphorylation* (hallmark, mean cos +0.67 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +0.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.5 | +1.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.3 | +0.7 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +2.2 | +0.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.9 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -6.7 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.7 | +2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:153,990,762-153,992,155 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MPS-1, MPS1, S27, eS27 |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 68 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P42677](https://www.uniprot.org/uniprotkb/P42677) (Small ribosomal subunit protein eS27):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Required for proper rRNA processing and maturation of 18S rRNAs. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in …

**Summary**, from NCBI Gene [6232](https://www.ncbi.nlm.nih.gov/gene/6232):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of four RNA species and approximately 80 structurally distinct proteins. This gene encodes a member of the S27e family of ribosomal proteins and component of the 40S subunit. The encoded protein contains a C4-type zinc finger domain that can bind to zinc and may bind to nucleic acid. Mutations in this gene have been identified in numerous …

**Accessions** — [HGNC:10416](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10416) · Entrez [6232](https://www.ncbi.nlm.nih.gov/gene/6232) · UniProt [P42677](https://www.uniprot.org/uniprotkb/P42677) · Ensembl [ENSG00000177954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177954)

## Data

Gene col 10881: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10881); `tables/drug_effects.parquet` (5 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10881, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10881]; `tensor/DDL_lfc|DDL_z.npy` [10881]; `embed/gene_vectors.npy` [10881]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10881 or target_col == 10881). Every well: [[RPS27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
