---
symbol: "MKKS"
type: "gene"
col: 4681
ensembl_id: "ENSG00000125863"
name: "MKKS centrosomal shuttling protein"
location: "20p12.2"
module: 1
arm: "+"
pooled_cpm: 23.38
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MKKS

*MKKS centrosomal shuttling protein* — 20p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.93× (z +9.4, q 4e-18, up in 38 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.44× (z +5.2, q 2e-05, up in 26 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.476×, NCI-H460 0.475×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.195×; ⚠ cell-cycle shift, explains ~71% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (LS 180 0.345×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SNU-1 0.243×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM209]] (+0.55, fdr 3e-05), [[DTWD1]] (+0.53, fdr 2e-05), [[LYPLAL1]] (+0.52, fdr 5e-05); moves opposite to [[MXD4]] (-0.46, fdr 3e-05), [[C19orf38]] (-0.46, fdr 6e-05), [[OAT]] (-0.45, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4681.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.93×** | +9.4 | 4e-18 | 38/44 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.94×** | +9.0 | 5e-17 | 28/33 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +6.7 | 4e-09 | 7/48 (KATO III, SNU-423, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +6.4 | 2e-08 | 31/45 (LOX-IMVI, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +5.2 | 2e-05 | 26/47 (SHP-77, COLO 205, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.44×** | +4.8 | 1e-04 | 21/37 (CFPAC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.34×** | +4.0 | 0.005 | 16/47 (LoVo, A549, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.31×** | +3.8 | 0.009 | 20/44 (HOP62, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.015 | 13/48 (SNU-423, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.032 | 17/48 (LoVo, SNU-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.4 | 0.036 | 18/48 (NCI-H1573, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.28×** | +3.4 | 0.036 | 19/47 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.1 | 0.091 | 12/48 (COLO 205, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.099 | 12/48 (hTERT-HPNE, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4681.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.476×, NCI-H460 0.475×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.195×; ⚠ cell-cycle shift, explains ~71% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (LS 180 0.345×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SNU-1 0.243×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.861× | -3.0 | 0.95 | 10/48 (A-427, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4681. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.64× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 46.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 18.5 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.46× (z +10.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LS 180 (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.345× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 26.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -9.6) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SNU-1 (line)]] | wt | 35.6 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.243× (z -8.5) |
| [[A-172 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4681), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM209]] | +0.55 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[DTWD1]] | +0.53 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[LYPLAL1]] | +0.52 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[MIOS]] | +0.50 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[NUP37]] | +0.49 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[LDAH]] | +0.49 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[N6AMT1]] | +0.49 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[MRPL15]] | +0.49 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[UBXN2B]] | +0.49 | +0.29 / +0.59 | both halves | 2e-04 |  |
| [[AVL9]] | +0.49 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[MRPS16]] | +0.48 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[TSEN15]] | +0.48 | +0.45 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXD4]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[C19orf38]] | -0.46 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[OAT]] | -0.45 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[C5AR1]] | -0.43 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[AVIL]] | -0.43 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[MYO7A]] | -0.43 | -0.51 / -0.25 | both halves | 4e-04 |  |
| [[OTUD5]] | -0.42 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[PBXIP1]] | -0.41 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[NXF1]] | -0.41 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[NDEL1]] | -0.41 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SHPK]] | -0.41 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[VPS9D1]] | -0.40 | -0.36 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.412). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.9, 2.8); signed map (-3.0, -38.4). **Vector** length 66.9, 12.1% of its response variance represented; |z| ≥ 3 in 680 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +3.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +6.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.9 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -2.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | +6.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.2 | +0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | MKKS centrosomal shuttling protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.2 — chr20:10,401,009-10,434,222 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously BBS6 |
| Gene groups (HGNC) | Chaperonins |
| Reactome | 5 pathways, smallest: BBSome-mediated cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPJ1](https://www.uniprot.org/uniprotkb/Q9NPJ1) (Molecular chaperone MKKS):

> Probable molecular chaperone that assists the folding of proteins upon ATP hydrolysis. Plays a role in the assembly of BBSome, a complex involved in ciliogenesis regulating transports vesicles to the cilia. May play a role in protein processing in limb, cardiac and reproductive system development. May play a role in cytokinesis.

**Summary**, from NCBI Gene [8195](https://www.ncbi.nlm.nih.gov/gene/8195):

> This gene encodes a protein which shares sequence similarity with other members of the type II chaperonin family. The encoded protein is a centrosome-shuttling protein and plays an important role in cytokinesis. This protein also interacts with other type II chaperonin members to form a complex known as the BBSome, which involves ciliary membrane biogenesis. This protein is encoded by a downstream open reading frame (dORF). Several upstream open reading frames (uORFs) have been identified, …

**Accessions** — [HGNC:7108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7108) · Entrez [8195](https://www.ncbi.nlm.nih.gov/gene/8195) · UniProt [Q9NPJ1](https://www.uniprot.org/uniprotkb/Q9NPJ1) · Ensembl [ENSG00000125863](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125863)

## Data

Gene col 4681: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4681); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4681, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4681]; `tensor/DDL_lfc|DDL_z.npy` [4681]; `embed/gene_vectors.npy` [4681]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4681 or target_col == 4681). Every well: [[MKKS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MKKS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
