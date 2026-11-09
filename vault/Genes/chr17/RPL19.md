---
symbol: "RPL19"
type: "gene"
col: 2930
ensembl_id: "ENSG00000108298"
name: "ribosomal protein L19"
location: "17q12"
module: 43
arm: "+"
pooled_cpm: 435.92
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL19

*ribosomal protein L19* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.25× (z +8.4, q 2e-14, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 15 lines (NCI-H1792 5.69×, SW480 4.22×, HT-29 3.87×, A549 4.94×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.615× (z -4.9, q 6e-04, down in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C-33 A 0.302×, A-427 0.328×, SNU-1 0.343×, RKO 0.393×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL26]] (+0.95, fdr 7e-06), [[RPL23]] (+0.95, fdr 7e-06), [[RPL31]] (+0.94, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2930.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 15 lines (NCI-H1792 5.69×, SW480 4.22×, HT-29 3.87×, A549 4.94×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.25×** | +8.4 | 2e-14 | 48/49 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +6.8 | 3e-09 | 43/44 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.97×** | +4.8 | 2e-04 | 46/48 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +4.7 | 4e-04 | 42/45 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.1 | 0.004 | 47/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | 1.56× | +3.1 | 0.21 | 35/47 (COLO 205, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2930.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C-33 A 0.302×, A-427 0.328×, SNU-1 0.343×, RKO 0.393×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.615×** | -4.9 | 6e-04 | 42/48 (C-33 A, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 329 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.3) |
| [[A-172 (line)]] | wt | 231 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 514 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.3) |
| [[A498 (line)]] | wt | 432 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 501 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +9.7) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 620 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -8.6) |
| [[HCT15 (line)]] | alt | 360 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 343 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +8.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 303 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 357 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 384 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 464 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 577 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 429 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +8.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 478 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 272 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 491 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 520 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 479 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.1) |
| [[SNU-1 (line)]] | wt | 460 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.0) |
| [[SNU-423 (line)]] | alt | 399 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 277 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 426 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 374 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2,532 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 218 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 653 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 306 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 518 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 302 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 338 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 492 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 840 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 333 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 391 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 453 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 440 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 336 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 369 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 429 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL26]] | +0.95 | +0.90 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.95 | +0.90 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL37]] ⚠ | +0.94 | +0.87 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL30]] ⚠ | +0.94 | +0.90 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL13]] | +0.94 | +0.92 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS17]] ⚠ | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | +0.94 | +0.89 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.94 | +0.92 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.94 | +0.88 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.93 | +0.87 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL34]] | +0.93 | +0.86 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL17]] | +0.93 | +0.90 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27]] | +0.93 | +0.88 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.93 | +0.86 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL12]] | +0.93 | +0.89 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.970). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.5, -28.1); signed map (-60.3, -4.8). **Vector** length 77.6, 52.0% of its response variance represented; |z| ≥ 3 in 449 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.81 to 19); *Translation initiation complex formation* (reactome, mean cos +0.78 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.78 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +1.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -0.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.9 | -0.3 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.9 | +0.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.9 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.2 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -0.1 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.8 | +0.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.6 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:39,200,283-39,204,840 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ27452, MGC71997, DKFZp779D216, L19, eL19 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P84098](https://www.uniprot.org/uniprotkb/P84098) (Large ribosomal subunit protein eL19):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6143](https://www.ncbi.nlm.nih.gov/gene/6143):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L19E family of ribosomal proteins. It is located in the cytoplasm. As is typical for genes encoding ribosomal proteins, there are multiple processed pseudogenes of this …

**Accessions** — [HGNC:10312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10312) · Entrez [6143](https://www.ncbi.nlm.nih.gov/gene/6143) · UniProt [P84098](https://www.uniprot.org/uniprotkb/P84098) · Ensembl [ENSG00000108298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108298)

## Data

Gene col 2930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2930); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2930]; `tensor/DDL_lfc|DDL_z.npy` [2930]; `embed/gene_vectors.npy` [2930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2930 or target_col == 2930). Every well: [[RPL19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
