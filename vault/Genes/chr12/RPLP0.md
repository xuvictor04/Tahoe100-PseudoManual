---
symbol: "RPLP0"
type: "gene"
col: 1573
ensembl_id: "ENSG00000089157"
name: "ribosomal protein lateral stalk subunit P0"
location: "12q24.23"
module: 43
arm: "+"
pooled_cpm: 391.62
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPLP0

*ribosomal protein lateral stalk subunit P0* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.64× (z +7.3, q 9e-11, up in 42 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.64×; ⚠ cell-cycle shift, explains ~20% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.436× (z -10.2, q 2e-21, down in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 15 lines (SNU-1 0.187×, C-33 A 0.270×, NCI-H2030 0.299×, H4 0.279×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL27A]] (+0.92, fdr 7e-06), [[RPS5]] (+0.91, fdr 7e-06), [[RACK1]] (+0.91, fdr 7e-06); moves opposite to [[MIS12]] (-0.64, fdr 1e-05), [[SLC35A4]] (-0.63, fdr 7e-06), [[SCAF1]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1573.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.64×; ⚠ cell-cycle shift, explains ~20% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +7.3 | 9e-11 | 42/44 (SNU-423, A-172, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.47×** | +7.3 | 9e-11 | 49/49 (A-172, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +6.7 | 4e-09 | 45/45 (C-33 A, C32, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.96×** | +5.9 | 6e-07 | 47/48 (SW 900, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.7 | 0.021 | 42/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1573.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 15 lines (SNU-1 0.187×, C-33 A 0.270×, NCI-H2030 0.299×, H4 0.279×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.436×** | -10.2 | 2e-21 | 46/48 (SNU-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.580×** | -4.7 | 7e-04 | 42/48 (SNU-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1573. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 377 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -14.6) |
| [[SNU-1 (line)]] | wt | 476 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -18.1) |
| [[A-427 (line)]] | wt | 377 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.3) |
| [[AN3 CA (line)]] | alt | 449 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.0) |
| [[BT-474 (line)]] | alt | 242 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -10.9) |
| [[CHP-212 (line)]] | wt | 361 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.3) |
| [[H4 (line)]] | wt | 361 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.9) |
| [[HCT15 (line)]] | alt | 454 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 384 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 454 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -8.7) |
| [[HOP62 (line)]] | alt | 340 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.8) |
| [[HT-29 (line)]] | alt | 453 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 535 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -11.2) |
| [[LS 180 (line)]] | wt | 488 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 376 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 346 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 401 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 397 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 488 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +10.3) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[NCI-H460 (line)]] | wt | 487 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -12.3) |
| [[PANC-1 (line)]] | alt | 581 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -11.9) |
| [[RKO (line)]] | wt | 580 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.7) |
| [[SHP-77 (line)]] | alt | 211 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 235 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -9.0) |
| [[SW48 (line)]] | wt | 561 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.1) |
| [[SW480 (line)]] | alt | 371 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -11.8) |
| [[A-172 (line)]] | wt | 182 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 299 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 411 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 216 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 363 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 282 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 259 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 344 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 283 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1,026 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 386 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 347 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 372 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 342 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1573), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 18 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL27A]] | +0.92 | +0.90 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS5]] | +0.91 | +0.89 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RACK1]] | +0.91 | +0.90 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPL7]] | +0.91 | +0.86 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL39]] | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 997 |
| [[RPS20]] | +0.88 | +0.86 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL12]] | +0.88 | +0.87 / +0.85 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.88 | +0.82 / +0.87 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS25]] | +0.87 | +0.87 / +0.84 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS24]] | +0.87 | +0.88 / +0.81 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL7A]] | +0.86 | +0.86 / +0.82 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.85 | +0.83 / +0.83 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIS12]] | -0.64 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[SLC35A4]] | -0.63 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[SCAF1]] | -0.61 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[TIA1]] | -0.59 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[FAM111A]] | -0.59 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.59 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[ZNF518A]] | -0.58 | -0.60 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.845). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-46.6, -29.4); signed map (-61.3, -5.9). **Vector** length 99.8, 57.9% of its response variance represented; |z| ≥ 3 in 558 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.73 to 19); *Translation initiation complex formation* (reactome, mean cos +0.72 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.72 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | +2.8 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.8 | +0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.5 | +1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.3 | -0.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.2 | -1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.1 | -10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.3 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.8 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.7 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -1.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.5 | +1.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.5 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein lateral stalk subunit P0 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:120,196,699-120,201,235 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRLP0, P0, L10E, RPP0, LP0, uL10 |
| Gene groups (HGNC) | L ribosomal proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 42 pathways, smallest: Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling; Interleukin-12 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P05388](https://www.uniprot.org/uniprotkb/P05388) (Large ribosomal subunit protein uL10):

> Ribosomal protein P0 is the functional equivalent of E.coli protein L10.

**Summary**, from NCBI Gene [6175](https://www.ncbi.nlm.nih.gov/gene/6175):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein, which is the functional equivalent of the E. coli L10 ribosomal protein, belongs to the L10P family of ribosomal proteins. It is a neutral phosphoprotein with a C-terminal end that is …

**Accessions** — [HGNC:10371](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10371) · Entrez [6175](https://www.ncbi.nlm.nih.gov/gene/6175) · UniProt [P05388](https://www.uniprot.org/uniprotkb/P05388) · Ensembl [ENSG00000089157](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089157)

## Data

Gene col 1573: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1573); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1573, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1573]; `tensor/DDL_lfc|DDL_z.npy` [1573]; `embed/gene_vectors.npy` [1573]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1573 or target_col == 1573). Every well: [[RPLP0 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPLP0.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
