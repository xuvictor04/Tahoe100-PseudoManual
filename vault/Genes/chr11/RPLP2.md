---
symbol: "RPLP2"
type: "gene"
col: 10838
ensembl_id: "ENSG00000177600"
name: "ribosomal protein lateral stalk subunit P2"
location: "11p15.5"
module: 131
arm: "+"
pooled_cpm: 355.77
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# RPLP2

*ribosomal protein lateral stalk subunit P2* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.26× (z +6.8, q 6e-09, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.530× (z -5.0, q 4e-04, down in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 0.261×, A-427 0.306×, C-33 A 0.305×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS21]] (+0.97, fdr 7e-06), [[RPS29]] (+0.96, fdr 7e-06), [[RPS25]] (+0.95, fdr 7e-06); moves opposite to [[PNPO]] (-0.74, fdr 7e-06), [[DCLRE1A]] (-0.71, fdr 7e-06).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10838.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.26×** | +6.8 | 6e-09 | 49/49 (COLO 205, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.08×** | +6.1 | 4e-07 | 44/44 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.36×** | +4.8 | 3e-04 | 48/48 (COLO 205, NCI-H460, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.47×** | +4.7 | 4e-04 | 45/45 (C-33 A, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **2.13×** | +4.3 | 0.002 | 45/48 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.8 | 0.014 | 47/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10838.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 0.261×, A-427 0.306×, C-33 A 0.305×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.530×** | -5.0 | 4e-04 | 43/48 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 379 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -9.2) |
| [[C-33 A (line)]] | alt | 326 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 256 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -9.6) |
| [[A-172 (line)]] | wt | 241 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 371 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 323 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 386 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 355 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 210 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 393 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 341 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 317 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 340 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 440 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 281 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 501 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 273 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 411 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 217 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 655 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 472 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 442 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 397 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 487 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 307 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 384 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 601 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 491 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 382 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 432 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 415 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 479 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 391 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS21]] | +0.97 | +0.94 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS29]] | +0.96 | +0.95 / +0.98 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS25]] | +0.95 | +0.91 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS10]] | +0.94 | +0.91 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 996 |
| [[RPL32]] | +0.94 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36A]] | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 995 |
| [[RPL31]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27A]] ⚠ | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL34]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL28]] | +0.93 | +0.89 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.93 | +0.89 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | +0.93 | +0.89 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.92 | +0.86 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL38]] | +0.92 | +0.87 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | -0.74 | -0.70 / -0.74 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.71 | -0.72 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.961). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-46.4, -26.9); signed map (-60.9, -3.3). **Vector** length 89.6, 62.8% of its response variance represented; |z| ≥ 3 in 453 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-2 modulates host translation machinery* (reactome, mean cos +0.90 to 12); *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.91 to 11); *Formation of the ternary complex, and subsequently, the 43S complex* (reactome, mean cos +0.91 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +2.5 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +0.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.8 | -0.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -7.7 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -7.4 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -7.0 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein lateral stalk subunit P2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:809,965-812,880 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P2, RPP2, MGC71408, LP2; previously D11S2243E |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P05387](https://www.uniprot.org/uniprotkb/P05387) (Large ribosomal subunit protein P2):

> Plays an important role in the elongation step of protein synthesis.

**Summary**, from NCBI Gene [6181](https://www.ncbi.nlm.nih.gov/gene/6181):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal phosphoprotein that is a component of the 60S subunit. The protein, which is a functional equivalent of the E. coli L7/L12 ribosomal protein, belongs to the L12P family of ribosomal proteins. It plays an important role in the elongation step of …

**Accessions** — [HGNC:10377](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10377) · Entrez [6181](https://www.ncbi.nlm.nih.gov/gene/6181) · UniProt [P05387](https://www.uniprot.org/uniprotkb/P05387) · Ensembl [ENSG00000177600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177600)

## Data

Gene col 10838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10838); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10838]; `tensor/DDL_lfc|DDL_z.npy` [10838]; `embed/gene_vectors.npy` [10838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10838 or target_col == 10838). Every well: [[RPLP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPLP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
