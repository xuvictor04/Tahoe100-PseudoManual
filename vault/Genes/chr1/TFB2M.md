---
symbol: "TFB2M"
type: "gene"
col: 8589
ensembl_id: "ENSG00000162851"
name: "transcription factor B2, mitochondrial"
location: "1q44"
module: 40
arm: "+"
pooled_cpm: 30.38
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# TFB2M

*transcription factor B2, mitochondrial* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 3.91× (z +9.2, q 2e-17, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.548× (z -7.8, q 3e-12, down in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.730× (z -5.8, q 1e-06, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCAF13]] (+0.67, fdr 1e-05), [[SNU13]] (+0.67, fdr 7e-06), [[THOC3]] (+0.66, fdr 7e-06); moves opposite to [[TFE3]] (-0.56, fdr 3e-05), [[TIA1]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8589.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **3.91×** | +9.2 | 2e-17 | 38/47 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.19×** | +5.3 | 3e-05 | 32/48 (NCI-H23, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.009 | 22/48 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.020 | 20/48 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.5 | 0.042 | 19/46 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.042 | 17/48 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.042 | 19/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.093 | 21/48 (BT-474, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.093 | 17/48 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.58× | +3.1 | 0.12 | 13/33 (SW480, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8589.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.548×** | -7.8 | 3e-12 | 34/44 (A498, PANC-1, …) | two highest doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.567×** | -7.1 | 4e-10 | 28/37 (AsPC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.730×** | -5.8 | 1e-06 | 28/47 (RKO, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.639×** | -5.6 | 3e-06 | 26/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.765×** | -4.9 | 9e-05 | 23/48 (LS 180, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.721×** | -4.3 | 0.002 | 25/48 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.743×** | -3.9 | 0.009 | 20/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 5 µM |  | 0.847× | -3.1 | 0.12 | 14/48 (CHP-212, SNU-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.782× | -3.1 | 0.12 | 12/48 (NCI-H2030, SW 1088, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.793× | -3.0 | 0.12 | 19/48 (CFPAC-1, H4, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.794× | -3.0 | 0.12 | 16/47 (SW480, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 63.0 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -11.8) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.321× (z -9.9) |
| [[PANC-1 (line)]] | alt | 37.8 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.230× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 31.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0903× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.418× (z -8.8) |
| [[LS 180 (line)]] | wt | 20.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.406× (z -9.0) |
| [[RKO (line)]] | wt | 35.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -13.5) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.3) |
| [[SNU-1 (line)]] | wt | 33.3 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.193× (z -8.9) |
| [[A549 (line)]] | wt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -8.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 44.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.125× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H2030 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -9.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 23.6 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0647× (z -12.1) |
| [[SW480 (line)]] | alt | 27.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -11.6) |
| [[A-172 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF13]] | +0.67 | +0.79 / +0.54 | both halves | 1e-05 | STRING 757 |
| [[SNU13]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 | STRING 498 |
| [[THOC3]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[DUXAP10]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[USPL1]] | +0.64 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[ELP2]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[URI1]] | +0.64 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[EEF1AKMT4]] | +0.64 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[PDPR2P]] | +0.64 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[OXNAD1]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[ALG3]] | +0.63 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[NUS1]] | +0.63 | +0.70 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFE3]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[TIA1]] | -0.53 | -0.57 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (0.4, -19.1); signed map (-53.8, -1.3). **Vector** length 108, 28.4% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | +3.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +4.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.5 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +9.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.7 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.4 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.3 | -5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.7 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor B2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:246,540,561-246,566,261 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23182, FLJ22661, Hkp1 |
| Gene groups (HGNC) | 7BS N6-adenosine DNA/RNA methyltransferases; Mitochondrial transcription initiation complex subunits; DNA/RNA methyltransferases |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 4 pathways, smallest: Mitochondrial transcription; Transcriptional activation of mitochondrial biogenesis; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5Q4](https://www.uniprot.org/uniprotkb/Q9H5Q4) (Dimethyladenosine transferase 2, mitochondrial):

> S-adenosyl-L-methionine-dependent rRNA methyltransferase which may methylate two specific adjacent adenosines in the loop of a conserved hairpin near the 3'-end of 12S mitochondrial rRNA (Probable). Component of the mitochondrial transcription initiation complex, composed at least of TFB2M, TFAM and POLRMT that is required for basal transcription of mitochondrial DNA. In this complex, TFAM recruits POLRMT to a specific promoter whereas TFB2M induces structural changes in POLRMT to enable …

**Summary**, from NCBI Gene [64216](https://www.ncbi.nlm.nih.gov/gene/64216):

> Enables mitochondrial transcription factor activity. Involved in transcription initiation at mitochondrial promoter. Located in mitochondrial nucleoid. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18559](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18559) · Entrez [64216](https://www.ncbi.nlm.nih.gov/gene/64216) · UniProt [Q9H5Q4](https://www.uniprot.org/uniprotkb/Q9H5Q4) · Ensembl [ENSG00000162851](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162851)

## Data

Gene col 8589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8589); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8589]; `tensor/DDL_lfc|DDL_z.npy` [8589]; `embed/gene_vectors.npy` [8589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8589 or target_col == 8589). Every well: [[TFB2M — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFB2M.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
