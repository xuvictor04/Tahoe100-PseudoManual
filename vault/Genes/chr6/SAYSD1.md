---
symbol: "SAYSD1"
type: "gene"
col: 3329
ensembl_id: "ENSG00000112167"
name: "SAYSVFN motif domain containing 1"
location: "6p21.2"
module: 16
arm: "+"
pooled_cpm: 4.55
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# SAYSD1

*SAYSVFN motif domain containing 1* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.19× (z +7.6, q 1e-11, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.40× (z +4.9, q 2e-04, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.403× (z -9.2, q 3e-17, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PABIR1]] (+0.73, fdr 7e-06), [[TMEM185B]] (+0.72, fdr 7e-06), [[PIGO]] (+0.72, fdr 7e-06); moves opposite to [[QPCTL]] (-0.64, fdr 7e-06), [[PMS2P4-1]] (-0.63, fdr 1e-05), [[ZNHIT1]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3329.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +7.6 | 1e-11 | 2/6 (PANC-1, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.3 | 3e-05 | 9/22 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +4.9 | 2e-04 | 12/46 (HOP62, COLO 205, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.56×** | +4.5 | 9e-04 | 12/47 (A-427, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.006 | 12/47 (KATO III, HT-29, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.007 | 10/44 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | 1.78× | +3.1 | 0.16 | 4/24 (NCI-H23, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.36× | +3.1 | 0.16 | 6/44 (HT-29, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3329.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.403×** | -9.2 | 3e-17 | 32/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.428×** | -8.5 | 4e-15 | 23/36 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.534×** | -6.3 | 5e-08 | 27/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -5.1 | 6e-05 | 17/36 (COLO 205, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.608×** | -5.0 | 7e-05 | 19/45 (LS 180, PANC-1, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.613×** | -4.9 | 9e-05 | 18/44 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.645×** | -4.4 | 9e-04 | 19/47 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.651×** | -4.3 | 0.001 | 17/46 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.443×** | -4.3 | 0.001 | 15/37 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.480×** | -3.9 | 0.006 | 10/43 (LS 180, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.680×** | -3.7 | 0.013 | 13/42 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.613×** | -3.5 | 0.021 | 9/46 (SW480, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.700×** | -3.5 | 0.021 | 14/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.724×** | -3.2 | 0.049 | 7/47 (A-427, HT-29, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -3.2 | 0.049 | 12/39 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3329. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 30.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -9.8) |
| [[KATO III (line)]] | alt | 8.93 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 3.83 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 6.62 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.212× (z -8.8) |
| [[SW1417 (line)]] | alt | 5.45 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0976× (z -9.9) |
| [[A-172 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3329), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PABIR1]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[TMEM185B]] | +0.72 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[PIGO]] | +0.72 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[N6AMT1]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[PRRC2A]] | +0.69 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[RTL6]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[CHTOP]] | +0.67 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[B3GALT9]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[C7orf25]] | +0.66 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[IRF2BP1]] | +0.64 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ACP2]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[BBS10]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QPCTL]] | -0.64 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[PMS2P4-1]] | -0.63 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[ZNHIT1]] | -0.59 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[COG7]] | -0.58 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.57 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[RABGEF1]] | -0.57 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[PRKRIP1]] | -0.56 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[RARS2]] | -0.56 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[HLA-F-AS1]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[DRD4]] | -0.55 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[GNRH1]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[SPACDR]] | -0.55 | -0.38 / -0.54 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.695). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-18.3, -2.3); signed map (0.6, -32.5). **Vector** length 47.8, 5.67% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +7.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.0 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -5.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | SAYSVFN motif domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:39,104,063-39,115,193 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11101; previously C6orf64 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPB0](https://www.uniprot.org/uniprotkb/Q9NPB0) (SAYSvFN domain-containing protein 1):

> Ufmylation 'reader' component of a translocation-associated quality control pathway, a mechanism that takes place when a ribosome has stalled during translation, and which is required to degrade clogged substrates. Specifically recognizes and binds ufmylated ribosomes when a ribosome has stalled, promoting the transport of stalled nascent chain via the TRAPP complex to lysosomes for degradation.

**Summary**, from NCBI Gene [55776](https://www.ncbi.nlm.nih.gov/gene/55776):

> Enables UFM1-modified protein reader activity. Involved in protein quality control for misfolded or incompletely synthesized proteins and rescue of stalled cytosolic ribosome. Is active in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21025](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21025) · Entrez [55776](https://www.ncbi.nlm.nih.gov/gene/55776) · UniProt [Q9NPB0](https://www.uniprot.org/uniprotkb/Q9NPB0) · Ensembl [ENSG00000112167](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112167)

## Data

Gene col 3329: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3329); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3329, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3329]; `tensor/DDL_lfc|DDL_z.npy` [3329]; `embed/gene_vectors.npy` [3329]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3329 or target_col == 3329). Every well: [[SAYSD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAYSD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
