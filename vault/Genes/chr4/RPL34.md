---
symbol: "RPL34"
type: "gene"
col: 3055
ensembl_id: "ENSG00000109475"
name: "ribosomal protein L34"
location: "4q25"
module: 43
arm: "+"
pooled_cpm: 311.0
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL34

*ribosomal protein L34* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.80× (z +5.6, q 1e-05, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.538× (z -5.5, q 2e-05, down in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C-33 A 0.317×, LS 180 0.325×, RKO 0.310×, Panc 03.27 0.379×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL35A]] (+0.97, fdr 7e-06), [[RPL26]] (+0.97, fdr 7e-06), [[RPL31]] (+0.97, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3055.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.80×** | +5.6 | 1e-05 | 48/49 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +5.1 | 8e-05 | 42/44 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.83×** | +3.8 | 0.030 | 41/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.72× | +3.1 | 0.24 | 39/45 (SNU-423, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3055.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C-33 A 0.317×, LS 180 0.325×, RKO 0.310×, Panc 03.27 0.379×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.538×** | -5.5 | 2e-05 | 43/48 (C-33 A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3055. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 342 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.7) |
| [[LS 180 (line)]] | wt | 472 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 544 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 369 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -8.9) |
| [[RKO (line)]] | wt | 371 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -9.7) |
| [[A-172 (line)]] | wt | 190 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 303 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 331 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 233 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 389 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 169 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 344 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 417 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 309 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 353 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 348 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 377 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 274 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 234 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 409 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 386 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 316 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 662 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 313 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 280 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 309 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 319 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 360 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 425 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 513 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 242 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3055), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL35A]] | +0.97 | +0.96 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.97 | +0.96 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.97 | +0.94 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.97 | +0.95 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL17]] | +0.96 | +0.93 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.96 | +0.92 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL23]] | +0.95 | +0.93 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27]] | +0.95 | +0.93 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS17]] ⚠ | +0.94 | +0.87 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS12]] | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.94 | +0.93 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP1]] | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.980). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.4, -27.6); signed map (-60.1, -4.2). **Vector** length 98.6, 63.9% of its response variance represented; |z| ≥ 3 in 374 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.82 to 19); *Translation initiation complex formation* (reactome, mean cos +0.78 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.78 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.2 | -0.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +1.7 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.5 | +1.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.5 | +0.5 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +2.4 | -0.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.9 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.8 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -0.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.7 | -0.6 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.5 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:108,620,569-108,630,412 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L34, eL34 |
| Gene groups (HGNC) | L ribosomal proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P49207](https://www.uniprot.org/uniprotkb/P49207) (Large ribosomal subunit protein eL34):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6164](https://www.ncbi.nlm.nih.gov/gene/6164):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L34E family of ribosomal proteins. It is located in the cytoplasm. This gene originally was thought to be located at 17q21, but it has been mapped to 4q. Overexpression of …

**Accessions** — [HGNC:10340](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10340) · Entrez [6164](https://www.ncbi.nlm.nih.gov/gene/6164) · UniProt [P49207](https://www.uniprot.org/uniprotkb/P49207) · Ensembl [ENSG00000109475](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109475)

## Data

Gene col 3055: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3055); `tables/drug_effects.parquet` (5 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3055, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3055]; `tensor/DDL_lfc|DDL_z.npy` [3055]; `embed/gene_vectors.npy` [3055]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3055 or target_col == 3055). Every well: [[RPL34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
