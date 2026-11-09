---
symbol: "PRELID1"
type: "gene"
col: 9778
ensembl_id: "ENSG00000169230"
name: "PRELI domain containing 1"
location: "5q35.3"
module: 58
arm: "+"
pooled_cpm: 41.26
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# PRELID1

*PRELI domain containing 1* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.28× (z +8.6, q 7e-15, up in 45 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +4.8, q 2e-04, up in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 7.11×, KATO III 4.97×, PANC-1 4.52×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HT-29 6.76×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.311×, SK-MEL-2 0.326×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NHP2]] (+0.68, fdr 7e-06), [[C19orf53]] (+0.66, fdr 7e-06), [[SNRPD2]] (+0.66, fdr 7e-06); moves opposite to [[ACIN1]] (-0.64, fdr 1e-05), [[USP16]] (-0.62, fdr 1e-05), [[SRRM2]] (-0.58, fdr 5e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9778.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 7.11×, KATO III 4.97×, PANC-1 4.52×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HT-29 6.76×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **4.28×** | +8.6 | 7e-15 | 45/45 (HT-29, SW480, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **3.52×** | +8.3 | 2e-14 | 38/39 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.60×** | +6.3 | 6e-08 | 37/42 (HOP62, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +5.6 | 4e-06 | 40/46 (MIA PaCa-2, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.8 | 2e-04 | 36/48 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.86×** | +4.4 | 9e-04 | 38/47 (NCI-H460, NCI-H1573, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.85×** | +4.4 | 9e-04 | 37/46 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.69×** | +3.7 | 0.013 | 36/48 (COLO 205, NCI-H1573, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.66×** | +3.4 | 0.048 | 28/48 (HEC-1-A, SNU-423, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **1.64×** | +3.3 | 0.057 | 29/47 (NCI-H1792, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9778.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.311×, SK-MEL-2 0.326×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.725× | -3.3 | 0.65 | 33/48 (NCI-H2030, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9778. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 29.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.76× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[KATO III (line)]] | alt | 39.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H2030 (line)]] | alt | 55.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 30.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.11× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[PANC-1 (line)]] | alt | 51.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 70.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.1) |
| [[A-172 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 73.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9778), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHP2]] | +0.68 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[C19orf53]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SNRPD2]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PRDX4]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[CENPX]] | +0.65 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[CHCHD2]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 | pathway: Mitochondrial protein degradation |
| [[TUFM]] | +0.64 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[TRAPPC1]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[NDUFS8]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[DEXI]] | +0.62 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[GUK1]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[RPS15]] ⚠ | +0.59 | +0.53 / +0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS21]] | +0.59 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACIN1]] | -0.64 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[USP16]] | -0.62 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[SRRM2]] | -0.58 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[LARP7]] | -0.58 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[KCNMB3]] | -0.57 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[SREK1]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[FNBP1P1]] | -0.55 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ZNF219]] | -0.54 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[OCIAD1]] | -0.54 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[COQ7]] | -0.54 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[BCLAF1]] | -0.54 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[USP40]] | -0.54 | -0.43 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-50.6, -20.2); signed map (-38.3, 7.3). **Vector** length 56.8, 18.2% of its response variance represented; |z| ≥ 3 in 492 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.7 | +2.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +1.6 | +3.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[Fusidic acid (drug)]] 5 µM |  | +1.1 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -2.7 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | +0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | PRELI domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,303,799-177,306,949 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-106, PX19, PRELI |
| Gene groups (HGNC) | PRELI domain containing |
| Reactome | 4 pathways, smallest: TP53 Regulates Transcription of Genes Involved in Cytochrome C Release; TP53 Regulates Transcription of Cell Death Genes; Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y255](https://www.uniprot.org/uniprotkb/Q9Y255) (PRELI domain-containing protein 1, mitochondrial):

> Involved in the modulation of the mitochondrial apoptotic pathway by ensuring the accumulation of cardiolipin (CL) in mitochondrial membranes. In vitro, the TRIAP1:PRELID1 complex mediates the transfer of phosphatidic acid (PA) between liposomes and probably functions as a PA transporter across the mitochondrion intermembrane space to provide PA for CL synthesis in the inner membrane. Regulates the mitochondrial apoptotic pathway in primary Th cells. Regulates Th cell differentiation by …

**Summary**, from NCBI Gene [27166](https://www.ncbi.nlm.nih.gov/gene/27166):

> This gene encodes a member of the late embryogenesis abundant motif-containing protein family. The encoded protein is localized to mitochondria and may function as a cytoprotectant by regulating cell death and differentiation. Alternative splicing results in multiple transcript variants encoding different isoforms. Several related pseudogenes have been identified. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:30255](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30255) · Entrez [27166](https://www.ncbi.nlm.nih.gov/gene/27166) · UniProt [Q9Y255](https://www.uniprot.org/uniprotkb/Q9Y255) · Ensembl [ENSG00000169230](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169230)

## Data

Gene col 9778: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9778); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9778, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9778]; `tensor/DDL_lfc|DDL_z.npy` [9778]; `embed/gene_vectors.npy` [9778]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9778 or target_col == 9778). Every well: [[PRELID1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRELID1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
