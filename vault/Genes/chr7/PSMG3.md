---
symbol: "PSMG3"
type: "gene"
col: 8100
ensembl_id: "ENSG00000157778"
name: "proteasome assembly chaperone 3"
location: "7p22.3"
module: 24
arm: "+"
pooled_cpm: 12.93
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# PSMG3

*proteasome assembly chaperone 3* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.25× (z +10.2, q 1e-21, up in 35 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.35× (z +4.1, q 0.004, up in 25 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.185×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFAB1]] (+0.57, fdr 2e-05), [[PDCD2L]] (+0.57, fdr 1e-05), [[MTLN]] (+0.54, fdr 1e-05, ⚠ MTLN in the vector space only through flagged drug-doses), [[NSUN5]] (+0.54, fdr 2e-05); moves opposite to [[YBX1]] (-0.58, fdr 6e-05), [[TMBIM6]] (-0.54, fdr 1e-05), [[M6PR]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8100.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **4.25×** | +10.2 | 1e-21 | 35/36 (SW 900, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **4.29×** | +9.9 | 2e-20 | 22/23 (SW 900, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.26×** | +7.3 | 6e-11 | 27/30 (SW 900, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.59×** | +6.4 | 2e-08 | 35/40 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.92×** | +4.4 | 0.001 | 27/46 (A-172, LS 180, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.85×** | +4.2 | 0.003 | 26/38 (NCI-H460, SW 900, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.35×** | +4.1 | 0.004 | 25/41 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **2.15×** | +3.7 | 0.018 | 23/43 (NCI-H460, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.12×** | +3.6 | 0.020 | 22/44 (NCI-H460, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +3.5 | 0.030 | 20/47 (HS-578T, SNU-423, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.63×** | +3.4 | 0.031 | 18/41 (C32, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Celecoxib (drug)]] 0.5 µM |  | **2.03×** | +3.4 | 0.035 | 21/46 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.57×** | +3.2 | 0.058 | 18/46 (SW480, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.57×** | +3.2 | 0.058 | 19/45 (NCI-H460, NCI-H1792, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.076 | 19/47 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +3.1 | 0.077 | 20/45 (HT-29, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.88×** | +3.0 | 0.085 | 19/40 (HOP62, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.185×; ⚠ cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8100. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 15.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.6× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 13.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.7× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 15.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.70× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 23.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.06× (z +9.3) ⚠ toxic; cell-cycle shift, explains ~37% of this change | — |
| [[SHP-77 (line)]] | alt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.81× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8100), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 6 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAB1]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[PDCD2L]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[MTLN]] ⚠ | +0.54 | +0.50 / +0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NSUN5]] | +0.54 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[TRMT112]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[RNF7]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[METTL5]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[NSUN5P1-1]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[TMEM70]] | +0.51 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[NSUN5P2-1]] ⚠ | +0.51 | +0.46 / +0.56 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SMNDC1]] | +0.51 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[NT5C]] | +0.51 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[DUSP12]] | +0.51 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[ANTKMT]] | +0.50 | +0.35 / +0.62 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YBX1]] | -0.58 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[TMBIM6]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[M6PR]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[TLN1]] | -0.52 | -0.37 / -0.60 | both halves | 7e-05 |  |
| [[APLP2]] | -0.49 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[CD164]] | -0.48 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[RPL4]] | -0.46 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.46 | -0.23 / -0.54 | both halves | 5e-04 |  |
| [[HCFC1]] | -0.45 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[MOB1A]] | -0.44 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[TARDBP]] | -0.44 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[AP2M1]] | -0.43 | -0.36 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.397). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-50.4, -18.3); signed map (-24.6, -18.8). **Vector** length 58.8, 12.6% of its response variance represented; |z| ≥ 3 in 545 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.6 | +3.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.5 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +2.2 | +4.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.6 | +3.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.4 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.4 | +0.1 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Decitabine (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | proteasome assembly chaperone 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:1,567,332-1,571,005 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10911, PAC3; previously C7orf48 |
| Reactome | 1 pathways, smallest: Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT73](https://www.uniprot.org/uniprotkb/Q9BT73) (Proteasome assembly chaperone 3):

> Chaperone protein which promotes assembly of the 20S proteasome. May cooperate with PSMG1-PSMG2 heterodimers to orchestrate the correct assembly of proteasomes.

**Summary**, from NCBI Gene [84262](https://www.ncbi.nlm.nih.gov/gene/84262):

> Enables molecular adaptor activity. Involved in chaperone-mediated protein complex assembly. Predicted to be located in cytosol. Predicted to be part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22420](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22420) · Entrez [84262](https://www.ncbi.nlm.nih.gov/gene/84262) · UniProt [Q9BT73](https://www.uniprot.org/uniprotkb/Q9BT73) · Ensembl [ENSG00000157778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157778)

## Data

Gene col 8100: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8100); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8100, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8100]; `tensor/DDL_lfc|DDL_z.npy` [8100]; `embed/gene_vectors.npy` [8100]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8100 or target_col == 8100). Every well: [[PSMG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
