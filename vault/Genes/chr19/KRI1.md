---
symbol: "KRI1"
type: "gene"
col: 4966
ensembl_id: "ENSG00000129347"
name: "KRI1 homolog"
location: "19p13.2"
module: 11
arm: "+"
pooled_cpm: 21.94
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# KRI1

*KRI1 homolog* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.95× (z +9.5, q 2e-18, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.606× (z -9.6, q 5e-19, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTRES1]] (+0.71, fdr 1e-05), [[SURF6]] (+0.71, fdr 7e-06), [[CEBPZ]] (+0.68, fdr 7e-06); moves opposite to [[GHITM]] (-0.64, fdr 1e-05), [[PAPOLA]] (-0.64, fdr 1e-05), [[GNAS]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4966.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +9.5 | 2e-18 | 41/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +9.0 | 5e-17 | 36/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +8.9 | 1e-16 | 43/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +8.7 | 6e-16 | 39/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +7.7 | 2e-12 | 34/47 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +6.9 | 5e-10 | 29/47 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~14% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.1 | 7e-08 | 29/46 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.2 | 1e-05 | 24/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.30×** | +5.1 | 2e-05 | 21/47 (PANC-1, HEC-1-A, …) | all doses, flat | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 2e-05 | 27/47 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +4.9 | 6e-05 | 22/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 3e-04 | 20/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.35×** | +4.5 | 3e-04 | 21/44 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.32×** | +4.1 | 0.002 | 20/47 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.7 | 0.009 | 21/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.016 | 15/48 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.025 | 9/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.032 | 13/47 (NCI-H1792, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4966.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.606×** | -9.6 | 5e-19 | 36/47 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.633×** | -6.8 | 4e-09 | 29/47 (C32, RKO, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -4.3 | 0.004 | 20/47 (A-427, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.772×** | -3.8 | 0.020 | 9/48 (SK-MEL-2, HOP62, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.799× | -3.1 | 0.24 | 15/40 (C32, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4966. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.8 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +14.0) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.57× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 19.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.210× (z -8.8) |
| [[RKO (line)]] | wt | 36.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -11.0) |
| [[A-172 (line)]] | wt | 20.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -8.6) |
| [[A-427 (line)]] | wt | 37.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0942× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 18.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -9.2) |
| [[SW480 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.391× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4966), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTRES1]] | +0.71 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[SURF6]] | +0.71 | +0.68 / +0.79 | both halves | 7e-06 | STRING 848 |
| [[CEBPZ]] | +0.68 | +0.66 / +0.74 | both halves | 7e-06 | STRING 890 |
| [[CENPB]] | +0.66 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[ESF1]] | +0.65 | +0.63 / +0.72 | both halves | 7e-06 | STRING 920 |
| [[ZNF146]] | +0.64 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[PPP1R35]] ⚠ | +0.64 | +0.62 / +0.59 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[REXO4]] | +0.64 | +0.60 / +0.69 | both halves | 7e-06 | STRING 430 |
| [[BRIX1]] | +0.63 | +0.59 / +0.71 | both halves | 7e-06 | STRING 422 |
| [[METTL2A]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[NSUN5]] | +0.62 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[MRPL15]] | +0.62 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[NIFK]] | +0.62 | +0.63 / +0.67 | both halves | 7e-06 | STRING 842 |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GHITM]] | -0.64 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[PAPOLA]] | -0.64 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[GNAS]] | -0.62 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[PGRMC1]] | -0.59 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[PDIA3]] | -0.58 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[SELENOF]] | -0.58 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[EDEM1]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[TMED4]] | -0.56 | -0.53 / -0.70 | both halves | 1e-05 |  |
| [[CDK2AP1]] | -0.56 | -0.32 / -0.61 | both halves | 1e-04 |  |
| [[TMEM167A]] | -0.56 | -0.36 / -0.65 | both halves | 1e-04 |  |
| [[CSDE1]] | -0.56 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[AP2B1]] | -0.56 | -0.43 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.548). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-41.3, -0.5); signed map (-1.9, -20.3). **Vector** length 97.3, 23.8% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +9.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.2 | -6.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.3 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -1.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | KRI1 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,553,085-10,566,031 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12949 |
| Matched by | ensembl_id |

UniProt [Q8N9T8](https://www.uniprot.org/uniprotkb/Q8N9T8) carries no function annotation.

**Summary**, from NCBI Gene [65095](https://www.ncbi.nlm.nih.gov/gene/65095):

> This gene overlaps with the gene for cysteine endopeptidase AUT-like 4 in a head-to-tail orientation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:25769](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25769) · Entrez [65095](https://www.ncbi.nlm.nih.gov/gene/65095) · UniProt [Q8N9T8](https://www.uniprot.org/uniprotkb/Q8N9T8) · Ensembl [ENSG00000129347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129347)

## Data

Gene col 4966: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4966); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4966, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4966]; `tensor/DDL_lfc|DDL_z.npy` [4966]; `embed/gene_vectors.npy` [4966]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4966 or target_col == 4966). Every well: [[KRI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
