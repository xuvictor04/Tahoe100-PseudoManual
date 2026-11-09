---
symbol: "SMPD2"
type: "gene"
col: 5725
ensembl_id: "ENSG00000135587"
name: "sphingomyelin phosphodiesterase 2"
location: "6q21"
module: 14
arm: "+"
pooled_cpm: 2.57
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SMPD2

*sphingomyelin phosphodiesterase 2* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.20× (z +9.1, q 3e-17, up in 6 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +5.9, q 6e-07, up in 8 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.104×; ⚠ toxic); [[Verteporfin (drug)]] 0.5 µM in 1 line (BT-474 0.0669×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLCD1]] (+0.55, fdr 3e-05), [[CIART]] (+0.54, fdr 3e-05), [[THBS3]] (+0.53, fdr 5e-05); moves opposite to [[KCTD20]] (-0.50, fdr 1e-04), [[FBXL18]] (-0.48, fdr 1e-04), [[ZNF544]] (-0.47, fdr 2e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5725.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.20×** | +9.1 | 3e-17 | 6/15 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +7.4 | 4e-11 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +6.4 | 3e-08 | 1/3 (A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.9 | 6e-07 | 8/31 (NCI-H2347, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +5.1 | 4e-05 | 12/42 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.9 | 8e-05 | 6/18 (NCI-H2030, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +4.4 | 8e-04 | 5/36 (LS 180, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +4.4 | 9e-04 | 8/32 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.42×** | +4.0 | 0.003 | 3/26 (A549, Panc 03.27, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.011 | 6/36 (MIA PaCa-2, A498, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.56×** | +3.6 | 0.014 | 1/6 (NCI-H460) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.4 | 0.025 | 2/16 (NCI-H23, LoVo) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.4 | 0.025 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.027 | 1/40 (A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.065 | 2/43 (hTERT-HPNE, SHP-77) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.085 | 3/40 (KATO III, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Orlistat (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.094 | 0/25 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5725.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.104×; ⚠ toxic); [[Verteporfin (drug)]] 0.5 µM in 1 line (BT-474 0.0669×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.843× | -6.9 | 3e-09 | 25/47 (Hs 766T, NCI-H2030, …) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.745× | -3.4 | 0.12 | 3/41 (COLO 205, LOX-IMVI, …) | two highest doses |  |
| [[Rimonabant (drug)]] 5 µM |  | 0.817× | -3.3 | 0.12 | 3/43 (SW 900, C32, …) | top dose only | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.754× | -3.3 | 0.12 | 7/33 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 0.05 µM |  | 0.737× | -3.3 | 0.12 | 4/24 (HS-578T, Hs 766T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.761× | -3.2 | 0.14 | 7/43 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5725. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 3.58 | 0 | 1 | — | [[Verteporfin (drug)]] 0.5 µM 0.0669× (z -8.5) |
| [[KATO III (line)]] | alt | 5.10 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.104× (z -8.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.968 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.946 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5725), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLCD1]] | +0.55 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[CIART]] | +0.54 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[THBS3]] | +0.53 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[DDR1]] | +0.52 | +0.39 / +0.48 | both halves | 6e-05 |  |
| [[SOD2]] | +0.51 | +0.43 / +0.47 | both halves | 4e-05 |  |
| [[SETD9]] | +0.50 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[CHASERR]] | +0.50 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[GSTK1]] | +0.50 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[GALT]] | +0.49 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[SPG21]] | +0.49 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[SLC12A7]] | +0.48 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[APEX1]] | +0.48 | +0.42 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD20]] | -0.50 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[FBXL18]] | -0.48 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[ZNF544]] | -0.47 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[ARHGAP29]] | -0.46 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[UBE2V2]] | -0.45 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[UCKL1-AS1]] | -0.44 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[ARPC5L]] | -0.44 | -0.43 / -0.45 | both halves | 4e-05 |  |
| [[ARID3B]] | -0.43 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[TMED7-TICAM2]] | -0.42 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[GON4L]] | -0.42 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[CRK]] | -0.42 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[PCMT1]] | -0.41 | -0.33 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.430). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.5, 4.3); signed map (42.3, 4.4). **Vector** length 32.0, 2.71% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +4.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +0.8 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +1.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.8 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +0.8 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +0.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.8 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.8 | -0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -0.8 | +3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.8 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | sphingomyelin phosphodiesterase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:109,440,724-109,443,919 (+) |
| Ensembl biotype | protein_coding |
| Also known as | nSMase, ISC1 |
| Reactome | 9 pathways, smallest: Ceramide signalling; TNFR1-mediated ceramide production; Glycosphingolipid catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O60906](https://www.uniprot.org/uniprotkb/O60906) (Sphingomyelin phosphodiesterase 2):

> Catalyzes, at least in vitro, the hydrolysis of sphingomyelin to form ceramide and phosphocholine. Also hydrolyzes 1-O-alkyl-2-lyso-sn-glycero-3-phosphocholine (lyso-platelet-activating factor) in vivo. Also acts on 1-acyl-2-lyso-sn-glycero-3-phosphocholine (lyso-PC) and sphingosylphosphocholine.

**Summary**, from NCBI Gene [6610](https://www.ncbi.nlm.nih.gov/gene/6610):

> This gene encodes a protein which was initially identified as a sphingomyelinase based on sequence similarity between bacterial sphingomyelinases and a yeast protein. Subsequent studies showed that its biological function is less likely to be as a sphingomyelinase and instead as a lysophospholipase. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:11121](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11121) · Entrez [6610](https://www.ncbi.nlm.nih.gov/gene/6610) · UniProt [O60906](https://www.uniprot.org/uniprotkb/O60906) · Ensembl [ENSG00000135587](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135587)

## Data

Gene col 5725: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5725); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5725, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5725]; `tensor/DDL_lfc|DDL_z.npy` [5725]; `embed/gene_vectors.npy` [5725]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5725 or target_col == 5725). Every well: [[SMPD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMPD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
