---
symbol: "HEBP1"
type: "gene"
col: 279
ensembl_id: "ENSG00000013583"
name: "heme binding protein 1"
location: "12p13.1"
module: 54
arm: "+"
pooled_cpm: 14.9
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# HEBP1

*heme binding protein 1* — 12p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.55× (z +11.4, q 2e-27, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.608× (z -8.5, q 8e-15, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPG]] (+0.74, fdr 1e-05), [[MPST]] (+0.73, fdr 7e-06), [[TMEM65]] (+0.70, fdr 1e-05); moves opposite to [[ZC3H4]] (-0.74, fdr 1e-05), [[TASOR]] (-0.70, fdr 1e-05), [[ZNF655]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RGS10]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 279.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.55×** | +11.4 | 2e-27 | 39/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.29×** | +10.1 | 2e-21 | 40/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +9.6 | 1e-19 | 41/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +5.8 | 9e-07 | 29/45 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.7 | 1e-06 | 29/46 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +5.6 | 2e-06 | 29/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.44×** | +4.4 | 8e-04 | 16/37 (MIA PaCa-2, CFPAC-1, …) | two highest doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.40×** | +4.1 | 0.003 | 21/42 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.34×** | +3.4 | 0.042 | 14/41 (A549, NCI-H1792, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.4 | 0.043 | 12/46 (HEC-1-A, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.32×** | +3.3 | 0.050 | 13/48 (LS 180, NCI-H460, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +3.1 | 0.079 | 5/48 (HT-29, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.28× | +3.0 | 0.11 | 15/47 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 279.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.608×** | -8.5 | 8e-15 | 36/47 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.618×** | -5.8 | 1e-06 | 24/45 (Panc 03.27, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.512×** | -4.2 | 0.003 | 21/44 (Panc 03.27, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.690×** | -4.2 | 0.003 | 19/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.740×** | -3.5 | 0.050 | 18/46 (NCI-H1573, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 279. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 24.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -15.4) |
| [[A549 (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0966× (z -9.5) ⚠ transcription drop |
| [[HOP62 (line)]] | alt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.0) |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 17.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.83× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 30.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -8.5) |
| [[SNU-423 (line)]] | alt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -13.6) |
| [[A-172 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 279), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | +0.74 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[MPST]] | +0.73 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[TMEM65]] | +0.70 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[SDHAP2]] | +0.70 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[RNF149]] | +0.70 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.69 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[CAMLG]] | +0.69 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.69 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[MTM1]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ATP7B]] | +0.69 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[KLHL7]] | +0.69 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[GNB2]] | +0.69 | +0.64 / +0.51 | both halves | 1e-05 | pathway: G alpha (i) signalling events |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H4]] | -0.74 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[TASOR]] | -0.70 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.70 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[FIZ1]] | -0.70 | -0.74 / -0.39 | both halves | 6e-05 |  |
| [[SRSF6]] | -0.70 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[FKRP]] | -0.68 | -0.71 / -0.36 | both halves | 9e-05 |  |
| [[LEKR1]] | -0.68 | -0.67 / -0.37 | both halves | 7e-05 |  |
| [[ST7L]] | -0.68 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[MIS12]] | -0.68 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[CLHC1]] | -0.67 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | -0.67 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[GDAP1]] | -0.67 | -0.67 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS10]] | C | RGS10 activity raises HEBP1's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without RGS10 | 0.003 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.5, -14.9); signed map (-38.1, 2.4). **Vector** length 76.5, 15.6% of its response variance represented; |z| ≥ 3 in 724 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.4 | +10.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +11.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +5.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +9.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.1 | +5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +1.5 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.2 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | heme binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.1 — chr12:12,974,870-13,000,265 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HEBP, HBP |
| Gene groups (HGNC) | Receptor ligands |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 7 pathways, smallest: Formyl peptide receptors bind formyl peptides and many other ligands; Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRV9](https://www.uniprot.org/uniprotkb/Q9NRV9) (Heme-binding protein 1):

> May bind free porphyrinogens that may be present in the cell and thus facilitate removal of these potentially toxic compound. Binds with a high affinity to one molecule of heme or porphyrins. It binds metalloporphyrins, free porphyrins and N-methylprotoporphyrin with similar affinities.

**Summary**, from NCBI Gene [50865](https://www.ncbi.nlm.nih.gov/gene/50865):

> The full-length protein encoded by this gene is an intracellular tetrapyrrole-binding protein. This protein includes a natural chemoattractant peptide of 21 amino acids at the N-terminus, which is a natural ligand for formyl peptide receptor-like receptor 2 (FPRL2) and promotes calcium mobilization and chemotaxis in monocytes and dendritic cells. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17176) · Entrez [50865](https://www.ncbi.nlm.nih.gov/gene/50865) · UniProt [Q9NRV9](https://www.uniprot.org/uniprotkb/Q9NRV9) · Ensembl [ENSG00000013583](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013583)

## Data

Gene col 279: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 279); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 279, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 279]; `tensor/DDL_lfc|DDL_z.npy` [279]; `embed/gene_vectors.npy` [279]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 279 or target_col == 279). Every well: [[HEBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
