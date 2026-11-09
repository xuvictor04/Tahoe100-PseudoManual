---
symbol: "KAT14"
type: "gene"
col: 7374
ensembl_id: "ENSG00000149474"
name: "lysine acetyltransferase 14"
location: "20p11.23"
module: 33
arm: "+"
pooled_cpm: 13.11
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# KAT14

*lysine acetyltransferase 14* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.91× (z +6.7, q 1e-08, up in 30 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.54× (z +4.6, q 1e-03, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.296× (z -13.2, q 9e-37, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ORC5]] (+0.73, fdr 7e-06), [[MRPL15]] (+0.73, fdr 7e-06), [[ZBTB24]] (+0.72, fdr 1e-05); moves opposite to [[LASP1]] (-0.62, fdr 9e-06), [[APLP2]] (-0.60, fdr 1e-05), [[LRP10]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7374.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +6.7 | 1e-08 | 30/41 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +4.6 | 1e-03 | 28/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.022 | 20/48 (NCI-H2347, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.6 | 0.031 | 18/40 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.031 | 14/47 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Darinaparsin (drug)]] 5 µM |  | 1.22× | +3.1 | 0.17 | 13/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.33× | +3.1 | 0.17 | 10/47 (A549, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7374.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.296×** | -13.2 | 9e-37 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.406×** | -9.2 | 9e-18 | 40/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.434×** | -9.0 | 4e-17 | 36/46 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.599×** | -7.8 | 7e-13 | 30/46 (PANC-1, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.519×** | -6.7 | 2e-09 | 34/47 (BT-474, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.559×** | -6.3 | 3e-08 | 28/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.575×** | -5.6 | 1e-06 | 26/48 (PANC-1, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.614×** | -5.0 | 4e-05 | 23/47 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.520×** | -3.7 | 0.014 | 15/44 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.714×** | -3.6 | 0.016 | 15/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.749×** | -3.1 | 0.089 | 7/48 (AN3 CA, AsPC-1, …) | two highest doses |  |
| [[Cytarabine (drug)]] 5 µM |  | **0.741×** | -3.1 | 0.089 | 9/46 (NCI-H2347, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.581×** | -3.1 | 0.095 | 12/48 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.8 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0856× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -18.1) |
| [[J82 (line)]] | alt | 11.2 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0843× (z -13.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.3) |
| [[LoVo (line)]] | wt | 15.6 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.216× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 9.78 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H460 (line)]] | wt | 12.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -10.5) |
| [[SW480 (line)]] | alt | 16.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -13.2) |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.101× (z -9.0) |
| [[C32 (line)]] | wt | 7.15 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0859× (z -8.6) |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -11.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 29.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -9.1) |
| [[LS 180 (line)]] | wt | 18.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.154× (z -10.0) ⚠ toxic |
| [[RKO (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -8.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.3) |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -9.0) |
| [[A-172 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORC5]] | +0.73 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[MRPL15]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[ZBTB24]] | +0.72 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[ZNF74]] | +0.71 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[BRIX1]] | +0.71 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[FANCF]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[DDX55]] | +0.68 | +0.49 / +0.77 | both halves | 1e-05 |  |
| [[PAK1IP1]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[TMEM177]] | +0.66 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[ASB13]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[ZNF22]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[AGGF1]] | +0.65 | +0.60 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LASP1]] | -0.62 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[APLP2]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[LRP10]] | -0.56 | -0.43 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-47.1, -7.2); signed map (-2.4, -40.4). **Vector** length 65.3, 11.4% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.1 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -3.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | +2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | lysine acetyltransferase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:18,137,228-18,188,387 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CRP2BP, dJ717M23.1, PRO1194, ATAC2; previously CSRP2BP |
| Gene groups (HGNC) | Lysine acetyltransferases; ATAC complex; GCN5 related N-acetyltransferases |
| Reactome | 6 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; HATs acetylate histones; Epigenetic regulation by WDR5-containing histone modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8E8](https://www.uniprot.org/uniprotkb/Q9H8E8) (Cysteine-rich protein 2-binding protein):

> Component of the ATAC complex, a complex with histone acetyltransferase activity on histones H3 and H4. May function as a scaffold for the ATAC complex to promote ATAC complex stability. Has also weak histone acetyltransferase activity toward histone H4. Required for the normal progression through G1 and G2/M phases of the cell cycle.

**Summary**, from NCBI Gene [57325](https://www.ncbi.nlm.nih.gov/gene/57325):

> CSRP2 is a protein containing two LIM domains, which are double zinc finger motifs found in proteins of diverse function. CSRP2 and some related proteins are thought to act as protein adapters, bridging two or more proteins to form a larger protein complex. The protein encoded by this gene binds to one of the LIM domains of CSRP2 and contains an acetyltransferase domain. Although the encoded protein has been detected in the cytoplasm, it is predominantly a nuclear protein. Alternatively spliced …

**Accessions** — [HGNC:15904](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15904) · Entrez [57325](https://www.ncbi.nlm.nih.gov/gene/57325) · UniProt [Q9H8E8](https://www.uniprot.org/uniprotkb/Q9H8E8) · Ensembl [ENSG00000149474](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149474)

## Data

Gene col 7374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7374); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7374]; `tensor/DDL_lfc|DDL_z.npy` [7374]; `embed/gene_vectors.npy` [7374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7374 or target_col == 7374). Every well: [[KAT14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KAT14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
