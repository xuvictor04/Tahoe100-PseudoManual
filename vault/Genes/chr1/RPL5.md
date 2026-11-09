---
symbol: "RPL5"
type: "gene"
col: 4334
ensembl_id: "ENSG00000122406"
name: "ribosomal protein L5"
location: "1p22.1"
module: 43
arm: "+"
pooled_cpm: 321.63
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL5

*ribosomal protein L5* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.62× (z +6.9, q 3e-09, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 4.14×, COLO 205 6.82×, A549 4.54×, HT-29 3.20×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 3.41×, SNU-423 3.99×, LoVo 3.26×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.39×; ⚠ cell-cycle shift, explains ~0% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-1 0.365×, C-33 A 0.395×, RKO 0.425×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS6]] (+0.93, fdr 7e-06, ⚠ RPS6 in the vector space only through flagged drug-doses), [[RPL17]] (+0.93, fdr 7e-06), [[RPS3]] (+0.93, fdr 7e-06, ⚠ RPS3 in the vector space only through flagged drug-doses), [[RPL26]] (+0.92, fdr 7e-06), [[RPL13]] (+0.91, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4334.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 4.14×, COLO 205 6.82×, A549 4.54×, HT-29 3.20×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 3.41×, SNU-423 3.99×, LoVo 3.26×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.39×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.62×** | +6.9 | 3e-09 | 48/49 (LoVo, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.29×** | +6.4 | 4e-08 | 44/44 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +4.3 | 0.003 | 40/45 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.68×** | +4.2 | 0.004 | 45/48 (SW 900, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.71×** | +4.1 | 0.004 | 42/47 (COLO 205, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.6 | 0.029 | 39/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.55×** | +3.5 | 0.033 | 39/48 (KATO III, NCI-H460, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4334.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-1 0.365×, C-33 A 0.395×, RKO 0.425×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.749× | -3.2 | 0.65 | 44/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.766× | -3.0 | 0.75 | 28/48 (SNU-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4334. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 499 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A549 (line)]] | wt | 284 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C-33 A (line)]] | alt | 384 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.1) |
| [[COLO 205 (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.82× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 360 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 405 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 305 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[RKO (line)]] | wt | 455 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.0) |
| [[SNU-1 (line)]] | wt | 361 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.5) |
| [[SNU-423 (line)]] | alt | 364 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.99× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 296 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 250 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 368 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 307 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 221 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 208 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 380 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 401 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 439 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 329 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 377 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 324 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 275 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 518 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 433 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 446 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 402 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 358 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 481 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 366 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 580 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 417 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4334), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS6]] ⚠ | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL17]] | +0.93 | +0.91 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3]] ⚠ | +0.93 | +0.88 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL26]] | +0.92 | +0.89 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.92 | +0.87 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL37]] ⚠ | +0.91 | +0.86 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS17]] ⚠ | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL13]] | +0.91 | +0.86 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.91 | +0.86 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.91 | +0.88 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.91 | +0.84 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.90 | +0.86 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL7]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.90 | +0.86 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.89 | +0.82 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.88 | +0.83 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.87 | +0.78 / +0.88 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.932). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.1, -28.4); signed map (-60.1, -5.1). **Vector** length 85.6, 51.9% of its response variance represented; |z| ≥ 3 in 539 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.79 to 19); *Translation initiation complex formation* (reactome, mean cos +0.77 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.77 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +0.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.6 | +0.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.6 | +1.2 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.5 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.7 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -4.3 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -3.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.3 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | +2.2 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.1 | -0.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:92,832,013-92,841,924 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L5, PPP1R135, uL18 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P46777](https://www.uniprot.org/uniprotkb/P46777) (Large ribosomal subunit protein uL18):

> Component of the ribosome, a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. The small ribosomal subunit (SSU) binds messenger RNAs (mRNAs) and translates the encoded message by selecting cognate aminoacyl-transfer RNA (tRNA) molecules. The large subunit (LSU) contains the ribosomal catalytic site termed the peptidyl transferase center (PTC), which catalyzes the formation of peptide bonds, thereby polymerizing the amino acids delivered by tRNAs into a …

**Summary**, from NCBI Gene [6125](https://www.ncbi.nlm.nih.gov/gene/6125):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of four RNA species and approximately 80 structurally distinct proteins. This gene encodes a member of the L18P family of ribosomal proteins and component of the 60S subunit. The encoded protein binds 5S rRNA to form a stable complex called the 5S ribonucleoprotein particle (RNP), which is necessary for the transport of nonribosome-associated …

**Accessions** — [HGNC:10360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10360) · Entrez [6125](https://www.ncbi.nlm.nih.gov/gene/6125) · UniProt [P46777](https://www.uniprot.org/uniprotkb/P46777) · Ensembl [ENSG00000122406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122406)

## Data

Gene col 4334: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4334); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4334, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4334]; `tensor/DDL_lfc|DDL_z.npy` [4334]; `embed/gene_vectors.npy` [4334]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4334 or target_col == 4334). Every well: [[RPL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
