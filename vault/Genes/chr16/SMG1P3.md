---
symbol: "SMG1P3"
type: "gene"
col: 11126
ensembl_id: "ENSG00000180747"
name: "SMG1 pseudogene 3"
location: "16p12.2"
module: 12
arm: "-"
pooled_cpm: 8.02
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# SMG1P3

*SMG1 pseudogene 3* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.16× (z +6.9, q 3e-09, up in 34 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0722×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Sunitinib (drug)]] 5 µM in 1 line (HCT15 0.0503×; ⚠ toxic); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0683×); [[Simotinib (drug)]] 0.5 µM in 1 line (C32 0.0635×); [[Vilanterol (drug)]] 0.05 µM in 1 line (C-33 A 0.0561×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMG1P1]] (+0.69, fdr 7e-06), [[AHCY]] (+0.64, fdr 1e-05), [[MAT2A]] (+0.62, fdr 7e-06); moves opposite to [[MRPS18C]] (-0.68, fdr 1e-05), [[SNRPB2]] (-0.68, fdr 7e-06), [[NKAP]] (-0.67, fdr 1e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11126.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.16×** | +6.9 | 3e-09 | 34/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +6.0 | 4e-07 | 24/40 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.95×** | +6.0 | 4e-07 | 30/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.74×** | +4.7 | 3e-04 | 20/42 (PANC-1, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.5 | 7e-04 | 16/36 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.0 | 0.004 | 19/43 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +4.0 | 0.004 | 18/45 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.004 | 15/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.008 | 14/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +3.7 | 0.012 | 13/46 (Hs 766T, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +3.5 | 0.025 | 13/44 (PANC-1, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.50×** | +3.4 | 0.036 | 10/45 (AsPC-1, SW480, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.050 | 9/46 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Baicalin (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.080 | 5/47 (A498, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +3.1 | 0.082 | 4/45 (COLO 205, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11126.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0722×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Sunitinib (drug)]] 5 µM in 1 line (HCT15 0.0503×; ⚠ toxic); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0683×); [[Simotinib (drug)]] 0.5 µM in 1 line (C32 0.0635×); [[Vilanterol (drug)]] 0.05 µM in 1 line (C-33 A 0.0561×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.784× | -3.2 | 0.45 | 17/47 (Hs 766T, SNU-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.522× | -3.1 | 0.45 | 13/37 (HS-578T, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11126. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 8.93 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0561× (z -9.7) |
| [[C32 (line)]] | wt | 5.82 | 0 | 1 | — | [[Simotinib (drug)]] 0.5 µM 0.0635× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 5.46 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0683× (z -10.0) |
| [[H4 (line)]] | wt | 7.62 | 0 | 1 | — | [[Quinidine (15% dihydroquinidine) (drug)]] 0.05 µM 0.0501× (z -9.0) |
| [[HCT15 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0503× (z -10.5) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 8.47 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0754× (z -8.6) |
| [[HOP62 (line)]] | alt | 4.72 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0797× (z -9.4) |
| [[Hs 766T (line)]] | wt | 9.64 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.106× (z -9.3) |
| [[HS-578T (line)]] | alt | 5.22 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0739× (z -9.3) |
| [[LS 180 (line)]] | wt | 5.24 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0870× (z -8.8) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 9.35 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0722× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 7.76 | 0 | 1 | — | [[Belumosudil (mesylate) (drug)]] 5 µM 0.0455× (z -8.8) |
| [[A-172 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11126), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*21 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P1]] | +0.69 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[AHCY]] | +0.64 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[MAT2A]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[RPSA]] | +0.61 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[ARHGAP4]] | +0.58 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[AKT1]] | +0.57 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TOP1MT]] | +0.57 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[GLB1L2]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PRKCSH]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[COL18A1]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ABCA2]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[YWHAQ]] | +0.55 | +0.47 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*79 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS18C]] | -0.68 | -0.54 / -0.77 | both halves | 1e-05 |  |
| [[SNRPB2]] | -0.68 | -0.62 / -0.72 | both halves | 7e-06 |  |
| [[NKAP]] | -0.67 | -0.56 / -0.74 | both halves | 1e-05 |  |
| [[MRPS31]] | -0.65 | -0.52 / -0.72 | both halves | 1e-05 |  |
| [[SLC4A1AP]] | -0.65 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[TCEAL8]] | -0.65 | -0.45 / -0.71 | both halves | 3e-05 |  |
| [[EID2]] | -0.63 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[MFAP1]] | -0.63 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[TRIM23]] | -0.63 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[ZCCHC9]] | -0.63 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[SPOP]] | -0.62 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[COIL]] | -0.62 | -0.52 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-40.7, -11.3); signed map (-21.7, -44.5). **Vector** length 42.2, 4.86% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.9 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.7 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.5 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.4 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +1.3 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +0.8 | +0.7 |
|  | [[Encorafenib (drug)]] 5 µM |  | +0.7 | +1.4 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +0.7 | +1.3 |
|  | [[Posaconazole (drug)]] 5 µM |  | +0.7 | +1.0 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | +0.6 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | +0.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.1 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SMG1 pseudogene 3 |
| Locus type | pseudogene |
| Location | 16p12.2 — chr16:21,447,078-21,501,886 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49860](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49860) · Entrez [100271836](https://www.ncbi.nlm.nih.gov/gene/100271836) · Ensembl [ENSG00000180747](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180747)

## Data

Gene col 11126: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11126); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11126, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11126]; `tensor/DDL_lfc|DDL_z.npy` [11126]; `embed/gene_vectors.npy` [11126]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11126 or target_col == 11126). Every well: [[SMG1P3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMG1P3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
