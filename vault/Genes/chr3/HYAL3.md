---
symbol: "HYAL3"
type: "gene"
col: 11854
ensembl_id: "ENSG00000186792"
name: "hyaluronidase 3"
location: "3p21.31"
module: 2
arm: "+"
pooled_cpm: 2.48
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# HYAL3

*hyaluronidase 3* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.34× (z +8.1, q 4e-13, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +5.0, q 1e-04, up in 14 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.481× (z -7.3, q 2e-10, down in 19 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAA80]] (+0.58, fdr 7e-06, ⚠ same locus), [[TESK1]] (+0.57, fdr 1e-05), [[SLC35C1]] (+0.55, fdr 1e-05), [[FASN]] (+0.54, fdr 1e-05); moves opposite to [[MRPS18B]] (-0.50, fdr 5e-05), [[POLK]] (-0.47, fdr 3e-05), [[LSM14A]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11854.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +8.1 | 4e-13 | 1/1 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +5.1 | 1e-04 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.0 | 1e-04 | 14/30 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +4.4 | 0.002 | 7/43 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.57×** | +4.2 | 0.002 | 5/25 (A-427, A498, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.52×** | +4.1 | 0.003 | 16/39 (SW48, SW480, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.003 | 8/32 (SW48, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +4.1 | 0.003 | 3/16 (Hs 766T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.010 | 6/26 (A-427, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +3.5 | 0.027 | 0/4 | rises with dose | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.077 | 3/41 (LoVo, LS 180, …) | top dose only | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.56×** | +3.1 | 0.078 | 2/33 (NCI-H460, NCI-H23) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.82×** | +3.1 | 0.078 | 1/18 (LS 180) | top dose only | noisy plate (z scaled); position effect removed |
| [[Estrone sulfate (potassium) (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.078 | 8/34 (A549, J82, …) | inconsistent across doses | position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.081 | 2/34 (hTERT-HPNE, A-427) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11854.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -7.3 | 2e-10 | 19/30 (SW480, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.615×** | -4.7 | 9e-04 | 13/39 (A-172, HOP62, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.632×** | -4.6 | 9e-04 | 10/42 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.658×** | -4.2 | 0.004 | 12/38 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.666×** | -4.1 | 0.005 | 11/24 (SW480, HCT15, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.463×** | -4.0 | 0.005 | 7/34 (HS-578T, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.669×** | -4.0 | 0.005 | 13/44 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.715×** | -3.4 | 0.054 | 10/39 (HCT15, Panc 03.27, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11854. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.26 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0636× (z -9.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HEC-1-A (line)]] | alt | 5.87 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.107× (z -8.8) |
| [[SW480 (line)]] | alt | 2.34 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0890× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.949 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11854), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA80]] | +0.58 | +0.58 / +0.61 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TESK1]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SLC35C1]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[FASN]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[NLGN2]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[SBF1]] | +0.53 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PCYT2]] | +0.52 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[AKT1]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[DHCR7]] | +0.52 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ABHD17A]] | +0.51 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[NSMF]] | +0.50 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[FBRSL1]] | +0.50 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[CHPF2]] | +0.50 | +0.41 / +0.54 | both halves | 4e-05 | pathway: Chondroitin sulfate/dermatan sulfate metabolism |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS18B]] | -0.50 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[POLK]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[LSM14A]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[NIPSNAP2]] | -0.47 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ESD]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[LINC01473]] | -0.45 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[CCDC25]] | -0.45 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[ABCB7]] | -0.44 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[COIL]] | -0.44 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[CHURC1]] | -0.43 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[LARP7]] | -0.43 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[PPIG]] | -0.43 | -0.38 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.547). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-3.5, -24.7); signed map (-51.5, 28.6). **Vector** length 42.9, 4.76% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +5.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.9 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +4.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +4.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.3 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -7.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.4 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.1 | -0.9 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.0 | -0.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | hyaluronidase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,292,831-50,299,405 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LUCA-3, LUCA14, Minna14 |
| Gene groups (HGNC) | Hyaluronidases |
| Reactome | 6 pathways, smallest: Hyaluronan degradation; CS/DS degradation; Hyaluronan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O43820](https://www.uniprot.org/uniprotkb/O43820) (Hyaluronidase-3):

> Facilitates sperm penetration into the layer of cumulus cells surrounding the egg by digesting hyaluronic acid. Involved in induction of the acrosome reaction in the sperm. Involved in follicular atresia, the breakdown of immature ovarian follicles that are not selected to ovulate. Induces ovarian granulosa cell apoptosis, possibly via apoptotic signaling pathway involving CASP8 and CASP3 activation, and poly(ADP-ribose) polymerase (PARP) cleavage. Has no hyaluronidase activity in embryonic …

**Summary**, from NCBI Gene [8372](https://www.ncbi.nlm.nih.gov/gene/8372):

> This gene encodes a member of the hyaluronidase family. Hyaluronidases are endoglycosidase enzymes that degrade hyaluronan, one of the major glycosaminoglycans of the extracellular matrix. The regulated turnover of hyaluronan plays a critical role in many biological processes including cell proliferation, migration and differentiation. The encoded protein may also play an important role in sperm function. This gene is one of several related genes in a region of chromosome 3p21.3 associated with …

**Accessions** — [HGNC:5322](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5322) · Entrez [8372](https://www.ncbi.nlm.nih.gov/gene/8372) · UniProt [O43820](https://www.uniprot.org/uniprotkb/O43820) · Ensembl [ENSG00000186792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186792)

## Data

Gene col 11854: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11854); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11854, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11854]; `tensor/DDL_lfc|DDL_z.npy` [11854]; `embed/gene_vectors.npy` [11854]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11854 or target_col == 11854). Every well: [[HYAL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HYAL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
