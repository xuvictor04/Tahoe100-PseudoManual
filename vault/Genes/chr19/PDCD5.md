---
symbol: "PDCD5"
type: "gene"
col: 2556
ensembl_id: "ENSG00000105185"
name: "programmed cell death 5"
location: "19q13.11"
module: 24
arm: "+"
pooled_cpm: 88.16
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# PDCD5

*programmed cell death 5* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.11× (z +8.3, q 8e-14, up in 47 of 48 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H1792 6.09×, PANC-1 4.69×, NCI-H460 4.65×, HOP62 4.05×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1792 4.93×, PANC-1 4.12×, HT-29 4.64×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.617× (z -4.9, q 7e-04, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOL7]] (+0.66, fdr 2e-05, ⚠ NOL7 in the vector space only through flagged drug-doses), [[POLR2I]] (+0.61, fdr 3e-05), [[SNHG7]] (+0.60, fdr 4e-05), [[EPB41L4A-AS1]] (+0.60, fdr 5e-05); moves opposite to [[HNRNPUL1]] (-0.62, fdr 4e-05), [[RAB1B]] (-0.61, fdr 3e-05), [[PIGT]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2556.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H1792 6.09×, PANC-1 4.69×, NCI-H460 4.65×, HOP62 4.05×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1792 4.93×, PANC-1 4.12×, HT-29 4.64×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +8.3 | 8e-14 | 47/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +6.5 | 2e-08 | 39/43 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +5.1 | 8e-05 | 38/45 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.95×** | +4.9 | 1e-04 | 44/48 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.75×** | +3.9 | 0.009 | 41/47 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.9 | 0.009 | 40/47 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.54× | +3.2 | 0.12 | 36/48 (SW 900, C32, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.51× | +3.0 | 0.17 | 36/48 (BT-474, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2556.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.617×** | -4.9 | 7e-04 | 34/48 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.266×** | -4.5 | 0.002 | 45/48 (RKO, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.603×** | -3.7 | 0.049 | 35/48 (A-427, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.382× | -3.3 | 0.14 | 35/49 (RKO, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.398× | -3.2 | 0.18 | 36/49 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 75.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +10.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 132 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 207 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 100 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 74.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +8.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 88.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 59.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +9.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 88.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 95.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 79.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 78.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 128 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 82.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 87.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 81.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 14 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOL7]] ⚠ | +0.66 | +0.48 / +0.69 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[POLR2I]] | +0.61 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[SNHG7]] | +0.60 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[EPB41L4A-AS1]] | +0.60 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[NSUN5P2-1]] ⚠ | +0.60 | +0.47 / +0.60 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS26]] | +0.60 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[PET117]] | +0.59 | +0.31 / +0.60 | both halves | 2e-04 |  |
| [[NDUFB9]] | +0.59 | +0.43 / +0.64 | both halves | 3e-05 | STRING 400 |
| [[GADD45GIP1]] | +0.58 | +0.36 / +0.66 | both halves | 1e-04 |  |
| [[ATP5ME]] | +0.58 | +0.32 / +0.70 | both halves | 1e-04 |  |
| [[ZC2HC1A]] | +0.58 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[MRPL21]] | +0.57 | +0.40 / +0.58 | both halves | 5e-05 | STRING 788 |
| [[CAMLG]] | +0.57 | +0.32 / +0.62 | both halves | 2e-04 |  |
| [[SNHG8]] | +0.57 | +0.41 / +0.64 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPUL1]] | -0.62 | -0.43 / -0.56 | both halves | 4e-05 |  |
| [[RAB1B]] | -0.61 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[PIGT]] | -0.60 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[NCSTN]] | -0.57 | -0.38 / -0.62 | both halves | 6e-05 |  |
| [[RAB11B]] | -0.57 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[LAMP1]] | -0.56 | -0.39 / -0.62 | both halves | 5e-05 |  |
| [[NID1]] | -0.56 | -0.24 / -0.60 | both halves | 4e-04 |  |
| [[GPAA1]] | -0.56 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[ARF1]] | -0.55 | -0.34 / -0.65 | both halves | 1e-04 |  |
| [[C2CD3]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[GANAB]] | -0.55 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[LRPAP1]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.476). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.8, -30.6); signed map (-16.9, -3.5). **Vector** length 64.6, 25.0% of its response variance represented; |z| ≥ 3 in 588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.1 | +0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.9 | +2.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.0 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.4 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +0.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | +0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | programmed cell death 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:32,581,190-32,587,453 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TFAR19, MGC9294 |
| Matched by | ensembl_id |

**Function**, from UniProt [O14737](https://www.uniprot.org/uniprotkb/O14737) (Programmed cell death protein 5):

> In response to DNA damage, associates with TP53/p53 to prevent MDM2-mediated degradation of TP53 and promote TP53-mediated signaling. Also protects KAT5/TIP60 from degradation, which further promotes TP53/p53-mediated signaling.

**Summary**, from NCBI Gene [9141](https://www.ncbi.nlm.nih.gov/gene/9141):

> This gene encodes a protein that is upregulated during apoptosis where it translocates rapidly from the cytoplasm to the nucleus. The encoded protein may be an important regulator of K(lysine) acetyltransferase 5 (a protein involved in transcription, DNA damage response and cell cycle control) by inhibiting its proteasome-dependent degradation. Pseudogenes have been identified on chromosomes 5 and 12 [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:8764](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8764) · Entrez [9141](https://www.ncbi.nlm.nih.gov/gene/9141) · UniProt [O14737](https://www.uniprot.org/uniprotkb/O14737) · Ensembl [ENSG00000105185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105185)

## Data

Gene col 2556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2556); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2556]; `tensor/DDL_lfc|DDL_z.npy` [2556]; `embed/gene_vectors.npy` [2556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2556 or target_col == 2556). Every well: [[PDCD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
