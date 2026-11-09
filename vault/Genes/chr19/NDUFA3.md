---
symbol: "NDUFA3"
type: "gene"
col: 10023
ensembl_id: "ENSG00000170906"
name: "NADH:ubiquinone oxidoreductase subunit A3"
location: "19q13.42"
module: 58
arm: "+"
pooled_cpm: 18.59
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# NDUFA3

*NADH:ubiquinone oxidoreductase subunit A3* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.29× (z +8.4, q 3e-14, up in 37 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 2.78× (z +3.3, q 0.086, up in 37 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 6.65×, NCI-H460 6.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 6.06×, NCI-H1792 8.22×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.535× (z -5.1, q 2e-04, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM160]] (+0.79, fdr 7e-06), [[NDUFS7]] (+0.79, fdr 7e-06), [[NDUFS8]] (+0.79, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.65, fdr 1e-05), [[ADSS2]] (-0.64, fdr 1e-05), [[ZXDB]] (-0.60, fdr 4e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10023.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 6.65×, NCI-H460 6.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 6.06×, NCI-H1792 8.22×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **4.29×** | +8.4 | 3e-14 | 37/39 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.04×** | +6.1 | 2e-07 | 23/28 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.73×** | +4.7 | 5e-04 | 31/33 (KATO III, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **2.18×** | +4.5 | 0.001 | 34/43 (SW1417, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.26×** | +4.3 | 0.002 | 36/48 (HCT15, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.09×** | +4.2 | 0.002 | 39/46 (SW480, PANC-1, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.78×** | +3.3 | 0.086 | 37/46 (SW1417, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | 2.68× | +3.2 | 0.11 | 32/44 (HEC-1-A, C-33 A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 2.59× | +3.0 | 0.15 | 29/44 (HCT15, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10023.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.535×** | -5.1 | 2e-04 | 33/47 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.542× | -3.5 | 0.11 | 27/47 (Panc 03.27, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.547× | -3.3 | 0.19 | 26/47 (C32, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10023. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1792 (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.22× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.69× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SW480 (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.65× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A-172 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10023), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 11 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM160]] | +0.79 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[NDUFS7]] | +0.79 | +0.77 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[NDUFS8]] | +0.79 | +0.73 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[DPM3]] | +0.76 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[NDUFB3]] | +0.73 | +0.54 / +0.82 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[ANAPC11]] | +0.73 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[C19orf53]] | +0.73 | +0.58 / +0.77 | both halves | 8e-06 |  |
| [[MRPL41]] ⚠ | +0.72 | +0.57 / +0.71 | both halves | 9e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ELOB]] | +0.72 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[NDUFAB1]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[UQCR11]] | +0.71 | +0.65 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 994 |
| [[TRMT112]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[MIEN1]] | +0.70 | +0.53 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.65 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[ADSS2]] | -0.64 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.60 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[EIF5]] | -0.60 | -0.58 / -0.29 | both halves | 2e-04 |  |
| [[U2AF2]] | -0.60 | -0.30 / -0.63 | both halves | 2e-04 |  |
| [[PARD6G-AS1]] | -0.59 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[EIF4G1]] | -0.58 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ZMPSTE24]] | -0.58 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[RNF6]] | -0.58 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[ZXDA]] | -0.57 | -0.45 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.0, -19.2); signed map (-37.0, 6.9). **Vector** length 63.8, 18.0% of its response variance represented; |z| ≥ 3 in 443 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cristae formation* (reactome, mean cos +0.57 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +3.9 | +4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.1 | +1.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | -0.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.5 | +3.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.0 | -0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | +0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:54,102,728-54,109,257 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B9 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O95167](https://www.uniprot.org/uniprotkb/O95167) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4696](https://www.ncbi.nlm.nih.gov/gene/4696):

> Predicted to enable NADH dehydrogenase (ubiquinone) activity. Predicted to be involved in mitochondrial electron transport, NADH to ubiquinone and proton motive force-driven mitochondrial ATP synthesis. Located in mitochondrial inner membrane. Part of respiratory chain complex I. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7686](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7686) · Entrez [4696](https://www.ncbi.nlm.nih.gov/gene/4696) · UniProt [O95167](https://www.uniprot.org/uniprotkb/O95167) · Ensembl [ENSG00000170906](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170906)

## Data

Gene col 10023: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10023); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10023, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10023]; `tensor/DDL_lfc|DDL_z.npy` [10023]; `embed/gene_vectors.npy` [10023]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10023 or target_col == 10023). Every well: [[NDUFA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
