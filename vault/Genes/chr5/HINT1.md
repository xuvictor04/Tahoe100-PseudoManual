---
symbol: "HINT1"
type: "gene"
col: 9818
ensembl_id: "ENSG00000169567"
name: "histidine triad nucleotide binding protein 1"
location: "5q23.3"
module: 131
arm: "+"
pooled_cpm: 66.69
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# HINT1

*histidine triad nucleotide binding protein 1* — 5q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.56× (z +7.6, q 2e-11, up in 40 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.75× (z +4.7, q 2e-04, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.591× (z -6.2, q 3e-07, down in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.370×, RKO 0.386×, AN3 CA 0.304×, NCI-H23 0.378×); [[Oxaprozin (drug)]] 5 µM in 1 line (NCI-H596 0.171×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NENF]] (+0.75, fdr 7e-06), [[RPLP1]] (+0.70, fdr 7e-06), [[RPS20]] (+0.70, fdr 7e-06); moves opposite to [[SLC35A4]] (-0.67, fdr 7e-06), [[PPP1R10]] (-0.62, fdr 1e-05), [[NOL6]] (-0.61, fdr 7e-06).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9818.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.56×** | +7.6 | 2e-11 | 40/42 (SW480, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.21×** | +6.5 | 3e-08 | 46/49 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +5.8 | 2e-06 | 39/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.89×** | +5.3 | 1e-05 | 46/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.0 | 5e-05 | 43/47 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.84×** | +4.9 | 8e-05 | 39/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.75×** | +4.7 | 2e-04 | 39/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.75×** | +4.7 | 2e-04 | 38/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +4.2 | 0.001 | 37/48 (RPMI-7951, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.2 | 0.002 | 33/48 (NCI-H2347, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.54×** | +3.6 | 0.014 | 32/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.032 | 28/50 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +3.1 | 0.093 | 31/48 (HEC-1-A, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9818.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.370×, RKO 0.386×, AN3 CA 0.304×, NCI-H23 0.378×); [[Oxaprozin (drug)]] 5 µM in 1 line (NCI-H596 0.171×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.591×** | -6.2 | 3e-07 | 40/48 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | 0.691× | -3.1 | 0.60 | 26/48 (HepG2/C3A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9818. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 79.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -9.6) |
| [[AN3 CA (line)]] | alt | 110 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.2) |
| [[LoVo (line)]] | wt | 77.3 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.45× (z +9.2) ⚠ toxic; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H23 (line)]] | alt | 43.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -8.9) |
| [[NCI-H596 (line)]] | alt | 70.0 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.171× (z -10.1) |
| [[RKO (line)]] | wt | 67.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -9.5) |
| [[A-172 (line)]] | wt | 88.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 80.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 75.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 104 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 86.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 56.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9818), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 12 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NENF]] | +0.75 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[RPLP1]] | +0.70 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[RPS20]] | +0.70 | +0.66 / +0.75 | both halves | 7e-06 | STRING 436 |
| [[MZT2B]] | +0.68 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[RPS24]] | +0.67 | +0.71 / +0.68 | both halves | 7e-06 | STRING 495 |
| [[RPS12]] | +0.67 | +0.54 / +0.76 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 449 |
| [[HIGD2A]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RPL13A]] | +0.66 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[RPS19]] | +0.66 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[RPL12]] | +0.66 | +0.61 / +0.76 | both halves | 7e-06 | STRING 434 |
| [[TRIM33]] | +0.66 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[MZT2A]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A4]] | -0.67 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[PPP1R10]] | -0.62 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[NOL6]] | -0.61 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[EGR1]] | -0.61 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.60 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[IER2]] | -0.60 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.60 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[CELSR3]] | -0.59 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[MIS12]] | -0.58 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[ZNF268]] | -0.58 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[ZFP41]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[ZNF548]] | -0.58 | -0.49 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-46.5, -25.5); signed map (-58.4, -5.1). **Vector** length 70.5, 26.8% of its response variance represented; |z| ≥ 3 in 614 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Termination* (reactome, mean cos +0.56 to 20); *Peptide chain elongation* (reactome, mean cos +0.58 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.58 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +4.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +0.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.8 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.8 | -0.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -3.7 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -3.6 | +7.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | +0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | histidine triad nucleotide binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.3 — chr5:131,155,383-131,224,468 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PKCI-1; previously PRKCNH1, HINT |
| Gene groups (HGNC) | Histidine triad superfamily; Cysteine endopeptidases |
| Hallmark sets | P53_PATHWAY |
| Reactome | 5 pathways, smallest: Regulation of MITF-M-dependent genes involved in apoptosis; Regulation of MITF-M-dependent genes involved in cell cycle and proliferation; Transcriptional and post-translational regulation of MITF-M expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [P49773](https://www.uniprot.org/uniprotkb/P49773) (Adenosine 5'-monophosphoramidase HINT1):

> Exhibits adenosine 5'-monophosphoramidase activity, hydrolyzing purine nucleotide phosphoramidates with a single phosphate group such as adenosine 5'monophosphoramidate (AMP-NH2) to yield AMP and NH2. Hydrolyzes adenosine 5'monophosphomorpholidate (AMP-morpholidate) and guanosine 5'monophosphomorpholidate (GMP-morpholidate). Hydrolyzes lysyl-AMP (AMP-N-epsilon-(N-alpha-acetyl lysine methyl ester)) generated by lysine tRNA ligase, as well as Met-AMP, His-AMP and Asp-AMP, lysyl-GMP …

**Summary**, from NCBI Gene [3094](https://www.ncbi.nlm.nih.gov/gene/3094):

> This gene encodes a protein that hydrolyzes purine nucleotide phosphoramidates substrates, including AMP-morpholidate, AMP-N-alanine methyl ester, AMP-alpha-acetyl lysine methyl ester, and AMP-NH2. The encoded protein interacts with these substrates via a histidine triad motif. This gene is considered a tumor suppressor gene. In addition, mutations in this gene can cause autosomal recessive neuromyotonia and axonal neuropathy. There are several related pseudogenes on chromosome 7. Several …

**Accessions** — [HGNC:4912](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4912) · Entrez [3094](https://www.ncbi.nlm.nih.gov/gene/3094) · UniProt [P49773](https://www.uniprot.org/uniprotkb/P49773) · Ensembl [ENSG00000169567](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169567)

## Data

Gene col 9818: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9818); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9818, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9818]; `tensor/DDL_lfc|DDL_z.npy` [9818]; `embed/gene_vectors.npy` [9818]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9818 or target_col == 9818). Every well: [[HINT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HINT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
