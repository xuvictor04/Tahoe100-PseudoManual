---
symbol: "PPWD1"
type: "gene"
col: 3478
ensembl_id: "ENSG00000113593"
name: "peptidylprolyl isomerase domain and WD repeat containing 1"
location: "5q12.3"
module: 1
arm: "+"
pooled_cpm: 44.62
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PPWD1

*peptidylprolyl isomerase domain and WD repeat containing 1* — 5q12.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.737× (z -7.0, q 2e-09, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZCCHC4]] (+0.61, fdr 1e-05), [[NDUFS1]] (+0.61, fdr 1e-05), [[MTHFSD]] (+0.59, fdr 1e-05); moves opposite to [[CCDC85B]] (-0.57, fdr 2e-05), [[RBM38]] (-0.56, fdr 5e-05), [[KHDRBS3]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3478.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.737×** | -7.0 | 2e-09 | 43/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.675×** | -6.4 | 6e-08 | 31/48 (NCI-H23, C-33 A, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.819×** | -4.6 | 6e-04 | 24/48 (NCI-H460, LS 180, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.754×** | -4.6 | 6e-04 | 30/48 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.747×** | -4.4 | 0.001 | 27/45 (C-33 A, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.758×** | -4.3 | 0.001 | 22/41 (HT-29, J82, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.774×** | -4.2 | 0.003 | 28/48 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.801×** | -3.6 | 0.022 | 21/48 (SNU-423, LOX-IMVI, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.805×** | -3.5 | 0.027 | 20/48 (SW1417, SNU-423, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.806×** | -3.5 | 0.027 | 20/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.808×** | -3.5 | 0.027 | 23/48 (PANC-1, SW 900, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.670×** | -3.3 | 0.037 | 22/48 (C32, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.750×** | -3.3 | 0.037 | 20/48 (PANC-1, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.752×** | -3.3 | 0.040 | 19/48 (SW 1271, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.755×** | -3.3 | 0.043 | 18/48 (NCI-H23, NCI-H460, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **0.772×** | -3.0 | 0.087 | 16/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 54.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.248× (z -10.8) |
| [[HCT15 (line)]] | alt | 67.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Sonidegib (drug)]] 5 µM 0.116× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 47.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[A-427 (line)]] | wt | 52.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -13.5) ⚠ cell-cycle shift, explains ~65% of this change |
| [[A498 (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -9.8) ⚠ cell-cycle shift, explains ~12% of this change |
| [[HT-29 (line)]] | alt | 45.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[J82 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[LoVo (line)]] | wt | 60.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.400× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[LS 180 (line)]] | wt | 45.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -11.5) ⚠ cell-cycle shift, explains ~12% of this change |
| [[NCI-H23 (line)]] | alt | 45.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H460 (line)]] | wt | 43.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -11.7) ⚠ cell-cycle shift, explains ~12% of this change |
| [[PANC-1 (line)]] | alt | 51.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.367× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[SK-MEL-2 (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -8.5) ⚠ cell-cycle shift, explains ~61% of this change |
| [[SW 1271 (line)]] | alt | 70.6 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.109× (z -8.5) |
| [[SW480 (line)]] | alt | 71.6 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.180× (z -10.4) ⚠ toxic |
| [[A-172 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC4]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[NDUFS1]] | +0.61 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[MTHFSD]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[GATB]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PPP4R3B]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[GPALPP1]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[BOD1]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[QRSL1]] | +0.56 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[CPSF7]] | +0.56 | +0.34 / +0.57 | both halves | 1e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[CARD8]] | +0.56 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[MCM3AP]] | +0.55 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[CEP20]] | +0.55 | +0.38 / +0.59 | both halves | 6e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC85B]] | -0.57 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[RBM38]] | -0.56 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[KHDRBS3]] | -0.56 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[GDPD5]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[SLC17A7]] | -0.54 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[CARD19]] | -0.54 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[FYN]] | -0.54 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[CARHSP1]] | -0.53 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[RRAS]] | -0.53 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[RNF24]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[UGCG]] | -0.52 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[PRKCD]] | -0.51 | -0.54 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.344). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.1, 11.7); signed map (9.5, -31.0). **Vector** length 74.0, 14.5% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.2 | +0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +0.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +1.2 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +1.0 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.8 | -7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.5 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.8 | -3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.5 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -0.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl isomerase domain and WD repeat containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.3 — chr5:65,563,236-65,587,549 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0073 |
| Gene groups (HGNC) | WD repeat domain containing; Cyclophilin peptidylprolyl isomerases; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BP3](https://www.uniprot.org/uniprotkb/Q96BP3) (Peptidylprolyl isomerase domain and WD repeat-containing protein 1):

> PPIase that catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and may therefore assist protein folding. May be involved in pre-mRNA splicing.

**Summary**, from NCBI Gene [23398](https://www.ncbi.nlm.nih.gov/gene/23398):

> Enables peptidyl-prolyl cis-trans isomerase activity. Predicted to be involved in mRNA splicing, via spliceosome. Located in nuclear body. Part of catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28954](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28954) · Entrez [23398](https://www.ncbi.nlm.nih.gov/gene/23398) · UniProt [Q96BP3](https://www.uniprot.org/uniprotkb/Q96BP3) · Ensembl [ENSG00000113593](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113593)

## Data

Gene col 3478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3478); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3478]; `tensor/DDL_lfc|DDL_z.npy` [3478]; `embed/gene_vectors.npy` [3478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3478 or target_col == 3478). Every well: [[PPWD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPWD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
