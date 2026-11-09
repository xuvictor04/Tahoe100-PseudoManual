---
symbol: "VPS72"
type: "gene"
col: 8646
ensembl_id: "ENSG00000163159"
name: "vacuolar protein sorting 72 homolog"
location: "1q21.3"
module: 16
arm: "+"
pooled_cpm: 17.4
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# VPS72

*vacuolar protein sorting 72 homolog* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.14× (z +9.1, q 6e-17, up in 9 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.52× (z +8.1, q 1e-13, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.545× (z -11.3, q 8e-27, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF780A]] (+0.77, fdr 7e-06), [[ZNF480]] (+0.74, fdr 7e-06), [[MRPL58]] (+0.73, fdr 7e-06); moves opposite to [[MBOAT7]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8646.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +9.1 | 6e-17 | 9/48 (NCI-H23, SW 900, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +8.1 | 1e-13 | 26/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +8.0 | 3e-13 | 28/46 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +7.5 | 1e-11 | 25/46 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +6.8 | 1e-09 | 20/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +6.3 | 3e-08 | 20/41 (SK-MEL-2, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +6.0 | 2e-07 | 21/48 (KATO III, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.25×** | +5.9 | 2e-07 | 23/47 (NCI-H1573, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~16% of this change | **1.27×** | +4.6 | 2e-04 | 16/43 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.5 | 5e-04 | 10/29 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 0.001 | 14/44 (HEC-1-A, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.029 | 13/43 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.035 | 12/46 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.044 | 3/45 (NCI-H460, J82, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.2 | 0.044 | 6/47 (HOP62, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8646.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.545×** | -11.3 | 8e-27 | 33/46 (SW 900, SW480, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -10.8 | 1e-24 | 34/46 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.715×** | -6.5 | 2e-08 | 22/48 (NCI-H460, SW480, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.728×** | -6.2 | 1e-07 | 23/48 (NCI-H23, NCI-H460, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.751×** | -5.6 | 3e-06 | 19/48 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.864× | -3.8 | 0.014 | 17/48 (A498, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.839× | -3.4 | 0.054 | 13/47 (SW480, HT-29, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.728×** | -3.2 | 0.093 | 6/45 (SHP-77, HS-578T, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8646. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 17.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -9.5) |
| [[H4 (line)]] | wt | 13.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0969× (z -9.7) |
| [[HCT15 (line)]] | alt | 22.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.136× (z -10.4) |
| [[LoVo (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -11.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 17.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 22.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -11.5) |
| [[SHP-77 (line)]] | alt | 31.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -9.9) |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0885× (z -9.8) |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0952× (z -12.7) ⚠ toxic |
| [[SW 900 (line)]] | alt | 18.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -13.2) |
| [[SW480 (line)]] | alt | 17.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -10.1) |
| [[A-172 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8646), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF780A]] | +0.77 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ZNF480]] | +0.74 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[MRPL58]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[ZNF502]] | +0.71 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[ZNF260]] | +0.71 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[MTPAP]] | +0.70 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[COPS5]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[PYM1]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[ZNF510]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ZNF317]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[ZNF606]] | +0.68 | +0.58 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT7]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.7, 10.3); signed map (2.3, -27.0). **Vector** length 69.5, 11.3% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.9 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +8.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.1 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -10.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -11.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.4 | -5.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -1.3 | +0.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | vacuolar protein sorting 72 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,176,304-151,195,321 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YL-1, YL1, Swc2; previously TCFL1 |
| Gene groups (HGNC) | SRCAP complex subunits; Tip60/Nua4 histone acetyltransferase complex subunits |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15906](https://www.uniprot.org/uniprotkb/Q15906) (Vacuolar protein sorting-associated protein 72 homolog):

> Deposition-and-exchange histone chaperone specific for H2AZ1, specifically chaperones H2AZ1 and deposits it into nucleosomes. As component of the SRCAP complex, mediates the ATP-dependent exchange of histone H2AZ1/H2B dimers for nucleosomal H2A/H2B, leading to transcriptional regulation of selected genes by chromatin remodeling.

**Summary**, from NCBI Gene [6944](https://www.ncbi.nlm.nih.gov/gene/6944):

> The protein encoded by this gene is a shared subunit of two multi-component complexes, the histone acetyltransferase complex TRRAP/TIP60 as well as the chromatin remodeling SRCAP-containing complex. The TRRAP/TIP60 complex acetylates nucleosomal histones important for transcriptional regulation, double strand DNA break repair and apoptosis. The SRCAP-containing complex catalyzes the exchange of histone H2A with the histone variant Htz1 (H2AFZ) into nucleosomes. This protein may be responsible …

**Accessions** — [HGNC:11644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11644) · Entrez [6944](https://www.ncbi.nlm.nih.gov/gene/6944) · UniProt [Q15906](https://www.uniprot.org/uniprotkb/Q15906) · Ensembl [ENSG00000163159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163159)

## Data

Gene col 8646: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8646); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8646, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8646]; `tensor/DDL_lfc|DDL_z.npy` [8646]; `embed/gene_vectors.npy` [8646]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8646 or target_col == 8646). Every well: [[VPS72 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS72.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
