---
symbol: "CZIB"
type: "gene"
col: 8506
ensembl_id: "ENSG00000162384"
name: "CXXC motif containing zinc binding protein"
location: "1p32.3"
module: 12
arm: "+"
pooled_cpm: 8.24
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CZIB

*CXXC motif containing zinc binding protein* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.57× (z +11.8, q 4e-29, up in 29 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.78× (z +3.9, q 0.007, up in 8 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 5.29×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.520× (z -8.1, q 2e-13, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDR39U1]] (+0.63, fdr 1e-05), [[KRT10-AS1]] (+0.61, fdr 1e-05), [[ZDHHC4]] (+0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8506.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 5.29×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +11.8 | 4e-29 | 29/33 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +8.1 | 1e-13 | 20/36 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +7.8 | 1e-12 | 9/14 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +5.7 | 2e-06 | 18/39 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +5.6 | 3e-06 | 13/20 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.7 | 2e-04 | 3/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.78×** | +3.9 | 0.007 | 8/37 (NCI-H1573, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.5 | 0.031 | 2/24 (PANC-1, A-427) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.032 | 6/47 (CHP-212, SNU-423, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | 1.61× | +3.1 | 0.12 | 2/39 (NCI-H2347, NCI-H2030) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8506.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.520×** | -8.1 | 2e-13 | 35/46 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.554×** | -7.4 | 5e-11 | 29/46 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.662×** | -7.3 | 6e-11 | 30/45 (A-427, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.564×** | -7.1 | 1e-10 | 26/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.578×** | -6.8 | 1e-09 | 30/47 (Panc 03.27, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.583×** | -6.7 | 2e-09 | 28/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.603×** | -6.3 | 2e-08 | 22/43 (HEC-1-A, HCT15, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.616×** | -6.1 | 1e-07 | 22/48 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.660×** | -5.2 | 1e-05 | 22/44 (HT-29, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.660×** | -5.2 | 1e-05 | 23/48 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.660×** | -5.2 | 1e-05 | 21/47 (NCI-H1792, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.654×** | -5.0 | 3e-05 | 21/44 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.720×** | -4.1 | 0.002 | 16/42 (MIA PaCa-2, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.730×** | -3.7 | 0.008 | 14/45 (RKO, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.746×** | -3.7 | 0.010 | 16/46 (HepG2/C3A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.747×** | -3.6 | 0.010 | 10/46 (SNU-423, NCI-H661, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8506. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 8.98 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 8.09 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.294× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 8.37 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -9.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 8.01 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.156× (z -11.4) |
| [[SHP-77 (line)]] | alt | 6.25 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.114× (z -8.5) |
| [[A-172 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8506), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDR39U1]] | +0.63 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[KRT10-AS1]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ZDHHC4]] | +0.60 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[PNPLA4]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[RABGGTA]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[NSMCE1]] | +0.57 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[TMEM42]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ERAL1]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[FASTK]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[MRPL40]] | +0.56 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TCEANC]] | +0.56 | +0.53 / +0.39 | both halves | 6e-05 |  |
| [[POLI]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.452). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-28.2, 17.2); signed map (6.2, -21.6). **Vector** length 42.2, 4.72% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +8.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.7 | +1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +0.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.1 | +3.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.1 | -6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.0 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -8.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.8 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -0.9 | -2.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -0.9 | -0.4 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -0.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | CXXC motif containing zinc binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:53,214,099-53,220,634 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20580; previously C1orf123 |
| Matched by | ensembl_id |

UniProt [Q9NWV4](https://www.uniprot.org/uniprotkb/Q9NWV4) carries no function annotation.

**Summary**, from NCBI Gene [54987](https://www.ncbi.nlm.nih.gov/gene/54987):

> Enables zinc ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26059) · Entrez [54987](https://www.ncbi.nlm.nih.gov/gene/54987) · UniProt [Q9NWV4](https://www.uniprot.org/uniprotkb/Q9NWV4) · Ensembl [ENSG00000162384](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162384)

## Data

Gene col 8506: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8506); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8506, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8506]; `tensor/DDL_lfc|DDL_z.npy` [8506]; `embed/gene_vectors.npy` [8506]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8506 or target_col == 8506). Every well: [[CZIB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CZIB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
