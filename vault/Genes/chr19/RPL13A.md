---
symbol: "RPL13A"
type: "gene"
col: 6629
ensembl_id: "ENSG00000142541"
name: "ribosomal protein L13a"
location: "19q13.33"
module: 43
arm: "+"
pooled_cpm: 267.24
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL13A

*ribosomal protein L13a* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.70× (z +6.7, q 9e-09, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +6.4, q 4e-08, up in 41 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (NCI-H2347 3.19×, AsPC-1 2.70×, SW1417 2.48×, J82 2.45×, …); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (COLO 205 5.52×, LoVo 3.86×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 3.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.511× (z -7.1, q 1e-09, down in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (SNU-1 0.248×, C-33 A 0.309×, NCI-H2030 0.312×, AN3 CA 0.326×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL12]] (+0.91, fdr 7e-06), [[RPL26]] (+0.91, fdr 7e-06), [[RPL17]] (+0.90, fdr 7e-06); moves opposite to [[SLC35A4]] (-0.70, fdr 7e-06), [[MIS12]] (-0.64, fdr 9e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6629.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (NCI-H2347 3.19×, AsPC-1 2.70×, SW1417 2.48×, J82 2.45×, …); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (COLO 205 5.52×, LoVo 3.86×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 3.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.70×** | +6.7 | 9e-09 | 48/49 (COLO 205, LoVo, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +6.4 | 4e-08 | 41/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.15×** | +5.8 | 9e-07 | 40/44 (LoVo, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +5.8 | 9e-07 | 46/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.94×** | +5.2 | 2e-05 | 46/48 (A-427, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +4.9 | 7e-05 | 39/45 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.1 | 0.003 | 40/50 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +4.1 | 0.003 | 6/50 (HepG2/C3A, HCT15, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.50×** | +3.2 | 0.082 | 36/48 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.51×** | +3.1 | 0.100 | 32/47 (COLO 205, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6629.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (SNU-1 0.248×, C-33 A 0.309×, NCI-H2030 0.312×, AN3 CA 0.326×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.511×** | -7.1 | 1e-09 | 43/48 (SNU-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.667× | -3.2 | 0.40 | 30/48 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6629. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 555 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 107 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +8.8) | — |
| [[A-427 (line)]] | wt | 266 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -8.9) |
| [[AN3 CA (line)]] | alt | 348 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 198 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 179 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.6) |
| [[C-33 A (line)]] | alt | 430 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.3) |
| [[CHP-212 (line)]] | wt | 217 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.1) |
| [[COLO 205 (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.52× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[J82 (line)]] | alt | 150 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 438 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.7) |
| [[LS 180 (line)]] | wt | 373 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 328 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 215 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 351 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 278 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.5) | — |
| [[RKO (line)]] | wt | 456 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -10.1) |
| [[SHP-77 (line)]] | alt | 135 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -8.7) |
| [[SNU-1 (line)]] | wt | 433 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -13.8) |
| [[SW1417 (line)]] | alt | 361 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +9.8) | — |
| [[SW480 (line)]] | alt | 309 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -8.8) |
| [[A498 (line)]] | wt | 174 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 426 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 305 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 299 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 253 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 214 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 250 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 504 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 265 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 251 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 391 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6629), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL12]] | +0.91 | +0.88 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.91 | +0.89 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL17]] | +0.90 | +0.93 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS4X]] | +0.90 | +0.85 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPS20]] | +0.89 | +0.84 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.89 | +0.85 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP1]] | +0.88 | +0.84 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.88 | +0.89 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS12]] | +0.88 | +0.80 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL7]] | +0.88 | +0.86 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL37]] ⚠ | +0.87 | +0.79 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL27A]] | +0.87 | +0.81 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A4]] | -0.70 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[MIS12]] | -0.64 | -0.57 / -0.66 | both halves | 9e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.910). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.5, -29.2); signed map (-60.5, -5.9). **Vector** length 99.9, 55.5% of its response variance represented; |z| ≥ 3 in 512 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.77 to 19); *Translation initiation complex formation* (reactome, mean cos +0.75 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.75 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +0.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.7 | +2.6 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | -0.0 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.3 | +0.5 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +2.3 | -0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.2 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.2 | +6.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -5.6 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -0.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.7 | +0.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.6 | -0.4 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L13a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,487,510-49,493,057 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L13A, uL13; previously TSTA1 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P40429](https://www.uniprot.org/uniprotkb/P40429) (Large ribosomal subunit protein uL13):

> Associated with ribosomes but is not required for canonical ribosome function and has extra-ribosomal functions. Component of the GAIT (gamma interferon-activated inhibitor of translation) complex which mediates interferon-gamma-induced transcript-selective translation inhibition in inflammation processes. Upon interferon-gamma activation and subsequent phosphorylation dissociates from the ribosome and assembles into the GAIT complex which binds to stem loop-containing GAIT elements in the …

**Summary**, from NCBI Gene [23521](https://www.ncbi.nlm.nih.gov/gene/23521):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a member of the L13P family of ribosomal proteins that is a component of the 60S subunit. The encoded protein also plays a role in the repression of inflammatory genes as a component of the IFN-gamma-activated inhibitor of translation (GAIT) complex. This …

**Accessions** — [HGNC:10304](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10304) · Entrez [23521](https://www.ncbi.nlm.nih.gov/gene/23521) · UniProt [P40429](https://www.uniprot.org/uniprotkb/P40429) · Ensembl [ENSG00000142541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142541)

## Data

Gene col 6629: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6629); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6629, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6629]; `tensor/DDL_lfc|DDL_z.npy` [6629]; `embed/gene_vectors.npy` [6629]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6629 or target_col == 6629). Every well: [[RPL13A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL13A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
