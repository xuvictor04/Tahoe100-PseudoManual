---
symbol: "RPL31"
type: "gene"
col: 976
ensembl_id: "ENSG00000071082"
name: "ribosomal protein L31"
location: "2q11.2"
module: 43
arm: "+"
pooled_cpm: 343.53
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

# RPL31

*ribosomal protein L31* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.97× (z +7.1, q 6e-10, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.551× (z -5.5, q 2e-05, down in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RKO 0.373×, SNU-1 0.353×, C-33 A 0.378×, CHP-212 0.339×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL35A]] (+0.98, fdr 7e-06), [[RPL26]] (+0.97, fdr 7e-06), [[RPL34]] (+0.97, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 976.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.97×** | +7.1 | 6e-10 | 49/49 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +5.3 | 3e-05 | 42/44 (C-33 A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.92×** | +4.3 | 0.004 | 43/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +3.6 | 0.048 | 39/45 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.69× | +3.3 | 0.11 | 45/47 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 976.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RKO 0.373×, SNU-1 0.353×, C-33 A 0.378×, CHP-212 0.339×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.551×** | -5.5 | 2e-05 | 46/48 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.609× | -3.2 | 0.37 | 35/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 976. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 332 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -8.6) |
| [[CHP-212 (line)]] | wt | 311 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -8.6) |
| [[RKO (line)]] | wt | 359 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -8.8) |
| [[SNU-1 (line)]] | wt | 458 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -8.6) |
| [[A-172 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 302 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 329 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 345 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 333 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 378 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 308 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 464 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 416 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 256 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 223 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 390 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 302 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 205 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 600 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 444 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 381 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 448 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 425 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 317 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 507 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 408 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 401 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 382 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 373 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 441 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 373 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 976), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL35A]] | +0.98 | +0.95 / +0.98 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.97 | +0.95 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.97 | +0.94 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS17]] ⚠ | +0.97 | +0.92 / +0.98 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL23]] | +0.97 | +0.93 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.97 | +0.95 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.96 | +0.93 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS27]] | +0.96 | +0.95 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3]] ⚠ | +0.96 | +0.91 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS14]] | +0.96 | +0.93 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.96 | +0.93 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36]] | +0.95 | +0.90 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL17]] | +0.95 | +0.90 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS12]] | +0.95 | +0.90 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.977). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.4, -27.4); signed map (-60.1, -4.0). **Vector** length 94.7, 61.9% of its response variance represented; |z| ≥ 3 in 363 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.81 to 19); *Translation initiation complex formation* (reactome, mean cos +0.77 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.77 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +0.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +0.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +1.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.3 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.2 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:101,002,229-101,024,032 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L31, eL31 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62899](https://www.uniprot.org/uniprotkb/P62899) (Large ribosomal subunit protein eL31):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6160](https://www.ncbi.nlm.nih.gov/gene/6160):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L31E family of ribosomal proteins. It is located in the cytoplasm. Higher levels of expression of this gene in familial adenomatous polyps compared to matched normal …

**Accessions** — [HGNC:10334](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10334) · Entrez [6160](https://www.ncbi.nlm.nih.gov/gene/6160) · UniProt [P62899](https://www.uniprot.org/uniprotkb/P62899) · Ensembl [ENSG00000071082](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071082)

## Data

Gene col 976: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 976); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 976, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 976]; `tensor/DDL_lfc|DDL_z.npy` [976]; `embed/gene_vectors.npy` [976]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 976 or target_col == 976). Every well: [[RPL31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
