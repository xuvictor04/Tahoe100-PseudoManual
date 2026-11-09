---
symbol: "RPL11"
type: "gene"
col: 6646
ensembl_id: "ENSG00000142676"
name: "ribosomal protein L11"
location: "1p36.11"
module: 43
arm: "+"
pooled_cpm: 448.55
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

# RPL11

*ribosomal protein L11* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.23× (z +8.3, q 5e-14, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (LoVo 4.55×, COLO 205 4.72×, Panc 03.27 3.73×, A549 4.76×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (MIA PaCa-2 4.13×, A549 3.87×, NCI-H460 3.47×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.23×; ⚠ cell-cycle shift, explains ~18% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.638× (z -4.9, q 5e-04, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.451×, RKO 0.432×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL26]] (+0.95, fdr 7e-06), [[RPL13]] (+0.95, fdr 7e-06), [[RPL19]] (+0.94, fdr 7e-06); moves opposite to [[MIS12]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6646.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (LoVo 4.55×, COLO 205 4.72×, Panc 03.27 3.73×, A549 4.76×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (MIA PaCa-2 4.13×, A549 3.87×, NCI-H460 3.47×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.23×; ⚠ cell-cycle shift, explains ~18% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.23×** | +8.3 | 5e-14 | 49/49 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +7.3 | 1e-10 | 44/44 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +5.5 | 6e-06 | 44/45 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.89×** | +5.0 | 9e-05 | 47/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.59×** | +3.5 | 0.056 | 37/47 (COLO 205, SHP-77, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.51× | +3.2 | 0.11 | 42/48 (COLO 205, KATO III, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6646.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.451×, RKO 0.432×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.638×** | -4.9 | 5e-04 | 39/48 (C-33 A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6646. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 291 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 367 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +9.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 567 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +9.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 431 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 437 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 468 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 746 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -8.8) |
| [[COLO 205 (line)]] | alt | 267 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 455 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 430 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 520 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 749 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 384 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 350 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 509 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.2) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[Panc 03.27 (line)]] | alt | 406 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 596 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -8.7) |
| [[SW 900 (line)]] | alt | 347 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 194 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 443 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 476 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 408 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 237 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 511 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 266 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 380 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 503 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 892 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 488 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 425 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 375 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 394 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 573 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 522 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 479 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 379 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 472 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 485 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 460 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 519 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 367 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 344 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 351 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 574 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 412 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 332 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 605 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 473 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6646), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL26]] | +0.95 | +0.95 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.95 | +0.93 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.94 | +0.92 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.94 | +0.93 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL32]] | +0.93 | +0.90 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.93 | +0.94 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL7]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL37]] ⚠ | +0.92 | +0.87 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS20]] | +0.92 | +0.93 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL12]] | +0.92 | +0.94 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.92 | +0.93 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS5]] | +0.92 | +0.89 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS25]] | +0.92 | +0.89 / +0.90 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIS12]] | -0.65 | -0.59 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.959). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.9, -28.4); signed map (-60.7, -5.0). **Vector** length 92.9, 62.4% of its response variance represented; |z| ≥ 3 in 472 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.82 to 19); *Translation initiation complex formation* (reactome, mean cos +0.79 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.79 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.0 | +1.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +1.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.3 | +0.5 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.2 | -0.3 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.2 | +0.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.5 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.4 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -0.1 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.3 | +0.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:23,691,742-23,696,835 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L11, uL5 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62913](https://www.uniprot.org/uniprotkb/P62913) (Large ribosomal subunit protein uL5):

> Component of the ribosome, a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. The small ribosomal subunit (SSU) binds messenger RNAs (mRNAs) and translates the encoded message by selecting cognate aminoacyl-transfer RNA (tRNA) molecules. The large subunit (LSU) contains the ribosomal catalytic site termed the peptidyl transferase center (PTC), which catalyzes the formation of peptide bonds, thereby polymerizing the amino acids delivered by tRNAs into a …

**Summary**, from NCBI Gene [6135](https://www.ncbi.nlm.nih.gov/gene/6135):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L5P family of ribosomal proteins. It is located in the cytoplasm. The protein probably associates with the 5S rRNA. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:10301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10301) · Entrez [6135](https://www.ncbi.nlm.nih.gov/gene/6135) · UniProt [P62913](https://www.uniprot.org/uniprotkb/P62913) · Ensembl [ENSG00000142676](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142676)

## Data

Gene col 6646: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6646); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6646, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6646]; `tensor/DDL_lfc|DDL_z.npy` [6646]; `embed/gene_vectors.npy` [6646]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6646 or target_col == 6646). Every well: [[RPL11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
