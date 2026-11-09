---
symbol: "POLR1H"
type: "gene"
col: 825
ensembl_id: "ENSG00000066379"
name: "RNA polymerase I subunit H"
location: "6p22.1"
module: 20
arm: "-"
pooled_cpm: 6.7
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# POLR1H

*RNA polymerase I subunit H* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.85× (z +12.1, q 7e-31, up in 36 of 41 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +7.6, q 5e-12, up in 32 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H2030 0.121×, A498 0.123×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (J82 0.107×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[8-Hydroxyquinoline (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0603×); [[Clotrimazole (drug)]] 5 µM in 1 line (Hs 766T 0.149×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0782×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TERF2IP]] (+0.73, fdr 7e-06), [[ZNF330]] (+0.70, fdr 1e-05), [[SNHG9]] (+0.69, fdr 9e-06); moves opposite to [[MAPK9]] (-0.72, fdr 7e-06), [[USP14]] (-0.67, fdr 1e-05), [[PSMD2]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 825.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.85×** | +12.1 | 7e-31 | 36/41 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.73×** | +7.9 | 9e-13 | 33/44 (PANC-1, AsPC-1, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +7.6 | 5e-12 | 32/40 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.50×** | +7.5 | 1e-11 | 34/41 (NCI-H1573, PANC-1, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.16×** | +6.3 | 4e-08 | 30/40 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.13×** | +6.2 | 7e-08 | 33/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +5.3 | 9e-06 | 23/46 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +4.8 | 1e-04 | 21/31 (NCI-H2030, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.77×** | +4.6 | 2e-04 | 18/36 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.73×** | +4.5 | 4e-04 | 21/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.63×** | +3.8 | 0.007 | 19/36 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.012 | 15/40 (SW 900, HS-578T, …) | top dose only | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 825.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H2030 0.121×, A498 0.123×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (J82 0.107×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[8-Hydroxyquinoline (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0603×); [[Clotrimazole (drug)]] 5 µM in 1 line (Hs 766T 0.149×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0782×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | 0.739× | -3.4 | 0.33 | 12/47 (A-427, HCT15, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.766× | -3.1 | 0.42 | 15/47 (SHP-77, NCI-H661, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.689× | -3.1 | 0.42 | 14/46 (hTERT-HPNE, C32, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 825. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.76 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +14.7) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1573 (line)]] | alt | 7.40 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 12.2× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A498 (line)]] | wt | 5.23 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 8.32 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.40× (z +12.2) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[HepG2_C3A (line)]] | wt | 7.87 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0782× (z -8.6) |
| [[Hs 766T (line)]] | wt | 4.88 | 0 | 1 | — | [[Clotrimazole (drug)]] 5 µM 0.149× (z -8.6) |
| [[J82 (line)]] | alt | 7.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 6.41 | 0 | 1 | — | [[8-Hydroxyquinoline (drug)]] 0.5 µM 0.0603× (z -9.0) |
| [[A-172 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 825), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2IP]] | +0.73 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[ZNF330]] | +0.70 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[SNHG9]] | +0.69 | +0.57 / +0.74 | both halves | 9e-06 |  |
| [[FBXL15]] | +0.69 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[SCAND1]] | +0.68 | +0.53 / +0.74 | both halves | 1e-05 |  |
| [[NDUFC1]] | +0.66 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[MED19]] | +0.66 | +0.57 / +0.72 | both halves | 8e-06 |  |
| [[FOXA2]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[HMGCL]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ACAP1]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[STAP2]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.64 | +0.53 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK9]] | -0.72 | -0.62 / -0.70 | both halves | 7e-06 |  |
| [[USP14]] | -0.67 | -0.51 / -0.70 | both halves | 1e-05 |  |
| [[PSMD2]] | -0.66 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.65 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[STIP1]] | -0.64 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[OPA1]] | -0.64 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[YWHAQ]] | -0.63 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[PSMD1]] | -0.63 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[UGGT1]] | -0.63 | -0.43 / -0.68 | both halves | 3e-05 |  |
| [[CCT3]] | -0.63 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[API5]] | -0.62 | -0.35 / -0.66 | both halves | 1e-04 |  |
| [[PTPN11]] | -0.62 | -0.41 / -0.70 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-38.3, -20.4); signed map (-4.9, 5.1). **Vector** length 63.5, 11.6% of its response variance represented; |z| ≥ 3 in 737 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.4 | +12.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.6 | +6.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.3 | +7.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | +0.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.2 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.1 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | +0.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase I subunit H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:30,058,899-30,064,909 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hZR14, HTEX-6, tctex-6, RPA12, A12.2; previously ZNRD1 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 9 pathways, smallest: RNA Polymerase I Transcription Termination; B-WICH complex positively regulates rRNA expression; RNA Polymerase I Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P1U0](https://www.uniprot.org/uniprotkb/Q9P1U0) (DNA-directed RNA polymerase I subunit RPA12):

> Core component of RNA polymerase I (Pol I), a DNA-dependent RNA polymerase which synthesizes ribosomal RNA precursors using the four ribonucleoside triphosphates as substrates. Can mediate Pol I proofreading of the nascent RNA transcript. Anchors into the Pol I active site to monitor transcription fidelity and cleave mis-incorporated 5'-ribonucleotides.

**Summary**, from NCBI Gene [30834](https://www.ncbi.nlm.nih.gov/gene/30834):

> This gene encodes a DNA-directed RNA polymerase I subunit. The encoded protein contains two potential zinc-binding motifs and may play a role in regulation of cell proliferation. The encoded protein may be involved in cancer and human immunodeficiency virus progression. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:13182](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13182) · Entrez [30834](https://www.ncbi.nlm.nih.gov/gene/30834) · UniProt [Q9P1U0](https://www.uniprot.org/uniprotkb/Q9P1U0) · Ensembl [ENSG00000066379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066379)

## Data

Gene col 825: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 825); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 825, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 825]; `tensor/DDL_lfc|DDL_z.npy` [825]; `embed/gene_vectors.npy` [825]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 825 or target_col == 825). Every well: [[POLR1H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR1H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
