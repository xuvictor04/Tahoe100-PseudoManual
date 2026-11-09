---
symbol: "RPL7"
type: "gene"
col: 7204
ensembl_id: "ENSG00000147604"
name: "ribosomal protein L7"
location: "8q21.11"
module: 43
arm: "+"
pooled_cpm: 286.95
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL7

*ribosomal protein L7* — 8q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.93× (z +7.7, q 5e-12, up in 43 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A498 3.79×, MIA PaCa-2 4.25×, HT-29 3.24×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.67×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 4.54×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.601× (z -5.3, q 5e-05, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (RKO 0.325×, SW480 0.352×, C-33 A 0.347×, LS 180 0.366×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS4X]] (+0.93, fdr 7e-06), [[RPL11]] (+0.93, fdr 7e-06), [[RACK1]] (+0.93, fdr 7e-06); moves opposite to [[MIS12]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7204.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A498 3.79×, MIA PaCa-2 4.25×, HT-29 3.24×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.67×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 4.54×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.93×** | +7.7 | 5e-12 | 43/44 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.19×** | +7.1 | 3e-10 | 48/49 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +5.4 | 2e-05 | 44/45 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.86×** | +4.7 | 5e-04 | 44/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.1 | 0.005 | 41/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.62×** | +3.5 | 0.045 | 35/47 (COLO 205, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7204.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (RKO 0.325×, SW480 0.352×, C-33 A 0.347×, LS 180 0.366×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.601×** | -5.3 | 5e-05 | 39/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 362 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.1) |
| [[A498 (line)]] | wt | 353 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +8.7) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 287 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -10.3) |
| [[HCT15 (line)]] | alt | 314 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.3) |
| [[LoVo (line)]] | wt | 396 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 374 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 208 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 426 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 335 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.9) | — |
| [[RKO (line)]] | wt | 677 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -11.8) |
| [[SNU-1 (line)]] | wt | 301 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -8.6) |
| [[SW480 (line)]] | alt | 349 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -10.8) |
| [[A-172 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 268 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 343 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 302 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 280 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 243 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 267 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 294 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 235 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 365 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 247 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 262 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 477 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 266 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 307 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 413 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS4X]] | +0.93 | +0.93 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 997 |
| [[RPL11]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RACK1]] | +0.93 | +0.89 / +0.92 | both halves | 7e-06 | STRING 999 |
| [[RPL19]] | +0.92 | +0.88 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS20]] | +0.92 | +0.89 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP0]] | +0.91 | +0.86 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL12]] | +0.90 | +0.88 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL5]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.89 | +0.87 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL30]] ⚠ | +0.89 | +0.83 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | +0.89 | +0.86 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS5]] | +0.89 | +0.87 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIS12]] | -0.66 | -0.57 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.923). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-46.1, -29.3); signed map (-60.8, -5.8). **Vector** length 85.4, 52.6% of its response variance represented; |z| ≥ 3 in 510 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.78 to 19); *Translation initiation complex formation* (reactome, mean cos +0.76 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.76 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +2.2 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.5 | -0.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +0.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -5.5 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.0 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | +0.7 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.9 | +0.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.9 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | +2.6 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.11 — chr8:73,290,242-73,295,789 (-) |
| Ensembl biotype | protein_coding |
| Also known as | humL7-1, L7, uL30 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P18124](https://www.uniprot.org/uniprotkb/P18124) (Large ribosomal subunit protein uL30):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Binds to G-rich structures in 28S rRNA and in mRNAs. Plays a regulatory role in the translation apparatus; inhibits cell-free translation of mRNAs.

**Summary**, from NCBI Gene [6129](https://www.ncbi.nlm.nih.gov/gene/6129):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L30P family of ribosomal proteins. It contains an N-terminal basic region-leucine zipper (BZIP)-like domain and the RNP consensus submotif RNP2. In vitro the BZIP-like …

**Accessions** — [HGNC:10363](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10363) · Entrez [6129](https://www.ncbi.nlm.nih.gov/gene/6129) · UniProt [P18124](https://www.uniprot.org/uniprotkb/P18124) · Ensembl [ENSG00000147604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147604)

## Data

Gene col 7204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7204); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7204]; `tensor/DDL_lfc|DDL_z.npy` [7204]; `embed/gene_vectors.npy` [7204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7204 or target_col == 7204). Every well: [[RPL7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
